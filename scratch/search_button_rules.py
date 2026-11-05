with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for old button declarations in style.css
keywords = [
    '.btn-primary {',
    '.btn-outline {',
    '.btn-secondary {',
    '.btn-gold {',
    '.s-btn-add {',
    '.btn-add-cart',
    '.bd-add-btn',
    '.btn-gift-notify',
    '.catalog-filter-btn.active'
]

for kw in keywords:
    pos = 0
    while True:
        idx = text.find(kw, pos)
        if idx == -1:
            break
        print(f"=== Keyword: {kw} at char {idx} ===")
        print(text[idx:idx+350])
        print("----------------------------")
        pos = idx + len(kw)

