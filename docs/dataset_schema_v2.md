# Dataset Schema V2

## Purpose

Dataset Schema V2 defines a standardized event-data architecture for future multi-domain geopolitical dataset expansion.

The goal is to preserve the V1 workflow architecture while making future events codable across Taiwan tension, export controls, sanctions, energy security, shipping disruption, critical minerals, cyber operations, defense industrial policy, AI infrastructure competition, and semiconductor industrial policy.

This document is schema design only. It does not add data, modify source logic, change retrieval weights, or expand current system capability.

## Design Principles

- Preserve deterministic analysis: every event should be structured enough to support transparent classification, retrieval, comparison, and caveats.
- Separate architecture from coverage: V2 fields should support broader domains without claiming those domains are already covered.
- Use auditable evidence: every coded event needs source support and analyst coding notes.
- Keep retrieval fields structured: important retrieval dimensions should be coded in fields, not buried in prose.
- Support market comparison where data exists: event-level metadata should be linkable to event-firm return rows, but market data should not be required for every event.
- Preserve safety boundaries: schema fields should support decision support, not forecasts, probabilities, expected returns, or investment recommendations.
- Make ambiguity visible: missing, uncertain, or ambiguous values should be coded explicitly.

## Required Fields

Every V2 event record should include:

- `event_id`
- `event_name`
- `event_date`
- `event_date_confidence`
- `category`
- `subcategory`
- `trigger`
- `actor_country`
- `target_country`
- `geography`
- `sector`
- `sectors_impacted`
- `companies_impacted`
- `strategic_significance`
- `market_relevance`
- `event_scope`
- `implementation_status`
- `source_url`
- `source_quality`
- `coding_notes`
- `analyst_caveat`

## Optional Fields

Optional fields should be used when available:

- `event_end_date`
- `event_duration_days`
- `policy_instrument`
- `affected_assets`
- `asset_exposure_type`
- `expected_direction`
- `market_channel`
- `supply_chain_channel`
- `threat_signal`
- `opportunity_signal`
- `state_support`
- `substitution_reallocation`
- `anticipation_level`
- `beneficiary_visibility`
- `support_materiality`
- `confound_flag_event`
- `related_event_id`
- `duplicate_group_id`
- `primary_test_eligible`
- `historical_notes`
- `secondary_sources`

## Field Definitions

| Field | Definition | Expected Format |
| --- | --- | --- |
| `event_id` | Unique event identifier. | Stable ID such as `V2E001`. |
| `event_name` | Short descriptive event title. | Plain text. |
| `event_date` | Primary event date used for retrieval and market comparison. | `YYYY-MM-DD`. |
| `event_date_confidence` | Confidence that the date is the correct event date. | `high`, `medium`, `low`. |
| `category` | Broad geopolitical event family. | Controlled value from `docs/event_dictionary.md`. |
| `subcategory` | More specific event mechanism. | Controlled or documented value. |
| `trigger` | What caused the event to enter the dataset. | Announcement, enforcement action, military event, disruption, sanction, etc. |
| `actor_country` | Initiating country or actor. | Country, multilateral body, or `non-state`. |
| `target_country` | Country or actor targeted or most directly affected. | Country, multilateral body, firm domicile, or `multiple`. |
| `geography` | Relevant geography for scenario matching. | Country, region, strait, route, or `global`. |
| `sector` | Primary sector label. | Controlled sector value. |
| `sectors_impacted` | Additional sectors affected. | Semicolon-separated list. |
| `companies_impacted` | Named firms or assets directly discussed in source material. | Semicolon-separated list or `none_identified`. |
| `strategic_significance` | Importance to geopolitical competition or security. | `0`, `1`, `2`, `3`. |
| `market_relevance` | Whether the event has plausible market or sector relevance. | `low`, `medium`, `high`. |
| `event_scope` | Breadth of the event. | `firm_specific`, `sector_wide`, `country_wide`, `regional`, `global`. |
| `implementation_status` | Whether action is proposed, announced, enacted, enforced, delayed, or revoked. | Controlled value. |
| `source_url` | Primary source URL. | URL. |
| `source_quality` | Reliability of source basis. | `primary`, `official`, `major_media`, `specialist`, `uncertain`. |
| `coding_notes` | Analyst notes explaining coding choices. | Plain text. |
| `analyst_caveat` | Short warning about interpretation limits. | Plain text. |

## Data Validation Rules

- `event_id` must be unique.
- `event_date` must be valid ISO date format.
- `event_date_confidence` must be `high`, `medium`, or `low`.
- `category` must match the category dictionary.
- `source_url` must be populated.
- `coding_notes` must be populated.
- `strategic_significance` must be an integer from `0` to `3`.
- `market_relevance` must be `low`, `medium`, or `high`.
- If `companies_impacted` is empty, code `none_identified`.
- If a field is unknown, code `unknown`; do not leave required fields blank.
- If an event is a duplicate or update of another event, populate `related_event_id` or `duplicate_group_id`.
- If market-return rows are later added, each row must link to a valid `event_id`.
- Do not code forecasts, expected returns, probabilities, or investment recommendations as event facts.

## Example Records

These are schema examples only. They are not new dataset rows and should not be treated as coded historical events.

### Example: Export Controls

| Field | Example Value |
| --- | --- |
| `event_id` | `V2E001` |
| `event_name` | `Example advanced chip export-control announcement` |
| `event_date` | `YYYY-MM-DD` |
| `event_date_confidence` | `high` |
| `category` | `Export Controls` |
| `subcategory` | `advanced_chip_control` |
| `trigger` | `government rule announcement` |
| `actor_country` | `US` |
| `target_country` | `China` |
| `geography` | `US/China` |
| `sector` | `AI chips` |
| `sectors_impacted` | `semiconductors;cloud infrastructure` |
| `companies_impacted` | `none_identified` |
| `strategic_significance` | `3` |
| `market_relevance` | `high` |
| `event_scope` | `sector_wide` |
| `implementation_status` | `announced` |
| `source_url` | `https://example.com/source` |
| `source_quality` | `official` |
| `coding_notes` | `Example only; not a coded event.` |
| `analyst_caveat` | `Use only after source verification and event-date review.` |

### Example: Shipping Disruption

| Field | Example Value |
| --- | --- |
| `event_id` | `V2E002` |
| `event_name` | `Example maritime route disruption` |
| `event_date` | `YYYY-MM-DD` |
| `event_date_confidence` | `medium` |
| `category` | `Shipping Disruption` |
| `subcategory` | `route_disruption` |
| `trigger` | `security incident` |
| `actor_country` | `unknown` |
| `target_country` | `multiple` |
| `geography` | `maritime chokepoint` |
| `sector` | `shipping` |
| `sectors_impacted` | `shipping;logistics;energy;retail` |
| `companies_impacted` | `none_identified` |
| `strategic_significance` | `2` |
| `market_relevance` | `high` |
| `event_scope` | `regional` |
| `implementation_status` | `active` |
| `source_url` | `https://example.com/source` |
| `source_quality` | `major_media` |
| `coding_notes` | `Example only; not a coded event.` |
| `analyst_caveat` | `Market interpretation depends on duration and rerouting evidence.` |
