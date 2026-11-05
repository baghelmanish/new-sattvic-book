with open("D:/Sattvic Books/index.html", "r", encoding="utf-8") as f:
    text = f.read()

old_str = '<a href="#" class="floating-vertical-btn open-catalog-modal" title="Download 2026 Catalog (PDF)" aria-label="Download Free 2026 Catalog">'
new_str = '<a href="#catalogModal" class="floating-vertical-btn open-catalog-modal" title="Download 2026 Catalog (PDF)" aria-label="Download Free 2026 Catalog">'

if old_str in text:
    text = text.replace(old_str, new_str)
    with open("D:/Sattvic Books/index.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully updated index.html!")
else:
    print("old_str not found in index.html!")

