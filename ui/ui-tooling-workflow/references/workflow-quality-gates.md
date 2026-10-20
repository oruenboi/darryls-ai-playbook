# Workflow Quality Gates

Use this reference to keep design and engineering aligned.

## Handoff
- Record the exact target and revision/date, assessment versus change intent, preserved constraints, and acceptance checks. Revalidate older findings against current code before applying them.
- Include token values, state behavior, and responsive rules.
- Document empty, loading, and error states.
- Keep design artifact and implementation docs synchronized.

## Collaboration
- Use clear branch naming and review standards.
- Document breaking changes before merging.
- Keep changelogs readable across functions.

## Testing
- Define unit, integration, and visual regression coverage.
- Gate critical UI changes with automated checks.
- Track regression issues to closure.

## Evidence and iteration

- Use the repository's existing checks and permitted browser/native tools. Do not require Impeccable binaries, background services, hooks, overlays, or automatic downloads.
- Keep observed behavior, measured values, and design judgment distinguishable. Each important finding needs a location, user impact, repair owner, and a check that would establish resolution.
- Inspect relevant viewports and states in a batch, repair in a batch, then confirm. A small local fix only needs its affected checks; a new flow needs end-to-end verification. Stop cosmetic iteration when acceptance criteria pass, without abandoning required correctness checks.
- Record source-only inspection, screenshot review, keyboard/mouse interaction, emulated touch, and physical-device tests separately. Do not claim screen-reader compatibility or touch behavior from layout inspection alone.
- Include actual command outcomes and untested limitations. Do not turn a heuristic score into a compliance certificate or a claim of measured performance.
- Assessment-only work ends with findings. Creating a report does not authorize repairs, pushes, PRs, or changes to project policy.

Local adaptation, 2026-10-03. See [source attribution](impeccable-attribution.md).
