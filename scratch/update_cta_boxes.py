# scratch/update_cta_boxes.py

# 1. Update style.css
with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .next-event-cta-box
old_next_box = '''.next-event-cta-box {
    background: linear-gradient(135deg, var(--clr-primary) 0%, #4A3319 50%, #20150D 100%);
    border: 1px solid rgba(197, 160, 89, 0.4);
    border-radius: 20px;
    padding: 4rem 2rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 16px 45px rgba(44, 30, 20, 0.16);
}

.next-event-cta-box::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 80% 20%, rgba(197, 160, 89, 0.18) 0%, transparent 60%),
                radial-gradient(circle at 20% 80%, rgba(197, 160, 89, 0.12) 0%, transparent 50%);
    pointer-events: none;
}'''

new_next_box = '''.next-event-cta-box {
    background: #FAF7EE;
    background: linear-gradient(135deg, #FFFFFF 0%, #FAF5EB 50%, #F5ECDB 100%) !important;
    border: 1.5px solid rgba(197, 160, 89, 0.45) !important;
    border-radius: 20px;
    padding: 4rem 2.5rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 14px 40px rgba(44, 30, 20, 0.08) !important;
}

.next-event-cta-box::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 85% 15%, rgba(197, 160, 89, 0.18) 0%, transparent 60%),
                radial-gradient(circle at 15% 85%, rgba(197, 160, 89, 0.14) 0%, transparent 50%);
    pointer-events: none;
}

.next-event-cta-box h2 {
    color: #2C1E14 !important;
}

.next-event-cta-box p {
    color: #5C4A3E !important;
}'''

# Update .conversation-closing-box
old_conv_box = '''.conversation-closing-box {
    background: linear-gradient(135deg, var(--clr-primary) 0%, #4A3319 50%, #20150D 100%);
    border: 1px solid rgba(197, 160, 89, 0.4);
    border-radius: 20px;
    padding: 3.5rem 2rem;
    color: #FFFFFF;
    box-shadow: 0 16px 45px rgba(44, 30, 20, 0.14);
    position: relative;
    overflow: hidden;
}

.conversation-closing-box::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 80% 20%, rgba(197, 160, 89, 0.16) 0%, transparent 60%),
                radial-gradient(circle at 20% 80%, rgba(197, 160, 89, 0.1) 0%, transparent 50%);
    pointer-events: none;
}'''

new_conv_box = '''.conversation-closing-box {
    background: #FAF7EE;
    background: linear-gradient(135deg, #FFFFFF 0%, #FAF5EB 50%, #F5ECDB 100%) !important;
    border: 1.5px solid rgba(197, 160, 89, 0.45) !important;
    border-radius: 20px;
    padding: 3.5rem 2.5rem;
    color: #2C1E14 !important;
    box-shadow: 0 14px 40px rgba(44, 30, 20, 0.08) !important;
    position: relative;
    overflow: hidden;
}

.conversation-closing-box::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 85% 15%, rgba(197, 160, 89, 0.18) 0%, transparent 60%),
                radial-gradient(circle at 15% 85%, rgba(197, 160, 89, 0.14) 0%, transparent 50%);
    pointer-events: none;
}

.conversation-closing-box h2 {
    color: #2C1E14 !important;
}

.conversation-closing-box p {
    color: #5C4A3E !important;
}'''

def normalize_and_replace(source, old_s, new_s):
    old_crlf = old_s.replace('\r\n', '\n').replace('\n', '\r\n')
    old_lf = old_s.replace('\r\n', '\n')
    if old_crlf in source:
        return source.replace(old_crlf, new_s.replace('\n', '\r\n')), True
    elif old_lf in source:
        return source.replace(old_lf, new_s), True
    return source, False

css, ok1 = normalize_and_replace(css, old_next_box, new_next_box)
css, ok2 = normalize_and_replace(css, old_conv_box, new_conv_box)

