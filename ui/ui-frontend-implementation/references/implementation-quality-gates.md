# Frontend Implementation Quality Gates

Use these gates before merging UI code.

## Structure
- Semantic landmarks and form markup are correct.
- Components are typed and props are explicit.
- State ownership is clear and localized where possible.

## Styling
- Token-based styling is used over hard-coded values.
- Responsive behavior is intentional at key breakpoints.
- Focus visibility and keyboard affordance are preserved.

## Reliability
- Loading, error, and empty states are implemented.
- Critical components have test coverage for behavior.
- Bundle impact is checked for large dependencies.

## Adverse content and states

Use representative long names, translated/expanded copy, large or missing values, and text zoom. Check that wrapping or truncation preserves the information needed to act. Where applicable, exercise slow/pending, offline, permission-limited, error, and success states; do not fabricate backend guarantees from a static prototype.

Inspect overlay placement inside clipping or scrolling ancestors. Choose a platform-supported popover/dialog/portal or another appropriate layout only if needed, and verify focus return, dismissal, scroll, and keyboard access. Do not use a modal merely because a local component is easy to build.

## Validate the affected path

Check native semantic controls, names, keyboard activation, visible focus, and updates announced where useful. Inspect the actual computed layout as well as the screenshot; image dimensions alone do not prove the CSS viewport. Use existing test commands and manually exercise changed controls. Label mouse, keyboard, viewport emulation, touch, and assistive-technology evidence separately.

Batch checks at representative supported sizes, make a coherent repair, then confirm. Preserve real regression protection without adding tests of incidental markup or restating implementation. Report unavailable checks rather than introducing unrequested infrastructure. Correctness failures remain blockers even when the cosmetic review budget is exhausted.

Local adaptation, 2026-10-03. See [source attribution](impeccable-attribution.md).
