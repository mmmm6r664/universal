#!/usr/bin/env python3
"""
Static site generator for Universal Relocations (migrated off WordPress/Elementor).
Run:  python3 build.py
Output: writes .html files into this directory, ready for `vercel deploy`.
"""
import os, pathlib

ROOT = pathlib.Path(__file__).parent
IMG = "https://www.universalrelocations.com/wp-content/uploads"  # existing hosted assets
LOGO = f"{IMG}/2023/12/Universal-Logo-BLUE.png"
LOGO_WHITE = f"{IMG}/2024/01/UR-LOGO-1-1200x286.png"

WA = "https://api.whatsapp.com/send/?phone=12017874088&text&type=phone_number&app_absent=0"

# ---------------------------------------------------------------------------
# Shared TOP BAR + HEADER
# ---------------------------------------------------------------------------
TOPBAR = f"""
  <div class="topbar">
    <div class="container">
      <div class="topbar-left">
        <a href="mailto:contact@universalrelocations.com">contact@universalrelocations.com</a>
      </div>
      <div class="topbar-right">
        <span class="phone"><img src="{IMG}/2024/02/united-states-flag-icon-1.png" alt="USA">1-888-323-7356</span>
        <span class="phone"><img src="{IMG}/2024/02/india-flag-icon-1.png" alt="India">1-800-103-7356</span>
        <span class="phone"><img src="{IMG}/2024/06/images-1.png" alt="UAE">800-13-7356</span>
        <span class="socials">
          <a href="https://portal.universalrelocations.com/moving-calculator/">Moving Calculator</a>
          <a href="/faq/">FAQ</a>
          <a href="/blogs/">Blogs</a>
        </span>
      </div>
    </div>
  </div>
"""

def nav_item(label, href, children=None):
    if not children:
        return f'<li><a href="{href}">{label}</a></li>'
    sub = "".join(f'<li><a href="{c[1]}">{c[0]}</a></li>' for c in children)
    return (f'<li class="has-dropdown"><a href="{href}">{label}<i class="caret"></i></a>'
            f'<ul class="dropdown">{sub}</ul></li>')

NAV = "".join([
    nav_item("Home", "/"),
    nav_item("About us", "/about-us/", [
        ("Company", "/company/"),
        ("Corporate Social Responsibility", "/corporate-social-responsibility/"),
        ("Career", "/career/"),
        ("Company News", "/company-news/"),
    ]),
    nav_item("Hubs", "#", [
        ("USA", "/usa/"),
        ("India", "/india/"),
        ("UAE", "/uae/"),
    ]),
    nav_item("Destinations", "/shipping-worldwide/", [
        ("Moving to Africa", "/moving-to-africa/"),
        ("Moving to Asia", "/moving-to-asia/"),
        ("Moving to Europe", "/moving-to-europe/"),
        ("Moving to North America", "/moving-to-north-america/"),
        ("Moving to Oceania", "/moving-to-oceania/"),
        ("Moving to South America", "/moving-to-south-america/"),
    ]),
    nav_item("Services", "/services/", [
        ("Groupage Solution", "/services/groupage-solution/"),
        ("Baggage Shipping", "/services/baggage-shipping/"),
        ("Transit Insurance", "/services/insurance/"),
        ("Storage &amp; Warehousing", "/services/storage/"),
        ("Pet Relocation", "/services/pet-relocations/"),
        ("International Relocation", "/services/international/"),
        ("Intrastate Relocation", "/services/intrastate/"),
        ("Fine Art Relocation", "/services/fine-art-relocations/"),
        ("Hospitality Logistics", "/services/hospitality-relocations/"),
        ("Corporate Relocation", "/services/corporate-relocation/"),
        ("Auto Shipping", "/services/auto-shipping/"),
    ]),
    nav_item("Resources", "/resources/", [
        ("Blogs", "/blogs/"),
        ("FAQ", "/faq/"),
        ("File a Claim", "/file-a-claim/"),
        ("Moving Checklist", "/moving-check-list/"),
        ("Moving Referral", "/referral/"),
        ("Packing Tips", "/packing-tips/"),
        ("Moving Terms", "/moving-terms/"),
        ("Shipping Terms", "/shipping-terms/"),
    ]),
    nav_item("Contact us", "/contact-us/"),
])

