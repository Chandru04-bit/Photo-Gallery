# UTSAV - Premium Stage, Tent & Pandal Contractor Website Template

A commercial-grade, multi-page website template built for **Stage, Tent & Pandal Contractors**. Tailored for wedding stage decoration, traditional marriage pandals, outdoor all-weather German tents, luxury reception staging, floral artistry, and corporate event setups.

---

## 1. Project Overview

- **Project Name:** UTSAV - Stage, Tent & Pandal Contractor
- **Website Type:** Multi-page commercial website template
- **Design Aesthetic:** Festive, elegant, traditional, and modern royal Indian celebration style with deep maroon and royal gold accents.
- **Technology Stack:** HTML5, CSS3, Vanilla JavaScript, Bootstrap 5.3.3, Bootstrap Icons 1.11.3.
- **Admin/User Dashboard:** None (Strictly excluded as per requirements).

---

## 2. Complete Folder & File Structure

```text
stage-tent-contractor/
│
├── index.html                           # Home 1 - Main Homepage (Grand Mandap & Pandal)
├── home-2.html                          # Home 2 - Alternative Homepage (Split Screen Modern)
├── about.html                           # About Us (Heritage, Mission, Team, Achievements)
├── services.html                        # Services Listing (12 Full Event Categories)
├── service-details.html                 # Service Details Master Layout & Facilities
├── gallery.html                         # Filterable Photo Gallery with Lightbox Modal
├── pricing.html                         # Pricing Packages (Basic, Standard, Premium, Custom)
├── blog.html                            # Blog Listing Page (6 Curated Articles)
├── blog-details.html                    # Blog Details Master Layout
├── contact.html                         # Contact Us with Form, Info Cards, Google Maps Embed
├── get-quote.html                       # Detailed Event Enquiry & Quotation Form
├── register.html                        # New Client & Event Planner Registration
├── 404.html                             # Custom 404 Error Page
├── coming-soon.html                     # Coming Soon Page with Live Countdown Timer
│
├── pages/
│   ├── services/
│   │   ├── wedding-stage.html           # Wedding Stage Decoration Details
│   │   ├── traditional-pandal.html      # Traditional Marriage Pandal Details
│   │   ├── reception-decoration.html    # Reception Stage Decoration Details
│   │   ├── engagement-decoration.html   # Engagement Decoration Details
│   │   ├── birthday-decoration.html     # Birthday Party Setup Details
│   │   ├── corporate-events.html        # Corporate Event Setup Details
│   │   ├── outdoor-events.html          # Outdoor German Tent Canopy Details
│   │   └── floral-decoration.html       # Exotic Floral Decoration Details
│   │
│   └── blogs/
│       ├── wedding-decoration-ideas.html    # Latest Wedding Stage Decoration Ideas
│       ├── pandal-decoration-trends.html    # Traditional Pandal Decoration Trends
│       ├── outdoor-event-ideas.html         # Outdoor Wedding & German Tent Guide
│       ├── floral-decoration-tips.html      # Floral Decoration & Fresh Bloom Care Tips
│       ├── stage-lighting-ideas.html        # Stage Lighting Ideas for Evening Celebrations
│       └── wedding-planning-guide.html      # Complete Wedding Planning & Decor Guide
│
├── assets/
│   ├── css/
│   │   ├── bootstrap.min.css            # Bootstrap 5.3.3 Core Framework
│   │   ├── bootstrap-icons.css          # Bootstrap Icons 1.11.3 Styles
│   │   ├── style.css                    # Main Custom Stylesheet
│   │   ├── responsive.css               # Multi-Device Responsive Tweaks
│   │   ├── animations.css               # Scroll Reveals, Keyframes & Glows
│   │   ├── dark-mode.css                # Royal Festive Dark Mode Theme
│   │   └── rtl.css                      # Bidirectional RTL / LTR Layout Support Stylesheet
│   │
│   ├── js/
│   │   ├── bootstrap.bundle.min.js      # Bootstrap 5 JS Bundle with Popper
│   │   ├── main.js                      # Sticky Nav, Back to Top, Dark Mode Toggle
│   │   ├── navigation.js                # Active Route Highlighting, Mobile Collapse
│   │   ├── gallery.js                   # Category Filtering, Fullscreen Lightbox
│   │   ├── forms.js                     # URL Pre-selection, Password Toggle
│   │   ├── validation.js                # Client-Side Form Validation & Feedback
│   │   └── animations.js                # IntersectionObserver, Counters, Countdown
│   │
│   ├── images/
│   │   ├── logo/                        # SVG Logos (Default, White, Royal Gold)
│   │   ├── favicon/                     # Favicons (.svg, .ico, 32x32.png, apple-touch)
│   │   ├── banners/                     # Hero & Page Header Backgrounds
│   │   ├── about/                       # Company Story, Experience & Team Photos
│   │   ├── services/                    # 12 Service Card Cover Photos
│   │   ├── gallery/                     # Curated Event Photography Subfolders
│   │   │   ├── wedding-stage/
│   │   │   ├── traditional-pandal/
│   │   │   ├── reception/
│   │   │   ├── engagement/
│   │   │   ├── birthday/
│   │   │   ├── corporate/
│   │   │   └── outdoor-events/
│   │   ├── testimonials/                # Client Reviewer Avatars
│   │   ├── blog/                        # 6 Article Featured Banners
│   │   └── backgrounds/                 # Subtle Mandap Pattern SVG
│   │
│   └── fonts/                           # Bootstrap Icons WOFF/WOFF2 Webfonts
│
└── README.md
```

