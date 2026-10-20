#!/usr/bin/env python3
"""Generate a basic typed React component scaffold."""

import argparse
import re
from pathlib import Path


def pascal(name: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in name.replace("_", "-").split("-") if part)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Component name, for example user-card")
    parser.add_argument("--out", default=".", help="Output directory")
    parser.add_argument("--force", action="store_true", help="Explicitly replace an existing output file")
    args = parser.parse_args()

    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9]*(?:[-_][A-Za-z0-9]+)*", args.name):
        parser.error("Use an ASCII letter followed by letters/digits, with optional hyphen/underscore-separated words.")
    comp = pascal(args.name)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    file_path = out / f"{comp}.tsx"

    template = f'''import React from "react";

type {comp}Props = {{
  className?: string;
}};

export function {comp}({{ className }}: {comp}Props) {{
  return (
    <section className={{className}} aria-label="{comp}">
      <h2>{comp}</h2>
    </section>
  );
}}
'''
    try:
        with file_path.open("w" if args.force else "x", encoding="utf-8") as output:
            output.write(template)
    except FileExistsError:
        parser.error("Output exists; choose another directory/name or explicitly use --force.")
    print(f"Created {file_path}")


if __name__ == "__main__":
    main()
