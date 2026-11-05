with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Check banner styles
print("=== BANNER TEXT STYLES IN CSS ===")
for cls in ['.about-header-bg', '.contact-header-bg', '.events-hero', '.press-header-bg']:
    has_h1 = f"{cls} h1" in css
    has_p = f"{cls} p" in css
    has_eyebrow = f"{cls} .eyebrow" in css
    print(f"{cls}: h1={has_h1}, p={has_p}, eyebrow={has_eyebrow}")

# Check section alternation styles
print("\n=== ALTERNATING SECTION STYLES IN CSS ===")
print("White sections:", 'section[style*="#FFFFFF"]' in css and '.about-story-section' in css)
print("Warm Cream sections:", 'section[style*="#FAF6EE"]' in css and '.collections' in css)
print("Soft Beige sections:", 'section[style*="#F6EBDD"]' in css and '.books' in css)
print("Dark sections:", '#322214' in css and '.footer' in css)