---

## 3. Design System & Color Palette

| Color Name | Hex Code | Purpose |
| :--- | :--- | :--- |
| **Deep Maroon** | `#5B1425` | Primary Brand Color, Badges, Dark Accents |
| **Royal Gold** | `#C6A15B` | Accent Color, Primary CTAs, Borders, Glows |
| **Warm Cream** | `#F8F2E8` | Section Backgrounds, Alternating Rows |
| **Ivory White** | `#FFFDF8` | Card Backgrounds, Page Canvas |
| **Dark Charcoal** | `#242020` | High-Contrast Typography, Dark Elements |

### Typography
- **Headings:** `'Playfair Display', Georgia, serif`
- **Body:** `'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`

---

## 4. Key Functional Features

1. **Dual Homepage Layouts:**
   - `index.html`: Grand royal mandap hero, trusted stats ribbon, 6-card service grid, 5-step work process, testimonial slider, featured pricing.
   - `home-2.html`: Split-screen hero layout, quick highlight ribbon, event statistics grid, signature wedding showcase, visual masonry.
2. **Interactive Photo Gallery (`gallery.html`):**
   - Instant category filtering (All, Wedding Stage, Traditional Pandal, Reception, Engagement, Birthday, Corporate, Outdoor).
   - Fullscreen Lightbox modal with next/previous navigation and keyboard support (`Escape`, `ArrowLeft`, `ArrowRight`).
3. **Transparent Pricing Packages (`pricing.html`):**
   - 4 tiers: Basic (₹35k), Standard (₹75k), Premium (₹1.5L), Custom Quote.
   - One-click navigation to `get-quote.html` with selected package pre-selected via URL query parameters (`?package=standard`).
   - Detailed side-by-side feature comparison table and FAQs.
4. **Comprehensive Quote Questionnaire (`get-quote.html`):**
   - Event types, guest counts, budget tiers, decor element checkboxes, and date validation.
5. **Interactive Client Feedback & Form Validation (`validation.js`):**
   - Real-time client-side validation for phone, email, and required inputs with transparent demo feedback.
6. **Live Countdown Timer (`coming-soon.html`):**
   - Real-time animated countdown timer (Days, Hours, Minutes, Seconds).
7. **Dark Mode Integration (`dark-mode.css`):**
   - Persistent theme switch (saved to `localStorage`) with deep royal maroon and gold highlights.
---

## 5. How to Run Locally

You can open the website directly using any web browser:
1. Double click on `index.html` to open in Google Chrome, Microsoft Edge, Firefox, or Safari.
2. Or serve via any local static server:
   ```bash
   python -m http.server 8000
   ```
   Then open `http://localhost:8000` in your browser.

---

## 6. Responsive Viewport Verification

Tested and validated across standard responsive breakpoints without horizontal scroll or truncated content:
- **320px – 375px:** iPhone SE / small Android devices
- **390px – 414px:** Modern smartphones (iPhone 14/15, Galaxy S series)
- **768px – 820px:** iPads and mid-sized tablets
- **1024px – 1280px:** Small laptops and iPad Pro landscape
- **1440px – 1920px:** High-resolution desktops and ultrawide monitors
