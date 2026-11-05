import os, re

html_files = [f for f in os.listdir("D:/Sattvic Books") if f.endswith(".html") and not f.startswith("podcast")]
ids_per_file = {}
links_per_file = {}

for hf in html_files:
    path = os.path.join("D:/Sattvic Books", hf)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # find all IDs
    ids = set(re.findall(r'id=["\']([^"\']+)["\']', content))
    ids_per_file[hf] = ids
    # find all hrefs
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    links_per_file[hf] = hrefs

print("--- CHECKING INTERNAL HASH ANCHORS ---")
broken_anchors = 0
for hf, hrefs in links_per_file.items():
    for link in hrefs:
        if link.startswith("#") and len(link) > 1:
            target_id = link[1:]
            if target_id not in ids_per_file[hf]:
                print(f"Broken local anchor in {hf}: {link}")
                broken_anchors += 1
        elif "#" in link and not link.startswith("http") and not link.startswith("mailto:") and not link.startswith("tel:"):
            parts = link.split("#")
            target_page = parts[0]
            target_id = parts[1]
            if target_page in ids_per_file:
                if target_id and target_id not in ids_per_file[target_page]:
                    print(f"Broken cross-page anchor from {hf} to {link}")
                    broken_anchors += 1

if broken_anchors == 0:
    print("ALL ANCHOR LINKS AND HASH TARGETS ARE 100% VALID!")

