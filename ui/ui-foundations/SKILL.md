---
name: ui-foundations
description: Build and review baseline UI quality for layout, typography, color, interaction states, accessibility, and responsive behavior. Use when starting a new UI, auditing an existing screen, or fixing visual/interaction inconsistency before higher-level architecture work.
---

# UI Foundations

## Objective
Establish non-negotiable baseline quality before advanced UX, component architecture, or implementation decisions.

## Workflow
For a review request, report findings without edits. For refinement, preserve the established identity and behavior. Read the full `references/foundation-audit-checklist.md` for audits and polish; use only its relevant checks for a small fix.

1. Audit visual structure: alignment, spacing, hierarchy, and typography scale.
2. Validate interaction states: default, hover, active, focus, disabled, loading, error, success.
3. Validate accessibility baseline: contrast, semantic structure, keyboard flow, and focus visibility.
4. Validate responsive behavior: mobile-first layout, breakpoint reflow, touch-target sizing.
5. Produce a remediation list grouped by severity and implementation effort.

## Foundation Checklist
- Use the existing spacing system and meaningful grouping; do not force a new 4px/8px grid onto a coherent design.
- Use semantic color roles for success, warning, and error; avoid color-only communication.
- Keep readable type hierarchy with consistent line-height and spacing.
- Ensure error, empty, and loading states are explicit and actionable.
- Ensure keyboard navigation is logical and free from traps.
- Keep motion supportive and optional; respect reduced-motion preferences.

## Deliverable Format
- Prioritized findings by area: Visual, Interaction, Accessibility, Responsive. Each needs a location, observed evidence, user impact, and concrete next action. Separate defects from design judgments; do not invent an aggregate score.
- Critical issues blocking release.
- Priority fixes for the next implementation cycle.
- Optional enhancements after baseline compliance.

## Layer Position
Foundational checks support relevant tasks; they do not require a separate full audit before every UI change.
## Resources
- Read `references/foundation-audit-checklist.md` when running baseline audits or release readiness checks.
- See `references/impeccable-attribution.md` for the source of adapted guidance.
