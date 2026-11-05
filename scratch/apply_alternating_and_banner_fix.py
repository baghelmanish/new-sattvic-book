with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

start_marker = "/* ==========================================================================\n   SITE-WIDE CLIENT SPECIFICATION PALETTE"
end_marker = "/* ==========================================================================\n   UNIFIED LUXURY BUTTON SUITE"

s_idx = css.find(start_marker)
e_idx = css.find(end_marker)

new_palette_section = """/* ==========================================================================
   SITE-WIDE CLIENT SPECIFICATION PALETTE — HARMONIZED LUXURY THEME ACROSS ALL PAGES
   ========================================================================== */

/* --- 1. INTERNAL PAGE HERO BANNERS & HEADERS (RICH DARK ESPRESSO WITH IVORY/CREAM TEXT) --- */
.about-header-bg,
.contact-header-bg,
.events-hero,
.press-header-bg {
    background: #322214 !important;
    background: linear-gradient(135deg, #322214 0%, #382618 50%, #20140B 100%) !important;
    position: relative !important;
    overflow: hidden !important;
    padding: 5.5rem 0 4rem 0 !important;
    text-align: center !important;
    border-bottom: 2px solid #D7B347 !important;
    color: #FBF5E9 !important;
}

/* Gold Eyebrow in Banners */
.about-header-bg .eyebrow,
.contact-header-bg .eyebrow,
.events-hero .eyebrow,
.press-header-bg .eyebrow,
.about-header-bg .text-gold,
.contact-header-bg .text-gold,
.events-hero .text-gold,
.press-header-bg .text-gold {
    color: #D7B347 !important;
    font-family: var(--font-body) !important;
    font-size: 0.88rem !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    display: inline-block !important;
    margin-bottom: 0.85rem !important;
}

/* Headings in Banners: Crisp Radiant Cream/Ivory with Playfair Serif */
.about-header-bg h1,
.about-header-bg h2,
.contact-header-bg h1,
.contact-header-bg h2,
.events-hero h1,
.events-hero h2,
.press-header-bg h1,
.press-header-bg h2 {
    color: #FBF5E9 !important;
    font-family: var(--font-heading) !important;
    font-size: 2.8rem !important;
    font-weight: 700 !important;
    line-height: 1.25 !important;
    margin-bottom: 1rem !important;
    max-width: 960px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.4) !important;
}

/* Subtitles / Paragraphs in Banners: High-Contrast Warm Pale Cream */
.about-header-bg p,
.contact-header-bg p,
.events-hero p,
.press-header-bg p {
    color: #E8DAC8 !important;
    font-family: var(--font-body) !important;
    font-size: 1.15rem !important;
    line-height: 1.7 !important;
    max-width: 800px !important;
    margin: 0 auto !important;
    opacity: 0.96 !important;
    text-shadow: 0 1px 4px rgba(0, 0, 0, 0.3) !important;
}

/* Subtle Gold Ambient Radial Glow */
.about-header-bg::before,
.contact-header-bg::before,
.events-hero::before,
.press-header-bg::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 50% 30%, rgba(215, 179, 71, 0.16) 0%, transparent 68%);
    pointer-events: none;
}


/* --- 2. SECTION BACKGROUND ALTERNATION (NATURAL VISUAL RHYTHM ACROSS ALL PAGES) --- */
body {
    background-color: #FAF6EE;
    color: #5E4A39;
    font-family: var(--font-body);
}

/* A. Crisp White Sections (#FFFFFF) */
.about-story-section,
.why-buy-section,
#get-in-touch,
#media-channels,
#learn-share-inspire,
section[style*="#FFFFFF"],
section[style*="#ffffff"],
section.bg-white {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
}

/* B. Warm Cream Sections (#FAF6EE) */
.collections,
#catalogs,
.gift-store-section,
#gift-store,
.cta,
#community,
.mission-vision-section,
#how-can-we-help,
section[style*="#FAF6EE"],
section[style*="#faf6ee"],
section.bg-cream {
    background-color: #FAF6EE !important;
    background: #FAF6EE !important;
}

/* C. Soft Beige Sections (#F6EBDD) */
.books,
#books,
.sattvic-book-shelf-section,
section[style*="#F6EBDD"],
section[style*="#f6ebdd"],
section.bg-soft-beige {
    background-color: #F6EBDD !important;
    background: #F6EBDD !important;
    border-top: 1px solid rgba(133, 94, 32, 0.15) !important;
    border-bottom: 1px solid rgba(133, 94, 32, 0.15) !important;
}

/* D. Deep Sacred Dark Sections (#322214) */
.bg-dark,
#philosophy,
.freebies-section,
#freebies,
.footer {
    background-color: #322214 !important;
    background: #322214 !important;
    color: #FBF5E9 !important;
}


/* --- 3. LIGHT SECTIONS HEADINGS: DARK BROWN #382618 --- */
section:not(.bg-dark):not(.freebies-section) h1,
section:not(.bg-dark):not(.freebies-section) h2,
section:not(.bg-dark):not(.freebies-section) h3,
section:not(.bg-dark):not(.freebies-section) h4,
section:not(.bg-dark):not(.freebies-section) h5,
section:not(.bg-dark):not(.freebies-section) h6,
.hero h1,
.hero h2,
.hero h3,
.hero-text h1,
.hero-text h2,
.hero-title,
.section-title,
.page-title,
.card-title,
.collection-card h3,
.sattvic-book-title,
.sattvic-book-card h3,
.why-buy-card h3,
.gift-store-card h3,
.gift-store-banner p,
.cta-box h2,
.cta-content h2,
.community-content h2,
.conversation-closing-box h2,
.next-event-cta-box h2,
.partner-showcase-card h3,
.press-book-card h3,
.press-kit-asset-card h3,
.custom-resource-card h3,
.contact-channel-card h3,
.mv-card h3,
.phil-tenet-card h3,
.featured-press-box h3,
.featured-diwali-card h3,
.event-card h3 {
    color: #382618 !important;
    font-family: var(--font-heading) !important;
    font-weight: 700 !important;
}


/* --- 4. LIGHT SECTIONS PARAGRAPHS: WARM BROWN #5E4A39 --- */
section:not(.bg-dark):not(.freebies-section) p,
.hero p,
.hero-text p,
.hero-subtitle,
.section-subtitle,
.lead,
.card-text,
.desc,
.bio-text,
.story-text,
.event-desc,
.partner-desc,
.press-desc,
.body-text,
.collection-card p,
.sattvic-book-author,
.sattvic-book-desc,
.why-buy-card p,
.gift-store-card p,
.cta-box p,
.cta-content p,
.community-content p,
.community-disclaimer,
.conversation-closing-box p,
.next-event-cta-box p,
.partner-showcase-card p,
.press-book-card p,
.press-kit-asset-card p,
.custom-resource-card p,
.contact-channel-card p,
.mv-card p,
.phil-tenet-card p {
    color: #5E4A39 !important;
    line-height: 1.65 !important;
}


/* --- 5. SMALL LABELS & EYEBROWS IN LIGHT SECTIONS: DARK GOLD #855E20 --- */
section:not(.bg-dark):not(.freebies-section) .eyebrow,
.hero-eyebrow,
.hero-text .eyebrow,
.section-eyebrow,
.collections-eyebrow,
.s-bookshelf-eyebrow,
.why-buy-eyebrow,
.gift-store-eyebrow,
.cta-box .eyebrow,
.category-tag,
.tag,
.badge-label,
.meta-label,
.event-date-badge,
.press-tag,
.partner-tag {
    color: #855E20 !important;
    font-family: var(--font-body) !important;
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    letter-spacing: 1.8px !important;
    text-transform: uppercase !important;
    display: inline-block !important;
    margin-bottom: 0.75rem !important;
}

section:not(.bg-dark):not(.freebies-section) .eyebrow i,
.section-eyebrow i,
.category-tag i,
.meta-label i {
    color: #855E20 !important;
    margin-right: 0.35rem !important;
}


/* --- 6. ALL CARDS & SURFACE BOXES: PURE WHITE #FFFFFF --- */
.collection-card,
.sattvic-book-card,
.shambhala-book-card,
.why-buy-card,
.gift-store-card,
.partner-showcase-card,
.press-book-card,
.press-kit-asset-card,
.custom-resource-card,
.contact-channel-card,
.channel-card,
.mv-card,
.phil-tenet-card,
.featured-press-box,
.featured-diwali-card,
.event-card,
.events-image-card,
.about-image-card,
.about-credentials-box,
.conversation-closing-box,
.next-event-cta-box,
.cta-box,
.modal-box,
.community-content,
.gift-store-banner {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border: 1px solid rgba(133, 94, 32, 0.16) !important;
    border-radius: 14px !important;
    box-shadow: 0 6px 20px rgba(56, 38, 24, 0.05) !important;
    transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
}

.collection-card:hover,
.sattvic-book-card:hover,
.shambhala-book-card:hover,
.why-buy-card:hover,
.gift-store-card:hover,
.partner-showcase-card:hover,
.press-book-card:hover,
.press-kit-asset-card:hover,
.custom-resource-card:hover,
.contact-channel-card:hover,
.mv-card:hover,
.phil-tenet-card:hover,
.featured-press-box:hover,
.featured-diwali-card:hover,
.event-card:hover {
    background: #FFFFFF !important;
    border-color: rgba(215, 179, 71, 0.6) !important;
    transform: translateY(-5px) !important;
    box-shadow: 0 16px 36px rgba(56, 38, 24, 0.09) !important;
}

/* Icon Badges inside Cards */
.icon-wrapper,
.why-buy-icon-wrapper,
.why-buy-icon-pill,
.gift-card-icon-wrap,
.mv-icon-badge,
.contact-icon-badge {
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

.collection-card:hover .icon-wrapper,
.why-buy-card:hover .why-buy-icon-wrapper,
.why-buy-card:hover .why-buy-icon-pill,
.gift-store-card:hover .gift-card-icon-wrap,
.mv-card:hover .mv-icon-badge,
.contact-channel-card:hover .contact-icon-badge {
    background: #D7B347 !important;
    color: #382618 !important;
    transform: scale(1.08) !important;
    box-shadow: 0 6px 18px rgba(215, 179, 71, 0.35) !important;
}

.why-buy-num {
    display: none !important;
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


/* --- 7. GIVEAWAYS & FOOTER: DARK BROWN #322214 BACKGROUND & CREAM #FBF5E9 TEXT --- */
.freebies-section,
#freebies,
.footer {
    background: #322214 !important;
    background-color: #322214 !important;
    border-top: 2px solid #D7B347 !important;
    color: #FBF5E9 !important;
}

.freebies-section h2,
.freebies-section .section-header h2,
.footer h3,
.footer h4,
.footer-col h4,
.footer-title {
    color: #FBF5E9 !important;
    font-family: var(--font-heading) !important;
}

.freebies-section p,
.freebies-section .section-header p,
.footer p,
.footer-desc,
.footer-text,
.footer-bottom p,
.copyright {
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

if s_idx != -1 and e_idx != -1:
    css_up = css[:s_idx] + new_palette_section + css[e_idx:]
    with open(r'd:\Sattvic Books\style.css', 'w', encoding='utf-8') as f:
        f.write(css_up)
    print("Updated style.css with restored alternating backgrounds and clear banner text!")
else:
    print("Could not find markers in style.css!")

