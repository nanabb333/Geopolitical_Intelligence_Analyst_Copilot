# V2 Field Mapping

This document maps `data/us_china_strategic_competition_pilot.csv` fields to the current V1 workflow schema.

Integration status values:

- Ready: can be used directly or with a simple rename.
- Needs Transformation: usable only after deterministic mapping.
- Missing: no V2 or V1 equivalent exists.

| V2 Field Name | Existing V1 Equivalent If Any | Required Transformation | Used by Classification? | Used by Retrieval? | Used by Comparison? | Used by Memo? | Integration Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `event_id` | `event_id` | None. Must remain unique. | No | Join context only | Yes, for return join | Yes | Ready |
| `event_name` | `event_name` | None. | No | Yes, token overlap | No | Yes | Ready |
| `event_date` | `event_date` | None if ISO date. | No | Sort tie-breaker | Event-date alignment needed | Yes | Ready |
| `geography` | `country_or_region` | Map to V1 geography label or composite region. | No | Yes | No | Yes | Needs Transformation |
| `category` | `event_type` | Map V2 category to V1 event family or add V2-native retrieval later. | No | Yes | No | Yes | Needs Transformation |
| `subcategory` | `policy_subtype` | Map V2 subcategory to V1 policy subtype where possible. | No | Yes | No | Yes | Needs Transformation |
| `trigger` | No direct V1 equivalent | Could enrich coding notes or future mechanism field. | No | Token overlap only if merged | No | Possible | Needs Transformation |
| `strategic_significance` | `strategic_importance` | Rename and preserve 0-3 scale. | No | No current weight | No | Yes | Needs Transformation |
| `market_relevance` | No direct V1 equivalent | Could become report metadata; not used today. | No | No | No | Possible | Missing |
| `sectors_impacted` | `sector` | Select primary sector or create deterministic sector-normalization rule. | No | Yes | Possible sector benchmark mapping | Yes | Needs Transformation |
| `companies_impacted` | No direct V1 event equivalent | Could support future asset mapping; not used by V1 retrieval. | No | Token overlap if merged | Asset mapping input | Possible | Needs Transformation |
| `historical_notes` | Partial `coding_notes` | Merge with `coding_notes` or keep separate in V2-native memo. | No | Token overlap if merged | No | Possible | Needs Transformation |
| `sources` | `source_url` | Rename to `source_url`; handle multiple URLs if added later. | No | No | No | Possible | Needs Transformation |
| `coding_notes` | `coding_notes` | None or merge with historical notes. | No | Yes, token overlap | No | Yes | Ready |
| `event_date_confidence` | `event_date_confidence` | None. | No | No | Event-date QA | Possible | Ready |
| `actor_country` | No direct V1 equivalent | Could inform `country_or_region`; preserve separately for V2. | No | Possible after mapping | No | Possible | Needs Transformation |
| `target_country` | No direct V1 equivalent | Could inform `country_or_region`; preserve separately for V2. | No | Possible after mapping | No | Possible | Needs Transformation |
| `event_scope` | No direct V1 equivalent | Could support future memo caveats. | No | No | No | Possible | Missing |
| `implementation_status` | No direct V1 equivalent | Could support future event timing caveats. | No | No | Event-date QA | Possible | Missing |
| `source_quality` | No direct V1 equivalent | Could support QA and memo caveats. | No | No | No | Possible | Missing |
| `analyst_caveat` | No direct V1 equivalent | Could merge into `coding_notes` or future caveat section. | No | Token overlap if merged | No | Yes, if report is extended later | Needs Transformation |
| Missing in V2 | `threat_signal` | Must be coded or derived by deterministic rules before V1 retrieval. | No | Yes | No | Pathway generation | Missing |
| Missing in V2 | `opportunity_signal` | Must be coded or derived by deterministic rules before V1 retrieval. | No | Yes | No | Pathway generation | Missing |
| Missing in V2 | `state_support` | Must be coded or derived by deterministic rules before V1 retrieval. | No | Yes | No | Pathway generation | Missing |
| Missing in V2 | `substitution_reallocation` | Needed for current pathway generation. | No | No | No | Pathway generation | Missing |
| Missing in V2 | `anticipation_level` | Needed for current pathway generation and memo context. | No | No | No | Yes | Missing |
| Missing in V2 | `support_materiality` | Displayed in current workbench report. | No | No | No | Yes | Missing |
| Missing in V2 | `confound_flag_event` | Useful for event-window QA. | No | No | Yes | Possible | Missing |
| Missing in V2 | `event_tier` | Used for analyst context, not directly weighted. | No | No | No | Possible | Missing |
| Missing in V2 | `primary_test_eligible` | Used for dataset governance, not current retrieval. | No | No | No | No | Missing |

## Mapping Assessment

The V2 pilot is not a drop-in replacement for `data/events.csv`.

The safest next step is a deterministic staging transformation that converts V2 rows into V1-compatible fields while preserving original V2 fields for audit. That transformation should be documented and tested before any workflow integration.
