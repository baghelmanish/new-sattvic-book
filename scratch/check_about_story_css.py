with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'\.about-story-section[^{]*\{[^}]*\}', text)
for m in matches:
    print(m)

