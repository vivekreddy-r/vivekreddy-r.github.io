"""Generate static case studies and project summaries from verified project notes.

Standard library only. Run from the repository root: python scripts/build_case_studies.py
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = json.loads((ROOT / "content/projects.json").read_text(encoding="utf-8"))
BASE = "https://v1vekreddy.github.io/"
RESUME = "https://drive.google.com/file/d/1ZKZkrltONeVqQ4238UbZ5IHSVpFeZGAL/view?usp=sharing"


def esc(value):
    return html.escape(str(value), quote=True)


def flow(items, compact=False):
    if not items:
        return ""
    if compact and len(items) > 3:
        items = [items[0], items[len(items) // 2], items[-1]]
    return '<ol class="architecture-flow' + (' compact-flow' if compact else '') + '" aria-label="Workflow architecture">' + ''.join(f'<li><span>{esc(item)}</span></li>' for item in items) + '</ol>'


def card(project, featured=False):
    url = f'projects/{project["slug"]}/'
    tags = ' · '.join(esc(tool) for tool in project['stack'])
    sources = ''.join(f'<a href="{esc(item["url"])}" target="_blank" rel="noopener noreferrer">{esc(item["label"])} ↗</a>' for item in project['sources'][:1])
    return f'''<article class="project-entry {'featured-project' if featured else 'project-row'}">
      <p class="project-meta">{esc(project['category'])}<span aria-hidden="true"> / </span><span>{esc(project['status'])}</span></p>
      <h3><a href="{url}">{esc(project['title'])}</a></h3>
      <p class="project-summary">{esc(project['summary'])}</p>
      {flow(project['flow'], True) if featured else ''}
      {f'<p class="project-tools">{tags}</p>' if tags else ''}
      <div class="project-links"><a href="{url}">{'Project overview' if project.get('limited') else 'Read case study'} <span aria-hidden="true">→</span></a>{sources}</div>
    </article>'''


def case_page(project):
    title, summary = esc(project['title']), esc(project['summary'])
    url = BASE + f'projects/{project["slug"]}/'
    source_links = ''.join(f'<a class="action-link" href="{esc(item["url"])}" target="_blank" rel="noopener noreferrer">{esc(item["label"])} ↗</a>' for item in project['sources'])
    if project.get('limited'):
        content = '''<section class="company-note" aria-labelledby="public-scope"><h2 id="public-scope">Company work</h2><p>I built an AI-powered QA automation agent as part of my company work. The source code and internal workflows are not published here.</p><p><a href="mailto:vivekreddyiitg@gmail.com">Get in touch</a> to discuss my contribution and the details I can share.</p></section>'''
    else:
        implementation = ''.join(f'<li>{esc(item)}</li>' for item in project['implementation'])
        content = f'''<section><h2>The problem</h2><p>{esc(project['problem'])}</p></section>
        <section><h2>System architecture</h2><p>{esc(project['approach'])}</p><figure class="architecture-figure">{flow(project['flow'])}<figcaption>Workflow schematic based on documented project notes. This is not a product screenshot.</figcaption></figure></section>
        <section><h2>Implementation</h2><ul class="case-points">{implementation}</ul></section>
        <section class="case-columns"><div><h2>Technical challenges</h2><p>{esc(project['challenges'])}</p></div><div><h2>Decisions &amp; trade-offs</h2><p>{esc(project['tradeoffs'])}</p></div></section>
        <section><h2>Evaluation &amp; outcomes</h2><p>{esc(project['outcome'])}</p></section>
        <section><h2>Evidence</h2><p>{esc(project['evidence'])}</p><div class="case-source-links">{source_links}</div></section>'''
    stack = ' · '.join(esc(item) for item in project['stack'])
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} | Vivek Reddy</title><meta name="description" content="{summary}" />
<link rel="canonical" href="{url}" />
<meta property="og:type" content="article" /><meta property="og:title" content="{title} | Vivek Reddy" /><meta property="og:description" content="{summary}" /><meta property="og:url" content="{url}" /><meta property="og:image" content="{BASE}assets/social-preview.png" />
<meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="{title} | Vivek Reddy" /><meta name="twitter:description" content="{summary}" /><meta name="twitter:image" content="{BASE}assets/social-preview.png" />
{'<meta name="robots" content="noindex, follow" />' if project.get('limited') else ''}
<link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml" />
<link rel="preload" href="../../assets/fonts/name.woff2" as="font" type="font/woff2" crossorigin />
<script src="../../theme.js?v=theme-2"></script><link rel="stylesheet" href="../../profile.css?v=portfolio-20261112" />
</head><body class="case-study-page">
<a class="skip-link" href="#main-content">Skip to content</a>
<header><div class="profile"><div><a class="site-name" href="../../">Vivek Reddy</a><p class="role">AI and ML Engineer · IIT Guwahati</p></div><div class="header-actions"><button class="theme-toggle" type="button" aria-label="Switch to dark mode" hidden><span aria-hidden="true">◐</span></button><a class="resume-link" href="{RESUME}" target="_blank" rel="noopener noreferrer">résumé ↗</a></div></div><nav class="main-navigation" aria-label="Case study navigation"><a href="../../#projects">← All projects</a><a href="../../#experience">Experience</a><a href="../../#contact">Contact</a></nav></header>
<main id="main-content" tabindex="-1"><article class="case-study"><header class="case-header"><p class="eyebrow">{esc(project['category'])} / {esc(project['status'])}</p><h1>{title}</h1><p class="intro-lead">{summary}</p>{f'<p class="project-tools">{stack}</p>' if stack else ''}</header>{content}</article></main>
<footer><p>© 2026 Vivek Reddy. <a href="../../#projects">Back to projects</a></p></footer></body></html>'''


def main():
    first = ''.join(card(project, True) for project in PROJECTS[:2])
    rest = ''.join(card(project) for project in PROJECTS[2:])
    block = f'''<!-- PROJECTS_START -->
    <section id="projects" aria-labelledby="projects-heading">
      <div class="section-heading"><h2 id="projects-heading">Selected engineering work</h2><p>Document intelligence, grounded answers, and real-time AI workflows.</p></div>
      <div class="featured-grid">{first}</div>
      <div class="project-list">{rest}</div>
    </section>
    <!-- PROJECTS_END -->'''
    homepage = ROOT / 'index.html'
    result = re.sub(r'<!-- PROJECTS_START -->.*?<!-- PROJECTS_END -->', lambda _: block, homepage.read_text(encoding='utf-8'), flags=re.S)
    homepage.write_text('\n'.join(line.rstrip() for line in result.splitlines()) + '\n', encoding='utf-8', newline='\n')
    for project in PROJECTS:
        directory = ROOT / 'projects' / project['slug']
        directory.mkdir(parents=True, exist_ok=True)
        (directory / 'index.html').write_text(case_page(project), encoding='utf-8', newline='\n')
    review = '# Content to verify\n\nThese are editorial tasks, not claims made by the site.\n\n'
    for project in PROJECTS:
        review += f'## {project["title"]}\n\n' + ''.join(f'- [ ] {item}\n' for item in project['verify']) + '\n'
    review += '## Profile\n\n- [ ] Confirm graduation month: current site says April 2026; supplied resume image says May 2026.\n- [ ] Confirm that the current role remains AI/ML Intern and July 2026 is the correct start date.\n- [ ] Confirm public viewing/download access to the supplied Drive resume.\n- [ ] Guardrails is not listed as a standalone skill: no specific guardrails tool or implementation was supplied.\n'
    (ROOT / 'CONTENT_REVIEW.md').write_text(review, encoding='utf-8', newline='\n')
    urls = [BASE] + [BASE + f'projects/{p["slug"]}/' for p in PROJECTS if not p.get('limited')]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{url}</loc></url>' for url in urls) + '</urlset>\n'
    (ROOT / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
    print(f'Generated {len(PROJECTS)} case studies, project summaries, sitemap, and content review checklist.')


if __name__ == '__main__':
    main()
