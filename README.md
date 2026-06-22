# Geopolitical Intelligence Analyst Copilot

Analyst Workflow Copilot.

A lightweight deterministic analyst workflow copilot that converts geopolitical scenario questions into structured intelligence briefs using transparent classification, historical analog retrieval, and Markdown memo generation.

This repository converts a user-described geopolitical event into a deterministic historical analog analysis using a local event-study database. It is designed as a research-to-intelligence workflow automation layer, not a forecasting system or investment tool.

## Product Vision

Geopolitical risk analysis should be grounded in historically comparable events before it is turned into executive decision support. This copilot takes a user question, classifies the event, retrieves similar historical analogs, summarizes observed market reactions from the event-study database, and produces a conservative executive brief.

## What The System Does

```text
User question
  -> Event classification
  -> Historical analog retrieval
  -> Market reaction comparison
  -> Scenario pathways
  -> Executive brief
```

The V0.1 workflow produces:

1. User Event Description
2. Event Classification
3. Most Similar Historical Events
4. Historical Market Reactions
5. Potential Future Pathways
6. Key Risks and Uncertainties
7. Executive Brief

## What The System Does Not Do

- No live news retrieval
- No external APIs
- No LLM calls
- No forecasting
- No return predictions
- No probability estimates
- No trading signals
- No investment recommendations

Similarity scores are deterministic retrieval scores only. They are not probabilities.

## Quick Start

Run from the repository root:

```bash
python3 src/run_scenario.py \
  --query "US announces a new semiconductor subsidy package." \
  --top-k 5 \
  --output results/semiconductor_subsidy_brief.md
```

The command writes a Markdown brief and also prints it to stdout.

## Example User Query

```text
US announces a new semiconductor subsidy package.
```

Example output summary:

```text
Classification: support / subsidy_award / semiconductors
Analog retrieval: CHIPS Act and semiconductor state-support events
Market reaction comparison: observed event-study windows from local CSV data
Pathways: state support, reallocation, anticipation, and implementation uncertainty
Brief type: historical analog decision-support memo
```

Additional curated examples are available in `examples/`.

## Repository Structure

```text
Geopolitical_Intelligence_Analyst_Copilot/
  data/
    events.csv
    event_firm_returns.csv
    sample_user_queries.csv
  docs/
    architecture.md
    methodology.md
    product_spec.md
    roadmap.md
    safety_boundaries.md
  examples/
    export_controls_brief.md
    semiconductor_subsidy_brief.md
  results/
    .gitkeep
  src/
    classify_event.py
    compare_market_reactions.py
    generate_brief.py
    generate_pathways.py
    retrieve_analogs.py
    run_scenario.py
  tests/
    test_classify_event.py
    test_generate_brief.py
    test_retrieve_analogs.py
```

## Documentation

- [Product Spec](docs/product_spec.md)
- [Architecture](docs/architecture.md)
- [Methodology](docs/methodology.md)
- [Safety Boundaries](docs/safety_boundaries.md)
- [Roadmap](docs/roadmap.md)

## Core Scripts

- `src/run_scenario.py`: main V0.1 orchestration CLI
- `src/classify_event.py`: deterministic rule-based event classification
- `src/retrieve_analogs.py`: weighted historical analog retrieval
- `src/compare_market_reactions.py`: observed event-study reaction summaries
- `src/generate_pathways.py`: deterministic qualitative scenario pathways
- `src/generate_brief.py`: Markdown executive brief generation

Existing scripts remain directly runnable for inspection and debugging.

## Inputs

- `data/events.csv`: coded geopolitical event database
- `data/event_firm_returns.csv`: event-level firm return outcomes and abnormal return windows
- `data/sample_user_queries.csv`: example user questions for local testing

## Relationship to Flagship System

Opportunity Under Geopolitical Competition
= flagship evidence-intelligence system

Geopolitical Intelligence Analyst Copilot
= workflow automation layer

The flagship system contains the broader evidence base and geopolitical competition framing. This copilot focuses on analyst productivity: scenario intake, classification, retrieval, and memo generation.

## Portfolio Positioning

Geopolitical Intelligence Analyst Copilot demonstrates how research assets and event-study outputs can be converted into an auditable deterministic analyst workflow copilot for executive risk analysis.

## Skills Demonstrated

- Product analytics architecture
- Geopolitical risk intelligence design
- Historical analog retrieval
- Event classification
- Event-study interpretation
- Executive brief generation
- Responsible AI/product safety boundaries
- Standard-library Python implementation
- Reproducible local workflow design

## Validation

```bash
python3 -m compileall src
python3 -m unittest discover tests
```

## Safety Boundary

The generated brief supports research and strategic analysis only. It must not be used as a forecast, return prediction, trading signal, or investment recommendation.
