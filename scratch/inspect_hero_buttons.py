with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '.hero-buttons' in l or '.hero .btn' in l:
        print(f"Line {i+1}: {l.strip()}")
        for j in range(max(0, i-2), min(len(lines), i+12)):
            print(f"  {j+1}: {lines[j].strip()}")
        print("=" * 40)

