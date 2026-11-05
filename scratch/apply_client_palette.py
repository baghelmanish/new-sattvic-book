import re

# Read style.css
with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update :root
old_root = """:root {
    /* Colors - Sattvic Books Cream & Gold Luxury Brand Palette */
    --clr-primary: #2C1E14;      /* Deep Warm Espresso (Headings & Luxury Brand Contrast) */
    --clr-primary-light: #4A3319; /* Warm Roasted Bronze */
    --clr-primary-dark: #382413;  /* Deep Roasted Espresso */
    --clr-gold: #C5A059;         /* Sacred Gold (Primary Accent & Button Fill) */
    --clr-gold-light: #DFC080;   /* Light Cream Gold */
    --clr-gold-dark: #A07C32;    /* Antique Deep Gold */
    --clr-gold-hover: #B89047;   /* Rich Gold Hover */
    --clr-secondary: #C5A059;    /* Sacred Gold for Accents & Highlights */
    --clr-bg: #FAF7F2;           /* Warm Luxury Cream/Ivory */
    --clr-surface: #FFFFFF;      /* Pure White for Cards & Surfaces */
    --clr-text: #2C1E14;         /* Deep Warm Espresso */
    --clr-text-light: #6A5A4D;   /* Warm Taupe Brown */
    --clr-dark-bg: #4A3319;      /* Warm Roasted Espresso for Dark Sections & Footer */
    
    /* Typography */
    --font-heading: 'Playfair Display', serif;
    --font-body: 'Inter', sans-serif;
    
    /* Spacing & Layout */
    --section-padding: 5rem 0;
    --container-width: 1200px;
    
    /* Effects */
    --shadow-soft: 0 10px 40px rgba(44, 30, 20, 0.06);
    --shadow-hover: 0 15px 50px rgba(197, 160, 89, 0.2);
    --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    --radius: 12px;
}"""

new_root = """:root {
    /* Colors - Sattvic Books Exact Client Luxury Palette */
    --clr-primary: #382618;       /* Dark brown (Headings & Primary Contrast) */
    --clr-primary-light: #5E4A39; /* Warm brown (Paragraphs & Body Text) */
    --clr-primary-dark: #322214;  /* Dark brown (Giveaways & Footer Background) */
    --clr-gold: #D7B347;          /* Gold background for primary buttons */
    --clr-gold-light: #F6EBDD;    /* Soft beige for Book Shelf */
    --clr-gold-dark: #855E20;     /* Dark gold for small labels & eyebrows */
    --clr-gold-hover: #C9A336;    /* Rich radiant gold button hover */
    --clr-secondary: #D7B347;     /* Gold accent */
    --clr-bg: #FAF6EE;            /* Warm cream background (Catalog, Gift Store, Newsletter) */
    --clr-cream: #FAF6EE;         /* Warm cream */
    --clr-soft-beige: #F6EBDD;    /* Soft beige (Book Shelf) */
    --clr-surface: #FFFFFF;       /* Pure white for Category, Book & Gift cards */
    --clr-text: #382618;          /* Dark brown headings & emphasis */
    --clr-text-light: #5E4A39;    /* Warm brown paragraphs */
    --clr-dark-bg: #322214;       /* Dark brown (Giveaways & Footer) */
    --clr-cream-text: #FBF5E9;    /* Cream text & links for Giveaways & Footer */
    
    /* Typography */
    --font-heading: 'Playfair Display', serif;
    --font-body: 'Inter', sans-serif;
    
    /* Spacing & Layout */
    --section-padding: 5rem 0;
    --container-width: 1200px;
    
    /* Effects */
    --shadow-soft: 0 10px 40px rgba(56, 38, 24, 0.05);
    --shadow-hover: 0 15px 50px rgba(215, 179, 71, 0.2);
    --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    --radius: 12px;
}"""

# 2. Update lines ~24727 .books rule
old_books_rule = """.books {
    background-color: #F5E8D6 !important;
    background: linear-gradient(180deg, #F7E9DC 0%, #F3E5D0 50%, #FAE6CE 100%) !important;
    border-top: 1.5px solid rgba(197, 160, 89, 0.35);
    border-bottom: 1.5px solid rgba(197, 160, 89, 0.35);
    position: relative;
    overflow: hidden;
}"""

