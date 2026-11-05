import re

# ==========================================
# 1. UPDATE press-kit.html
# ==========================================
with open("D:/Sattvic Books/press-kit.html", "r", encoding="utf-8") as f:
    pk = f.read()

# Section 3: At A Glance
old_pk_sec3 = """        <!-- Section 3: Brand Information / At A Glance -->
        <section class="section-padding" style="background-color: #FFFFFF;">
            <div class="container" style="max-width: 960px;">
                <div class="text-center fade-in-up" style="margin-bottom: 2rem;">
                    <span class="eyebrow text-gold">At A Glance</span>
                    <h2
                        style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.3rem; color: var(--clr-primary);">
                        Brand Information</h2>
                </div>

                <div class="brand-info-grid fade-in-up">
                    <div class="brand-info-item">
                        <span class="info-label">Brand</span>
                        <span class="info-val">Sattvic Books</span>
                    </div>
                    <div class="brand-info-item">
                        <span class="info-label">Parent Organization</span>
                        <span class="info-val">The Sattvic Method Company</span>
                    </div>
                    <div class="brand-info-item">
                        <span class="info-label">Founder &amp; Author</span>
                        <span class="info-val">Dr. Rani Iyer</span>
                    </div>
                    <div class="brand-info-item">
                        <span class="info-label">Focus</span>
                        <span class="info-val">Literature for Conscious Living</span>
                    </div>
                    <div class="brand-info-item">
                        <span class="info-label">Inauguration</span>
                        <span class="info-val">Diwali 2026 (November 9, 2026)</span>
                    </div>
                    <div class="brand-info-item">
                        <span class="info-label">Headquarters</span>
                        <span class="info-val">India &amp; USA</span>
                    </div>
                </div>
            </div>
        </section>"""

new_pk_sec3 = """        <!-- Section 3: Brand Information / At A Glance (Signature Dark Mode Design) -->
        <section class="section-padding bg-dark" style="background-color: #322214 !important; background: linear-gradient(135deg, #322214 0%, #20150D 100%) !important; color: #FFFFFF !important; border-top: 1px solid rgba(215, 179, 71, 0.28); border-bottom: 1px solid rgba(215, 179, 71, 0.28);">
            <div class="container" style="max-width: 960px;">
                <div class="text-center fade-in-up" style="margin-bottom: 2.5rem;">
                    <span class="eyebrow text-gold" style="color: #D7B347 !important; letter-spacing: 2.4px; font-weight: 700; text-transform: uppercase; font-size: 0.88rem; display: block; margin-bottom: 0.6rem;">At A Glance</span>
                    <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.4rem; color: #FFFFFF !important; margin: 0; font-weight: 700;">Brand Information</h2>
                </div>

                <div class="brand-info-grid fade-in-up">
                    <div class="brand-info-item" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 12px; padding: 1.4rem 1.6rem; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);">
                        <span class="info-label" style="color: #D7B347 !important; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.8rem; display: block; margin-bottom: 0.4rem;">Brand</span>
                        <span class="info-val" style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.18rem; font-weight: 700;">Sattvic Books</span>
                    </div>
                    <div class="brand-info-item" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 12px; padding: 1.4rem 1.6rem; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);">
                        <span class="info-label" style="color: #D7B347 !important; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.8rem; display: block; margin-bottom: 0.4rem;">Parent Organization</span>
                        <span class="info-val" style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.18rem; font-weight: 700;">The Sattvic Method Company</span>
                    </div>
                    <div class="brand-info-item" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 12px; padding: 1.4rem 1.6rem; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);">
                        <span class="info-label" style="color: #D7B347 !important; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.8rem; display: block; margin-bottom: 0.4rem;">Founder &amp; Author</span>
                        <span class="info-val" style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.18rem; font-weight: 700;">Dr. Rani Iyer</span>
                    </div>
                    <div class="brand-info-item" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 12px; padding: 1.4rem 1.6rem; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);">
                        <span class="info-label" style="color: #D7B347 !important; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.8rem; display: block; margin-bottom: 0.4rem;">Focus</span>
                        <span class="info-val" style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.18rem; font-weight: 700;">Literature for Conscious Living</span>
                    </div>
                    <div class="brand-info-item" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 12px; padding: 1.4rem 1.6rem; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);">
                        <span class="info-label" style="color: #D7B347 !important; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.8rem; display: block; margin-bottom: 0.4rem;">Inauguration</span>
                        <span class="info-val" style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.18rem; font-weight: 700;">Diwali 2026 (November 9, 2026)</span>
                    </div>
                    <div class="brand-info-item" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 12px; padding: 1.4rem 1.6rem; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);">
                        <span class="info-label" style="color: #D7B347 !important; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.8rem; display: block; margin-bottom: 0.4rem;">Headquarters</span>
                        <span class="info-val" style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.18rem; font-weight: 700;">India &amp; USA</span>
                    </div>
                </div>
            </div>
        </section>"""

