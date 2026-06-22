# Product Specification: V0.1

## Product Goal

Build a lightweight Geopolitical Intelligence Analyst Copilot that converts a user-described event into a structured historical analog brief using the existing event-study database.

## User

Primary V0.1 users are researchers, analysts, and strategy teams who need to translate a geopolitical event narrative into a disciplined historical comparison and reusable Markdown memo.

## User Workflow

```text
User Event Description
  -> Event Classification
  -> Historical Analog Retrieval
  -> Scenario Brief Generation
```

## Required Inputs

### `data/events.csv`

Coded event database containing event metadata such as:

- `event_id`
- `event_date`
- `event_name`
- `event_type`
- `policy_subtype`
- `country_or_region`
- `sector`
- strategic and signal intensity fields

### `data/event_firm_returns.csv`

Event-study return data containing:

- `event_id`
- `asset_id`
- exposure role fields
- event-day returns
- abnormal returns
- cumulative abnormal returns across event windows
- data quality flags

## Required Outputs

### 1. Most Similar Historical Events

Ranked list of retrieved analog events with similarity scores and matched rationale.

### 2. Historical Market Reactions

Summary of event-day and CAR windows from available event-firm return records.

### 3. Potential Future Pathways

Narrative pathways derived from historical analog patterns. These are not forecasts and include no probability estimates.

### 4. Key Risks and Uncertainties

Data limitations, coding ambiguity, confound flags, anticipation risk, coverage gaps, and analog mismatch risks.

### 5. Executive Brief

Concise intelligence-style Markdown brief suitable for research and strategy review.

## Explicit Non-Goals

- Forecasting future prices or market levels
- Estimating probabilities
- Recommending investments, trades, hedges, or portfolio changes
- Using external APIs
- Real-time news ingestion
- Automated data enrichment
- Model-driven generation

## V0.1 Acceptance Criteria

- Runs locally with Python standard library only
- Reads only local CSV inputs
- Classifies an event description deterministically
- Retrieves analogs deterministically
- Produces a Markdown brief
- Clearly labels all outputs as historical analog analysis rather than forecast or investment advice

## Future Versions

Future versions may add richer ontologies, analyst review workflows, confidence diagnostics, vector retrieval, or API deployment. Those are intentionally out of scope for V0.1.
