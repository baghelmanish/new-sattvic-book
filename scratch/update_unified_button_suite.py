with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('/* ==========================================================================\n   UNIFIED LUXURY BUTTON SUITE')
if idx == -1:
    idx = css.find('UNIFIED LUXURY BUTTON SUITE')
    # find comment start
    idx = css.rfind('/*', 0, idx)

new_suite = """/* ==========================================================================
   UNIFIED LUXURY BUTTON SUITE — 100% IDENTICAL SIGNATURE STYLE ACROSS ALL BUTTONS
   ========================================================================== */

/* Universal Button Base: Warm Camel/Wheat Gold with Deep Espresso Text */
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
    background: #DFBF77 !important;
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    color: #2C1E14 !important;
    border: none !important;
    font-weight: 700 !important;
    font-family: var(--font-body) !important;
    letter-spacing: 0.3px !important;
    box-shadow: 0 4px 15px rgba(197, 160, 89, 0.3) !important;
    transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    text-decoration: none !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 0.45rem !important;
    cursor: pointer !important;
    outline: none !important;
}

/* Visited links keep espresso text */
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
    color: #2C1E14 !important;
}

/* Hover State: Richer Radiant Warm Gold with Lift & Glow */
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
    background: linear-gradient(135deg, #D4AF37 0%, #C5A059 100%) !important;
    color: #1A0F07 !important;
    border: none !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 22px rgba(197, 160, 89, 0.45) !important;
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
    transform: translateY(0) !important;
    box-shadow: 0 2px 8px rgba(197, 160, 89, 0.25) !important;
}

/* Icons inside all buttons: Deep Espresso Contrast */
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
    color: #2C1E14 !important;
    fill: #2C1E14 !important;
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
    color: #1A0F07 !important;
    fill: #1A0F07 !important;
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
    box-shadow: 0 -4px 18px rgba(197, 160, 89, 0.35) !important;
}

.floating-vertical-btn:hover {
    transform: translate(calc(50% - 21px), -50%) rotate(-90deg) translateY(-4px) !important;
    box-shadow: 0 -8px 25px rgba(197, 160, 89, 0.5) !important;
}

@media (max-width: 992px) {
    .floating-vertical-btn {
        border-radius: 30px !important;
        padding: 0.65rem 1.2rem !important;
    }
}
"""

css_new = css[:idx] + new_suite
with open(r'd:\Sattvic Books\style.css', 'w', encoding='utf-8') as f:
    f.write(css_new)
print("Updated UNIFIED LUXURY BUTTON SUITE successfully!")

