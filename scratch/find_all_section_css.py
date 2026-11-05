with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for sel in ['.collections', '.books', '.why-buy-section', '.gift-store-section', '.freebies-section', '.cta', '.footer']:
    pos = 0
    print(f"=== Matches for {sel} ===")
    while True:
        idx = text.find(sel, pos)
        if idx == -1:
            break
        # print snippet
        end = text.find('}', idx)
        if end != -1 and end - idx < 500:
            print(f"At {idx}:")
            print(text[idx:end+1].strip())
            print("---")
        pos = idx + len(sel)