HEADER = f"""
  <header class="site-header">
    <div class="container nav">
      <a class="nav-logo" href="/"><img src="{LOGO}" alt="Universal Relocations"></a>
      <ul class="nav-menu">{NAV}</ul>
      <div class="nav-cta">
        <a class="btn btn-primary" href="/contact-us/" data-open-assistant>Get a Quote</a>
        <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>
"""

# ---------------------------------------------------------------------------
# Shared FOOTER
# ---------------------------------------------------------------------------
def flink(label, href): return f'<li><a href="{href}">{label}</a></li>'

FOOTER = f"""
  <footer class="site-footer">
    <div class="footer-top">
      <div class="container footer-grid">
        <div>
          <div class="footer-logo"><img src="{LOGO}" alt="Universal Relocations"></div>
          <p>The one-stop relocation service for international, interstate and intrastate shipping needs. Established 1998, moving families and businesses across the world with precision and care.</p>
          <p class="fmc-note">MC #836909-C &nbsp; New Jersey #39PC00115200 &nbsp; TxDMV #007065281C<br>
          FMC OTI #NF025083 &nbsp; US DOT #2428388 &nbsp; CA #662949</p>
        </div>
        <div>
          <h5>Terms &amp; Conditions</h5>
          <ul>
            {flink("Anti-Bribery &amp; Code of Conduct", "/anti-bribery-code-of-conduct/")}
            {flink("Cancellation &amp; Refund Policy", "/cancel-and-refund-policy/")}
            {flink("Cookies Policy", "/universal-relocations-cookies-policy/")}
            {flink("Data Policy", "/data-policy/")}
            {flink("Environmental Policy", "/environmental-policy/")}
            {flink("Privacy Policy", "/privacy-policy/")}
            {flink("Terms &amp; Conditions", "/terms-and-condition/")}
            {flink("SMS Terms of Service", "/sms-terms-of-service/")}
            {flink("Credit Application", "/credit-application/")}
            {flink("Supplier Registration", "/vendor/")}
          </ul>
        </div>
        <div>
          <h5>Ocean Shipping</h5>
          <ul>
            {flink("Bill Of Lading", "/bill-of-lading/")}
            {flink("FMC Rules &amp; Tariff", "/fmc-rules-tariff/")}
            {flink("File A Claim", "/file-a-claim/")}
            {flink("Historic FMC Rules &amp; Tariff", "/historic-fmc-rules-tariff/")}
          </ul>
          <h5 style="margin-top:26px">Resources</h5>
          <ul>
            {flink("Moving Checklist", "/moving-check-list/")}
            {flink("Packing Tips", "/packing-tips/")}
            {flink("Moving Terms", "/moving-terms/")}
          </ul>
        </div>
        <div>
          <h5>Our Locations</h5>
          <div class="footer-locations">
            <div>
              <h6><a href="/usa/">USA</a></h6>
              <ul>
                {flink("New Jersey", "/usa/locations/new-jersey/")}
                {flink("Maryland", "/usa/locations/maryland/")}
                {flink("Georgia", "/usa/locations/georgia/")}
                {flink("Texas", "/usa/locations/texas/")}
                {flink("California", "/usa/locations/california/")}
              </ul>
            </div>
            <div>
              <h6><a href="/india/">India</a></h6>
              <ul>
                {flink("Chennai", "/india/locations/chennai/")}
                {flink("Bangalore", "/india/locations/bangalore/")}
                {flink("Hyderabad", "/india/locations/hyderabad/")}
                {flink("Mumbai", "/india/locations/mumbai/")}
                {flink("New Delhi", "/india/locations/delhi/")}
              </ul>
            </div>
            <div>
              <h6><a href="/uae/">UAE</a></h6>
              <ul>{flink("Dubai", "/uae/locations/dubai/")}</ul>
            </div>
          </div>
          <p class="fmc-note">U.S. federal law (the Shipping Act of 1984) requires Ocean Transportation Intermediaries to be licensed and bonded. Universal Relocations Inc. is licensed by the US Federal Maritime Commission — FMC-OTI No. NF025083.</p>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <span>© Copyright 2026. All rights reserved. Universal Relocations.</span>
        <span>
          <a href="https://facebook.com/universalrelocations">Facebook</a> &nbsp;·&nbsp;
          <a href="http://Twitter.com/Universal_Relo">Twitter</a> &nbsp;·&nbsp;
          <a href="http://instagram.com/universalrelocationsinc">Instagram</a> &nbsp;·&nbsp;
          <a href="https://www.youtube.com/channel/UCSt03dR9jOcvrHaV22CLH0Q">YouTube</a>
        </span>
      </div>
    </div>
  </footer>
  <a class="wa-float" href="{WA}" aria-label="WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163a11.867 11.867 0 01-1.587-5.945C.16 5.335 5.495 0 12.05 0a11.817 11.817 0 018.413 3.488 11.824 11.824 0 013.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 01-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.82 9.82 0 001.511 5.26l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.52.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.5-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
  </a>
"""

