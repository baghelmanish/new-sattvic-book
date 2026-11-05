# 1. Update media-press.html
with open("D:/Sattvic Books/media-press.html", "r", encoding="utf-8") as f:
    mp = f.read()

old_mp = """        <!-- Our Diwali Launch Section -->
        <section class="section-padding" style="background-color: #FAF6EE; border-top: 1px solid rgba(44, 30, 20, 0.06); border-bottom: 1px solid rgba(44, 30, 20, 0.06);">
            <div class="container" style="max-width: 900px;">
                <div class="fade-in-up text-center" style="background: linear-gradient(135deg, #322214 0%, #322214 100%); color: #FFFFFF; padding: 3.2rem 2.8rem; border-radius: 14px; border: 1px solid rgba(197, 160, 89, 0.35); box-shadow: 0 10px 30px rgba(56, 36, 19, 0.18);">
                    <span class="eyebrow text-gold" style="letter-spacing: 2.2px;">Festival of Lights</span>
                    <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.3rem; color: #FFFFFF; margin-bottom: 1.2rem;">Our Diwali Launch</h2>
                    <div style="margin: 0 auto 1.6rem; max-width: 480px; border-radius: 10px; overflow: hidden; border: 1px solid rgba(197, 160, 89, 0.4); box-shadow: 0 6px 20px rgba(0,0,0,0.25);">
                        <img src="assets/diwali-launch-celebration.jpg" alt="Sattvic Books Diwali Launch" style="width: 100%; height: auto; display: block; max-height: 220px; object-fit: cover; object-position: center top;">
                    </div>
                    <p style="font-size: 1.15rem; line-height: 1.8; color: rgba(255, 255, 255, 0.95); margin-bottom: 1.4rem; max-width: 760px; margin-left: auto; margin-right: auto;">
                        Diwali celebrates the triumph of light over darkness and knowledge over ignorance. The launch of Sattvic Books during this auspicious season reflects our aspiration to make the light of knowledge available to more readers.
                    </p>
                    <p style="font-size: 1.25rem; line-height: 1.8; color: var(--clr-gold-light); font-style: italic; font-family: 'Playfair Display', Georgia, serif; margin-bottom: 0;">
                        Our invitation is simple: discover a book, explore an idea, share a story, and welcome more wisdom into your life.
                    </p>
                </div>
            </div>
        </section>"""

new_mp = """        <!-- Our Diwali Launch Section -->
        <section class="section-padding" style="background-color: #FAF6EE; border-top: 1px solid rgba(44, 30, 20, 0.06); border-bottom: 1px solid rgba(44, 30, 20, 0.06);">
            <div class="container" style="max-width: 900px;">
                <div class="dark-feature-card fade-in-up text-center" style="background: linear-gradient(135deg, #322214 0%, #20150D 100%) !important; color: #FFFFFF !important; padding: 3.5rem 2.8rem; border-radius: 16px; border: 1.5px solid rgba(215, 179, 71, 0.45) !important; box-shadow: 0 16px 45px rgba(32, 21, 13, 0.28) !important;">
                    <span class="eyebrow text-gold" style="letter-spacing: 2.4px; color: #D7B347 !important; font-weight: 700; text-transform: uppercase; font-size: 0.88rem; display: block; margin-bottom: 0.8rem;">Festival of Lights</span>
                    <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.4rem; color: #FFFFFF !important; margin-bottom: 1.4rem; font-weight: 700;">Our Diwali Launch</h2>
                    <div style="margin: 0 auto 1.8rem; max-width: 520px; border-radius: 12px; overflow: hidden; border: 1.5px solid rgba(215, 179, 71, 0.45); box-shadow: 0 8px 25px rgba(0,0,0,0.35);">
                        <img src="assets/diwali-launch-celebration.jpg" alt="Sattvic Books Diwali Launch" style="width: 100%; height: auto; display: block; max-height: 240px; object-fit: cover; object-position: center top;">
                    </div>
                    <p style="font-size: 1.15rem; line-height: 1.85; color: rgba(255, 255, 255, 0.95) !important; margin-bottom: 1.4rem; max-width: 760px; margin-left: auto; margin-right: auto;">
                        Diwali celebrates the triumph of light over darkness and knowledge over ignorance. The launch of Sattvic Books during this auspicious season reflects our aspiration to make the light of knowledge available to more readers.
                    </p>
                    <p style="font-size: 1.25rem; line-height: 1.8; color: #F1D487 !important; font-style: italic; font-family: 'Playfair Display', Georgia, serif; font-weight: 600; margin-bottom: 0;">
                        Our invitation is simple: discover a book, explore an idea, share a story, and welcome more wisdom into your life.
                    </p>
                </div>
            </div>
        </section>"""

