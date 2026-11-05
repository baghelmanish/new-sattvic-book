with open(r'd:\Sattvic Books\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
modals = re.findall(r'<div[^>]*modal[^>]*>.*?</div>\s*</div>', html, re.DOTALL | re.IGNORECASE)
print(f"Modals count: {len(modals)}")
for m in modals:
    print(m[:300])
    btns = re.findall(r'<(?:button|a)[^>]*>.*?</(?:button|a)>', m)
    for b in btns:
        print("   Modal btn:", b)
    print("=" * 40)

