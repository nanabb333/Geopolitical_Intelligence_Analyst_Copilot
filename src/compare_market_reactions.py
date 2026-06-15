#!/usr/bin/env python3
"""Historical market reaction summaries for scenario analogs.

This module reports observed event-study outcomes from local CSV files. It does
not forecast, recommend trades, or estimate future returns.
"""

from __future__ import annotations

from statistics import mean
from typing import Any


REACTION_METRICS = [
    "event_day_return",
    "ar_market_event_day",
    "ar_tech_event_day",
    "ar_sector_event_day",
    "car_market_m1_p1",
    "car_tech_m1_p1",
    "car_sector_m1_p1",
    "car_market_m3_p3",
    "car_sector_m3_p3",
    "car_market_m7_p7",
    "car_sector_m7_p7",
]


def numeric(value: str | None) -> float | None:
    """Convert CSV numeric text to float, preserving blanks as missing values."""
    if value in (None, ""):
        return None
    try:
        return float(value)
    except ValueError:
        return None


def summarize_reactions(rows: list[dict[str, str]]) -> dict[str, Any]:
    """Summarize observed historical return rows for one event."""
    summary: dict[str, Any] = {"record_count": len(rows), "averages": {}, "data_quality_flags": []}
    for metric in REACTION_METRICS:
        values = [numeric(row.get(metric)) for row in rows]
        clean_values = [value for value in values if value is not None]
        if clean_values:
            summary["averages"][metric] = mean(clean_values)
    summary["data_quality_flags"] = sorted({row.get("data_quality_flag", "") for row in rows if row.get("data_quality_flag")})
    return summary


def summarize_analog_reaction_context(analogs: list[Any]) -> dict[str, Any]:
    """Return portfolio-style context across retrieved analogs without prediction."""
    analogs_with_returns = [analog for analog in analogs if analog.reaction_summary.get("record_count", 0)]
    clean_flags = sorted(
        {
            flag
            for analog in analogs
            for flag in analog.reaction_summary.get("data_quality_flags", [])
            if flag
        }
    )
    return {
        "analog_count": len(analogs),
        "analogs_with_return_records": len(analogs_with_returns),
        "analogs_without_return_records": len(analogs) - len(analogs_with_returns),
        "data_quality_flags": clean_flags,
    }
