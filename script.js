document.addEventListener('DOMContentLoaded', () => {

    /* =========================================
       1. WhatsApp Button Pulse Control
       ========================================= */
    const whatsappBtn = document.getElementById('whatsapp-btn');
    let hasScrolled = false;

    // Remove pulse on scroll
    const handleScroll = () => {
        if (!hasScrolled && window.scrollY > 50) {
            whatsappBtn.classList.remove('pulse-animation');
            hasScrolled = true;
            window.removeEventListener('scroll', handleScroll);
        }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });

    /* =========================================
       1.5. Header Glassmorphism on Scroll
       ========================================= */
    const header = document.getElementById('main-header');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('py-3');
            header.classList.remove('py-6');
        } else {
            header.classList.remove('py-3');
            header.classList.add('py-6');
        }
    }, { passive: true });

    // Remove pulse after 5 seconds regardless of scroll
    setTimeout(() => {
        if (whatsappBtn && whatsappBtn.classList.contains('pulse-animation')) {
            whatsappBtn.classList.remove('pulse-animation');
        }
    }, 5000);


    /* =========================================
       2. Accordion Logic
       ========================================= */
    const accordionItems = document.querySelectorAll('.accordion-item');

    accordionItems.forEach(item => {
        const header = item.querySelector('.accordion-header');
        const content = item.querySelector('.accordion-content');
        const icon = item.querySelector('.icon-plus');

        header.addEventListener('click', () => {
            const isExpanded = header.getAttribute('aria-expanded') === 'true';

            // Close all items
            accordionItems.forEach(otherItem => {
                const otherHeader = otherItem.querySelector('.accordion-header');
                const otherContent = otherItem.querySelector('.accordion-content');
                const otherIcon = otherItem.querySelector('.icon-plus');
                
                if (otherHeader !== header) {
                    otherHeader.setAttribute('aria-expanded', 'false');
                    otherContent.style.maxHeight = '0px';
                    otherContent.style.paddingTop = '0px';
                    if (otherIcon) otherIcon.textContent = '+';
                }
            });

            // Toggle current item
            if (!isExpanded) {
                header.setAttribute('aria-expanded', 'true');
                content.style.maxHeight = content.scrollHeight + 40 + 'px'; // +40 for padding
                content.style.paddingTop = '1.5rem';
                if (icon) icon.textContent = '−';
            } else {
                header.setAttribute('aria-expanded', 'false');
                content.style.maxHeight = '0px';
                content.style.paddingTop = '0px';
                if (icon) icon.textContent = '+';
            }
        });
    });


    /* =========================================
       3. Blind Gallery (Meta Ads)
       ========================================= */
    const galleryItems = document.querySelectorAll('.blind-gallery-item');

    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            const img = this.querySelector('img');
            const overlay = this.querySelector('.overlay-reveal');
            
            if (img && img.classList.contains('filter-blur')) {
                // Remove blur
                img.classList.remove('filter-blur');
                img.style.transform = 'scale(1)'; 
                
                if (overlay) {
                    // Hide overlay
                    overlay.style.opacity = '0';
                    setTimeout(() => {
                        overlay.style.display = 'none';
                    }, 500);
                }
            }
        });
    });

    /* =========================================
       4. Modal & Swiper Gallery Logic
       ========================================= */
    window.openModal = function(modalId) {
        const modal = document.getElementById(modalId);
        if (!modal) return;
        
        document.body.style.overflow = 'hidden';
        modal.classList.remove('hidden');
        setTimeout(() => {
            modal.classList.remove('opacity-0');
            modal.classList.add('opacity-100');
        }, 10);

        const index = modalId.split('-')[1];
        
        const lazyMedia = modal.querySelectorAll('[data-src]');
        lazyMedia.forEach(media => {
            if (!media.getAttribute('src') && media.getAttribute('data-src')) {
                media.setAttribute('src', media.getAttribute('data-src'));
                if(media.tagName === 'VIDEO') {
                    media.load();
                }
            }
        });

        if (!modal.swiperInstance) {
            modal.swiperInstance = new Swiper('.swiper-' + index, {
                loop: true,
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                },
                pagination: {
                    el: '.swiper-pagination',
                    clickable: true,
                },
                on: {
                    slideChangeTransitionEnd: function () {
                        const swiper = this;
                        const videos = modal.querySelectorAll('video');
                        videos.forEach(v => v.pause());
                        const activeSlide = swiper.slides[swiper.activeIndex];
                        if (activeSlide) {
                            const activeVideo = activeSlide.querySelector('video');
                            if (activeVideo) activeVideo.play().catch(e => console.log("Autoplay prevented"));
                        }
                    }
                }
            });
        }
        
        setTimeout(() => {
            const activeSlide = modal.querySelector('.swiper-slide-active');
            if (activeSlide) {
                const activeVideo = activeSlide.querySelector('video');
                if (activeVideo) activeVideo.play().catch(e => console.log("Autoplay prevented"));
            }
        }, 300);
    };

    window.closeModal = function(modalId) {
        const modal = document.getElementById(modalId);
        if (!modal) return;
        
        const videos = modal.querySelectorAll('video');
        videos.forEach(v => v.pause());

        modal.classList.remove('opacity-100');
        modal.classList.add('opacity-0');
        
        setTimeout(() => {
            modal.classList.add('hidden');
            document.body.style.overflow = '';
        }, 300);
    };

    // Close Modal on Escape Key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            const openModal = document.querySelector('.fixed.inset-0:not(.hidden)');
            if (openModal) window.closeModal(openModal.id);
        }
    });

    // Close Modal on Click Outside
    document.querySelectorAll('.fixed.inset-0').forEach(modal => {
        modal.addEventListener('click', (e) => {
            // Check if user clicked exactly on the backdrop (not inside the content)
            if (e.target === modal) {
                window.closeModal(modal.id);
            }
        });
    });
});
