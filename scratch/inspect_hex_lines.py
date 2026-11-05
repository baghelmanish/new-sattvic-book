import glob
import re

for h in sorted(glob.glob(r'd:\Sattvic Books\*.html')):
    fname = h.split('\\')[-1]
    if fname in ['podcast_backup.html', 'podcast.html', 'index.html']:
        continue
    with open(h, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"\n==================== {fname} ====================")
    for i, line in enumerate(lines):
        if any(c in line for c in ['#FAF7F2', '#2C1E14', '#6A5A4D', '#A07C32', '#4A3319']):
            print(f"Line {i+1}: {line.strip()[:110]}")

