---
name: ui-frontend-implementation
description: Translate UI and design systems into maintainable frontend code using semantic HTML, modern CSS, React, TypeScript, and component-library integration. Use when building production UI, implementing components, or improving code quality and maintainability.
---

# UI Frontend Implementation

## Objective
Convert design-system intent into production-grade code that is accessible, scalable, and performance-aware.

## Workflow
1. Establish semantic HTML structure and accessible interaction markup.
2. Implement layout using scalable CSS architecture with responsive behavior.
3. Build components in the project's existing framework; use typed React components when React is already the chosen stack.
4. Integrate system tokens through CSS variables or utility theming.
5. Connect library primitives (for example Radix, shadcn, table tooling) without breaking system standards.
6. Verify behavior, accessibility, and maintainability before merge.

## Implementation Rules
- Preserve identity, content, and behavior outside the requested change. An assessment request does not authorize implementation.
- Keep component logic and visual concerns modular.
- Prefer composition over inheritance.
- Type props and state to reduce runtime ambiguity.
- Prevent style drift by enforcing token-based styling.
- Avoid heavy dependencies when native platform features are sufficient.

## Deliverable Format
- Implementation plan by component and dependency.
- Code-level decisions for state, composition, and styling.
- Accessibility and responsive verification notes.
- Known tradeoffs and follow-up tasks.

## Layer Position
Reuse established system contracts; a small fix does not require creating a design system first.
## Resources
- Read `references/implementation-quality-gates.md` before merge review.
- Use `scripts/component_scaffold.py` for new modules only when its output matches the chosen framework and project conventions.
- The scaffold validates component names and refuses existing output unless `--force` is explicitly chosen. Inspect the target before replacement. The generated semantic element and accessible name are starting points, not proof of accessibility.
