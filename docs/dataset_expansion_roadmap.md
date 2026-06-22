# Dataset Expansion Roadmap

## Executive Summary

Geopolitical Intelligence Analyst Copilot should be positioned as a general geopolitical intelligence workflow platform currently validated on a semiconductor-focused historical analogue dataset.

The V1 workflow architecture is generalizable:

```text
Question
  -> Scenario Classification
  -> Historical Analogue Retrieval
  -> Market Reaction Comparison
  -> Observed Pathways
  -> Executive Memo
  -> Markdown Export
```

The current limitation is not the workflow architecture. The limitation is dataset breadth: the coded historical analogue base is concentrated in semiconductor-centered geopolitical competition from 2022-2024. Future value should come from expanding event coverage while preserving the deterministic, auditable workflow.

## Current Dataset Boundary

The current dataset contains:

- 12 coded historical events in `data/events.csv`.
- 3 event-firm return rows in `data/event_firm_returns.csv`.
- 4 sample user questions in `data/sample_user_queries.csv`.
- Event coverage from 2022-08-09 to 2024-04-25.
- Strongest coverage in semiconductor industrial policy, export controls, entity-list actions, semiconductor-equipment restrictions, CHIPS Act support, and selected China/Japan/Taiwan-linked semiconductor cases.

Current coverage should be described as V1 validation coverage, not the full intended product boundary.

## Why the Workflow Is Generalizable

The workflow separates reusable product functions from domain-specific data:

- Scenario classification can be extended with additional event types, sectors, regions, and mechanism vocabularies.
- Historical analogue retrieval already operates on structured event fields rather than hardcoded semiconductor-only records.
- Market reaction comparison can ingest additional event-firm return rows if they follow the existing event-linked schema.
- Observed pathway generation can be expanded with additional mechanism families while keeping deterministic logic.
- Executive memo generation already uses structured sections that can support multiple geopolitical risk domains.
- Markdown export is domain-neutral.

This means the architecture can support broader geopolitical risk coverage after new historical events are coded and validated.

## Why the Current Data Is Narrow

The current data was intentionally built as a focused proof of workflow automation. It validates the end-to-end workbench on a coherent subset of geopolitical competition: semiconductor policy and technology restrictions.

Narrowness comes from:

- limited event count;
- limited market-return rows;
- concentration in semiconductor sectors;
- concentration in U.S., China, Japan, Taiwan-linked, and South Korea-linked cases;
- absence of direct Taiwan military-crisis, energy, cyber, shipping, critical-minerals, and broad sanctions cases.

This is a dataset limitation, not evidence that the workflow must remain semiconductor-only.

## Target Future Coverage Areas

Future coverage should expand from semiconductor competition into broader geopolitical risk domains:

- Taiwan military tension
- Export controls
- Sanctions
- Semiconductor industrial policy
- Energy security
- Shipping and maritime disruption
- Critical minerals
- Cyber operations
- Defense industrial policy
- AI infrastructure competition

## Priority Expansion Categories

| Category | Why It Matters | Example Event Types | Market or Sector Relevance | Current Dataset Support | Recommended Priority |
| --- | --- | --- | --- | --- | --- |
| Taiwan military tension | Taiwan risk is central to semiconductor supply chains, regional security, and global risk analysis. | Military exercises, blockade-risk episodes, airspace incursions, crisis communications, shipping disruption warnings. | Semiconductors, shipping, defense, insurance, regional equities, supply-chain exposed firms. | Partially Supported | High |
| Export controls | Export controls are already core to the current dataset and are a natural expansion path. | Advanced chip controls, equipment restrictions, software restrictions, allied-control alignment, license-rule changes. | Semiconductors, AI chips, equipment suppliers, cloud infrastructure, multinational technology firms. | Supported | High |
| Sanctions | Sanctions are a common geopolitical risk mechanism but current coverage is only adjacent through entity-list and restriction cases. | Entity-list actions, financial sanctions, procurement bans, secondary sanctions, sectoral sanctions. | Technology, finance, defense, energy, logistics, affected counterparties. | Partially Supported | High |
| Semiconductor industrial policy | This is the validated V1 domain and should remain a benchmark category for data quality. | Subsidy awards, fab investments, industrial-policy legislation, tax credits, capacity guarantees. | Semiconductor manufacturers, equipment suppliers, foundries, memory firms, regional development. | Supported | High |
| Energy security | Energy shocks are a major geopolitical risk domain currently absent from the dataset. | Oil sanctions, gas supply disruptions, strategic reserve actions, LNG restrictions, pipeline incidents. | Energy producers, utilities, transport, inflation-sensitive sectors, regional markets. | Unsupported | Medium |
| Shipping and maritime disruption | Maritime disruptions connect geopolitical shocks to supply chains and inflation risk. | Strait closures, port disruption, maritime insurance changes, naval incidents, rerouting announcements. | Shipping, logistics, retail supply chains, commodities, semiconductors, insurers. | Unsupported | High |
| Critical minerals | Critical minerals are increasingly strategic for energy transition, defense, and technology supply chains. | Export restrictions, mine nationalization, processing bans, strategic stockpiles, subsidy programs. | Batteries, electric vehicles, defense, energy storage, industrials. | Unsupported | Medium |
| Cyber operations | Cyber events can affect infrastructure, firms, and state competition, but require careful evidence coding. | State-linked intrusions, infrastructure attacks, sanctions after cyber operations, data-theft disclosures. | Technology, financial services, utilities, defense, insurers. | Unsupported | Medium |
| Defense industrial policy | Defense industrial policy links state support, procurement, and geopolitical competition. | Defense-production funding, munitions capacity expansion, export approvals, procurement restrictions. | Defense contractors, aerospace, electronics, semiconductors, industrials. | Partially Supported | Medium |
| AI infrastructure competition | AI infrastructure extends naturally from chip controls into compute, data centers, cloud, and power demand. | Compute restrictions, cloud-access controls, AI data-center investment, accelerator subsidies, model-export restrictions. | AI chips, cloud providers, data centers, power, cooling, semiconductors. | Partially Supported | High |

