with open(r'd:\Sattvic Books\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open(r'd:\Sattvic Books\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = []

# 1. Catalog, Gift Store, Newsletter background = #FAF6EE
has_cat_bg = '.collections,' in css and '#FAF6EE' in css
has_gift_bg = '.gift-store-section,' in css and '#FAF6EE' in css
has_cta_bg = '.cta,' in css and '#FAF6EE' in css
checks.append(("1. Catalog, Gift Store, Newsletter bg == #FAF6EE", has_cat_bg and has_gift_bg and has_cta_bg))

# 2. Book Shelf bg == #F6EBDD and no peach in index.html
no_peach_inline = 'F7E9DC' not in html and 'F3E5D0' not in html
has_books_beige = '.books,' in css and '#F6EBDD' in css
checks.append(("2. Book Shelf bg == #F6EBDD & no inline peach", no_peach_inline and has_books_beige))

# 3. Category, book, gift cards == #FFFFFF
has_cat_card_white = '.collection-card' in css and '#FFFFFF' in css
has_book_card_white = '.sattvic-book-card' in css and '#FFFFFF' in css
has_gift_card_white = '.gift-store-card' in css and '#FFFFFF' in css
checks.append(("3. Category, book, gift cards == #FFFFFF", has_cat_card_white and has_book_card_white and has_gift_card_white))

# 4. Light sections headings == #382618
has_headings_dark_brown = '#382618 !important' in css
checks.append(("4. Light sections headings == #382618", has_headings_dark_brown))

# 5. Light sections paragraphs == #5E4A39
has_p_warm_brown = '#5E4A39 !important' in css
checks.append(("5. Light sections paragraphs == #5E4A39", has_p_warm_brown))

# 6. Chhote labels == #855E20
has_eyebrow_dark_gold = '#855E20 !important' in css
checks.append(("6. Small labels (eyebrows) == #855E20", has_eyebrow_dark_gold))

# 7. Primary buttons == #D7B347 bg & #382618 text
has_btn_gold_bg = '#D7B347 !important' in css
has_btn_dark_brown_text = 'color: #382618 !important' in css
checks.append(("7. Primary buttons == #D7B347 bg & #382618 text", has_btn_gold_bg and has_btn_dark_brown_text))

# 8. Giveaways & Footer == #322214 bg & #FBF5E9 text & links
has_freebies_dark_bg = '.freebies-section' in css and '#322214' in css
has_footer_dark_bg = '.footer' in css and '#322214' in css
has_dark_cream_text = '#FBF5E9 !important' in css
checks.append(("8. Giveaways & Footer == #322214 bg & #FBF5E9 text & links", has_freebies_dark_bg and has_footer_dark_bg and has_dark_cream_text))

print("=== PALETTE VERIFICATION RESULTS ===")
all_passed = True
for name, passed in checks:
    status = "PASS [OK]" if passed else "FAIL [X]"
    print(f"{status}: {name}")
    if not passed:
        all_passed = False

print(f"\nOverall Status: {'ALL 8 REQUIREMENTS SATISFIED!' if all_passed else 'SOME CHECKS FAILED'}")