# ---------------------------------------------------------------------------
# Page wrapper
# ---------------------------------------------------------------------------
def page(title, body, desc="", canonical=""):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  {f'<link rel="canonical" href="{canonical}">' if canonical else ''}
  <link rel="icon" href="{IMG}/2024/01/Universal-Round-Logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/styles.css">
</head>
<body>
{TOPBAR}
{HEADER}
{body}
{FOOTER}
<script src="/assets/script.js"></script>
<script src="/assets/assistant.js" defer></script>
</body>
</html>
"""

def write(path, html):
    """path like 'index' or 'company/index' -> writes <path>.html style dir/index.html"""
    if path == "index":
        out = ROOT / "index.html"
    else:
        d = ROOT / path
        d.mkdir(parents=True, exist_ok=True)
        out = d / "index.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out.relative_to(ROOT))

# ---------------------------------------------------------------------------
# HOMEPAGE
# ---------------------------------------------------------------------------
def icon(name):
    paths = {
        "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 010 18M12 3a15 15 0 000 18"/>',
        "ship": '<path d="M3 14l1.5 6h15L21 14M5 14V7l7-3 7 3v7M9 9h6"/>',
        "bolt": '<path d="M13 2L3 14h7l-1 8 10-12h-7z"/>',
        "truck": '<path d="M1 3h15v13H1zM16 8h4l3 3v5h-7M5.5 19a2 2 0 100-4 2 2 0 000 4zM18.5 19a2 2 0 100-4 2 2 0 000 4z"/>',
        "shield": '<path d="M12 2l8 3v6c0 5-3.5 8.5-8 11-4.5-2.5-8-6-8-11V5z"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    }
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{paths[name]}</svg>')

def svc_card(title, text, href):
    return f"""<div class="svc">
      <h4>{title}</h4><p>{text}</p>
      <a class="more" href="{href}">View More →</a>
    </div>"""

def hub_card(name, text, href, tel, img):
    return f"""<div class="hub-card">
      <div class="img" style="background-image:url('{img}')"></div>
      <div class="body">
        <h3>{name}</h3><p>{text}</p>
        <div class="row">
          <a class="btn btn-ghost" href="{href}">Explore Hub</a>
          <span class="tel">{tel}</span>
        </div>
      </div>
    </div>"""

def review(text, who, src="Google Review"):
    return f"""<div class="review">
      <div class="stars">★★★★★</div>
      <p>“{text}”</p>
      <div class="who">{who}</div><div class="src">{src}</div>
    </div>"""

HOME_BODY = f"""
<section class="hero">
  <div class="container">
    <div class="hero-copy">
      <span class="eyebrow" style="color:var(--accent)">The One-Stop Relocation Service</span>
      <h1>Across Borders,<br>Beyond Boundaries.<br>Your Global Move Begins Here.</h1>
      <p>Expert international, interstate and intrastate moving tailored to you. From removals and logistics to customs clearance — we handle every detail so you can focus on your new chapter.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#" data-open-assistant>Get an Instant Estimate</a>
        <a class="btn btn-outline" href="https://calendly.com/UniversalrelocationsOfficial">Schedule a Video Survey</a>
      </div>
      <div class="hero-badges">
        <div class="hero-badge"><b>28+</b><span>Years of Experience</span></div>
        <div class="hero-badge"><b>190+</b><span>Countries Covered</span></div>
        <div class="hero-badge"><b>4.5★</b><span>Trustpilot (2000+ reviews)</span></div>
      </div>
    </div>

    <div class="quote-card">
      <h3>Get your free quote</h3>
      <p class="sub">Tell us about your move and we'll be in touch.</p>
      <form id="quote-form">
        <div class="quote-grid">
          <div class="field"><label>Moving From *</label><input required placeholder="City / Country"></div>
          <div class="field"><label>Moving To *</label><input required placeholder="City / Country"></div>
          <div class="field"><label>Move Date</label><input type="date"></div>
          <div class="field"><label>Move Size</label>
            <select><option value="">Select…</option><option>Baggage</option><option>Studio</option>
            <option>1 Bedroom</option><option>2 Bedroom</option><option>3 Bedroom</option><option>4+ Bedroom</option></select>
          </div>
          <div class="field full"><label>Name</label><input required placeholder="Your name"></div>
          <div class="field"><label>Email</label><input type="email" required placeholder="you@email.com"></div>
          <div class="field"><label>Phone</label><input type="tel" required placeholder="Phone"></div>
          <div class="consent full">
            <input type="checkbox" required id="sms">
            <label for="sms" style="font-weight:400">I consent to receive SMS messages from Universal Relocations about my quote and shipment updates. Frequency may vary; data rates may apply. Reply STOP to opt out. See our <a href="/privacy-policy/" style="color:var(--blue)">Privacy Policy</a> &amp; <a href="/terms-and-condition/" style="color:var(--blue)">Terms</a>.</label>
          </div>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
  </div>
