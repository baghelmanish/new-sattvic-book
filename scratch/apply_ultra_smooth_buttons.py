import re
import glob

with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove old footer button block (around line 1478)
old_footer_block_pattern = r'/\* Footer Download Free Catalog Button \*/.*?(?=\.social-links)'
match = re.search(old_footer_block_pattern, css, re.DOTALL)
if match:
    css = css[:match.start()] + css[match.end():]
    print("Removed obsolete footer button block from earlier CSS!")
else:
    print("Could not find footer button block to delete!")

# 2. Harmonize early .btn rule (around line 215)
old_early_btn = """.btn,
button.btn,
a.btn {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    vertical-align: middle !important;
    gap: 0.55rem !important;
    padding: 0.85rem 1.8rem !important;
    border-radius: 30px !important;
    font-family: var(--font-body) !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    line-height: 1.2 !important;
    letter-spacing: 0.3px !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    border: 2px solid transparent !important;
    text-decoration: none !important;
    outline: none !important;
    box-sizing: border-box !important;
    white-space: nowrap !important;
    user-select: none !important;
}"""

new_early_btn = """.btn,
button.btn,
a.btn {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    vertical-align: middle !important;
    gap: 0.5rem !important;
    padding: 0.85rem 2.2rem !important;
    border-radius: 50px !important;
    font-family: var(--font-body) !important;
    font-weight: 700 !important;
    font-size: 0.96rem !important;
    line-height: 1.2 !important;
    letter-spacing: 0.3px !important;
    cursor: pointer !important;
    border: none !important;
    text-decoration: none !important;
    outline: none !important;
    box-sizing: border-box !important;
    white-space: nowrap !important;
    user-select: none !important;
    position: relative !important;
    transform: translate3d(0, 0, 0) !important;
    backface-visibility: hidden !important;
    -webkit-backface-visibility: hidden !important;
    will-change: transform, box-shadow !important;
    transition: transform 0.25s cubic-bezier(0.25, 0.8, 0.25, 1),
                background-color 0.25s ease,
                box-shadow 0.25s ease,
                color 0.25s ease !important;
}"""

css_norm = css.replace('\r\n', '\n')
o_norm = old_early_btn.replace('\r\n', '\n')
n_norm = new_early_btn.replace('\r\n', '\n')

if o_norm in css_norm:
    css_norm = css_norm.replace(o_norm, n_norm)
    print("Harmonized early .btn definition!")
else:
    print("Early .btn block not found exactly for replacement")

# 3. Update UNIFIED LUXURY BUTTON SUITE at the end of style.css
suite_start = css_norm.find("/* ==========================================================================\n   UNIFIED LUXURY BUTTON SUITE")
if suite_start == -1:
    suite_start = css_norm.find("UNIFIED LUXURY BUTTON SUITE")
    suite_start = css_norm.rfind("/*", 0, suite_start)

