for fname in ['privacy-policy.html', 'terms-of-service.html', 'shipping-returns.html']:
    print(f"================ {fname} ================")
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    import re
    # find text in main or legal-card
    match = re.search(r'<div class="legal-content-card">(.*?)</div>\s*</div>\s*</main>', text, re.DOTALL)
    if match:
        content = match.group(1)
        # remove tags for a clean preview
        clean = re.sub(r'<[^>]+>', ' ', content)
        clean = ' '.join(clean.split())
        print(clean[:500])
    else:
        print("Not found, first 300 chars:")
        print(text[:300])

