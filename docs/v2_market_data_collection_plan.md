# V2 Market Data Collection Plan

## Executive Summary

The US-China Strategic Competition pilot dataset needs a market reaction data layer before it can support V2 market comparison. The next step is not integration or feature development; it is disciplined market-data collection design.

This plan defines how to collect event-linked market rows without inventing reactions, overstating evidence, or adding forecasts.

Planning references:

- [V2 Market Mapping Plan](v2_market_mapping_plan.md)
- [V2 Pilot Event Selection](v2_pilot_event_selection.md)

## Market Data Objective

The objective is to create a reproducible market dataset that links selected V2 pilot events to observed historical asset, sector, index, or commodity returns.

The dataset should support descriptive historical comparison only:

- what happened around prior coded events;
- which assets or sectors had observable event-window data;
- where data is missing or confounded;
- how much confidence analysts should place in the comparison.

## Priority Event Categories

Prioritize categories that are both strategically important and easier to map to market proxies:

1. AI Chip Restrictions.
2. Export Controls.
3. Sanctions / Entity List.
4. Critical Minerals.
5. Strategic Investment Screening.
6. Supply Chain Relocation.
7. Industrial Policy.
8. Taiwan-related tension as one subcategory.

Do not prioritize broad military or Taiwan scenarios until event-date and exposure mapping rules are mature.

## Suggested Market Proxies

Suggested proxy types:

- named target or beneficiary equities where source evidence identifies firms;
- semiconductor sector ETFs or indexes;
- broad market indexes for geography;
- technology or AI infrastructure indexes where relevant;
- critical-minerals, battery, or materials proxies for minerals events;
- regional equity indexes for Taiwan-related tension;
- logistics or shipping indexes only after shipping-specific events are added.

Proxy selection must be documented before return calculation. Do not select proxies based on observed price movement.

## Data Collection Sequence

1. Select 5-7 pilot events for initial market-data review.
2. Confirm event dates and event-date confidence.
3. Define exposure roles for each event.
4. Select assets and benchmarks before calculating returns.
5. Pull or calculate historical prices from a documented source.
6. Calculate `t0`, `m1_p1`, `m3_p3`, and `m7_p7` windows where data allows.
7. Record raw return, benchmark return, abnormal return, data source, and calculation notes.
8. Flag earnings, macro, policy, liquidity, or missing-data conflicts.
9. Review rows before using them in any report.

## Minimum Viable Market Dataset

Minimum viable V2 market dataset:

- 5-7 pilot events.
- At least 2 exposure roles per event where feasible.
- At least one benchmark per row.
- Event-day and short CAR windows.
- Clear source and calculation notes.
- Explicit limitations for every row.
- No fake or placeholder returns.

Recommended first batch:

- one AI chip restriction event;
- one export-control event;
- one entity-list or procurement-restriction event;
- one critical-minerals event;
- one strategic investment-screening event;
- one industrial-policy event;
- one supply-chain relocation event.

The current representative selection is documented in [V2 Pilot Event Selection](v2_pilot_event_selection.md), with proxy and benchmark planning details in [V2 Market Mapping Plan](v2_market_mapping_plan.md).

## Quality Control Rules

- Every row must match a valid V2 event ID.
- Every row must have a documented data source.
- Every row must include calculation notes.
- Benchmark choice must be justified before return calculation.
- Missing returns must stay blank.
- Confounded windows must be flagged.
- Duplicate event-asset-window rows must be reviewed.
- Rows should be marked `low` confidence when event timing or proxy mapping is uncertain.

## Risks and Limitations

- Some events affect sectors indirectly and may not map cleanly to tradable proxies.
- Multi-day policy events may create event-date ambiguity.
- Single-firm reactions can be confounded by earnings or company news.
- Critical-minerals proxies may be imperfect.
- Taiwan-related tension may affect broad risk sentiment rather than a narrow asset.
- Sparse market data can weaken report quality if not disclosed.

## Recommended Next Sprint

Recommended next sprint: V2 Market Data Template Validation.

Scope:

1. Review the selected 5-7 events in [V2 Pilot Event Selection](v2_pilot_event_selection.md).
2. Confirm asset and benchmark proxies from [V2 Market Mapping Plan](v2_market_mapping_plan.md).
3. Validate event-date and trading-calendar conventions.
4. Populate a small market-data sample only with real sourced returns.
5. Add CSV integrity tests for populated rows.

Do not integrate V2 into the workbench until the sample market data passes review.
