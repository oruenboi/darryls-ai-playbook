---
name: ui-design-system-architecture
description: Build and govern scalable design systems using tokens, reusable components, variants, and contribution standards. Use when creating or refactoring a component system, enabling theming, or reducing UI inconsistency across teams.
---

# UI Design System Architecture

## Objective
Turn UX decisions into reusable primitives, components, and patterns with governance for long-term consistency.

## Workflow
For an existing product, inspect current tokens, components, and neighboring screens before proposing replacements. A local exception does not automatically justify a new shared abstraction or governance exercise.

1. Define token foundations: color, typography, spacing, radius, and elevation.
2. Map semantic token aliases for states and themes.
3. Build component APIs with controlled variants and states.
4. Standardize reusable patterns (forms, tables, modals, navigation).
5. Define contribution, versioning, and deprecation policy.
6. Publish and maintain documentation with examples and constraints.

## System Rules
- Prefer semantic tokens over hard-coded values.
- Keep component APIs predictable and minimal.
- Model complete state coverage, including disabled, loading, and error.
- Avoid one-off overrides that bypass system constraints.
- Track breaking changes and migration guidance.

## Deliverable Format
- Token taxonomy and naming convention.
- Component inventory with variant/state matrix.
- Pattern catalog and usage boundaries.
- Governance model: approvals, changelog, and release process.
- Debt register for drift and refactor priorities.

## Layer Position
Layer 3 (Design Systems and Component Architecture). Feed implementation layer with stable contracts.
## Resources
- Read `references/token-component-rubric.md` when reviewing token/component quality.
- Reuse `assets/component-spec-template.md` for new component proposals.
- Reuse `assets/token-registry-template.json` when defining or migrating token inventories.
