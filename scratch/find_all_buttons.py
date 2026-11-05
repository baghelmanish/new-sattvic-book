import glob
import re

button_classes = set()
button_tags = []

for html_file in glob.glob(r'd:\Sattvic Books\*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # buttons
    for m in re.finditer(r'<button([^>]*)>(.*?)</button>', content, re.DOTALL | re.IGNORECASE):
        attrs, inner = m.groups()
        class_m = re.search(r'class=["\']([^"\']+)["\']', attrs)
        cname = class_m.group(1) if class_m else 'NO_CLASS'
        button_tags.append((html_file.split('\\')[-1], 'button', cname, inner.strip()[:40]))
        if class_m:
            button_classes.update(class_m.group(1).split())
            
    # links styled as buttons
    for m in re.finditer(r'<a([^>]*)>(.*?)</a>', content, re.DOTALL | re.IGNORECASE):
        attrs, inner = m.groups()
        class_m = re.search(r'class=["\']([^"\']+)["\']', attrs)
        if class_m and any(k in class_m.group(1) for k in ['btn', 'button']):
            cname = class_m.group(1)
            button_tags.append((html_file.split('\\')[-1], 'a', cname, inner.strip()[:40]))
            button_classes.update(cname.split())

print("Unique button classes found across all pages:")
for c in sorted(button_classes):
    print(f"  - {c}")

print(f"\nTotal button / btn-styled elements: {len(button_tags)}")