</section>

<!-- Feature strip -->
<section class="section">
  <div class="container">
    <div class="text-center">
      <span class="eyebrow">Why Universal Relocations?</span>
      <h2 class="section-title">Relocate <span>With Ease</span></h2>
      <p class="section-intro">Established in 1998, we built our name on international moving — relocating corporate expatriates and diplomats across every business sector. Many of those first clients are still with us today.</p>
    </div>
    <div class="features" style="margin-top:44px">
      <div class="feature"><div class="ic">{icon('globe')}</div><h4>International Expertise</h4><p>Our seasoned experts bring a wealth of experience, ensuring that your move is handled with precision and care.</p></div>
      <div class="feature"><div class="ic">{icon('ship')}</div><h4>Global Network</h4><p>We understand the intricacies of each destination, ensuring a smooth transition and making you feel at home, no matter where you go.</p></div>
      <div class="feature"><div class="ic">{icon('bolt')}</div><h4>Innovation in Motion</h4><p>From state-of-the-art logistics to cutting-edge tracking technology, we embrace innovation to enhance your moving experience.</p></div>
    </div>
  </div>
</section>

<!-- Hubs -->
<section class="section section-soft">
  <div class="container text-center">
    <span class="eyebrow">Our Global Presence</span>
    <h2 class="section-title">Our Hubs Across the World</h2>
    <p class="section-intro">From local moves to international relocations, our global hubs provide trusted moving and relocation services across key destinations worldwide.</p>
    <div class="hubs">
      {hub_card("USA", "Reliable moving and relocation services for homes, families, and businesses across the United States.", "/usa/", "1-888-323-7356", f"{IMG}/2026/08/usa-hub.png")}
      {hub_card("UAE", "Expert moving and relocation solutions for individuals, families, and businesses across the UAE.", "/uae/", "800-13-7356", f"{IMG}/2026/08/UAE-Hub-Page.png")}
      {hub_card("India", "Trusted moving and relocation services across India, helping you move with confidence and ease.", "/india/", "1-800-103-7356", f"{IMG}/2026/08/India-Taj-Mahal-1.jpg.jpeg")}
    </div>
  </div>
