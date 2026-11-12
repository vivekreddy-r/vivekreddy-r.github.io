# Portfolio audit and implementation plan

Inspected 12 November 2026: https://v1vekreddy.github.io/ and the publishing
branch of v1vekreddy/v1vekreddy.github.io. Public project evidence inspected in
v1vekreddy/self-rag. Existing resume and the user's supplied work descriptions
are the sources for employer work. No private implementation is published.

## Existing strengths to preserve

- Static HTML/CSS and a small theme script; no framework or build dependency.
- IM Fell English SC name, Inter body, Lora section headings.
- White/charcoal themes, underlined blue links, compact navigation.
- Working Drive resume, contact links, semantic sections, readable prose.

## Prioritized findings

1. Intro and Experience repeat OCR, RAG, and speech content. Replace the repeated
   intro with a concise engineering proposition and route readers to projects.
2. Projects have no detail pages or evidence links. Add structured summaries,
   factual architecture schematics, and dedicated case studies. Link only
   verified public code. Distinguish company work from open source.
3. GitHub links use an obsolete username. Update them to v1vekreddy.
4. Skills and a compact contact destination are absent. Add categorized,
   demonstrated skills and a short contact block rather than a badge wall.
5. Head markup lacks a canonical, Open Graph/Twitter preview, and structured
   person data. Add these for the current public hostname.
6. Remote font CSS adds a discovery round trip. Self-host the same font families,
   preload the distinctive name face, and retain swap/fallback rendering.

## Implementation sequence

1. Preserve existing CSS tokens and typography; refine spacing and calls to action.
2. Add project data, reusable case-study template, and generated static pages.
3. Tighten experience prose, separate About, and add Skills and Contact.
4. Validate static links, themes, keyboard access, mobile overflow, metadata,
   asset loading, and performance. Publish through the existing gh-pages source.

## Evidence and publication boundaries

- OCR, RAG evaluation, LiveKit transcription, and research-assistant descriptions
   come from supplied work/resume material; they are not independently benchmarked.
- Only the Self-RAG project currently has a verified matching public repository.
- QA automation is company work. Stack, scope, outcomes, and implementation have
   not been provided: do not invent them or add a source-code link.
- No new numerical business-impact claim will be introduced. Existing qualitative
   outcomes are distinguished from measured evaluation results.
- Schematics are explanatory diagrams, not screenshots of a private product.
