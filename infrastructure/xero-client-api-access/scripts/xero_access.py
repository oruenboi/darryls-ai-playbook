"""Client-scoped Windows PKCE connections; verification never writes accounting records."""
import argparse
import base64
import ctypes
from ctypes import wintypes
import hashlib
import hmac
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from pathlib import Path
import secrets
import re
from uuid import UUID
import sys
import time
from urllib.parse import parse_qs, urlencode, urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError, URLError

CONFIG = None
PROFILE = None
NAMESPACE = None
AUTH = 'https://login.xero.com/identity/connect/authorize'
TOKEN = 'https://identity.xero.com/connect/token'
CONNECTIONS = 'https://api.xero.com/connections'
ORGANISATION = 'https://api.xero.com/api.xro/2.0/Organisation'
APPROVED_SCOPES = {'offline_access', 'accounting.settings.read', 'accounting.contacts.read',
               'accounting.invoices.read', 'accounting.banktransactions.read',
               'accounting.payments.read', 'accounting.settings', 'accounting.contacts',
               'accounting.attachments', 'accounting.payments', 'accounting.invoices',
               'accounting.banktransactions', 'accounting.manualjournals', 'accounting.budgets.read',
               'accounting.reports.aged.read', 'accounting.reports.balancesheet.read',
               'accounting.reports.banksummary.read', 'accounting.reports.budgetsummary.read',
               'accounting.reports.executivesummary.read', 'accounting.reports.profitandloss.read',
               'accounting.reports.trialbalance.read', 'accounting.reports.taxreports.read',
               'files', 'assets', 'projects', 'accounting.attachments.read',
               'accounting.manualjournals.read', 'files.read', 'assets.read', 'projects.read',
               'accounting.reports.tenninetynine.read', 'payroll.employees', 'payroll.employees.read',
               'payroll.payruns', 'payroll.payruns.read', 'payroll.payslip', 'payroll.payslip.read',
               'payroll.settings', 'payroll.settings.read', 'payroll.timesheets', 'payroll.timesheets.read'}


class AccessError(Exception):
    pass


def config():
    global NAMESPACE
    document = json.loads(CONFIG.read_text(encoding='utf-8'))
    if document.get('schema_version') != 1:
        raise AccessError('Unsupported configuration schema_version.')
    namespace = document.get('credential_namespace', '')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', namespace) or len(namespace) > 64:
        raise AccessError('Use a unique lowercase client-agent credential_namespace.')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', PROFILE or ''):
        raise AccessError('Select a safe explicit profile name.')
    if PROFILE not in document.get('profiles', {}):
        raise AccessError('Profile is not configured.')
    c = {**document, **document['profiles'][PROFILE], 'profile': PROFILE}
    callback = urlsplit(c.get('redirect_uri', ''))
    if (callback.scheme != 'http' or callback.hostname != 'localhost' or not callback.port
            or callback.port < 1024 or callback.path != '/callback'
            or callback.query or callback.fragment or callback.username or callback.password):
        raise AccessError('Use an exact http://localhost:PORT/callback registered redirect.')
    if not c.get('client_id') or not isinstance(c['client_id'], str):
        raise AccessError('Register the app and configure its public client_id.')
    scopes = set(c.get('scopes', []))
    if (not scopes or not scopes <= APPROVED_SCOPES or 'offline_access' not in scopes
            or not scopes.intersection({'accounting.settings', 'accounting.settings.read'})):
        raise AccessError('Select supported scopes including offline access and organisation settings access.')
    orgs = c.get('organisations', [])
    if not orgs:
        raise AccessError('Configure the intended organisations first.')
    if c.get('connection_limit') is not None and len(orgs) > c['connection_limit']:
        raise AccessError('Profile exceeds its verified connection limit.')
    names, ids, labels = set(), set(), set()
    for org in orgs:
        if not org.get('label') or not org.get('expected_name'):
            raise AccessError('Each organisation requires a label and exact expected_name.')
        if org['expected_name'] in names:
            raise AccessError('Duplicate organisation name within profile.')
        names.add(org['expected_name'])
        if org['label'] in labels:
            raise AccessError('Duplicate organisation label within profile.')
        labels.add(org['label'])
        if org.get('tenant_id'):
            try:
                UUID(org['tenant_id'])
            except (ValueError, TypeError):
                raise AccessError('Invalid tenant ID.') from None
            if org['tenant_id'] in ids:
                raise AccessError('Duplicate tenant ID within profile.')
            ids.add(org['tenant_id'])
        reject_excluded(c, org)
    evidence = Path(c.get('evidence_dir', ''))
    if not c.get('evidence_dir'):
        raise AccessError('Configure an evidence_dir for non-secret verification reports.')
    c['evidence_dir'] = str((CONFIG.parent / evidence).resolve())
    NAMESPACE = namespace
    return c


