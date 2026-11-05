import os, re

html_files = [f for f in os.listdir("D:/Sattvic Books") if f.endswith(".html") and not f.startswith("podcast")]

print("=== DEEP AUDIT OF ALL PUBLIC PAGES ===")
all_passed = True

for hf in html_files:
    path = os.path.join("D:/Sattvic Books", hf)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Check images
    img_matches = re.findall(r'<img([^>]+)>', content)
    for img_attr in img_matches:
        # Check src
        src_m = re.search(r'src=["\']([^"\']+)["\']', img_attr)
        if not src_m or not src_m.group(1).strip():
            print(f"[{hf}] Error: <img> tag missing src!")
            all_passed = False
        else:
            src = src_m.group(1).strip()
            if not src.startswith("http") and not src.startswith("data:"):
                local_path = os.path.join("D:/Sattvic Books", src.replace("/", "\\"))
                if not os.path.exists(local_path):
                    print(f"[{hf}] Error: Missing local image file: {src}")
                    all_passed = False
        # Check alt
        alt_m = re.search(r'alt=["\']([^"\']*)["\']', img_attr)
        if not alt_m:
            print(f"[{hf}] Warning: <img> tag missing alt attribute in: {img_attr[:50]}")

    # 2. Check title and meta description
    if "<title>" not in content:
        print(f"[{hf}] Error: Missing <title> tag!")
        all_passed = False
    if 'name="description"' not in content:
        print(f"[{hf}] Warning: Missing meta description!")

    # 3. Check for empty links href=""
    empty_links = re.findall(r'<a\s+[^>]*href=["\']\s*["\']', content)
    if empty_links:
        print(f"[{hf}] Warning: Found {len(empty_links)} empty href links!")
        all_passed = False

if all_passed:
    print("ALL 9 PUBLIC PAGES PASSED THE DEEP AUDIT 100%!")

