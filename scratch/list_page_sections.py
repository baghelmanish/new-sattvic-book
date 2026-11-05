import glob
import re

internal_pages = ['about.html', 'contact.html', 'events.html', 'media-press.html', 'press-kit.html', 'press-releases.html', 'reading-partners.html', 'press-release-diwali-launch.html']

for p in internal_pages:
    path = f'd:\\Sattvic Books\\{p}'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    print(f"\n==================== SECTIONS IN {p} ====================")
    sections = re.findall(r'<section([^>]*)>', html, re.IGNORECASE)
    for i, s in enumerate(sections):
        print(f"  Section {i+1}: {s.strip()[:100]}")

