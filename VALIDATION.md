# Portfolio improvement report

Implemented 12 November 2026. The existing static site, typography, blue links,
light/dark themes, and Google Drive resume destination are preserved.

## Before and after

| Area | Before | After |
| --- | --- | --- |
| Introduction | Work details repeated Experience | Concise engineering proposition, IIT background, project/resume/social actions |
| Projects | Two brief text summaries | Two featured projects, four compact entries, six linked detail pages |
| Evidence | No project evidence links | Verified Self-RAG source and tests; explanatory workflow schematics; explicit boundaries for company work |
| Experience | Long descriptions overlapping About | Two paragraphs focused on delivered OCR, speech, and retrieval integrations |
| Skills | No dedicated section | Four categories tied to demonstrated work |
| Contact | Header links only | Header links retained and a compact, directly addressable contact destination |
| Technical | Remote font CSS, stale GitHub URL, limited social metadata | Same fonts self-hosted with licenses; current GitHub links; canonical, social image, Person schema, sitemap and robots |

## Files and reusable pieces

- `index.html`: hero, navigation, project summaries, experience, skills, contact, metadata, skip link.
- `profile.css`: existing tokens retained; responsive cards, workflow diagrams, detail pages, focus and reduced-motion styles.
- `theme.js`: existing behavior retained without adding a runtime dependency.
- `content/projects.json`: project content, evidence links, and editorial verification tasks.
- `scripts/build_case_studies.py`: reusable static card/detail-page templates and sitemap/checklist generation.
- `projects/*/index.html`: six generated pages. The limited QA company overview is excluded from indexing and sitemap until a substantive write-up is available.
- `assets/`: licensed local fonts, favicon, and a typography-based social image rather than a fabricated product screenshot.
- `scripts/verify_portfolio.py`: static site integrity checks.
- `scripts/prepare_assets.py`: optional social-image authoring tool; not needed to serve or deploy the site.

## Verification

- Static generation and validation passed for seven pages: local links/assets,
  anchors, unique IDs, one H1 per page, language, descriptions, canonicals, and social metadata.
- `node --check theme.js` and `git diff --check` passed.
- 36 browser checks passed using Playwright and axe, installed outside the publishing repository.
- No automated WCAG A/AA violations found on the homepage in light/dark modes or on all six detail pages in mobile layout. This is not a full accessibility certification.
- Keyboard skip navigation, saved theme preference, and reduced-motion behavior passed.
- No horizontal overflow at 320, 390, 768, 1024, and 1440 pixels; six detail pages also checked at mobile width.
- No browser runtime errors. Desktop, mobile, dark-mode, detail-page, and social-image renders inspected.
- No frontend dependency, lint configuration, or bundler existed. The Python generator is the relevant build step; no framework build or configured lint command is available.

Initial Lighthouse mobile lab runs:

| Metric | Existing live site | Updated local site |
| --- | ---: | ---: |
| Performance | 99 | 96 |
| Accessibility | 100 | 100 |
| Best practices | 96 | 100 |
| SEO | 91 | 100 |
| Largest contentful paint | 1.8 s | 1.2 s |
| Cumulative layout shift | 0 | 0 |
| Total blocking time | 0 ms | 220 ms |

These runs use simulated mobile conditions, and the origins differ. They do not
establish a performance improvement or regression, and are not field Core Web Vitals.
Raw JSON, functional-check results, and screenshots are retained in the workspace's
`output/portfolio-audit/` directory. A live post-deployment check is recorded separately there.

### Published-site verification

GitHub Pages deployment succeeded for implementation commit `9a2e647`.
All 36 browser checks also passed against https://v1vekreddy.github.io/.
The homepage, six project pages, three fonts, social image, robots, and sitemap
returned HTTP 200 (13 checks). The published homepage contains the new headline.

Post-deployment Lighthouse mobile run: **Performance 98, Accessibility 100,
Best Practices 100, SEO 100**. FCP/LCP: 1.1 s; CLS: 0; TBT: 140 ms.
These are one-run lab measurements; short CPU tasks and test-host load can vary.
Scores do not establish full accessibility compliance or real-user performance.

## Content requiring verification and next improvements

See `CONTENT_REVIEW.md` for the complete per-project checklist. Highest priorities:

1. Approved company examples and a concise shareable QA-agent contribution summary.
2. Reproducible evaluation sets, configuration, and real results before adding numerical claims.
3. Matching repositories or shareable artifacts for the evaluation framework and research assistant.
4. Graduation month (existing site: April; supplied resume: May), internship dates/title, and Drive public-access permissions.

Only the Self-RAG repository currently has matched public source evidence. The
company QA entry has no invented stack, public repository, or result. No Zepto
dates, achievements, or recommendation-project implementation were added without evidence.
External source links were checked against the public repository; LinkedIn and
Drive access policies cannot be established from a successful HTTP response alone.
The resume opens the supplied Drive viewer, where downloading depends on its owner settings.
