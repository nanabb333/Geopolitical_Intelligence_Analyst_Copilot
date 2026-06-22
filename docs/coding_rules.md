# Coding Rules

These rules govern future event selection and coding for multi-domain geopolitical dataset expansion. They protect the project from overclaiming, duplicate events, weak sourcing, and inconsistent field usage.

## Event Selection Rules

- Select events with a clear geopolitical, policy, security, or strategic-economics trigger.
- Prefer events with identifiable dates and public documentation.
- Prioritize events that can plausibly support scenario classification, historical analogue retrieval, pathway generation, or market-reaction comparison.
- Do not include routine market moves without a geopolitical event trigger.
- Do not include forecasts, rumors, or speculative scenarios as historical events.
- Do not add events solely because they fit a desired conclusion.

## Event Inclusion Standards

An event should be included only when:

- The event has at least one credible source.
- The event date can be identified with at least medium confidence.
- The category and subcategory can be coded using the event dictionary.
- The event has a plausible market, sector, supply-chain, security, or strategic relevance.
- Coding notes can explain why the event belongs in the dataset.

Events should be held for review when:

- Source evidence is incomplete.
- Event timing is ambiguous.
- The event overlaps heavily with another coded event.
- Sector or category classification is uncertain.
- The event is important but not yet codable with current fields.

## Source Quality Standards

Preferred source hierarchy:

1. Official government, regulator, company, exchange, or international organization source.
2. Major financial or international news organization.
3. Specialist trade publication with clear sourcing.
4. Academic, think-tank, or research note for background context.
5. Secondary commentary only when used as context, not as the sole event source.

Source requirements:

- Every included event must include a primary source URL where possible.
- If no official source exists, explain the source limitation in `coding_notes`.
- Record the source access date when practical.
- Do not rely on social media posts as sole evidence unless they are official statements.

## Duplicate Event Handling

- Do not create separate records for multiple articles about the same event.
- Use the original announcement, enforcement action, or material update as the primary event record.
- Use `related_event_id` for later implementation details, revisions, or follow-on actions.
- Use `duplicate_group_id` when several records are intentionally grouped.
- If a follow-on event materially changes policy scope, enforcement, geography, or market relevance, it may receive a separate event ID.

## Ambiguous Event Handling

- Use `unknown` rather than forcing a field value.
- Add an analyst caveat when event category, geography, market channel, or affected firms are uncertain.
- Mark event-date confidence as `low` when timing is approximate.
- Hold ambiguous events for review if they would materially affect retrieval quality.
- Prefer conservative coding over broad interpretation.

## Missing Data Rules

- Required fields should not be blank.
- Use `unknown` for unknown text values.
- Use `none_identified` when no companies or assets are identified.
- Use `not_applicable` when a field does not apply to the event type.
- Missing market-return data should not block event inclusion, but it must be visible in later market comparison output.
- Do not infer company impact or market direction without source or coding rationale.

## Documentation Standards

Every coded event should include:

- clear event name;
- source URL;
- category and subcategory;
- event-date confidence;
- strategic significance rationale;
- market relevance rationale;
- coding notes;
- analyst caveat.

Dataset documentation should be updated when:

- a new category is introduced;
- a controlled value is added;
- inclusion or exclusion rules change;
- duplicate handling creates a new convention;
- validation identifies recurring ambiguity.
