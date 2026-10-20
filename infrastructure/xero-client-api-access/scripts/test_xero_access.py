"""Synthetic-only tests; no requests to live Xero."""
import base64
import contextlib
import copy
import hashlib
import http.client
import io
import json
import tempfile
import threading
import unittest
from http.server import HTTPServer
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, urlencode, urlsplit
import xero_access as x

ID = '00000000-0000-4000-8000-000000000001'
OTHER = '00000000-0000-4000-8000-000000000002'


def example():
    return {'schema_version': 1, 'credential_namespace': 'synthetic-client',
            'redirect_uri': 'http://localhost:8769/callback', 'evidence_dir': 'evidence',
            'scopes': ['offline_access', 'accounting.settings.read'], 'excluded': [],
            'profiles': {'primary': {'app_name': 'Synthetic App', 'client_id': 'synthetic-client-id',
                         'connection_limit': 10, 'organisations': [
                             {'label': 'Synthetic', 'expected_name': 'Synthetic Company', 'tenant_id': ID}]}}}


def tokens(scopes=None):
    return {'access_token': 'synthetic-access-only', 'refresh_token': 'synthetic-refresh-only',
            'scope': ' '.join(scopes or ['offline_access', 'accounting.settings.read']), 'expires_in': 1800}


class ClientAccess(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / 'config.json'
        self.doc = example()
        self.path.write_text(json.dumps(self.doc), encoding='utf-8')
        self.patches = [patch.object(x, 'CONFIG', self.path), patch.object(x, 'PROFILE', 'primary'),
                        patch.object(x, 'NAMESPACE', 'synthetic-client'),
                        patch.dict(x.os.environ, {'LOCALAPPDATA': self.temp.name})]
        for p in self.patches:
            p.start(); self.addCleanup(p.stop)
        self.c = x.config()

    def test_client_and_profile_namespaces_are_isolated(self):
        one = x.local_dir()
        with patch.object(x, 'NAMESPACE', 'second-client'):
            two = x.local_dir()
        with patch.object(x, 'PROFILE', 'secondary'):
            three = x.local_dir()
        self.assertEqual(len({one, two, three}), 3)
        with patch.object(x, 'PROFILE', '../escape'):
            with self.assertRaises(x.AccessError): x.local_dir()

    def test_config_exclusions_duplicates_and_provider_limit(self):
        for edit in ['exclude', 'duplicate', 'capacity', 'callback']:
            d = example()
            if edit == 'exclude': d['excluded'] = [ID]
            if edit == 'duplicate': d['profiles']['primary']['organisations'] *= 2
            if edit == 'capacity': d['profiles']['primary']['connection_limit'] = 0
            if edit == 'callback': d['redirect_uri'] = 'http://external.example/callback'
            self.path.write_text(json.dumps(d), encoding='utf-8')
            with self.assertRaises(x.AccessError): x.config()

    def test_pinned_identity_and_name(self):
        rows = [{'tenantId': ID, 'tenantName': 'Synthetic Company', 'tenantType': 'ORGANISATION'}]
        self.assertEqual(len(x.match_connections(self.c, rows)), 1)
        self.assertEqual(x.match_connections(self.c, [dict(rows[0], tenantId=OTHER)]), [])
        with self.assertRaises(x.AccessError): x.match_connections(self.c, rows * 2)
        with self.assertRaises(x.AccessError): x.match_connections(self.c, [dict(rows[0], tenantName='Renamed')])
        self.c['organisations'][0]['tenant_id'] = None
        with self.assertRaises(x.AccessError): x.match_connections(self.c, rows)

    def test_encrypted_storage_and_identity_binding(self):
        x.save_tokens(tokens(), self.c)
        blob = (x.local_dir() / 'tokens.dpapi').read_bytes()
        self.assertNotIn(b'synthetic-access-only', blob)
        self.assertNotIn(b'synthetic-refresh-only', blob)
        saved = json.loads(x.protect(blob, decrypt=True))
        self.assertEqual(saved['tokens']['access_token'], 'synthetic-access-only')
        with self.assertRaises(x.AccessError): x.access_token(dict(self.c, client_id='other'))
        original = x.local_dir()
        with patch.object(x, 'local_dir', return_value=original), patch.object(x, 'NAMESPACE', 'other-client'):
            with self.assertRaises(x.AccessError): x.access_token(self.c)

    def test_scope_upgrade_requires_consent_not_refresh(self):
        x.save_tokens(tokens(), self.c)
        changed = dict(self.c, scopes=['offline_access', 'accounting.settings'])
        with patch.object(x, 'request') as request:
            with self.assertRaises(x.AccessError): x.access_token(changed, force_refresh=True)
            request.assert_not_called()
        with self.assertRaises(x.AccessError):
            x.save_tokens(tokens(['offline_access', 'accounting.settings', 'payroll.employees']), self.c)

    def test_management_grant_and_rotating_refresh(self):
        scope = ['offline_access', 'accounting.settings', 'accounting.invoices', 'assets']
        c = dict(self.c, scopes=scope)
        x.save_tokens(tokens(scope), c)
        fresh = dict(tokens(scope), access_token='new-synthetic-access', refresh_token='new-synthetic-refresh')
        with patch.object(x, 'request', return_value=fresh) as request:
            self.assertEqual(x.access_token(c, True), 'new-synthetic-access')
            self.assertEqual(request.call_args.kwargs['form']['refresh_token'], 'synthetic-refresh-only')
        saved = json.loads(x.protect((x.local_dir() / 'tokens.dpapi').read_bytes(), decrypt=True))
        self.assertEqual(saved['tokens']['refresh_token'], 'new-synthetic-refresh')

    def test_no_arbitrary_endpoint_or_accounting_post(self):
        for url, kwargs in [('https://external.example', {}), (x.ORGANISATION, {'form': {}}), (x.TOKEN, {})]:
            with self.assertRaises(x.AccessError): x.request(url, **kwargs)

    def test_discovery_does_not_pin_or_read_books(self):
        self.c['organisations'][0]['tenant_id'] = None
        before = self.path.read_bytes()
        rows = [{'tenantId': ID, 'tenantName': 'Synthetic Company', 'tenantType': 'ORGANISATION'},
                {'tenantId': OTHER, 'tenantName': 'Unrelated', 'tenantType': 'ORGANISATION'}]
        with patch.object(x, 'access_token', return_value='synthetic'), patch.object(x, 'request', return_value=rows) as req:
            out = io.StringIO()
            with contextlib.redirect_stdout(out): x.discover(self.c)
            self.assertEqual(json.loads(out.getvalue())['candidates_for_review'],
                             [{'expected_name': 'Synthetic Company', 'tenant_id': ID}])
            req.assert_called_once_with(x.CONNECTIONS, bearer='synthetic')
        self.assertEqual(before, self.path.read_bytes())

    def test_complete_partial_and_unexpected_live_evidence(self):
        x.save_tokens(tokens(), self.c)
        before = self.path.read_bytes()
        rows = [{'tenantId': ID, 'tenantName': 'Synthetic Company', 'tenantType': 'ORGANISATION'}]
        def fake(url, **kwargs):
            if url == x.CONNECTIONS: return rows
            self.assertEqual(kwargs['tenant'], ID)
            return {'Organisations': [{'OrganisationID': ID, 'Name': 'Synthetic Company', 'LegalName': 'Synthetic Legal'}]}
        with patch.object(x, 'request', side_effect=fake), contextlib.redirect_stdout(io.StringIO()):
            self.assertTrue(x.verify(self.c))
            self.assertTrue(x.verify(self.c))
        self.assertEqual(len(list(Path(self.c['evidence_dir']).glob('*.json'))), 2)
        self.assertEqual(before, self.path.read_bytes())
        with patch.object(x, 'request', return_value=[]), contextlib.redirect_stdout(io.StringIO()):
            self.assertFalse(x.verify(self.c))
        with patch.object(x, 'request', return_value=[dict(rows[0], tenantId=OTHER)]):
            with self.assertRaises(x.AccessError): x.verify(self.c)

    def test_callback_state_host_pkce_and_secret_free_logging(self):
        # Actual loopback-only callback; fake token exchange prevents any Xero network use.
        server = HTTPServer(('127.0.0.1', 0), x.BaseHTTPRequestHandler)
        port = server.server_address[1]
        c = dict(self.c, redirect_uri=f'http://localhost:{port}/callback')
        ready = threading.Event()
        errors = []
        def factory(address, handler):
            self.assertEqual(address, ('127.0.0.1', port))
            server.RequestHandlerClass = handler
            ready.set()
            return server
        def worker():
            try: x.connect(c)
            except Exception as e: errors.append(e)
        def get(path, host=None):
            conn = http.client.HTTPConnection('127.0.0.1', port, timeout=3)
            conn.request('GET', path, headers={'Host': host or f'localhost:{port}'})
            response = conn.getresponse()
            result = response.status, response.getheader('Location'), response.read()
            conn.close()
            return result
        out = io.StringIO()
        with patch.object(x, 'HTTPServer', side_effect=factory), patch.object(x, 'request', return_value=tokens()) as req, patch.object(x, 'save_tokens') as save, contextlib.redirect_stdout(out):
            thread = threading.Thread(target=worker, daemon=True); thread.start()
            self.assertTrue(ready.wait(3))
            self.assertEqual(get('/start', 'external.example')[0], 400)
            code, location, _ = get('/start')
            self.assertEqual(code, 302)
            auth = parse_qs(urlsplit(location).query)
            self.assertEqual(get('/callback?state=incorrect&code=synthetic-code')[0], 400)
            self.assertFalse(req.called)
            good = '/callback?' + urlencode({'state': auth['state'][0], 'code': 'synthetic-code'})
            self.assertEqual(get(good)[0], 200)
            thread.join(3)
            self.assertFalse(thread.is_alive()); self.assertEqual(errors, [])
            verifier = req.call_args.kwargs['form']['code_verifier']
            challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip('=')
            self.assertEqual(challenge, auth['code_challenge'][0])
            save.assert_called_once()
        self.assertNotIn('synthetic-code', out.getvalue())
        self.assertNotIn(auth['state'][0], out.getvalue())


if __name__ == '__main__':
    unittest.main()
