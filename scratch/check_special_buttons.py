import glob
import re

targets = [
    'btn-listen',
    'copy-asset-btn',
    'copy-coupon-btn',
    'promo-ticker-code-btn',
    'promo-ticker-shop-btn',
    'pod-filter-btn',
    'pod-plat-btn',
    'btn-subscribe',
    'open-catalog-modal',
    'open-gift-notify',
    'open-rsvp-modal',
    'btn-sm'
]

with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

for t in targets:
    pos = 0
    found = False
    while True:
        idx = css.find('.' + t, pos)
        if idx == -1:
            break
        found = True
        end = css.find('}', idx)
        print(f"[{t}] found in style.css:")
        print(css[idx:end+1].strip())
        print("-" * 30)
        pos = end + 1
    if not found:
        print(f"[{t}] NOT found in style.css directly")

