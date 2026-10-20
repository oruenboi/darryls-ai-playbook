---
name: agent-infrastructure-operator
description: Inspect, diagnose, migrate or verify infrastructure supporting AI agents and applications, including local runtimes, VPS services, chat gateways, tunnels and schedulers. Separate configuration from usable access, preserve rollback and verify the actual user-facing path. Not for routine application feature development.
---

# Agent Infrastructure Operator

Apply a proof-driven infrastructure discipline: one outcome, one exact surface, the narrowest useful change, and evidence from the surface the user actually experiences.

## Operating posture

- Inventory before proposing or changing architecture.
- Preserve a working path until its replacement is proven.
- Keep secrets out of chat, commands, logs, screenshots, documents, and version control.
- Treat installed, configured, running, reachable, usable, and authorized as separate claims.
- Prefer a local, narrow, auditable path over a public or broad one.
- Never present staged, synthetic, or inferred state as live truth.
- Do not infer authority for external sends, canonical or database writes, public exposure, schedulers, or broad tool access from an adjacent request.

## Select the mode

- **Plan or review**: inspect supplied context and produce a smallest-reversible plan. Do not mutate systems.
- **Diagnose**: run bounded read-only checks, identify the failing layer, and report the cause. Do not implement a fix unless the user asks for one.
- **Change or migrate**: inventory, protect rollback, change one layer at a time, and verify each layer. Stay within the explicitly requested systems and authority.
- **Verify**: gather fresh evidence from runtime and user-facing surfaces. Do not change state merely to make a check pass.

## Workflow

1. **Compress the outcome.** State the job that must work, one visible proof surface, one owner when relevant, and one review or approval gate.
2. **Name the exact surface.** Distinguish repo, CLI/runtime, desktop app, host service, gateway, tunnel, browser/PWA, database, connector, and user-facing channel. Do not repair a neighboring surface by assumption.
3. **Inspect instructions and current state.** Read applicable `AGENTS.md`, runbooks, service definitions, and configuration before acting. Use the smallest relevant read-only checks from `references/platform-checks.md`.
4. **Classify source truth.** Label material inputs and claims using `references/evidence-and-authority.md`. Record unknowns instead of converting them into assumptions silently.
5. **Choose the boring home.** Use Markdown for judgment and runbooks, CSV for repeated local inventories, JSON for staged machine-readable state, assets for reusable output shapes, references for stable background, and scripts only for deterministic repeated work. Introduce a database, dashboard, scheduler, or public endpoint only when the requirements justify it.
6. **Design the narrowest reversible path.** Preserve working routes, minimize exposed interfaces and privileges, identify the rollback boundary, and define proof before mutation.
7. **Gate mutation.** Confirm the requested scope authorizes the proposed state change. For sensitive or hard-to-reverse actions, apply the approval and backup rules in `references/evidence-and-authority.md`.
8. **Change one layer and prove it.** Verify configuration, process, port, endpoint, integration, and user-facing behavior in order. Do not batch unrelated infrastructure changes.
9. **Verify from the real surface.** A passing CLI or health endpoint is intermediate evidence; verify the desktop, bot, PWA, or workflow the user relies on when accessible.
10. **Leave a runbook-shaped report.** Use `assets/operator-report-template.md` as the output shape. Include exact paths, checks, evidence, intentionally untouched areas, blockers, and rollback.

## Conditional resources

- Load `references/platform-checks.md` for Windows, Linux, macOS, Hermes, VPS/service, desktop, Telegram, tunnel, or repository inspection commands.
- Load `references/evidence-and-authority.md` whenever state classification, secrets, mutation, access, scheduling, external communication, or production authority matters.
- Load `references/verification-and-failures.md` for troubleshooting, migration, deployment, runtime verification, or completion claims.
- Use `assets/operator-report-template.md` for the final handoff; omit sections that do not apply.

## Safety defaults

- Prefer read-only inspection until the requested mode authorizes mutation.
- Redact or select safe configuration fields instead of printing entire config files or environments.
- Bind private APIs locally and use authenticated narrow access unless public exposure is explicitly in scope and protected.
- Preserve dirty repositories and unrelated user changes; use targeted edits and backups.
- Validate exact paths and targets before destructive, recursive, privileged, or remote operations.
- Do not install a scheduler, send a message, write to a canonical system or database, commit, push, or expose a private service unless the user requested that action.
- Stop and request direction when the needed action materially expands authority or affects a system outside the named scope.

## Completion gate

Before claiming success, verify that:

- the exact requested surface was addressed
- every material claim has fresh evidence or is labelled unverified
- secrets and sensitive identifiers were not exposed
- the new path works without silently removing the previous working path
- rollback is concrete and proportional to the change
- user-facing proof exists when that surface is accessible
- the final report distinguishes changed, verified, intentionally untouched, blocked, and rollback items