if old_pk_sec3 in pk:
    pk = pk.replace(old_pk_sec3, new_pk_sec3)
    print("Updated press-kit.html Section 3 (LF)")
elif old_pk_sec3.replace("\n", "\r\n") in pk:
    pk = pk.replace(old_pk_sec3.replace("\n", "\r\n"), new_pk_sec3.replace("\n", "\r\n"))
    print("Updated press-kit.html Section 3 (CRLF)")
else:
    print("Warning: old_pk_sec3 not matched in press-kit.html")

# Section 8: Compliance & Attribution
old_pk_sec8 = """        <!-- Section 8: Compliance & Attribution -->
        <section class="section-padding"
            style="background-color: #FAF6EE; border-top: 1px solid rgba(44, 30, 20, 0.06); border-bottom: 1px solid rgba(44, 30, 20, 0.06);">
            <div class="container" style="max-width: 900px;">
                <div class="text-center fade-in-up" style="margin-bottom: 1.8rem;">
                    <span class="eyebrow text-gold">Compliance &amp; Attribution</span>
                    <h2
                        style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.3rem; color: var(--clr-primary);">
                        Media Usage Guidelines</h2>
                </div>
                <div class="fade-in-up"
                    style="background: #FFFFFF; border: 1px solid rgba(197, 160, 89, 0.3); border-radius: 12px; padding: 2.4rem; box-shadow: 0 4px 18px rgba(44, 30, 20, 0.04);">
                    <p
                        style="font-size: 1.08rem; line-height: 1.8; color: var(--clr-text-main); margin-bottom: 1.2rem;">
                        The Sattvic Books name, logo, photographs, and publication images may be used for legitimate
                        editorial, review, and media coverage purposes.
                    </p>
                    <p style="font-size: 1.05rem; line-height: 1.8; color: var(--clr-text-main); margin-bottom: 0;">
                        We request that any coverage include attribution to <strong
                            style="color: var(--clr-primary);">Sattvic Books</strong> and a reference to our official
                        website (<strong style="color: var(--clr-primary);">sattvicbooks.com</strong>).
                    </p>
                </div>
            </div>
        </section>"""

new_pk_sec8 = """        <!-- Section 8: Compliance & Attribution (Signature Dark Mode Design) -->
        <section class="section-padding bg-dark"
            style="background-color: #322214 !important; background: linear-gradient(135deg, #322214 0%, #20150D 100%) !important; color: #FFFFFF !important; border-top: 1px solid rgba(215, 179, 71, 0.28); border-bottom: 1px solid rgba(215, 179, 71, 0.28);">
            <div class="container" style="max-width: 900px;">
                <div class="text-center fade-in-up" style="margin-bottom: 2rem;">
                    <span class="eyebrow text-gold" style="color: #D7B347 !important; letter-spacing: 2.4px; font-weight: 700; text-transform: uppercase; font-size: 0.88rem; display: block; margin-bottom: 0.6rem;">Compliance &amp; Attribution</span>
                    <h2
                        style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.4rem; color: #FFFFFF !important; margin: 0; font-weight: 700;">
                        Media Usage Guidelines</h2>
                </div>
                <div class="dark-feature-card fade-in-up"
                    style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.4) !important; border-radius: 14px; padding: 2.6rem; box-shadow: 0 12px 35px rgba(0, 0, 0, 0.35);">
                    <p
                        style="font-size: 1.12rem; line-height: 1.85; color: rgba(255, 255, 255, 0.95) !important; margin-bottom: 1.2rem;">
                        The Sattvic Books name, logo, photographs, and publication images may be used for legitimate
                        editorial, review, and media coverage purposes.
                    </p>
                    <p style="font-size: 1.08rem; line-height: 1.85; color: rgba(255, 255, 255, 0.9) !important; margin-bottom: 0;">
                        We request that any coverage include attribution to <strong
                            style="color: #D7B347 !important; font-weight: 700;">Sattvic Books</strong> and a reference to our official
                        website (<strong style="color: #D7B347 !important; font-weight: 700;">sattvicbooks.com</strong>).
                    </p>
                </div>
            </div>
        </section>"""

