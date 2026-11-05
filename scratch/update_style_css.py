with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .books section background and corner watermarks
old_books_bg = '''/* 3. Our Book Shelf (Featured Publications) \u2014 Distinct Sattvic Herbal Sage Background */
.books {
    background: linear-gradient(180deg, #FAF7F2 0%, #F5EFEB 100%) !important;
    border-top: 1px solid rgba(44, 30, 20, 0.09);
    border-bottom: 1px solid rgba(44, 30, 20, 0.09);
    position: relative;
}

.books .sattvic-book-card,
.books .shambhala-book-card {
    background: #FFFFFF !important;
    border: 1px solid rgba(44, 30, 20, 0.12) !important;
    box-shadow: 0 8px 25px rgba(44, 30, 20, 0.07) !important;
}

.books .sattvic-book-card:hover,
.books .shambhala-book-card:hover {
    box-shadow: 0 16px 40px rgba(44, 30, 20, 0.16) !important;
    border-color: var(--clr-gold) !important;
}'''

new_books_bg = '''/* 3. Our Book Shelf (Featured Publications) — Warm Luxury Champagne Cream with Botanical Watermarks */
.books {
    background: #FAF4E8 !important;
    background: linear-gradient(180deg, #FBF6EC 0%, #FAF4E8 50%, #F5ECDC 100%) !important;
    border-top: 1px solid rgba(197, 160, 89, 0.22);
    border-bottom: 1px solid rgba(197, 160, 89, 0.22);
    position: relative;
    overflow: hidden;
}

.books::before {
    content: '';
    position: absolute;
    top: -15px;
    left: -15px;
    width: 220px;
    height: 220px;
    background-image: url('assets/botanical-corner.svg');
    background-size: contain;
    background-repeat: no-repeat;
    pointer-events: none;
    z-index: 1;
    opacity: 0.85;
}

.books::after {
    content: '';
    position: absolute;
    top: -15px;
    right: -15px;
    width: 220px;
    height: 220px;
    background-image: url('assets/botanical-corner.svg');
    background-size: contain;
    background-repeat: no-repeat;
    transform: scaleX(-1);
    pointer-events: none;
    z-index: 1;
    opacity: 0.85;
}

.books .container {
    position: relative;
    z-index: 2;
}

.books .sattvic-book-card,
.books .shambhala-book-card {
    background: #FFFFFF !important;
    border: 1px solid rgba(44, 30, 20, 0.08) !important;
    box-shadow: 0 4px 18px rgba(44, 30, 20, 0.05) !important;
}

.books .sattvic-book-card:hover,
.books .shambhala-book-card:hover {
    box-shadow: 0 14px 34px rgba(44, 30, 20, 0.12) !important;
    border-color: rgba(197, 160, 89, 0.45) !important;
}'''

# Normalize line endings for replacement
def normalize_and_replace(source, old_s, new_s):
    old_crlf = old_s.replace('\r\n', '\n').replace('\n', '\r\n')
    old_lf = old_s.replace('\r\n', '\n')
    if old_crlf in source:
        return source.replace(old_crlf, new_s.replace('\n', '\r\n')), True
    elif old_lf in source:
        return source.replace(old_lf, new_s), True
    return source, False

css, ok1 = normalize_and_replace(css, old_books_bg, new_books_bg)
print(f"Books background replaced: {ok1}")