new_ultra_smooth_suite = """/* ==========================================================================
   UNIFIED LUXURY BUTTON SUITE — BUTTER-SMOOTH & ZERO HOVER JITTER
   ========================================================================== */

/* Universal Button Base: Gold #D7B347 with Dark Brown #382618 Text */
.btn,
.btn-primary,
.btn-secondary,
.btn-gold,
.btn-primary-gold,
.btn-outline,
.btn-outline-dark,
.btn-outline-gold,
.s-btn-add,
.btn-add-cart,
.bd-add-btn,
.btn-listen,
.btn-subscribe,
.read-release-btn,
.browse-catalog-pill-btn,
.view-catalog-pill-btn,
.btn-gift-notify,
.trigger-freebie,
.asset-card-btn,
.copy-asset-btn,
.footer-catalog-btn,
.footer-catalogue-btn,
.floating-vertical-btn,
.subscribe-form button,
.notify-form button,
.modal-box .btn,
.modal-form-actions .btn,
button[type="submit"]:not(.modal-close) {
    background: #D7B347 !important;
    background-color: #D7B347 !important;
    color: #382618 !important;
    border: none !important;
    font-weight: 700 !important;
    font-family: var(--font-body) !important;
    letter-spacing: 0.3px !important;
    box-shadow: 0 4px 15px rgba(215, 179, 71, 0.3) !important;
    text-decoration: none !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    vertical-align: middle !important;
    gap: 0.45rem !important;
    cursor: pointer !important;
    outline: none !important;
    position: relative !important;
    box-sizing: border-box !important;
    backface-visibility: hidden !important;
    -webkit-backface-visibility: hidden !important;
    transform: translate3d(0, 0, 0) !important;
    will-change: transform, box-shadow !important;
    transition: transform 0.25s cubic-bezier(0.25, 0.8, 0.25, 1),
                background-color 0.25s ease,
                box-shadow 0.25s ease,
                color 0.25s ease !important;
}

/* Anti-Jitter Hit-Area Buffer: Prevents edge-hover rapid oscillation ("matakna") */
.btn::after,
.footer-catalog-btn::after,
.browse-catalog-pill-btn::after,
.view-catalog-pill-btn::after,
.btn-gift-notify::after {
    content: '';
    position: absolute;
    top: -6px;
    bottom: -6px;
    left: 0;
    right: 0;
    pointer-events: auto;
    border-radius: inherit;
}

/* Visited links retain dark brown text */
.btn:visited,
.btn-primary:visited,
.btn-secondary:visited,
.btn-gold:visited,
.btn-outline:visited,
.s-btn-add:visited,
.browse-catalog-pill-btn:visited,
.view-catalog-pill-btn:visited,
.footer-catalog-btn:visited,
.floating-vertical-btn:visited {
    color: #382618 !important;
}

/* Hover State: Butter-Smooth Lift & Radiant Warm Gold Glow */
.btn:hover,
.btn-primary:hover,
.btn-secondary:hover,
.btn-gold:hover,
.btn-primary-gold:hover,
.btn-outline:hover,
.btn-outline-dark:hover,
.btn-outline-gold:hover,
.s-btn-add:hover,
.btn-add-cart:hover,
.bd-add-btn:hover,
.btn-listen:hover,
.btn-subscribe:hover,
.read-release-btn:hover,
.browse-catalog-pill-btn:hover,
.view-catalog-pill-btn:hover,
.btn-gift-notify:hover,
.trigger-freebie:hover,
.asset-card-btn:hover,
.copy-asset-btn:hover,
.footer-catalog-btn:hover,
.footer-catalogue-btn:hover,
.floating-vertical-btn:hover,
.subscribe-form button:hover,
.notify-form button:hover,
.modal-box .btn:hover,
.modal-form-actions .btn:hover,
button[type="submit"]:not(.modal-close):hover {
    background: #C9A336 !important;
    background-color: #C9A336 !important;
    color: #20140B !important;
    border: none !important;
    transform: translate3d(0, -2px, 0) !important;
    box-shadow: 0 8px 22px rgba(215, 179, 71, 0.45) !important;
}

/* Active State */
.btn:active,
.btn-primary:active,
.btn-secondary:active,
.btn-gold:active,
.btn-outline:active,
.s-btn-add:active,
.btn-add-cart:active,
.bd-add-btn:active,
.browse-catalog-pill-btn:active,
.view-catalog-pill-btn:active,
.btn-gift-notify:active,
.trigger-freebie:active,
.asset-card-btn:active,
.footer-catalog-btn:active,
.floating-vertical-btn:active {
    transform: translate3d(0, 0, 0) !important;
    box-shadow: 0 2px 8px rgba(215, 179, 71, 0.25) !important;
}

/* Icons inside all buttons: Dark Brown #382618 Contrast */
.btn i,
.btn svg,
.s-btn-add i,
.btn-add-cart i,
.bd-add-btn i,
.btn-listen i,
.btn-subscribe i,
.browse-catalog-pill-btn i,
.view-catalog-pill-btn i,
.btn-gift-notify i,
.trigger-freebie i,
.asset-card-btn i,
.footer-catalog-btn i,
.footer-catalogue-btn i,
.floating-vertical-btn i {
    color: #382618 !important;
    fill: #382618 !important;
    transition: transform 0.25s ease !important;
}

.btn:hover i,
.btn:hover svg,
.s-btn-add:hover i,
.btn-add-cart:hover i,
.bd-add-btn:hover i,
.btn-listen:hover i,
.btn-subscribe:hover i,
.browse-catalog-pill-btn:hover i,
.view-catalog-pill-btn:hover i,
.btn-gift-notify:hover i,
.trigger-freebie:hover i,
.asset-card-btn:hover i,
.footer-catalog-btn:hover i,
.footer-catalogue-btn:hover i,
.floating-vertical-btn:hover i {
    color: #20140B !important;
    fill: #20140B !important;
}

/* Pill Shapes for Standalone & Major Action Buttons */
.browse-catalog-pill-btn,
.view-catalog-pill-btn,
.btn-gift-notify,
.footer-catalog-btn,
.footer-catalogue-btn,
.hero-buttons .btn,
.cta-box .btn,
.next-event-cta-box .btn,
.conversation-closing-box .btn,
.about-cta-actions .btn {
    border-radius: 50px !important;
    padding: 0.85rem 2.2rem !important;
    font-size: 0.96rem !important;
}

/* Card Action Buttons (Compact Rounded) */
.s-btn-add,
.btn-add-cart,
.bd-add-btn,
.freebie-card .btn,
.asset-card-btn,
.press-book-actions .btn,
.custom-resource-actions .btn,
.subscribe-form button {
    border-radius: 8px !important;
    padding: 0.72rem 1.2rem !important;
    font-size: 0.88rem !important;
}

/* Floating Vertical Side Button (Pill Shape with Signature Gold) */
.floating-vertical-btn {
    border-radius: 30px !important;
    padding: 0.75rem 1.6rem !important;
    border: none !important;
    box-shadow: 0 -4px 18px rgba(215, 179, 71, 0.35) !important;
}

.floating-vertical-btn:hover {
    transform: translate(calc(50% - 21px), -50%) rotate(-90deg) translateY(-4px) !important;
    box-shadow: 0 -8px 25px rgba(215, 179, 71, 0.5) !important;
}

@media (max-width: 992px) {
    .floating-vertical-btn {
        border-radius: 30px !important;
        padding: 0.65rem 1.2rem !important;
    }
}
"""

if suite_start != -1:
    css_norm = css_norm[:suite_start] + new_ultra_smooth_suite
    with open(r'd:\Sattvic Books\style.css', 'w', encoding='utf-8') as f:
        f.write(css_norm)
    print("Updated style.css with ultra-smooth button suite!")
else:
    print("Could not find suite start!")
