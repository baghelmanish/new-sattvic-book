with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for m in re.finditer(r'hero-buttons[^{]*\{[^}]*\}', text):
    print(m.group(0).strip())
    print("-" * 30)

for m in re.finditer(r'\.hero[^{]*\.btn[^{]*\{[^}]*\}', text):
    print(m.group(0).strip())
    print("-" * 30)

