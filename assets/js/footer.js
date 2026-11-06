(() => {
  const scriptUrl = document.currentScript?.src;
  if (!scriptUrl) {
    console.error('Unable to determine the shared footer asset location.');
    return;
  }

  const siteRoot = new URL('../../', scriptUrl);
  const page = (path) => new URL(path, siteRoot).href;
  const footer = `
    <footer class="site-footer utsav-footer">
      <div class="container">
        <div class="row g-4 g-xl-5">
          <div class="col-lg-4 col-md-6">
            <a href="${page('index.html')}" class="footer-logo d-inline-block" aria-label="UTSAV Decor home">
              <img src="${page('assets/images/logo/logo-footer.svg')}" alt="UTSAV Decor — Stage, Tent, Pandal">
            </a>
            <p class="footer-about">
              UTSAV is a premier stage, tent, and pandal contracting company specializing in grand wedding mandaps, reception stages, German marquee canopies, and festival decor setups.
            </p>
            <div class="footer-social" aria-label="Social media">
              <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="bi bi-facebook"></i></a>
              <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><i class="bi bi-instagram"></i></a>
              <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><i class="bi bi-youtube"></i></a>
              <a href="https://pinterest.com" target="_blank" rel="noopener noreferrer" aria-label="Pinterest"><i class="bi bi-pinterest"></i></a>
            </div>
          </div>

          <div class="col-lg-2 col-md-6 col-6">
            <h4 class="footer-title">Quick Links</h4>
            <ul class="footer-links">
              <li><a href="${page('index.html')}"><i class="bi bi-chevron-right"></i> Home</a></li>
              <li><a href="${page('about.html')}"><i class="bi bi-chevron-right"></i> About Us</a></li>
              <li><a href="${page('services.html')}"><i class="bi bi-chevron-right"></i> Our Services</a></li>
              <li><a href="${page('gallery.html')}"><i class="bi bi-chevron-right"></i> Photo Gallery</a></li>
              <li><a href="${page('pricing.html')}"><i class="bi bi-chevron-right"></i> Packages</a></li>
              <li><a href="${page('blog.html')}"><i class="bi bi-chevron-right"></i> News &amp; Tips</a></li>
              <li><a href="${page('contact.html')}"><i class="bi bi-chevron-right"></i> Contact Us</a></li>
            </ul>
          </div>

          <div class="col-lg-3 col-md-6 col-6">
            <h4 class="footer-title">Our Services</h4>
            <ul class="footer-links">
              <li><a href="${page('pages/services/wedding-stage.html')}"><i class="bi bi-chevron-right"></i> Wedding Stage</a></li>
              <li><a href="${page('pages/services/traditional-pandal.html')}"><i class="bi bi-chevron-right"></i> Traditional Pandal</a></li>
              <li><a href="${page('pages/services/reception-decoration.html')}"><i class="bi bi-chevron-right"></i> Reception Decoration</a></li>
              <li><a href="${page('pages/services/outdoor-events.html')}"><i class="bi bi-chevron-right"></i> Outdoor Event Tents</a></li>
              <li><a href="${page('pages/services/birthday-decoration.html')}"><i class="bi bi-chevron-right"></i> Birthday Events</a></li>
              <li><a href="${page('pages/services/corporate-events.html')}"><i class="bi bi-chevron-right"></i> Corporate Setup</a></li>
            </ul>
          </div>

          <div class="col-lg-3 col-md-6">
            <h4 class="footer-title">Contact Us</h4>
            <div class="footer-contact-item">
              <i class="bi bi-geo-alt-fill" aria-hidden="true"></i>
              <span>48, Grand Trunk Road, Anna Nagar, Chennai - 600040</span>
            </div>
            <div class="footer-contact-item">
              <i class="bi bi-telephone-fill" aria-hidden="true"></i>
              <span><a href="tel:+919840123456">+91 98401 23456</a><br><a href="tel:+919840123457">+91 98401 23457</a></span>
            </div>
            <div class="footer-contact-item">
              <i class="bi bi-envelope-fill" aria-hidden="true"></i>
              <span><a href="mailto:info@utsavdecor.com">info@utsavdecor.com</a></span>
            </div>
            <div class="footer-contact-item">
              <i class="bi bi-clock-fill" aria-hidden="true"></i>
              <span>Mon - Sat: 9:00 AM - 8:30 PM<br>Sun: 10:00 AM - 5:00 PM</span>
            </div>
          </div>
        </div>

        <div class="footer-bottom">
          <div class="row align-items-center gy-2">
            <div class="col-md-6 text-center text-md-start">
              &copy; 2026 UTSAV Stage, Tent &amp; Pandal Contractor. All Rights Reserved.
            </div>
            <div class="col-md-6 text-center text-md-end">
              <a href="${page('coming-soon.html')}" class="me-3">Coming Soon</a>
              <a href="${page('404.html')}">404 Error</a>
            </div>
          </div>
        </div>
      </div>
    </footer>
    <a href="#top" class="back-to-top utsav-back-to-top" aria-label="Scroll to top">
      <i class="bi bi-arrow-up" aria-hidden="true"></i>
    </a>`;

  if (document.querySelector('.utsav-footer')) {
    return;
  }

  document.body.insertAdjacentHTML('beforeend', footer);
})();