def reject_excluded(c, org):
    values = {str(org.get(k, '')).casefold() for k in ('label', 'expected_name', 'tenant_id')}
    if values.intersection({str(v).casefold() for v in c.get('excluded', [])}):
        raise AccessError('Organisation is explicitly excluded.')


def local_dir():
    if os.name != 'nt':
        raise AccessError('This helper requires Windows DPAPI. Use an OS-native secret store on other hosts.')
    for value in (NAMESPACE, PROFILE):
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', value or ''):
            raise AccessError('Explicit safe client namespace and profile are required.')
    d = Path(os.environ['LOCALAPPDATA']) / 'CodexClientConnections' / 'Xero' / NAMESPACE / PROFILE
    d.mkdir(parents=True, exist_ok=True)
    return d


class Blob(ctypes.Structure):
    _fields_ = [('cbData', wintypes.DWORD), ('pbData', ctypes.POINTER(ctypes.c_ubyte))]


def protect(data, decrypt=False):
    if os.name != 'nt':
        raise AccessError('DPAPI is only supported on Windows.')
    buf = (ctypes.c_ubyte * len(data)).from_buffer_copy(data)
    source = Blob(len(data), buf)
    output = Blob()
    crypt = ctypes.WinDLL('crypt32', use_last_error=True)
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel.LocalFree.argtypes = [ctypes.c_void_p]
    kernel.LocalFree.restype = ctypes.c_void_p
    function = crypt.CryptUnprotectData if decrypt else crypt.CryptProtectData
    function.argtypes = [ctypes.POINTER(Blob), ctypes.c_void_p, ctypes.c_void_p,
                         ctypes.c_void_p, ctypes.c_void_p, wintypes.DWORD,
                         ctypes.POINTER(Blob)]
    function.restype = wintypes.BOOL
    if not function(ctypes.byref(source), None, None, None, None, 1, ctypes.byref(output)):
        raise AccessError('Windows credential protection failed.')
    try:
        return ctypes.string_at(output.pbData, output.cbData)
    finally:
        kernel.LocalFree(output.pbData)


class Lock:
    def __enter__(self):
        import msvcrt
        self.f = (local_dir().parent / 'operation.lock').open('a+b')
        self.f.seek(0)
        if not self.f.read(1):
            self.f.write(b'0'); self.f.flush()
        self.f.seek(0)
        try:
            msvcrt.locking(self.f.fileno(), msvcrt.LK_NBLCK, 1)
        except OSError:
            self.f.close()
            raise AccessError('Another Xero access operation is running.') from None
        return self

    def __exit__(self, *_):
        import msvcrt
        self.f.seek(0)
        msvcrt.locking(self.f.fileno(), msvcrt.LK_UNLCK, 1)
        self.f.close()


def save_tokens(tokens, c):
    if not tokens.get('access_token') or not tokens.get('refresh_token'):
        raise AccessError('Token response lacks persistent access; reconnect.')
    scopes = set(tokens.get('scope', '').split())
    requested = set(c['scopes'])
    if (not scopes or not scopes <= requested or not requested <= APPROVED_SCOPES
            or not scopes.intersection({'accounting.settings', 'accounting.settings.read'})):
        raise AccessError('Unexpected granted scopes; tokens were not activated.')
    record = {'client_id': c['client_id'], 'namespace': NAMESPACE, 'profile': PROFILE, 'tokens': tokens,
              'expires_at': time.time() + int(tokens['expires_in']) - 60}
    target = local_dir() / 'tokens.dpapi'
    temporary = target.with_suffix('.tmp')
    temporary.write_bytes(protect(json.dumps(record).encode()))
    os.replace(temporary, target)


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def request(url, *, bearer=None, tenant=None, form=None):
    if url not in {TOKEN, CONNECTIONS, ORGANISATION}:
        raise AccessError('Endpoint is not allowlisted.')
    if (form is not None) != (url == TOKEN):
        raise AccessError('Only OAuth token exchange permits POST.')
    headers = {'Accept': 'application/json'}
    data = None
    if bearer:
        headers['Authorization'] = 'Bearer ' + bearer
    if tenant:
        headers['xero-tenant-id'] = tenant
    if form is not None:
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = urlencode(form).encode()
    try:
        with build_opener(NoRedirect).open(Request(url, data=data, headers=headers), timeout=30) as r:
            return json.load(r)
    except HTTPError as e:
        raise AccessError(f'Xero HTTP {e.code}; stopped without retry. Response body withheld.') from None
    except (URLError, TimeoutError, json.JSONDecodeError):
        raise AccessError('Xero network/response failure; stopped without retry.') from None


