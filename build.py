#!/usr/bin/env python3
"""
Static site generator for Universal Relocations (migrated off WordPress/Elementor).
Run:  python3 build.py
Output: writes .html files into this directory, ready for `vercel deploy`.
"""
import os, pathlib

ROOT = pathlib.Path(__file__).parent
IMG = "https://www.universalrelocations.com/wp-content/uploads"  # existing hosted assets
LOGO = f"{IMG}/2023/12/Universal-Logo-BLUE.png"   # real brand logo (navy) for white header
LOGO_WHITE = "/assets/logo-white.png"             # white reversed wordmark for navy footer

WA = "https://api.whatsapp.com/send/?phone=12017874088&text&type=phone_number&app_absent=0"

# Route-finder countries (name, slug). Hubs where Universal has offices:
COUNTRIES = [
    ("India", "india"), ("United Kingdom", "uk"), ("United States", "usa"),
    ("Canada", "canada"), ("UAE", "uae"), ("Saudi Arabia", "saudi-arabia"),
    ("Mexico", "mexico"), ("Germany", "germany"), ("Philippines", "philippines"),
    ("Japan", "japan"), ("Australia", "australia"), ("New Zealand", "new-zealand"),
    ("France", "france"), ("Italy", "italy"),
]
ROUTE_OPTIONS = "".join(f'<option value="{s}">{n}</option>' for n, s in COUNTRIES)
HUB_COUNTRIES = {"usa", "india", "uae"}

# Hero background video (plane flying) — generated from the hero montage, hosted locally.
HERO_VIDEO = "/assets/hero.mp4"

def _asset_ver():
    """Content hash of ALL assets for cache-busting so deploys never serve stale files."""
    import hashlib
    h = hashlib.md5()
    adir = ROOT / "assets"
    if adir.exists():
        for p in sorted(adir.glob("*")):
            if p.is_file():
                h.update(p.read_bytes())
    return h.hexdigest()[:8]
ASSET_VER = _asset_ver()

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

# ---- Footer icons ----
IC_PHONE = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1.9.3 1.8.6 2.7a2 2 0 0 1-.5 2.1L7.8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.5 2.7.6A2 2 0 0 1 22 16.9z"/></svg>'
IC_MAIL = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 6 10-6"/></svg>'
IC_PIN = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'

_SOC = [
  ("Facebook", "https://facebook.com/universalrelocations", '<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12a12 12 0 1 0-13.9 11.9v-8.4H7.1V12h3V9.4c0-3 1.8-4.6 4.5-4.6 1.3 0 2.6.2 2.6.2v2.9h-1.5c-1.4 0-1.9.9-1.9 1.8V12h3.3l-.5 3.5h-2.8v8.4A12 12 0 0 0 24 12z"/></svg>'),
  ("X", "https://twitter.com/Universal_Relo", '<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor"><path d="M18.2 2.2h3.3l-7.2 8.3L23 21.8h-6.6l-5.2-6.8-6 6.8H1.9l7.7-8.8L1.3 2.2H8l4.7 6.2 5.5-6.2zm-1.2 17.6h1.8L7.1 4.1H5.2l11.8 15.7z"/></svg>'),
  ("Instagram", "https://instagram.com/universalrelocationsinc", '<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4a3.7 3.7 0 0 1-1.4-.9 3.7 3.7 0 0 1-.9-1.4c-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.2A6.6 6.6 0 1 0 18.6 12 6.6 6.6 0 0 0 12 5.4zm0 10.9A4.3 4.3 0 1 1 16.3 12 4.3 4.3 0 0 1 12 16.3zm6.8-11.2a1.5 1.5 0 1 1-1.5-1.5 1.5 1.5 0 0 1 1.5 1.5z"/></svg>'),
  ("YouTube", "https://www.youtube.com/channel/UCSt03dR9jOcvrHaV22CLH0Q", '<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.3 3.6-6.3 3.6z"/></svg>'),
  ("WhatsApp", WA, '<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163a11.867 11.867 0 0 1-1.587-5.945C.16 5.335 5.495 0 12.05 0a11.817 11.817 0 0 1 8.413 3.488 11.824 11.824 0 0 1 3.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 0 1-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.82 9.82 0 0 0 1.511 5.26l-.999 3.648 3.742-.981z"/></svg>'),
]
FOOTER_SOCIAL = "".join(
    f'<a class="soc" href="{u}" aria-label="{n}" target="_blank" rel="noopener">{s}</a>'
    for n, u, s in _SOC)

