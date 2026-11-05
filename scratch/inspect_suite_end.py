with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('UNIFIED LUXURY BUTTON SUITE')
print(text[idx:])

