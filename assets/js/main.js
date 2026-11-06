/**
 * PROJECT 58 – UTSAV STAGE, TENT & PANDAL CONTRACTOR
 * Core Main Script (main.js)
 */

// Early apply direction & theme from localStorage to prevent layout flashing
(function() {
  try {
    const savedDirection = localStorage.getItem('utsav_direction') || localStorage.getItem('direction') || 'ltr';
    document.documentElement.setAttribute('dir', savedDirection);
    const savedTheme = localStorage.getItem('utsav_theme') || localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
  } catch (e) {
    /* ignore storage access exceptions */
  }
})();

document.addEventListener('DOMContentLoaded', () => {
  const getStoredPreference = (keys, fallback) => {
    try {
      for (const key of keys) {
        const value = localStorage.getItem(key);
        if (value) return value;
      }
    } catch (e) {
      console.warn('Preference storage warning:', e);
    }
    return fallback;
  };

  // Sticky Navbar on Scroll
  const navbar = document.querySelector('.main-navbar');
  const backToTopBtn = document.querySelector('.back-to-top');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;

    // Sticky Nav
    if (navbar) {
      if (scrollY > 60) {
        navbar.classList.add('sticky-nav');
      } else {
        navbar.classList.remove('sticky-nav');
      }
    }

    // Back to Top Button visibility
    if (backToTopBtn) {
      if (scrollY > 400) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    }
  });

  // Back to Top click
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // Dark Mode Toggle & Persistence
  const updateThemeButtons = (theme) => {
    const allToggleBtns = document.querySelectorAll('#themeToggleBtn, #themeToggleBtnMobile, .theme-toggle-btn');
    allToggleBtns.forEach(btn => {
      const icon = btn.querySelector('i');
      if (icon) {
        icon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-stars-fill';
      }
      btn.setAttribute('aria-label', theme === 'dark' ? 'Switch to Light Theme' : 'Switch to Dark Theme');
      btn.setAttribute('title', theme === 'dark' ? 'Switch to Light Theme' : 'Switch to Dark Theme');
    });
  };

  const updateBrandLogos = (theme) => {
    document.querySelectorAll('.navbar-brand img').forEach(logo => {
      const src = logo.getAttribute('src');
      if (src && /(?:^|\/)logo(?:-dark)?\.svg$/.test(src)) {
        logo.setAttribute('src', src.replace(/logo(?:-dark)?\.svg$/, theme === 'dark' ? 'logo-dark.svg' : 'logo.svg'));
      }
    });
  };

  const setTheme = (theme) => {
    const activeTheme = theme === 'dark' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', activeTheme);
    try {
      localStorage.setItem('utsav_theme', activeTheme);
      localStorage.setItem('theme', activeTheme);
    } catch (e) {
      console.warn('Theme storage warning:', e);
    }
    updateThemeButtons(activeTheme);
    updateBrandLogos(activeTheme);
    window.dispatchEvent(new CustomEvent('themechange', { detail: { theme: activeTheme } }));
  };

  // Initialize theme on DOM ready
  const savedTheme = getStoredPreference(
    ['utsav_theme', 'theme'],
    document.documentElement.getAttribute('data-theme') || 'light'
  );
  setTheme(savedTheme);

  // Global robust event delegation for theme toggle buttons (desktop, mobile, offcanvas)
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('#themeToggleBtn, #themeToggleBtnMobile, .theme-toggle-btn');
    if (btn) {
      e.preventDefault();
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      setTheme(newTheme);
    }
  });

  // LTR & RTL Language Direction Toggle & Persistence
  const dirButtons = document.querySelectorAll('.btn-dir-toggle, [data-dir]');
  const initialDirection = getStoredPreference(
    ['utsav_direction', 'direction'],
    document.documentElement.getAttribute('dir') || 'ltr'
  );

  const setDirection = (direction) => {
    const dir = direction === 'rtl' ? 'rtl' : 'ltr';
    document.documentElement.setAttribute('dir', dir);

    try {
      localStorage.setItem('utsav_direction', dir);
      localStorage.setItem('direction', dir);
    } catch (e) {
      console.warn('Direction persistence storage warning:', e);
    }

    // Update active states immediately on all direction toggle buttons across the DOM
    const allButtons = document.querySelectorAll('.btn-dir-toggle, [data-dir]');
    allButtons.forEach(btn => {
      const btnDir = btn.getAttribute('data-dir');
      const isActive = btnDir === dir;
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
    });

    // Notify any components of direction change
    window.dispatchEvent(new CustomEvent('directionchange', { detail: { direction: dir } }));
  };

  // Initialize active state on load
  setDirection(initialDirection);

  // Bind click listener to all direction toggle buttons
  document.addEventListener('click', (e) => {
    const dirBtn = e.target.closest('.btn-dir-toggle, [data-dir]');
    if (dirBtn) {
      e.preventDefault();
      const targetDir = dirBtn.getAttribute('data-dir');
      if (targetDir) {
        setDirection(targetDir);
      }
    }
  });

  // Smooth scroll for internal links
  document.querySelectorAll('a[href^="#"]:not([href="#"]):not([data-bs-toggle])').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId && targetId !== '#') {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          e.preventDefault();
          targetElement.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });
});
