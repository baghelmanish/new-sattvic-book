# scratch/enhance_home_palette.py

with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Append a dedicated, high-priority section at the end of style.css:
# "LUXURY CREAM & GOLD MASTER PALETTE ENHANCEMENTS (MATCHES ATTACHMENT FLAWLESSLY)"

enhancements_css = '''

/* ==========================================================================
   LUXURY CREAM & GOLD MASTER PALETTE ENHANCEMENTS (MATCHES REFERENCE IMAGE)
   ========================================================================== */

/* 1. Global Gold Button Styling: Warm Wheat/Camel Gold with Deep Espresso Text */
.btn-primary,
.btn-gold,
.btn-primary-gold {
    background: #DFBF77 !important;
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    color: #2C1E14 !important;
    border: none !important;
    font-weight: 700 !important;
    letter-spacing: 0.3px !important;
    box-shadow: 0 4px 15px rgba(197, 160, 89, 0.28) !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}

.btn-primary:hover,
.btn-gold:hover,
.btn-primary-gold:hover {
    background: linear-gradient(135deg, #D4AF37 0%, #C5A059 100%) !important;
    color: #1A0F07 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(197, 160, 89, 0.42) !important;
}

.btn-outline {
    background-color: #FFFFFF !important;
    color: #2C1E14 !important;
    border: 1.5px solid rgba(197, 160, 89, 0.5) !important;
    font-weight: 600 !important;
    box-shadow: 0 3px 12px rgba(44, 30, 20, 0.04) !important;
    transition: all 0.3s ease !important;
}

.btn-outline:hover {
    background-color: #FAF4E8 !important;
    border-color: var(--clr-gold) !important;
    color: #2C1E14 !important;
    transform: translateY(-2px) !important;
}

/* 2. Navbar Refinement */
.navbar {
    background-color: rgba(255, 255, 255, 0.98) !important;
    border-bottom: 1px solid rgba(197, 160, 89, 0.25) !important;
    box-shadow: 0 2px 14px rgba(44, 30, 20, 0.04) !important;
}

.nav-links a {
    color: #2C1E14 !important;
    font-weight: 600 !important;
}

.nav-links a:hover,
.nav-links a.active {
    color: #A07C32 !important;
}

/* 3. Hero Section */
.hero {
    border-bottom: none !important;
}

.hero h1 {
    color: #2C1E14 !important;
}

.hero-subtext {
    color: #5C4A3E !important;
}

/* 4. Promo Ticker Strip */
.promo-ticker-strip {
    background: linear-gradient(90deg, #DFBF77 0%, #D4AF37 50%, #DFBF77 100%) !important;
    border-top: 1px solid rgba(197, 160, 89, 0.4) !important;
    border-bottom: 1px solid rgba(197, 160, 89, 0.4) !important;
}

.promo-ticker-item {
    color: #2C1E14 !important;
}

.promo-ticker-badge {
    background: #2C1E14 !important;
    color: #DFC080 !important;
}

.promo-ticker-code-btn {
    background: rgba(44, 30, 20, 0.1) !important;
    border: 1px dashed #2C1E14 !important;
    color: #2C1E14 !important;
}

.promo-ticker-code-btn:hover {
    background: #2C1E14 !important;
    color: #DFC080 !important;
}

.promo-ticker-shop-btn {
    color: #2C1E14 !important;
    font-weight: 700 !important;
}

/* 5. Featured Catalog (Explore Our Catalog): Warm Ivory Cream Background with Pop-out White Cards */
.collections {
    background-color: #FAF6EE !important;
    background: linear-gradient(180deg, #FAF6EE 0%, #FAF4EA 100%) !important;
    border-bottom: 1px solid rgba(197, 160, 89, 0.2) !important;
}

.collections .collection-card {
    background-color: #FFFFFF !important;
    border: 1px solid rgba(197, 160, 89, 0.25) !important;
    border-radius: 14px !important;
    box-shadow: 0 6px 22px rgba(44, 30, 20, 0.05) !important;
    transition: all 0.35s ease !important;
}

.collections .collection-card:hover {
    background-color: #FFFFFF !important;
    border-color: rgba(197, 160, 89, 0.5) !important;
    transform: translateY(-5px) !important;
    box-shadow: 0 16px 38px rgba(44, 30, 20, 0.1) !important;
}

.collections .icon-wrapper {
    width: 64px !important;
    height: 64px !important;
    border-radius: 50% !important;
    background: rgba(223, 191, 119, 0.18) !important;
    border: 1.5px solid rgba(197, 160, 89, 0.35) !important;
    color: #A07C32 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 1.6rem !important;
    margin: 0 auto 1.2rem !important;
    transition: all 0.35s ease !important;
}

.collections .collection-card:hover .icon-wrapper {
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    color: #2C1E14 !important;
    transform: scale(1.08) !important;
    box-shadow: 0 6px 18px rgba(197, 160, 89, 0.35) !important;
}

.collections .collection-card h3 {
    color: #2C1E14 !important;
    font-size: 1.2rem !important;
    font-weight: 700 !important;
    margin-bottom: 0.5rem !important;
}

.collections .collection-card p {
    color: #6A5A4D !important;
    font-size: 0.92rem !important;
    line-height: 1.6 !important;
}

/* 6. Why Buy from Sattvic Books? (Clean Warm Linen White with Elegant Rounded Cards) */
.why-buy-section {
    background-color: #FFFFFF !important;
    background: linear-gradient(180deg, #FFFFFF 0%, #FEFBF7 100%) !important;
    border-top: 1px solid rgba(197, 160, 89, 0.18) !important;
    border-bottom: 1px solid rgba(197, 160, 89, 0.18) !important;
}

.why-buy-card {
    background: #FFFFFF !important;
    border-radius: 14px !important;
    padding: 2.2rem 1.6rem 2rem !important;
    border: 1px solid rgba(197, 160, 89, 0.22) !important;
    box-shadow: 0 6px 20px rgba(44, 30, 20, 0.05) !important;
    transition: all 0.35s ease !important;
    border-bottom: 3px solid transparent !important;
}

.why-buy-card:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 16px 38px rgba(44, 30, 20, 0.1) !important;
    border-color: rgba(197, 160, 89, 0.5) !important;
    border-bottom: 3px solid #D4AF37 !important;
}

.why-buy-icon-wrapper,
.why-buy-icon-pill {
    width: 60px !important;
    height: 60px !important;
    border-radius: 50% !important;
    background: rgba(223, 191, 119, 0.16) !important;
    border: 1.5px solid rgba(197, 160, 89, 0.35) !important;
    color: #A07C32 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 1.5rem !important;
    margin: 0 auto 1.2rem auto !important;
    box-shadow: none !important;
    transition: all 0.35s ease !important;
}

.why-buy-card:hover .why-buy-icon-wrapper,
.why-buy-card:hover .why-buy-icon-pill {
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    color: #2C1E14 !important;
    transform: scale(1.08) !important;
    box-shadow: 0 6px 18px rgba(197, 160, 89, 0.35) !important;
}

.why-buy-num {
    display: none !important; /* Hide numbers to match clean reference screenshot */
}

.why-buy-card h3 {
    font-family: var(--font-heading) !important;
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    color: #2C1E14 !important;
    margin-bottom: 0.6rem !important;
}

.why-buy-card p {
    font-size: 0.92rem !important;
    color: #6A5A4D !important;
    line-height: 1.6 !important;
    margin: 0 !important;
}

/* 7. Gift Store Section (Warm Cream Palette with Gentle Shadows) */
.gift-store-section {
    background: #FAF5EB !important;
    background: linear-gradient(180deg, #FBF6EC 0%, #FAF5EB 50%, #F5ECDB 100%) !important;
    border-top: 1px solid rgba(197, 160, 89, 0.22) !important;
    border-bottom: 1px solid rgba(197, 160, 89, 0.22) !important;
}

.gift-store-card {
    background: #FFFFFF !important;
    border-radius: 14px !important;
    padding: 2.2rem 1.6rem 2rem !important;
    border: 1px solid rgba(197, 160, 89, 0.22) !important;
    border-top: none !important;
    box-shadow: 0 6px 20px rgba(44, 30, 20, 0.05) !important;
    transition: all 0.35s ease !important;
}

.gift-store-card:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 16px 38px rgba(44, 30, 20, 0.1) !important;
    border-color: rgba(197, 160, 89, 0.45) !important;
}

.gift-card-icon-wrap {
    width: 60px !important;
    height: 60px !important;
    border-radius: 50% !important;
    background: rgba(223, 191, 119, 0.16) !important;
    border: 1.5px solid rgba(197, 160, 89, 0.35) !important;
    color: #A07C32 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 1.5rem !important;
    margin: 0 auto 1.2rem auto !important;
    box-shadow: none !important;
    transition: all 0.35s ease !important;
}

.gift-store-card:hover .gift-card-icon-wrap {
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    color: #2C1E14 !important;
    transform: scale(1.08) !important;
    box-shadow: 0 6px 18px rgba(197, 160, 89, 0.35) !important;
}

.gift-badge-coming-soon {
    font-family: var(--font-body) !important;
    font-size: 0.74rem !important;
    font-weight: 700 !important;
    letter-spacing: 1.1px !important;
    color: #A07C32 !important;
    background: rgba(223, 191, 119, 0.16) !important;
    border: 1px solid rgba(197, 160, 89, 0.35) !important;
    padding: 0.35rem 0.95rem !important;
    border-radius: 30px !important;
    text-transform: uppercase !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.4rem !important;
    margin-top: auto !important;
    width: fit-content !important;
}

.gift-store-banner {
    background: #FFFFFF !important;
    background: linear-gradient(135deg, #FAF8F3 0%, #F5ECDB 100%) !important;
    border-radius: 16px !important;
    padding: 2.2rem 2rem !important;
    border: 1.5px solid rgba(197, 160, 89, 0.4) !important;
    box-shadow: 0 8px 25px rgba(44, 30, 20, 0.06) !important;
}

.gift-store-banner p {
    font-size: 1.25rem !important;
    color: #2C1E14 !important;
    font-weight: 700 !important;
    margin-bottom: 1.2rem !important;
}

.btn-gift-notify {
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    color: #2C1E14 !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.85rem 2.2rem !important;
    box-shadow: 0 4px 15px rgba(197, 160, 89, 0.3) !important;
}

.btn-gift-notify:hover {
    background: linear-gradient(135deg, #D4AF37 0%, #C5A059 100%) !important;
    color: #1A0F07 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 22px rgba(197, 160, 89, 0.42) !important;
}

/* 8. Giveaways Section: Deep Sacred Roasted Espresso with Translucent Cards */
.freebies-section {
    background: linear-gradient(135deg, #3A2312 0%, #4A3319 50%, #52381B 100%) !important;
    border-top: 2px solid var(--clr-gold) !important;
    border-bottom: 2px solid var(--clr-gold) !important;
}

.freebie-card {
    background-color: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(197, 160, 89, 0.32) !important;
    border-radius: 14px !important;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2) !important;
}

.freebie-card:hover {
    background-color: rgba(255, 255, 255, 0.09) !important;
    border-color: var(--clr-gold) !important;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35) !important;
}

.freebie-card .btn,
.freebie-card .trigger-freebie {
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    color: #2C1E14 !important;
    border: none !important;
    font-weight: 700 !important;
    border-radius: 6px !important;
    box-shadow: 0 4px 14px rgba(197, 160, 89, 0.28) !important;
    padding: 0.72rem 1.4rem !important;
}

.freebie-card .btn:hover,
.freebie-card .trigger-freebie:hover {
    background: linear-gradient(135deg, #D4AF37 0%, #C5A059 100%) !important;
    color: #1A0F07 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 18px rgba(197, 160, 89, 0.42) !important;
}

/* 9. Final CTA & Community Section */
.cta {
    background: #FAF6EE !important;
    background: linear-gradient(180deg, #FAF6EE 0%, #FAF4EA 100%) !important;
    border-top: 1px solid rgba(197, 160, 89, 0.22) !important;
}

.cta-box {
    background-color: #FFFFFF !important;
    border: 1.5px solid rgba(197, 160, 89, 0.38) !important;
    border-radius: 18px !important;
    box-shadow: 0 10px 35px rgba(44, 30, 20, 0.06) !important;
}

.cta-content {
    background: linear-gradient(135deg, #FAF8F3 0%, #F5ECDB 100%) !important;
    border-right: 1px solid rgba(44, 30, 20, 0.08) !important;
}

.cta-content h2,
.community-content h2 {
    color: #2C1E14 !important;
}

.cta-content p,
.community-content p {
    color: #5C4A3E !important;
}

.community-content {
    background-color: #FFFFFF !important;
}

.subscribe-form input {
    background: #FFFFFF !important;
    border: 1.5px solid rgba(44, 30, 20, 0.16) !important;
    color: #2C1E14 !important;
    border-radius: 6px !important;
}

.subscribe-form input:focus {
    border-color: var(--clr-gold) !important;
    box-shadow: 0 0 0 3px rgba(197, 160, 89, 0.2) !important;
    outline: none;
}

/* 10. Footer Section */
.footer {
    background: linear-gradient(135deg, #2C1E14 0%, #382413 50%, #20150D 100%) !important;
    border-top: 2px solid var(--clr-gold) !important;
    color: #D9CEC5 !important;
}

.footer h3 {
    color: #DFC080 !important;
    font-family: var(--font-heading) !important;
}

.footer a {
    color: #D9CEC5 !important;
    transition: color 0.2s ease !important;
}

.footer a:hover {
    color: #DFC080 !important;
}

.footer-bottom {
    border-top: 1px solid rgba(197, 160, 89, 0.2) !important;
    color: #A99B91 !important;
}
'''

# Check if enhancements already present, if so replace or append
marker = "/* ==========================================================================\n   LUXURY CREAM & GOLD MASTER PALETTE ENHANCEMENTS"
idx = css.find(marker)
if idx != -1:
    css = css[:idx] + enhancements_css.strip() + "\n"
    print("Replaced existing master palette enhancements.")
else:
    css = css + "\n" + enhancements_css.strip() + "\n"
    print("Appended master palette enhancements.")

with open(r'd:\Sattvic Books\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css successfully updated!")

