# scratch/update_sri_lakshmi.py

# 1. Update index.html
with open(r'd:\Sattvic Books\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Book 1 and Book 2 in index.html
old_book_cards = '''                <!-- Book 1: Meghadootam: The Cloud Messenger -->
                <div class="sattvic-book-card">
                    <div class="s-book-top">
                        <div class="s-book-cover-wrap">
                            <a href="https://web.mytiny.us/sattvic-books/product/meghadootam-the-cloud-messenger/" title="View Details - Meghadootam: The Cloud Messenger" aria-label="View Details - Meghadootam: The Cloud Messenger">
                                <img src="assets/meghadootam-cover.png" alt="Meghadootam: The Cloud Messenger by Mahakavi Kalidasa" class="s-book-cover-img" loading="lazy">
                            </a>
                        </div>
                        <h3 class="s-book-title"><a href="https://web.mytiny.us/sattvic-books/product/meghadootam-the-cloud-messenger/">Meghadootam: The Cloud Messenger</a></h3>
                        <div class="s-book-author">By Mahakavi Kalidasa</div>
                        <p class="s-book-tagline">A bilingual picture book in English &amp; Sanskrit.</p>
                    </div>
                    <div class="s-book-bottom">
                        <div class="s-book-price-row">
                            <span class="s-book-price">$17.77</span>
                            <span class="s-book-stock"><i class="fa-solid fa-circle"></i> Available</span>
                        </div>
                        <a href="https://web.mytiny.us/sattvic-books/product/meghadootam-the-cloud-messenger/" class="s-btn-add" title="View Details for Meghadootam: The Cloud Messenger" aria-label="View Details for Meghadootam: The Cloud Messenger">
                            View Details <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>

                <!-- Book 2: Sri Lakshmi Chaturvimsati Namavali -->
                <div class="sattvic-book-card">
                    <div class="s-book-top">
                        <div class="s-book-cover-wrap">
                            <a href="https://web.mytiny.us/sattvic-books/product/sri-lak%e1%b9%a3mi-chaturvi%e1%b9%83sati-namavali/" title="View Details - Sri Lakshmi Chaturvimsati Namavali" aria-label="View Details - Sri Lakshmi Chaturvimsati Namavali">
                                <img src="assets/sri-lakshmi-chaturvimsati-namavali.png" alt="Sri Lakshmi Chaturvimsati Namavali" class="s-book-cover-img" loading="lazy">
                            </a>
                        </div>
                        <h3 class="s-book-title"><a href="https://web.mytiny.us/sattvic-books/product/sri-lak%e1%b9%a3mi-chaturvi%e1%b9%83sati-namavali/">Sri Lakshmi Chaturvimsati Namavali</a></h3>
                        <div class="s-book-author">By Dr. Rani Iyer</div>
                        <p class="s-book-tagline">24 sacred names of Goddess Lakshmi.</p>
                    </div>
                    <div class="s-book-bottom">
                        <div class="s-book-price-row">
                            <span class="s-book-price">$11.99</span>
                            <span class="s-book-stock"><i class="fa-solid fa-circle"></i> Available</span>
                        </div>
                        <a href="https://web.mytiny.us/sattvic-books/product/sri-lak%e1%b9%a3mi-chaturvi%e1%b9%83sati-namavali/" class="s-btn-add" title="View Details for Sri Lakshmi Chaturvimsati Namavali" aria-label="View Details for Sri Lakshmi Chaturvimsati Namavali">
                            View Details <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>'''

new_book_cards = '''                <!-- Book 1: Meghadootam: The Cloud Messenger -->
                <div class="sattvic-book-card">
                    <div class="s-book-top">
                        <div class="s-book-cover-wrap">
                            <a href="https://web.mytiny.us/sattvic-books/product/meghadootam-the-cloud-messenger/" title="View Details - Meghadootam: The Cloud Messenger" aria-label="View Details - Meghadootam: The Cloud Messenger">
                                <img src="assets/meghadootam-cover.png" alt="Meghadootam: The Cloud Messenger by Mahakavi Kalidasa" class="s-book-cover-img" loading="lazy">
                            </a>
                        </div>
                        <h3 class="s-book-title"><a href="https://web.mytiny.us/sattvic-books/product/meghadootam-the-cloud-messenger/">Meghadootam: The Cloud Messenger</a></h3>
                        <div class="s-book-author">By Mahakavi Kalidasa</div>
                        <p class="s-book-tagline">A bilingual picture book in English &amp; Sanskrit.</p>
                        <div class="s-book-isbn"><i class="fa-solid fa-barcode"></i> ISBN: 978-1-967672-23-3</div>
                    </div>
                    <div class="s-book-bottom">
                        <div class="s-book-price-row">
                            <span class="s-book-price">$17.77</span>
                            <span class="s-book-stock"><i class="fa-solid fa-circle"></i> Available</span>
                        </div>
                        <a href="https://web.mytiny.us/sattvic-books/product/meghadootam-the-cloud-messenger/" class="s-btn-add" title="View Details for Meghadootam: The Cloud Messenger" aria-label="View Details for Meghadootam: The Cloud Messenger">
                            View Details <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>

                <!-- Book 2: Sri Lakshmi Chaturvimsati Namavali -->
                <div class="sattvic-book-card">
                    <div class="s-book-top">
                        <div class="s-book-cover-wrap">
                            <a href="https://web.mytiny.us/sattvic-books/product/sri-lak%e1%b9%a3mi-chaturvi%e1%b9%83sati-namavali/" title="View Details - Sri Lakshmi Chaturvimsati Namavali" aria-label="View Details - Sri Lakshmi Chaturvimsati Namavali">
                                <img src="assets/sri-lakshmi-chaturvimsati-namavali.png" alt="Sri Lakshmi Chaturvimsati Namavali" class="s-book-cover-img" loading="lazy">
                            </a>
                        </div>
                        <h3 class="s-book-title"><a href="https://web.mytiny.us/sattvic-books/product/sri-lak%e1%b9%a3mi-chaturvi%e1%b9%83sati-namavali/">Sri Lakshmi Chaturvimsati Namavali</a></h3>
                        <div class="s-book-author">By Dr. Rani Iyer</div>
                        <p class="s-book-tagline">24 sacred names of Goddess Lakshmi.</p>
                        <div class="s-book-isbn"><i class="fa-solid fa-barcode"></i> ISBN: 978-1-967672-22-6</div>
                    </div>
                    <div class="s-book-bottom">
                        <div class="s-book-price-row">
                            <span class="s-book-price"><span class="price-val">$0.00</span> <span class="badge-free">Free</span></span>
                            <span class="s-book-stock"><i class="fa-solid fa-circle"></i> Available</span>
                        </div>
                        <a href="https://web.mytiny.us/sattvic-books/product/sri-lak%e1%b9%a3mi-chaturvi%e1%b9%83sati-namavali/" class="s-btn-add" title="View Details for Sri Lakshmi Chaturvimsati Namavali" aria-label="View Details for Sri Lakshmi Chaturvimsati Namavali">
                            View Details <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>'''

def normalize_and_replace(source, old_s, new_s):
    old_crlf = old_s.replace('\r\n', '\n').replace('\n', '\r\n')
    old_lf = old_s.replace('\r\n', '\n')
    if old_crlf in source:
        return source.replace(old_crlf, new_s.replace('\n', '\r\n')), True
    elif old_lf in source:
        return source.replace(old_lf, new_s), True
    return source, False

html, ok_idx = normalize_and_replace(html, old_book_cards, new_book_cards)
print(f"index.html book cards replaced: {ok_idx}")
with open(r'd:\Sattvic Books\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_addition = '''
/* Book ISBN & Free Badge Enhancements */
.s-book-isbn {
    font-size: 0.76rem !important;
    color: #7A6B60 !important;
    font-weight: 600 !important;
    margin-bottom: 0.6rem !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.35rem !important;
}

.s-book-isbn i {
    color: var(--clr-gold-dark, #A07C32) !important;
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
'''

if '.s-book-isbn' not in css:
    css = css + '\n' + css_addition.strip() + '\n'
    print("style.css: added .s-book-isbn and .badge-free")
    with open(r'd:\Sattvic Books\style.css', 'w', encoding='utf-8') as f:
        f.write(css)

# 3. Update press-kit.html lines 415-425
with open(r'd:\Sattvic Books\press-kit.html', 'r', encoding='utf-8') as f:
    press_html = f.read()

old_press_meta = '''                                    <span><i class="fa-solid fa-om" style="color: var(--clr-gold);"></i> 24 Sacred Names</span>
                                    <span>&bull;</span>
                                    <span style="font-weight: 700; color: var(--clr-primary);"><i class="fa-solid fa-tag" style="color: var(--clr-gold);"></i> Deepavali 2026 Edition</span>'''

new_press_meta = '''                                    <span><i class="fa-solid fa-om" style="color: var(--clr-gold);"></i> 24 Sacred Names</span>
                                    <span>&bull;</span>
                                    <span><i class="fa-solid fa-barcode" style="color: var(--clr-gold);"></i> ISBN: 978-1-967672-22-6</span>
                                    <span>&bull;</span>
                                    <span style="font-weight: 700; color: var(--clr-primary);"><i class="fa-solid fa-tag" style="color: var(--clr-gold);"></i> Free ($0.00) &bull; Deepavali 2026 Edition</span>'''

press_html, ok_pr = normalize_and_replace(press_html, old_press_meta, new_press_meta)
print(f"press-kit.html updated: {ok_pr}")
with open(r'd:\Sattvic Books\press-kit.html', 'w', encoding='utf-8') as f:
    f.write(press_html)

# 4. Update reading-partners.html
with open(r'd:\Sattvic Books\reading-partners.html', 'r', encoding='utf-8') as f:
    reading_html = f.read()

old_read_meta = '''                                    <span class="custom-resource-meta-highlight">
                                        <i class="fa-solid fa-tag"></i> Price: $11.99 &bull; Deepavali 2026 Edition
                                    </span>'''

new_read_meta = '''                                    <span class="custom-resource-meta-highlight">
                                        <i class="fa-solid fa-barcode"></i> ISBN: 978-1-967672-22-6 &bull; <i class="fa-solid fa-tag"></i> Price: Free ($0.00) &bull; Deepavali 2026 Edition
                                    </span>'''

reading_html, ok_rd = normalize_and_replace(reading_html, old_read_meta, new_read_meta)
print(f"reading-partners.html updated: {ok_rd}")
with open(r'd:\Sattvic Books\reading-partners.html', 'w', encoding='utf-8') as f:
    f.write(reading_html)

# 5. Update press-release-diwali-launch.html
with open(r'd:\Sattvic Books\press-release-diwali-launch.html', 'r', encoding='utf-8') as f:
    pr_diwali = f.read()

old_pr_diwali = 'Chants &amp; Meditations &bull; $11.99'
new_pr_diwali = 'Chants &amp; Meditations &bull; Free ($0.00) &bull; ISBN: 978-1-967672-22-6'

if old_pr_diwali in pr_diwali:
    pr_diwali = pr_diwali.replace(old_pr_diwali, new_pr_diwali)
    print("press-release-diwali-launch.html updated: True")
    with open(r'd:\Sattvic Books\press-release-diwali-launch.html', 'w', encoding='utf-8') as f:
        f.write(pr_diwali)
else:
    print("press-release-diwali-launch.html target not found")

print("All Sri Lakshmi updates completed!")