def access_token(c, force_refresh=False):
    p = local_dir() / 'tokens.dpapi'
    if not p.exists():
        raise AccessError('No connection saved. Run connect and complete Xero consent.')
    record = json.loads(protect(p.read_bytes(), decrypt=True))
    if (record.get('client_id') != c['client_id'] or record.get('namespace') != NAMESPACE
            or record.get('profile') != PROFILE):
        raise AccessError('Stored credentials belong to a different app.')
    t = record['tokens']
    if set(t.get('scope', '').split()) != set(c['scopes']):
        raise AccessError('Requested scopes changed or are incomplete; run connect for fresh consent.')
    if force_refresh or time.time() >= record['expires_at']:
        t = request(TOKEN, form={'grant_type': 'refresh_token', 'client_id': c['client_id'],
                                 'refresh_token': t['refresh_token']})
        save_tokens(t, c)
    return t['access_token']


def match_connections(c, connections):
    """Only explicitly pinned organisations may reach an accounting endpoint."""
    matches = []
    for org in c['organisations']:
        reject_excluded(c, org)
        if not org.get('tenant_id'):
            raise AccessError('Review discovery or consent evidence and pin tenant IDs before verification.')
        rows = [r for r in connections if r.get('tenantType') == 'ORGANISATION'
                and r.get('tenantId') == org['tenant_id']]
        if len(rows) > 1:
            raise AccessError('Ambiguous duplicate connection; resolve explicitly.')
        if rows and rows[0].get('tenantName') != org['expected_name']:
            raise AccessError('Organisation name changed; review the pinned identity.')
        if rows:
            matches.append((org, rows[0]))
    return matches


def discover(c):
    token = access_token(c)
    rows = request(CONNECTIONS, bearer=token)
    expected = {o['expected_name'] for o in c['organisations']}
    candidates = []
    for row in rows:
        if row.get('tenantName') in expected and row.get('tenantType') == 'ORGANISATION':
            reject_excluded(c, {'expected_name': row['tenantName'], 'tenant_id': row['tenantId']})
            candidates.append({'expected_name': row['tenantName'], 'tenant_id': row['tenantId']})
    print(json.dumps({'candidates_for_review': candidates, 'mapping_changed': False}, indent=2))


def verify(c, force_refresh=False):
    token = access_token(c, force_refresh)
    connections = request(CONNECTIONS, bearer=token)
    pinned = {o.get('tenant_id') for o in c['organisations']}
    if any(r.get('tenantId') not in pinned for r in connections):
        raise AccessError('The app has connections outside this profile; review before claiming scoped access.')
    matched = match_connections(c, connections)
    results = []
    for org, connection in matched:
        tenant = connection['tenantId']
        reply = request(ORGANISATION, bearer=token, tenant=tenant)
        records = reply.get('Organisations', [])
        if len(records) != 1 or records[0].get('OrganisationID') != tenant:
            raise AccessError('Organisation identity did not match the selected tenant.')
        rec = records[0]
        if rec.get('Name') != org['expected_name']:
            raise AccessError('Organisation name changed; review mapping before proceeding.')
        org['tenant_id'] = tenant
        results.append({'label': org['label'], 'name': rec.get('Name'),
                        'legal_name': rec.get('LegalName'), 'tenant_id': tenant,
                        'status': 'verified Organisation GET'})
    missing = [o['label'] for o in c['organisations'] if o['label'] not in {r['label'] for r in results}]
    evidence = {'verified_at_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                'organisations': results, 'pending': missing,
                'excluded': c.get('excluded', []), 'refresh_tested': force_refresh, 'profile': PROFILE}
    saved = json.loads(protect((local_dir() / 'tokens.dpapi').read_bytes(), decrypt=True))
    granted = saved['tokens'].get('scope', '').split()
    evidence['granted_scopes'] = granted
    evidence['missing_requested_scopes'] = sorted(set(c['scopes']) - set(granted))
    evidence['accounting_write_tested'] = False
    evidence_dir = Path(c['evidence_dir'])
    evidence_dir.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime('%Y%m%dT%H%M%SZ', time.gmtime()) + '-' + secrets.token_hex(3)
    out = evidence_dir / f'xero-verification-{PROFILE}-{stamp}.json'
    out.write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(evidence, indent=2))
    return not missing and not evidence['missing_requested_scopes']


