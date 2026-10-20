# Evidence and Authority

Use this reference to prevent staged artifacts, reachable runtimes, or adjacent permissions from being mistaken for production truth or operating authority.

## Source-truth classes

| Class | Meaning | Allowed claim |
| --- | --- | --- |
| `real` | Fresh live state, direct observation, or a user-provided value explicitly accepted as current | State what was observed and how |
| `staged` | Local or reviewable artifact not yet activated | Describe as prepared or awaiting review |
| `synthetic` | Fixture, demo, mock, placeholder, or generated example | Use only for testing or illustration |
| `missing` | Required input or evidence is absent | Name the blocker and owner if known |
| `unknown` | Present or plausible but not verified | Keep the claim unresolved |

Do not promote `staged`, `synthetic`, or `unknown` evidence to `real` without fresh proof.

## State-claim ladder

Treat each state as a separate claim:

1. **Discovered**: the component or artifact exists.
2. **Installed**: required binaries or packages are present.
3. **Configured**: configuration parses and points to intended dependencies.
4. **Running**: the process or service is active.
5. **Reachable**: the intended client can contact it through the intended path.
6. **Usable**: a harmless end-to-end action works from the user-facing surface.
7. **Authorized**: the runtime has only the approved capabilities and boundaries.

Evidence at one level does not prove the next.

## Authority dimensions

Track authority independently for:

- UI access
- chat receive and reply
- file read
- local file write
- terminal execution
- remote host execution
- external send
- database write
- canonical business-system mutation
- scheduler or unattended execution
- public network exposure
- credential or secret access

A user request explicitly naming an action and target can authorize that action. Do not infer another authority dimension from it. For example, permission to configure a bot does not automatically authorize sending messages or enabling a scheduler.

## Mutation gate

Before a state change:

1. Resolve the exact target, surface, environment, and owner.
2. Confirm the action is within the user's request.
3. Inspect current state and preserve unrelated working paths.
4. Identify the failure radius and rollback action.
5. Back up material configuration or data when the mutation is difficult to reverse.
6. Avoid printing secrets while inspecting or backing up state.
7. Apply one bounded change, then verify it before continuing.

Request direction before proceeding when the necessary action would materially expand scope, expose a private service publicly, activate unattended execution, communicate externally, overwrite canonical data, or perform a destructive migration not already requested.

## Backup guidance

- Use explicit, resolved paths rather than broad globs or home-directory targets.
- Keep permissions and ownership appropriate for secret-bearing files.
- Record the backup location and restoration command without exposing secret contents.
- Prefer application-native snapshots or exports for databases and managed services.
- Test restoration when the risk warrants it; an untested backup is only partial evidence.
