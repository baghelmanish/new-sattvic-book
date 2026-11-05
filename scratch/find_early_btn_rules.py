with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for sel in ['open-catalog-modal', '.btn-outline', '.btn-primary', '.hero-buttons']:
    matches = re.findall(rf'([^{{\n]*{re.escape(sel)}[^{{\n]*\{{[^}}]*\}})', text)
    print(f"=== Matches for {sel}: {len(matches)} ===")
    for m in matches:
        print(m.strip()[:160])
        print("---")

