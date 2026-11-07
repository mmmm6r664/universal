"""Content + route pages for Universal Relocations. Imported by build.py."""

# Rich service content (title, lead paragraph, feature bullets)
SERVICES = {
    "international": ("International Relocation",
        "Whether you're moving for work, family, or adventure, our international relocation services ensure a hassle-free move to any part of the world from the USA and India. We handle everything from removals to logistics to customs clearance, so you can focus on the excitement of your new journey.",
        ["Door-to-door ocean & air freight", "Full customs documentation & clearance", "Export-grade packing & crating", "Destination delivery & unpacking"]),
    "corporate-relocation": ("Corporate Relocation",
        "We understand how tricky office and employee moves can be. With precise planning and expert logistics, our seamless transitions minimize business disruption, ensuring an efficient relocation experience tailored to your company's needs.",
        ["Dedicated move coordinator", "Employee & assignee moves", "IT & office equipment handling", "Flexible scheduling to limit downtime"]),
    "pet-relocations": ("Pet Relocation",
        "Your furry companions are family. Our specialized pet moving services ensure a safe journey for your pets, tailoring every detail to their comfort and happiness — because every pet deserves a first-class ticket to their next chapter.",
        ["IPATA-affiliated pet logistics", "Health certificates & import permits", "Airline-approved crates", "Door-to-door pet transport"]),
    "groupage-solution": ("Groupage Solution",
        "Moving just a few items? Unlock cost-effective, eco-friendly moving with our Groupage Service. We consolidate shipments to optimize container space and reduce your carbon footprint — a community of movers embracing a sustainable approach.",
        ["Shared-container shipping", "Lower cost for smaller loads", "Eco-friendly consolidation", "Regular sailing schedules"]),
    "storage": ("Storage &amp; Warehousing",
        "Secure your memories with our Storage and Warehousing solutions — where your belongings find a home away from home. Our state-of-the-art facilities offer more than storage; they provide peace of mind, with flexible short- and long-term options.",
        ["Climate-controlled facilities", "24/7 security & monitoring", "Short & long-term options", "Full inventory management"]),
    "intrastate": ("Intrastate &amp; Interstate Relocation",
        "Universal Relocations offers comprehensive interstate and intrastate relocation services, ensuring a smooth and stress-free move. Our experienced team handles every aspect of your relocation, from packing and loading to transportation.",
        ["Local & long-distance moves", "Professional packing & loading", "Licensed & insured transport", "Transparent, upfront pricing"]),
    "baggage-shipping": ("Baggage Shipping",
        "Affordable, reliable baggage and excess-luggage shipping for students, professionals and families. Send your boxes and bags ahead without airline excess-baggage fees, with full tracking from pickup to delivery.",
        ["Student & excess-baggage shipping", "Box-by-box pricing", "Pickup from your door", "End-to-end tracking"]),
    "insurance": ("Transit Insurance",
        "Protect what matters most. Our transit insurance options give you comprehensive coverage for your belongings throughout the journey, so you can move with complete peace of mind.",
        ["All-risk coverage options", "Simple valuation process", "Fast, fair claims handling", "Coverage for air & ocean transit"]),
    "fine-art-relocations": ("Fine Art Relocation",
        "Specialized handling for art, antiques and high-value items. Our fine-art teams use custom crating, climate control and white-glove handling to move your most precious pieces with museum-grade care.",
        ["Custom crating & packing", "Climate-controlled transport", "Condition reporting", "White-glove installation"]),
    "hospitality-relocations": ("Hospitality Logistics",
        "End-to-end logistics for hotels, resorts and hospitality projects — from FF&E (furniture, fixtures & equipment) procurement logistics to on-site delivery, storage and installation coordination.",
        ["FF&E logistics", "Project-based warehousing", "Consolidation & delivery", "On-site installation support"]),
    "auto-shipping": ("Auto Shipping",
        "Ship your car, motorcycle or vehicle safely across the country or overseas. We manage documentation, container or RoRo shipping, and destination clearance for a smooth vehicle relocation.",
        ["Container & RoRo shipping", "Domestic & international", "Full export documentation", "Insured vehicle transport"]),
}

