#!/usr/bin/env python3
"""Create a simple asset manifest with SHA-256 hashes."""

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("asset_dir", help="Directory containing assets")
    parser.add_argument("--out", default="asset-manifest.json", help="Output manifest path")
    parser.add_argument("--force", action="store_true", help="Explicitly replace an existing manifest")
    args = parser.parse_args()

    root = Path(args.asset_dir).resolve()
    if not root.is_dir():
        parser.error("Asset directory must exist.")
    target = Path(args.out).resolve()
    files = []
    for path in root.rglob("*"):
        if not path.is_file() or path.resolve() == target:
            continue
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            parser.error("Asset links outside the selected directory are not supported.")
        files.append(path)
    manifest = []
    for p in sorted(files):
        manifest.append(
            {
                "path": str(p.relative_to(root)).replace("\\", "/"),
                "bytes": p.stat().st_size,
                "sha256": sha256(p),
            }
        )

    try:
        with target.open("w" if args.force else "x", encoding="utf-8") as output:
            output.write(json.dumps({"files": manifest}, indent=2) + "\n")
    except FileExistsError:
        parser.error("Manifest exists; choose another path or explicitly use --force.")
    print(f"Wrote {args.out} with {len(manifest)} entries")


if __name__ == "__main__":
    main()
