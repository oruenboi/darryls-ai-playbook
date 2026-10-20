---
name: xero-client-api-access
description: Connect or reconnect client organisations to an agent through the Xero API; set up OAuth apps, choose scopes, isolate credentials, map tenants, and verify persistent access. Use for initial onboarding, additional companies, scope upgrades, and expired connections, rather than accounting transactions themselves.
---

# Xero Client API Access

Make the client's requested API access work and leave a repeatable connection path. An agent is the application; Xero app registrations are its OAuth identities. More than one registration is a possible deployment choice, not a requirement.

## Establish the boundary

- Inspect the project instructions and existing Xero tooling/configuration before creating anything. Prefer a functioning supported connector or client; the bundled helper is a Windows desktop PKCE fallback.
- Resolve the intended companies, explicit exclusions, application identity, project root and storage location. Folder labels are candidates, not Xero legal names or tenant IDs.
- Ask browser-only versus ongoing API access only if the request is ambiguous. Reuse explicit permission and app choices already made in the session.
- Preserve other clients' apps and credentials. Never default to the first connection or borrow a token cache merely because it is present. Inspect metadata without printing secrets.
- Read [connection workflow](references/connection-workflow.md) for onboarding, additional companies or recovery; read [scope selection](references/scopes.md) when deciding or changing permissions.

## Connect

1. Inspect current Xero app registrations and their actual capacity. Check current official pricing/limits when capacity matters. Do not assume a five-company limit, a fixed price, one app per company or a two-app split. Follow the user's chosen arrangement within provider limits; do not purchase a tier or split registrations merely to avoid a limit without resolving that choice.
2. For a local desktop agent, prefer PKCE when a new registration is needed. A hosted service may require the standard code flow and a server secret store. Do not move a working app between flows blindly.
3. Select scopes from the user's task. Access requests do not automatically imply read-only; explicit write-access requests should receive the corresponding management scopes. Scope possession is distinct from authority to execute an accounting transaction.
4. Prepare the app fields, callback, credential isolation, company mapping and scope list before any required final approval. Match organisation names and IDs from Xero. Keep user login/MFA with the user when needed.
5. Apply the actual tool's consent policy at the action point. Do not add a blanket approval gate to read-only inventory, local preparation or every company click. When confirmation is required, show the exact apps, companies, permissions and ongoing access, and batch unchanged grants where the tool permits. A later material permission expansion requires an updated preview.
6. Finish consent and token exchange. Use a separate client namespace and profile per OAuth grant family. Never copy a rotating refresh token into multiple independently refreshed caches.

For the bundled runner, read [Windows helper](references/windows-helper.md). It accepts external client configuration and stores user-bound DPAPI ciphertext outside the project and synced client documents. It does not install or run Eve, accounting writes, a scheduler or a general API proxy.

## Prove access and close out

- Check each assigned tenant using an authenticated Organisation GET; compare tenant ID, display name and legal name. Pin IDs before business endpoints. A browser session or saved token is not proof of API usability.
- Refresh each profile, then verify all its assigned tenants. Compare returned scopes with the reviewed request. Report missing or blocked companies/scopes explicitly; never treat partial coverage as complete.
- Test access without changing books. Report write permissions as granted, and actual write operations as untested unless a separately authorised business task exercised them.
- Save non-secret mapping, verification timestamps, scope evidence and repeatable commands in the client's designated storage. Keep secrets out of the skill, wiki, logs and source captures. Update the existing project index/log or runbook when appropriate.
- Retain a usable working integration and a precise recovery/revocation path. Future reconnection should affect only the intended profile.

## Reuse boundary

Keep this skill client-neutral. Client names, tenant/client IDs, exclusions, paths, role choices and approvals belong in each engagement. Do not carry one client's grant, browser quirk or price into another engagement as a universal rule. Validate modified helpers with the bundled synthetic tests; those tests must not contact live Xero or alter real grants.
