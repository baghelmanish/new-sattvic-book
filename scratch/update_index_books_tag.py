with open(r'd:\Sattvic Books\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '<section class="books section-padding" id="books" style="background: linear-gradient(180deg, #F7E9DC 0%, #F3E5D0 50%, #FAE6CE 100%);">'
replacement = '<section class="books section-padding" id="books">'

if target in html:
    html = html.replace(target, replacement)
    with open(r'd:\Sattvic Books\index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully removed inline peach background from #books in index.html!")
else:
    print("Target tag not found in index.html!")