if old_pk_sec8 in pk:
    pk = pk.replace(old_pk_sec8, new_pk_sec8)
    print("Updated press-kit.html Section 8 (LF)")
elif old_pk_sec8.replace("\n", "\r\n") in pk:
    pk = pk.replace(old_pk_sec8.replace("\n", "\r\n"), new_pk_sec8.replace("\n", "\r\n"))
    print("Updated press-kit.html Section 8 (CRLF)")
else:
    print("Warning: old_pk_sec8 not matched in press-kit.html")

with open("D:/Sattvic Books/press-kit.html", "w", encoding="utf-8") as f:
    f.write(pk)


# ==========================================
# 2. UPDATE reading-partners.html
# ==========================================
with open("D:/Sattvic Books/reading-partners.html", "r", encoding="utf-8") as f:
    rp = f.read()

# Section 2: Collaborative Paths
old_rp_sec2 = """        <!-- Section 2: Collaborative Paths (Our Reading Partnerships) -->
        <section class="section-padding" style="background-color: #FAF6EE; border-top: 1px solid rgba(44, 30, 20, 0.06); border-bottom: 1px solid rgba(44, 30, 20, 0.06);">
            <div class="container" style="max-width: 1040px;">
                <div class="text-center fade-in-up" style="margin-bottom: 2.5rem;">
                    <span class="eyebrow text-gold">Collaborative Paths</span>
                    <h2
                        style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.3rem; color: var(--clr-primary);">
                        Our Reading Partnerships</h2>
                </div>

                <div class="partnerships-showcase-grid fade-in-up">

                    <!-- 1. For Teachers & Schools -->
                    <div class="partner-showcase-card">
                        <div class="partner-icon-circle"><i class="fa-solid fa-chalkboard-user"></i></div>
                        <h3>For Teachers &amp; Schools</h3>
                        <p>Bring thoughtfully selected books into classroom learning through educational resources and
                            classroom licensing arrangements.</p>
                    </div>

                    <!-- 2. For Libraries -->
                    <div class="partner-showcase-card">
                        <div class="partner-icon-circle"><i class="fa-solid fa-book-open-reader"></i></div>
                        <h3>For Libraries</h3>
                        <p>Curated titles that enrich community collections with wholesome literature for readers of
                            all ages.</p>
                    </div>

                    <!-- 3. For Book Clubs -->
                    <div class="partner-showcase-card">
                        <div class="partner-icon-circle"><i class="fa-solid fa-people-roof"></i></div>
                        <h3>For Book Clubs</h3>
                        <p>Discussion guides, author access opportunities, and bulk purchase options for reading groups.
                        </p>
                    </div>

                    <!-- 4. For Community Initiatives -->
                    <div class="partner-showcase-card">
                        <div class="partner-icon-circle"><i class="fa-solid fa-hands-holding-child"></i></div>
                        <h3>For Community Initiatives</h3>
                        <p>Collaborative programs supporting literacy drives, cultural events, and community-led
                            learning.</p>
                    </div>

                </div>
            </div>
        </section>"""

