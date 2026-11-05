import glob
import re

for h in glob.glob(r'd:\Sattvic Books\*.html'):
    fname = h.split('\\')[-1]
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.findall(r'class=["\'][^"\']*header-bg[^"\']*["\']', content)
    if m:
        print(f"[{fname}] {m}")

