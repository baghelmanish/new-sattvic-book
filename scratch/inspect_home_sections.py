with open(r'd:\Sattvic Books\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Find all section tags and their classes/ids in index.html
sections = re.findall(r'<section[^>]*>', html, re.IGNORECASE)
for s in sections:
    print(s)

footer = re.search(r'<footer[^>]*>', html, re.IGNORECASE)
if footer:
    print(footer.group(0))

