with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

def get_rules(selector):
    return [m for m in re.findall(rf'([^{{\n]*{re.escape(selector)}[^{{\n]*\{{[^}}]*\}})', css)]

print("=== s-btn-add rules ===")
for r in get_rules('.s-btn-add'):
    print(r.strip()[:180])
    print("---")

print("\n=== hero-buttons .btn rules ===")
for r in get_rules('.hero-buttons .btn'):
    print(r.strip()[:180])
    print("---")

print("\n=== footer-catalog-btn rules ===")
for r in get_rules('.footer-catalog-btn'):
    print(r.strip()[:180])
    print("---")

