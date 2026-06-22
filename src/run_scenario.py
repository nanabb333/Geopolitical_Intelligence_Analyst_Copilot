#!/usr/bin/env python3
"""Main Analyst Workbench scenario intelligence CLI."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from generate_workbench_report import DEFAULT_EVENTS_PATH, DEFAULT_RETURNS_PATH, generate_workbench_report
except ImportError:  # pragma: no cover - supports package-style imports
    from .generate_workbench_report import DEFAULT_EVENTS_PATH, DEFAULT_RETURNS_PATH, generate_workbench_report


def run_scenario(
    query: str,
    output: Path,
    top_k: int = 5,
    events_path: Path = DEFAULT_EVENTS_PATH,
    returns_path: Path = DEFAULT_RETURNS_PATH,
) -> str:
    """Generate and write a Markdown Analyst Workbench report."""
    brief = generate_workbench_report(query, top_k=top_k, events_path=events_path, returns_path=returns_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(brief, encoding="utf-8")
    return brief


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the deterministic Analyst Workbench workflow.")
    parser.add_argument("--query", required=True, help="User geopolitical question or event description.")
    parser.add_argument("--top-k", type=int, default=5, help="Number of historical analogs to include.")
    parser.add_argument("--output", required=True, type=Path, help="Markdown output path.")
    parser.add_argument("--events", type=Path, default=DEFAULT_EVENTS_PATH, help="Path to events.csv.")
    parser.add_argument("--returns", type=Path, default=DEFAULT_RETURNS_PATH, help="Path to event_firm_returns.csv.")
    args = parser.parse_args()

    brief = run_scenario(args.query, args.output, args.top_k, args.events, args.returns)
    print(brief)


if __name__ == "__main__":
    main()
