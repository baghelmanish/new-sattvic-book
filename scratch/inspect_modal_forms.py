with open(r'd:\Sattvic Books\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
catalog_modal = re.search(r'id="catalogModal"[^>]*>(.*?)id="giftNotifyModal"', html, re.DOTALL)
if catalog_modal:
    print("Catalog modal buttons & inputs:")
    for b in re.findall(r'<(?:button|input)[^>]*>', catalog_modal.group(1)):
        print("  ", b)

gift_modal = re.search(r'id="giftNotifyModal"[^>]*>(.*?)id="actionModal"', html, re.DOTALL)
if gift_modal:
    print("Gift modal buttons & inputs:")
    for b in re.findall(r'<(?:button|input)[^>]*>', gift_modal.group(1)):
        print("  ", b)

