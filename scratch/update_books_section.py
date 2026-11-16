import re

# 1. Update index.html
with open(r'd:\Sattvic Books\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace View All Books in Featured Catalog with clean pill button
old_view_catalog = '''            <div class="text-center mt-4">
                <a href="https://sattvicbooks.com/shop/" class="btn btn-primary" style="padding: 0.9rem 2.2rem; font-size: 1rem;">
                    <i class="fa-solid fa-book-open" style="margin-right: 0.45rem;"></i> View All Books <i class="fa-solid fa-arrow-right" style="margin-left: 0.35rem;"></i>
                </a>
            </div>'''

new_view_catalog = '''            <div class="text-center mt-4">
                <a href="https://sattvicbooks.com/shop/" class="view-catalog-pill-btn" title="View Books">
                    View Books <i class="fa-solid fa-arrow-right"></i>
                </a>
            </div>'''

if old_view_catalog in html:
    html = html.replace(old_view_catalog, new_view_catalog)
    print("Replaced view-catalog button successfully")
else:
    print("Warning: old_view_catalog not found verbatim, checking regex...")
    pattern = re.compile(r'<div class="text-center mt-4">\s*<a href="https://web\.mytiny\.us/sattvic-books/shop/" class="btn btn-primary"[^>]*>.*?View All Books.*?</a>\s*</div>', re.DOTALL)
    html = pattern.sub(new_view_catalog, html, count=1)

# Now replace the book grid and browse button
old_books_grid_start = '<div class="sattvic-book-grid fade-in">'
old_books_grid_end = '    <!-- Why Buy from Sattvic Books? Section -->'

new_books_section_content = '''<div class="sattvic-book-grid fade-in">
                
                <!-- Book 1: Meghadootam: The Cloud Messenger -->
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
                </div>

                <!-- Book 3: The Garden Inside You -->
                <div class="sattvic-book-card">
                    <div class="s-book-top">
                        <div class="s-book-cover-wrap">
                            <a href="https://web.mytiny.us/sattvic-books/product/the-garden-inside-you/" title="View Details - The Garden Inside You" aria-label="View Details - The Garden Inside You">
                                <img src="assets/the-garden-inside-you.png" alt="The Garden Inside You by Dr. Rani Iyer" class="s-book-cover-img" loading="lazy">
                            </a>
                        </div>
                        <h3 class="s-book-title"><a href="https://web.mytiny.us/sattvic-books/product/the-garden-inside-you/">The Garden Inside You</a></h3>
                        <div class="s-book-author">By Dr. Rani Iyer</div>
                        <p class="s-book-tagline">Discover the magic, wisdom, and you.</p>
                    </div>
                    <div class="s-book-bottom">
                        <div class="s-book-price-row">
                            <span class="s-book-price">$11.97</span>
                            <span class="s-book-stock"><i class="fa-solid fa-circle"></i> Available</span>
                        </div>
                        <a href="https://web.mytiny.us/sattvic-books/product/the-garden-inside-you/" class="s-btn-add" title="View Details for The Garden Inside You" aria-label="View Details for The Garden Inside You">
                            View Details <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>

                <!-- Book 4: Gauri Ganesh (Spiral Edition) -->
                <div class="sattvic-book-card">
                    <div class="s-book-top">
                        <div class="s-book-cover-wrap">
                            <a href="https://web.mytiny.us/sattvic-books/product/gauri-ganesh-digital-kirtan-picture-book/" title="View Details - Gauri Ganesh (Spiral Edition)" aria-label="View Details - Gauri Ganesh (Spiral Edition)">
                                <img src="assets/gauri-ganesh.png" alt="Gauri Ganesh (Spiral Edition)" class="s-book-cover-img" loading="lazy">
                            </a>
                        </div>
                        <h3 class="s-book-title"><a href="https://web.mytiny.us/sattvic-books/product/gauri-ganesh-digital-kirtan-picture-book/">Gauri Ganesh (Spiral Edition)</a></h3>
                        <div class="s-book-author">By Dr. Rani Iyer</div>
                        <p class="s-book-tagline">A divine bonding tale for all ages.</p>
                    </div>
                    <div class="s-book-bottom">
                        <div class="s-book-price-row">
                            <span class="s-book-price">$11.99</span>
                            <span class="s-book-stock"><i class="fa-solid fa-circle"></i> Available</span>
                        </div>
                        <a href="https://web.mytiny.us/sattvic-books/product/gauri-ganesh-digital-kirtan-picture-book/" class="s-btn-add" title="View Details for Gauri Ganesh (Spiral Edition)" aria-label="View Details for Gaurianesh (Spiral Edition)">
                            View Details <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>

            </div>
            
            <div class="text-center mt-4">
                <a href="https://sattvicbooks.com/shop/" class="browse-catalog-pill-btn" title="Browse All Books &amp; Categories">
                    <i class="fa-solid fa-book-bookmark"></i> Browse All Books &amp; Categories
                </a>
            </div>
        </div>
    </section>

'''

# Extract and replace between old_books_grid_start and old_books_grid_end
idx1 = html.find(old_books_grid_start)
idx2 = html.find(old_books_grid_end)
if idx1 != -1 and idx2 != -1:
    html = html[:idx1] + new_books_section_content + html[idx2:]
    print("Replaced book shelf section in index.html successfully")
    with open(r'd:\Sattvic Books\index.html', 'w', encoding='utf-8') as f:
        f.write(html)
else:
    print(f"Error finding indices: idx1={idx1}, idx2={idx2}")

print("index.html update complete!")

