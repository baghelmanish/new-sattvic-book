from PIL import Image

img = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\.user_uploaded\media_1793806192784_1b49f971.jpg')
w, h = img.size

# Let's crop the CTA section very precisely
# Image size is 341 x 1024
# CTA section is around y = 880 to 960
cta_crop = img.crop((10, int(h * 0.88), w - 10, int(h * 0.95)))
# Resize with bicubic to 4x size so we can see text clearly
cta_large = cta_crop.resize((cta_crop.width * 4, cta_crop.height * 4), Image.Resampling.LANCZOS)
cta_large.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\cta_large.png')

# Footer crop
footer_crop = img.crop((0, int(h * 0.95), w, h))
footer_large = footer_crop.resize((footer_crop.width * 4, footer_crop.height * 4), Image.Resampling.LANCZOS)
footer_large.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\footer_large.png')

print("Saved cta_large.png and footer_large.png")