new_books_rule = """.books {
    background-color: #F6EBDD !important;
    background: #F6EBDD !important;
    border-top: 1.5px solid rgba(133, 94, 32, 0.25);
    border-bottom: 1.5px solid rgba(133, 94, 32, 0.25);
    position: relative;
    overflow: hidden;
}"""

# 3. Master Section block replacement
# Locate start of 5. Featured Catalog
start_marker = "/* 5. Featured Catalog (Explore Our Catalog)"
end_marker = "/* ==========================================================================\n   UNIFIED LUXURY BUTTON SUITE"
if end_marker not in css:
    end_marker = "UNIFIED LUXURY BUTTON SUITE"

s_idx = css.find(start_marker)
e_idx = css.find(end_marker)
if e_idx != -1:
    e_idx = css.rfind("/*", 0, e_idx)

print("start_marker at:", s_idx)
print("end_marker at:", e_idx)

new_master_section = """/* ==========================================================================
   HOMEPAGE CLIENT SPECIFICATION PALETTE — EXACT HARMONIZED LUXURY THEME
   ========================================================================== */

/* --- 1. GLOBAL LIGHT SECTIONS HEADINGS, PARAGRAPHS & SMALL LABELS --- */

/* Light sections: Hero, Catalog, Book Shelf, Why Buy, Gift Store, CTA / Newsletter */
.hero,
.collections,
.books,
.why-buy-section,
.gift-store-section,
.cta {
    color: #5E4A39;
}

/* Light sections ki headings: Dark brown #382618 */
.hero h1,
.hero h2,
.hero h3,
.hero-text h1,
.hero-text h2,
.hero-title,
.collections h2,
.collections-header h2,
.collection-card h3,
.books h2,
.sattvic-book-grid h3,
.sattvic-book-title,
.why-buy-section h2,
.why-buy-card h3,
.gift-store-section h2,
.gift-store-card h3,
.gift-store-banner p,
.cta h2,
.cta-box h2,
.cta-content h2,
.community-content h2,
.section-header h2,
.section-title {
    color: #382618 !important;
    font-family: var(--font-heading) !important;
    font-weight: 700 !important;
}

/* Light sections ke paragraphs: Warm brown #5E4A39 */
.hero p,
.hero-text p,
.hero-subtitle,
.collections p,
.collections-header p,
.collections-subtitle,
.collection-card p,
.books p,
.sattvic-book-author,
.sattvic-book-desc,
.why-buy-section p,
.why-buy-subtitle,
.why-buy-card p,
.gift-store-section p,
.gift-store-subtitle,
.gift-store-card p,
.cta p,
.cta-box p,
.cta-content p,
.community-content p,
.community-disclaimer,
.section-header p,
.section-subtitle {
    color: #5E4A39 !important;
    line-height: 1.65 !important;
}

/* Chhote labels, jaise Featured Catalog aur Our Book Shelf: Dark gold #855E20 */
.eyebrow,
.section-eyebrow,
.collections-eyebrow,
.s-bookshelf-eyebrow,
.why-buy-eyebrow,
.gift-store-eyebrow,
.hero-eyebrow,
.cta-box .eyebrow,
.section-header .eyebrow,
.hero-text .eyebrow {
    color: #855E20 !important;
    font-family: var(--font-body) !important;
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    letter-spacing: 1.8px !important;
    text-transform: uppercase !important;
    display: inline-block !important;
    margin-bottom: 0.75rem !important;
}

.eyebrow i,
.section-eyebrow i {
    color: #855E20 !important;
    margin-right: 0.35rem !important;
}


/* --- 2. CATALOG SECTION: WARM CREAM #FAF6EE BACKGROUND & WHITE #FFFFFF CARDS --- */
.collections,
#catalogs {
    background: #FAF6EE !important;
    background-color: #FAF6EE !important;
    border-bottom: 1px solid rgba(133, 94, 32, 0.15) !important;
}

/* Category cards: White #FFFFFF */
.collections .collection-card,
.collection-card {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border: 1px solid rgba(133, 94, 32, 0.16) !important;
    border-radius: 14px !important;
    box-shadow: 0 6px 20px rgba(56, 38, 24, 0.05) !important;
    transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
}

.collections .collection-card:hover,
.collection-card:hover {
    background: #FFFFFF !important;
    border-color: rgba(215, 179, 71, 0.6) !important;
    transform: translateY(-5px) !important;
    box-shadow: 0 16px 36px rgba(56, 38, 24, 0.09) !important;
}

.collections .icon-wrapper {
    width: 62px !important;
    height: 62px !important;
    border-radius: 50% !important;
    background: rgba(215, 179, 71, 0.16) !important;
    border: 1.5px solid rgba(215, 179, 71, 0.35) !important;
    color: #855E20 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 1.5rem !important;
    margin: 0 auto 1.2rem auto !important;
    transition: all 0.35s ease !important;
}

.collections .collection-card:hover .icon-wrapper {
    background: #D7B347 !important;
    color: #382618 !important;
    transform: scale(1.08) !important;
    box-shadow: 0 6px 18px rgba(215, 179, 71, 0.35) !important;
}


/* --- 3. BOOK SHELF SECTION: SOFT BEIGE #F6EBDD BACKGROUND & WHITE #FFFFFF CARDS --- */
.books,
#books,
.sattvic-book-shelf-section {
    background: #F6EBDD !important;
    background-color: #F6EBDD !important;
    border-top: 1px solid rgba(133, 94, 32, 0.15) !important;
    border-bottom: 1px solid rgba(133, 94, 32, 0.15) !important;
    position: relative;
    overflow: hidden;
}

/* Book cards: White #FFFFFF */
.sattvic-book-card,
.books .sattvic-book-card,
.books .shambhala-book-card,
.shambhala-book-card {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border: 1px solid rgba(133, 94, 32, 0.16) !important;
    border-radius: 14px !important;
    box-shadow: 0 6px 20px rgba(56, 38, 24, 0.05) !important;
    padding: 1.4rem !important;
    transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
}

.sattvic-book-card:hover,
.books .sattvic-book-card:hover,
.books .shambhala-book-card:hover {
    background: #FFFFFF !important;
    border-color: rgba(215, 179, 71, 0.6) !important;
    transform: translateY(-5px) !important;
    box-shadow: 0 16px 36px rgba(56, 38, 24, 0.09) !important;
}

.s-book-price {
    color: #382618 !important;
    font-weight: 700 !important;
}

.s-book-price .price-val {
    color: #382618 !important;
    font-size: 1.15rem !important;
    font-weight: 800 !important;
}

.s-book-isbn {
    font-size: 0.76rem !important;
    color: #5E4A39 !important;
    font-weight: 600 !important;
    margin-bottom: 0.6rem !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.35rem !important;
}

.s-book-isbn i {
    color: #855E20 !important;
    font-size: 0.78rem !important;
}

.badge-free {
    display: inline-block !important;
    background: rgba(40, 167, 69, 0.12) !important;
    color: #28A745 !important;
    font-size: 0.74rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    padding: 0.15rem 0.5rem !important;
    border-radius: 4px !important;
    vertical-align: middle !important;
    margin-left: 0.35rem !important;
    font-family: var(--font-body) !important;
}


/* --- 4. WHY BUY SECTION: CRISP WHITE BACKGROUND WITH WHITE CARDS --- */
.why-buy-section {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border-top: 1px solid rgba(133, 94, 32, 0.12) !important;
    border-bottom: 1px solid rgba(133, 94, 32, 0.12) !important;
}

.why-buy-card {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border-radius: 14px !important;
    padding: 2.2rem 1.6rem 2rem !important;
    border: 1px solid rgba(133, 94, 32, 0.16) !important;
    box-shadow: 0 6px 20px rgba(56, 38, 24, 0.05) !important;
    transition: all 0.35s ease !important;
}

.why-buy-card:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 16px 36px rgba(56, 38, 24, 0.09) !important;
    border-color: rgba(215, 179, 71, 0.6) !important;
}

.why-buy-icon-wrapper,
.why-buy-icon-pill {
    width: 60px !important;
    height: 60px !important;
    border-radius: 50% !important;
    background: rgba(215, 179, 71, 0.16) !important;
    border: 1.5px solid rgba(215, 179, 71, 0.35) !important;
    color: #855E20 !important;
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
    background: #D7B347 !important;
    color: #382618 !important;
    transform: scale(1.08) !important;
    box-shadow: 0 6px 18px rgba(215, 179, 71, 0.35) !important;
}

.why-buy-num {
    display: none !important;
}


/* --- 5. GIFT STORE SECTION: WARM CREAM #FAF6EE BACKGROUND & WHITE #FFFFFF CARDS --- */
.gift-store-section,
#gift-store {
    background: #FAF6EE !important;
    background-color: #FAF6EE !important;
    border-top: 1px solid rgba(133, 94, 32, 0.15) !important;
    border-bottom: 1px solid rgba(133, 94, 32, 0.15) !important;
}

/* Gift cards: White #FFFFFF */
.gift-store-card {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border-radius: 14px !important;
    padding: 2.2rem 1.6rem 2rem !important;
    border: 1px solid rgba(133, 94, 32, 0.16) !important;
    box-shadow: 0 6px 20px rgba(56, 38, 24, 0.05) !important;
    transition: all 0.35s ease !important;
}

.gift-store-card:hover {
    background: #FFFFFF !important;
    transform: translateY(-5px) !important;
    box-shadow: 0 16px 36px rgba(56, 38, 24, 0.09) !important;
    border-color: rgba(215, 179, 71, 0.6) !important;
}

.gift-card-icon-wrap {
    width: 60px !important;
    height: 60px !important;
    border-radius: 50% !important;
    background: rgba(215, 179, 71, 0.16) !important;
    border: 1.5px solid rgba(215, 179, 71, 0.35) !important;
    color: #855E20 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 1.5rem !important;
    margin: 0 auto 1.2rem auto !important;
    box-shadow: none !important;
    transition: all 0.35s ease !important;
}

.gift-store-card:hover .gift-card-icon-wrap {
    background: #D7B347 !important;
    color: #382618 !important;
    transform: scale(1.08) !important;
    box-shadow: 0 6px 18px rgba(215, 179, 71, 0.35) !important;
}

.gift-badge-coming-soon {
    font-family: var(--font-body) !important;
    font-size: 0.74rem !important;
    font-weight: 700 !important;
    letter-spacing: 1.1px !important;
    color: #855E20 !important;
    background: rgba(215, 179, 71, 0.16) !important;
    border: 1px solid rgba(133, 94, 32, 0.25) !important;
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
    background-color: #FFFFFF !important;
    border-radius: 16px !important;
    padding: 2.2rem 2rem !important;
    border: 1.5px solid rgba(215, 179, 71, 0.4) !important;
    box-shadow: 0 8px 25px rgba(56, 38, 24, 0.06) !important;
}

.gift-store-banner p {
    font-size: 1.25rem !important;
    color: #382618 !important;
    font-weight: 700 !important;
    margin-bottom: 1.2rem !important;
}


/* --- 6. GIVEAWAYS SECTION: DARK BROWN #322214 BACKGROUND & CREAM #FBF5E9 TEXT --- */
.freebies-section,
#freebies {
    background: #322214 !important;
    background-color: #322214 !important;
    border-top: 2px solid #D7B347 !important;
    border-bottom: 2px solid #D7B347 !important;
    color: #FBF5E9 !important;
}

.freebies-section h2,
.freebies-section .section-header h2 {
    color: #FBF5E9 !important;
}

.freebies-section p,
.freebies-section .section-header p {
    color: #FBF5E9 !important;
    opacity: 0.92;
}

.freebies-section .eyebrow {
    color: #D7B347 !important;
}

.freebies-section .eyebrow i {
    color: #D7B347 !important;
}

.freebie-card {
    background: rgba(251, 245, 233, 0.05) !important;
    background-color: rgba(251, 245, 233, 0.05) !important;
    border: 1px solid rgba(215, 179, 71, 0.3) !important;
    border-radius: 14px !important;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25) !important;
    color: #FBF5E9 !important;
}

.freebie-card:hover {
    background: rgba(251, 245, 233, 0.09) !important;
    border-color: #D7B347 !important;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4) !important;
}

.freebie-card h3 {
    color: #FBF5E9 !important;
}

.freebie-card p {
    color: #E8DAC8 !important;
}

.freebie-card .icon-wrapper,
.freebie-icon {
    color: #D7B347 !important;
}


/* --- 7. NEWSLETTER & CTA SECTION: WARM CREAM #FAF6EE BACKGROUND & WHITE #FFFFFF CARDS --- */
.cta,
#community {
    background: #FAF6EE !important;
    background-color: #FAF6EE !important;
    border-top: 1px solid rgba(133, 94, 32, 0.15) !important;
}

.cta-box {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border: 1.5px solid rgba(215, 179, 71, 0.38) !important;
    border-radius: 18px !important;
    box-shadow: 0 10px 35px rgba(56, 38, 24, 0.06) !important;
    overflow: hidden !important;
}

.cta-content {
    background: #FAF6EE !important;
    background-color: #FAF6EE !important;
    border-right: 1px solid rgba(133, 94, 32, 0.12) !important;
}

.community-content {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
}

.subscribe-form input {
    background: #FFFFFF !important;
    border: 1.5px solid rgba(56, 38, 24, 0.18) !important;
    color: #382618 !important;
    border-radius: 6px !important;
}

.subscribe-form input:focus {
    border-color: #D7B347 !important;
    box-shadow: 0 0 0 3px rgba(215, 179, 71, 0.25) !important;
    outline: none;
}


/* --- 8. FOOTER SECTION: DARK BROWN #322214 BACKGROUND & CREAM #FBF5E9 TEXT & LINKS --- */
.footer {
    background: #322214 !important;
    background-color: #322214 !important;
    border-top: 2px solid #D7B347 !important;
    color: #FBF5E9 !important;
    padding: 4rem 0 2rem;
}

.footer h3,
.footer h4,
.footer-col h4,
.footer-title {
    color: #FBF5E9 !important;
    font-family: var(--font-heading) !important;
}

.footer p,
.footer-desc,
.footer-text,
.footer-bottom p,
.copyright {
    color: #FBF5E9 !important;
    opacity: 0.92;
}

.footer a,
.footer-links a,
.footer-bottom-links a,
.footer-bottom a {
    color: #FBF5E9 !important;
    transition: color 0.25s ease !important;
}

.footer a:hover,
.footer-links a:hover,
.footer-bottom-links a:hover,
.footer-bottom a:hover {
    color: #D7B347 !important;
}

.footer-bottom {
    border-top: 1px solid rgba(251, 245, 233, 0.12) !important;
    color: #FBF5E9 !important;
}

.footer-social a,
.social-icon {
    border: 1px solid rgba(251, 245, 233, 0.22) !important;
    color: #FBF5E9 !important;
    background: transparent !important;
    transition: all 0.25s ease !important;
}

.footer-social a:hover,
.social-icon:hover {
    background: #D7B347 !important;
    color: #322214 !important;
    border-color: #D7B347 !important;
}


"""

