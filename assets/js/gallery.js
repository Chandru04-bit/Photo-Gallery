/**
 * PROJECT 58 – UTSAV STAGE, TENT & PANDAL CONTRACTOR
 * Gallery & Lightbox Script (gallery.js)
 */

document.addEventListener('DOMContentLoaded', () => {
  const filterBtns = document.querySelectorAll('.gallery-filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-item');
  const lightboxModal = document.getElementById('galleryLightbox');

  if (!galleryItems.length) return;

  // Filter gallery items by category
  if (filterBtns.length) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const category = btn.getAttribute('data-filter');

        galleryItems.forEach(item => {
          const itemCat = item.getAttribute('data-category');
          if (category === 'all' || itemCat === category) {
            item.parentElement.style.display = 'block';
            setTimeout(() => {
              item.style.opacity = '1';
              item.style.transform = 'scale(1)';
            }, 50);
          } else {
            item.style.opacity = '0';
            item.style.transform = 'scale(0.9)';
            setTimeout(() => {
              item.parentElement.style.display = 'none';
            }, 300);
          }
        });
      });
    });
  }

  // Lightbox functionality
  if (lightboxModal) {
    const lightboxImg = lightboxModal.querySelector('.lightbox-content img');
    const lightboxTitle = lightboxModal.querySelector('.lightbox-caption h4');
    const lightboxCat = lightboxModal.querySelector('.lightbox-caption p');
    const closeBtn = lightboxModal.querySelector('.lightbox-close');
    const prevBtn = lightboxModal.querySelector('.lightbox-prev');
    const nextBtn = lightboxModal.querySelector('.lightbox-next');

    let currentIndex = 0;
    let visibleItems = [];

    const updateVisibleItems = () => {
      visibleItems = Array.from(galleryItems).filter(item => {
        return item.parentElement.style.display !== 'none';
      });
    };

    const showImageAtIndex = (index) => {
      updateVisibleItems();
      if (!visibleItems.length) return;

      if (index < 0) {
        currentIndex = visibleItems.length - 1;
      } else if (index >= visibleItems.length) {
        currentIndex = 0;
      } else {
        currentIndex = index;
      }

      const currentItem = visibleItems[currentIndex];
      const img = currentItem.querySelector('img');
      const title = currentItem.querySelector('.gallery-overlay h5') || currentItem.getAttribute('data-title');
      const cat = currentItem.querySelector('.gallery-overlay span') || currentItem.getAttribute('data-category');

      if (img && lightboxImg) {
        lightboxImg.src = img.src;
        lightboxImg.alt = img.alt || 'Gallery Image';
      }
      if (lightboxTitle) {
        lightboxTitle.textContent = typeof title === 'string' ? title : (title ? title.textContent : 'Event Decoration');
      }
      if (lightboxCat) {
        lightboxCat.textContent = typeof cat === 'string' ? cat : (cat ? cat.textContent : 'Stage & Pandal Decor');
      }
    };

    // Open Lightbox
    galleryItems.forEach((item) => {
      item.addEventListener('click', () => {
        updateVisibleItems();
        currentIndex = visibleItems.indexOf(item);
        if (currentIndex === -1) currentIndex = 0;
        showImageAtIndex(currentIndex);
        lightboxModal.classList.add('active');
        document.body.style.overflow = 'hidden';
      });
    });

    // Close Lightbox
    const closeLightbox = () => {
      lightboxModal.classList.remove('active');
      document.body.style.overflow = '';
    };

    if (closeBtn) closeBtn.addEventListener('click', closeLightbox);

    lightboxModal.addEventListener('click', (e) => {
      if (e.target === lightboxModal) {
        closeLightbox();
      }
    });

    // Prev / Next Controls
    if (prevBtn) {
      prevBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        showImageAtIndex(currentIndex - 1);
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        showImageAtIndex(currentIndex + 1);
      });
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (!lightboxModal.classList.contains('active')) return;

      if (e.key === 'Escape') {
        closeLightbox();
      } else if (e.key === 'ArrowLeft') {
        showImageAtIndex(currentIndex - 1);
      } else if (e.key === 'ArrowRight') {
        showImageAtIndex(currentIndex + 1);
      }
    });
  }
});
