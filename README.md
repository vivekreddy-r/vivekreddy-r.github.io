# Vivek Reddy — Personal Portfolio

Personal website for Vivek Reddy, AI and ML Engineer and IIT Guwahati graduate.

The site uses HTML, CSS, and JavaScript with saved light/dark preferences.
The resume opens in Google Drive. Contact and social links are in the header.

Live website: https://v1vekreddy.github.io/

GitHub Pages publishes the root of the gh-pages branch.

## Local preview and editing

Run `python -m http.server 8000` and open http://localhost:8000/.
There is no frontend package install or framework build step.

- Edit profile, experience, skills, and contact in `index.html`.
- Edit project content in `content/projects.json`, then run `python scripts/build_case_studies.py`.
- The generator updates the homepage project list, six static detail pages, sitemap, and `CONTENT_REVIEW.md`.
- Run `python scripts/verify_portfolio.py` to check local links, headings, assets, and metadata.
- `profile.css` contains shared design tokens and responsive styles; `theme.js` manages saved light/dark preferences.
- Fonts are self-hosted in `assets/fonts/`, with their licenses. `assets/social-preview.png` is the social sharing image.
- Optional asset regeneration: install Pillow and fonttools with Brotli support, then run `python scripts/prepare_assets.py`. These are authoring tools, not website dependencies.

See `AUDIT.md`, `VALIDATION.md`, and `CONTENT_REVIEW.md` for findings, validation results, and outstanding content tasks. Company projects have no invented public repository or metrics.
