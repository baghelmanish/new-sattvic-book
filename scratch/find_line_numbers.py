with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def find_lines(pattern):
    import re
    res = []
    for idx, l in enumerate(lines):
        if re.search(pattern, l):
            res.append((idx + 1, l.rstrip()))
    return res

print("btn-primary lines:", find_lines(r'^\.btn-primary\b'))
print("btn-outline lines:", find_lines(r'^\.btn-outline\b'))
print("btn-add-cart lines:", find_lines(r'\.btn-add-cart\b'))
print("catalog-filter-btn.active lines:", find_lines(r'\.catalog-filter-btn\.active\b'))