SERVICE_ORDER = ["international", "corporate-relocation", "intrastate", "baggage-shipping",
                 "groupage-solution", "storage", "pet-relocations", "insurance",
                 "fine-art-relocations", "auto-shipping", "hospitality-relocations"]

# Simple route pages: slug -> (title, breadcrumb-trail, lead paragraph)
SIMPLE = {
    "about-us": ("About Us", "Established in 1998, Universal Relocations began by developing our international moving business — relocating corporate expatriates and diplomats across a wide range of sectors. Nearly three decades later, we're still moving families and businesses across the world with the same precision and care."),
    "company": ("Our Company", "At Universal Relocations, moving is more than changing locations; it's a life transition that deserves precision, care, and a touch of personalized service. As your global moving partner, we turn your international relocation into a seamless and memorable journey."),
    "corporate-social-responsibility": ("Corporate Social Responsibility", "We believe responsible business builds a better world. Our CSR commitments span sustainable shipping practices, community support and ethical operations across every hub we serve."),
    "career": ("Kick Start Your Career Journey", "Join a global team that moves lives for a living. Explore careers at Universal Relocations and help families and businesses relocate with confidence."),
    "company-news": ("Company News", "The latest announcements, milestones and press from Universal Relocations."),
    "shipping-worldwide": ("Shipping Worldwide", "From local moves to international relocations, we ship to and from destinations across the globe. Explore moving guides by region below."),
    "moving-to-africa": ("Moving to Africa", "Relocating to Africa? Our international teams handle shipping, customs and destination delivery across the continent."),
    "moving-to-asia": ("Moving to Asia", "Expert relocation services to destinations across Asia, with dedicated hubs in India and partner networks region-wide."),
    "moving-to-europe": ("Moving to Europe", "Seamless moves to Europe — ocean and air freight, customs clearance and door-to-door delivery across the continent."),
    "moving-to-north-america": ("Moving to North America", "Trusted relocation into the USA, Canada and across North America, backed by our US hub and FMC licensing."),
    "moving-to-oceania": ("Moving to Oceania", "Relocating to Australia, New Zealand or the Pacific? We manage every step of your move to Oceania."),
    "moving-to-south-america": ("Moving to South America", "International moving services to destinations across South America with full logistics and customs support."),
    "usa": ("USA Hub", "Reliable moving and relocation services for homes, families, and businesses across the United States. Call us at 1-888-323-7356."),
    "india": ("India Hub", "Trusted moving and relocation services across India, helping you move with confidence and ease. Call us at 1-800-103-7356."),
    "uae": ("UAE Hub", "Expert moving and relocation solutions for individuals, families, and businesses across the UAE. Call us at 800-13-7356."),
    "resources": ("Resources", "Guides, tools and references to help you plan and prepare for your move."),
    "blogs": ("Blogs", "Tips, guides and stories to help you prepare for your move."),
    "file-a-claim": ("File a Claim", "If something wasn't right with your shipment, we're here to help. Start your claim and our team will guide you through the process."),
    "moving-check-list": ("Moving Checklist", "Stay organized from start to finish with our step-by-step moving checklist covering the weeks before, during and after your move."),
    "referral": ("Moving Referral", "Love moving with us? Refer a friend and you both benefit. Learn more about our referral program."),
    "packing-tips": ("Packing Tips", "Practical, movers-approved packing tips to keep your belongings safe in transit."),
    "moving-terms": ("Moving Terms", "A glossary of common moving terms to help you understand your estimate, paperwork and process."),
    "shipping-terms": ("Shipping Terms", "Key ocean and air shipping terms explained — from bill of lading to demurrage."),
    # Legal
    "privacy-policy": ("Privacy Policy", "How we collect, use and protect your personal information."),
    "terms-and-condition": ("Terms & Conditions", "The terms that govern the use of our services and website."),
    "sms-terms-of-service": ("SMS Terms of Service", "Terms governing SMS communications from Universal Relocations."),
    "universal-relocations-cookies-policy": ("Cookies Policy", "How this website uses cookies and similar technologies."),
    "data-policy": ("Data Policy", "Our approach to data handling and protection."),
    "environmental-policy": ("Environmental Policy", "Our commitment to sustainable, lower-impact shipping and operations."),
    "anti-bribery-code-of-conduct": ("Anti-Bribery & Code of Conduct", "Our standards for ethical business conduct across every market."),
    "cancel-and-refund-policy": ("Cancellation & Refund Policy", "Our policy on cancellations and refunds."),
    "credit-application": ("Credit Application", "Apply for a trade credit account with Universal Relocations."),
    "vendor": ("Supplier Registration", "Register as a supplier or partner agent with Universal Relocations."),
    "bill-of-lading": ("Bill of Lading", "Access bill of lading information and resources."),
    "fmc-rules-tariff": ("FMC Rules & Tariff", "Our published Federal Maritime Commission rules and tariff information."),
    "historic-fmc-rules-tariff": ("Historic FMC Rules & Tariff", "Archived Federal Maritime Commission rules and tariff records."),
}

