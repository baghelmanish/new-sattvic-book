import glob
import re

for h in sorted(glob.glob(r'd:\Sattvic Books\*.html')):
    fname = h.split('\\')[-1]
    if fname in ['podcast_backup.html', 'podcast.html']:
        continue
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check old background colors
    old_bg = re.findall(r'#FAF7F2|#F5E8D6|#F7E9DC|#F5ECDB|#2C1E14|#6A5A4D|#A07C32|#4A3319', content)
    if old_bg:
        print(f"[{fname}] found old hex codes: {set(old_bg)}")

