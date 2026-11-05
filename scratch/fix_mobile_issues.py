# 1. Update events.html
with open("D:/Sattvic Books/events.html", "r", encoding="utf-8") as f:
    ev = f.read()

old_ev_btn = """                    <div>
                        <a href="contact.html" class="btn btn-primary" style="padding: 0.9rem 2.2rem; font-size: 1.05rem; display: inline-flex; align-items: center; justify-content: center; text-decoration: none;">
                            <i class="fa-solid fa-calendar-days" style="margin-right: 0.5rem;"></i> Explore Upcoming Events / Register Now
                        </a>
                    </div>"""

new_ev_btn = """                    <div style="max-width: 580px; margin: 0 auto; width: 100%;">
                        <a href="contact.html" class="btn btn-primary events-main-cta-btn" style="text-decoration: none;">
                            <i class="fa-solid fa-calendar-days" style="margin-right: 0.5rem;"></i> Explore Upcoming Events / Register Now
                        </a>
                    </div>"""

if old_ev_btn in ev:
    ev = ev.replace(old_ev_btn, new_ev_btn)
    print("Updated events.html button (LF)")
elif old_ev_btn.replace("\n", "\r\n") in ev:
    ev = ev.replace(old_ev_btn.replace("\n", "\r\n"), new_ev_btn.replace("\n", "\r\n"))
    print("Updated events.html button (CRLF)")
else:
    print("Warning: old_ev_btn not matched in events.html")

with open("D:/Sattvic Books/events.html", "w", encoding="utf-8") as f:
    f.write(ev)


# 2. Update press-release-diwali-launch.html
with open("D:/Sattvic Books/press-release-diwali-launch.html", "r", encoding="utf-8") as f:
    pr = f.read()

old_pr_box = """                        <!-- Media Contact Box -->
                        <div style="background: #FAF6EE; border: 1px solid rgba(44, 30, 20, 0.12); border-radius: 10px; padding: 1.8rem 2rem; margin: 2.2rem 0;">
                            <h3 style="margin-top: 0; margin-bottom: 0.8rem; color: var(--clr-primary); font-size: 1.3rem;">Media Contact</h3>
                            <p style="margin-bottom: 0.4rem; font-weight: 600; color: var(--clr-primary);">The Sattvic Method Company</p>
                            <p style="margin-bottom: 0.4rem;">
                                <strong>Email:</strong> <a href="mailto:sattvicbooks@gmail.com" style="color: var(--clr-primary); text-decoration: underline;">sattvicbooks@gmail.com</a>
                            </p>
                            <p style="margin-bottom: 0.4rem;">
                                <strong>Website:</strong> <a href="https://thesattvicmethodcompany.com/" target="_blank" rel="noopener noreferrer" style="color: var(--clr-primary);">https://thesattvicmethodcompany.com/</a>
                            </p>
                            <p style="margin-bottom: 0;">
                                <strong>Sattvic Books:</strong> <a href="https://sattvicbooks.com" target="_blank" rel="noopener noreferrer" style="color: var(--clr-primary);">https://sattvicbooks.com</a>
                            </p>
                        </div>"""

new_pr_box = """                        <!-- Media Contact Box -->
                        <div class="media-contact-box" style="background: #FAF6EE; border: 1px solid rgba(44, 30, 20, 0.12); border-radius: 10px; padding: 1.8rem 2rem; margin: 2.2rem 0; overflow-wrap: break-word; word-break: break-word;">
                            <h3 style="margin-top: 0; margin-bottom: 0.8rem; color: var(--clr-primary); font-size: 1.3rem;">Media Contact</h3>
                            <p style="margin-bottom: 0.4rem; font-weight: 600; color: var(--clr-primary);">The Sattvic Method Company</p>
                            <p style="margin-bottom: 0.4rem; overflow-wrap: break-word; word-break: break-word;">
                                <strong>Email:</strong> <a href="mailto:sattvicbooks@gmail.com" style="color: var(--clr-primary); text-decoration: underline; word-break: break-all;">sattvicbooks@gmail.com</a>
                            </p>
                            <p style="margin-bottom: 0.4rem; overflow-wrap: break-word; word-break: break-word;">
                                <strong>Website:</strong> <a href="https://thesattvicmethodcompany.com/" target="_blank" rel="noopener noreferrer" style="color: var(--clr-primary); word-break: break-all; display: inline-block;">https://thesattvicmethodcompany.com/</a>
                            </p>
                            <p style="margin-bottom: 0; overflow-wrap: break-word; word-break: break-word;">
                                <strong>Sattvic Books:</strong> <a href="https://sattvicbooks.com" target="_blank" rel="noopener noreferrer" style="color: var(--clr-primary); word-break: break-all; display: inline-block;">https://sattvicbooks.com</a>
                            </p>
                        </div>"""

if old_pr_box in pr:
    pr = pr.replace(old_pr_box, new_pr_box)
    print("Updated press-release-diwali-launch.html media contact box (LF)")
elif old_pr_box.replace("\n", "\r\n") in pr:
    pr = pr.replace(old_pr_box.replace("\n", "\r\n"), new_pr_box.replace("\n", "\r\n"))
    print("Updated press-release-diwali-launch.html media contact box (CRLF)")
else:
    print("Warning: old_pr_box not matched in press-release-diwali-launch.html")

with open("D:/Sattvic Books/press-release-diwali-launch.html", "w", encoding="utf-8") as f:
    f.write(pr)


# 3. Update style.css
with open("D:/Sattvic Books/style.css", "r", encoding="utf-8") as f:
    css = f.read()

mobile_css_additions = """
/* ==========================================================================
   MOBILE SCREEN FIXES: EVENT BUTTON FULL WIDTH & MEDIA CONTACT URL BREAK
   ========================================================================== */
.media-contact-box {
    overflow-wrap: break-word !important;
    word-break: break-word !important;
}

.media-contact-box a {
    word-break: break-all !important;
    overflow-wrap: anywhere !important;
}

@media (max-width: 768px) {
    /* Event Page Button: Full width on mobile screens so it never clips or cuts off */
    .events-main-cta-btn,
    .next-event-cta-box .btn,
    .next-event-cta-inner .btn {
        width: 100% !important;
        max-width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: normal !important;
        text-align: center !important;
        padding: 0.9rem 1.2rem !important;
        font-size: 0.95rem !important;
        line-height: 1.4 !important;
        box-sizing: border-box !important;
    }

    /* Press Release Media Contact Box: Responsive padding & safe word wrapping */
    .media-contact-box {
        padding: 1.4rem 1.1rem !important;
    }
}
"""

if "MOBILE SCREEN FIXES: EVENT BUTTON FULL WIDTH" not in css:
    css += mobile_css_additions
    with open("D:/Sattvic Books/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Added mobile CSS rules to style.css!")
else:
    print("mobile CSS rules already in style.css")

