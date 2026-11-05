import glob, re

files = glob.glob(r'd:\Sattvic Books\*.html')
pat = re.compile(r'<(?:a|button)\s+[^>]*class="[^"]*btn[^"]*"[^>]*style="([^"]+)"', re.DOTALL)

for fpath in files:
    if 'backup' in fpath: continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    fname = fpath.split('\\')[-1]
    matches = pat.findall(content)
    if matches:
        print(f'=== {fname}: {len(matches)} buttons with inline style ===')
        for s in matches[:4]:
            print('   style:', s.strip()[:80])