if old_mp in mp:
    mp = mp.replace(old_mp, new_mp)
    print("Updated media-press.html (LF)")
elif old_mp.replace("\n", "\r\n") in mp:
    mp = mp.replace(old_mp.replace("\n", "\r\n"), new_mp.replace("\n", "\r\n"))
    print("Updated media-press.html (CRLF)")
else:
    print("Warning: could not match old_mp in media-press.html")

with open("D:/Sattvic Books/media-press.html", "w", encoding="utf-8") as f:
    f.write(mp)

# 2. Update press-release-diwali-launch.html
with open("D:/Sattvic Books/press-release-diwali-launch.html", "r", encoding="utf-8") as f:
    pr = f.read()

old_pr = """                        <!-- Special Diwali Discount Box -->
                        <div style="background: linear-gradient(135deg, #322214 0%, #322214 100%); color: #FFFFFF; padding: 2.2rem 2.4rem; border-radius: 12px; border: 1px solid rgba(197, 160, 89, 0.35); margin: 2.2rem 0; box-shadow: 0 8px 25px rgba(56, 36, 19, 0.15);">
                            <span class="eyebrow text-gold" style="letter-spacing: 2px;">Inauguration Offer</span>
                            <h2 style="color: #FFFFFF; font-size: 1.85rem; margin-top: 0.3rem; margin-bottom: 0.8rem;">A Diwali Gift to Readers: 10% Off All Books</h2>
                            <p style="color: rgba(255, 255, 255, 0.95); font-size: 1.08rem; line-height: 1.75; margin-bottom: 1rem;">
                                To celebrate the inauguration, Sattvic Books is offering readers a special 10% discount on all books from November 9, 2026, through January 14, 2027, concluding on the occasion of Makar Sankranti.
                            </p>
                            <p style="color: var(--clr-gold-light); font-size: 1.08rem; line-height: 1.75; margin-bottom: 0; font-style: italic;">
                                Whether readers are looking for a thoughtful holiday gift, an engaging book for a child, a practical cookbook, or a meaningful addition to their personal library, this is an opportunity to discover something that can continue giving long after the festive season.
                            </p>
                        </div>"""

new_pr = """                        <!-- Special Diwali Discount Box -->
                        <div class="dark-feature-card" style="background: linear-gradient(135deg, #322214 0%, #20150D 100%) !important; color: #FFFFFF !important; padding: 2.4rem 2.4rem; border-radius: 14px; border: 1.5px solid rgba(215, 179, 71, 0.45) !important; margin: 2.2rem 0; box-shadow: 0 12px 35px rgba(32, 21, 13, 0.22) !important;">
                            <span class="eyebrow text-gold" style="letter-spacing: 2.2px; color: #D7B347 !important; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; display: block; margin-bottom: 0.5rem;">Inauguration Offer</span>
                            <h2 style="color: #FFFFFF !important; font-size: 1.85rem; margin-top: 0.3rem; margin-bottom: 0.8rem; font-family: 'Playfair Display', Georgia, serif; font-weight: 700;">A Diwali Gift to Readers: 10% Off All Books</h2>
                            <p style="color: rgba(255, 255, 255, 0.95) !important; font-size: 1.08rem; line-height: 1.75; margin-bottom: 1rem;">
                                To celebrate the inauguration, Sattvic Books is offering readers a special 10% discount on all books from November 9, 2026, through January 14, 2027, concluding on the occasion of Makar Sankranti.
                            </p>
                            <p style="color: #F1D487 !important; font-size: 1.08rem; line-height: 1.75; margin-bottom: 0; font-style: italic; font-weight: 600;">
                                Whether readers are looking for a thoughtful holiday gift, an engaging book for a child, a practical cookbook, or a meaningful addition to their personal library, this is an opportunity to discover something that can continue giving long after the festive season.
                            </p>
                        </div>"""

