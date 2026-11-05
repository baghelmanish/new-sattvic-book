import re

for fname in [r'd:\Sattvic Books\press-kit.html', r'd:\Sattvic Books\reading-partners.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # replace footer button with standard single-line new button
    pattern = r'<a href="#catalogModal" class="btn footer-catalog-btn open-catalog-modal"><i\s+class="fa-solid fa-file-pdf"></i> Download Free Catalog</a>'
    new_btn = '<a href="#catalogModal" class="btn footer-catalog-btn open-catalog-modal"><i class="fa-solid fa-file-pdf"></i> Download 2026 Catalog (PDF)</a>'
    
    sub_text, count = re.subn(pattern, new_btn, text)
    if count > 0:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(sub_text)
        print(f"Updated {fname} footer button ({count} times)!")
    else:
        print(f"No match in {fname}")

