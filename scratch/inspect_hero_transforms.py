with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for sel in ['.hero-content', '.hero-text', '.hero']:
    matches = re.findall(rf'([^{{\n]*{re.escape(sel)}[^{{\n]*\{{[^}}]*\}})', text)
    for m in matches:
        if 'hover' in m or 'transform' in m or 'transition' in m or 'animation' in m:
            print(m.strip()[:200])
            print("---")

