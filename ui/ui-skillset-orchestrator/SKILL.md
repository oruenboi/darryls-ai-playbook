---
name: ui-skillset-orchestrator
description: Coordinate UI skills when a request genuinely spans multiple domains or needs explicit handoffs. Route by task, platform, and scope; do not impose the full UI workflow on a focused single-skill change.
---

# UI Skillset Orchestrator

## Objective
Choose the smallest useful set of UI skills and preserve the user's scope. The layers below are responsibilities, not a mandatory sequence.

## Skills Map
1. `ui-foundations`
2. `ui-ux-information-architecture`
3. `ui-design-system-architecture`
4. `ui-frontend-implementation`
5. `ui-data-dashboard`
6. `ui-ai-aware-design`
7. `ui-asset-visual-automation`
8. `ui-tooling-workflow`
9. `ui-performance-optimisation`
10. `ui-strategic-architecture`

## Orchestration Workflow
1. Resolve the target and intent: assessment only, narrow refinement, redesign, or new build. Assessment does not authorize fixes. Refinement preserves identity, factual copy, behavior, and unrelated code.
2. Identify the platform and the surface's purpose: completing a task, persuading a visitor, reading, or experiencing a creative work. Use this to resolve tradeoffs, not to force a visual template.
3. Read existing brief/design evidence and relevant source. Missing PRODUCT.md or DESIGN.md is not permission to invent context, redesign, or create project policies.
4. Select only specialists whose decisions are needed. A spacing repair need not load UX, system governance, assets, or performance. Existing contracts can be reused without recreating them.
5. Hand off the target, preserved constraints, evidence, and acceptance checks. For a small task these can be a few sentences; broader work can use the tooling skill's handoff template.
6. Return findings for assessment-only work. For authorized changes, implement then verify affected states and representative sizes. Batch review and repairs; stop cosmetic iteration once the agreed checks pass, but do not skip required correctness checks.

## Interaction Rules
- Accessibility, accurate content, and task completion outrank visual novelty. A pinned brief and an established system outrank generic aesthetic preferences.
- For Windows-native UI, use appropriate native-platform guidance. If installed, winui-design-review and related WinUI skills can help; they are optional and are not included in this UI package. If unavailable, use project documentation and report the limitation rather than claiming they ran. Do not import web-only controls, font rules, or decorative styling over Fluent conventions.
- For dense tables, load ui-data-dashboard. For AI decisions, preserve ui-ai-aware-design's evidence, uncertainty, approval, and override controls.
- Use existing tools. Do not require Impeccable binaries, hooks, browser injection, automatic downloads, or subagents. Additional tools and delegation need their own applicable authorization.

## Deliverable Format
- Scope and selected skills, with reasons; omit unused layers.
- Relevant findings or changes, their acceptance evidence, and unverified limitations.
- Handoffs and rollback considerations proportional to the change, not a mandatory governance report.

## Resources
- Read `references/ui-skillset-integration-playbook.md` when choosing a cross-domain route or resolving ownership.
- Source attribution for the adapted design workflow is in `references/impeccable-attribution.md`; it is not a runtime dependency.
