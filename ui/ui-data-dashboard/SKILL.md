---
name: ui-data-dashboard
description: Design and implement data-heavy interfaces such as tables, filters, audit logs, and dense dashboards. Use when building analytics/workflow screens, structuring tabular interactions, or improving usability in high-density information environments.
---

# UI Data Dashboard

## Objective
Create scalable, high-clarity data interfaces optimized for decision workflows and operational accuracy.

## Workflow
1. Define information hierarchy and table column priority.
2. Design sorting and filtering interactions with explicit active-state visibility.
3. Choose pagination or infinite-scroll strategy based on task model.
4. Implement inline editing, validation, and conflict handling.
5. Structure status badges and audit trails for unambiguous state tracking.
6. Tune density and loading patterns to preserve readability and speed.

## Interaction Rules
- Treat density and familiar controls as useful when they support the task; do not restyle an operational workbench as a marketing page.
- Preserve context when users navigate, filter, or edit.
- Keep filter logic visible and reversible.
- Prefer skeletons over generic spinners for structured content.
- Use icon plus text for critical statuses.
- Support keyboard-efficient batch operations where relevant.

## Deliverable Format
- Data-screen interaction map.
- Table and filter specification.
- State model for edit, save, error, and conflict paths.
- Performance risks and mitigation notes.

## Layer Position
Layer 5 (Data and Dashboard UI). Extend core implementation patterns for data-dense operations.
## Resources
- Read `references/dashboard-ux-rubric.md` when evaluating table, filter, and audit-log UX quality.
