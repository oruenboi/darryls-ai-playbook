# UI & User Experience

Skills for practitioners building client portals, accounting workbenches and AI-enabled review screens. Choose by the task; the collection is not an eleven-stage process.

## Choosing a skill

Start with [ui-skillset-orchestrator](ui-skillset-orchestrator/) when a request spans several areas. A focused task can use its specialist directly.

| Level | Skill | Use for |
| --- | --- | --- |
| Core | [ui-foundations](ui-foundations/) | Layout, typography, accessibility and responsive reviews |
| Core | [ui-ux-information-architecture](ui-ux-information-architecture/) | Navigation, task flows and content hierarchy |
| Core | [ui-frontend-implementation](ui-frontend-implementation/) | Implementing components in the chosen project stack |
| Core | [ui-data-dashboard](ui-data-dashboard/) | Tables, filters, inline editing and audit logs |
| Core | [ui-ai-aware-design](ui-ai-aware-design/) | Evidence, uncertainty, approval and override controls |
| Advanced | [ui-design-system-architecture](ui-design-system-architecture/) | Shared tokens, components and themes |
| Advanced | [ui-asset-visual-automation](ui-asset-visual-automation/) | Consistent assets and hash manifests |
| Advanced | [ui-tooling-workflow](ui-tooling-workflow/) | Design handoffs, testing and release checks |
| Advanced | [ui-performance-optimisation](ui-performance-optimisation/) | Measured bottlenecks and report comparisons |
| Advanced | [ui-strategic-architecture](ui-strategic-architecture/) | Multi-product governance and migration planning |

Keep each selected skill's whole folder, including supporting references and assets. Figma, Storybook, image-generation services and WinUI skills are conditional tools, not bundled dependencies or required installations. The collection does not install tools, delegate work or authorise external actions.

## Helpers and validation

The four Python helpers use the standard library; Python 3.10+ covers the collection. The component scaffold generates React/TSX, so use it only in an appropriate project. File-generating helpers refuse existing output unless explicitly passed `--force`; review the target before replacement.

The performance helper summarises existing Lighthouse JSON. It does not run Lighthouse, measure a site or report INP. Missing metrics remain unavailable; TTI is included only for legacy reports. Comparable test conditions are still needed to interpret deltas.

Run the synthetic helper checks from the repository root:

```sh
python -B -m unittest discover -s tests -p test_ui_helpers.py -v
```

Publication checks on 2026-10-20: all 11 skill entrypoints passed structural validation and all 8 helper tests passed. These checks do not establish UI quality, accessibility compliance or production behaviour; those require verification in the target product.

## Attribution and changes

Several references adapt selected Impeccable guidance. Their source-revision notes and bundled Apache-2.0 licence files are retained within the affected skills; they are not a runtime dependency. See, for example, [source attribution](ui-foundations/references/impeccable-attribution.md).

Public-package changes on 2026-10-20: safer file generation and component names, self-excluding asset manifests, explicit performance units and input validation, calibrated-confidence guidance, optional WinUI routing, and synthetic regression tests. The installed local skills were not changed by this publication.
