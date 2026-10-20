# Token and Component Rubric

Use this rubric when reviewing design-system changes.

## Tokens
- Use semantic token names instead of raw values.
- Keep scale steps consistent across color, type, and spacing.
- Define state tokens for default, hover, focus, disabled, and error.

## Components
- Keep APIs small and predictable.
- Provide variant and size model before release.
- Include accessibility behavior in component definition.

## Governance
- Record breaking changes and migration notes.
- Require usage examples for new components.
- Reject one-off overrides that bypass token usage.

## Classify drift before editing

| Evidence | Appropriate level of repair |
| --- | --- |
| Repeated semantic need with no current representation | Propose a reusable token or variant with examples |
| An existing component already owns the behavior | Reuse it rather than maintain a divergent copy |
| The flow contradicts neighboring product mental models | Return the flow decision to UX before changing styles |
| One incorrect value or incomplete state | Repair locally using the existing contract |

Read the implementation as evidence when formal design documents are absent. Do not create PRODUCT.md, DESIGN.md, a theme engine, or a new component library merely to complete this review. Preserve platform controls and established brand choices; evaluate their suitability rather than imposing universal fonts, corner radii, or palette rules.

Check change reach: affected variants, consumers, states, and themes. Prefer a scoped change over a global token adjustment when only one consumer is wrong. Document intentional exceptions rather than masking them through increasingly broad overrides.

Local adaptation, 2026-10-03. See [source attribution](impeccable-attribution.md).
