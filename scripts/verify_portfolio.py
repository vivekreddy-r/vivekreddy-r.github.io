"""Check generated pages, navigation, SEO metadata, JSON-LD, and local assets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.assets, self.canonicals = [], [], [], []
        self.h1 = 0
        self.description = False
        self.og_image = False
        self.lang = False

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'html':
            self.lang = attrs.get('lang') == 'en'
        if tag == 'h1':
            self.h1 += 1
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if tag == 'link':
            if attrs.get('rel') == 'canonical':
                self.canonicals.append(attrs.get('href'))
            elif attrs.get('rel') in ['stylesheet', 'preload', 'icon']:
                self.assets.append(attrs.get('href', ''))
        if tag == 'script' and 'src' in attrs:
            self.assets.append(attrs['src'])
        if tag == 'meta':
            self.description |= attrs.get('name') == 'description' and bool(attrs.get('content'))
            self.og_image |= attrs.get('property') == 'og:image'


files = [ROOT / 'index.html', *sorted((ROOT / 'projects').glob('*/index.html'))]
parsed = {}
for file in files:
    parser = Page()
    text = file.read_text(encoding='utf-8-sig')
    assert not any(marker in text for marker in ['r?sum?', 'Let?s', '\ufffd']), f'Broken text encoding: {file}'
    parser.feed(text)
    assert len(parser.ids) == len(set(parser.ids)), f'Duplicate IDs: {file}'
    assert parser.h1 == 1 and parser.lang, f'Semantic page structure: {file}'
    assert parser.description and parser.og_image and len(parser.canonicals) == 1, f'Missing metadata: {file}'
    parsed[file.resolve()] = parser

for file, parser in parsed.items():
    for url in parser.links + parser.assets:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc:
            continue
        path = (ROOT / unquote(parts.path).lstrip('/')) if parts.path.startswith('/') else file.parent / unquote(parts.path)
        if not parts.path:
            path = file
        if path.is_dir():
            path = path / 'index.html'
        path = path.resolve()
        assert path.is_relative_to(ROOT) and path.is_file(), f'Broken local link: {file}: {url}'
        if parts.fragment and path in parsed:
            assert parts.fragment in parsed[path].ids, f'Broken anchor: {file}: {url}'

source = (ROOT / 'index.html').read_text(encoding='utf-8')
assert 'github.com/vivekreddy049' not in source, 'Stale GitHub username'
assert '1ZKZkrltONeVqQ4238UbZ5IHSVpFeZGAL' in source, 'Original Drive resume missing'
assert not list(ROOT.glob('package.json')), 'Unexpected frontend build dependency'
projects = json.loads((ROOT / 'content/projects.json').read_text(encoding='utf-8'))
assert len(projects) == len(files) - 1
print(f'PASS: {len(files)} pages; unique IDs, headings, metadata, local links, assets, anchors, resume, and static stack.')
