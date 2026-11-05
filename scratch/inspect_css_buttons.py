import re

with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

classes_to_check = [
    'copy-asset-btn',
    'copy-coupon-btn',
    'promo-ticker',
    'pod-filter-btn',
    'pod-plat-btn',
    'btn-listen',
    'btn-subscribe'
]

for c in classes_to_check:
    print(f"=== Matches for {c} ===")
    matches = re.findall(rf'(\.[^{{\n]*{c}[^{{\n]*\{{[^}}]*\}})', css)
    for m in matches[:3]:
        print(m[:300])
        print("---")

