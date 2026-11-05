import glob

html_files = sorted(glob.glob(r'd:\Sattvic Books\*.html'))

replacements = {
    '#FAF7F2': '#FAF6EE',
    '#2C1E14': '#382618',
    '#6A5A4D': '#5E4A39',
    '#A07C32': '#855E20',
    '#4A3319': '#322214',
    '#382413': '#322214',
    '#E2C27E': '#D7B347',
}

for h in html_files:
    fname = h.split('\\')[-1]
    if fname in ['podcast_backup.html']:
        continue
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = 0
    for old, new in replacements.items():
        c = content.count(old)
        if c > 0:
            count += c
            print(f"[{fname}] {old} -> {new} ({c} times)")
    if count == 0:
        print(f"[{fname}] No replacements needed")

