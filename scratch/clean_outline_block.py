with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_outline_block = """/* Outline Dark Button for Luxury Espresso Contrast */
.btn-outline-dark {
    background-color: transparent !important;
    color: var(--clr-primary) !important;
    border: 1.5px solid var(--clr-primary) !important;
    border-radius: var(--radius) !important;
    transition: var(--transition) !important;
}

.btn-outline-dark:hover {
    background-color: var(--clr-primary) !important;
    color: #FFFFFF !important;
    border-color: var(--clr-primary) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(44, 30, 20, 0.25) !important;
}

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
}"""

new_outline_block = """/* Unified Signature Buttons: Luxury Camel-Gold with Deep Espresso Text */
.btn-outline-dark,
.btn-outline,
.btn-primary,
.btn-gold,
.btn-primary-gold {
    background: #DFBF77 !important;
    background: linear-gradient(135deg, #E2C27E 0%, #D4AF37 100%) !important;
    color: #2C1E14 !important;
    border: none !important;
    font-weight: 700 !important;
    letter-spacing: 0.3px !important;
    box-shadow: 0 4px 15px rgba(197, 160, 89, 0.3) !important;
    transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}

.btn-outline-dark:hover,
.btn-outline:hover,
.btn-primary:hover,
.btn-gold:hover,
.btn-primary-gold:hover {
    background: linear-gradient(135deg, #D4AF37 0%, #C5A059 100%) !important;
    color: #1A0F07 !important;
    border: none !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 22px rgba(197, 160, 89, 0.45) !important;
}"""

c_norm = css.replace('\r\n', '\n')
o_norm = old_outline_block.replace('\r\n', '\n')
n_norm = new_outline_block.replace('\r\n', '\n')

if o_norm in c_norm:
    c_norm = c_norm.replace(o_norm, n_norm)
    with open(r'd:\Sattvic Books\style.css', 'w', encoding='utf-8') as f:
        f.write(c_norm)
    print("Successfully replaced outline block in style.css!")
else:
    print("Could not find outline block!")

