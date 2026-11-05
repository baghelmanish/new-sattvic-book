with open("D:/Sattvic Books/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Remove .floating-vertical-btn from universal button selector list
css = css.replace(".footer-catalogue-btn,\n.floating-vertical-btn,\n.subscribe-form", ".footer-catalogue-btn,\n.subscribe-form")
css = css.replace(".footer-catalogue-btn,\r\n.floating-vertical-btn,\r\n.subscribe-form", ".footer-catalogue-btn,\r\n.subscribe-form")

# 2. Remove .floating-vertical-btn:visited
css = css.replace(".footer-catalog-btn:visited,\n.floating-vertical-btn:visited {", ".footer-catalog-btn:visited {")
css = css.replace(".footer-catalog-btn:visited,\r\n.floating-vertical-btn:visited {", ".footer-catalog-btn:visited {")

# 3. Remove .floating-vertical-btn:hover from universal hover selector list
css = css.replace(".footer-catalogue-btn:hover,\n.floating-vertical-btn:hover,\n.subscribe-form button:hover,", ".footer-catalogue-btn:hover,\n.subscribe-form button:hover,")
css = css.replace(".footer-catalogue-btn:hover,\r\n.floating-vertical-btn:hover,\r\n.subscribe-form button:hover,", ".footer-catalogue-btn:hover,\r\n.subscribe-form button:hover,")

# 4. Remove .floating-vertical-btn:active from universal active list
css = css.replace(".footer-catalog-btn:active,\n.floating-vertical-btn:active {", ".footer-catalog-btn:active {")
css = css.replace(".footer-catalog-btn:active,\r\n.floating-vertical-btn:active {", ".footer-catalog-btn:active {")

# 5. Remove .floating-vertical-btn i from icon lists
css = css.replace(".footer-catalogue-btn i,\n.floating-vertical-btn i {", ".footer-catalogue-btn i {")
css = css.replace(".footer-catalogue-btn i,\r\n.floating-vertical-btn i {", ".footer-catalogue-btn i {")

css = css.replace(".footer-catalogue-btn:hover i,\n.floating-vertical-btn:hover i {", ".footer-catalogue-btn:hover i {")
css = css.replace(".footer-catalogue-btn:hover i,\r\n.floating-vertical-btn:hover i {", ".footer-catalogue-btn:hover i {")

# 6. Replace the block at lines 10712-10730 with dedicated, bulletproof styling
old_block_1 = """/* Floating Vertical Side Button (Pill Shape with Signature Gold) */
.floating-vertical-btn {
    border-radius: 30px !important;
    padding: 0.75rem 1.6rem !important;
    border: none !important;
    box-shadow: 0 -4px 18px rgba(215, 179, 71, 0.35) !important;
}

.floating-vertical-btn:hover {
    transform: translate(calc(50% - 21px), -50%) rotate(-90deg) !important;
    box-shadow: 0 -8px 25px rgba(215, 179, 71, 0.5) !important;
}

@media (max-width: 992px) {
    .floating-vertical-btn {
        border-radius: 30px !important;
        padding: 0.65rem 1.2rem !important;
    }
}"""

new_block = """/* ==========================================================================
   FLOATING VERTICAL SIDE TAB (RIGHT-SIDE FIXED BUTTON - 100% VISIBLE & ROCK SOLID)
   ========================================================================== */
.floating-vertical-btn {
    position: fixed !important;
    right: 0 !important;
    top: 50% !important;
    transform-origin: center center !important;
    transform: translate(calc(50% - 22px), -50%) rotate(-90deg) !important;
    z-index: 999999 !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 0.65rem !important;
    padding: 0.75rem 1.6rem !important;
    background: #D7B347 !important;
    background-color: #D7B347 !important;
    color: #382618 !important;
    border: 2px solid #855E20 !important;
    border-bottom: none !important;
    border-radius: 12px 12px 0 0 !important;
    font-family: var(--font-body) !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    text-decoration: none !important;
    white-space: nowrap !important;
    box-shadow: 0 -6px 24px rgba(44, 30, 20, 0.35) !important;
    cursor: pointer !important;
    pointer-events: auto !important;
    visibility: visible !important;
    opacity: 1 !important;
    transition: background-color 0.25s ease, box-shadow 0.25s ease, color 0.25s ease !important;
}

.floating-vertical-btn i {
    font-size: 1.05rem !important;
    color: #382618 !important;
    fill: #382618 !important;
    transition: color 0.25s ease !important;
}

.floating-vertical-btn:hover {
    background: #C9A336 !important;
    background-color: #C9A336 !important;
    color: #20140B !important;
    border-color: #382618 !important;
    transform: translate(calc(50% - 22px), -50%) rotate(-90deg) !important;
    box-shadow: 0 -10px 28px rgba(215, 179, 71, 0.6) !important;
}

.floating-vertical-btn:hover i {
    color: #20140B !important;
    fill: #20140B !important;
}

.floating-vertical-btn:active {
    transform: translate(calc(50% - 22px), -50%) rotate(-90deg) scale(0.98) !important;
}

@media (max-width: 992px) {
    .floating-vertical-btn {
        top: auto !important;
        bottom: 20px !important;
        right: 15px !important;
        transform: none !important;
        writing-mode: horizontal-tb !important;
        border-radius: 50px !important;
        border: 2px solid #855E20 !important;
        padding: 0.7rem 1.4rem !important;
        font-size: 0.82rem !important;
        box-shadow: 0 6px 22px rgba(0, 0, 0, 0.35) !important;
    }

    .floating-vertical-btn:hover {
        transform: none !important;
    }

    .floating-vertical-btn:active {
        transform: scale(0.98) !important;
    }
}"""

if old_block_1 in css:
    css = css.replace(old_block_1, new_block)
    print("Replaced old_block_1 with LF")
elif old_block_1.replace("\n", "\r\n") in css:
    css = css.replace(old_block_1.replace("\n", "\r\n"), new_block.replace("\n", "\r\n"))
    print("Replaced old_block_1 with CRLF")
else:
    print("old_block_1 not found, checking match")

with open("D:/Sattvic Books/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Finished updating style.css")

