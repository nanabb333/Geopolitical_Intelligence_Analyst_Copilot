# Architecture

Geopolitical Intelligence Analyst Copilot is a deterministic analyst workflow layer for scenario intake, classification, historical analog retrieval, market-reaction context, and Markdown memo generation.

## Design Principles

- Deterministic before generative
- Local files before external services
- Transparent scoring before opaque ranking
- Historical analogs before future claims
- Research auditability before workflow automation
- Analyst productivity before product sprawl

## Components

```text
src/classify_event.py
  - Converts a free-text event description into a structured event profile.
  - Uses keyword and phrase rules.
  - Produces transparent matched evidence.

src/retrieve_analogs.py
  - Loads events.csv and event_firm_returns.csv.
  - Scores historical events against the classified profile.
  - Joins available market reaction records.
  - Returns ranked analogs and score explanations.

src/generate_brief.py
  - Orchestrates classification and retrieval.
  - Formats a Markdown intelligence brief.
  - Writes to stdout or results/*.md.
```

## Data Flow

```text
User description
  -> classify_event.classify_event()
  -> retrieve_analogs.retrieve_analogs()
  -> generate_brief.generate_brief()
  -> Markdown brief
```

## Retrieval Scoring

The V0.1 similarity score is a weighted sum:

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

Scores are normalized to a 0-100 scale against the maximum possible score. They are similarity scores only.

## Determinism

The same input files and user description produce the same output. V0.1 does not call external APIs, randomize rankings, or use external model inference.

## Failure Modes

- Sparse data can produce shallow analog pools.
- Keyword rules may miss subtle geopolitical framing.
- Market reactions are limited to coded assets and available windows.
- Anticipated events can show muted market reactions.
- Confounded event windows can weaken analog interpretation.

## Extension Points

- Add ontology files for event types and sectors.
- Add analyst-reviewed classification overrides.
- Add tests for retrieval rankings.
- Add a small local web UI.
- Add richer return aggregation by asset type or exposure role.

These are deferred until the deterministic core is stable.
