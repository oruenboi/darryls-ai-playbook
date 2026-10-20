# Connection workflow and recovery

## Inventory and registration

Inspect the scoped project and available connector tools first. If using the portal, read the app list, registration type, registered redirect and connection management. A public client ID is configuration; a client secret and tokens are secrets. Do not reveal secrets to inspect a connection.

Existing clients may already have a connection path. A GET /connections returning 401 usually establishes only that the access token failed. Use that integration's normal refresh mechanism when authorised; do not replace its app, rotate its credentials or switch its tenant by inference.

For a new desktop PKCE registration, prepare:

- App name derived from this agent/application; profile suffixes only if needed.
- The user's verified company/application URL, not a fabricated production site.
- Exact registered loopback callback used by the local listener.
- Accurate answers to the portal's current AI-use and security questions. Do not equate normal inference with model training, and do not attest to unverified operational practices.
- The provider's terms/security declarations and the actual data-access consent as distinct actions.

Select capacity after inspecting the current app limits, existing connections and user preference. An app registration can cover multiple organisations; conversely, multiple registrations can serve one application when that is the chosen supported setup. Existing subscriptions/roles can also limit individual endpoints.

## Organisation mapping

Build a per-profile mapping of label, exact Xero display name and tenant UUID, with explicit exclusions. Browser consent selectors can expose tenant IDs; otherwise use GET /connections and review exact-name candidates. The bundled discover command returns only configured-name matches and never silently changes the map. Verify legal name with Organisation after consent. Renames, duplicate names or duplicate connection rows need resolution before continuing. Never choose an unrelated tenant because the desired company is unavailable.

Repeat consent only for missing companies under the intended app. Same app/user connections normally accumulate; verify the result rather than assume accumulation. Keep a single canonical refresh cache per app/user grant family. Do not revoke previous company connections merely to add another.

## Evidence and failure handling

Use this order: local config validity, callback/listener readiness, provider consent, successful exchange and encrypted save, connections inventory, Organisation reads, refreshed scopes and reads. Record which level actually succeeded.

- Consent denied or cancelled: no success claim; report the affected profile.
- 401: check expiry and refresh/reconnect within that profile; do not reset another integration.
- 403: inspect scope, organisation user role and endpoint/plan availability; an OAuth scope alone does not prove endpoint access.
- 429: stop and respect Retry-After or the current provider window; do not launch parallel probes.
- Network timeout during refresh: preserve the encrypted cache and failure evidence; investigate rotation/retry semantics before repeated exchanges.
- Callback page error: inspect the local listener result and perform an API read before deciding the grant failed. In one observed flow Chrome blocked the final local confirmation page after the token exchange had already succeeded. This is a diagnostic possibility, not an instruction to ignore browser security warnings or assume success.
- Scope change: restart consent with the exact revised scope set. An old refresh token cannot grant new scopes. A material change invalidates the earlier narrow consent preview.

An excluded company with no Xero needs no subscription or replacement organisation created. Record it as excluded rather than failed.

## Completion and rollback

Report the assigned company/profile map, granted scope families, refresh/API verification, missing access and commands. Grant broad access when requested without performing a sample financial write. Keep no secret values in the report.

If the user asks to revoke, disconnect only the specified app/tenant grant through the provider and handle only its isolated local cache. Do not delete client business data or another app's connection. No scheduler is implied by persistent refresh capability.

Official references (recheck current rules when used):

- https://developer.xero.com/documentation/guides/oauth2/pkce-flow/
- https://developer.xero.com/documentation/guides/oauth2/auth-flow/
- https://developer.xero.com/documentation/guides/oauth2/limits/
- https://developer.xero.com/pricing
- https://developer.xero.com/partner/security-requirements-for-developer-partners
