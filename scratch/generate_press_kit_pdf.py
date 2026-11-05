import os
from PIL import Image, ImageDraw, ImageFont

def create_press_kit():
    w, h = 1240, 1754  # A4 at ~150 DPI
    im = Image.new("RGB", (w, h), color="#FAF6EE")
    draw = ImageDraw.Draw(im)

    # Outer ornate gold double border
    draw.rectangle([(40, 40), (w - 40, h - 40)], outline="#D7B347", width=3)
    draw.rectangle([(48, 48), (w - 48, h - 48)], outline="#855E20", width=1)

    # Fonts
    f_title = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 36)
    f_subtitle = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 22)
    f_h2 = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 24)
    f_body_bold = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 16)
    f_body = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 15)
    f_small = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 13)

    # Load & Paste Logo
    logo_path = "D:/Sattvic Books/assets/sattvic-books-logo.png"
    y = 80
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        lw, lh = logo.size
        target_h = 100
        target_w = int(lw * (target_h / lh))
        logo = logo.resize((target_w, target_h), Image.Resampling.LANCZOS)
        # paste with transparency
        lx = (w - target_w) // 2
        im.paste(logo, (lx, y), mask=logo)
        y += target_h + 20

    # Title Banner
    draw.text((w // 2, y), "SATTVIC BOOKS", font=f_title, fill="#382618", anchor="mm")
    y += 35
    draw.text((w // 2, y), "OFFICIAL PRESS KIT & MEDIA PACK (2026)", font=f_subtitle, fill="#855E20", anchor="mm")
    y += 25
    draw.text((w // 2, y), "Wisdom Unfolding — Literature for Mindful, Conscious Living", font=f_body, fill="#5E4A39", anchor="mm")
    y += 30

    # Decorative divider
    draw.line([(100, y), (w - 100, y)], fill="#D7B347", width=2)
    y += 30

    # Section 1: Overview
    draw.text((100, y), "1. BRAND OVERVIEW & PUBLISHING MISSION", font=f_h2, fill="#382618")
    y += 35
    overview_text = [
        "Sattvic Books is a dedicated publishing house committed to creating conscious literature that nourishes",
        "the intellect, expands spiritual awareness, and grounds daily life in timeless principles. Inspired by India's",
        "profound philosophical heritage, our publications present ancient Vedic wisdom, wellness practices, and mindful",
        "living in clear, accessible, and beautifully produced editions for contemporary global readers."
    ]
    for line in overview_text:
        draw.text((100, y), line, font=f_body, fill="#5E4A39")
        y += 22
    y += 20

    # Section 2: Core Philosophical Tenets
    draw.text((100, y), "2. CORE PHILOSOPHICAL TENETS", font=f_h2, fill="#382618")
    y += 35
    tenets = [
        ("Satya (Truth):", "Authentic translation and faithful preservation of traditional wisdom and spiritual teachings."),
        ("Dharma (Righteous Living):", "Ethical literature that promotes mindful conduct, compassion, and inner integrity."),
        ("Seva (Selfless Service):", "Publishing to uplift communities, support schools, and cultivate conscious reading circles."),
        ("Abhyasa (Dedicated Practice):", "Practical spiritual disciplines, daily rituals, mantras, and wholesome recipes for everyday life.")
    ]
    for t_title, t_desc in tenets:
        draw.text((120, y), t_title, font=f_body_bold, fill="#855E20")
        draw.text((360, y), t_desc, font=f_body, fill="#5E4A39")
        y += 25
    y += 20

    # Section 3: Featured Catalog Titles
    draw.text((100, y), "3. FEATURED PUBLICATIONS & CORE RELEASES", font=f_h2, fill="#382618")
    y += 35
    books = [
        ("Sri Lakshmi Chaturvimsati Namavali", "Sacred Sanskrit 24 Names of Goddess Lakshmi with meaning & chanting guides."),
        ("Meghadootam by Kalidasa", "Classic poetic Sanskrit masterpiece translated into accessible prose and verse."),
        ("Navadurga: Sacred Coloring Journey", "Devotional, meditative coloring and contemplation book celebrating the Divine Mother."),
        ("High-Protein Sattvic Recipes", "Wholesome, plant-based, prana-rich Ayurvedic culinary guide for modern vitality.")
    ]
    for b_title, b_desc in books:
        draw.text((120, y), f"•  {b_title}:", font=f_body_bold, fill="#382618")
        draw.text((450, y), b_desc, font=f_body, fill="#5E4A39")
        y += 25
    y += 20

    # Section 4: Founder Biography
    draw.text((100, y), "4. LEADERSHIP & FOUNDER", font=f_h2, fill="#382618")
    y += 35
    bio_lines = [
        "Founded by Dr. Rani Iyer, author, researcher, and conscious lifestyle practitioner.",
        "Under her leadership, Sattvic Books bridges classical scholarship with experiential wellness,",
        "inspiring thousands of families to embrace mindful living and spiritual grounding."
    ]
    for line in bio_lines:
        draw.text((100, y), line, font=f_body, fill="#5E4A39")
        y += 22
    y += 25

    # Section 5: Media & Editorial Contact Box (Dark card)
    box_top = y
    box_bottom = y + 180
    draw.rectangle([(90, box_top), (w - 90, box_bottom)], fill="#322214", outline="#D7B347", width=2)
    by = box_top + 25
    draw.text((w // 2, by), "MEDIA, INTERVIEWS & EDITORIAL INQUIRIES", font=f_subtitle, fill="#FAF6EE", anchor="mm")
    by += 32
    draw.text((w // 2, by), "Press Inquiries: info@thesattvicmethodcompany.com  |  Editorial: editor@sattvicbooks.com", font=f_body, fill="#FAF6EE", anchor="mm")
    by += 28
    draw.text((w // 2, by), "Official Website: https://sattvicbooks.com  |  Headquarters: India & USA", font=f_body, fill="#D7B347", anchor="mm")
    by += 28
    draw.text((w // 2, by), "Digital Press Assets, Headshots & High-Res Covers: https://sattvicbooks.com/press-kit.html", font=f_small, fill="#FAF6EE", anchor="mm")

    # Bottom footer text
    draw.text((w // 2, h - 60), "© 2026 Sattvic Books | The Sattvic Method Company. All Rights Reserved.", font=f_small, fill="#855E20", anchor="mm")

    output_path = "D:/Sattvic Books/assets/press-pack-sample.pdf"
    im.save(output_path, "PDF", resolution=150.0)
    print(f"Generated press pack PDF successfully at {output_path} (Size: {os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    create_press_kit()