# 2. Update lines 5030-5210 in style.css
old_card_css = '''.sattvic-book-grid,
.shambhala-book-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
}

.sattvic-book-card,
.shambhala-book-card {
    background: #FFFFFF;
    border-radius: 14px;
    border: 1px solid rgba(44, 30, 20, 0.08);
    box-shadow: 0 4px 18px rgba(44, 30, 20, 0.05);
    padding: 1.4rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    position: relative;
}

.sattvic-book-card:hover,
.shambhala-book-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 32px rgba(44, 30, 20, 0.12);
    border-color: rgba(197, 160, 89, 0.4);
}

.s-book-cover-wrap {
    position: relative;
    text-align: center;
    margin-bottom: 1.2rem;
    background: #FDFBF7;
    padding: 0;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.s-book-badge {
    display: none !important;
}

.s-book-cover-img {
    width: 100%;
    aspect-ratio: 3 / 4;
    object-fit: cover;
    border-radius: 10px;
    box-shadow: none;
    transition: transform 0.35s ease;
    display: block;
}

.sattvic-book-card:hover .s-book-cover-img,
.shambhala-book-card:hover .s-book-cover-img {
    transform: scale(1.03);
}

.s-book-cat-tag {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--clr-gold-dark);
    margin-bottom: 0.35rem;
}

.s-book-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 1.2rem;
    font-weight: 700;
    line-height: 1.35;
    color: var(--clr-primary);
    margin-bottom: 0.4rem;
}

.s-book-title a {
    color: inherit;
    text-decoration: none;
    transition: color 0.2s;
}

.s-book-title a:hover {
    color: var(--clr-gold-dark);
}

.s-book-author {
    font-size: 0.88rem;
    color: var(--clr-text-muted);
    margin-bottom: 0.8rem;
}

.s-book-formats {
    font-size: 0.75rem;
    color: var(--clr-text-light);
    margin-bottom: 0.6rem;
}

.s-book-price-row {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    margin-bottom: 1.2rem;
    padding-top: 0.6rem;
    border-top: 1px dashed rgba(44, 30, 20, 0.1);
}

.s-book-price {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--clr-primary);
    font-family: 'Playfair Display', Georgia, serif;
}

.s-book-stock {
    font-size: 0.75rem;
    color: var(--clr-gold-dark, #9B7732);
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.3rem;
}

.s-book-actions {
    display: flex;
    gap: 0.6rem;
    align-items: center;
}

.s-btn-add {
    flex: 1;
    padding: 0.65rem 0.75rem;
    font-size: 0.84rem;
    font-weight: 700;
    letter-spacing: 0.3px;
    background: var(--clr-gold) !important;
    color: #FFFFFF !important;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: var(--transition);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.4rem;
    white-space: nowrap;
    box-shadow: 0 4px 12px rgba(197, 160, 89, 0.25);
}

.s-btn-add:hover {
    background: var(--clr-gold-dark) !important;
    color: #FFFFFF !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(197, 160, 89, 0.38);
}

.s-btn-details {
    flex: 0 0 38px;
    width: 38px;
    height: 38px;
    padding: 0;
    font-size: 0.92rem;
    border: 1.5px solid rgba(44, 30, 20, 0.2);
    border-radius: 6px;
    color: var(--clr-primary);
    text-decoration: none;
    transition: var(--transition);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.s-btn-details:hover {
    border-color: var(--clr-primary);
    background: var(--clr-primary);
    color: #FFFFFF;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(44, 30, 20, 0.15);
}'''

