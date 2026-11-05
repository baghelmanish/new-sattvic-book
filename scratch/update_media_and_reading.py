# scratch/update_media_and_reading.py

# 1. Update media-press.html
with open(r'd:\Sattvic Books\media-press.html', 'r', encoding='utf-8') as f:
    media_html = f.read()

idx_media = media_html.find('Interview &amp; Collaboration Requests')
if idx_media != -1:
    idx_start = media_html.rfind('<section', 0, idx_media)
    idx_end = media_html.find('</section>', idx_media)
    if idx_start != -1 and idx_end != -1:
        new_media_section = '''<section class="section-padding" style="background-color: #FAF7F2; border-top: 1px solid rgba(44, 30, 20, 0.06);">
            <div class="container" style="max-width: 860px;">
                <div class="conversation-closing-box fade-in-up text-center">
                    <span class="eyebrow" style="color: var(--clr-gold-dark, #A07C32); letter-spacing: 2px; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; display: block; margin-bottom: 0.6rem;">Connect With Us</span>
                    <h2 style="color: #2C1E14; font-size: 2.3rem; margin-bottom: 1.2rem; font-family: 'Playfair Display', Georgia, serif;">Interview &amp; Collaboration Requests</h2>
                    <p style="color: #5C4A3E; font-size: 1.12rem; line-height: 1.8; margin-bottom: 2rem; max-width: 760px; margin-left: auto; margin-right: auto;">
                        For media interviews, editorial features, book reviews, author conversations, podcast appearances, speaking engagements, and publishing collaborations, please reach out through our media inquiry form.
                    </p>

                    <div style="background: #FFFFFF; border: 1.5px solid rgba(197, 160, 89, 0.4); border-radius: 12px; padding: 1.8rem; margin-bottom: 2rem; display: inline-flex; flex-direction: column; gap: 0.8rem; text-align: center; max-width: 520px; width: 100%; box-shadow: 0 4px 18px rgba(44, 30, 20, 0.05);">
                        <div style="font-size: 1.05rem; color: #2C1E14;">
                            <strong style="color: var(--clr-gold-dark, #A07C32); text-transform: uppercase; letter-spacing: 1.2px; font-size: 0.82rem; display: block; margin-bottom: 0.2rem;">Media &amp; Press Contact:</strong>
                            <a href="mailto:sattvicbooks@gmail.com" style="color: #2C1E14; font-weight: 600; text-decoration: underline; display: inline-flex; align-items: center; justify-content: center; gap: 0.45rem;"><i class="fa-solid fa-envelope" style="color: var(--clr-gold-dark, #A07C32);"></i> sattvicbooks@gmail.com</a>
                        </div>
                        <div style="font-size: 1.05rem; color: #2C1E14;">
                            <strong style="color: var(--clr-gold-dark, #A07C32); text-transform: uppercase; letter-spacing: 1.2px; font-size: 0.82rem; display: block; margin-bottom: 0.2rem;">Website:</strong>
                            <a href="https://sattvicbooks.com" target="_blank" rel="noopener noreferrer" style="color: #A07C32; font-weight: 600; text-decoration: underline;">https://sattvicbooks.com</a>
                        </div>
                    </div>

                    <div style="margin-top: 1rem;">
                        <a href="contact.html#get-in-touch" class="btn btn-primary" style="background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%); color: #2C1E14; border: none; padding: 0.85rem 2.2rem; font-size: 1.02rem; font-weight: 700; border-radius: 8px; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.3);">
                            <i class="fa-solid fa-paper-plane" style="margin-right: 0.5rem;"></i> Send Media Inquiry
                        </a>
                    </div>

                    <div style="font-family: 'Playfair Display', Georgia, serif; font-size: 1.35rem; font-weight: 600; color: #A07C32; margin-top: 2.2rem; font-style: italic;">
                        Explore Sattvic Books. Discover the light of wisdom.
                    </div>
                </div>
            </div>'''
        media_html = media_html[:idx_start] + new_media_section + media_html[idx_end:]
        with open(r'd:\Sattvic Books\media-press.html', 'w', encoding='utf-8') as f:
            f.write(media_html)
        print("media-press.html updated successfully!")

