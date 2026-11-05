with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update lines 235-330
old_btn_primary = """/* Primary Button: Solid Gold -> Rich Deep Gold Hover */
.btn-primary {
    background-color: var(--clr-gold) !important;
    color: #FFFFFF !important;
    border-color: var(--clr-gold) !important;
    box-shadow: 0 4px 15px rgba(197, 160, 89, 0.28) !important;
}

.btn-primary:hover {
    background-color: var(--clr-gold-dark) !important;
    border-color: var(--clr-gold-dark) !important;
    color: #FFFFFF !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(197, 160, 89, 0.42) !important;
}

.btn-primary:active {
    transform: translateY(0) !important;
    box-shadow: 0 2px 8px rgba(197, 160, 89, 0.25) !important;
}

/* Secondary Button / Gold / Primary-Gold */
.btn-secondary,
.btn-gold,
.btn-primary-gold {
    background-color: var(--clr-gold) !important;
    color: var(--clr-primary) !important;
    border-color: var(--clr-gold) !important;
    box-shadow: 0 4px 15px rgba(197, 160, 89, 0.22) !important;
}

.btn-secondary:hover,
.btn-gold:hover,
.btn-primary-gold:hover {
    background-color: var(--clr-primary) !important;
    border-color: var(--clr-primary) !important;
    color: #FFFFFF !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(44, 30, 20, 0.3) !important;
}

.btn-secondary:active,
.btn-gold:active,
.btn-primary-gold:active {
    transform: translateY(0) !important;
}

/* Outline Button */
.btn-outline {
    background-color: #FFFFFF !important;
    color: var(--clr-primary) !important;
    border: 1.5px solid var(--clr-gold) !important;
    box-shadow: 0 4px 14px rgba(197, 160, 89, 0.12) !important;
}

.btn-outline:hover {
    background-color: var(--clr-gold) !important;
    border-color: var(--clr-gold) !important;
    color: #FFFFFF !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(197, 160, 89, 0.35) !important;
}

.btn-outline:active {
    transform: translateY(0) !important;
}

/* Outline Gold Button (for dark backgrounds or luxury cards) */
.btn-outline-gold {
    background-color: rgba(255, 255, 255, 0.88) !important;
    color: var(--clr-gold-dark) !important;
    border: 2px solid var(--clr-gold) !important;
    box-shadow: 0 4px 14px rgba(197, 160, 89, 0.12) !important;
}

.btn-outline-gold:hover {
    background-color: var(--clr-gold) !important;
    border-color: var(--clr-gold) !important;
    color: var(--clr-primary) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(197, 160, 89, 0.35) !important;
}

.btn-outline-gold:active {
    transform: translateY(0) !important;
}"""

new_btn_primary = """/* Primary & Secondary Buttons: Unified Signature Luxury Gold with Deep Espresso Text */
.btn-primary,
.btn-secondary,
.btn-gold,
.btn-primary-gold,
.btn-outline,
.btn-outline-gold {
    background: #DFBF77 !important;
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    color: #2C1E14 !important;
    border: none !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 15px rgba(197, 160, 89, 0.3) !important;
    transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}

.btn-primary:hover,
.btn-secondary:hover,
.btn-gold:hover,
.btn-primary-gold:hover,
.btn-outline:hover,
.btn-outline-gold:hover {
    background: linear-gradient(135deg, #D4AF37 0%, #C5A059 100%) !important;
    color: #1A0F07 !important;
    border: none !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 22px rgba(197, 160, 89, 0.45) !important;
}

.btn-primary:active,
.btn-secondary:active,
.btn-gold:active,
.btn-primary-gold:active,
.btn-outline:active,
.btn-outline-gold:active {
    transform: translateY(0) !important;
    box-shadow: 0 2px 8px rgba(197, 160, 89, 0.25) !important;
}"""

# 2. Update lines 347-378
old_ecommerce_btns = """/* Unified E-Commerce Add To Cart Buttons */
.s-btn-add,
.btn-add-cart,
.bd-add-btn {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    gap: 0.45rem !important;
    font-family: var(--font-body) !important;
    font-size: 0.88rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    background-color: var(--clr-gold) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.7rem 1.2rem !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    outline: none !important;
    box-shadow: 0 3px 10px rgba(197, 160, 89, 0.28) !important;
}

.s-btn-add:hover,
.btn-add-cart:hover,
.bd-add-btn:hover {
    background-color: var(--clr-gold-dark) !important;
    border-color: var(--clr-gold-dark) !important;
    color: #FFFFFF !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 16px rgba(197, 160, 89, 0.4) !important;
}"""

new_ecommerce_btns = """/* Unified E-Commerce Add To Cart Buttons */
.s-btn-add,
.btn-add-cart,
.bd-add-btn {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    gap: 0.45rem !important;
    font-family: var(--font-body) !important;
    font-size: 0.88rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    color: #2C1E14 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.7rem 1.2rem !important;
    cursor: pointer !important;
    transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    outline: none !important;
    box-shadow: 0 4px 15px rgba(197, 160, 89, 0.3) !important;
}

.s-btn-add:hover,
.btn-add-cart:hover,
.bd-add-btn:hover {
    background: linear-gradient(135deg, #D4AF37 0%, #C5A059 100%) !important;
    border: none !important;
    color: #1A0F07 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 22px rgba(197, 160, 89, 0.45) !important;
}"""

# 3. Update lines 504-515 (active filter pills)
old_filter_active = """.catalog-filter-btn.active,
.events-filter-pill.active,
.event-tab-btn.active,
.media-tab-btn.active,
.press-filter-btn.active,
.pod-filter-btn.active,
.bd-tab-btn.active {
    background: var(--clr-gold) !important;
    color: #FFFFFF !important;
    border-color: var(--clr-gold) !important;
    box-shadow: 0 4px 14px rgba(197, 160, 89, 0.35) !important;
}"""

new_filter_active = """.catalog-filter-btn.active,
.events-filter-pill.active,
.event-tab-btn.active,
.media-tab-btn.active,
.press-filter-btn.active,
.pod-filter-btn.active,
.bd-tab-btn.active {
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    color: #2C1E14 !important;
    border: none !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 14px rgba(197, 160, 89, 0.35) !important;
}"""

def replace_normalized(content, old, new):
    c_norm = content.replace('\r\n', '\n')
    o_norm = old.replace('\r\n', '\n')
    n_norm = new.replace('\r\n', '\n')
    if o_norm not in c_norm:
        print("COULD NOT FIND BLOCK:")
        print(o_norm[:100])
        return content, False
    return c_norm.replace(o_norm, n_norm), True

css_up, s1 = replace_normalized(css, old_btn_primary, new_btn_primary)
css_up, s2 = replace_normalized(css_up, old_ecommerce_btns, new_ecommerce_btns)
css_up, s3 = replace_normalized(css_up, old_filter_active, new_filter_active)

print(f"Replacements status: s1={s1}, s2={s2}, s3={s3}")

if s1 and s2 and s3:
    with open(r'd:\Sattvic Books\style.css', 'w', encoding='utf-8') as f:
        f.write(css_up)
    print("Updated style.css successfully!")
else:
    print("Error updating style.css")

