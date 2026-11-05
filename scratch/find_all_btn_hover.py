with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

matches = re.findall(r'(\.btn[^{]*:hover[^{]*\{[^}]*\})', css)
print(f"Total .btn:hover rules: {len(matches)}")
for m in matches:
    print(m.strip())
    print("-" * 30)

hero_matches = re.findall(r'(\.hero[^{]*:hover[^{]*\{[^}]*\})', css)
print(f"Total .hero:hover rules: {len(hero_matches)}")
for m in hero_matches:
    print(m.strip())
    print("-" * 30)