new_rp_sec2 = """        <!-- Section 2: Collaborative Paths (Signature Dark Mode Design) -->
        <section class="section-padding bg-dark" style="background-color: #322214 !important; background: linear-gradient(135deg, #322214 0%, #20150D 100%) !important; color: #FFFFFF !important; border-top: 1px solid rgba(215, 179, 71, 0.28); border-bottom: 1px solid rgba(215, 179, 71, 0.28);">
            <div class="container" style="max-width: 1040px;">
                <div class="text-center fade-in-up" style="margin-bottom: 2.8rem;">
                    <span class="eyebrow text-gold" style="color: #D7B347 !important; letter-spacing: 2.4px; font-weight: 700; text-transform: uppercase; font-size: 0.88rem; display: block; margin-bottom: 0.6rem;">Collaborative Paths</span>
                    <h2
                        style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.4rem; color: #FFFFFF !important; margin: 0; font-weight: 700;">
                        Our Reading Partnerships</h2>
                </div>

                <div class="partnerships-showcase-grid fade-in-up">

                    <!-- 1. For Teachers & Schools -->
                    <div class="partner-showcase-card" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 14px; padding: 2rem 1.6rem; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);">
                        <div class="partner-icon-circle" style="background: rgba(215, 179, 71, 0.18) !important; border: 1.5px solid rgba(215, 179, 71, 0.5) !important; color: #D7B347 !important;"><i class="fa-solid fa-chalkboard-user"></i></div>
                        <h3 style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.3rem; margin-top: 1rem; margin-bottom: 0.6rem; font-weight: 700;">For Teachers &amp; Schools</h3>
                        <p style="color: rgba(255, 255, 255, 0.9) !important; font-size: 0.98rem; line-height: 1.7; margin: 0;">Bring thoughtfully selected books into classroom learning through educational resources and
                            classroom licensing arrangements.</p>
                    </div>

                    <!-- 2. For Libraries -->
                    <div class="partner-showcase-card" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 14px; padding: 2rem 1.6rem; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);">
                        <div class="partner-icon-circle" style="background: rgba(215, 179, 71, 0.18) !important; border: 1.5px solid rgba(215, 179, 71, 0.5) !important; color: #D7B347 !important;"><i class="fa-solid fa-book-open-reader"></i></div>
                        <h3 style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.3rem; margin-top: 1rem; margin-bottom: 0.6rem; font-weight: 700;">For Libraries</h3>
                        <p style="color: rgba(255, 255, 255, 0.9) !important; font-size: 0.98rem; line-height: 1.7; margin: 0;">Curated titles that enrich community collections with wholesome literature for readers of
                            all ages.</p>
                    </div>

                    <!-- 3. For Book Clubs -->
                    <div class="partner-showcase-card" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 14px; padding: 2rem 1.6rem; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);">
                        <div class="partner-icon-circle" style="background: rgba(215, 179, 71, 0.18) !important; border: 1.5px solid rgba(215, 179, 71, 0.5) !important; color: #D7B347 !important;"><i class="fa-solid fa-people-roof"></i></div>
                        <h3 style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.3rem; margin-top: 1rem; margin-bottom: 0.6rem; font-weight: 700;">For Book Clubs</h3>
                        <p style="color: rgba(255, 255, 255, 0.9) !important; font-size: 0.98rem; line-height: 1.7; margin: 0;">Discussion guides, author access opportunities, and bulk purchase options for reading groups.
                        </p>
                    </div>

                    <!-- 4. For Community Initiatives -->
                    <div class="partner-showcase-card" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 14px; padding: 2rem 1.6rem; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);">
                        <div class="partner-icon-circle" style="background: rgba(215, 179, 71, 0.18) !important; border: 1.5px solid rgba(215, 179, 71, 0.5) !important; color: #D7B347 !important;"><i class="fa-solid fa-hands-holding-child"></i></div>
                        <h3 style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.3rem; margin-top: 1rem; margin-bottom: 0.6rem; font-weight: 700;">For Community Initiatives</h3>
                        <p style="color: rgba(255, 255, 255, 0.9) !important; font-size: 0.98rem; line-height: 1.7; margin: 0;">Collaborative programs supporting literacy drives, cultural events, and community-led
                            learning.</p>
                    </div>

                </div>
            </div>
        </section>"""

if old_rp_sec2 in rp:
    rp = rp.replace(old_rp_sec2, new_rp_sec2)
    print("Updated reading-partners.html Section 2 (LF)")
elif old_rp_sec2.replace("\n", "\r\n") in rp:
    rp = rp.replace(old_rp_sec2.replace("\n", "\r\n"), new_rp_sec2.replace("\n", "\r\n"))
    print("Updated reading-partners.html Section 2 (CRLF)")
else:
    print("Warning: old_rp_sec2 not matched in reading-partners.html")

