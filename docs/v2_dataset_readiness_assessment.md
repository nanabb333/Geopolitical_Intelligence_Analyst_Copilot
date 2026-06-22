# V2 Dataset Readiness Assessment

## Whether the Current Workflow Can Support Broader Datasets

The current V1 workflow can support broader datasets at the architecture level.

The workflow already separates:

- scenario intake;
- classification;
- historical analogue retrieval;
- market-reaction comparison;
- observed pathway generation;
- executive memo generation;
- Markdown export.

These stages are not inherently semiconductor-only. The limiting factor is the current dataset and controlled vocabulary, not the overall workflow design.

Broader datasets can be introduced if future events preserve structured fields for category, subcategory, geography, sector, strategic significance, market relevance, source quality, and coding notes.

## Risks of Expansion

- Category drift: new categories may be coded inconsistently without a dictionary.
- Overclaiming: broader examples may imply support before enough events exist.
- Sparse market data: many geopolitical events will lack clean event-firm return rows.
- Ambiguous event dates: military, cyber, shipping, and sanctions events may unfold over multiple dates.
- Duplicates: announcement, enforcement, retaliation, and market-reaction dates can be confused.
- Retrieval mismatch: current classification and scoring logic may not fully exploit future V2 fields until a later code sprint.
- Documentation burden: broader coverage requires stronger source and coding discipline.

## Expected Challenges

- Defining event boundaries for multi-day crises.
- Separating direct events from background geopolitical tension.
- Assigning geography when events have global or supply-chain effects.
- Coding affected companies without drifting into investment recommendations.
- Distinguishing sanctions, export controls, procurement bans, and industrial policy.
- Maintaining deterministic rules while expanding vocabulary.
- Preventing example questions from outpacing actual coded data coverage.

## Recommended First Expansion Category

Recommended first expansion category: Taiwan military tension.

Reasoning:

- It is strategically important and recruiter-relevant.
- It connects naturally to the current semiconductor validation dataset.
- It exposes the current system's most important coverage gap.
- It can test whether the workflow handles geopolitical tension beyond industrial policy.
- It supports later expansion into shipping disruption, defense, insurance, and regional-market exposure.

Recommended pilot scope:

- 8-12 Taiwan military-tension events.
- Include military exercises, escalation episodes, blockade-risk signals, diplomatic triggers, and de-escalation events.
- Code event-date confidence carefully.
- Separate military-tension events from semiconductor-policy events unless the source directly links them.
- Add market rows only where event dates and affected assets are defensible.

Second recommended category: Shipping and maritime disruption.

Reasoning:

- It is adjacent to Taiwan tension and supply-chain risk.
- It broadens the system beyond semiconductors while remaining analytically concrete.
- It adds portfolio relevance for logistics, energy, commodities, and inflation-sensitive sectors.

## Readiness Verdict

V2 dataset expansion is ready for schema-design and pilot-coding preparation.

The repository should not expand source logic until a pilot dataset exposes a concrete need. The next sprint should focus on coding standards, event templates, category dictionary use, and a small reviewed candidate-event set.
