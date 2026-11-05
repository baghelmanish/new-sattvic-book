with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

for sel in ['.hero-buttons', '.footer-catalog-btn', '.btn:hover', '.hero .btn']:
    pos = 0
    print(f"=== CSS matching {sel} ===")
    while True:
        idx = css.find(sel, pos)
        if idx == -1:
            break
        end = css.find('}', idx)
        print(css[idx:end+1].strip())
        print("---")
        pos = end + 1

