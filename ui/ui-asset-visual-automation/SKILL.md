---
name: ui-asset-visual-automation
description: Generate and manage UI visual assets with consistency, automation, and web-performance constraints. Use when creating icon/illustration pipelines, integrating image generation APIs, or enforcing reusable asset standards across products.
---

# UI Asset Visual Automation

## Objective
Build repeatable visual-asset pipelines that balance speed, consistency, and production performance.

## Workflow
1. Define asset style system: grid, stroke, palette, and naming standards.
2. Produce or refine vectors to match tokenized design language.
3. Configure AI-assisted generation prompts with reproducibility controls.
4. Implement API-driven generation and asynchronous batch handling.
5. Transform and optimize outputs (for example SVG or WebP) for web delivery.
6. Apply caching, hashing, and CDN distribution.
7. Enforce governance with accessibility and style compliance checks.

## Production Rules
- Keep asset generation deterministic where possible.
- Remove unnecessary vector metadata and excessive nodes.
- Use token-compatible recoloring (variables or currentColor).
- Prevent duplicate generation via naming and hash strategy.
- Validate contrast and non-color-only meaning in iconography.

## Deliverable Format
- Asset standard spec and style checklist.
- Generation and post-processing workflow.
- Versioning and traceability plan.
- Delivery performance notes and cache strategy.

## Layer Position
Layer 7 (Asset Generation and Visual Automation). Support interface consistency at scale.
## Resources
- Read `references/asset-pipeline-standards.md` before generating or approving asset batches.
- Run `scripts/asset_manifest.py` to generate hash-based manifests for versioning and cache-safe delivery.
- The helper uses Python 3.10+ and excludes its own output. It refuses existing output unless `--force` is explicitly chosen; review the exact output path before replacement. Use a selected public asset directory, not a workspace containing secrets.
