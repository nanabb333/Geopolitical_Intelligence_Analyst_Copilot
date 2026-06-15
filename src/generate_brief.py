#!/usr/bin/env python3
"""Generate a deterministic historical analog scenario brief."""

from __future__ import annotations

import argparse
from dataclasses import asdict
from pathlib import Path

try:
    from compare_market_reactions import summarize_analog_reaction_context
    from generate_pathways import generate_pathways
    from retrieve_analogs import AnalogResult, DEFAULT_EVENTS_PATH, DEFAULT_RETURNS_PATH, retrieve_analogs
except ImportError:  # pragma: no cover - supports package-style imports
    from .compare_market_reactions import summarize_analog_reaction_context
    from .generate_pathways import generate_pathways
    from .retrieve_analogs import AnalogResult, DEFAULT_EVENTS_PATH, DEFAULT_RETURNS_PATH, retrieve_analogs


def pct(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    return f"{value * 100:.2f}%"


def _format_reaction_summary(analog: AnalogResult) -> list[str]:
    averages = analog.reaction_summary.get("averages", {})
    if not averages:
        return ["- No event-firm return rows are available for this analog in `event_firm_returns.csv`."]

    lines = [f"- Return records: {analog.reaction_summary.get('record_count', 0)}"]
    for metric in [
        "event_day_return",
        "ar_market_event_day",
        "ar_sector_event_day",
        "car_market_m1_p1",
        "car_sector_m1_p1",
        "car_market_m3_p3",
        "car_sector_m3_p3",
        "car_market_m7_p7",
        "car_sector_m7_p7",
    ]:
        if metric in averages:
            lines.append(f"- Average `{metric}`: {pct(averages[metric])}")
    flags = analog.reaction_summary.get("data_quality_flags", [])
    if flags:
        lines.append(f"- Data quality flags: {', '.join(flags)}")
    return lines


def generate_brief(
    description: str,
    top_k: int = 5,
    events_path: Path = DEFAULT_EVENTS_PATH,
    returns_path: Path = DEFAULT_RETURNS_PATH,
) -> str:
    classification, analogs = retrieve_analogs(description, events_path, returns_path, top_k)
    classification_dict = asdict(classification)
    reaction_context = summarize_analog_reaction_context(analogs)
    pathways = generate_pathways(classification, analogs)

    lines = [
        "# Historical Analog Scenario Brief",
        "",
        "> V0.1 historical analog analysis only. This brief is not a forecast, probability estimate, trading recommendation, or investment recommendation.",
        "",
        "## User Event Description",
        "",
        description,
        "",
        "## Event Classification",
        "",
    ]
    for key in ["event_type", "policy_subtype", "country_or_region", "sector", "threat_signal", "opportunity_signal", "state_support"]:
        lines.append(f"- `{key}`: {classification_dict[key]}")
    if classification.caveats:
        lines.append("- Classification caveats: " + "; ".join(classification.caveats))

    lines.extend(["", "## Most Similar Historical Events", ""])
    for index, analog in enumerate(analogs, start=1):
        event = analog.event
        rationale = "; ".join(analog.score_rationale) if analog.score_rationale else "No strong deterministic match rationale."
        lines.extend(
            [
                f"### {index}. {event.get('event_name', 'Unknown event')}",
                "",
                f"- Event ID: `{event.get('event_id', '')}`",
                f"- Date: {event.get('event_date', '')}",
                f"- Similarity score: {analog.similarity_score:.2f}/100",
                f"- Type/subtype: `{event.get('event_type', '')}` / `{event.get('policy_subtype', '')}`",
                f"- Country or region: `{event.get('country_or_region', '')}`",
                f"- Sector: `{event.get('sector', '')}`",
                f"- Rationale: {rationale}",
                "",
            ]
        )

    lines.extend(["## Historical Market Reactions", ""])
    lines.extend(
        [
            f"- Retrieved analogs: {reaction_context['analog_count']}",
            f"- Analogs with return records: {reaction_context['analogs_with_return_records']}",
            f"- Analogs without return records: {reaction_context['analogs_without_return_records']}",
            "",
        ]
    )
    for analog in analogs:
        lines.extend([f"### {analog.event.get('event_name', 'Unknown event')}", ""])
        lines.extend(_format_reaction_summary(analog))
        lines.append("")

    lines.extend(["## Potential Future Pathways", ""])
    for pathway in pathways:
        lines.append(f"### {pathway['name']}")
        lines.append("")
        lines.append(f"- Historical basis: {pathway['historical_basis']}")
        lines.append(f"- Monitoring focus: {pathway['monitoring_focus']}")
        lines.append(f"- Interpretation limit: {pathway['interpretation_limit']}")
        lines.append("")

    lines.extend(
        [
            "",
            "## Key Risks and Uncertainties",
            "",
            "- Analog similarity is based on coded historical fields and keyword classification, not causal identification.",
            "- Sparse return coverage can overemphasize events with available asset rows.",
            "- Anticipated policy actions may have muted event-window reactions.",
            "- Confounding macro, earnings, or concurrent policy news can weaken interpretation.",
            "- Sector labels may hide meaningful differences across firms, supply-chain positions, and jurisdictions.",
            "",
            "## Executive Brief",
            "",
        ]
    )
    top = analogs[0] if analogs else None
    if top:
        lines.append(
            f"The described event classifies primarily as `{classification.event_type}` / `{classification.policy_subtype}` in `{classification.sector}`. "
            f"The closest retrieved analog is `{top.event.get('event_name')}` with a deterministic similarity score of {top.similarity_score:.2f}/100. "
            "The analog set should be read as a structured historical comparison, with attention to support materiality, threat intensity, anticipation, and data quality flags."
        )
    else:
        lines.append(
            "No historical analogs were retrieved. Review input data coverage and classification rules before using the brief."
        )
    lines.append("")
    lines.append("This V0.1 output supports research and strategic analysis only.")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a historical analog scenario brief.")
    parser.add_argument("description", help="User-described geopolitical event.")
    parser.add_argument("--top-k", type=int, default=5, help="Number of analogs to include.")
    parser.add_argument("--events", type=Path, default=DEFAULT_EVENTS_PATH, help="Path to events.csv.")
    parser.add_argument("--returns", type=Path, default=DEFAULT_RETURNS_PATH, help="Path to event_firm_returns.csv.")
    parser.add_argument("--output", type=Path, help="Optional Markdown output path.")
    args = parser.parse_args()

    brief = generate_brief(args.description, args.top_k, args.events, args.returns)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(brief, encoding="utf-8")
    print(brief)


if __name__ == "__main__":
    main()
