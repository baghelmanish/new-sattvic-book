document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Navigation Toggle
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('nav-links');
    const links = navLinks.querySelectorAll('a');

    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        const icon = hamburger.querySelector('i');
        if (navLinks.classList.contains('active')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-xmark');
        } else {
            icon.classList.remove('fa-xmark');
            icon.classList.add('fa-bars');
        }
    });

    // Close mobile menu when a link is clicked
    links.forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            const icon = hamburger.querySelector('i');
            icon.classList.remove('fa-xmark');
            icon.classList.add('fa-bars');
        });
    });

    // 2. Sticky Navbar on Scroll
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 3. Scroll Animations (Intersection Observer)
    const appearOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const appearOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('visible'); // was 'appear' — fixed to match CSS
                observer.unobserve(entry.target);
            }
        });
    }, appearOptions);

    const faders = document.querySelectorAll('.fade-in, .fade-in-up');
    faders.forEach(fader => {
        appearOnScroll.observe(fader);
    });
    // Safety: mark all visible after 800ms in case observer misses them
    setTimeout(() => {
        document.querySelectorAll('.fade-in, .fade-in-up').forEach(el => el.classList.add('visible'));
    }, 800);

    // Keyboard accessibility for hamburger menu
    if (hamburger) {
        hamburger.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                hamburger.click();
            }
        });
    }

    // 4. Form Submission Handling (Generic forms only, exclude specialized forms)
    const genericForms = document.querySelectorAll('form:not(#catalogForm):not(#catalogueForm):not(#contactForm)');
    genericForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = form.querySelector('button[type="submit"]') || form.querySelector('button');
            if (!btn) return;
            const originalText = btn.innerText;
            btn.innerText = 'Thank You!';
            btn.style.backgroundColor = '#C5A059'; // Gold color
            btn.style.borderColor = '#C5A059';
            btn.style.color = '#fff';
            
            setTimeout(() => {
                form.reset();
                btn.innerText = originalText;
                btn.style = '';
            }, 3000);
        });
    });

    // 5. Featured Books Slider (Swiper.js)
    const sliderContainer = document.querySelector('.books-slider');
    if (sliderContainer && typeof Swiper !== 'undefined') {
        const bookSlider = new Swiper('.books-slider', {
            slidesPerView: 1,
            spaceBetween: 20,
            loop: true,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            breakpoints: {
                640: {
                    slidesPerView: 2,
                    spaceBetween: 20,
                },
                992: {
                    slidesPerView: 3,
                    spaceBetween: 30,
                },
                1200: {
                    slidesPerView: 4,
                    spaceBetween: 30,
                }
            },
            autoplay: {
                delay: 4000,
                disableOnInteraction: false,
            }
        });
    }

    // 6. Cart Management Logic
    const CartManager = {
        items: JSON.parse(localStorage.getItem('sattvicCart')) || [],
        
        save() {
            localStorage.setItem('sattvicCart', JSON.stringify(this.items));
            this.updateBadge();
        },
        
        add(item) {
            // Check if already in cart
            const existing = this.items.find(i => i.id === item.id);
            if (!existing) {
                this.items.push(item);
                this.save();
                // Optional: Show a subtle toast or visual feedback here instead of just an alert
                alert(item.title + ' added to your cart!');
            } else {
                alert(item.title + ' is already in your cart.');
            }
        },
        
        remove(id) {
            this.items = this.items.filter(i => i.id !== id);
            this.save();
            this.renderCartPage();
        },
        
        updateBadge() {
            const badges = document.querySelectorAll('.cart-badge');
            badges.forEach(badge => {
                badge.innerText = this.items.length;
            });
        },
        
        renderCartPage() {
            const cartItemsList = document.getElementById('cartItemsList');
            const cartSubtotal = document.getElementById('cartSubtotal');
            const cartTotal = document.getElementById('cartTotal');
            const emptyMsg = document.getElementById('emptyCartMessage');
            const cartContainer = document.getElementById('cartContainer');
            
            if (!cartItemsList) return; // Not on cart page
            
            if (this.items.length === 0) {
                cartContainer.style.display = 'none';
                emptyMsg.style.display = 'block';
                return;
            }
            
            cartContainer.style.display = 'grid';
            emptyMsg.style.display = 'none';
            cartItemsList.innerHTML = '';
            
            let total = 0;
            
            this.items.forEach(item => {
                total += parseFloat(item.price);
                const div = document.createElement('div');
                // No fade-in class — items are added dynamically and must be visible immediately
                div.className = 'cart-item';
                div.style.cssText = 'display:grid;grid-template-columns:90px 1fr auto;gap:1.2rem;align-items:center;padding:1.2rem 1.5rem;background:#fff;border-radius:12px;margin-bottom:1rem;box-shadow:0 4px 20px rgba(44, 30, 20,0.06);border:1px solid rgba(44, 30, 20,0.07);';
                div.innerHTML = `
                    <img src="${item.image}" alt="${item.title}" style="width:80px;height:110px;object-fit:cover;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,0.12);">
                    <div>
                        <div style="font-size:0.72rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#C5A059;margin-bottom:0.3rem;">Sattvic Books</div>
                        <h4 style="font-family:'Playfair Display',serif;font-size:1.1rem;color:#2C1E14;margin-bottom:0.4rem;line-height:1.3;">${item.title}</h4>
                        <div style="font-size:0.85rem;color:#6A5A4D;margin-bottom:0.5rem;">Paperback &nbsp;|&nbsp; Print Edition</div>
                        <div style="font-size:1.2rem;font-weight:700;color:#C5A059;">$${item.price}</div>
                    </div>
                    <button onclick="window.removeFromCart('${item.id}')" title="Remove" style="background:none;border:none;cursor:pointer;color:#999;font-size:1.1rem;padding:0.4rem;border-radius:6px;transition:all 0.2s;" onmouseover="this.style.color='#e53e3e';this.style.background='rgba(229,62,62,0.08)'" onmouseout="this.style.color='#999';this.style.background='none'"><i class="fa-solid fa-trash-can"></i></button>
                `;
                cartItemsList.appendChild(div);
            });
            
            const formattedTotal = '$' + total.toFixed(2);
            cartSubtotal.innerText = formattedTotal;
            cartTotal.innerText = formattedTotal;
        }
    };

    // Expose remove function globally for inline onclick handlers
    window.removeFromCart = (id) => {
        CartManager.remove(id);
    };

    // Initialize badge on load
    CartManager.updateBadge();
    
    // Render cart if on cart page
    CartManager.renderCartPage();

    // 7. Add to Cart Button Listeners (Event Delegation for 100% Reliability)
    document.addEventListener('click', (e) => {
        const btn = e.target.closest('.btn-add-cart');
        if (btn) {
            e.preventDefault();
            const id = btn.getAttribute('data-id');
            const title = btn.getAttribute('data-title');
            const price = btn.getAttribute('data-price');
            const image = btn.getAttribute('data-image');
            
            CartManager.add({ id, title, price, image });
            
            // Visual button ripple feedback
            const originalHtml = btn.innerHTML;
            btn.innerHTML = '<i class="fa-solid fa-check"></i> Added!';
            btn.style.backgroundColor = '#B89047';
            btn.style.color = '#fff';
            setTimeout(() => {
                btn.innerHTML = originalHtml;
                btn.style.backgroundColor = '';
                btn.style.color = '';
            }, 1400);
        }
    });

    // 8. Checkout Modal Functionality (for cart.html)
    const checkoutBtn = document.getElementById('checkoutBtn');
    const checkoutModal = document.getElementById('checkoutModal');
    const closeCheckoutModal = document.getElementById('closeCheckoutModal');
    const notifyMeBtn = document.getElementById('notifyMeBtn');

    if (checkoutBtn && checkoutModal) {
        checkoutBtn.addEventListener('click', () => checkoutModal.classList.add('active'));
        closeCheckoutModal.addEventListener('click', () => checkoutModal.classList.remove('active'));
        
        checkoutModal.addEventListener('click', (e) => {
            if (e.target === checkoutModal) checkoutModal.classList.remove('active');
        });
        
        notifyMeBtn.addEventListener('click', () => checkoutModal.classList.remove('active'));
    }

    // 9. Press Releases Page Filtering & Modal Viewer
    const pressFilterBtns = document.querySelectorAll('.press-filter-btn');
    const pressCards = document.querySelectorAll('.press-card');
    const featuredPressBoxes = document.querySelectorAll('.featured-press-box');

    if (pressFilterBtns.length > 0) {
        pressFilterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                pressFilterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                const filter = btn.getAttribute('data-filter');
                
                // Filter featured boxes
                featuredPressBoxes.forEach(box => {
                    const category = box.getAttribute('data-category');
                    if (filter === 'all' || filter === category) {
                        box.style.display = '';
                    } else {
                        box.style.display = 'none';
                    }
                });

                // Filter grid cards
                pressCards.forEach(card => {
                    const category = card.getAttribute('data-category');
                    if (filter === 'all' || category === filter) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // Press Release Content Registry (Authentic Data from The Sattvic Method Company)
    const pressReleaseData = {
        'chaturmasya-release': {
            badge: 'Featured Program',
            badgeClass: 'badge-upcoming',
            title: 'Chaturmasya Sadhana 2026: Living Science of the Body-Temple',
            date: 'July 2026',
            location: 'Global Vedic Community',
            image: 'assets/chaturmasya-news.png',
            body: `
                <p><strong>GLOBAL ANNOUNCEMENT — July 2026</strong> — The Sattvic Method Company officially announces the commencement of registration for <em>Chaturmasya Sadhana 2026</em>, a 4-month guided spiritual journey rooted in timeless Vedic science and inner discipline.</p>
                <p>Chaturmasya is traditionally one of the most sacred periods of the Vedic calendar — a time when cosmic energies invite us to slow down, turn inward, and deepen our sadhana. The 2026 program integrates daily contemplative practices, subconscious realignment, mind-body detoxification, and sacred teachings designed for contemporary seekers.</p>
                <blockquote>"When we treat the body as a living temple and harmonize our daily rhythms with cosmic cycles, natural health, clarity, and peace arise effortlessly." — The Sattvic Method Faculty</blockquote>
                <p>Participants receive weekly guided contemplation audios, a personalized sadhana journal, and access to live community satsangs.</p>
                <p><a href="https://thesattvicmethodcompany.com/chaturmasya-sadhana-2026/" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm" style="margin-top: 0.5rem; display: inline-flex;">Visit Sadhana Portal <i class="fa-solid fa-arrow-up-right-from-square" style="margin-left: 0.4rem;"></i></a></p>
            `
        },
        'doulas-silence-release': {
            badge: 'Latest Book Launch',
            badgeClass: 'badge-published',
            title: "The Doula’s Silence: Stories of Loss, Grace, and the Divine Feminine",
            date: 'August 2026',
            location: 'Womb of Stars Series (#7)',
            image: 'assets/the-doulas-silence-press.png',
            body: `
                <p><strong>RELEASE DATE — August 2026</strong> — The Sattvic Method Company is proud to present <em>The Doula’s Silence</em>, the poignant seventh volume in the celebrated <em>Womb of Stars</em> literary collection.</p>
                <p>She has brought 218 babies into the world. She has never held one of her own. Mira is a doula — skilled, present, indispensable in hospital delivery rooms and home births alike. But beneath her steady hands lies a silent grief that has never spoken its name.</p>
                <p>A luminous, devastating short story exploring what women carry quietly, sacred surrender, and the extraordinary grace discovered when we finally allow ourselves to be held.</p>
                <blockquote>"A masterpiece of emotional restraint and profound spiritual tenderness." — Literary Review</blockquote>
                <p><a href="https://web.mytiny.us/sattvic-books/product/the-doulas-silence/" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm" style="margin-top: 0.5rem; display: inline-flex;">View Product Details <i class="fa-solid fa-arrow-up-right-from-square" style="margin-left: 0.4rem;"></i></a></p>
            `
        },
        'talking-cow-release': {
            badge: "Children's Books",
            badgeClass: 'badge-published',
            title: "'The Talking Cow and the Tree That Mooed' Enchanting Young Hearts",
            date: 'July 2026',
            location: 'The Sattvic Method Imprint',
            image: 'assets/the-talking-cow.png',
            body: `
                <p><strong>RELEASE ANNOUNCEMENT — July 2026</strong> — <em>The Talking Cow and the Tree That Mooed</em> invites young readers and families into a whimsical, heartwarming world where kindness speaks in surprising ways.</p>
                <p>What if the whole world was already good, and you just hadn’t learned to see it yet? Ramba the cow only wanted to help. Filled with lush illustrations and timeless values, this uplifting tale teaches children about empathy, non-harming (Ahimsa), and discovering beauty in nature's quietest corners.</p>
                <p>Perfect for bedtime storytelling, preschool reading circles, and conscious families seeking value-rich literature.</p>
            `
        },
        'rice-grew-release': {
            badge: "Children's Literature",
            badgeClass: 'badge-published',
            title: "'The Rice That Grew': An Ancient Indian Folktale Reimagined for Kids",
            date: 'June 2026',
            location: 'Kanchipuram Heritage Series',
            image: 'assets/the-rice-that-grew.png',
            body: `
                <p><strong>RELEASE ANNOUNCEMENT — June 2026</strong> — Drawing inspiration from classical Sanskrit literature (Dandin's <em>Dashakumaracharita</em>), <em>The Rice That Grew</em> transports children to the historic temples and fragrant kitchens of ancient Kanchipuram.</p>
                <p>When young Shaktikumara searches for wisdom and true partnership, he encounters Gomini, whose creative resourcefulness turns a single measure of paddy into a feast fit for kings. This joyful story celebrates mindfulness, gratitude for food, and the genius of Indian culinary heritage.</p>
                <p>Features rich full-color heritage artwork and a glossary of traditional cooking implements.</p>
            `
        },
        'recipe-keeper-release': {
            badge: 'Healing Fiction',
            badgeClass: 'badge-published',
            title: "'The Recipe Keeper' Unveils Grief as Devotion and Sacred Kitchen Space",
            date: 'June 2026',
            location: 'Womb of Stars Series (#6)',
            image: 'assets/the-recipe-keeper.png',
            body: `
                <p><strong>RELEASE ANNOUNCEMENT — June 2026</strong> — The Sattvic Method Company releases <em>The Recipe Keeper</em>, Book #6 in the <em>Womb of Stars</em> collection.</p>
                <p>Bharati is a celebrated culinary icon who reinvented herself on a prime-time cooking show while secretly mourning the sudden loss of her nineteen-year-old son. Between measuring spices and kneading dough, she discovers that cooking can be both an altar and an avenue of profound healing.</p>
                <blockquote>"In the quiet chemistry of the kitchen, every recipe is a prayer, and every shared meal an offering to love that never dies."</blockquote>
                <p><a href="https://web.mytiny.us/sattvic-books/product/the-recipe-keeper/" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm" style="margin-top: 0.5rem; display: inline-flex;">View Book Page <i class="fa-solid fa-arrow-up-right-from-square" style="margin-left: 0.4rem;"></i></a></p>
            `
        },
        'thirteen-cradles-release': {
            badge: 'Literary Fiction',
            badgeClass: 'badge-published',
            title: "'Thirteen Cradles' Explores Maternal Devotion Across Bundelkhand's Red Earth",
            date: 'May 2026',
            location: 'Womb of Stars Series (#4)',
            image: 'assets/thirteen-cradles.png',
            body: `
                <p><strong>RELEASE ANNOUNCEMENT — May 2026</strong> — <em>Thirteen Cradles</em> is an unforgettable portrait of motherly love set in Bundelkhand, an arid region of red earth and harsh winds.</p>
                <p>Sushila has been pregnant fourteen times. Across seasons of drought and silent devotion, she walks before dawn to whisper prayers to the rising sun. A powerful meditation on faith, generational resilience, and the sanctified bond of womanhood.</p>
            `
        },
        'clay-ash-release': {
            badge: 'Adults & Healing',
            badgeClass: 'badge-published',
            title: "'Clay & Ash': Kumartuli Sculptors, Sacred River Mud, and the Divine Eyes",
            date: 'May 2026',
            location: 'Womb of Stars Series (#3)',
            image: 'assets/clay-and-ash.png',
            body: `
                <p><strong>RELEASE ANNOUNCEMENT — May 2026</strong> — In the cramped, clay-dusted lanes of Kolkata’s Kumartuli where sacred idols are molded from holy Ganga silt, Gauri has spent forty years painting the lifegiving eyes (*Chokkhu Daan*) onto the fierce, compassionate face of Goddess Durga.</p>
                <p><em>Clay & Ash</em> probes deep questions of human suffering, artistic duty, and the invisible threads connecting mortal sorrow with transcendent divine grace.</p>
            `
        },
        'coral-keeper-release': {
            badge: 'Healing Fiction',
            badgeClass: 'badge-published',
            title: "'The Coral Keeper': Sixty Feet Beneath the Waves, Finding Inner Surrender",
            date: 'April 2026',
            location: 'Womb of Stars Series (#1)',
            image: 'assets/the-coral-keeper.png',
            body: `
                <p><strong>RELEASE ANNOUNCEMENT — April 2026</strong> — She has suffered repeated loss and stopped praying altogether. The only refuge left is sixty feet beneath the turquoise ocean swells among the living coral reefs.</p>
                <p>In the silence of deep waters, away from human expectations and medical charts, she rediscovers breath, surrender, and the eternal embrace of the Divine Feminine.</p>
            `
        },
        'accountants-ledger-release': {
            badge: 'Contemporary Healing',
            badgeClass: 'badge-published',
            title: "'The Accountant’s Ledger': Tracking Cycles, Yielding Control to the Unseen",
            date: 'April 2026',
            location: 'Womb of Stars Series (#2)',
            image: 'assets/the-accountants-ledger.png',
            body: `
                <p><strong>RELEASE ANNOUNCEMENT — April 2026</strong> — Priya Iyer is a meticulous Toronto tax accountant accustomed to numbers balancing perfectly. When facing infertility, she attempts to manage heartbreak with precision spreadsheets: Cycle Number, Follicle Count, Estradiol, Lining Thickness.</p>
                <p>A poignant, modern, and deeply relatable story about the limits of human calculation and the peace discovered when we surrender control to the higher intelligence of life.</p>
            `
        },
        'breakfast-recipes-release': {
            badge: 'Ayurvedic Cookbooks',
            badgeClass: 'badge-published',
            title: "'Sattvic Breakfast Recipes': 30 Morning Meals for Energy & Clarity",
            date: 'March 2026',
            location: 'Culinary Wisdom Series',
            image: 'assets/sattvic-breakfast-recipes.png',
            body: `
                <p><strong>RELEASE ANNOUNCEMENT — March 2026</strong> — There is a precious moment before the rush of the modern day begins when the mind is receptive and clean. <em>Sattvic Breakfast Recipes</em> offers 30 whole-food, plant-powered morning recipes crafted according to Ayurvedic food synergy.</p>
                <p>Free from refined sugars, onion, garlic, and processed ingredients, these recipes balance Agni (digestive fire), stabilize prana, and sustain mental focus throughout the day.</p>
            `
        },
        'tree-children-release': {
            badge: "Children's Imprint",
            badgeClass: 'badge-published',
            title: "'The Gift That Became A Tree' Inspiring Children Toward Compassion & Nature",
            date: 'March 2026',
            location: 'Illustrated Mindful Series',
            image: 'assets/the-gift-that-became-a-tree.webp',
            body: `
                <p><strong>RELEASE ANNOUNCEMENT — March 2026</strong> — <em>The Gift That Became A Tree</em> follows a young king whose journey into the forest teaches him the deepest truth of leadership: real strength comes from selfless generosity and living in harmony with nature.</p>
                <p>Featuring breathtaking watercolor illustrations and a parent-teacher discussion guide on environmental stewardship and mindfulness.</p>
            `
        },
        'featured': {
            badge: 'Featured Program',
            badgeClass: 'badge-upcoming',
            title: 'Chaturmasya Sadhana 2026: Living Science of the Body-Temple',
            date: 'July 2026',
            location: 'Global Vedic Community',
            image: 'assets/chaturmasya-news.png',
            body: `
                <p><strong>GLOBAL ANNOUNCEMENT — July 2026</strong> — The Sattvic Method Company officially announces the commencement of registration for <em>Chaturmasya Sadhana 2026</em>, a 4-month guided spiritual journey rooted in timeless Vedic science and inner discipline.</p>
                <p>Chaturmasya is traditionally one of the most sacred periods of the Vedic calendar — a time when cosmic energies invite us to slow down, turn inward, and deepen our sadhana.</p>
            `
        }
    };

    // Press Modal Event Delegation Handler
    document.addEventListener('click', (e) => {
        const btn = e.target.closest('.open-press-modal');
        if (btn) {
            e.preventDefault();
            const key = btn.getAttribute('data-release');
            const data = pressReleaseData[key] || pressReleaseData['featured'];
            
            const pressModal = document.getElementById('pressModal');
            const modalBadge = document.getElementById('modalPressBadge');
            const modalTitle = document.getElementById('modalPressTitle');
            const modalDate = document.getElementById('modalPressDate');
            const modalLocation = document.getElementById('modalPressLocation');
            const modalBody = document.getElementById('modalPressBody');

            if (modalBadge) {
                modalBadge.className = 'press-badge ' + data.badgeClass;
                modalBadge.innerText = data.badge;
            }
            if (modalTitle) modalTitle.innerText = data.title;
            if (modalDate) modalDate.innerHTML = `<i class="fa-regular fa-calendar"></i> ${data.date}`;
            if (modalLocation) modalLocation.innerHTML = `<i class="fa-solid fa-location-dot"></i> ${data.location}`;
            if (modalBody) {
                modalBody.innerHTML = `
                    <div class="press-modal-layout">
                        <img src="${data.image}" alt="${data.title}" class="press-modal-book-img">
                        <div>${data.body}</div>
                    </div>
                `;
            }

            if (pressModal) {
                pressModal.classList.add('active');
                document.body.style.overflow = 'hidden';
            }
        }
    });

    const pressModal = document.getElementById('pressModal');
    const closePressModal = document.getElementById('closePressModal');
    const modalCloseBtn = document.getElementById('modalCloseBtn');

    const closeModalFunc = () => {
        if (pressModal) {
            pressModal.classList.remove('active');
            document.body.style.overflow = '';
        }
    };

    if (closePressModal) closePressModal.addEventListener('click', closeModalFunc);
    if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeModalFunc);
    if (pressModal) {
        pressModal.addEventListener('click', (e) => {
            if (e.target === pressModal) closeModalFunc();
        });
    }

    // Close on Escape key press
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && pressModal && pressModal.classList.contains('active')) {
            closeModalFunc();
        }
    });

    // Press Kit Download Listener
    const downloadKitBtn = document.getElementById('downloadKitBtn');
    if (downloadKitBtn) {
        downloadKitBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const dummyBlob = new Blob([
                "Sattvic Books Official Press Kit 2026\nHigh-Res Covers, Author Bios, Press Releases & Brand Assets."
            ], { type: 'application/zip' });
            const blobUrl = URL.createObjectURL(dummyBlob);
            const a = document.createElement('a');
            a.href = blobUrl;
            a.download = 'Sattvic_Books_Official_Press_Kit_2026.zip';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        });
    }

    // 10. Catalog Download Lead Capture Modal Logic
    const catalogModal = document.getElementById('catalogModal') || document.getElementById('catalogueModal');
    const openCatalogBtns = document.querySelectorAll('.open-catalog-modal, .open-catalogue-modal');
    const closeCatalogModal = document.getElementById('closeCatalogModal') || document.getElementById('closeCatalogueModal');
    const catalogForm = document.getElementById('catalogForm') || document.getElementById('catalogueForm');

    openCatalogBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (catalogModal) {
                e.preventDefault();
                catalogModal.classList.add('active');
            } else {
                window.location.href = 'index.html#catalogModal';
            }
        });
    });

    if (catalogModal) {
        if (closeCatalogModal) {
            closeCatalogModal.addEventListener('click', () => {
                catalogModal.classList.remove('active');
            });
        }

        catalogModal.addEventListener('click', (e) => {
            if (e.target === catalogModal) catalogModal.classList.remove('active');
        });

        // Close catalog modal on Escape key press
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && catalogModal.classList.contains('active')) {
                catalogModal.classList.remove('active');
            }
        });

        if (catalogForm) {
            catalogForm.addEventListener('submit', (e) => {
                e.preventDefault();
                const btn = catalogForm.querySelector('button[type="submit"]');
                const originalText = btn.innerHTML;
                
                btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending Catalog PDF...';
                btn.disabled = true;

                setTimeout(() => {
                    catalogModal.classList.remove('active');
                    btn.innerHTML = originalText;
                    btn.disabled = false;
                    catalogForm.reset();

                    // Trigger simulated PDF Download
                    const dummyBlob = new Blob([
                        "%PDF-1.5 Sattvic Books 2026 Official Catalog & Reading Guide\nWelcome to Sattvic Books - Ancient Wisdom for Modern Living."
                    ], { type: 'application/pdf' });
                    const blobUrl = URL.createObjectURL(dummyBlob);
                    const a = document.createElement('a');
                    a.href = blobUrl;
                    a.download = 'Sattvic_Books_2026_Official_Catalog.pdf';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);

                    showActionModal(
                        '<i class="fa-solid fa-envelope-circle-check" style="color: var(--clr-gold);"></i>',
                        'Catalog Sent to Your Email!',
                        'Please check your email inbox to receive your <strong>2026 Sattvic Books Catalog (PDF)</strong>. Your instant download has also started.'
                    );
                }, 1200);
            });
        }
    }

    // 11. Event Sub-Tabs Switcher (Meet Author vs Book Club)
    const eventTabBtns = document.querySelectorAll('.event-tab-btn');
    const tabPanels = document.querySelectorAll('.tab-panel');

    eventTabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            eventTabBtns.forEach(b => b.classList.remove('active'));
            tabPanels.forEach(p => p.classList.remove('active'));

            btn.classList.add('active');
            const targetTab = btn.getAttribute('data-tab');
            const targetPanel = document.getElementById('tab-' + targetTab);
            if (targetPanel) targetPanel.classList.add('active');
        });
    });

    // 12. Media Hub Sub-Tabs Switcher (Discussions, YT Videos, Releases, Courses)
    const mediaTabBtns = document.querySelectorAll('.media-tab-btn');
    const mediaTabPanels = document.querySelectorAll('.media-tab-panel');

    mediaTabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            mediaTabBtns.forEach(b => b.classList.remove('active'));
            mediaTabPanels.forEach(p => p.classList.remove('active'));

            btn.classList.add('active');
            const targetTab = btn.getAttribute('data-tab');
            const targetPanel = document.getElementById('tab-' + targetTab);
            if (targetPanel) targetPanel.classList.add('active');
        });
    });

    // 13. Freebie / Giveaway Direct Downloads Handler
    const freebieBtns = document.querySelectorAll('.trigger-freebie');
    freebieBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const itemTitle = btn.getAttribute('data-title') || 'Free Resource';
            
            // Create dummy file download
            const dummyBlob = new Blob([
                `Sattvic Books Freebie Resource: ${itemTitle}\nThank you for choosing Sattvic Books!`
            ], { type: 'text/plain' });
            const blobUrl = URL.createObjectURL(dummyBlob);
            const a = document.createElement('a');
            a.href = blobUrl;
            a.download = `${itemTitle.replace(/\s+/g, '_')}.txt`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);

            showActionModal(
                '<i class="fa-solid fa-circle-check" style="color: var(--clr-gold);"></i>',
                'Download Started!',
                `Your free download for <strong>${itemTitle}</strong> has begun. Enjoy your mindful reading!`
            );
        });
    });

    // 14. Action Modal Helpers (RSVP, Course Enrollment, Discussion Modals)
    const actionModal = document.getElementById('actionModal');
    const closeActionModal = document.getElementById('closeActionModal');
    const actionModalOk = document.getElementById('actionModalOk');

    function showActionModal(iconHtml, titleText, bodyText) {
        if (!actionModal) return;
        const modalIcon = document.getElementById('actionModalIcon');
        const modalTitle = document.getElementById('actionModalTitle');
        const modalBody = document.getElementById('actionModalBody');

        if (modalIcon) modalIcon.innerHTML = iconHtml;
        if (modalTitle) modalTitle.innerText = titleText;
        if (modalBody) modalBody.innerHTML = bodyText;

        actionModal.classList.add('active');
    }

    if (closeActionModal) closeActionModal.addEventListener('click', () => actionModal.classList.remove('active'));
    if (actionModalOk) actionModalOk.addEventListener('click', () => actionModal.classList.remove('active'));
    if (actionModal) {
        actionModal.addEventListener('click', (e) => {
            if (e.target === actionModal) actionModal.classList.remove('active');
        });
    }

    // RSVP Event Listeners
    document.querySelectorAll('.open-rsvp-modal').forEach(btn => {
        btn.addEventListener('click', () => {
            const eventName = btn.getAttribute('data-event') || 'Event';
            showActionModal(
                '<i class="fa-solid fa-calendar-check" style="color: var(--clr-gold);"></i>',
                'RSVP Confirmed!',
                `You have successfully registered for <strong>${eventName}</strong>. A calendar invite link has been sent.`
            );
        });
    });

    // Course Enrollment Listeners
    document.querySelectorAll('.open-course-modal').forEach(btn => {
        btn.addEventListener('click', () => {
            const courseName = btn.getAttribute('data-course') || 'Online Course';
            showActionModal(
                '<i class="fa-solid fa-graduation-cap" style="color: var(--clr-gold);"></i>',
                'Course Registration',
                `Welcome to <strong>${courseName}</strong>! Registration for this masterclass will open with the launch of our digital learning platform.`
            );
        });
    });

    // Discussion Join Listeners
    document.querySelectorAll('.open-discussion-modal').forEach(btn => {
        btn.addEventListener('click', () => {
            const topic = btn.getAttribute('data-title') || 'Book Discussion';
            showActionModal(
                '<i class="fa-solid fa-comments" style="color: var(--clr-gold);"></i>',
                'Reader Discussion Forum',
                `Opening reader discussion thread for <strong>${topic}</strong>. Join the conversation and share your reflection!`
            );
        });
    });

    // Book Club Signup Form Handler
    const clubForm = document.getElementById('clubForm');
    if (clubForm) {
        clubForm.addEventListener('submit', (e) => {
            e.preventDefault();
            showActionModal(
                '<i class="fa-solid fa-people-group" style="color: var(--clr-gold);"></i>',
                'Welcome to Sattvic Book Club!',
                'You are now registered for our September reading circle. Watch your inbox for discussion guides and Zoom links!'
            );
            clubForm.reset();
        });
    }

    // 15. Gift Store Notification Handler
    document.querySelectorAll('.open-gift-notify').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            showActionModal(
                '<i class="fa-solid fa-gift" style="color: var(--clr-gold);"></i>',
                'Gift Store Opening Soon!',
                'Our Gift Store is being lovingly prepared. You will be among the first to be notified as soon as our curated gift collections, bundles, and gift cards open!'
            );
        });
    });

    // 16. Meet the Author Form (Email, CAPTCHA, Notes <= 100 words)
    const meetAuthorForm = document.getElementById('meetAuthorForm');
    const authorNotes = document.getElementById('authorNotes');
    const authorNotesWordCount = document.getElementById('authorNotesWordCount');
    const authorNotesError = document.getElementById('authorNotesError');
    const meetAuthorCaptchaQuestion = document.getElementById('meetAuthorCaptchaQuestion');
    const meetAuthorCaptchaInput = document.getElementById('meetAuthorCaptchaInput');
    const refreshMeetAuthorCaptcha = document.getElementById('refreshMeetAuthorCaptcha');
    const meetAuthorCaptchaError = document.getElementById('meetAuthorCaptchaError');

    let captchaA = 6;
    let captchaB = 7;

    function generateCaptcha() {
        captchaA = Math.floor(Math.random() * 9) + 2;
        captchaB = Math.floor(Math.random() * 9) + 2;
        if (meetAuthorCaptchaQuestion) {
            meetAuthorCaptchaQuestion.textContent = `What is ${captchaA} + ${captchaB}?`;
        }
        if (meetAuthorCaptchaInput) {
            meetAuthorCaptchaInput.value = '';
        }
        if (meetAuthorCaptchaError) {
            meetAuthorCaptchaError.style.display = 'none';
        }
    }

    if (refreshMeetAuthorCaptcha) {
        refreshMeetAuthorCaptcha.addEventListener('click', generateCaptcha);
    }

    function countWords(str) {
        if (!str) return 0;
        const matches = str.trim().match(/\S+/g);
        return matches ? matches.length : 0;
    }

    if (authorNotes && authorNotesWordCount) {
        authorNotes.addEventListener('input', () => {
            const words = countWords(authorNotes.value);
            authorNotesWordCount.textContent = `${words} / 100 words`;
            if (words > 100) {
                authorNotesWordCount.style.color = '#e53e3e';
                if (authorNotesError) authorNotesError.style.display = 'block';
            } else {
                authorNotesWordCount.style.color = 'var(--clr-text-muted)';
                if (authorNotesError) authorNotesError.style.display = 'none';
            }
        });
    }

    if (meetAuthorForm) {
        generateCaptcha();
        meetAuthorForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = (document.getElementById('authorEmail')?.value || '').trim();
            const notes = (authorNotes?.value || '').trim();
            const words = countWords(notes);
            const captchaUserAnswer = parseInt(meetAuthorCaptchaInput?.value, 10);

            if (!email) {
                document.getElementById('authorEmail')?.focus();
                return;
            }

            if (words > 100) {
                if (authorNotesError) authorNotesError.style.display = 'block';
                authorNotes?.focus();
                return;
            }

            if (captchaUserAnswer !== (captchaA + captchaB)) {
                if (meetAuthorCaptchaError) meetAuthorCaptchaError.style.display = 'block';
                meetAuthorCaptchaInput?.focus();
                return;
            }

            // Success
            showActionModal(
                '<i class="fa-solid fa-circle-check" style="color: var(--clr-gold);"></i>',
                'Note Sent to the Author!',
                `Thank you! Your note and message have been delivered to our authors. A confirmation and event invitation have been sent to <strong>${email}</strong>.`
            );

            meetAuthorForm.reset();
            if (authorNotesWordCount) authorNotesWordCount.textContent = '0 / 100 words';
            if (authorNotesError) authorNotesError.style.display = 'none';
            generateCaptcha();
        });
    }

    // 25. Promo Ticker Coupon Code Copy Handler
    const copyCouponBtns = document.querySelectorAll('.copy-coupon-btn');
    if (copyCouponBtns.length > 0) {
        copyCouponBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const code = btn.getAttribute('data-code') || 'SATTVIC20';
                
                const copyText = () => {
                    const originalHTML = btn.innerHTML;
                    btn.innerHTML = `<span>Copied!</span> <i class="fa-solid fa-check"></i>`;
                    btn.style.background = 'var(--clr-gold)';
                    btn.style.color = '#2C1E14';
                    btn.style.borderStyle = 'solid';

                    setTimeout(() => {
                        btn.innerHTML = originalHTML;
                        btn.style.background = '';
                        btn.style.color = '';
                        btn.style.borderStyle = '';
                    }, 2200);
                };

                if (navigator.clipboard && navigator.clipboard.writeText) {
                    navigator.clipboard.writeText(code).then(copyText).catch(() => {
                        copyText();
                    });
                } else {
                    const tempInput = document.createElement('input');
                    tempInput.value = code;
                    document.body.appendChild(tempInput);
                    tempInput.select();
                    document.execCommand('copy');
                    document.body.removeChild(tempInput);
                    copyText();
                }
            });
        });
    }
});


