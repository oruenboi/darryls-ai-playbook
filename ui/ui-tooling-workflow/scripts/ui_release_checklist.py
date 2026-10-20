#!/usr/bin/env python3
"""Generate a markdown release checklist for UI changes."""

import argparse
from datetime import date
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("feature", help="Feature or release name")
    p.add_argument("--out", default="ui-release-checklist.md", help="Output markdown path")
    p.add_argument("--force", action="store_true", help="Explicitly replace an existing output file")
    args = p.parse_args()

    content = f'''# UI Release Checklist: {args.feature}

Date: {date.today().isoformat()}

## Design and Handoff
- [ ] Existing design documentation covers relevant default, loading, empty, error, and success states
- [ ] Token values and spacing rules documented
- [ ] Responsive behavior documented for key breakpoints

## Engineering
- [ ] Component behavior matches design spec
- [ ] Accessibility checks completed (focus, keyboard, semantics)
- [ ] No unintended design-system overrides

## Testing
- [ ] Unit tests updated
- [ ] Integration paths validated
- [ ] Visual regression checks passed

## Release Notes
- [ ] Breaking changes documented
- [ ] Migration notes added if needed
'''

    try:
        with Path(args.out).open("w" if args.force else "x", encoding="utf-8") as output:
            output.write(content)
    except FileExistsError:
        p.error("Output exists; choose another path or explicitly use --force.")
    print(f"Created {args.out}")


if __name__ == "__main__":
    main()
