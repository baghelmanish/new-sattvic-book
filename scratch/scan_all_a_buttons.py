import glob
import re

a_buttons = []
for html_file in glob.glob(r'd:\Sattvic Books\*.html'):
    fname = html_file.split('\\')[-1]
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # find all <a> tags
    for m in re.finditer(r'<a\s+([^>]*?)>(.*?)</a>', content, re.DOTALL | re.IGNORECASE):
        attrs, inner = m.groups()
        class_m = re.search(r'class=["\']([^"\']+)["\']', attrs)
        cname = class_m.group(1) if class_m else ''
        text_clean = re.sub(r'<[^>]+>', '', inner).strip()
        # if class has btn or text looks like an action
        if 'btn' in cname or any(c in cname for c in ['pill', 'action', 'cta']) or any(kw in text_clean.lower() for kw in ['catalog', 'details', 'shop', 'explore', 'download', 'listen', 'subscribe', 'rsvp', 'register', 'contact']):
            a_buttons.append((fname, cname, text_clean[:35]))

print(f"Total action links found: {len(a_buttons)}")
print("\nSample of action links across pages:")
for fname, cname, text in a_buttons[:40]:
    print(f"[{fname}] class='{cname}' -> '{text}'")

