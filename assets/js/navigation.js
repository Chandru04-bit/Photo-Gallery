/**
 * PROJECT 58 – UTSAV STAGE, TENT & PANDAL CONTRACTOR
 * Navigation Script (navigation.js)
 */

document.addEventListener('DOMContentLoaded', () => {
  // Highlight active menu item based on current URL path (supports clean URLs and .html)
  const currentPath = (window.location.pathname.split('/').pop() || 'index').replace(/\.html$/, '') || 'index';
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link, .dropdown-item');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;

    // Direct match or root index match
    const linkFile = href.split('/').pop().replace(/\.html$/, '');
    if (linkFile === currentPath || ((currentPath === '' || currentPath === 'index') && (linkFile === 'index' || linkFile === ''))) {
      link.classList.add('active');

      // Also set parent dropdown nav-link active if inside dropdown
      const parentDropdown = link.closest('.nav-item.dropdown');
      if (parentDropdown) {
        const toggle = parentDropdown.querySelector('.dropdown-toggle');
        if (toggle) toggle.classList.add('active');
      }
    }
  });

  // Close mobile navigation offcanvas/collapse when clicking outside or clicking a nav-link (if not dropdown toggle)
  const navbarCollapse = document.querySelector('.navbar-collapse');
  const navbarToggler = document.querySelector('.navbar-toggler');

  if (navbarCollapse && navbarToggler) {
    document.querySelectorAll('.navbar-nav .nav-link:not(.dropdown-toggle)').forEach(link => {
      link.addEventListener('click', () => {
        if (navbarCollapse.classList.contains('show')) {
          navbarToggler.click();
        }
      });
    });
  }
});
