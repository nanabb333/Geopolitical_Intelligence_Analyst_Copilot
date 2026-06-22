# V2 Market Data Requirements

The V2 US-China Strategic Competition pilot dataset does not yet support market reaction comparison. The current V1 comparison layer requires event-linked return rows similar to `data/event_firm_returns.csv`.

This document defines what is needed before V2 market comparison should be enabled.

## Event Date Alignment

Each market row must align to a defensible event trading date.

Requirements:

- `event_id` must match a V2 pilot event.
- `event_t0_trade_date` must be the first valid trading day on or after the event date unless a documented alternate convention is used.
- Event-date confidence must be reviewed before market rows are accepted.
- Multi-day events must document why the selected date is used.
- Announcement date, rule publication date, implementation date, and enforcement date should not be mixed without coding notes.

## Asset or Sector Mapping

Each market row needs a clear exposure target.

Minimum fields:

- `event_id`
- `asset_id`
- `asset_name`
- `ticker_or_identifier`
- `exposure_role`
- `primary_beneficiary`
- `analysis_role`
- `sector`
- `geography`

Exposure roles should include controlled values such as:

- `named_beneficiary`
- `constrained_firm`
- `supplier`
- `customer`
- `substitute_beneficiary`
- `sector_benchmark`
- `market_benchmark`

## Benchmark Selection

V2 comparisons need documented benchmarks.

Recommended benchmark fields:

- `market_benchmark_id`
- `sector_benchmark_id`
- `technology_benchmark_id`, where relevant
- `regional_benchmark_id`, where relevant
- `benchmark_rationale`

Benchmarks should be selected before abnormal returns are calculated. They should not be chosen after observing the result.

## Return Window Requirements

At minimum, V2 should preserve the V1 return windows:

- `event_day_return`
- `ar_market_event_day`
- `ar_sector_event_day`
- `car_market_m1_p1`
- `car_sector_m1_p1`
- `car_market_m3_p3`
- `car_sector_m3_p3`
- `car_market_m7_p7`
- `car_sector_m7_p7`

Optional additions:

- `car_market_m10_p10`
- `car_sector_m10_p10`
- `pre_event_return_m5_m1`
- `post_event_return_p1_p5`

Longer windows should be used cautiously because confounds increase quickly in geopolitical event analysis.

## Abnormal Return or Comparison Metric

The current workflow summarizes historical observed returns and abnormal returns. V2 should keep the same non-predictive standard.

Required metric discipline:

- Use observed historical returns only.
- Document benchmark source.
- Document calculation method.
- Preserve missing values rather than filling them with assumptions.
- Do not calculate expected returns.
- Do not infer future price direction.

## Missing Data Risks

Without V2 market rows:

- the workbench will report no event-firm return records for V2 analogues;
- market comparison will be incomplete;
- users may overread analogue retrieval without market context;
- report quality will be weaker for risk committee or portfolio manager review.

Sparse market data is acceptable if disclosed. It is not acceptable to imply broad market evidence where rows do not exist.

## Source Requirements

Market data should come from a reproducible and documented source.

Required documentation:

- price data source;
- benchmark source;
- trading calendar convention;
- corporate action adjustment convention;
- calculation script or method;
- data access date;
- known gaps or vendor limitations.

## Minimum Viable Market-Data Structure

A minimum viable V2 market file should include:

```text
event_id
asset_id
asset_name
ticker_or_identifier
exposure_role
primary_beneficiary
analysis_role
sector
geography
event_t0_trade_date
event_day_return
ar_market_event_day
ar_sector_event_day
car_market_m1_p1
car_sector_m1_p1
car_market_m3_p3
car_sector_m3_p3
car_market_m7_p7
car_sector_m7_p7
market_benchmark_id
sector_benchmark_id
benchmark_rationale
earnings_conflict
macro_conflict
policy_conflict
event_window_coverage
data_quality_flag
calculation_notes
```

Minimum viable coverage:

- at least one reviewed market row for each event used in market-reaction examples;
- multiple exposure roles for restrictions, sanctions, supply-chain relocation, and strategic investment screening;
- explicit flags where no clean return window exists.

## Integration Recommendation

Do not enable V2 market reaction comparison until a V2 market data file exists and passes validation.

The next sprint should create a market-data template and codebook before calculating any rows.
