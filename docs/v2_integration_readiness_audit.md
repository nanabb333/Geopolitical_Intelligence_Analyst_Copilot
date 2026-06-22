# V2 Integration Readiness Audit

## Executive Summary

The V2 US-China Strategic Competition pilot dataset is not ready for direct integration into the V1 Analyst Workbench workflow.

The pilot is useful as a schema-governed expansion dataset, but V1 retrieval, pathway generation, market comparison, and report formatting expect the existing `data/events.csv` and `data/event_firm_returns.csv` schemas. Directly passing `data/us_china_strategic_competition_pilot.csv` into the V1 workflow would produce weak retrieval scores, missing report fields, and no meaningful market reaction comparison.

Recommended verdict: No-Go for direct integration. Go for a controlled integration-planning sprint that builds a field transformation layer, V2-compatible tests, and V2 market-return data before using the pilot in the workbench.

## Current V1 Data Flow

The current workflow uses:

```text
User query
  -> classify_event.classify_event()
  -> retrieve_analogs.retrieve_analogs()
  -> compare_market_reactions.summarize_reactions()
  -> generate_pathways.generate_pathways()
  -> generate_workbench_report.generate_workbench_report()
  -> Markdown report
```

Current V1 inputs:

- `data/events.csv`
- `data/event_firm_returns.csv`

Current V1 retrieval fields:

- `event_type`
- `policy_subtype`
- `country_or_region`
- `sector`
- `threat_signal`
- `opportunity_signal`
- `state_support`
- event-name and coding-note token overlap

Current V1 report fields:

- `event_id`
- `event_name`
- `event_date`
- `event_type`
- `policy_subtype`
- `country_or_region`
- `sector`
- `strategic_importance`
- `support_materiality`
- `anticipation_level`
- `coding_notes`

Current V1 market comparison joins event return rows by `event_id`.

## Current V2 Pilot Dataset Status

The V2 pilot file is:

```text
data/us_china_strategic_competition_pilot.csv
```

Current status:

- 15 rows.
- US-China strategic competition scope.
- Real historical events.
- Schema-governed columns.
- Source URLs and coding notes included.
- No event-firm market-return rows.
- Not wired into V1 workflow.
- Not transformed into V1-compatible event fields.

The V2 pilot is suitable for data architecture review and future integration planning. It is not yet suitable as a drop-in replacement for `data/events.csv`.

## Missing Integration Requirements

Before integration, the project needs:

- A deterministic V2-to-V1 field mapping or a V2-native retrieval layer.
- Controlled category mapping from V2 `category` and `subcategory` to V1 `event_type` and `policy_subtype`.
- Geography mapping from V2 `geography`, `actor_country`, and `target_country` to V1 `country_or_region`.
- Sector mapping from V2 `sectors_impacted` to V1 single `sector`.
- Signal coding for `threat_signal`, `opportunity_signal`, `state_support`, `substitution_reallocation`, and `anticipation_level`.
- Market-return rows linked to V2 `event_id` values.
- Tests proving V2 rows can be retrieved, summarized, and displayed without breaking V1 behaviour.
- Documentation that V2 integration does not imply forecasting, expected returns, or investment recommendations.

## Required Field Mapping

The mapping is documented in [V2 Field Mapping](v2_field_mapping.md).

Highest-priority transformations:

- `category` -> V1 `event_type`
- `subcategory` -> V1 `policy_subtype`
- `geography` or actor/target fields -> V1 `country_or_region`
- `sectors_impacted` -> V1 `sector`
- `strategic_significance` -> V1 `strategic_importance`
- `sources` -> V1 `source_url`
- V2 notes fields -> V1 `coding_notes`

These transformations must be explicit and tested. They should not be inferred ad hoc inside report generation.

## Market Return Data Requirements

The V2 pilot cannot support market reaction comparison until event-linked return rows are added.

Minimum market requirements:

- valid `event_id` matching V2 pilot rows;
- asset or sector mapping;
- event trading date alignment;
- benchmark selection;
- event-day return;
- abnormal-return metrics;
- cumulative abnormal-return windows;
- data quality and confound flags.

Detailed requirements are documented in [V2 Market Data Requirements](v2_market_data_requirements.md).

## Retrieval Compatibility Assessment

Current V2 retrieval compatibility: Not ready.

Reasons:

- V2 file lacks `event_type`.
- V2 file lacks `policy_subtype`.
- V2 file lacks `country_or_region`.
- V2 file has `sectors_impacted`, but V1 retrieval expects one `sector`.
- V2 file lacks numeric `threat_signal`, `opportunity_signal`, and `state_support`.
- V2 categories are richer than V1 keyword labels and require a mapping.
- Token overlap would still function, but it would be too weak to support reliable analogue ranking alone.

Direct integration would produce artificially low or misleading similarity scores.

## Classification Compatibility Assessment

Current V2 classification compatibility: Partial.

The existing classifier can classify some US-China pilot questions if they use V1-supported terms such as export controls, sanctions, restrictions, entity list, subsidy, funding, semiconductors, AI chips, and critical minerals.

Gaps:

- strategic investment screening is not a current classifier subtype;
- supply-chain relocation is not a current classifier subtype;
- critical minerals map only partially through the `energy` sector rule;
- Taiwan-related tension may classify as `Taiwan` geography but lacks a V1 event family;
- V2 category labels do not map directly to classifier outputs.

Do not change classification logic until V2 integration requirements are tested and accepted.

## Testing Requirements

Before integration, add tests for:

- V2 CSV schema integrity.
- V2-to-V1 field transformation.
- No duplicate V2 event IDs.
- Valid dates.
- Category values matching `docs/event_dictionary.md`.
- Retrieval on transformed V2 events.
- Market comparison behaviour when V2 return rows are missing.
- Market comparison behaviour when V2 return rows are present.
- Workbench report rendering with transformed V2 events.
- Regression tests proving V1 retrieval and report output remain unchanged.

## Risks of Premature Integration

- Misleading similarity scores caused by missing V1 retrieval fields.
- Report sections displaying `n/a` for important event metadata.
- Market reaction comparison showing no return rows for all V2 analogues.
- Classifier outputs failing to align with V2 categories.
- Analyst users overreading V2 rows as fully production-ready.
- Portfolio reviewers interpreting the pilot as a fully integrated US-China risk system.
- Hidden field transformations creating inconsistent or non-auditable results.

## Recommended Integration Plan

1. Keep V1 workflow frozen.
2. Define a deterministic V2-to-V1 transformation specification.
3. Create a transformed staging file for testing, not production.
4. Add V2 market-return template rows only after asset mapping and event-date alignment are reviewed.
5. Add tests for transformation, retrieval compatibility, and missing-market-data handling.
6. Run V2 pilot reports in a separate experimental mode or documented notebook after tests pass.
7. Only then decide whether to add source-level support for V2-native fields.

## Go / No-Go Recommendation

No-Go for direct V2 integration into the V1 workbench today.

Go for an integration-readiness sprint focused on mapping, tests, and market-data design. The V2 pilot should remain documented as a schema-governed expansion dataset until those requirements are complete.
