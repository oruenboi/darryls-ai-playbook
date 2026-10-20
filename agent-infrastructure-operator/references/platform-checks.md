# Platform Checks

Load only the sections relevant to the named surface. Start with the smallest read-only set. Avoid commands that dump full environments or configuration files.

## Contents

- Repository and instructions
- Processes, services, and listening ports
- Hermes runtime
- Desktop and Office/Claw3D
- Telegram or chat gateways
- VPS and hosted services
- Tunnels and remote connections

## Repository and instructions

Use `rg` first when available.

### PowerShell

```powershell
Get-Location
git status --short
rg --files -g 'AGENTS.md' -g '*.md' -g '*.json' -g '*.yaml' -g '*.yml'
Get-Content -LiteralPath '.\AGENTS.md'
```

### Bash or zsh

```bash
pwd
git status --short
rg --files -g 'AGENTS.md' -g '*.md' -g '*.json' -g '*.yaml' -g '*.yml'
sed -n '1,220p' AGENTS.md
```

Read applicable instruction files to the end; the shell preview above is not a complete read if the file exceeds 220 lines. Do not run broad cleanup in a dirty repository. Inspect nested `AGENTS.md` files before touching files below them.

## Processes, services, and listening ports

### Windows PowerShell

```powershell
Get-Process | Where-Object { $_.ProcessName -match 'hermes|gateway|node|telegram|openclaw' } | Select-Object ProcessName, Id, Path
Get-Service | Where-Object { $_.Name -match 'hermes|gateway|openclaw' -or $_.DisplayName -match 'hermes|gateway|openclaw' } | Select-Object Status, Name, DisplayName
Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, OwningProcess
```

### Linux

```bash
ps -eo pid,comm | rg -i 'hermes|gateway|node|telegram|openclaw'
systemctl show <service> --property=ActiveState,SubState,MainPID
ss -lntp
```

### macOS

```bash
ps -axo pid,comm | rg -i 'hermes|gateway|node|telegram|openclaw'
launchctl list | rg -i 'hermes|gateway|openclaw'
lsof -nP -iTCP -sTCP:LISTEN
```

Filter large outputs to the relevant process or port. Avoid full process command lines, which can contain credentials. Service status and logs can also expose secret-bearing arguments or payloads: select safe fields and apply local redaction before returning output to the model or chat. If safe redaction cannot be established, do not dump the logs.

## Hermes runtime

Discover the installed command surface first:

```text
hermes --version
hermes --help
```

Use status, diagnostic, profile or gateway commands only if listed in that version's help. Inspect diagnostic behavior before running it; a command labelled "doctor" may offer repairs or contact external services. Record CLI, desktop, profile and gateway state separately.

## Desktop and Office/Claw3D

Inspect only safe fields. Never print API keys or entire configuration objects. The field names below are examples, not a guarantee of safe values: inspect and redact embedded credentials, query tokens, user identifiers and secret-bearing URLs locally before returning selected fields.

### PowerShell example

```powershell
$desktopConfig = Get-Content -LiteralPath '<desktop-config-path>' -Raw | ConvertFrom-Json
$desktopConfig | Select-Object gateway, adapterType, office, mode, remoteUrl
```

### jq example

```bash
jq '{gateway,adapterType,office,mode,remoteUrl}' <desktop-config-path>
```

After configuration checks, verify the actual desktop or Office surface through its visible connection state, accessibility tree, screenshot, or harmless interaction.

## Telegram or chat gateways

- Identify the exact bot handle, gateway/profile, allowed users, and allowed chats.
- Never print or paste the bot token.
- Verify gateway process state and redacted logs before sending a test.
- Send a harmless test only when messaging is explicitly in scope.
- Confirm delivery in the exact target chat and correlate it with gateway logs.
- Treat receiving, replying, group mentions, and proactive sends as separate capabilities.

## VPS and hosted services

- Confirm the exact host and service before connecting or changing anything.
- Inspect service definition, environment source, bind address, port, health check, and recent redacted logs.
- Prefer localhost binding behind an authenticated tunnel or proxy when public access is unnecessary.
- Verify firewall, reverse-proxy, TLS, and authentication layers separately when public access is required.
- Preserve the existing service path until the replacement passes end-to-end verification.

## Tunnels and remote connections

- Identify both endpoints, bind addresses, forwarded ports, authentication, and permitted destinations.
- Prefer restricted keys and destination allowlists over general shell access.
- Prove local listening state, tunnel establishment, remote endpoint response, and consuming-app behavior separately.
- Do not classify a tunnel as usable solely because its process is running.
