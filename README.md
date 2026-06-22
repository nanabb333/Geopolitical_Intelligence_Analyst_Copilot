# Geopolitical Intelligence Analyst Copilot

Geopolitical Intelligence Analyst Copilot is a deterministic workflow automation product for geopolitical risk analysis. It turns analyst questions into structured intelligence briefs by combining scenario classification, historical analogue retrieval, observed market-reaction context, pathway framing, and Markdown memo export.

The repository demonstrates business analytics, risk analytics, workflow automation, and product thinking in a local, auditable Python project. It is designed as a research-to-intelligence productivity layer, not a forecasting system, trading tool, or investment recommendation engine.

## Product Overview

The product helps analysts move from an unstructured geopolitical question to a structured evidence brief suitable for portfolio manager, risk committee, strategy team, or graduate portfolio review.

It is intentionally scoped as an analyst productivity tool. It does not replace analyst judgement, ingest live news, call external APIs, use LLMs, make forecasts, estimate probabilities, or recommend investments.

## Demo Workflow

```text
Question
  -> Scenario Classification
  -> Historical Analogue Retrieval
  -> Market Reaction Comparison
  -> Observed Pathway Generation
  -> Executive Memo
  -> Markdown Export
```

The demo workflow is implemented through local CSV inputs and standard-library Python. Each step remains auditable:

- scenario classification uses deterministic keyword rules;
- historical analogue retrieval uses local coded events and transparent similarity scoring;
- market comparison summarizes local event-study rows only;
- observed pathways are deterministic analyst-review frames;
- executive memo generation packages the evidence into a reusable Markdown report.

## How To Run

Run the main scenario workflow from the repository root:

```bash
python3 src/run_scenario.py \
  --query "US announces a new semiconductor subsidy package." \
  --top-k 5 \
  --output results/semiconductor_subsidy_brief.md
```

Generate the Analyst Workbench report directly:

```bash
python3 src/generate_workbench_report.py \
  "US announces a new semiconductor subsidy package." \
  --top-k 5 \
  --output results/analyst_workbench_report.md
```

Run validation:

```bash
python3 -m compileall src
python3 -m unittest discover tests
```

## Validation Evidence

The repository includes a Validation & Evidence Package for portfolio review:

- [Analyst Validation Suite](docs/analyst_validation_suite.md)
- [Workflow Acceptance Tests](docs/workflow_acceptance_tests.md)
- [Example Analyst Questions](docs/example_questions.md)

Current validation status:

- `python3 -m compileall src`: PASS
- `python3 -m unittest discover tests`: PASS
- Unit test result: 9 tests passing
- Workbench report sections A-E: covered by tests
- Safety-boundary language: covered by tests
- No source logic changed during the evidence package sprint
- Classification, retrieval, scoring, and report-generation logic preserved during this README packaging sprint

## Portfolio Value

This project is relevant to analytics and risk roles because it demonstrates how structured data, deterministic logic, and clear product framing can improve analyst throughput without overstating automation.

- Business Analytics: converts an ambiguous decision-support workflow into repeatable inputs, outputs, documentation, and validation evidence.
- Risk Analytics: structures geopolitical scenarios around historical analogues, observed event windows, uncertainty notes, and safety boundaries.
- Workflow Automation: automates intake-to-memo packaging while preserving transparent intermediate steps for analyst review.
- AI-assisted decision support: shows where deterministic automation can support intelligence workflows without LLM calls or opaque prediction claims.
- Analyst Productivity: reduces first-pass memo assembly work and gives reviewers a consistent evidence format.

## Example Analyst Questions

Representative analyst questions are grouped by:

- Taiwan Risk
- Semiconductor Policy
- Military Escalation
- Strategic Investment
- Technology Restrictions

See [Example Analyst Questions](docs/example_questions.md) for the full 15-question set.

## Representative Outputs

Placeholder documentation files are available for curated portfolio examples:

- [Taiwan Blockade](docs/example_outputs/taiwan_blockade.md)
- [Export Controls](docs/example_outputs/export_controls.md)
- [Semiconductor Sanctions](docs/example_outputs/semiconductor_sanctions.md)
- [Military Exercise](docs/example_outputs/military_exercise.md)
- [Strategic Investment](docs/example_outputs/strategic_investment.md)

These files are documentation placeholders for future generated reports. They do not add product functionality.

## Reproducibility

Run validation from the repository root:

```bash
python3 -m compileall src
python3 -m unittest discover tests
```

Generate a deterministic workbench report:

```bash
python3 src/run_scenario.py \
  --query "US announces a new semiconductor subsidy package." \
  --top-k 5 \
  --output results/semiconductor_subsidy_brief.md
```

The same query and local CSV inputs produce the same report. No external APIs, LLM calls, live news feeds, dashboards, forecasting modules, or investment-recommendation logic are used.

## What The System Does

```text
User question
  -> Event classification
  -> Historical analog retrieval
  -> Market reaction comparison
  -> Scenario pathways
  -> Executive brief
```

The workflow produces:

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

## Analyst Workbench

The Analyst Workbench expands the original question-to-brief demo into a deterministic analyst workflow:

```text
Question
  -> Scenario Classification
  -> Historical Analogue Retrieval
  -> Market Reaction Comparison
  -> Observed Pathway Generation
  -> Executive Memo
  -> Export Package
```

`src/run_scenario.py` now generates a structured Markdown workbench report with clearly separated sections:

- A. Scenario Classification
- B. Historical Analogues
- C. Market Reaction Comparison
- D. Observed Pathways
- E. Executive Memo

The workflow preserves the existing classification and retrieval logic. It extends orchestration and presentation by packaging matched classification terms, ranked analogues, observed event-study reaction summaries, deterministic pathway frames, executive memo language, and export-package metadata into one analyst-ready report.

Use it when a portfolio manager, risk committee, strategy team, or analyst-review process needs a disciplined first-pass scenario memo grounded in local historical analogues. The workbench remains deterministic: it uses local CSV files only and does not add LLM calls, APIs, dashboards, real-time monitoring, forecasting, or investment recommendations.

See [Analyst Workbench](docs/analyst_workbench.md) for workflow details, inputs, outputs, and intended use.

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

- [Analyst Workbench](docs/analyst_workbench.md)
- [Analyst Validation Suite](docs/analyst_validation_suite.md)
- [Workflow Acceptance Tests](docs/workflow_acceptance_tests.md)
- [Example Analyst Questions](docs/example_questions.md)
- [Product Spec](docs/product_spec.md)
- [Architecture](docs/architecture.md)
- [Methodology](docs/methodology.md)
- [Safety Boundaries](docs/safety_boundaries.md)
- [Roadmap](docs/roadmap.md)

## Core Scripts

- `src/run_scenario.py`: main Analyst Workbench orchestration CLI
- `src/classify_event.py`: deterministic rule-based event classification
- `src/retrieve_analogs.py`: weighted historical analog retrieval
- `src/compare_market_reactions.py`: observed event-study reaction summaries
- `src/generate_pathways.py`: deterministic qualitative scenario pathways
- `src/generate_workbench_report.py`: structured Markdown Analyst Workbench report generation
- `src/generate_brief.py`: legacy Markdown executive brief generation

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

For Business Analytics and Strategy Analytics, it demonstrates structured intake-to-memo automation, repeatable decision-support outputs, and clear user workflow design.

For Risk Analytics and Geopolitical Intelligence, it demonstrates transparent event classification, historical analog retrieval, market-reaction context, and explicit safety boundaries.

For AI workflow automation roles, it demonstrates where deterministic automation can create analyst leverage without relying on external APIs, LLM calls, or opaque prediction claims.

## Skills Demonstrated

- Product analytics architecture
- Geopolitical risk intelligence design
- Business, risk, and strategy analytics positioning
- Analyst productivity workflow automation
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