if old_pr in pr:
    pr = pr.replace(old_pr, new_pr)
    print("Updated press-release-diwali-launch.html (LF)")
elif old_pr.replace("\n", "\r\n") in pr:
    pr = pr.replace(old_pr.replace("\n", "\r\n"), new_pr.replace("\n", "\r\n"))
    print("Updated press-release-diwali-launch.html (CRLF)")
else:
    print("Warning: could not match old_pr in press-release-diwali-launch.html")

with open("D:/Sattvic Books/press-release-diwali-launch.html", "w", encoding="utf-8") as f:
    f.write(pr)

# 3. Add High-Priority CSS for .dark-feature-card in style.css
with open("D:/Sattvic Books/style.css", "r", encoding="utf-8") as f:
    css = f.read()

dark_card_css = """
/* ==========================================================================
   DARK FEATURE CARDS & HIGHLIGHT BOXES (IMMUNITY FROM LIGHT-MODE OVERRIDES)
   ========================================================================== */
.dark-feature-card,
section .dark-feature-card,
section:not(.bg-dark) .dark-feature-card,
section:not(.bg-dark) .next-event-cta-box {
    background: linear-gradient(135deg, #322214 0%, #20150D 100%) !important;
    color: #FFFFFF !important;
}

.dark-feature-card .eyebrow,
section:not(.bg-dark) .dark-feature-card .eyebrow,
section:not(.bg-dark) .next-event-cta-box .eyebrow {
    color: #D7B347 !important;
    text-transform: uppercase !important;
    letter-spacing: 2.2px !important;
    font-weight: 700 !important;
}

.dark-feature-card h1,
.dark-feature-card h2,
.dark-feature-card h3,
.dark-feature-card h4,
section:not(.bg-dark) .dark-feature-card h1,
section:not(.bg-dark) .dark-feature-card h2,
section:not(.bg-dark) .dark-feature-card h3,
section:not(.bg-dark) .dark-feature-card h4,
section:not(.bg-dark) .next-event-cta-box h1,
section:not(.bg-dark) .next-event-cta-box h2,
section:not(.bg-dark) .next-event-cta-box h3,
section:not(.bg-dark) .next-event-cta-box h4 {
    color: #FFFFFF !important;
    font-family: var(--font-heading) !important;
}

.dark-feature-card p,
section:not(.bg-dark) .dark-feature-card p,
section:not(.bg-dark) .next-event-cta-box p {
    color: rgba(255, 255, 255, 0.95) !important;
    line-height: 1.8 !important;
}

.dark-feature-card p[style*="italic"],
.dark-feature-card .cta-quote,
section:not(.bg-dark) .dark-feature-card p[style*="italic"],
section:not(.bg-dark) .next-event-cta-box p[style*="italic"] {
    color: #F1D487 !important;
    font-style: italic !important;
}
"""

if "DARK FEATURE CARDS & HIGHLIGHT BOXES" not in css:
    css += dark_card_css
    with open("D:/Sattvic Books/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Added dark_card_css to style.css!")
else:
    print("dark_card_css already present in style.css")

