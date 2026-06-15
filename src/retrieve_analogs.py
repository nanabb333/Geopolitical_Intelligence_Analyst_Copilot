#!/usr/bin/env python3
"""Deterministic historical analog retrieval for V0.1."""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

try:
    from compare_market_reactions import numeric, summarize_reactions
    from classify_event import ClassifiedEvent, classify_event, tokenize
except ImportError:  # pragma: no cover - supports package-style imports
    from .compare_market_reactions import numeric, summarize_reactions
    from .classify_event import ClassifiedEvent, classify_event, tokenize


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVENTS_PATH = REPO_ROOT / "data" / "events.csv"
DEFAULT_RETURNS_PATH = REPO_ROOT / "data" / "event_firm_returns.csv"

WEIGHTS = {
    "event_type": 3.0,
    "policy_subtype": 2.5,
    "sector": 2.0,
    "country_or_region": 1.5,
    "threat_signal": 1.0,
    "opportunity_signal": 1.0,
    "state_support": 1.0,
    "token_overlap": 2.0,
}
MAX_SCORE = sum(WEIGHTS.values())


@dataclass(frozen=True)
class AnalogResult:
    event: dict[str, str]
    similarity_score: float
    score_breakdown: dict[str, float]
    score_rationale: list[str]
    market_reactions: list[dict[str, str]]
    reaction_summary: dict[str, Any]


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _signal_alignment(classified_value: int, event_value: str) -> float:
    event_num = numeric(event_value)
    if event_num is None:
        return 0.0
    if classified_value == 0 and event_num == 0:
        return 1.0
    distance = abs(classified_value - event_num)
    return max(0.0, 1.0 - (distance / 3.0))


def _token_overlap_score(classification: ClassifiedEvent, event: dict[str, str]) -> float:
    query_tokens = tokenize(classification.description)
    event_text = " ".join(
        [
            event.get("event_name", ""),
            event.get("event_type", ""),
            event.get("policy_subtype", ""),
            event.get("country_or_region", ""),
            event.get("sector", ""),
            event.get("coding_notes", ""),
        ]
    )
    event_tokens = tokenize(event_text)
    if not query_tokens or not event_tokens:
        return 0.0
    return len(query_tokens & event_tokens) / len(query_tokens | event_tokens)


def _field_match(classified_value: str, event_value: str) -> float:
    if classified_value == "unknown" or not event_value:
        return 0.0
    left = classified_value.lower()
    right = event_value.lower()
    if left == right:
        return 1.0
    separators = ["/", ";", ","]
    parts = [right]
    for separator in separators:
        parts = [piece for part in parts for piece in part.split(separator)]
    if left in {part.strip() for part in parts}:
        return 1.0
    if left in right or right in left:
        return 0.75
    return 0.0


def score_event(classification: ClassifiedEvent, event: dict[str, str]) -> tuple[float, dict[str, float], list[str]]:
    breakdown = {key: 0.0 for key in WEIGHTS}
    rationale: list[str] = []

    for field in ["event_type", "policy_subtype", "sector", "country_or_region"]:
        classified_value = getattr(classification, field)
        event_value = event.get(field, "")
        match_strength = _field_match(classified_value, event_value)
        if match_strength:
            breakdown[field] = WEIGHTS[field] * match_strength
            match_label = "matched" if match_strength == 1.0 else "partially matched"
            rationale.append(f"{field} {match_label}: {classified_value} vs {event_value}")

    for field in ["threat_signal", "opportunity_signal", "state_support"]:
        alignment = _signal_alignment(getattr(classification, field), event.get(field, ""))
        breakdown[field] = WEIGHTS[field] * alignment
        if alignment >= 0.67:
            rationale.append(f"{field} aligned with historical coding")

    overlap = _token_overlap_score(classification, event)
    breakdown["token_overlap"] = WEIGHTS["token_overlap"] * overlap
    if overlap > 0:
        rationale.append(f"token overlap contributed {overlap:.2f}")

    raw_score = sum(breakdown.values())
    normalized = round((raw_score / MAX_SCORE) * 100, 2)
    return normalized, breakdown, rationale


def retrieve_analogs(
    description: str,
    events_path: Path = DEFAULT_EVENTS_PATH,
    returns_path: Path = DEFAULT_RETURNS_PATH,
    top_k: int = 5,
) -> tuple[ClassifiedEvent, list[AnalogResult]]:
    classification = classify_event(description)
    events = load_csv(events_path)
    returns = load_csv(returns_path)
    returns_by_event: dict[str, list[dict[str, str]]] = {}
    for row in returns:
        returns_by_event.setdefault(row["event_id"], []).append(row)

    results = []
    for event in events:
        score, breakdown, rationale = score_event(classification, event)
        market_reactions = returns_by_event.get(event["event_id"], [])
        results.append(
            AnalogResult(
                event=event,
                similarity_score=score,
                score_breakdown={key: round(value, 4) for key, value in breakdown.items()},
                score_rationale=rationale,
                market_reactions=market_reactions,
                reaction_summary=summarize_reactions(market_reactions),
            )
        )

    results.sort(key=lambda item: (-item.similarity_score, item.event.get("event_date", ""), item.event.get("event_id", "")))
    return classification, results[:top_k]


def main() -> None:
    parser = argparse.ArgumentParser(description="Retrieve deterministic historical analogs.")
    parser.add_argument("description", help="User-described geopolitical event.")
    parser.add_argument("--top-k", type=int, default=5, help="Number of analogs to return.")
    parser.add_argument("--events", type=Path, default=DEFAULT_EVENTS_PATH, help="Path to events.csv.")
    parser.add_argument("--returns", type=Path, default=DEFAULT_RETURNS_PATH, help="Path to event_firm_returns.csv.")
    args = parser.parse_args()

    classification, analogs = retrieve_analogs(args.description, args.events, args.returns, args.top_k)
    payload = {
        "classification": asdict(classification),
        "analogs": [asdict(analog) for analog in analogs],
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
