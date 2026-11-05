import glob
import re

html_files = sorted(glob.glob(r'd:\Sattvic Books\*.html'))
print(f"Total HTML files: {len(html_files)}")

for h in html_files:
    fname = h.split('\\')[-1]
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for inline styles with background or color
    inline_styles = re.findall(r'style=["\']([^"\']*(?:background|color|#)[^"\']*)["\']', content, re.IGNORECASE)
    print(f"\n[{fname}] - Inline styles with bg/color: {len(inline_styles)}")
    for s in inline_styles[:5]:
        print(f"   style='{s.strip()[:80]}'")
    if len(inline_styles) > 5:
        print(f"   ... and {len(inline_styles)-5} more")

