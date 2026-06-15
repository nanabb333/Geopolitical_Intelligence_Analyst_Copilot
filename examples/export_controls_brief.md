# Historical Analog Scenario Brief

> V0.1 historical analog analysis only. This brief is not a forecast, probability estimate, trading recommendation, or investment recommendation.

## User Event Description

China announces export controls on gallium and germanium.

## Event Classification

- `event_type`: threat_contrast
- `policy_subtype`: export_control
- `country_or_region`: China
- `sector`: unknown
- `threat_signal`: 1
- `opportunity_signal`: 0
- `state_support`: 0
- Classification caveats: No deterministic sector rule matched.

## Most Similar Historical Events

### 1. Japan announces semiconductor-equipment export controls

- Event ID: `E005`
- Date: 2023-03-31
- Similarity score: 55.95/100
- Type/subtype: `threat_contrast` / `export_control`
- Country or region: `Japan`
- Sector: `semiconductor equipment`
- Rationale: event_type matched: threat_contrast vs threat_contrast; policy_subtype matched: export_control vs export_control; state_support aligned with historical coding; token overlap contributed 0.17

### 2. Nvidia discloses AI chip export-license requirement

- Event ID: `E002`
- Date: 2022-08-31
- Similarity score: 54.19/100
- Type/subtype: `threat_contrast` / `export_control`
- Country or region: `US`
- Sector: `AI chips`
- Rationale: event_type matched: threat_contrast vs threat_contrast; policy_subtype matched: export_control vs export_control; state_support aligned with historical coding; token overlap contributed 0.04

### 3. BIS advanced computing and semiconductor controls

- Event ID: `E003`
- Date: 2022-10-07
- Similarity score: 52.69/100
- Type/subtype: `threat_contrast` / `export_control`
- Country or region: `US`
- Sector: `semiconductors`
- Rationale: event_type matched: threat_contrast vs threat_contrast; policy_subtype matched: export_control vs export_control; state_support aligned with historical coding; token overlap contributed 0.11

### 4. China restricts Micron procurement

- Event ID: `E006`
- Date: 2023-05-21
- Similarity score: 44.73/100
- Type/subtype: `threat_contrast` / `retaliation`
- Country or region: `China`
- Sector: `memory chips`
- Rationale: event_type matched: threat_contrast vs threat_contrast; country_or_region matched: China vs China; state_support aligned with historical coding; token overlap contributed 0.05

### 5. YMTC and other Chinese entities added to Entity List

- Event ID: `E004`
- Date: 2022-12-15
- Similarity score: 33.33/100
- Type/subtype: `threat_contrast` / `entity_list`
- Country or region: `US`
- Sector: `memory chips`
- Rationale: event_type matched: threat_contrast vs threat_contrast; state_support aligned with historical coding

## Historical Market Reactions

- Retrieved analogs: 5
- Analogs with return records: 0
- Analogs without return records: 5

### Japan announces semiconductor-equipment export controls

- No event-firm return rows are available for this analog in `event_firm_returns.csv`.

### Nvidia discloses AI chip export-license requirement

- No event-firm return rows are available for this analog in `event_firm_returns.csv`.

### BIS advanced computing and semiconductor controls

- No event-firm return rows are available for this analog in `event_firm_returns.csv`.

### China restricts Micron procurement

- No event-firm return rows are available for this analog in `event_firm_returns.csv`.

### YMTC and other Chinese entities added to Entity List

- No event-firm return rows are available for this analog in `event_firm_returns.csv`.

## Potential Future Pathways

### Restriction pathway

- Historical basis: Retrieved analogs include export controls, restrictions, or other threat-coded events.
- Monitoring focus: Distinguish directly constrained firms from substitute beneficiaries and supply-chain rerouting effects.
- Interpretation limit: Historical reactions may reflect event-specific exposure and cannot be projected forward.

### Reallocation pathway

- Historical basis: Analog coding indicates possible substitution or strategic supply-chain reallocation.
- Monitoring focus: Review exposure roles, sector positioning, jurisdictional constraints, and second-order beneficiaries.
- Interpretation limit: Substitution effects are heterogeneous and may not appear in short event windows.

### Anticipation pathway

- Historical basis: Some analogs were partly anticipated before the coded event date.
- Monitoring focus: Separate policy surprise from implementation detail and prior market incorporation.
- Interpretation limit: Muted observed reactions may reflect prior anticipation rather than low strategic importance.


## Key Risks and Uncertainties

- Analog similarity is based on coded historical fields and keyword classification, not causal identification.
- Sparse return coverage can overemphasize events with available asset rows.
- Anticipated policy actions may have muted event-window reactions.
- Confounding macro, earnings, or concurrent policy news can weaken interpretation.
- Sector labels may hide meaningful differences across firms, supply-chain positions, and jurisdictions.

## Executive Brief

The described event classifies primarily as `threat_contrast` / `export_control` in `unknown`. The closest retrieved analog is `Japan announces semiconductor-equipment export controls` with a deterministic similarity score of 55.95/100. The analog set should be read as a structured historical comparison, with attention to support materiality, threat intensity, anticipation, and data quality flags.

This V0.1 output supports research and strategic analysis only.