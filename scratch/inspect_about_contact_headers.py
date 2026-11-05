with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

for sel in ['about-header', 'contact-header']:
    matches = re.findall(rf'([^{{\n]*{re.escape(sel)}[^{{\n]*\{{[^}}]*\}})', css)
    print(f"=== Matches for {sel}: {len(matches)} ===")
    for m in matches:
        print(m.strip()[:250])
        print("---")

