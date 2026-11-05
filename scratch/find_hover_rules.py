with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Find rules matching .hero-buttons, .footer-catalog-btn, .btn-outline, .btn-primary
selectors = ['.hero-buttons .btn', '.footer-catalog-btn', '.btn-outline', '.btn-primary']

for s in selectors:
    print(f"\n==================== RULES FOR {s} ====================")
    matches = re.findall(rf'([^{{\n]*{re.escape(s)}[^{{\n]*\{{[^}}]*\}})', css)
    for m in matches:
        if 'hover' in m:
            print("[HOVER]", m.strip())
        elif 'transition' in m or 'transform' in m:
            print("[TRANSFORM/TRANSITION]", m.strip())

