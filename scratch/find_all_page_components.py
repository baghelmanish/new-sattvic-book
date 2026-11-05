import glob
import re

card_classes = set()
section_classes = set()
hero_classes = set()

for h in glob.glob(r'd:\Sattvic Books\*.html'):
    fname = h.split('\\')[-1]
    if fname in ['podcast_backup.html']:
        continue
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for tag in re.findall(r'<section[^>]*class=["\']([^"\']+)["\']', content):
        section_classes.update(tag.split())
    
    for tag in re.findall(r'<div[^>]*class=["\']([^"\']+)["\']', content):
        for c in tag.split():
            if any(k in c.lower() for k in ['card', 'tile', 'box', 'item', 'channel', 'partner', 'event', 'asset']):
                card_classes.add(c)
            if 'hero' in c.lower() or 'banner' in c.lower():
                hero_classes.add(c)

print("Section classes found:")
print(sorted(section_classes))
print("\nHero/Banner classes found:")
print(sorted(hero_classes))
print("\nCard/Box classes found:")
print(sorted([c for c in card_classes if 'card' in c or 'box' in c or 'tile' in c]))