# Section 4: Institutional Access
old_rp_sec4 = """        <!-- Section 4: Institutional Access (Enquiries & Categories) -->
        <section class="section-padding" style="background-color: #FAF6EE; border-top: 1px solid rgba(44, 30, 20, 0.06); border-bottom: 1px solid rgba(44, 30, 20, 0.06);">
            <div class="container" style="max-width: 900px;">
                <div class="text-center fade-in-up" style="margin-bottom: 2rem;">
                    <span class="eyebrow text-gold">Institutional Access</span>
                    <h2
                        style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.3rem; color: var(--clr-primary); margin-bottom: 0.8rem;">
                        Institutional &amp; Educational Enquiries</h2>
                    <p style="font-size: 1.15rem; color: var(--clr-text-main); font-weight: 600;">
                        Sattvic Books welcomes enquiries from:
                    </p>
                </div>

                <div class="categories-showcase-grid fade-in-up"
                    style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));">
                    <div class="category-showcase-card">
                        <div class="cat-icon"><i class="fa-solid fa-school"></i></div>
                        <h4>Schools and educational institutions</h4>
                    </div>
                    <div class="category-showcase-card">
                        <div class="cat-icon"><i class="fa-solid fa-book-bookmark"></i></div>
                        <h4>Libraries and cultural centres</h4>
                    </div>
                    <div class="category-showcase-card">
                        <div class="cat-icon"><i class="fa-solid fa-landmark"></i></div>
                        <h4>Independent bookstores</h4>
                    </div>
                    <div class="category-showcase-card">
                        <div class="cat-icon"><i class="fa-solid fa-building-columns"></i></div>
                        <h4>Organizations interested in custom publishing</h4>
                    </div>
                </div>

                <div class="text-center fade-in-up" style="margin-top: 2.5rem;">
                    <a href="contact.html#get-in-touch" class="btn btn-primary"
                        style="padding: 0.85rem 2.2rem; font-size: 1.05rem;">
                        <i class="fa-solid fa-paper-plane" style="margin-right: 0.5rem;"></i> Submit Institutional Enquiry
                    </a>
                </div>
            </div>
        </section>"""

new_rp_sec4 = """        <!-- Section 4: Institutional Access (Signature Dark Mode Design) -->
        <section class="section-padding bg-dark" style="background-color: #322214 !important; background: linear-gradient(135deg, #322214 0%, #20150D 100%) !important; color: #FFFFFF !important; border-top: 1px solid rgba(215, 179, 71, 0.28); border-bottom: 1px solid rgba(215, 179, 71, 0.28);">
            <div class="container" style="max-width: 900px;">
                <div class="text-center fade-in-up" style="margin-bottom: 2.2rem;">
                    <span class="eyebrow text-gold" style="color: #D7B347 !important; letter-spacing: 2.4px; font-weight: 700; text-transform: uppercase; font-size: 0.88rem; display: block; margin-bottom: 0.6rem;">Institutional Access</span>
                    <h2
                        style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.4rem; color: #FFFFFF !important; margin-bottom: 0.8rem; font-weight: 700;">
                        Institutional &amp; Educational Enquiries</h2>
                    <p style="font-size: 1.15rem; color: rgba(255, 255, 255, 0.95) !important; font-weight: 600;">
                        Sattvic Books welcomes enquiries from:
                    </p>
                </div>

                <div class="categories-showcase-grid fade-in-up"
                    style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));">
                    <div class="category-showcase-card" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 12px; padding: 1.4rem 1.6rem; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);">
                        <div class="cat-icon" style="background: rgba(215, 179, 71, 0.18) !important; border: 1.5px solid rgba(215, 179, 71, 0.5) !important; color: #D7B347 !important;"><i class="fa-solid fa-school"></i></div>
                        <h4 style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.05rem; font-weight: 600; margin: 0;">Schools and educational institutions</h4>
                    </div>
                    <div class="category-showcase-card" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 12px; padding: 1.4rem 1.6rem; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);">
                        <div class="cat-icon" style="background: rgba(215, 179, 71, 0.18) !important; border: 1.5px solid rgba(215, 179, 71, 0.5) !important; color: #D7B347 !important;"><i class="fa-solid fa-book-bookmark"></i></div>
                        <h4 style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.05rem; font-weight: 600; margin: 0;">Libraries and cultural centres</h4>
                    </div>
                    <div class="category-showcase-card" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 12px; padding: 1.4rem 1.6rem; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);">
                        <div class="cat-icon" style="background: rgba(215, 179, 71, 0.18) !important; border: 1.5px solid rgba(215, 179, 71, 0.5) !important; color: #D7B347 !important;"><i class="fa-solid fa-landmark"></i></div>
                        <h4 style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.05rem; font-weight: 600; margin: 0;">Independent bookstores</h4>
                    </div>
                    <div class="category-showcase-card" style="background: rgba(255, 255, 255, 0.05) !important; border: 1.5px solid rgba(215, 179, 71, 0.35) !important; border-radius: 12px; padding: 1.4rem 1.6rem; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);">
                        <div class="cat-icon" style="background: rgba(215, 179, 71, 0.18) !important; border: 1.5px solid rgba(215, 179, 71, 0.5) !important; color: #D7B347 !important;"><i class="fa-solid fa-building-columns"></i></div>
                        <h4 style="color: #FFFFFF !important; font-family: 'Playfair Display', Georgia, serif; font-size: 1.05rem; font-weight: 600; margin: 0;">Organizations interested in custom publishing</h4>
                    </div>
                </div>

                <div class="text-center fade-in-up" style="margin-top: 2.5rem;">
                    <a href="contact.html#get-in-touch" class="btn btn-primary"
                        style="padding: 0.85rem 2.2rem; font-size: 1.05rem;">
                        <i class="fa-solid fa-paper-plane" style="margin-right: 0.5rem;"></i> Submit Institutional Enquiry
                    </a>
                </div>
            </div>
        </section>"""

