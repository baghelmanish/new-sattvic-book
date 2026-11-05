import glob
import re

internal_pages = ['about.html', 'contact.html', 'events.html', 'media-press.html', 'press-kit.html', 'press-releases.html', 'reading-partners.html', 'press-release-diwali-launch.html']

for p in internal_pages:
    path = f'd:\\Sattvic Books\\{p}'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    print(f"\n==================== BANNER IN {p} ====================")
    # Find header or hero section
    header_m = re.search(r'(<(?:header|section|div)[^>]*(?:hero|banner|header)[^>]*>.*?</(?:header|section|div)>)', html, re.DOTALL | re.IGNORECASE)
    if header_m:
        print(header_m.group(0)[:600])
    else:
        # search first section
        first_sec = re.search(r'(<section[^>]*>.*?</section>)', html, re.DOTALL | re.IGNORECASE)
        if first_sec:
            print(first_sec.group(0)[:600])