FOOTER_CONTACT = f"""
          <div class="footer-contact">
            <a class="ci" href="tel:+18883237356"><span class="ci-ic">{IC_PHONE}</span><span><b>USA</b>1-888-323-7356</span></a>
            <a class="ci" href="tel:+18001037356"><span class="ci-ic">{IC_PHONE}</span><span><b>India</b>1-800-103-7356</span></a>
            <a class="ci" href="tel:+800137356"><span class="ci-ic">{IC_PHONE}</span><span><b>UAE</b>800-13-7356</span></a>
            <a class="ci" href="mailto:contact@universalrelocations.com"><span class="ci-ic">{IC_MAIL}</span><span><b>Email</b>contact@universalrelocations.com</span></a>
          </div>"""

FOOTER = f"""
  <footer class="site-footer">
    <div class="footer-cta">
      <div class="container">
        <div class="footer-cta-text">
          <h3>Ready to plan your move?</h3>
          <p>Get a free, no-obligation estimate in minutes — or talk to a move manager.</p>
        </div>
        <div class="footer-cta-actions">
          <a class="btn btn-primary" href="/assistant/">Get an Instant Estimate</a>
          <a class="btn btn-outline" href="/contact-us/">Contact Us</a>
        </div>
      </div>
    </div>
    <div class="footer-top">
      <div class="container footer-grid">
        <div class="footer-brand">
          <div class="footer-brandname">Universal Relocations</div>
          <p>The one-stop relocation service for international, interstate and intrastate shipping needs. Established 1998, moving families and businesses across the world with precision and care.</p>
          {FOOTER_CONTACT}
          <div class="footer-social">{FOOTER_SOCIAL}</div>
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
        <span>Licensed &amp; bonded NVOCC · FMC-OTI No. NF025083</span>
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
  <link rel="stylesheet" href="/assets/styles.css?v={ASSET_VER}">
</head>
<body>
{TOPBAR}
{HEADER}
{body}
{FOOTER}
<script src="/assets/script.js?v={ASSET_VER}"></script>
<script src="/assets/assistant.js?v={ASSET_VER}" defer></script>
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
    return (f'<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
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
          <a class="tel" href="tel:{tel}"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1.9.3 1.8.6 2.7a2 2 0 0 1-.5 2.1L7.8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.5 2.7.6A2 2 0 0 1 22 16.9z"/></svg><span>{tel}</span></a>
        </div>
      </div>
    </div>"""

def review(text, who, src="Google Review"):
    return f"""<div class="review">
      <div class="stars">★★★★★</div>
      <p>“{text}”</p>
      <div class="who">{who}</div><div class="src">{src}</div>
    </div>"""

AFFIL_LOGOS = "".join(f'<img height="64" src="{IMG}/2026/10/{n}" alt="{a}">' for n, a in [
    ("01-fidi.png", "FIDI"), ("02-faim.png", "FAIM"), ("03-iamx.png", "IAM"),
    ("05-paima.png", "PAIMA"), ("06-ipata.png", "IPATA"), ("07-ara.png", "ARA"),
    ("09-fmc.png", "FMC"), ("10-iso-9001.png", "ISO 9001")])
PRESS_LOGOS = "".join(f'<img height="42" src="{IMG}/2025/08/{n}" alt="{a}">' for n, a in [
    ("Forbes.png", "Forbes"), ("Fox-News.png", "Fox News"), ("Yahoo.png", "Yahoo Finance"),
    ("MSN.png", "MSN"), ("Associated-Press.png", "Associated Press"),
    ("Bussiness-Insider.png", "Business Insider"), ("Gulf-News.png", "Gulf News"),
    ("Khaleej-Times.png", "Khaleej Times")])

