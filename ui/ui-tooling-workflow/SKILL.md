---
name: ui-tooling-workflow
description: Align design and engineering delivery using Figma systems, Storybook documentation, Git workflows, and UI testing strategy. Use when establishing team process, improving handoff quality, or reducing design-to-code drift.
---

# UI Tooling Workflow

## Objective
Create a reliable delivery system that keeps design intent and implementation behavior synchronized.

## Workflow
1. Structure design files and component variants with clear conventions.
2. Maintain component documentation in the project's existing tools; use Storybook when adopted, not as an installation prerequisite.
3. Define branch, PR, and review standards for UI changes.
4. Formalize handoff artifacts: tokens, states, responsive behavior, and edge cases.
5. Add automated checks for unit, integration, and visual regression coverage.
6. Close feedback loops between designers and engineers after each release cycle.

## Collaboration Rules
- Check shipped component behavior against current documentation and examples; resolve drift rather than trusting a filename or stale Storybook story.
- Keep Figma and shipped component states aligned.
- Document breaking changes and migration impact before release.
- Require explicit treatment of loading, empty, and error states.
- Keep commits and changelogs understandable by cross-functional stakeholders.

## Deliverable Format
- Workflow map from design proposal to production release.
- Handoff checklist and acceptance criteria.
- Testing matrix by component criticality.
- Governance rules for updates and regressions.

## Layer Position
Layer 8 (Tooling and Workflow). Enable repeatable multi-team execution.
## Resources
- Read `references/workflow-quality-gates.md` when preparing handoff and release criteria.
- Use `scripts/ui_release_checklist.py` when a durable release checklist is requested or useful; a small fix need not generate one.
- Checklist generation refuses existing output unless `--force` is explicitly chosen. Review the target before replacement; an unchecked checklist is not verification evidence.
- Reuse `assets/handoff-template.md` for consistent design-to-engineering handoff artifacts.
- Read `references/workflow-quality-gates.md` for evidence and proportional verification. Source attribution is in `references/impeccable-attribution.md`.
