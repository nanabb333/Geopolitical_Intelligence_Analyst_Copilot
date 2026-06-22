#!/usr/bin/env python3
"""Generate a deterministic Analyst Workbench Markdown report."""

from __future__ import annotations

import argparse
from dataclasses import asdict
from pathlib import Path
from typing import Any

try:
    from compare_market_reactions import summarize_analog_reaction_context
    from generate_pathways import generate_pathways
    from retrieve_analogs import AnalogResult, DEFAULT_EVENTS_PATH, DEFAULT_RETURNS_PATH, retrieve_analogs
except ImportError:  # pragma: no cover - supports package-style imports
    from .compare_market_reactions import summarize_analog_reaction_context
    from .generate_pathways import generate_pathways
    from .retrieve_analogs import AnalogResult, DEFAULT_EVENTS_PATH, DEFAULT_RETURNS_PATH, retrieve_analogs


SUMMARY_METRICS = [
    "event_day_return",
    "ar_market_event_day",
    "ar_sector_event_day",
    "car_market_m1_p1",
    "car_sector_m1_p1",
    "car_market_m3_p3",
    "car_sector_m3_p3",
    "car_market_m7_p7",
    "car_sector_m7_p7",
]


def pct(value: float | int | None) -> str:
    """Format a decimal return as a percentage for analyst reports."""
    if value is None:
        return "n/a"
    return f"{value * 100:.2f}%"


def _signal_label(value: int) -> str:
    labels = {0: "none", 1: "low", 2: "medium", 3: "high"}
    return f"{value} ({labels.get(value, 'unclassified')})"


def _clean(value: Any, fallback: str = "n/a") -> str:
    if value is None:
        return fallback
    text = str(value).strip()
    return text if text else fallback


def _join_or_na(values: list[str]) -> str:
    cleaned = [_clean(value, "") for value in values if _clean(value, "")]
    return ", ".join(cleaned) if cleaned else "n/a"


def _analog_rationale(analog: AnalogResult) -> str:
    return "; ".join(analog.score_rationale) if analog.score_rationale else "No strong deterministic match rationale."


def _market_direction(averages: dict[str, float]) -> str:
    preferred_metric = None
    for metric in ["car_sector_m1_p1", "ar_sector_event_day", "event_day_return"]:
        if metric in averages:
            preferred_metric = averages[metric]
            break
    if preferred_metric is None:
        return "not available"
    if preferred_metric > 0:
        return "positive observed average"
    if preferred_metric < 0:
        return "negative observed average"
    return "flat observed average"


def _format_metric_list(analog: AnalogResult) -> list[str]:
    averages = analog.reaction_summary.get("averages", {})
    if not averages:
        return ["- Observed market data: no event-firm return rows available."]
    lines = [f"- Return records: {analog.reaction_summary.get('record_count', 0)}"]
    lines.append(f"- Directional read: {_market_direction(averages)}")
    for metric in SUMMARY_METRICS:
        if metric in averages:
            lines.append(f"- Average `{metric}`: {pct(averages[metric])}")
    flags = analog.reaction_summary.get("data_quality_flags", [])
    if flags:
        lines.append(f"- Data quality flags: {_join_or_na(flags)}")
    return lines


def _top_analog_sentence(analogs: list[AnalogResult]) -> str:
    if not analogs:
        return "No historical analogues were retrieved from the local dataset."
    top = analogs[0]
    return (
        f"The closest retrieved analogue is `{top.event.get('event_name')}` "
        f"({top.event.get('event_date')}) with a deterministic similarity score of "
        f"{top.similarity_score:.2f}/100."
    )


