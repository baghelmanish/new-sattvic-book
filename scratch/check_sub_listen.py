import glob
import re

for html_file in glob.glob(r'd:\Sattvic Books\*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'btn-subscribe' in content:
        print(f"btn-subscribe in {html_file}")
    if 'btn-listen' in content:
        print(f"btn-listen in {html_file}")

