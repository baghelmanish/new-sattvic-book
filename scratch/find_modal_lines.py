with open(r'd:\Sattvic Books\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'modal' in l.lower():
        print(f"Line {i+1}: {l.strip()[:100]}")

