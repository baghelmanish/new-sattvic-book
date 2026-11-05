with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for sel in ['header {', 'header.', '.page-header', '.hero', 'header ']:
    pos = 0
    while True:
        idx = text.find(sel, pos)
        if idx == -1:
            break
        print(f"=== Match for {sel} at {idx} ===")
        print(text[idx:idx+250].strip())
        print("-" * 30)
        pos = idx + len(sel)