HOME_BODY = f"""
<section class="hello-hero">
  <video class="hero-video" autoplay muted loop playsinline preload="metadata" poster="/assets/hero-bg.jpg?v={ASSET_VER}">
    <source src="{HERO_VIDEO}?v={ASSET_VER}" type="video/mp4">
  </video>
  <div class="container hello-inner">
    <h1 class="hello-title" id="hero-rotate"><span class="hr-text">Hello,</span><span class="hr-cursor">|</span></h1>
    <p class="hello-sub">Whatever you're moving, wherever to — just tell us, and start here.</p>

    <form class="hero-prompt" id="hero-prompt-form">
      <input id="hero-prompt-input" type="text" autocomplete="off" aria-label="Describe your move in your own words">
      <div class="hero-prompt-actions">
        <button type="button" class="hp-icon" id="hp-mic" aria-label="Voice input">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0014 0M12 17v4"/></svg>
        </button>
        <button type="submit" class="hp-go" aria-label="Start">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </button>
      </div>
    </form>

    <div class="hero-suggest">
      <span class="hs-label">Try:</span>
      <button class="hs-chip" data-prompt="I want to move my 3 bedroom apartment from New York to Delhi">Move a 3-bedroom, New York → Delhi</button>
      <button class="hs-chip" data-prompt="I want to ship 5 boxes of 25 kg each from Chennai to San Francisco">Ship 5 boxes, Chennai → San Francisco</button>
      <button class="hs-chip" data-prompt="I want to move my car from Dubai to Toronto">Move a car, Dubai → Toronto</button>
      <button class="hs-chip" data-prompt="How much will it cost to move 10 boxes from Dallas to Abu Dhabi">10 boxes, Dallas → Abu Dhabi</button>
    </div>

    <div class="hello-badges">
      <div class="hb"><b>28+</b><span>Years of experience</span></div>
      <div class="hb"><b>190+</b><span>Countries covered</span></div>
      <div class="hb"><b>4.5★</b><span>Trustpilot · 2000+ reviews</span></div>
      <div class="hb"><b>FMC</b><span>Licensed &amp; bonded NVOCC</span></div>
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

<!-- Route finder -->
<section class="section section-soft">
  <div class="container text-center">
    <span class="eyebrow">Find Your Route</span>
    <h2 class="section-title">Where are you moving?</h2>
    <p class="section-intro">Pick your origin and destination to see a dedicated moving guide, timelines and services for your exact route.</p>
    <form id="route-form" class="route-finder">
      <div class="route-field">
        <label>Moving from</label>
        <select id="route-from" required><option value="" disabled selected>Select country…</option>{ROUTE_OPTIONS}</select>
      </div>
      <span class="route-arrow" aria-hidden="true">→</span>
      <div class="route-field">
        <label>Moving to</label>
        <select id="route-to" required><option value="" disabled selected>Select country…</option>{ROUTE_OPTIONS}</select>
      </div>
      <button type="submit" class="btn btn-primary">Find Your Route</button>
    </form>
    <p id="route-error" class="route-error" hidden>Please choose two different countries.</p>
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
      <div class="p"><div class="p-ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8M8 10h2M12 10h2M16 10h0M8 14h2M12 14h2M16 14h0M8 18h2M12 18h2M16 18h0"/></svg></div><h4>Moving Calculator</h4><p>Calculate the volume of your items &amp; get an instant quote.</p><a class="btn btn-primary" style="margin-top:14px" href="https://portal.universalrelocations.com/moving-calculator/">Calculate Now</a></div>
      <div class="p"><div class="p-ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 8.6 8.6 0 0 1-3.8-.8L3 20l1-4a8.4 8.4 0 0 1-.8-3.6A8.4 8.4 0 0 1 12 3.5a8.4 8.4 0 0 1 9 8z"/></svg></div><h4>Talk to a Move Manager</h4><p>Get in touch with our move consultants for personal guidance.</p><a class="btn btn-ghost" style="margin-top:14px" href="/contact-us/">Contact Us</a></div>
      <div class="p"><div class="p-ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="14" height="14" rx="2"/><path d="M16 10l6-3v10l-6-3z"/></svg></div><h4>Video Pre-Move Survey</h4><p>Pick a day and time to join our surveyor on a video call for a complimentary estimate.</p><a class="btn btn-ghost" style="margin-top:14px" href="https://calendly.com/UniversalrelocationsOfficial">Schedule a Call</a></div>
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
    <div class="logos-slider">
      <div class="logos-track">{AFFIL_LOGOS}{AFFIL_LOGOS}</div>
    </div>
    <h2 class="section-title" style="margin-top:56px">As Seen On</h2>
    <div class="logos-slider">
      <div class="logos-track press">{PRESS_LOGOS}{PRESS_LOGOS}</div>
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

ASSISTANT_BODY = """
<section class="chat-page">
  <div class="chat-wrap">
    <div class="chat-head">
      <h1>Universal Relocations Move Assistant</h1>
      <p>Tell me about your move and I'll get you an instant estimate.</p>
    </div>
    <div class="chat-stream" id="chat-stream"></div>
    <div class="chat-inputbar" id="chat-inputbar"></div>
  </div>
</section>
"""

if __name__ == "__main__":
    import pages  # the rest of the content pages
    write("assistant", page(
        "Move Assistant | Universal Relocations",
        ASSISTANT_BODY,
        "Plan your move and get an instant estimate with the Universal Move Assistant.",
    ))
    write("index", page(
        "Universal Relocations | Your Trusted Expert Moving Partner",
        HOME_BODY,
        "Universal Relocations offers expert moving services tailored to your needs. Hassle-free international, interstate and intrastate moving with a dedicated team of professional movers.",
        "https://www.universalrelocations.com",
    ))
    pages.build(globals())
    print("\\nDone.")
