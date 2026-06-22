# Analyst Validation Suite

## Validation Objective

The validation objective is to show that the Analyst Workbench operates as a deterministic analyst productivity workflow rather than a forecasting, recommendation, or real-time intelligence system.

The suite validates whether the repository can:

- accept a representative geopolitical analyst question;
- classify the scenario with transparent keyword logic;
- retrieve historical analogues from local coded events;
- summarize observed market-reaction records from local data;
- generate observed pathway frames without probabilities or forecasts;
- produce a structured Markdown report suitable for portfolio manager, risk committee, strategy team, or analyst-review handoff.

## Workflow Components Tested

The validation suite covers the current local workflow:

```text
Question
  -> Scenario Classification
  -> Historical Analogue Retrieval
  -> Market Reaction Comparison
  -> Observed Pathway Generation
  -> Executive Memo
  -> Markdown Export
```

Components under validation:

- `src/run_scenario.py`: command-line orchestration.
- `src/classify_event.py`: deterministic scenario classification.
- `src/retrieve_analogs.py`: deterministic historical analogue retrieval.
- `src/compare_market_reactions.py`: observed event-study reaction summaries.
- `src/generate_pathways.py`: deterministic pathway framing.
- `src/generate_workbench_report.py`: structured Markdown report generation.

## Scenario Coverage

The validation scenarios emphasize common geopolitical intelligence questions that an analyst might ask during early triage:

- Taiwan risk scenarios involving blockade, military exercises, or supply-chain disruption.
- Semiconductor policy scenarios involving subsidies, industrial policy, and strategic capacity.
- Military escalation scenarios involving sanctions, restrictions, or defense-related tension.
- Strategic investment scenarios involving state support, fabs, or critical industrial capacity.
- Technology restriction scenarios involving export controls, entity lists, sanctions, or license requirements.

This scenario coverage is designed to demonstrate breadth of workflow handling, not predictive accuracy.

## Test Methodology

Validation uses repository-local, deterministic checks only:

1. Compile source files with `python3 -m compileall src`.
2. Run unit tests with `python3 -m unittest discover tests`.
3. Verify that generated reports contain the required Analyst Workbench sections.
4. Confirm that safety language is present and prohibited investment or probability language is absent.
5. Review example analyst questions for scenario diversity and fit with the repository's coded event domain.

The methodology intentionally avoids:

- external APIs;
- LLM calls;
- live news monitoring;
- dashboards;
- forecasting;
- investment recommendations.

## Observed Results

Observed validation results for the current repository state:

| Validation Check | Observed Result | Status |
| --- | --- | --- |
| Python source compilation | `python3 -m compileall src` completes successfully | Pass |
| Unit test suite | `python3 -m unittest discover tests` runs 9 tests successfully | Pass |
| Workbench report structure | Report includes A-E workbench sections and export package metadata | Pass |
| Safety boundaries | Report includes non-forecast and non-recommendation language | Pass |
| Classification logic preservation | No changes required to `src/classify_event.py` | Pass |
| Retrieval and scoring preservation | No changes required to `src/retrieve_analogs.py` | Pass |

## Known Limitations

- Classification is keyword based and may miss nuanced phrasing.
- Retrieval quality depends on the breadth and coding quality of `data/events.csv`.
- Market-reaction comparison is limited to event-firm rows available in `data/event_firm_returns.csv`.
- Similarity scores are retrieval scores only and are not probabilities.
- Observed pathways are analyst-review frames, not forecasts.
- Sparse or indirect historical analogues may require manual analyst caveats.
- The workbench does not ingest live data, call APIs, or update the dataset automatically.

## Conclusions

The validation suite supports the portfolio claim that this repository is a deterministic analyst workflow tool. It demonstrates repeatable scenario intake, classification, analogue retrieval, market context synthesis, pathway framing, and Markdown memo export without adding LLM calls, external APIs, forecasting, or investment recommendations.

The strongest portfolio value is workflow automation: the repository shows how a lightweight local codebase can turn a geopolitical question into a structured evidence package that is easier for analysts, portfolio managers, risk committees, and strategy teams to review.
