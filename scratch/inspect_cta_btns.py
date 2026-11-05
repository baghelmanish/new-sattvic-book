from PIL import Image

# Let's crop specifically around the buttons in the CTA area
img = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\crop_reference_cta.jpg')
w, h = img.size

# Left box button (Get Started)
# Right box button (Stay Connected)
print(f"CTA crop size: {w}x{h}")

# Save zoomed-in buttons
btn_left = img.crop((0, int(h * 0.5), int(w * 0.5), h))
btn_left.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\crop_cta_btn_left.jpg')

btn_right = img.crop((int(w * 0.5), int(h * 0.5), w, h))
btn_right.save(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\crop_cta_btn_right.jpg')

# Footer crop
f_img = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\crop_reference_footer.jpg')
fw, fh = f_img.size
print(f"Footer crop size: {fw}x{fh}")

