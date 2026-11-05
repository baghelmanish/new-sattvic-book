with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

selectors_to_check = [
    '--clr-primary',
    '--clr-bg',
    '--clr-text',
    '.collections {',
    '.collections-header',
    '.books {',
    '.s-bookshelf-section',
    '.s-book-card',
    '.collection-card',
    '.why-buy-section',
    '.why-buy-card',
    '.gift-store-section',
    '.gift-store-card',
    '.freebies-section',
    '.freebie-card',
    '.cta {',
    '.cta-box',
    '.footer {'
]

for sel in selectors_to_check:
    idx = css.find(sel)
    print(f"=== {sel} (found at {idx}) ===")
    if idx != -1:
        print(css[idx:idx+250].strip())
    print("-" * 30)

