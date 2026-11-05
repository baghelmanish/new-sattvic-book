with open("D:/Sattvic Books/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Update lines 6250-6285
old_box = """/* Be Part of What's Next CTA Box */
.next-event-cta-box {
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
}"""

new_box = """/* Be Part of What's Next CTA Box (Signature Dark Mode Design) */
.next-event-cta-box {
    background: #322214 !important;
    background: linear-gradient(135deg, #322214 0%, #4A3319 50%, #20150D 100%) !important;
    border: 1.5px solid rgba(215, 179, 71, 0.45) !important;
    border-radius: 20px !important;
    padding: 4rem 2.5rem !important;
    position: relative !important;
    overflow: hidden !important;
    box-shadow: 0 16px 45px rgba(32, 21, 13, 0.28) !important;
    color: #FFFFFF !important;
}

.next-event-cta-box::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 85% 15%, rgba(215, 179, 71, 0.2) 0%, transparent 60%),
                radial-gradient(circle at 15% 85%, rgba(215, 179, 71, 0.15) 0%, transparent 50%);
    pointer-events: none;
}

.next-event-cta-box .eyebrow {
    color: #D7B347 !important;
}

.next-event-cta-box h2 {
    color: #FFFFFF !important;
}

.next-event-cta-box p {
    color: rgba(255, 255, 255, 0.92) !important;
}"""

if old_box in css:
    css = css.replace(old_box, new_box)
    print("Replaced old_box with LF")
elif old_box.replace("\n", "\r\n") in css:
    css = css.replace(old_box.replace("\n", "\r\n"), new_box.replace("\n", "\r\n"))
    print("Replaced old_box with CRLF")
else:
    print("Warning: old_box not matched exactly, checking lines")

# 2. Remove .next-event-cta-box h2 from line 10177
css = css.replace(".conversation-closing-box h2,\n.next-event-cta-box h2,\n", ".conversation-closing-box h2,\n")
css = css.replace(".conversation-closing-box h2,\r\n.next-event-cta-box h2,\r\n", ".conversation-closing-box h2,\r\n")

# 3. Remove .next-event-cta-box p from line 10219
css = css.replace(".conversation-closing-box p,\n.next-event-cta-box p,\n", ".conversation-closing-box p,\n")
css = css.replace(".conversation-closing-box p,\r\n.next-event-cta-box p,\r\n", ".conversation-closing-box p,\r\n")

# 4. Remove .next-event-cta-box from line 10289 (background: #FFFFFF)
css = css.replace(".conversation-closing-box,\n.next-event-cta-box,\n", ".conversation-closing-box,\n")
css = css.replace(".conversation-closing-box,\r\n.next-event-cta-box,\r\n", ".conversation-closing-box,\r\n")

with open("D:/Sattvic Books/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated style.css for dark mode next-event-cta-box!")

