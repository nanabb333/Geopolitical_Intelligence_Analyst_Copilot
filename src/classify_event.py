#!/usr/bin/env python3
"""Deterministic event classification for V0.1."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from typing import Iterable


KEYWORD_RULES = {
    "event_type": {
        "threat_contrast": [
            "export control",
            "export controls",
            "sanction",
            "sanctions",
            "restriction",
            "restricted",
            "blacklist",
            "entity list",
            "license requirement",
            "ban",
        ],
        "broad_policy": [
            "act",
            "law",
            "legislation",
            "industrial policy",
            "strategy",
            "package",
            "program",
        ],
        "support": [
            "award",
            "grant",
            "subsidy",
            "loan",
            "tax credit",
            "funding",
            "incentive",
        ],
    },
    "policy_subtype": {
        "export_control": ["export control", "export controls", "license requirement", "restricted export"],
        "entity_list": ["entity list", "blacklist", "listed entity"],
        "legislation": ["act", "law", "legislation", "bill", "congress"],
        "subsidy_award": ["award", "grant", "funding award", "subsidy", "loan"],
        "fab_investment": ["fab opens", "fabrication investment", "fab investment", "factory opening"],
        "retaliation": ["retaliation", "retaliates", "procurement restriction", "restricts procurement"],
        "industrial_policy": ["industrial policy", "subsidy", "tax credit", "incentive", "domestic capacity"],
    },
    "country_or_region": {
        "US": ["united states", "u.s.", "us ", "america", "american", "congress", "white house", "bis"],
        "China": ["china", "chinese", "prc", "beijing"],
        "EU": ["european union", "eu ", "europe"],
        "Taiwan": ["taiwan", "taiwanese"],
        "Japan": ["japan", "japanese"],
    },
    "sector": {
        "semiconductors": ["semiconductor", "semiconductors", "chip", "chips", "fab", "fabrication"],
        "AI chips": ["ai chip", "ai chips", "advanced computing", "gpu", "accelerator"],
        "memory chips": ["memory chip", "memory chips", "dram", "nand", "ymtc"],
        "defense": ["defense", "missile", "military", "aerospace"],
        "energy": ["energy", "oil", "gas", "battery", "critical minerals"],
    },
}


@dataclass(frozen=True)
class ClassifiedEvent:
    description: str
    event_type: str
    policy_subtype: str
    country_or_region: str
    sector: str
    threat_signal: int
    opportunity_signal: int
    state_support: int
    matched_terms: dict[str, list[str]]
    caveats: list[str]


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", f" {text.lower()} ").strip()


def tokenize(text: str) -> set[str]:
    stopwords = {
        "a",
        "an",
        "and",
        "are",
        "as",
        "for",
        "in",
        "into",
        "new",
        "of",
        "on",
        "or",
        "the",
        "to",
        "with",
    }
    return {token for token in re.findall(r"[a-z0-9]+", text.lower()) if token not in stopwords}


def _matches(text: str, phrases: Iterable[str]) -> list[str]:
    found = []
    padded = f" {text} "
    for phrase in phrases:
        pattern = phrase.lower()
        if pattern.endswith(" "):
            if pattern in padded:
                found.append(phrase.strip())
        elif pattern in text:
            found.append(phrase)
    return found


def _best_label(text: str, dimension: str, default: str) -> tuple[str, list[str]]:
    candidates = []
    for label, phrases in KEYWORD_RULES[dimension].items():
        found = _matches(text, phrases)
        if found:
            candidates.append((len(found), sum(len(item.split()) for item in found), label, found))
    if not candidates:
        return default, []
    candidates.sort(reverse=True)
    _, _, label, found = candidates[0]
    return label, found


def classify_event(description: str) -> ClassifiedEvent:
    """Classify a free-text geopolitical event description with transparent rules."""
    text = normalize_text(description)
    matched_terms: dict[str, list[str]] = {}

    event_type, matched_terms["event_type"] = _best_label(text, "event_type", "unknown")
    policy_subtype, matched_terms["policy_subtype"] = _best_label(text, "policy_subtype", "unknown")
    country_or_region, matched_terms["country_or_region"] = _best_label(text, "country_or_region", "unknown")
    sector, matched_terms["sector"] = _best_label(text, "sector", "unknown")

    threat_terms = ["export control", "sanction", "restriction", "ban", "blacklist", "entity list", "license"]
    opportunity_terms = ["subsidy", "grant", "award", "tax credit", "incentive", "funding", "support"]
    state_support_terms = ["subsidy", "grant", "award", "tax credit", "loan", "funding", "support", "industrial policy"]

    threat_matches = _matches(text, threat_terms)
    opportunity_matches = _matches(text, opportunity_terms)
    support_matches = _matches(text, state_support_terms)
    matched_terms["threat_signal"] = threat_matches
    matched_terms["opportunity_signal"] = opportunity_matches
    matched_terms["state_support"] = support_matches

    caveats = []
    for dimension, value in [
        ("event_type", event_type),
        ("policy_subtype", policy_subtype),
        ("country_or_region", country_or_region),
        ("sector", sector),
    ]:
        if value == "unknown":
            caveats.append(f"No deterministic {dimension} rule matched.")

    return ClassifiedEvent(
        description=description,
        event_type=event_type,
        policy_subtype=policy_subtype,
        country_or_region=country_or_region,
        sector=sector,
        threat_signal=min(3, len(threat_matches)),
        opportunity_signal=min(3, len(opportunity_matches)),
        state_support=min(3, len(support_matches)),
        matched_terms=matched_terms,
        caveats=caveats,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify a geopolitical event description.")
    parser.add_argument("description", help="User-described geopolitical event.")
    args = parser.parse_args()
    print(json.dumps(asdict(classify_event(args.description)), indent=2))


if __name__ == "__main__":
    main()
