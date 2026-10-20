# Asset Pipeline Standards

Use this reference when producing or automating UI assets.

## Visual Consistency
- Keep icon grid, stroke width, and corner treatment consistent.
- Use token-compatible color strategy.
- Clean vectors to remove unnecessary nodes and metadata.

## Automation Controls
- Version prompts and generation parameters.
- Store run metadata for traceability.
- Enforce deterministic settings where supported.

## Delivery
- Optimize SVG and raster outputs for web.
- Use hashed filenames for cache-safe releases.
- Validate contrast and accessibility constraints.

## Choose assets for the task

Use a coherent icon family and verify stroke weight, optical size, and accessible names. Preserve familiar platform icons when appropriate. Real product imagery or supplied evidence should serve the page's meaning; do not generate decoration simply because an image tool is available.

Respect supplied art direction, reuse/licensing conditions, and provenance. Never imply generated imagery is customer evidence or a factual product screenshot. SVG is appropriate for icons, diagrams, or illustration when it fits the brief; do not impose a blanket format prohibition.

Define responsive dimensions and reserve layout space. Evaluate asset and font costs on the actual target, not appearance alone. Generation and external services require a relevant task and authorized scope, not an automatic pipeline for every UI change.

Local adaptation, 2026-10-03. See [source attribution](impeccable-attribution.md).
