with open(r'd:\Sattvic Books\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Get Started
cta_idx = text.find('id="community"')
print('=== CTA SECTION ===')
print(text[cta_idx:cta_idx+1500])

# Footer
footer_idx = text.find('<footer')
print('\n=== FOOTER SECTION ===')
print(text[footer_idx:footer_idx+1500])

