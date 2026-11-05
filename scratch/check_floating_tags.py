import os, re

html_files = [f for f in os.listdir("D:/Sattvic Books") if f.endswith(".html") and not f.startswith("podcast")]
for hf in html_files:
    with open(os.path.join("D:/Sattvic Books", hf), "r", encoding="utf-8") as f:
        c = f.read()
    m = re.search(r'<a[^>]*class=["\'][^"\']*floating-vertical-btn[^"\']*["\'][^>]*>', c)
    if m:
        print(hf, "->", m.group(0))

