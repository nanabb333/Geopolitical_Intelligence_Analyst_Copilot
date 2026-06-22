# Methodology

## Overview

V0.1 of Geopolitical Intelligence Analyst Copilot converts a user-described geopolitical event into a historical analog brief using local CSV inputs only. The workflow is deterministic and auditable:

```text
User description
  -> Event classification
  -> Historical analog retrieval
  -> Market reaction comparison
  -> Scenario pathway generation
  -> Executive brief
```

## Event Classification

`src/classify_event.py` uses transparent keyword and phrase rules to assign:

- `event_type`
- `policy_subtype`
- `country_or_region`
- `sector`
- `threat_signal`
- `opportunity_signal`
- `state_support`

The classifier also records matched terms and caveats when no deterministic rule matches. It is intentionally simple in V0.1 so the classification basis is visible to an analyst.

## Historical Analog Retrieval

`src/retrieve_analogs.py` loads `data/events.csv`, classifies the user query, and ranks historical events using deterministic weighted similarity.

The current V0.1 score includes:

| Feature | Weight |
| --- | ---: |
| event type match | 3.0 |
| policy subtype match | 2.5 |
| sector match | 2.0 |
| country or region match | 1.5 |
| threat signal alignment | 1.0 |
| opportunity signal alignment | 1.0 |
| state support alignment | 1.0 |
| token overlap | up to 2.0 |

Scores are normalized to a 0-100 scale for readability. They are retrieval scores only and must not be interpreted as probabilities or predictions.

## Market Reaction Comparison

`src/compare_market_reactions.py` summarizes observed event-study rows from `data/event_firm_returns.csv`.

The module reports averages for available return and abnormal return windows, including:

- event-day return
- event-day abnormal returns
- CAR windows around the event
- data quality flags
- return record coverage

These are historical observations for retrieved analogs. They are not estimates of future returns.

## Scenario Pathway Generation

`src/generate_pathways.py` creates deterministic qualitative pathway frames from event classification and analog metadata.

Pathways may include:

- restriction pathway
- state-support pathway
- reallocation pathway
- anticipation pathway
- ambiguous-policy pathway

Each pathway includes:

- historical basis
- monitoring focus
- interpretation limit

The pathways are decision-support frames, not forecasts.

## Brief Generation

`src/generate_brief.py` assembles the classification, analogs, market reaction summaries, pathways, risks, and executive summary into a Markdown brief.

`src/run_scenario.py` is the main copilot CLI for running the complete analyst workflow.

## Interpretation Limits

- Keyword classification can miss subtle geopolitical framing.
- Sparse return data can produce shallow market-reaction sections.
- Similarity depends on coded event fields and available historical coverage.
- Anticipated events may show muted event-window reactions.
- Confounding macro, earnings, or policy news may affect observed reactions.
- Historical analogs support structured comparison; they do not predict outcomes.