</section>

<!-- Services -->
<section class="section">
  <div class="container text-center">
    <span class="eyebrow">What We Do</span>
    <h2 class="section-title">The “One-Stop” <span>Relocation Service</span></h2>
    <p class="section-intro">For international, interstate and intrastate shipping needs. Moving is more than changing locations — it's a life transition that deserves precision, care, and a touch of personalized service.</p>
    <div class="services-grid">
      {svc_card("International Relocation", "Hassle-free moves to any part of the world from the USA and India. We handle removals, logistics and customs clearance so you can focus on the journey.", "/services/international/")}
      {svc_card("Corporate Relocation", "Precise planning and expert logistics for seamless office and employee moves that minimize business disruption.", "/services/corporate-relocation/")}
      {svc_card("Pet Relocation", "Specialized, caring pet moving services — every detail tailored to your companion's comfort and a first-class trip to their next chapter.", "/services/pet-relocations/")}
      {svc_card("Groupage Solution", "Cost-effective, eco-friendly shared-container shipping. We consolidate shipments to optimize space and reduce your carbon footprint.", "/services/groupage-solution/")}
      {svc_card("Storage &amp; Warehousing", "State-of-the-art, secure storage with flexible short- and long-term options — your belongings' home away from home.", "/services/storage/")}
      {svc_card("Intra &amp; Interstate Move", "Comprehensive interstate and intrastate relocation — packing, loading and transportation handled by our experienced team.", "/services/intrastate/")}
    </div>
    <div style="margin-top:36px"><a class="btn btn-blue" href="/services/">View All Services</a></div>
  </div>
</section>

<!-- Move manager CTA -->
<section class="section section-navy">
  <div class="container">
    <div class="promise">
      <div class="p"><h4>Moving Calculator</h4><p>Calculate the volume of your items &amp; get an instant quote.</p><a class="btn btn-primary" style="margin-top:14px" href="https://portal.universalrelocations.com/moving-calculator/">Calculate Now</a></div>
      <div class="p"><h4>Talk to a Move Manager</h4><p>Get in touch with our move consultants for personal guidance.</p><a class="btn btn-ghost" style="margin-top:14px" href="/contact-us/">Contact Us</a></div>
      <div class="p"><h4>Video Pre-Move Survey</h4><p>Pick a day and time to join our surveyor on a video call for a complimentary estimate.</p><a class="btn btn-ghost" style="margin-top:14px" href="https://calendly.com/UniversalrelocationsOfficial">Schedule a Call</a></div>
    </div>
  </div>
</section>

<!-- Stats -->
<section class="section section-navy" style="padding-top:0">
  <div class="container">
    <div class="stats">
      <div class="stat"><b data-count="28" data-suffix="+">0</b><span>Years of Experience</span></div>
      <div class="stat"><b data-count="50" data-suffix="k+">0</b><span>Satisfied Clients</span></div>
      <div class="stat"><b data-count="190" data-suffix="+">0</b><span>Countries Covered</span></div>
      <div class="stat"><b data-count="2" data-suffix="MM+">0</b><span>Tons Moved</span></div>
    </div>
  </div>
</section>

