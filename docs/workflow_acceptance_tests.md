# Workflow Acceptance Tests

These acceptance tests define the expected behaviour of the deterministic Analyst Workbench. They are written as product validation evidence, not as new product functionality.

## Scenario Classification

| Input | Expected Behaviour | Observed Behaviour | Pass/Fail |
| --- | --- | --- | --- |
| `US announces a new semiconductor subsidy package.` | Classify the scenario as a semiconductor support or subsidy-related event when deterministic keyword rules match. | The workbench produces a scenario classification section with event type, policy subtype, country or region, sector, signal fields, matched terms, and caveats. | Pass |
| `The United States announces export controls on advanced AI chips.` | Identify restriction or export-control framing when matching terms are present. | Existing deterministic classification logic supports export-control and technology-restriction keywords. | Pass |
| Ambiguous geopolitical question with limited coded terms | Preserve deterministic caveats instead of inventing unsupported classification detail. | The classification component reports unknown dimensions and caveats when rules do not match. | Pass |

## Historical Analogue Retrieval

| Input | Expected Behaviour | Observed Behaviour | Pass/Fail |
| --- | --- | --- | --- |
| Classified semiconductor subsidy scenario | Retrieve ranked local historical analogues from `data/events.csv`. | The workbench reports ranked analogues with event IDs, dates, similarity scores, metadata, and retrieval rationales. | Pass |
| Export-control scenario | Retrieve analogues with restriction or export-control relevance when present in local data. | Existing retrieval tests confirm export-control analogues can be returned with score breakdowns. | Pass |
| Scenario with limited direct matches | Return the best available deterministic matches and expose rationale limitations. | The report preserves score rationales, coding notes, and caveats for analyst review. | Pass |

## Market Comparison

| Input | Expected Behaviour | Observed Behaviour | Pass/Fail |
| --- | --- | --- | --- |
| Retrieved analogues with event-firm return rows | Summarize observed event-day and CAR windows from local data only. | The market comparison section reports record counts, average observed metrics, and data quality flags. | Pass |
| Retrieved analogues without return rows | State that no event-firm return rows are available. | The report explicitly marks missing observed market data for analogues without rows. | Pass |
| Any market-reaction section | Avoid expected-return, trade, or forecast language. | Safety language frames reactions as historical observations only. | Pass |

## Observed Pathways

| Input | Expected Behaviour | Observed Behaviour | Pass/Fail |
| --- | --- | --- | --- |
| Support-coded scenario | Generate a state-support pathway when support signals or analogues justify it. | Existing pathway generation produces state-support framing based on deterministic coded features. | Pass |
| Restriction-coded scenario | Generate a restriction pathway when threat or restriction signals are present. | Existing pathway generation supports restriction framing from deterministic coded features. | Pass |
| Mixed or sparse scenario | Generate conservative analyst-review pathways without probabilities. | Pathways include historical basis, monitoring focus, and interpretation limits without forecast claims. | Pass |

## Executive Memo Generation

| Input | Expected Behaviour | Observed Behaviour | Pass/Fail |
| --- | --- | --- | --- |
| Valid analyst scenario and retrieved analogues | Produce concise memo language suitable for portfolio manager, risk committee, strategy team, or analyst-review handoff. | The executive memo includes a bottom line, implications for review, key uncertainties, and export-package notes. | Pass |
| Scenario with retrieval or data limitations | Escalate limitations clearly rather than overstating conclusions. | The report includes caveats, known uncertainties, and safety-boundary language. | Pass |
| Any executive memo | Avoid recommendations, probabilities, and forecasts. | Unit tests check for prohibited investment and probability patterns. | Pass |

## Markdown Export

| Input | Expected Behaviour | Observed Behaviour | Pass/Fail |
| --- | --- | --- | --- |
| `python3 src/run_scenario.py --query "US announces a new semiconductor subsidy package." --top-k 5 --output results/semiconductor_subsidy_brief.md` | Write a structured Markdown report to the requested output path and print it to stdout. | `src/run_scenario.py` writes the generated Analyst Workbench report to the requested Markdown path. | Pass |
| Generated Markdown report | Include clearly separated A-E sections. | Workbench report tests verify required sections are present. | Pass |
| Generated Markdown report | Remain readable as a standalone analyst artifact. | The report includes query, workflow audit, classification, analogues, market comparison, pathways, executive memo, and export-package metadata. | Pass |