def generate_workbench_report(
    description: str,
    top_k: int = 5,
    events_path: Path = DEFAULT_EVENTS_PATH,
    returns_path: Path = DEFAULT_RETURNS_PATH,
) -> str:
    """Generate the Analyst Workbench Markdown report from local deterministic inputs."""
    classification, analogs = retrieve_analogs(description, events_path, returns_path, top_k)
    classification_dict = asdict(classification)
    reaction_context = summarize_analog_reaction_context(analogs)
    pathways = generate_pathways(classification, analogs)
    caveats = classification.caveats or ["No classification caveats produced by deterministic rules."]

    lines = [
        "# Analyst Workbench Report",
        "",
        "> Deterministic historical-analogue analysis only. This report is not a forecast, probability estimate, trading signal, or investment recommendation.",
        "",
        "## Workflow Audit",
        "",
        "- Current workflow preserved: question -> classification -> retrieval -> brief.",
        "- Expanded workbench workflow: question -> scenario classification -> historical analogue retrieval -> market reaction comparison -> observed pathway generation -> executive memo -> export package.",
        "- Classification and retrieval reuse the existing deterministic modules without external APIs, LLM calls, dashboards, real-time monitoring, forecasts, or recommendations.",
        "",
        "## Analyst Query",
        "",
        description,
        "",
        "## A. Scenario Classification",
        "",
        "| Field | Workbench Output |",
        "| --- | --- |",
    ]
    for key in ["event_type", "policy_subtype", "country_or_region", "sector"]:
        lines.append(f"| `{key}` | `{classification_dict[key]}` |")
    lines.extend(
        [
            f"| `threat_signal` | {_signal_label(classification.threat_signal)} |",
            f"| `opportunity_signal` | {_signal_label(classification.opportunity_signal)} |",
            f"| `state_support` | {_signal_label(classification.state_support)} |",
            "",
            "Matched deterministic terms:",
            "",
        ]
    )
    for key, terms in classification.matched_terms.items():
        lines.append(f"- `{key}`: {_join_or_na(terms)}")
    lines.extend(["", "Classification caveats:", ""])
    for caveat in caveats:
        lines.append(f"- {caveat}")

    lines.extend(["", "## B. Historical Analogues", ""])
    if not analogs:
        lines.append("No analogues were retrieved. Review local input data and deterministic classification coverage.")
    for index, analog in enumerate(analogs, start=1):
        event = analog.event
        lines.extend(
            [
                f"### {index}. {event.get('event_name', 'Unknown event')}",
                "",
                f"- Event ID: `{event.get('event_id', '')}`",
                f"- Date: {_clean(event.get('event_date'))}",
                f"- Similarity score: {analog.similarity_score:.2f}/100",
                f"- Type/subtype: `{event.get('event_type', '')}` / `{event.get('policy_subtype', '')}`",
                f"- Country or region: `{event.get('country_or_region', '')}`",
                f"- Sector: `{event.get('sector', '')}`",
                f"- Strategic importance coding: {_clean(event.get('strategic_importance'))}",
                f"- Support materiality: {_clean(event.get('support_materiality'))}",
                f"- Anticipation level: {_clean(event.get('anticipation_level'))}",
                f"- Retrieval rationale: {_analog_rationale(analog)}",
                f"- Coding note: {_clean(event.get('coding_notes'))}",
                "",
            ]
        )

    lines.extend(
        [
            "## C. Market Reaction Comparison",
            "",
            f"- Retrieved analogues: {reaction_context['analog_count']}",
            f"- Analogues with return records: {reaction_context['analogs_with_return_records']}",
            f"- Analogues without return records: {reaction_context['analogs_without_return_records']}",
            f"- Cross-analogue data quality flags: {_join_or_na(reaction_context.get('data_quality_flags', []))}",
            "",
        ]
    )
    for analog in analogs:
        lines.extend([f"### {analog.event.get('event_name', 'Unknown event')}", ""])
        lines.extend(_format_metric_list(analog))
        lines.append("")

    lines.extend(["## D. Observed Pathways", ""])
    for pathway in pathways:
        lines.extend(
            [
                f"### {pathway['name']}",
                "",
                f"- Historical basis: {pathway['historical_basis']}",
                f"- Analyst monitoring focus: {pathway['monitoring_focus']}",
                f"- Interpretation limit: {pathway['interpretation_limit']}",
                "",
            ]
        )

    lines.extend(["## E. Executive Memo", ""])
    lines.extend(
        [
            "### Bottom Line",
            "",
            (
                f"The submitted scenario classifies as `{classification.event_type}` / `{classification.policy_subtype}` "
                f"for `{classification.sector}` in `{classification.country_or_region}`. "
                f"{_top_analog_sentence(analogs)}"
            ),
            "",
            "### Implications for Review",
            "",
            "- Use the analogue set to structure analyst discussion around mechanism fit, support materiality, threat intensity, anticipation, and data quality.",
            "- Treat observed market reactions as historical context from coded event windows, not as a projection for the submitted scenario.",
            "- Escalate classification caveats, sparse return coverage, and confounded event windows before relying on the comparison in committee discussion.",
            "",
            "### Key Uncertainties",
            "",
            "- Keyword classification may miss nuance in scenario wording or jurisdictional framing.",
            "- Event-window reactions can be distorted by anticipation, earnings, macro news, or overlapping policy announcements.",
            "- Sector-level labels may hide firm-specific exposure, supply-chain position, and beneficiary differences.",
            "- The local dataset may not contain enough direct analogues for rare or cross-sector events.",
            "",
            "### Export Package",
            "",
            "- Primary artifact: structured Markdown Analyst Workbench report.",
            "- Reusable sections: scenario classification, historical analogues, market reaction comparison, observed pathways, and executive memo.",
            "- Source inputs: local `events.csv`, local `event_firm_returns.csv`, deterministic classification rules, deterministic retrieval weights.",
            "- Intended handoff: portfolio manager, risk committee, strategy team, or analyst review queue.",
            "",
            "This output supports research, workflow automation, and strategic analysis only.",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a deterministic Analyst Workbench report.")
    parser.add_argument("description", help="User-described geopolitical event.")
    parser.add_argument("--top-k", type=int, default=5, help="Number of historical analogues to include.")
    parser.add_argument("--events", type=Path, default=DEFAULT_EVENTS_PATH, help="Path to events.csv.")
    parser.add_argument("--returns", type=Path, default=DEFAULT_RETURNS_PATH, help="Path to event_firm_returns.csv.")
    parser.add_argument("--output", type=Path, help="Optional Markdown output path.")
    args = parser.parse_args()

    report = generate_workbench_report(args.description, args.top_k, args.events, args.returns)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
