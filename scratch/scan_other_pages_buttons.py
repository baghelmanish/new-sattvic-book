import glob
import re

for html_file in sorted(glob.glob(r'd:\Sattvic Books\*.html')):
    fname = html_file.split('\\')[-1]
    if fname in ['index.html', 'about.html', 'contact.html', 'events.html']:
        continue
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n==================== {fname} ====================")
    for m in re.finditer(r'<(?:button|a)\s+([^>]*?)>(.*?)</(?:button|a)>', content, re.DOTALL | re.IGNORECASE):
        attrs, inner = m.groups()
        class_m = re.search(r'class=["\']([^"\']+)["\']', attrs)
        cname = class_m.group(1) if class_m else ''
        text_clean = re.sub(r'<[^>]+>', '', inner).strip()
        if 'btn' in cname or 'pill' in cname:
            print(f"  class='{cname}' -> '{text_clean[:40]}'")