new_card_css = '''.sattvic-book-grid,
.shambhala-book-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.8rem;
}

.sattvic-book-card,
.shambhala-book-card {
    background: #FFFFFF;
    border-radius: 12px;
    border: 1px solid rgba(44, 30, 20, 0.08);
    box-shadow: 0 4px 18px rgba(44, 30, 20, 0.05);
    padding: 1.25rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    position: relative;
}

.sattvic-book-card:hover,
.shambhala-book-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 14px 32px rgba(44, 30, 20, 0.12);
    border-color: rgba(197, 160, 89, 0.45);
}

.s-book-top {
    display: flex;
    flex-direction: column;
}

.s-book-cover-wrap {
    position: relative;
    text-align: center;
    margin-bottom: 0.95rem;
    background: #FAF7F2;
    padding: 0;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 3px 12px rgba(44, 30, 20, 0.07);
    border: 1px solid rgba(44, 30, 20, 0.06);
}

.s-book-badge {
    display: none !important;
}

.s-book-cover-img {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: none;
    transition: transform 0.35s ease;
    display: block;
}

.sattvic-book-card:hover .s-book-cover-img,
.shambhala-book-card:hover .s-book-cover-img {
    transform: scale(1.03);
}

.s-book-cat-tag {
    display: none !important;
}

.s-book-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 1.12rem;
    font-weight: 700;
    line-height: 1.35;
    color: #2C1E14;
    margin-bottom: 0.3rem;
    min-height: 2.8rem;
}

.s-book-title a {
    color: #2C1E14;
    text-decoration: none;
    transition: color 0.2s;
}

.s-book-title a:hover {
    color: #A67C28;
}

.s-book-author {
    font-size: 0.85rem;
    color: #776B63;
    margin-bottom: 0.45rem;
    font-weight: 500;
}

.s-book-tagline {
    font-size: 0.82rem;
    color: #8C7B70;
    line-height: 1.45;
    margin-bottom: 0.9rem;
    min-height: 2.5rem;
}

.s-book-formats {
    display: none !important;
}

.s-book-bottom {
    margin-top: auto;
}

.s-book-price-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.85rem;
    padding-top: 0.75rem;
    border-top: 1px dashed rgba(44, 30, 20, 0.12);
}

.s-book-price {
    font-size: 1.25rem;
    font-weight: 700;
    color: #2C1E14;
    font-family: 'Playfair Display', Georgia, serif;
}

.s-book-stock {
    font-size: 0.8rem;
    color: #555555;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
}

.s-book-stock i {
    color: #28A745;
    font-size: 0.55rem;
}

.s-book-actions {
    display: flex;
    gap: 0.6rem;
    align-items: center;
}

.s-btn-add {
    width: 100%;
    padding: 0.72rem 1rem;
    font-size: 0.88rem;
    font-weight: 700;
    letter-spacing: 0.3px;
    background: #E0C079 !important;
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    color: #2C1E14 !important;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.25s ease;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.45rem;
    white-space: nowrap;
    box-shadow: 0 3px 10px rgba(197, 160, 89, 0.25);
    text-decoration: none;
}

.s-btn-add:hover {
    background: linear-gradient(135deg, #D4AF37 0%, #C5A059 100%) !important;
    color: #1A0F07 !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(197, 160, 89, 0.38);
}

.s-btn-details {
    display: none !important;
}

/* Rounded Pill Browse Button below Book Shelf (Matches Attachment Exactly) */
.browse-catalog-pill-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.6rem;
    padding: 0.85rem 2.4rem;
    font-size: 0.96rem;
    font-weight: 700;
    color: #2C1E14 !important;
    background: #E0C079 !important;
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    border: none;
    border-radius: 50px;
    text-decoration: none;
    box-shadow: 0 4px 16px rgba(197, 160, 89, 0.32);
    transition: all 0.25s ease;
}

.browse-catalog-pill-btn:hover {
    background: linear-gradient(135deg, #D4AF37 0%, #C5A059 100%) !important;
    color: #1A0F07 !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 22px rgba(197, 160, 89, 0.45);
}

/* Rounded Pill View Books Button below Explore Our Catalog */
.view-catalog-pill-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.65rem 2rem;
    font-size: 0.92rem;
    font-weight: 600;
    color: #2C1E14 !important;
    background: #FFFFFF !important;
    border: 1.5px solid rgba(44, 30, 20, 0.16) !important;
    border-radius: 50px;
    text-decoration: none;
    box-shadow: 0 2px 10px rgba(44, 30, 20, 0.05);
    transition: all 0.25s ease;
}

.view-catalog-pill-btn:hover {
    background: #FAF5EB !important;
    border-color: #C5A059 !important;
    color: #2C1E14 !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(197, 160, 89, 0.2);
}'''

css, ok2 = normalize_and_replace(css, old_card_css, new_card_css)
print(f"Card CSS replaced: {ok2}")

with open(r'd:\Sattvic Books\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css update complete!")

