import glob
import re

for h in sorted(glob.glob(r'd:\Sattvic Books\*.html')):
    fname = h.split('\\')[-1]
    if fname == 'podcast_backup.html':
        continue
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # footer button
    footer_btns = re.findall(r'<a[^>]*footer-catalog-btn[^>]*>(.*?)</a>', content, re.DOTALL)
    if footer_btns:
        print(f"[{fname}] Footer button text: {[re.sub(r'<[^>]+>', '', b).strip() for b in footer_btns]}")
    
    # Get Started or CTA button
    cta_matches = re.findall(r'(Get Started.*?<a[^>]*class=["\'][^"\']*btn[^"\']*["\'][^>]*>(.*?)</a>)', content, re.DOTALL)
    if cta_matches:
        for full, b in cta_matches:
            clean_btn = re.sub(r'<[^>]+>', '', b).strip()
            print(f"[{fname}] Get Started button text: '{clean_btn}'")