if old_rp_sec4 in rp:
    rp = rp.replace(old_rp_sec4, new_rp_sec4)
    print("Updated reading-partners.html Section 4 (LF)")
elif old_rp_sec4.replace("\n", "\r\n") in rp:
    rp = rp.replace(old_rp_sec4.replace("\n", "\r\n"), new_rp_sec4.replace("\n", "\r\n"))
    print("Updated reading-partners.html Section 4 (CRLF)")
else:
    print("Warning: old_rp_sec4 not matched in reading-partners.html")

with open("D:/Sattvic Books/reading-partners.html", "w", encoding="utf-8") as f:
    f.write(rp)


# ==========================================
# 3. UPDATE style.css WITH BULLETPROOF DARK SECTION STYLES
# ==========================================
with open("D:/Sattvic Books/style.css", "r", encoding="utf-8") as f:
    css = f.read()

dark_section_css = """
/* ==========================================================================
   EXCLUSIVE DARK MODE SECTION COMPONENT STYLING (press-kit & reading-partners)
   ========================================================================== */
.bg-dark .brand-info-item,
section.bg-dark .brand-info-item {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1.5px solid rgba(215, 179, 71, 0.35) !important;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35) !important;
}

.bg-dark .brand-info-item .info-label,
section.bg-dark .brand-info-item .info-label {
    color: #D7B347 !important;
}

.bg-dark .brand-info-item .info-val,
section.bg-dark .brand-info-item .info-val {
    color: #FFFFFF !important;
}

.bg-dark .partner-showcase-card,
section.bg-dark .partner-showcase-card {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1.5px solid rgba(215, 179, 71, 0.35) !important;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3) !important;
}

.bg-dark .partner-showcase-card h3,
section.bg-dark .partner-showcase-card h3 {
    color: #FFFFFF !important;
}

.bg-dark .partner-showcase-card p,
section.bg-dark .partner-showcase-card p {
    color: rgba(255, 255, 255, 0.9) !important;
}

.bg-dark .partner-icon-circle,
section.bg-dark .partner-icon-circle {
    background: rgba(215, 179, 71, 0.18) !important;
    border: 1.5px solid rgba(215, 179, 71, 0.5) !important;
    color: #D7B347 !important;
}

.bg-dark .category-showcase-card,
section.bg-dark .category-showcase-card {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1.5px solid rgba(215, 179, 71, 0.35) !important;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3) !important;
}

.bg-dark .category-showcase-card h4,
section.bg-dark .category-showcase-card h4 {
    color: #FFFFFF !important;
}

.bg-dark .category-showcase-card .cat-icon,
section.bg-dark .category-showcase-card .cat-icon {
    background: rgba(215, 179, 71, 0.18) !important;
    border: 1.5px solid rgba(215, 179, 71, 0.5) !important;
    color: #D7B347 !important;
}
"""

if "EXCLUSIVE DARK MODE SECTION COMPONENT STYLING" not in css:
    css += dark_section_css
    with open("D:/Sattvic Books/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Added dark_section_css to style.css!")
else:
    print("dark_section_css already in style.css")