print(f"style.css: next_box replaced: {ok1}, conv_box replaced: {ok2}")
with open(r'd:\Sattvic Books\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update events.html
with open(r'd:\Sattvic Books\events.html', 'r', encoding='utf-8') as f:
    events_html = f.read()

old_events_cta = '''        <!-- Section 5: Be Part of What's Next! -->
        <section class="section-padding" style="background-color: #FFFFFF;">
            <div class="container" style="max-width: 860px;">
                <div class="next-event-cta-box fade-in-up text-center">
                    <div class="next-event-cta-inner">
                        <h2 style="color: #FFFFFF; font-size: 2.6rem; margin-bottom: 1.2rem; font-family: 'Playfair Display', Georgia, serif;">Be Part of What's Next!</h2>
                        <p style="color: rgba(255, 255, 255, 0.95); font-size: 1.15rem; line-height: 1.8; margin-bottom: 1rem;">
                            A meaningful experience can begin with a single conversation, a new story, or an idea that inspires you.
                        </p>
                        <p style="color: rgba(255, 255, 255, 0.88); font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.5rem;">
                            Stay connected with Sattvic Books to discover upcoming workshops, special gatherings, book launches, and learning opportunities.
                        </p>
                        <p style="color: var(--clr-gold-light); font-size: 1.35rem; font-family: 'Playfair Display', Georgia, serif; font-style: italic; font-weight: 600; margin-bottom: 2rem;">
                            Don't just read about inspiration. Experience it!
                        </p>
                        <div>
                            <a href="contact.html" class="btn btn-primary" style="background-color: var(--clr-gold); color: var(--clr-primary); border-color: var(--clr-gold); padding: 0.95rem 2.4rem; font-size: 1.05rem; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; text-decoration: none;">
                                <i class="fa-solid fa-calendar-check" style="margin-right: 0.5rem;"></i> Explore Events &amp; Register Today
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

new_events_cta = '''        <!-- Section 5: Be Part of What's Next! -->
        <section class="section-padding" style="background-color: #FFFFFF;">
            <div class="container" style="max-width: 860px;">
                <div class="next-event-cta-box fade-in-up text-center">
                    <div class="next-event-cta-inner">
                        <span class="eyebrow" style="color: var(--clr-gold-dark, #A07C32); letter-spacing: 2px; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; display: block; margin-bottom: 0.8rem;">Upcoming Community</span>
                        <h2 style="color: #2C1E14; font-size: 2.6rem; margin-bottom: 1.2rem; font-family: 'Playfair Display', Georgia, serif;">Be Part of What's Next!</h2>
                        <p style="color: #5C4A3E; font-size: 1.15rem; line-height: 1.8; margin-bottom: 1rem;">
                            A meaningful experience can begin with a single conversation, a new story, or an idea that inspires you.
                        </p>
                        <p style="color: #6A5A4D; font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.5rem;">
                            Stay connected with Sattvic Books to discover upcoming workshops, special gatherings, book launches, and learning opportunities.
                        </p>
                        <p style="color: #A07C32; font-size: 1.35rem; font-family: 'Playfair Display', Georgia, serif; font-style: italic; font-weight: 600; margin-bottom: 2rem;">
                            Don't just read about inspiration. Experience it!
                        </p>
                        <div>
                            <a href="contact.html" class="btn btn-primary" style="background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%); color: #2C1E14; border: none; padding: 0.95rem 2.4rem; font-size: 1.05rem; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; text-decoration: none; border-radius: 8px; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.3);">
                                <i class="fa-solid fa-calendar-check" style="margin-right: 0.5rem;"></i> Explore Events &amp; Register Today
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

events_html, ok_ev = normalize_and_replace(events_html, old_events_cta, new_events_cta)
print(f"events.html: cta replaced: {ok_ev}")
with open(r'd:\Sattvic Books\events.html', 'w', encoding='utf-8') as f:
    f.write(events_html)

# 3. Update press-kit.html
with open(r'd:\Sattvic Books\press-kit.html', 'r', encoding='utf-8') as f:
    press_html = f.read()

old_press_cta = '''        <!-- Section 10: Official Website & Media Channels -->
        <section class="section-padding" id="media-channels" style="background-color: #FFFFFF;">
            <div class="container" style="max-width: 960px;">
                <div class="conversation-closing-box fade-in-up text-center">
                    <span class="eyebrow text-gold" style="letter-spacing: 2px;">Media Desk</span>
                    <h2
                        style="color: #FFFFFF; font-size: 2.3rem; margin-bottom: 1.2rem; font-family: 'Playfair Display', Georgia, serif;">
                        Official Website &amp; Media Channels</h2>
                    <p
                        style="color: rgba(255, 255, 255, 0.95); font-size: 1.12rem; line-height: 1.8; margin-bottom: 1.8rem; max-width: 760px; margin-left: auto; margin-right: auto;">
                        For interviews, book reviews, publication information, author features, speaking opportunities,
                        and media collaborations, connect with us through our verified official channels.
                    </p>

                    <div
                        style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(197, 160, 89, 0.35); border-radius: 12px; padding: 1.8rem; margin-bottom: 2rem; display: inline-flex; flex-direction: column; gap: 0.8rem; text-align: center; max-width: 540px; width: 100%;">
                        <div
                            style="font-size: 1.15rem; color: #FFFFFF; font-family: 'Playfair Display', Georgia, serif; font-weight: 700;">
                            Sattvic Books | The Sattvic Method Company
                        </div>
                        <div style="font-size: 1.05rem; color: #FFFFFF;">
                            <strong
                                style="color: var(--clr-gold-light); text-transform: uppercase; letter-spacing: 1.2px; font-size: 0.82rem; display: block; margin-bottom: 0.2rem;">Official
                                Website</strong>
                            <a href="https://sattvicbooks.com/" target="_blank" rel="noopener noreferrer"
                                style="color: var(--clr-gold-light); font-weight: 700; text-decoration: underline;">https://sattvicbooks.com/</a>
                        </div>
                        <div style="font-size: 1.05rem; color: #FFFFFF;">
                            <strong
                                style="color: var(--clr-gold-light); text-transform: uppercase; letter-spacing: 1.2px; font-size: 0.82rem; display: block; margin-bottom: 0.2rem;">Media
                                &amp; Editorial Inquiries</strong>
                            <a href="mailto:info@thesattvicmethodcompany.com"
                                style="color: #FFFFFF; font-weight: 600; text-decoration: none;">info@thesattvicmethodcompany.com</a>
                        </div>
                    </div>

                    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                        <a href="contact.html" class="btn btn-primary"
                            style="background-color: var(--clr-gold); color: var(--clr-primary); border-color: var(--clr-gold); padding: 0.95rem 2.2rem; font-size: 1.05rem; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; text-decoration: none;">
                            <i class="fa-solid fa-paper-plane" style="margin-right: 0.5rem;"></i> Contact Media Team
                        </a>
                        <a href="assets/press-pack-sample.pdf" class="btn btn-outline" download
                            style="border-color: rgba(255, 255, 255, 0.6); color: #FFFFFF; padding: 0.95rem 2.2rem; font-size: 1.05rem; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; text-decoration: none;">
                            <i class="fa-solid fa-download" style="margin-right: 0.5rem;"></i> Download Press Kit (PDF)
                        </a>
                    </div>
                </div>
            </div>
        </section>'''

new_press_cta = '''        <!-- Section 10: Official Website & Media Channels -->
        <section class="section-padding" id="media-channels" style="background-color: #FFFFFF;">
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
            </div>
        </section>'''

press_html, ok_pr = normalize_and_replace(press_html, old_press_cta, new_press_cta)
print(f"press-kit.html: cta replaced: {ok_pr}")
with open(r'd:\Sattvic Books\press-kit.html', 'w', encoding='utf-8') as f:
    f.write(press_html)

# 4. Update contact.html
with open(r'd:\Sattvic Books\contact.html', 'r', encoding='utf-8') as f:
    contact_html = f.read()

old_contact_cta = '''        <section class="section-padding" style="background-color: #FAF7F2; border-top: 1px solid rgba(44, 30, 20, 0.06);">
            <div class="container" style="max-width: 860px;">
                <div class="conversation-closing-box fade-in-up text-center">
                    <span class="eyebrow text-gold" style="letter-spacing: 2px;">Begin a Journey</span>
                    <h2 style="color: #FFFFFF; font-size: 2.4rem; margin-bottom: 1.2rem; font-family: 'Playfair Display', Georgia, serif;">Let's Begin a Conversation</h2>
                    <p style="color: rgba(255, 255, 255, 0.95); font-size: 1.15rem; line-height: 1.8; margin-bottom: 1.2rem; max-width: 760px; margin-left: auto; margin-right: auto;">
                        Your curiosity, feedback, and ideas matter to us. Whether you're discovering our books for the first time or are already part of our growing community, we're grateful to connect with you.
                    </p>
                    <p style="color: var(--clr-gold-light); font-size: 1.12rem; line-height: 1.8; margin-bottom: 1.8rem; max-width: 760px; margin-left: auto; margin-right: auto; font-style: italic;">
                        Thank you for being part of our journey toward knowledge, mindful living, and spiritual growth.
                    </p>
                    <div style="font-family: 'Playfair Display', Georgia, serif; font-size: 1.35rem; font-weight: 700; color: #FFFFFF; letter-spacing: 1px;">
                        - The Sattvic Books Team
                    </div>
                </div>
            </div>
        </section>'''

new_contact_cta = '''        <section class="section-padding" style="background-color: #FAF7F2; border-top: 1px solid rgba(44, 30, 20, 0.06);">
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
            </div>
        </section>'''

contact_html, ok_ct = normalize_and_replace(contact_html, old_contact_cta, new_contact_cta)
print(f"contact.html: cta replaced: {ok_ct}")
with open(r'd:\Sattvic Books\contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

print("All files updated successfully!")

