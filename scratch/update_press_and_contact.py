# scratch/update_press_and_contact.py
import re

# 1. Update press-kit.html
with open(r'd:\Sattvic Books\press-kit.html', 'r', encoding='utf-8') as f:
    press_html = f.read()

# Locate section #media-channels
start_tag = '<section class="section-padding" id="media-channels"'
end_tag = '</section>'
idx_start = press_html.find(start_tag)
idx_end = press_html.find(end_tag, idx_start)

if idx_start != -1 and idx_end != -1:
    new_press_section = '''<section class="section-padding" id="media-channels" style="background-color: #FFFFFF;">
            <div class="container" style="max-width: 960px;">
                <div class="conversation-closing-box fade-in-up text-center">
                    <span class="eyebrow" style="color: var(--clr-gold-dark, #A07C32); letter-spacing: 2px; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; display: block; margin-bottom: 0.6rem;">Media Desk</span>
                    <h2
                        style="color: #2C1E14; font-size: 2.3rem; margin-bottom: 1.2rem; font-family: 'Playfair Display', Georgia, serif;">
                        Official Website &amp; Media Channels</h2>
                    <p
                        style="color: #5C4A3E; font-size: 1.12rem; line-height: 1.8; margin-bottom: 1.8rem; max-width: 760px; margin-left: auto; margin-right: auto;">
                        For interviews, book reviews, publication information, author features, speaking opportunities,
                        and media collaborations, connect with us through our verified official channels.
                    </p>

                    <div
                        style="background: #FFFFFF; border: 1.5px solid rgba(197, 160, 89, 0.4); border-radius: 12px; padding: 1.8rem; margin-bottom: 2rem; display: inline-flex; flex-direction: column; gap: 0.8rem; text-align: center; max-width: 540px; width: 100%; box-shadow: 0 4px 18px rgba(44, 30, 20, 0.05);">
                        <div
                            style="font-size: 1.15rem; color: #2C1E14; font-family: 'Playfair Display', Georgia, serif; font-weight: 700;">
                            Sattvic Books | The Sattvic Method Company
                        </div>
                        <div style="font-size: 1.05rem; color: #2C1E14;">
                            <strong
                                style="color: var(--clr-gold-dark, #A07C32); text-transform: uppercase; letter-spacing: 1.2px; font-size: 0.82rem; display: block; margin-bottom: 0.2rem;">Official
                                Website</strong>
                            <a href="https://sattvicbooks.com/" target="_blank" rel="noopener noreferrer"
                                style="color: #A07C32; font-weight: 700; text-decoration: underline;">https://sattvicbooks.com/</a>
                        </div>
                        <div style="font-size: 1.05rem; color: #2C1E14;">
                            <strong
                                style="color: var(--clr-gold-dark, #A07C32); text-transform: uppercase; letter-spacing: 1.2px; font-size: 0.82rem; display: block; margin-bottom: 0.2rem;">Media
                                &amp; Editorial Inquiries</strong>
                            <a href="mailto:info@thesattvicmethodcompany.com"
                                style="color: #2C1E14; font-weight: 600; text-decoration: none;">info@thesattvicmethodcompany.com</a>
                        </div>
                    </div>

                    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                        <a href="contact.html" class="btn btn-primary"
                            style="background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%); color: #2C1E14; border: none; padding: 0.95rem 2.2rem; font-size: 1.05rem; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; text-decoration: none; border-radius: 8px; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.3);">
                            <i class="fa-solid fa-paper-plane" style="margin-right: 0.5rem;"></i> Contact Media Team
                        </a>
                        <a href="assets/press-pack-sample.pdf" class="btn btn-outline" download
                            style="border: 1.5px solid var(--clr-gold); background: #FFFFFF; color: #2C1E14; padding: 0.95rem 2.2rem; font-size: 1.05rem; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; text-decoration: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(44, 30, 20, 0.05);">
                            <i class="fa-solid fa-download" style="margin-right: 0.5rem;"></i> Download Press Kit (PDF)
                        </a>
                    </div>
                </div>
            </div>'''
    press_html = press_html[:idx_start] + new_press_section + press_html[idx_end:]
    with open(r'd:\Sattvic Books\press-kit.html', 'w', encoding='utf-8') as f:
        f.write(press_html)
    print("press-kit.html updated successfully!")
else:
    print(f"Error finding press-kit section: idx_start={idx_start}, idx_end={idx_end}")

# 2. Update contact.html
with open(r'd:\Sattvic Books\contact.html', 'r', encoding='utf-8') as f:
    contact_html = f.read()

# Locate section containing Begin a Journey
idx_begin = contact_html.find('Begin a Journey')
if idx_begin != -1:
    idx_sec_start = contact_html.rfind('<section', 0, idx_begin)
    idx_sec_end = contact_html.find('</section>', idx_begin)
    if idx_sec_start != -1 and idx_sec_end != -1:
        new_contact_section = '''<section class="section-padding" style="background-color: #FAF7F2; border-top: 1px solid rgba(44, 30, 20, 0.06);">
            <div class="container" style="max-width: 860px;">
                <div class="conversation-closing-box fade-in-up text-center">
                    <span class="eyebrow" style="color: var(--clr-gold-dark, #A07C32); letter-spacing: 2px; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; display: block; margin-bottom: 0.6rem;">Begin a Journey</span>
                    <h2 style="color: #2C1E14; font-size: 2.4rem; margin-bottom: 1.2rem; font-family: 'Playfair Display', Georgia, serif;">Let's Begin a Conversation</h2>
                    <p style="color: #5C4A3E; font-size: 1.15rem; line-height: 1.8; margin-bottom: 1.2rem; max-width: 760px; margin-left: auto; margin-right: auto;">
                        Your curiosity, feedback, and ideas matter to us. Whether you're discovering our books for the first time or are already part of our growing community, we're grateful to connect with you.
                    </p>
                    <p style="color: #A07C32; font-size: 1.12rem; line-height: 1.8; margin-bottom: 1.8rem; max-width: 760px; margin-left: auto; margin-right: auto; font-style: italic; font-weight: 600;">
                        Thank you for being part of our journey toward knowledge, mindful living, and spiritual growth.
                    </p>
                    <div style="font-family: 'Playfair Display', Georgia, serif; font-size: 1.35rem; font-weight: 700; color: #2C1E14; letter-spacing: 1px;">
                        - The Sattvic Books Team
                    </div>
                </div>
            </div>'''
        contact_html = contact_html[:idx_sec_start] + new_contact_section + contact_html[idx_sec_end:]
        with open(r'd:\Sattvic Books\contact.html', 'w', encoding='utf-8') as f:
            f.write(contact_html)
        print("contact.html updated successfully!")
    else:
        print(f"Error finding contact section bounds: {idx_sec_start}, {idx_sec_end}")
else:
    print("Error: 'Begin a Journey' not found in contact.html")