# 4. Update UNIFIED LUXURY BUTTON SUITE to use #D7B347 background and #382618 text
new_button_suite = """/* ==========================================================================
   UNIFIED LUXURY BUTTON SUITE — GOLD #D7B347 BACKGROUND & DARK BROWN #382618 TEXT
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
    transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    text-decoration: none !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 0.45rem !important;
    cursor: pointer !important;
    outline: none !important;
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
    background: #C9A336 !important;
    background-color: #C9A336 !important;
    color: #20140B !important;
    border: none !important;
    transform: translateY(-2px) !important;
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
    transform: translateY(0) !important;
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

# Let's perform replacements
css_up = css.replace('\r\n', '\n')
old_root_norm = old_root.replace('\r\n', '\n')
new_root_norm = new_root.replace('\r\n', '\n')
old_books_norm = old_books_rule.replace('\r\n', '\n')
new_books_norm = new_books_rule.replace('\r\n', '\n')

r1 = False
if old_root_norm in css_up:
    css_up = css_up.replace(old_root_norm, new_root_norm)
    r1 = True

r2 = False
if old_books_norm in css_up:
    css_up = css_up.replace(old_books_norm, new_books_norm)
    r2 = True

# Replace section block and button suite
btn_suite_start = css_up.find("/* ==========================================================================\n   UNIFIED LUXURY BUTTON SUITE")
if btn_suite_start == -1:
    btn_suite_start = css_up.find("UNIFIED LUXURY BUTTON SUITE")
    btn_suite_start = css_up.rfind("/*", 0, btn_suite_start)

sec_block_start = css_up.find("/* 5. Featured Catalog (Explore Our Catalog)")

print("r1 (:root) =", r1)
print("r2 (.books) =", r2)
print("sec_block_start =", sec_block_start)
print("btn_suite_start =", btn_suite_start)

if sec_block_start != -1 and btn_suite_start != -1:
    css_final = css_up[:sec_block_start] + new_master_section + new_button_suite
    with open(r'd:\Sattvic Books\style.css', 'w', encoding='utf-8') as f:
        f.write(css_final)
    print("Updated style.css successfully!")
else:
    print("Could not find section block or button suite positions!")

