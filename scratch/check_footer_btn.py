import numpy as np
from PIL import Image

f_img = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\footer_large.png')
print("Footer dimensions:", f_img.size)

# Let's inspect CTA buttons specifically
cta_img = Image.open(r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\scratch\cta_large.png')
print("CTA dimensions:", cta_img.size)

