from PIL import Image

# Let's inspect the Get Started section in media_1793806192784_1b49f971.jpg
im = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\.user_uploaded\media_1793806192784_1b49f971.jpg')
w, h = im.size

# The CTA area is from y = 880 to 950
# Let's crop with high precision and save at 8x scale with high contrast
cta_box = im.crop((15, int(h * 0.885), int(w * 0.5), int(h * 0.945)))
cta_box_large = cta_box.resize((cta_box.width * 8, cta_box.height * 8), Image.Resampling.LANCZOS)
cta_box_large.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\get_started_large.png')

# Now let's crop footer
footer_box = im.crop((10, int(h * 0.95), int(w * 0.4), int(h * 0.99)))
footer_box_large = footer_box.resize((footer_box.width * 8, footer_box.height * 8), Image.Resampling.LANCZOS)
footer_box_large.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\footer_brand_large.png')

print("Saved get_started_large.png and footer_brand_large.png")

