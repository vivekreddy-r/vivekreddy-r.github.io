"""Regenerate the typography-only social image. Requires Pillow and fonttools[woff]."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

root = Path(__file__).resolve().parents[1]
out = root.parent / 'output' / 'portfolio-audit'
out.mkdir(parents=True, exist_ok=True)
for family in ['name', 'body', 'heading']:
    font = TTFont(root / 'assets' / 'fonts' / (family + '.woff2'))
    font.flavor = None
    font.save(out / (family + '.ttf'))

image = Image.new('RGB', (1200, 630), '#ffffff')
draw = ImageDraw.Draw(image)
name = ImageFont.truetype(str(out / 'name.ttf'), 76)
headline = ImageFont.truetype(str(out / 'heading.ttf'), 42)
body = ImageFont.truetype(str(out / 'body.ttf'), 25)
small = ImageFont.truetype(str(out / 'body.ttf'), 21)
draw.text((72, 65), 'Vivek Reddy', font=name, fill='#161a22')
draw.text((76, 176), 'AI / ML ENGINEER · IIT GUWAHATI', font=small, fill='#526170')
draw.line((76, 238, 1124, 238), fill='#d9dde4', width=2)
draw.text((76, 290), 'Building AI systems that work', font=headline, fill='#161a22')
draw.text((76, 352), 'beyond the prototype.', font=headline, fill='#161a22')
draw.text((76, 456), 'Document intelligence · LLM workflows · Real-time AI', font=body, fill='#526170')
draw.text((76, 548), 'v1vekreddy.github.io', font=small, fill='#183ba2')
image.save(root / 'assets' / 'social-preview.png', optimize=True)
print('Generated 1200 x 630 social preview.')