LOCATIONS = {
    "usa": ["new-jersey", "maryland", "georgia", "texas", "california"],
    "india": ["chennai", "bangalore", "hyderabad", "mumbai", "delhi"],
    "uae": ["dubai"],
}

FAQS = [
    ("How far in advance should I book my move?", "For international moves we recommend booking 4–6 weeks ahead where possible. For local and interstate moves, 2–3 weeks is usually enough, but we accommodate shorter timelines whenever we can."),
    ("Do you provide packing materials and services?", "Yes. We offer full and partial packing with export-grade materials, as well as specialty crating for fragile, high-value and oversized items."),
    ("How long does an international move take?", "Transit time depends on origin, destination and shipping method. Ocean shipments typically take several weeks to a few months door-to-door; air freight is faster. Your move coordinator will give you an estimate for your specific route."),
    ("Is my shipment insured?", "We offer transit insurance options so your belongings are protected throughout the journey. Ask your coordinator about all-risk coverage and valuation."),
    ("How do I get a quote?", "Use our online Moving Calculator, book a free video pre-move survey, or submit the quote form and a move consultant will contact you."),
    ("Can I track my shipment?", "Yes — we provide door-to-door tracking and keep you updated at every stage of your move."),
]


def build(g):
    """g = build.py globals(): gives us page(), interior(), write(), icon(), IMG, etc."""
    page = g["page"]; interior = g["interior"]; write = g["write"]; IMG = g["IMG"]

    def cta_block():
        return """<div style="text-align:center;margin-top:40px;padding:36px;background:var(--bg-soft);border-radius:var(--radius)">
          <h3 style="margin-bottom:10px">Ready to plan your move?</h3>
          <p style="margin-bottom:20px">Get a free, no-obligation quote from our move consultants.</p>
          <a class="btn btn-primary" href="/contact-us/">Get a Quote</a>
          <a class="btn btn-ghost" href="/moving-calculator/" style="margin-left:10px">Moving Calculator</a>
        </div>"""

    import expand as X
    # ---- Service detail pages (enriched: process, who-for, FAQs, hero image) ----
    X.build_services(g, SERVICES, SERVICE_ORDER, cta_block)

    # ---- Services index ----
    cards = ""
    for slug in SERVICE_ORDER:
        title, lead, _ = SERVICES[slug]
        short = lead[:140].rsplit(" ", 1)[0] + "…"
        cards += f"""<div class="info-card"><h3>{title}</h3><p>{short}</p>
          <a class="more" style="color:var(--blue);font-weight:600;font-size:.86rem" href="/services/{slug}/">View More →</a></div>"""
    svc_inner = f'<p class="section-intro" style="margin-bottom:34px">From a single baggage box to a full corporate relocation across continents, explore our complete range of moving services.</p><div class="card-grid">{cards}</div>{cta_block()}'
    write("services", interior("Our Services", [("Home", "/"), ("Services", "")], svc_inner,
          "Explore the full range of moving and relocation services from Universal Relocations."))

    # ---- Contact page ----
    def citem(ic, h, body):
        return f'<div class="item"><div class="ic">{g["icon"](ic)}</div><div><h4>{h}</h4><p>{body}</p></div></div>'
    contact_inner = f"""<div class="contact-grid">
      <div class="contact-info">
        <h2 style="margin-bottom:20px">Get in touch</h2>
        {citem("globe","Email","contact@universalrelocations.com")}
        {citem("truck","USA","1-888-323-7356")}
        {citem("truck","India","1-800-103-7356")}
        {citem("truck","UAE","800-13-7356")}
        {citem("clock","Support","24/7 online support at every step of your move")}
        <p style="margin-top:10px"><a class="btn btn-blue" href="https://calendly.com/UniversalrelocationsOfficial">Schedule a Video Survey</a></p>
      </div>
      <div class="quote-card" style="box-shadow:var(--shadow)">
        <h3>Request a free quote</h3><p class="sub">We'll follow up on your request and contact you.</p>
        <form id="quote-form">
          <div class="quote-grid">
            <div class="field"><label>Moving From *</label><input required></div>
            <div class="field"><label>Moving To *</label><input required></div>
            <div class="field full"><label>Name</label><input required></div>
            <div class="field"><label>Email</label><input type="email" required></div>
            <div class="field"><label>Phone</label><input type="tel" required></div>
            <div class="field full"><label>Move Size</label><select><option>Baggage</option><option>Studio</option><option>1 Bedroom</option><option>2 Bedroom</option><option>3 Bedroom</option><option>4+ Bedroom</option></select></div>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>"""
    write("contact-us", interior("Contact Us", [("Home", "/"), ("Contact", "")], contact_inner,
          "Contact Universal Relocations for a free moving quote. USA, India and UAE offices."))

    # ---- FAQ ----
    faq_inner = '<div class="prose">' + "".join(
        f"<h3>{q}</h3><p>{a}</p>" for q, a in FAQS) + "</div>" + cta_block()
    write("faq", interior("Frequently Asked Questions", [("Home", "/"), ("FAQ", "")], faq_inner,
          "Answers to common questions about moving with Universal Relocations."))

    # ---- Rich reconstructed pages (real content) + hero image + FAQs ----
    import content as C
    def _region_of(slug):
        r = slug.replace("moving-to-", "").replace("-", " ").title()
        return r
    for slug, (title_override, body) in C.RICH.items():
        title = title_override or SIMPLE[slug][0]
        crumbs = [("Home", "/"), (title.replace("&", "&amp;"), "")]
        faq_html = ""; faq_head = ""
        if slug.startswith("moving-to-"):
            f = X.dest_faqs(_region_of(slug)); faq_html = X.faq_block(f); faq_head = X.faq_schema(f)
        elif slug in ("usa", "india", "uae"):
            f = X.hub_faqs(X.HUB_NAME[slug]); faq_html = X.faq_block(f); faq_head = X.faq_schema(f)
        elif slug == "shipping-worldwide":
            f = X.dest_faqs("destinations worldwide"); faq_html = X.faq_block(f); faq_head = X.faq_schema(f)
        inner = f'<div class="prose">{body}</div>{faq_html}{cta_block()}'
        write(slug, interior(title.replace("&", "&amp;"), crumbs, inner,
              SIMPLE[slug][1][:155], hero_img=X.hero_for(g, slug), extra_head=faq_head))

    # ---- Functional + simple pages (enriched where we have real content) ----
    FUNC = X.functional_pages()
    for slug, (title, lead) in SIMPLE.items():
        if slug in C.RICH:
            continue
        crumbs = [("Home", "/"), (title.replace("&", "&amp;"), "")]
        if slug in FUNC:
            ftitle, body, faqs = FUNC[slug]
            inner = (f'<div class="prose">{body}</div>'
                     + (X.faq_block(faqs) if faqs else "") + cta_block())
            write(slug, interior(ftitle, crumbs, inner,
                  SIMPLE[slug][1][:155], hero_img=X.hero_for(g, slug),
                  extra_head=(X.faq_schema(faqs) if faqs else "")))
        else:
            inner = f'<div class="prose"><p style="font-size:1.1rem">{lead}</p></div>{cta_block()}'
            write(slug, interior(title.replace("&", "&amp;"), crumbs, inner,
                  f"{title} — Universal Relocations.", hero_img=X.hero_for(g, slug)))

    # ---- Major-city pages for the three hubs ----
    X.build_cities(g, cta_block)

    # ---- Dedicated mode pages (LCL/FCL/air/baggage/auto/pet) for hub corridors ----
    X.build_modes(g, cta_block)
    CORRIDOR_SET = {(fs, ts) for _, fs, _, ts in X.CORRIDORS}

    # ---- Route-pair pages: Moving from X to Y (all ordered pairs) ----
    from urllib.parse import quote
    COUNTRIES = g["COUNTRIES"]; HUBS_C = g["HUB_COUNTRIES"]
    SVC_LIST = C._ul([
        "International door-to-door relocation",
        "Groupage / shared-container shipping (cost-effective for smaller loads)",
        "Baggage &amp; box shipping", "Vehicle / auto shipping", "Transit insurance",
        "Storage &amp; warehousing", "Pet relocation", "Fine-art &amp; specialist handling",
    ])
    def route_page(fn, fs, tn, ts):
        bits = []
        if fs in HUBS_C:
            bits.append(f"Because {fn} is one of our hub countries, your packing, collection and export paperwork are handled directly by our own Universal Relocations team on the ground.")
        if ts in HUBS_C:
            bits.append(f"With our own hub in {tn}, customs clearance and final door-to-door delivery are managed end-to-end by our local team.")
        hub_html = ("<p>" + " ".join(bits) + "</p>") if bits else ""
        # Dedicated mode links for the flagship hub corridors
        mode_html = ""
        if (fs, ts) in CORRIDOR_SET:
            links = "".join(
                f'<a href="/moving/{fs}-to-{ts}/{mk}/">{X._strip(X.MODES[mk]["label"])}</a>'
                for mk in X.MODE_ORDER)
            mode_html = (f'<h2>Shipping options for {fn} &rarr; {tn}</h2>'
                         f'<p>Explore a dedicated guide for each way to ship on this route:</p>'
                         f'<div class="related-routes">{links}</div>')
        others = [(n, s) for n, s in COUNTRIES if s not in (fs, ts)][:6]
        rel = f'<a href="/moving/{ts}-to-{fs}/">{tn} &rarr; {fn}</a>' + "".join(
            f'<a href="/moving/{fs}-to-{s}/">{fn} &rarr; {n}</a>' for n, s in others)
        faqs = X.route_faqs(fn, tn)
        inner = (
            '<div class="prose">'
            f'<p style="font-size:1.12rem">Planning a move from <b>{fn}</b> to <b>{tn}</b>? Universal Relocations makes your international relocation from {fn} to {tn} seamless — from export-grade packing and ocean or air freight to customs clearance and door-to-door delivery. With 28+ years of experience and full FMC licensing, we move households, professionals and businesses on this route with precision and care.</p>'
            f'<h2>How your {fn} &rarr; {tn} move works</h2>' + C.PROCESS +
            f'<h2>Services for your {fn} &rarr; {tn} move</h2>' + SVC_LIST +
            mode_html +
            f'<h2>What to know about moving from {fn} to {tn}</h2>'
            f'<p>Most {fn}-to-{tn} household moves travel by sea freight, with air freight available for urgent or smaller shipments. Our team prepares all export and import documentation and handles customs clearance — including any transfer-of-residence or duty-relief paperwork — at both ends. Transit times vary by season and port; your dedicated move manager confirms exact timing and the most cost-effective option for your volume.</p>'
            + hub_html +
            f'<div style="margin:22px 0"><a class="btn btn-primary" href="/moving-calculator/">Estimate your volume</a> '
            f'<a class="btn btn-ghost" href="/assistant/?q={quote("I want to move from " + fn + " to " + tn)}" style="margin-left:8px">Instant {fn} &rarr; {tn} estimate</a></div>'
            f'<h2>Related routes</h2><div class="related-routes">{rel}</div>'
            '</div>'
            + X.faq_block(faqs))
        write(f"moving/{fs}-to-{ts}", interior(f"Moving from {fn} to {tn}",
              [("Home", "/"), (f"{fn} &rarr; {tn}", "")], inner,
              f"Moving from {fn} to {tn} — international relocation, shipping and customs with Universal Relocations.",
              hero_img=g["HERO_SHIP"], extra_head=X.faq_schema(faqs)))
    rc = 0
    for fn, fs in COUNTRIES:
        for tn, ts in COUNTRIES:
            if fs != ts:
                route_page(fn, fs, tn, ts); rc += 1
    print(f"Route pages built: {rc}")

    print("Content pages built.")
