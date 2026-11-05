import glob

html_files = sorted(glob.glob(r'd:\Sattvic Books\*.html'))

replacements = [
    ('#FAF7F2', '#FAF6EE'),
    ('#2C1E14', '#382618'),
    ('#6A5A4D', '#5E4A39'),
    ('#A07C32', '#855E20'),
    ('#4A3319', '#322214'),
    ('#382413', '#322214'),
    ('#E2C27E', '#D7B347'),
]

total_mods = 0
for h in html_files:
    fname = h.split('\\')[-1]
    if fname in ['podcast_backup.html']:
        continue
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig = content
    for old, new in replacements:
        content = content.replace(old, new)
    
    if content != orig:
        with open(h, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fname} successfully!")
        total_mods += 1
    else:
        print(f"No changes needed in {fname}")

print(f"\nTotal files updated: {total_mods}")

