import glob
import re

for h in sorted(glob.glob(r'd:\Sattvic Books\*.html')):
    fname = h.split('\\')[-1]
    if fname in ['podcast_backup.html', 'podcast.html', 'index.html']:
        continue
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sections = re.findall(r'<section[^>]*>', content, re.IGNORECASE)
    print(f"\n==================== {fname} ({len(sections)} sections) ====================")
    for s in sections:
        print("  ", s[:120])