<!-- Promise -->
<section class="section section-soft">
  <div class="container text-center">
    <span class="eyebrow">Why Choose Us</span>
    <h2 class="section-title">Move With Confidence</h2>
    <div class="promise" style="margin-top:40px">
      <div class="p"><h4>28 Years of Expertise</h4><p>Your journey, our legacy — nearly three decades of trusted moving experience.</p></div>
      <div class="p"><h4>Real-Time Tracking</h4><p>Door-to-door tracking so you can watch your journey unfold with confidence.</p></div>
      <div class="p"><h4>24/7 Online Support</h4><p>Your move, your time — online assistance available at every click.</p></div>
    </div>
  </div>
</section>

<!-- Reviews -->
<section class="section">
  <div class="container text-center">
    <span class="eyebrow">Rated 4.4 on Google · 4.5 on Trustpilot</span>
    <h2 class="section-title">What Our Customers Say</h2>
    <div class="reviews">
      {review("Professional, helpful and transparent in every step of our move. We had a great experience with Universal Relocations.", "Rohan Arora")}
      {review("Boxes were picked up on time and we were kept informed throughout. Items delivered on time with prompt responses to every query. Highly recommend for USA to India moves.", "Aarti Mehra")}
      {review("Everything went smoothly from pickup to delivery. The team kept us informed and all boxes reached in perfect condition. Definitely recommend.", "Ashish Chaudhary")}
    </div>
  </div>
</section>

<!-- Affiliations / press -->
<section class="section section-soft">
  <div class="container text-center">
    <span class="eyebrow">Our Affiliations</span>
    <h2 class="section-title">Accredited &amp; Trusted</h2>
    <div class="logos">
      <img src="{IMG}/2026/10/01-fidi.png" alt="FIDI">
      <img src="{IMG}/2026/10/02-faim.png" alt="FAIM">
      <img src="{IMG}/2026/10/03-iamx.png" alt="IAM">
      <img src="{IMG}/2026/10/05-paima.png" alt="PAIMA">
      <img src="{IMG}/2026/10/06-ipata.png" alt="IPATA">
      <img src="{IMG}/2026/10/07-ara.png" alt="ARA">
      <img src="{IMG}/2026/10/09-fmc.png" alt="FMC">
      <img src="{IMG}/2026/10/10-iso-9001.png" alt="ISO 9001">
    </div>
    <h2 class="section-title" style="margin-top:56px">As Seen On</h2>
    <div class="logos press">
      <img src="{IMG}/2025/08/Forbes.png" alt="Forbes">
      <img src="{IMG}/2025/08/Fox-News.png" alt="Fox News">
      <img src="{IMG}/2025/08/Yahoo.png" alt="Yahoo Finance">
      <img src="{IMG}/2025/08/MSN.png" alt="MSN">
      <img src="{IMG}/2025/08/Associated-Press.png" alt="Associated Press">
      <img src="{IMG}/2025/08/Bussiness-Insider.png" alt="Business Insider">
      <img src="{IMG}/2025/08/Gulf-News.png" alt="Gulf News">
      <img src="{IMG}/2025/08/Khaleej-Times.png" alt="Khaleej Times">
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# Interior page helpers
# ---------------------------------------------------------------------------
def page_hero(title, crumbs):
    trail = ' / '.join(f'<a href="{h}">{l}</a>' if h else l for l, h in crumbs)
    return f"""<section class="page-hero"><div class="container">
      <h1>{title}</h1><div class="crumbs">{trail}</div></div></section>"""

def interior(title, crumbs, inner, desc=""):
    body = page_hero(title, crumbs) + f'<section class="section"><div class="container">{inner}</div></section>'
    return page(f"{title} | Universal Relocations", body, desc)

if __name__ == "__main__":
    import pages  # the rest of the content pages
    write("index", page(
        "Universal Relocations | Your Trusted Expert Moving Partner",
        HOME_BODY,
        "Universal Relocations offers expert moving services tailored to your needs. Hassle-free international, interstate and intrastate moving with a dedicated team of professional movers.",
        "https://www.universalrelocations.com",
    ))
    pages.build(globals())
    print("\\nDone.")
