# V2 Market Mapping Plan

This plan identifies representative US-China Strategic Competition pilot events for future market-data collection. It does not add market returns, calculate abnormal returns, forecast outcomes, or provide investment advice.

## Selected Events

### V2P001

- Event ID: V2P001
- Event Name: CHIPS and Science Act signed
- Event Date: 2022-08-09
- Category: Industrial Policy
- Why Selected: Anchor industrial-policy event and useful bridge from V1 semiconductor support cases to broader V2 strategic competition.
- Primary Affected Sector: Semiconductors and advanced manufacturing.
- Possible Asset Proxy: Semiconductor sector ETF or broad semiconductor index; individual beneficiaries only if directly mapped in later review.
- Possible Benchmark: Broad US equity index plus semiconductor sector benchmark.
- Suggested Return Window: `t0`, `m1_p1`, `m3_p3`; longer windows require anticipation caveat.
- Data Source Needed: Adjusted daily prices for selected semiconductor proxy and benchmark.
- Expected Data Challenges: Highly anticipated legislation; broad policy event may have muted or confounded event-day reaction.
- Coding Confidence: Medium.
- Notes: Use as industrial-policy reference, not as evidence of expected future support-event reaction.

### V2P002

- Event ID: V2P002
- Event Name: BIS advanced computing and semiconductor manufacturing export controls
- Event Date: 2022-10-07
- Category: Export Controls
- Why Selected: Core export-control event and direct extension of current V1 technology-restriction coverage.
- Primary Affected Sector: AI chips, semiconductors, semiconductor equipment.
- Possible Asset Proxy: Semiconductor sector ETF or semiconductor-equipment proxy.
- Possible Benchmark: Broad US equity index plus semiconductor sector benchmark.
- Suggested Return Window: `t0`, `m1_p1`, `m3_p3`, `m7_p7`.
- Data Source Needed: Adjusted daily prices for semiconductor proxy, equipment proxy, and benchmark.
- Expected Data Challenges: Multiple rule components; event may affect constrained firms, substitutes, suppliers, and customers differently.
- Coding Confidence: High.
- Notes: Candidate for multiple exposure roles after asset mapping is reviewed.

### V2P003

- Event ID: V2P003
- Event Name: YMTC and other Chinese entities added to Entity List
- Event Date: 2022-12-15
- Category: Sanctions / Entity List
- Why Selected: Named-entity restriction case that covers sanctions/entity-list mechanics.
- Primary Affected Sector: Memory chips and semiconductors.
- Possible Asset Proxy: Memory-chip sector proxy or listed peer proxy where direct target data is unavailable.
- Possible Benchmark: Semiconductor sector benchmark and broad regional equity benchmark if China-listed comparables are used.
- Suggested Return Window: `t0`, `m1_p1`, `m3_p3`.
- Data Source Needed: Adjusted daily prices for selected proxy assets and benchmark.
- Expected Data Challenges: YMTC may not have straightforward public equity data; proxy selection could be indirect.
- Coding Confidence: Medium.
- Notes: Do not force a single-firm return row if no defensible public asset proxy exists.

### V2P006

- Event ID: V2P006
- Event Name: China announces gallium and germanium export controls
- Event Date: 2023-07-03
- Category: Critical Minerals
- Why Selected: Critical-minerals event adjacent to semiconductors, defense, and clean-energy supply chains.
- Primary Affected Sector: Critical minerals and semiconductor inputs.
- Possible Asset Proxy: Materials or critical-minerals proxy; semiconductor sector proxy as secondary.
- Possible Benchmark: Broad market benchmark plus materials or semiconductor benchmark.
- Suggested Return Window: `t0`, `m1_p1`, `m3_p3`.
- Data Source Needed: Adjusted daily prices for materials/critical-minerals proxy and benchmark.
- Expected Data Challenges: Public proxies may be imperfect; direct gallium/germanium exposure is difficult to isolate.
- Coding Confidence: Medium.
- Notes: Proxy rationale is more important than breadth; avoid selecting assets after observing returns.

### V2P007

- Event ID: V2P007
- Event Name: US executive order on outbound investment in sensitive technologies
- Event Date: 2023-08-09
- Category: Strategic Investment Screening
- Why Selected: Primary strategic investment-screening event in the pilot dataset.
- Primary Affected Sector: Semiconductors, microelectronics, AI, quantum.
- Possible Asset Proxy: Broad technology index, semiconductor proxy, or China technology benchmark.
- Possible Benchmark: Broad US equity index plus technology or semiconductor benchmark.
- Suggested Return Window: `t0`, `m1_p1`, `m3_p3`.
- Data Source Needed: Adjusted daily prices for technology/semiconductor proxy and benchmark.
- Expected Data Challenges: Framework announcement rather than final rule; market reaction may reflect prior anticipation.
- Coding Confidence: Medium.
- Notes: May be better paired with V2P014 in a later implementation-versus-announcement comparison.

### V2P008

- Event ID: V2P008
- Event Name: BIS updates advanced computing and semiconductor export controls
- Event Date: 2023-10-17
- Category: AI Chip Restrictions
- Why Selected: Representative AI chip restriction event with named exposed companies.
- Primary Affected Sector: AI chips, semiconductors, cloud infrastructure.
- Possible Asset Proxy: Named exposed equities such as NVIDIA or AMD, plus semiconductor sector proxy.
- Possible Benchmark: Broad US equity index plus semiconductor or technology benchmark.
- Suggested Return Window: `t0`, `m1_p1`, `m3_p3`, `m7_p7`.
- Data Source Needed: Adjusted daily prices for named assets, semiconductor benchmark, and broad benchmark.
- Expected Data Challenges: Named firms may have earnings, product, or macro confounds; rule details are technical.
- Coding Confidence: High.
- Notes: Strong candidate for initial market rows because named assets and benchmark proxies are likely available.

### V2P011

- Event ID: V2P011
- Event Name: TSMC Arizona CHIPS preliminary terms announced
- Event Date: 2024-04-08
- Category: Supply Chain Relocation
- Why Selected: Semiconductor-linked supply-chain relocation and strategic fab investment case.
- Primary Affected Sector: Foundry, semiconductors, advanced manufacturing.
- Possible Asset Proxy: TSMC ADR or foundry/semiconductor sector proxy.
- Possible Benchmark: Broad US equity index, Taiwan equity benchmark, and semiconductor sector benchmark.
- Suggested Return Window: `t0`, `m1_p1`, `m3_p3`, `m7_p7`.
- Data Source Needed: Adjusted daily prices for TSMC ADR, semiconductor benchmark, and regional benchmark if used.
- Expected Data Challenges: Preliminary terms; named-company return may include firm-specific and Taiwan-market factors.
- Coding Confidence: High.
- Notes: Useful bridge between V1 CHIPS support events and V2 supply-chain relocation framing.

## Coverage Notes

The selected events cover export controls, sanctions/entity-list mechanics, AI chip restrictions, industrial policy, strategic investment screening, critical minerals, and supply-chain relocation.

Taiwan-related tension is intentionally not selected for the first market-mapping batch because the current goal is to prioritize events with clearer asset or sector mapping before broader risk-sentiment mapping.
