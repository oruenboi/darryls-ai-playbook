#!/usr/bin/env python3
"""Summarize key Lighthouse metrics from one or two report files."""

import argparse
import csv
import json
import math
import sys
from pathlib import Path

METRICS = {
    "first-contentful-paint": "FCP",
    "largest-contentful-paint": "LCP",
    "interactive": "TTI",
    "speed-index": "Speed Index",
    "cumulative-layout-shift": "CLS",
    "total-blocking-time": "TBT",
}
UNITS = {label: ("unitless" if label == "CLS" else "ms") for label in METRICS.values()}


def load_metrics(report: Path) -> dict:
    data = json.loads(report.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("audits"), dict):
        raise ValueError("Expected a Lighthouse report containing an audits object.")
    audits = data.get("audits", {})
    out = {}
    for key, label in METRICS.items():
        audit = audits.get(key, {})
        if not isinstance(audit, dict):
            raise ValueError("Invalid audit entry.")
        val = audit.get("numericValue")
        if val is not None and (isinstance(val, bool) or not isinstance(val, (int, float)) or not math.isfinite(val)):
            raise ValueError("Expected finite numeric audit values.")
        out[label] = val
    return out


def fmt(v):
    return "n/a" if v is None else f"{v:.2f}"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("baseline", help="Baseline Lighthouse JSON")
    p.add_argument("--candidate", help="Candidate Lighthouse JSON")
    args = p.parse_args()

    try:
        base = load_metrics(Path(args.baseline))
        cand = load_metrics(Path(args.candidate)) if args.candidate else None
    except (OSError, ValueError):
        p.error("Could not read valid Lighthouse JSON reports with numeric audit values.")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(["Metric", "Unit", "Baseline", "Candidate", "Delta"])
    if not args.candidate:
        for k, v in base.items():
            writer.writerow([k, UNITS[k], fmt(v), "", ""])
        return

    for k in METRICS.values():
        b = base.get(k)
        c = cand.get(k)
        if b is None or c is None:
            d = "n/a"
        else:
            d = f"{(c - b):.2f}"
        writer.writerow([k, UNITS[k], fmt(b), fmt(c), d])


if __name__ == "__main__":
    main()
