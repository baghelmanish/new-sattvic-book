with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for sel in ['header', 'about', 'contact']:
    m = re.findall(rf'(\.{sel}[^{{\n]*\{{[^}}]*\}})', text)
    print(f"Matches for .{sel}: {len(m)}")
    for item in m[:5]:
        print("  ", item.strip()[:100])

