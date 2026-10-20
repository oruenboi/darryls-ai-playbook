# Verification and Failure Handling

Use this reference for migrations, changes, debugging, and any claim that infrastructure is working.

## Proof ladder

Verify one layer at a time:

1. **Artifact**: the intended configuration, unit, profile, or manifest exists with a redacted expected shape.
2. **Validation**: the relevant parser, doctor, linter, or dry run succeeds.
3. **Runtime**: the expected process or service is active under the intended identity.
4. **Network**: the expected address and port are listening through the intended access path.
5. **Protocol**: health, API, WebSocket, webhook, or gateway behavior succeeds.
6. **Integration**: the consuming app, profile, bot, or adapter sees the runtime.
7. **User surface**: a harmless end-to-end action works where the user experiences it.
8. **Authority**: permissions and autonomy remain within the approved boundary.

Stop at the first failed layer and investigate there before changing later layers.

## Evidence quality

Prefer evidence in this order:

1. Direct user-facing result
2. Protocol or API response from the intended client path
3. Service state plus correlated logs
4. Process, port, file, or configuration state
5. Plan, command text, or staged artifact

Use timestamps and exact surfaces when state may change. Redact secrets and sensitive payloads.

## Common failure modes

- **Wrong surface**: repairing a repo, CLI, or gateway adjacent to the actual broken desktop, bot, or service.
- **Fake completion**: calling something connected because configuration exists or a process started.
- **Over-broad access**: opening public ports or granting a shell when a local bind, tunnel, or allowlist is enough.
- **Secret leakage**: printing full config, environment variables, tokens, headers, or private logs.
- **Toolset confusion**: assuming CLI, desktop, VPS, Telegram, and profiles expose identical tools or authority.
- **Scheduler fantasy**: describing a cron, task, launchd, or systemd schedule as active without checking the scheduler and its execution evidence.
- **Canonical drift**: allowing staged or synthetic outputs to be treated as source truth.
- **Batch-change ambiguity**: modifying several layers before checking which one fixed or broke the path.
- **Rollback fiction**: naming rollback without preserving the prior state or giving a concrete restoration step.

## Completion rule

If the final user-facing step cannot be tested, say exactly which lower layers were verified and label overall usability unverified. Do not replace missing proof with confidence language.
