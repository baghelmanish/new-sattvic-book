with open(r'd:\Sattvic Books\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('aria-label="View Details for Gaurianesh (Spiral Edition)"', 'aria-label="View Details for Gauri Ganesh (Spiral Edition)"')

with open(r'd:\Sattvic Books\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Typo fixed successfully!')

