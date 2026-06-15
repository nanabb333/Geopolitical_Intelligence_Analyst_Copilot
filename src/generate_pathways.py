#!/usr/bin/env python3
"""Deterministic scenario pathway generation.

Pathways are qualitative monitoring frames derived from historical analog
metadata. They are not forecasts and do not include probabilities.
"""

from __future__ import annotations

from typing import Any


def _score_value(event: dict[str, str], field: str) -> float:
    try:
        return float(event.get(field) or 0)
    except ValueError:
        return 0.0


def generate_pathways(classification: Any, analogs: list[Any]) -> list[dict[str, str]]:
    """Generate conservative pathway narratives from classification and analogs."""
    has_threat = classification.threat_signal > 0 or any(_score_value(analog.event, "threat_signal") >= 2 for analog in analogs)
    has_support = classification.state_support > 0 or any(_score_value(analog.event, "state_support") >= 2 for analog in analogs)
    has_substitution = any(_score_value(analog.event, "substitution_reallocation") >= 2 for analog in analogs)
    has_high_anticipation = any(_score_value(analog.event, "anticipation_level") >= 2 for analog in analogs)

    pathways: list[dict[str, str]] = []
    if has_threat:
        pathways.append(
            {
                "name": "Restriction pathway",
                "historical_basis": "Retrieved analogs include export controls, restrictions, or other threat-coded events.",
                "monitoring_focus": "Distinguish directly constrained firms from substitute beneficiaries and supply-chain rerouting effects.",
                "interpretation_limit": "Historical reactions may reflect event-specific exposure and cannot be projected forward.",
            }
        )
    if has_support:
        pathways.append(
            {
                "name": "State-support pathway",
                "historical_basis": "Retrieved analogs include subsidy, award, or industrial-policy support mechanisms.",
                "monitoring_focus": "Track support materiality, beneficiary visibility, implementation credibility, and whether support was anticipated.",
                "interpretation_limit": "Support announcements can be interpreted as both opportunity and evidence of strategic vulnerability.",
            }
        )
    if has_substitution:
        pathways.append(
            {
                "name": "Reallocation pathway",
                "historical_basis": "Analog coding indicates possible substitution or strategic supply-chain reallocation.",
                "monitoring_focus": "Review exposure roles, sector positioning, jurisdictional constraints, and second-order beneficiaries.",
                "interpretation_limit": "Substitution effects are heterogeneous and may not appear in short event windows.",
            }
        )
    if has_high_anticipation:
        pathways.append(
            {
                "name": "Anticipation pathway",
                "historical_basis": "Some analogs were partly anticipated before the coded event date.",
                "monitoring_focus": "Separate policy surprise from implementation detail and prior market incorporation.",
                "interpretation_limit": "Muted observed reactions may reflect prior anticipation rather than low strategic importance.",
            }
        )
    if not pathways:
        pathways.append(
            {
                "name": "Ambiguous-policy pathway",
                "historical_basis": "Available analogs do not strongly identify a single coded mechanism.",
                "monitoring_focus": "Prioritize analyst review of classification fit, sector mapping, and source context.",
                "interpretation_limit": "Low similarity or sparse records weaken historical comparison value.",
            }
        )
    return pathways
