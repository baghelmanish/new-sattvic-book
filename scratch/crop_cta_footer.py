from PIL import Image

img = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\.user_uploaded\media_1793806192784_1b49f971.jpg')
w, h = img.size
print(f"Image dimensions: {w}x{h}")

# In media_1793806192784_1b49f971.jpg:
# Get Started section is near the bottom, before footer
# Footer is at the very bottom
crop_cta = img.crop((0, int(h * 0.88), w, int(h * 0.96)))
crop_cta.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\crop_reference_cta.jpg')

crop_footer = img.crop((0, int(h * 0.95), w, h))
crop_footer.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\crop_reference_footer.jpg')

print("Cropped CTA and Footer from reference image successfully!")

