with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if any(k in l for k in ['.footer-catalog', '.hero-buttons', 'footer .btn']):
        print(f"Line {i+1}: {l.strip()}")