def connect(c):
    callback = urlsplit(c['redirect_uri'])
    state = secrets.token_urlsafe(32)
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip('=')
    params = {'response_type': 'code', 'client_id': c['client_id'],
              'redirect_uri': c['redirect_uri'], 'scope': ' '.join(c['scopes']),
              'state': state, 'code_challenge': challenge, 'code_challenge_method': 'S256'}
    finished = False
    succeeded = False
    deadline = time.monotonic() + 900

    class Callback(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass  # Never log OAuth codes or URLs.

        def do_GET(self):
            nonlocal finished, succeeded
            path = urlsplit(self.path)
            if self.headers.get('Host') != callback.netloc:
                self.send_error(400); return
            if path.path == '/start':
                self.send_response(302)
                self.send_header('Location', AUTH + '?' + urlencode(params))
                self.send_header('Cache-Control', 'no-store')
                self.end_headers(); return
            if path.path != '/callback':
                self.send_error(404); return
            query = parse_qs(path.query)
            supplied = query.get('state', [])
            if len(supplied) != 1 or not hmac.compare_digest(supplied[0], state):
                self.send_error(400, 'OAuth state rejected'); return
            finished = True
            message = 'Xero did not grant access. No credentials changed.'
            code = query.get('code', [])
            if len(code) == 1 and 'error' not in query:
                try:
                    tokens = request(TOKEN, form={'grant_type': 'authorization_code',
                                     'client_id': c['client_id'], 'code': code[0],
                                     'redirect_uri': c['redirect_uri'], 'code_verifier': verifier})
                    save_tokens(tokens, c)
                    succeeded = True
                    message = 'Xero connection saved securely. Return to Codex for organisation verification.'
                except AccessError as error:
                    message = str(error)
            self.send_response(200 if succeeded else 400)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Referrer-Policy', 'no-referrer')
            self.end_headers()
            self.wfile.write(message.encode())

    with HTTPServer(('127.0.0.1', callback.port), Callback) as server:
        server.timeout = 1
        print(f'Open http://{callback.netloc}/start . Waiting up to 15 minutes for consent.', flush=True)
        while not finished and time.monotonic() < deadline:
            server.handle_request()
    if not succeeded:
        raise AccessError('Connection not completed; no API access verified.')
    print('Connection stored. Run verify to check the allowed organisations.')


def main():
    global PROFILE, CONFIG
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['validate', 'connect', 'discover', 'verify', 'refresh-verify'])
    parser.add_argument('--profile', required=True)
    parser.add_argument('--config', required=True, type=Path)
    args = parser.parse_args()
    PROFILE = args.profile
    CONFIG = args.config.resolve()
    try:
        c = config()
        if args.command == 'validate':
            print('Configuration valid. This does not establish API access.')
            return 0
        with Lock():
            if args.command == 'connect':
                connect(c)
            elif args.command == 'discover':
                discover(c)
            elif not verify(c, args.command == 'refresh-verify'):
                return 2
        return 0
    except AccessError as error:
        print(str(error), file=sys.stderr)
        return 1
    except (OSError, ValueError, KeyError, TypeError):
        # Configuration/OS/token exceptions may contain sensitive values; never dump them.
        print('Xero operation stopped. Check registration, consent, local storage and connection status; no accounting writes performed.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
