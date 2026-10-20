# Bundled Windows PKCE helper

Use scripts/xero_access.py when no existing supported connection path fits. Python 3.11+ standard library only; Windows DPAPI is required. On other operating systems use the platform's protected secret store or an existing supported OAuth client instead of writing plaintext tokens.

## Configure

Copy assets/config.example.json to the client's project, preserving any existing config. Replace the synthetic fields with reviewed client values:

- credential_namespace: a unique client-agent slug, never reused across engagements.
- profiles: arbitrary safe lowercase profile names, each with its app name, public client_id, organisation list and verified connection_limit (or null if not yet determined).
- redirect_uri: the exact registered http://localhost:PORT/callback, using a free local port above 1023. The helper binds 127.0.0.1 only.
- scopes: explicitly reviewed requested scopes, including offline_access and a settings scope for verification. The example starts with identity verification only; it is not a universal recommended grant.
- organisations: label, exact expected_name and pinned tenant_id UUID. Null IDs are allowed for connect/discover but verification refuses them until reviewed and pinned.
- excluded: exact labels, Xero names or tenant IDs that must not be connected or queried.
- evidence_dir: the user-designated location for non-secret reports, absolute or relative to this config file. Reports use unique timestamped filenames.

App registrations and public client IDs are configured through the current Xero portal. No client secret is needed for PKCE. This script does not create apps, accept terms, choose a subscription or click consent.

## Commands

Substitute actual absolute paths for SCRIPT and CONFIG and the chosen profile for PROFILE:

```powershell
python SCRIPT validate --config CONFIG --profile PROFILE
python SCRIPT connect --config CONFIG --profile PROFILE
python SCRIPT discover --config CONFIG --profile PROFILE
python SCRIPT verify --config CONFIG --profile PROFILE
python SCRIPT refresh-verify --config CONFIG --profile PROFILE
```

SCRIPT is the installed skill's scripts/xero_access.py. CONFIG is the client-specific JSON file, never a shared skill asset. To test the skill itself:

```powershell
python -m unittest discover -s SCRIPTS_DIRECTORY -p test_xero_access.py -v
```

Connect prints only a local start address and waits up to 15 minutes. Open that address using browser tools. It redirects to official Xero consent using in-memory state and PKCE. Complete the already reviewed company grant, then use discover if IDs still need mapping and verify each pinned company. Repeat for remaining organisations; run profiles sequentially when they use the same callback port.

Discover lists exact-name candidates for review without changing config or reading accounting records. Verify saves identity and granted/missing-scope evidence but does not modify mappings or business records. Exit 0 means all configured tenants and scopes passed; 2 means partial coverage; 1 means the operation stopped. A valid local config is not proof of access.

## Storage and security

The canonical cache is under LOCALAPPDATA/CodexClientConnections/Xero/NAMESPACE/PROFILE/tokens.dpapi. Windows user-bound DPAPI encrypts access/refresh tokens; encrypted records also bind client_id, namespace and profile. Do not move live tokens from a pre-existing app into this new cache. Migrate a working integration only as an explicitly scoped operation with refresh-rotation coordination.

A namespace-wide process lock serializes operations across its profiles. Writes replace ciphertext atomically. No token/authorization-code values are printed. The callback accepts the exact Host/path and constant-time matching state, then consumes the flow once. HTTPS API redirects are refused. Only token POST, connections GET and Organisation GET exist; granted write scopes do not add a general-purpose write command.

Requested scope changes are detected before an existing cache can be reused. Run connect for reviewed fresh consent. A failed grant never proves access. Return-code and live evidence checks remain required even if the callback page looks successful, or if the page errors after a completed exchange.

Same-user Windows processes can still decrypt DPAPI data. This is local user isolation, not a defence against compromise of the logged-in account. No scheduler, public listener, model runtime or billing subscription is installed.