## Suggested Event Fields

Future event records should preserve existing fields and add only fields that improve structured retrieval, pathway generation, or market comparison.

Recommended additions for expanded datasets:

- `event_family`: broad domain such as technology_restriction, energy_security, maritime_disruption, sanctions, cyber, military_tension.
- `mechanism`: specific channel such as export_control, subsidy, blockade_risk, sanctions, supply_disruption, procurement_ban.
- `affected_geography`: direct geography affected by the event.
- `actor_country`: initiating government or actor.
- `target_country`: target government, firm domicile, or affected jurisdiction.
- `affected_sector`: sector or sectors affected.
- `asset_exposure_type`: beneficiary, constrained firm, substitute beneficiary, supplier, customer, benchmark.
- `directness`: whether the event directly affects assets or indirectly changes risk perception.
- `implementation_status`: announced, enacted, preliminary, enforced, delayed, revoked.
- `source_confidence`: evidence quality rating.
- `event_scope`: firm-specific, sector-wide, country-wide, regional, global.
- `market_channel`: policy support, demand shock, supply shock, restriction, retaliation, security risk, infrastructure disruption.
- `analyst_caveat`: concise warning about interpretation limits.

## Minimum Viable Expanded Dataset

A useful V2 dataset should be broad enough to test whether the general workflow holds beyond semiconductors.

Minimum recommended target:

- 60-100 coded events across at least 6 event families.
- At least 8-12 events per high-priority category.
- At least 25-40 event-firm return rows across multiple exposure roles.
- At least 3 geographies per category where possible.
- At least 2-3 representative example questions per category.
- Clear source URLs, coding notes, event-date confidence, and confound flags for every event.

Minimum category mix:

- Taiwan military tension: 8-12 events.
- Export controls: 10-15 events.
- Sanctions: 8-12 events.
- Semiconductor industrial policy: retain and expand to 15-20 events.
- Shipping and maritime disruption: 8-12 events.
- AI infrastructure competition: 8-12 events.

Energy security, critical minerals, cyber operations, and defense industrial policy can be added in later batches if V2 capacity is limited.

## Data Quality Standards

Expansion should maintain the current repo's strongest product quality: deterministic, auditable evidence.

Required standards:

- Every event must have a source URL and coding note.
- Event dates must be tied to a public announcement or identifiable event timestamp.
- Event-date confidence should be coded explicitly.
- Confound flags should be recorded for events with overlapping earnings, macro, or policy news.
- Market-return rows should link to valid `event_id` values.
- Exposure role should be coded consistently.
- Similarity fields should be structured, not hidden in narrative text.
- Unsupported or ambiguous cases should be marked with caveats rather than forced into a category.
- Dataset changes should preserve reproducibility and avoid invented events.

## Recommended Next Sprint

Recommended next sprint: "V2 Dataset Expansion Planning and Schema Hardening."

Use the V2 dataset architecture documents as governing references:

- [Dataset Schema V2](dataset_schema_v2.md)
- [Event Coding Template](event_coding_template.md)
- [Event Dictionary](event_dictionary.md)
- [Coding Rules](coding_rules.md)
- [V2 Dataset Readiness Assessment](v2_dataset_readiness_assessment.md)

Suggested scope:

1. Freeze V1 code and current validation package.
2. Use `docs/dataset_schema_v2.md` as the target schema for candidate events.
3. Use `docs/event_coding_template.md` and `docs/event_dictionary.md` for all candidate-event coding.
4. Select 2 expansion categories for pilot coding: Taiwan military tension and shipping/maritime disruption.
5. Code 10-15 candidate events without changing retrieval or report-generation logic.
6. Run a coverage review before deciding whether source logic needs any V2 extensions.

Do not change architecture until the new data shows a concrete limitation.

## Portfolio Positioning

Use this positioning:

```text
Geopolitical Intelligence Analyst Copilot is a general geopolitical intelligence workflow platform currently validated on a semiconductor-focused historical analogue dataset.
```

This language preserves the product ambition without overclaiming current coverage. It makes clear that V1 proves the workflow and that future dataset expansion is the path to broader geopolitical risk coverage.
