with open("D:/Sattvic Books/events.html", "r", encoding="utf-8") as f:
    text = f.read()

old_sec5 = """        <!-- Section 5: Be Part of What's Next! -->
        <section class="section-padding" style="background-color: #FFFFFF;">
            <div class="container" style="max-width: 860px;">
                <div class="next-event-cta-box fade-in-up text-center">
                    <div class="next-event-cta-inner">
                        <span class="eyebrow" style="color: var(--clr-gold-dark, #855E20); letter-spacing: 2px; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; display: block; margin-bottom: 0.8rem;">Upcoming Community</span>
                        <h2 style="color: #382618; font-size: 2.6rem; margin-bottom: 1.2rem; font-family: 'Playfair Display', Georgia, serif;">Be Part of What's Next!</h2>
                        <p style="color: #5C4A3E; font-size: 1.15rem; line-height: 1.8; margin-bottom: 1rem;">
                            A meaningful experience can begin with a single conversation, a new story, or an idea that inspires you.
                        </p>
                        <p style="color: #5E4A39; font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.5rem;">
                            Stay connected with Sattvic Books to discover upcoming workshops, special gatherings, book launches, and learning opportunities.
                        </p>
                        <p style="color: #855E20; font-size: 1.35rem; font-family: 'Playfair Display', Georgia, serif; font-style: italic; font-weight: 600; margin-bottom: 2rem;">
                            Don't just read about inspiration. Experience it!
                        </p>
                        <div>
                            <a href="contact.html" class="btn btn-primary">
                                <i class="fa-solid fa-calendar-check" style="margin-right: 0.5rem;"></i> Explore Events &amp; Register Today
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

new_sec5 = """        <!-- Section 5: Upcoming Community (Signature Dark Mode Design) -->
        <section class="section-padding" style="background-color: #FFFFFF;">
            <div class="container" style="max-width: 860px;">
                <div class="next-event-cta-box fade-in-up text-center" style="background: linear-gradient(135deg, #322214 0%, #4A3319 50%, #20150D 100%) !important; border: 1.5px solid rgba(215, 179, 71, 0.45) !important; border-radius: 20px; padding: 4rem 2.5rem; position: relative; overflow: hidden; box-shadow: 0 16px 45px rgba(32, 21, 13, 0.28) !important; color: #FFFFFF !important;">
                    <div class="next-event-cta-inner" style="position: relative; z-index: 1;">
                        <span class="eyebrow text-gold" style="color: #D7B347 !important; letter-spacing: 2.5px; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; display: block; margin-bottom: 0.8rem;">Upcoming Community</span>
                        <h2 style="color: #FFFFFF !important; font-size: 2.6rem; margin-bottom: 1.2rem; font-family: 'Playfair Display', Georgia, serif;">Be Part of What's Next!</h2>
                        <p style="color: rgba(255, 255, 255, 0.95) !important; font-size: 1.15rem; line-height: 1.8; margin-bottom: 1rem;">
                            A meaningful experience can begin with a single conversation, a new story, or an idea that inspires you.
                        </p>
                        <p style="color: rgba(255, 255, 255, 0.88) !important; font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.5rem;">
                            Stay connected with Sattvic Books to discover upcoming workshops, special gatherings, book launches, and learning opportunities.
                        </p>
                        <p style="color: #F1D487 !important; font-size: 1.35rem; font-family: 'Playfair Display', Georgia, serif; font-style: italic; font-weight: 600; margin-bottom: 2rem;">
                            Don't just read about inspiration. Experience it!
                        </p>
                        <div>
                            <a href="contact.html" class="btn btn-primary">
                                <i class="fa-solid fa-calendar-check" style="margin-right: 0.5rem;"></i> Explore Events &amp; Register Today
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

if old_sec5 in text:
    text = text.replace(old_sec5, new_sec5)
    print("Replaced with LF")
elif old_sec5.replace("\n", "\r\n") in text:
    text = text.replace(old_sec5.replace("\n", "\r\n"), new_sec5.replace("\n", "\r\n"))
    print("Replaced with CRLF")
else:
    print("Could not match old_sec5 directly, please verify!")

with open("D:/Sattvic Books/events.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated events.html successfully!")

