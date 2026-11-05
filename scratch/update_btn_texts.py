import re
import glob

# 1. Update HTML files for Button Texts
html_files = sorted(glob.glob(r'd:\Sattvic Books\*.html'))

old_footer_btn = '<a href="#catalogModal" class="btn footer-catalog-btn open-catalog-modal"><i class="fa-solid fa-file-pdf"></i> Download Free Catalog</a>'
new_footer_btn = '<a href="#catalogModal" class="btn footer-catalog-btn open-catalog-modal"><i class="fa-solid fa-file-pdf"></i> Download 2026 Catalog (PDF)</a>'

old_cta_btn = '<a href="https://web.mytiny.us/sattvic-books/shop/" class="btn btn-primary"><i class="fa-solid fa-book-open"></i> Explore Our Catalog <i class="fa-solid fa-arrow-right"></i></a>'
new_cta_btn = '<a href="https://web.mytiny.us/sattvic-books/shop/" class="btn btn-primary"><i class="fa-solid fa-compass"></i> Begin Your Journey <i class="fa-solid fa-arrow-right"></i></a>'

for h in html_files:
    fname = h.split('\\')[-1]
    if fname == 'podcast_backup.html':
        continue
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    if old_footer_btn in content:
        content = content.replace(old_footer_btn, new_footer_btn)
        modified = True
        print(f"[{fname}] Updated footer button text!")
    
    if fname == 'index.html' and old_cta_btn in content:
        content = content.replace(old_cta_btn, new_cta_btn)
        modified = True
        print(f"[{fname}] Updated Get Started button text to 'Begin Your Journey'!")
    
    if modified:
        with open(h, 'w', encoding='utf-8') as f:
            f.write(content)

print("HTML Button text updates complete!")