# 2. Update reading-partners.html
with open(r'd:\Sattvic Books\reading-partners.html', 'r', encoding='utf-8') as f:
    reading_html = f.read()

idx_reading = reading_html.find('contact-partnerships')
if idx_reading != -1:
    idx_start = reading_html.rfind('<section', 0, idx_reading)
    idx_end = reading_html.find('</section>', idx_reading)
    if idx_start != -1 and idx_end != -1:
        new_reading_section = '''<section class="section-padding" id="contact-partnerships"
            style="background-color: #FAF7F2; border-top: 1px solid rgba(44, 30, 20, 0.06);">
            <div class="container" style="max-width: 860px;">
                <div class="conversation-closing-box fade-in-up text-center">
                    <span class="eyebrow" style="color: var(--clr-gold-dark, #A07C32); letter-spacing: 2px; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; display: block; margin-bottom: 0.6rem;">Join the Movement</span>
                    <h2
                        style="color: #2C1E14; font-size: 2.3rem; margin-bottom: 1.2rem; font-family: 'Playfair Display', Georgia, serif;">
                        Let&#39;s Make Reading a Shared Journey</h2>

                    <p
                        style="color: #5C4A3E; font-size: 1.12rem; line-height: 1.8; margin-bottom: 1.2rem; max-width: 760px; margin-left: auto; margin-right: auto;">
                        Do you lead a reading group, teach children, manage a library, or organize a Balavihar program?
                        We would love to hear about your work and explore opportunities to collaborate.
                    </p>
                    <p
                        style="color: #5C4A3E; font-size: 1.12rem; line-height: 1.8; margin-bottom: 1.4rem; max-width: 760px; margin-left: auto; margin-right: auto;">
                        Tell us about your group, the books you are interested in, and the kind of learning experience
                        you hope to create. Together, we can make books a starting point for discovery, connection, and
                        lifelong learning.
                    </p>
                    <p
                        style="color: #A07C32; font-size: 1.25rem; line-height: 1.8; margin-bottom: 2rem; max-width: 760px; margin-left: auto; margin-right: auto; font-family: 'Playfair Display', Georgia, serif; font-weight: 600;">
                        Partner with Sattvic Books. Bring meaningful reading into your community.
                    </p>

                    <!-- Exact Client CTA Button -->
                    <div style="margin-bottom: 2.5rem;">
                        <a href="contact.html#get-in-touch" class="btn btn-primary"
                            style="background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%); color: #2C1E14; border: none; padding: 1rem 2.5rem; font-size: 1.05rem; letter-spacing: 0.5px; text-transform: uppercase; font-weight: 700; border-radius: 8px; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.3);">
                            <i class="fa-solid fa-paper-plane" style="margin-right: 0.6rem;"></i> CONTACT US ABOUT
                            READING PARTNERSHIPS
                        </a>
                    </div>

                    <div style="border-top: 1px solid rgba(197, 160, 89, 0.3); padding-top: 1.8rem;">
                        <div
                            style="font-family: 'Playfair Display', Georgia, serif; font-size: 1.4rem; font-weight: 700; color: #2C1E14; letter-spacing: 1px; margin-bottom: 0.4rem;">
                            Read. Reflect. Grow.
                        </div>
                        <div style="font-size: 1.05rem; color: #6A5A4D;">
                            Inspiring minds, touching hearts, and nurturing lifelong values through books.
                        </div>
                    </div>
                </div>
            </div>'''
        reading_html = reading_html[:idx_start] + new_reading_section + reading_html[idx_end:]
        with open(r'd:\Sattvic Books\reading-partners.html', 'w', encoding='utf-8') as f:
            f.write(reading_html)
        print("reading-partners.html updated successfully!")

