"""
Expansion module for Universal Relocations:
 - FAQ accordion + FAQ JSON-LD schema (comprehensive FAQs on every page)
 - Six dedicated shipping-mode pages (LCL, FCL, Air Freight, Baggage, Auto, Pet)
   for the three inter-hub corridors (USA<->India, UAE<->India, USA<->UAE)
 - Major-city pages for the three hubs (USA, India, UAE)
Imported and called by pages.build().
"""
from urllib.parse import quote

# ---------------------------------------------------------------------------
# FAQ engine  (accordion HTML + schema.org FAQPage JSON-LD)
# ---------------------------------------------------------------------------
def faq_block(faqs, heading="Frequently asked questions"):
    items = "".join(
        f'<details class="faq-item"><summary>{q}</summary>'
        f'<div class="faq-a">{a}</div></details>'
        for q, a in faqs)
    return (f'<section class="faq-section"><h2>{heading}</h2>{items}</section>')

def faq_schema(faqs):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": _strip(a)}}
            for q, a in faqs],
    }
    return f'<script type="application/ld+json">{json.dumps(data)}</script>'

def _strip(html):
    import re
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html)).strip()

def _ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def _steps(items):
    return '<ol class="process">' + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

# ---------------------------------------------------------------------------
# Hubs & corridors
# ---------------------------------------------------------------------------
HUB_TEL = {"usa": "1-888-323-7356", "india": "1-800-103-7356", "uae": "800-13-7356"}
HUB_NAME = {"usa": "USA", "india": "India", "uae": "UAE"}

# Directional corridors that get dedicated mode pages
CORRIDORS = [
    ("usa", "India"[:0] or "United States", "india", "India"),
]
# build cleanly:
CORRIDORS = [
    ("United States", "usa", "India", "india"),
    ("India", "india", "United States", "usa"),
    ("UAE", "uae", "India", "india"),
    ("India", "india", "UAE", "uae"),
    ("United States", "usa", "UAE", "uae"),
    ("UAE", "uae", "United States", "usa"),
]

# ---------------------------------------------------------------------------
# Six shipping modes
# ---------------------------------------------------------------------------
# each: label, url-seg, hero-key, tagline, overview, how-steps, included, best_for, docs, mode_faqs(fn)
MODES = {}

MODES["lcl"] = {
    "label": "LCL Shipping (Groupage)",
    "short": "LCL",
    "hero": "HERO_SHIP",
    "tag": "Less-than-Container-Load — share a container, pay only for the space you use.",
    "overview": "LCL (Less-than-Container-Load), also called groupage or shared-container shipping, is the most cost-effective way to move a part-load internationally. Your household goods are professionally packed, consolidated with other shipments into a shared ocean container, and separated again at destination for door delivery. You pay only for the volume (cubic feet / cubic metres) your goods occupy, which makes LCL ideal for studios, one-bedroom moves, and anyone shipping a modest load without the cost of a full container.",
    "how": [
        "Free video or in-home survey to measure your volume and give a firm LCL rate.",
        "Export-grade packing and inventory at your origin address.",
        "Collection and consolidation into a shared container at our warehouse.",
        "Ocean transit with full documentation and tracking.",
        "Customs clearance and de-consolidation at destination.",
        "Door delivery, unpacking and debris removal on request.",
    ],
    "included": [
        "Volume-based pricing — pay only for the space you use",
        "Professional export packing &amp; wrapping",
        "Shared-container consolidation on regular sailings",
        "Full export &amp; import customs documentation",
        "Door-to-door delivery with online tracking",
    ],
    "best_for": "Studios, 1–bedroom homes, partial loads and budget-conscious moves where you don't need a container to yourself.",
}
MODES["fcl"] = {
    "label": "FCL Shipping (Full Container)",
    "short": "FCL",
    "hero": "HERO_SHIP",
    "tag": "A full 20ft or 40ft container reserved exclusively for your move.",
    "overview": "FCL (Full-Container-Load) gives you sole use of a 20ft or 40ft ocean container for your household goods. Because nothing else travels inside, your container is loaded at your home, sealed, and not opened again until customs or your destination residence — the fastest, most secure and most private way to ship a full home internationally. FCL is the right choice for 2-bedroom homes and larger, for vehicles shipped alongside household goods, and whenever you want a dedicated, direct transit.",
    "how": [
        "Pre-move survey to confirm whether a 20ft or 40ft container fits your volume.",
        "Export packing, crating and a detailed inventory at your residence.",
        "Container positioned at your door, loaded and sealed on-site.",
        "Direct ocean transit — your container is not shared or re-handled.",
        "Customs clearance at destination with our in-house brokerage.",
        "Delivery to your new home, unpacking and furniture reassembly.",
    ],
    "included": [
        "Exclusive 20ft / 40ft container for your goods only",
        "Container loaded and sealed at your home",
        "Faster, more direct transit than shared shipping",
        "Export-grade packing, crating &amp; inventory",
        "Door-to-door delivery, unpacking &amp; reassembly",
    ],
    "best_for": "2–bedroom homes and larger, villas, moves that include a vehicle, and anyone who wants maximum security, speed and privacy.",
}
MODES["air-freight"] = {
    "label": "Air Freight",
    "short": "Air Freight",
    "hero": "HERO_TRUCK",
    "tag": "The fastest way to move — door-to-door in days, not weeks.",
    "overview": "Air freight is the quickest international moving option, with door-to-door transit typically measured in days rather than the weeks ocean shipping takes. It's priced on chargeable weight (the greater of actual or volumetric weight), so it's most economical for essentials, urgent items, smaller consignments and anything you need soon after you land — a starter set of clothing, kitchenware, documents, electronics or a child's necessities. We handle export packing, airline documentation, security screening and destination customs so your priority items are waiting for you.",
    "how": [
        "Survey or packing list to calculate chargeable weight and quote.",
        "Export packing designed for air cargo handling and screening.",
        "Collection and lodgement with the airline, with security screening.",
        "Air transit on the next available service.",
        "Customs clearance and rapid destination delivery.",
    ],
    "included": [
        "Fastest international transit — days, not weeks",
        "Priced on chargeable weight for smaller, urgent loads",
        "Airline documentation &amp; security screening handled",
        "Ideal pairing with a slower ocean shipment for the rest",
        "Door-to-door delivery with tracking",
    ],
    "best_for": "Urgent and essential items, documents, electronics, a first set of belongings to tide you over, and smaller high-priority consignments.",
}
MODES["baggage"] = {
    "label": "Baggage &amp; Box Shipping",
    "short": "Baggage",
    "hero": "HERO_MOVE2",
    "tag": "Send boxes and excess luggage ahead — skip airline excess-baggage fees.",
    "overview": "Baggage shipping (also called excess-baggage or box shipping) is the simple, affordable way to send a handful of boxes, suitcases or cartons internationally without paying punishing airline excess-baggage charges. It's the most popular option for students, young professionals and anyone relocating with personal effects rather than furniture. We collect from your door, ship by air or sea depending on how quickly you need it, and deliver to your destination address with full tracking box-by-box.",
    "how": [
        "Tell us how many boxes/bags and your deadline for a per-box price.",
        "We deliver cartons and materials, or you pack your own.",
        "Door pickup of your boxes and luggage.",
        "Air or sea shipping to suit your budget and timeline.",
        "Customs clearance and delivery to your destination door.",
    ],
    "included": [
        "Transparent per-box / per-bag pricing",
        "No airline excess-baggage fees",
        "Door-to-door collection and delivery",
        "Air (fast) or sea (economical) options",
        "End-to-end box-level tracking",
    ],
    "best_for": "Students, single movers, and anyone sending a few boxes or suitcases rather than a household of furniture.",
}
MODES["auto-shipping"] = {
    "label": "Auto / Vehicle Shipping",
    "short": "Auto Shipping",
    "hero": "HERO_SHIP",
    "tag": "Ship your car, motorcycle or scooter safely overseas.",
    "overview": "We ship cars, motorcycles, scooters and other vehicles internationally by container (shared or exclusive) or RoRo (roll-on/roll-off), managing every step of the process — export documentation, title and ownership paperwork, marine insurance, customs clearance and destination registration support. Vehicles can travel on their own or be loaded alongside your household goods in an FCL container to save cost. Each destination has its own import rules on age, emissions and duties, and our team confirms exactly what applies before you ship.",
    "how": [
        "Vehicle assessment and the right method — container or RoRo.",
        "Title, ownership and export documentation prepared.",
        "Vehicle delivered to port or loaded with your household container.",
        "Ocean transit with marine insurance in place.",
        "Destination customs clearance, duty handling and release.",
    ],
    "included": [
        "Container or RoRo vehicle shipping",
        "Full export &amp; title documentation",
        "Marine transit insurance options",
        "Destination customs &amp; duty handling",
        "Option to load with your household FCL container",
    ],
    "best_for": "Anyone relocating with a car or motorcycle, classic/collector vehicles, and households shipping a vehicle alongside their goods.",
}
MODES["pet"] = {
    "label": "Pet Relocation",
    "short": "Pet Relocation",
    "hero": "HERO_SURVEY",
    "tag": "A safe, stress-free journey for the family members with four legs.",
    "overview": "Our IPATA-affiliated pet relocation service moves dogs, cats and other pets internationally with their comfort and safety first. We arrange airline-approved travel crates, the health certificates, vaccinations and import permits each country requires, and manage flight booking, airport handling and — where needed — quarantine arrangements. Every destination has its own entry rules (microchip, rabies titre test, waiting periods), and we map out the exact timeline for your pet well in advance so nothing is rushed.",
    "how": [
        "Consultation on your pet, destination rules and timeline.",
        "Correctly sized, airline-approved IATA travel crate.",
        "Vaccinations, microchip, titre tests and health certificates arranged.",
        "Import permits and (if required) quarantine booking.",
        "Flight booking, airport check-in and destination collection.",
    ],
    "included": [
        "IPATA-affiliated pet logistics",
        "Airline-approved IATA travel crates",
        "Health certificates, vaccinations &amp; import permits",
        "Quarantine coordination where required",
        "Door-to-door pet transport &amp; airport handling",
    ],
    "best_for": "Families relocating with dogs, cats or other pets who want the paperwork, crate and flight handled end-to-end.",
}

MODE_ORDER = ["lcl", "fcl", "air-freight", "baggage", "auto-shipping", "pet"]

# Per-corridor flavour notes used to differentiate pages
CORRIDOR_NOTE = {
    ("usa", "india"): "The USA–India corridor is Universal Relocations' flagship lane. We run regular consolidations from the US East and West Coasts to Chennai, Mumbai, Delhi, Bangalore and Hyderabad, and as an FMC-licensed carrier with our own India offices we handle both ends in-house — including Transfer of Residence (TR) customs clearance for returning residents.",
    ("india", "usa"): "Moving from India to the USA, our India offices manage export packing and documentation while our US team clears customs and delivers to your door. We ship from all major Indian ports to destinations across the United States.",
    ("uae", "india"): "The UAE–India lane is one of the busiest relocation corridors in the world. With our own teams in Dubai and across India, we offer frequent sailings, competitive groupage rates and in-house Transfer of Residence clearance for returning Indian residents.",
    ("india", "uae"): "From India to the UAE, we handle export formalities in India and customs clearance and delivery in Dubai, Abu Dhabi and across the Emirates through our own UAE operation.",
    ("usa", "uae"): "On the USA–UAE lane we move professionals, families and corporate assignees to Dubai, Abu Dhabi and the wider Emirates, clearing destination customs through our own UAE team.",
    ("uae", "usa"): "From the UAE to the USA, we manage packing and export in the Emirates and FMC-licensed customs clearance and delivery across the United States.",
}

def _corridor_faqs(fn, fs, tn, ts, mode_key):
    m = MODES[mode_key]
    label = _strip(m["label"])
    faqs = [
        (f"How long does {label.lower()} from {fn} to {tn} take?",
         f"Transit time depends on the exact origin and destination and the season. Your dedicated move manager confirms a firm timeline for your {fn}–{tn} shipment after your survey. Air options are the fastest; ocean options are the most economical."),
        (f"How is my {fn} to {tn} move priced?",
         "LCL and baggage are priced on volume (or number of boxes), FCL on the container size you reserve, air freight on chargeable weight, and vehicle/pet moves per item with the required documentation. You get a firm, itemised quote after a free survey — no hidden fees."),
        (f"Do you handle customs clearance in {tn}?",
         f"Yes. We prepare all export paperwork in {fn} and clear customs in {tn}, including any Transfer of Residence or duty-relief paperwork you qualify for. Our in-house brokerage manages both ends so you don't deal with agents yourself."),
        ("What documents will I need?",
         "Typically a passport, visa/residence proof, a detailed packing inventory and (for returning residents) Transfer of Residence paperwork. For vehicles you'll also need title and registration; for pets, vaccination and health records. We send you an exact checklist for your route."),
        ("Is my shipment insured?",
         "Yes — we offer all-risk marine transit insurance. Your coordinator explains valuation and coverage so your belongings are protected door-to-door."),
        ("Can I get a quote without an in-home visit?",
         "Absolutely. Book a free video survey from your phone, use our online Moving Calculator to estimate volume, or send us a room-by-room list and we'll quote from that."),
    ]
    return faqs


def build_modes(g, cta_block):
    """Dedicated mode pages: /moving/{fs}-to-{ts}/{mode}/ for the hub corridors."""
    interior = g["interior"]; write = g["write"]
    heroes = {k: g[k] for k in ("HERO_SHIP", "HERO_TRUCK", "HERO_MOVE1", "HERO_MOVE2",
                                "HERO_SURVEY", "HERO_BRAND")}
    count = 0
    for fn, fs, tn, ts in CORRIDORS:
        for mk in MODE_ORDER:
            m = MODES[mk]
            label = m["label"]
            hero = heroes.get(m["hero"], g["HERO_SHIP"])
            note = CORRIDOR_NOTE.get((fs, ts), "")
            faqs = _corridor_faqs(fn, fs, tn, ts, mk)
            lbl = _strip(label).split("(")[0].strip()
            overview = m["overview"].replace("{fn}", fn).replace("{tn}", tn)
            # other modes as icon chips
            MICON = {"lcl":"ship","fcl":"cubes","air-freight":"plane","baggage":"box","auto-shipping":"car","pet":"paw"}
            chips = "".join(
                f'<a href="/moving/{fs}-to-{ts}/{o}/">{icon(MICON.get(o,"ship"))}<span>{_strip(MODES[o]["label"]).split("(")[0].strip()}</span></a>'
                for o in MODE_ORDER if o != mk)
            step_pairs = [(f"Step {i+1}", s) for i, s in enumerate(m["how"])]
            sections = (
                isec(lead_split(f'<p>{m["tag"]}</p><p>{overview}</p>', STATS))
                + orange_stats()
                + isec(step_cards(step_pairs), alt=True,
                       head=sec_head(f"{lbl}: {fn} &rarr; {tn}, step by step", "", "How it works"))
                + isec(media_row(g.get(MODE_BODY.get(mk, "PH_SHIP2"), g["HERO_SHIP"]), "What’s included", _ul(m["included"]))
                       + (f'<div class="callout" style="margin-top:40px"><div class="co-txt"><h3>Is {lbl.lower()} right for you?</h3>'
                          f'<p><b>Best for:</b> {m["best_for"]}' + (f' {note}' if note else '') + '</p></div>'
                          f'<div><a class="btn btn-accent" href="/moving-calculator/">Estimate volume</a></div></div>'))
                + cost_timeline_section(f"{lbl.lower()} on this route")
                + compare_table()
                + docs_section(alt=False)
                + isec(f'<div class="mode-chip-grid">{chips}</div>', alt=True,
                       head=sec_head(f"Other ways to ship {fn} &rarr; {tn}", "Compare every option for this route.", "More options"))
                + why_us_band(alt=False)
                + trust_logos(g, alt=True)
                + faq_isec(faqs + EXTRA_FAQS)
                + cta_isec())
            title = f"{lbl} from {fn} to {tn}"
            write(f"moving/{fs}-to-{ts}/{mk}",
                  interior(title,
                           [("Home", "/"), (f"{fn} &rarr; {tn}", f"/moving/{fs}-to-{ts}/"),
                            (m["short"], "")],
                           sections,
                           f"{_strip(label)} from {fn} to {tn} — Universal Relocations. Door-to-door, insured, customs handled.",
                           hero_img=hero, extra_head=faq_schema(faqs + EXTRA_FAQS),
                           subtitle=m["tag"], raw=True))
            count += 1
    print(f"Mode pages built: {count}")
    return count


# ---------------------------------------------------------------------------
# Major-city pages for the three hubs
# ---------------------------------------------------------------------------
CITIES = {
    "usa": {
        "hero": "HERO_USA", "tel": "1-888-323-7356",
        "cities": [
            ("New York", "new-york", "New York and the tri-state area"),
            ("New Jersey", "new-jersey", "New Jersey"),
            ("Los Angeles", "los-angeles", "Los Angeles and Southern California"),
            ("San Francisco Bay Area", "san-francisco", "the San Francisco Bay Area"),
            ("Chicago", "chicago", "Chicago and the Midwest"),
            ("Houston", "houston", "Houston and Texas"),
            ("Dallas", "dallas", "Dallas–Fort Worth"),
            ("Atlanta", "atlanta", "Atlanta and the Southeast"),
            ("Washington DC", "washington-dc", "the Washington DC metro"),
            ("Seattle", "seattle", "Seattle and the Pacific Northwest"),
            ("Boston", "boston", "Boston and New England"),
        ],
    },
    "india": {
        "hero": "HERO_INDIA", "tel": "1-800-103-7356",
        "cities": [
            ("Chennai", "chennai", "Chennai and Tamil Nadu"),
            ("Mumbai", "mumbai", "Mumbai and Maharashtra"),
            ("Delhi NCR", "delhi", "Delhi, Gurgaon, Noida and the NCR"),
            ("Bangalore", "bangalore", "Bengaluru and Karnataka"),
            ("Hyderabad", "hyderabad", "Hyderabad and Telangana"),
            ("Pune", "pune", "Pune"),
            ("Kolkata", "kolkata", "Kolkata and eastern India"),
            ("Ahmedabad", "ahmedabad", "Ahmedabad and Gujarat"),
            ("Kochi", "kochi", "Kochi and Kerala"),
            ("Coimbatore", "coimbatore", "Coimbatore"),
        ],
    },
    "uae": {
        "hero": "HERO_UAE", "tel": "800-13-7356",
        "cities": [
            ("Dubai", "dubai", "Dubai"),
            ("Abu Dhabi", "abu-dhabi", "Abu Dhabi"),
            ("Sharjah", "sharjah", "Sharjah"),
            ("Ajman", "ajman", "Ajman"),
            ("Ras Al Khaimah", "ras-al-khaimah", "Ras Al Khaimah"),
            ("Al Ain", "al-ain", "Al Ain"),
        ],
    },
}

def _city_faqs(city, hubslug):
    hub = HUB_NAME[hubslug]
    return [
        (f"What moving services do you offer in {city}?",
         f"From {city} we handle international relocation (LCL and FCL ocean freight, air freight), local and domestic moves, baggage &amp; box shipping, vehicle shipping, pet relocation, storage and insurance — packed, documented and delivered door-to-door."),
        (f"How much does moving from {city} cost?",
         "Your price depends on volume, destination and service level. Book a free video survey or use our online Moving Calculator for an estimate, then we confirm a firm, itemised quote with no hidden fees."),
        (f"Do you provide packing in {city}?",
         "Yes — full and partial export-grade packing, plus specialty crating for fragile, high-value and oversized items, all handled by our trained local crews."),
        (f"How far ahead should I book my {city} move?",
         "For international moves we suggest 4–6 weeks where possible; for local moves 1–2 weeks is usually enough. We accommodate shorter timelines whenever we can."),
        ("Is my shipment insured and tracked?",
         "Yes. We offer all-risk transit insurance and give you door-to-door tracking with updates at every stage of your move."),
    ]


# ---------------------------------------------------------------------------
# Service-page depth (overview, process, who-for, FAQs) per service slug
# ---------------------------------------------------------------------------
_GEN_PROCESS = [
    "Free survey — video or in-home — to scope your move and give a firm quote.",
    "A dedicated move coordinator plans timing, materials and paperwork with you.",
    "Export-grade packing, wrapping and a full inventory at your door.",
    "Shipping by the best method for your goods, with documents and tracking.",
    "Customs clearance at destination through our in-house brokerage.",
    "Delivery, unpacking, reassembly and debris removal at your new home.",
]
SERVICE_DETAIL = {
    "international": {"hero": "HERO_SHIP",
        "who": "Families, professionals, students and corporate assignees moving between countries — any size, any destination.",
        "faqs": [
            ("How long does an international move take?", "It depends on route and method. Ocean freight is typically a few weeks to a couple of months door-to-door; air freight is a matter of days. Your coordinator gives an exact estimate for your route after a survey."),
            ("LCL or FCL — which should I choose?", "LCL (shared container) is most economical for studios and one-bedroom loads; FCL (your own 20ft/40ft container) is faster, more secure and better value for two-bedroom homes and larger. We advise the right fit at survey."),
            ("Do you handle customs and Transfer of Residence?", "Yes — we prepare all export and import paperwork and clear customs at both ends, including Transfer of Residence and duty-relief claims for returning residents."),
            ("Is my shipment insured?", "We offer all-risk marine transit insurance with a simple valuation process, so your belongings are protected the whole way."),
        ]},
    "corporate-relocation": {"hero": "HERO_SURVEY",
        "who": "HR and mobility teams, and employees or assignees relocating for work — single moves or whole-office programmes.",
        "faqs": [
            ("Can you manage a full employee mobility programme?", "Yes — from single assignee moves to multi-family programmes, with a dedicated coordinator, consolidated reporting and policy-compliant service levels."),
            ("Do you move office equipment and IT?", "We handle office furniture, IT and equipment with careful packing, labelling and reinstallation to limit downtime."),
            ("Can you work to our relocation policy and budget?", "Absolutely — we tailor scope (packing tiers, insurance, storage, destination services) to your policy and provide transparent, itemised costs."),
        ]},
    "pet-relocations": {"hero": "HERO_SURVEY",
        "who": "Anyone relocating with dogs, cats or other pets who wants crates, health paperwork and flights handled end-to-end.",
        "faqs": [
            ("What paperwork does my pet need?", "Requirements vary by destination but usually include a microchip, up-to-date rabies vaccination (sometimes a titre test), a health certificate and an import permit. We map the exact timeline for your country."),
            ("Will my pet need quarantine?", "Some destinations require it, some don't. We confirm the rules for your route early and arrange any quarantine booking so there are no surprises."),
            ("Are the crates airline-approved?", "Yes — we supply correctly sized IATA-compliant travel crates so your pet flies safely and comfortably."),
        ]},
    "groupage-solution": {"hero": "HERO_SHIP",
        "who": "Smaller and partial loads — studios, one-bedroom moves and budget-conscious shippers who don't need a full container.",
        "faqs": [
            ("How is groupage priced?", "By the volume your goods occupy (cubic feet / cubic metres), so you only pay for the space you use — far cheaper than a full container for smaller loads."),
            ("Will my goods be safe in a shared container?", "Yes — every shipment is professionally packed, inventoried and secured. Goods are consolidated and de-consolidated in our own warehouses."),
            ("How often do containers sail?", "We run regular consolidations on our main lanes. Your coordinator gives you the next available sailing and a transit estimate."),
        ]},
    "storage": {"hero": "HERO_MOVE1",
        "who": "Anyone needing a secure gap between move-out and move-in, or long-term storage during an overseas posting.",
        "faqs": [
            ("Do you offer short and long-term storage?", "Both — flexible by the week or by the month, in secure, monitored, climate-controlled facilities."),
            ("Is my inventory tracked in storage?", "Yes — every item is inventoried on intake and you can request release or redelivery whenever you need it."),
            ("Is stored property insured?", "Storage insurance is available — ask your coordinator about coverage and valuation."),
        ]},
    "intrastate": {"hero": "HERO_MOVE2",
        "who": "Local and long-distance domestic moves — homes and offices moving within or between states.",
        "faqs": [
            ("Do you handle both local and interstate moves?", "Yes — from a cross-town apartment move to a long-distance interstate relocation, fully packed, loaded and insured."),
            ("Is the transport licensed and insured?", "Yes — licensed, insured transport with transparent, upfront pricing and no surprise charges."),
            ("Can you pack for me?", "Full and partial packing is available, with materials and crews supplied."),
        ]},
    "baggage-shipping": {"hero": "HERO_MOVE2",
        "who": "Students, single movers and anyone sending a few boxes or suitcases rather than furniture.",
        "faqs": [
            ("How is baggage shipping priced?", "Per box or per bag, with clear pricing and no airline excess-baggage fees. Choose air for speed or sea for the lowest cost."),
            ("Do you collect from my door?", "Yes — door-to-door pickup and delivery with box-level tracking from start to finish."),
            ("How long does it take?", "Air shipments arrive in days; sea shipments take longer but cost less. We'll match the option to your deadline."),
        ]},
    "insurance": {"hero": "HERO_SHIP",
        "who": "Every shipper who wants their belongings protected against loss or damage in transit.",
        "faqs": [
            ("What does transit insurance cover?", "All-risk coverage options protect your goods against loss or damage throughout the journey, by air or ocean."),
            ("How do I value my shipment?", "We use a simple valuation process — you declare the replacement value and we explain the coverage and premium."),
            ("How are claims handled?", "Quickly and fairly — your coordinator guides you through documentation and settlement if anything goes wrong."),
        ]},
    "fine-art-relocations": {"hero": "HERO_MOVE1",
        "who": "Collectors, galleries and anyone moving art, antiques or high-value, fragile pieces.",
        "faqs": [
            ("How do you protect fragile and high-value pieces?", "With custom crating, climate-controlled transport, soft-wrap and white-glove handling, plus condition reporting before and after transit."),
            ("Do you provide condition reports?", "Yes — documented condition reporting is part of our fine-art service."),
            ("Can you install at destination?", "We offer white-glove delivery and installation at your destination residence or gallery."),
        ]},
    "hospitality-relocations": {"hero": "HERO_SHIP",
        "who": "Hotels, resorts and hospitality projects needing FF&E logistics, warehousing and installation.",
        "faqs": [
            ("What is FF&E logistics?", "Managing the furniture, fixtures and equipment for a hospitality project — consolidation, warehousing, delivery scheduling and on-site installation support."),
            ("Can you store project stock until the site is ready?", "Yes — project-based warehousing lets us receive and consolidate FF&E and deliver on your installation schedule."),
            ("Do you coordinate on-site installation?", "We provide delivery and on-site installation support coordinated with your project timeline."),
        ]},
    "auto-shipping": {"hero": "HERO_SHIP",
        "who": "Anyone relocating with a car or motorcycle, including vehicles shipped alongside household goods.",
        "faqs": [
            ("Container or RoRo — what's the difference?", "Container shipping encloses your vehicle (optionally with your household goods); RoRo (roll-on/roll-off) is often cheaper for a vehicle on its own. We advise the best fit for your route."),
            ("What documents does my vehicle need?", "Typically the title/ownership, registration and export paperwork. Destination import rules on age, emissions and duty vary — we confirm what applies before you ship."),
            ("Can I ship my car with my household goods?", "Yes — loading a vehicle into your FCL container alongside your belongings is a cost-effective option we handle routinely."),
        ]},
}

def build_services(g, SERVICES, SERVICE_ORDER, cta_block):
    interior = g["interior"]; write = g["write"]
    heroes = {k: g[k] for k in ("HERO_SHIP", "HERO_SURVEY", "HERO_MOVE1", "HERO_MOVE2", "HERO_BRAND")}
    for slug in SERVICE_ORDER:
        title, lead, bullets = SERVICES[slug]
        d = SERVICE_DETAIL.get(slug, {})
        hero = heroes.get(d.get("hero", "HERO_SHIP"), g["HERO_SHIP"])
        faqs = d.get("faqs", [])
        tclean = _strip(title)
        SVC_BODY = {"international":"PH_STAFF1","corporate-relocation":"HERO_SURVEY","pet-relocations":"HERO_MOVE1",
                    "groupage-solution":"PH_SHIP2","storage":"HERO_LOGISTICS","intrastate":"HERO_MOVE2",
                    "baggage-shipping":"HERO_MOVE2","insurance":"PH_STAFF2","fine-art-relocations":"HERO_MOVE1",
                    "hospitality-relocations":"HERO_LOGISTICS","auto-shipping":"PH_SHIP2"}
        photo = g.get(SVC_BODY.get(slug, "PH_STAFF1"), g["HERO_SHIP"])
        over = d.get("overview") or (
            f"Our {tclean.lower()} service is built around one idea: that a move should feel handled, not endured. "
            "From the first free survey to the final reassembled piece of furniture, a single dedicated coordinator "
            "plans every stage — materials, timing, documentation, shipping and delivery — and stays reachable "
            "throughout. We’ve refined this over 28+ years and hundreds of thousands of items moved, which is why "
            "families, professionals and companies come back to us and recommend us to others.")
        lead_html = (f'<p>{lead}</p>'
                     + (f'<p><b>Who it’s for:</b> {d["who"]}</p>' if d.get("who") else ''))
        full_faqs = faqs + EXTRA_FAQS
        sections = (
            isec(lead_split(lead_html, STATS))
            + orange_stats()
            + prompt_band(title=f"Get an instant {tclean.lower()} estimate")
            + prose_section(f"About our {tclean.lower()}", [over], "Overview")
            + isec(check_grid(bullets), alt=True,
                   head=sec_head("What’s included", f"Everything your {tclean.lower()} needs, handled end-to-end.", "What you get"))
            + isec(media_row(photo, f"How your {tclean.lower()} works",
                   '<p>One dedicated coordinator owns your move from the first survey to the final box — planning, packing, shipping, customs and delivery.</p>'
                   + _ul([t for _, t in GEN_STEPS])))
            + cost_timeline_section(f"your {tclean.lower()}")
            + docs_section(alt=True)
            + core_strengths()
            + why_us_band(alt=False)
            + trust_logos(g, alt=True)
            + isec(callout(f"Get a tailored {tclean.lower()} quote",
                   "Tell us about your move and we’ll send a firm, competitive quote — no obligation.",
                   "Get a free quote", "/contact-us/", "Estimate volume", "/moving-calculator/"))
            + faq_isec(full_faqs)
            + cta_isec())
        write(f"services/{slug}", interior(title.replace("&amp;", "&"),
              [("Home", "/"), ("Services", "/services/"), (title, "")], sections,
              f"{title} from Universal Relocations — expert, insured and fully tracked.",
              hero_img=hero, extra_head=faq_schema(full_faqs),
              subtitle=_strip(lead)[:150] + "…", raw=True))
    print("Service pages built (enriched).")


def build_cities(g, cta_block):
    interior = g["interior"]; write = g["write"]
    heroes = {k: g[k] for k in ("HERO_USA", "HERO_INDIA", "HERO_UAE")}
    count = 0
    for hubslug, data in CITIES.items():
        hub = HUB_NAME[hubslug]; tel = data["tel"]
        hero = heroes.get(data["hero"], g["HERO_BRAND"])
        for city, slug, area in data["cities"]:
            faqs = _city_faqs(city, hubslug)
            # popular destinations from this city (hub-aware)
            if hubslug == "india":
                dests = [("the USA", "/moving/india-to-usa/"), ("the UAE", "/moving/india-to-uae/"),
                         ("the UK", "/moving/india-to-uk/"), ("Canada", "/moving/india-to-canada/"),
                         ("Australia", "/moving/india-to-australia/")]
            elif hubslug == "usa":
                dests = [("India", "/moving/usa-to-india/"), ("the UAE", "/moving/usa-to-uae/"),
                         ("the UK", "/moving/usa-to-uk/"), ("Canada", "/moving/usa-to-canada/"),
                         ("Australia", "/moving/usa-to-australia/")]
            else:
                dests = [("India", "/moving/uae-to-india/"), ("the USA", "/moving/uae-to-usa/"),
                         ("Canada", "/moving/uae-to-canada/"), ("the UK", "/moving/uae-to-uk/")]
            dl = "".join(f'<a href="{h}">{city} &rarr; {n}</a>' for n, h in dests)
            svc_cards = feature_cards([
                ("globe", "International relocation", "LCL &amp; FCL ocean freight and air freight to any destination."),
                ("box", "Baggage &amp; box shipping", "Send boxes and excess luggage with no airline excess fees."),
                ("home", "Local &amp; domestic moves", "Home and office moves across the city and the country."),
                ("car", "Vehicle shipping", "Cars and motorcycles by container or RoRo, documents handled."),
                ("warehouse", "Storage &amp; warehousing", "Secure, climate-controlled short and long-term storage."),
                ("shield", "Insurance &amp; crating", "All-risk transit cover and specialist crating for fragile pieces."),
            ])
            step_pairs = [
                ("Free survey", f"Video or in-home survey anywhere in {area}, then a firm, itemised quote."),
                ("Pack &amp; inventory", "Export-grade packing and a full inventory at your door."),
                ("Ship &amp; clear", "Shipping by sea or air, with customs handled at both ends."),
                ("Deliver", "Delivery, unpacking and reassembly at your new home."),
            ]
            lead_html = (f'<p>Universal Relocations provides trusted local and international moving services in {area}. '
                f'Whether you’re relocating across {city}, to another part of {hub}, or overseas, our local crews deliver the '
                f'export-grade packing, customs expertise, tracking and personal support we’ve built over 28+ years.</p>'
                f'<p><a class="btn btn-primary" href="/moving-calculator/">Get an estimate</a> '
                f'<a class="btn btn-ghost" href="tel:{tel}" style="margin-left:8px">Call {tel}</a></p>')
            sections = (
                isec(lead_split(lead_html, STATS))
                + orange_stats()
                + prompt_band(title=f"Get a moving estimate from {city}",
                    chips=[(f"I want to move my 3 bedroom home from {city}", f"Move a home from {city}"),
                           (f"I want to ship boxes from {city}", f"Ship boxes from {city}"),
                           (f"I want to move my car from {city}", f"Move a car from {city}"),
                           (f"How much to move from {city} overseas", f"Move overseas from {city}")])
                + isec(svc_cards, alt=True, head=sec_head(f"Our moving services in {city}",
                       "One team for every kind of move, local or international.", "Services"))
                + isec(media_row(g.get("HERO_MOVE1"), f"How your {city} move works",
                       '<p>From first survey to final box, one dedicated coordinator keeps your move on track.</p>'
                       + _ul([t for _, t in step_pairs])))
                + isec(f'<div class="related-routes">{dl}</div>', alt=True,
                       head=sec_head(f"Popular routes from {city}", "Dedicated guides for the moves we handle most.", "Where to"))
                + cost_timeline_section(f"your move from {city}", alt=False)
                + docs_section(alt=True)
                + core_strengths()
                + why_us_band(alt=False)
                + trust_logos(g, alt=True)
                + faq_isec(faqs + EXTRA_FAQS)
                + cta_isec())
            write(f"{hubslug}/locations/{slug}",
                  interior(f"Movers in {city}",
                           [("Home", "/"), (hub, f"/{hubslug}/"), (city, "")],
                           sections,
                           f"Professional movers in {city}, {hub}. International &amp; local relocation, packing, shipping and customs with Universal Relocations.",
                           hero_img=hero, extra_head=faq_schema(faqs + EXTRA_FAQS),
                           subtitle=f"Professional local &amp; international movers in {area}.", raw=True))
            count += 1
    print(f"City pages built: {count}")
    return count


# ---------------------------------------------------------------------------
# Hero image picker + FAQ banks for destination / hub / route / functional pages
# ---------------------------------------------------------------------------
def hero_for(g, slug):
    s = slug
    if s in ("usa",): return g["HERO_USA"]
    if s in ("india",): return g["HERO_INDIA"]
    if s in ("uae",): return g["HERO_UAE"]
    if s.startswith("moving-to-"): return g["HERO_SHIP"]
    if s in ("shipping-worldwide",): return g["HERO_SHIP"]
    if s in ("about-us", "company", "corporate-social-responsibility", "company-news",
             "career", "press"): return g["HERO_SURVEY"]
    if s in ("packing-tips", "moving-check-list", "moving-terms", "shipping-terms",
             "resources", "blogs", "file-a-claim", "referral"): return g["HERO_MOVE1"]
    if s in ("contact-us",): return g["HERO_SURVEY"]
    return g["HERO_BRAND"]

def dest_faqs(region):
    return [
        (f"What does a move to {region} include?",
         "Export-grade packing, door-to-door ocean or air freight, full customs documentation and clearance, and delivery and unpacking at your new home — all managed by one dedicated coordinator."),
        (f"How long does shipping to {region} take?",
         "It varies by exact destination, port and season. Ocean freight is the economical choice and takes a few weeks to a couple of months door-to-door; air freight is far faster. We confirm a firm timeline after your survey."),
        ("Can I ship a partial load or just a few boxes?",
         "Yes — choose LCL (shared container) or baggage/box shipping for smaller loads, or FCL (your own container) for a full home. We'll recommend the most cost-effective option."),
        ("Do you handle customs and duties?",
         "Yes — we prepare all paperwork and clear customs at destination, including any transfer-of-residence or duty-relief relief you qualify for."),
        ("How do I get a quote?",
         "Book a free video survey, use our online Moving Calculator, or send a room-by-room list — we'll return a firm, itemised quote with no hidden fees."),
    ]

def hub_faqs(hubname):
    return [
        (f"What areas do you cover from your {hubname} hub?",
         f"Our {hubname} operation serves all major cities and surrounding regions for both inbound and outbound moves, with our own crews and warehouses."),
        ("What services are available?",
         "International relocation (LCL, FCL, air freight), baggage &amp; box shipping, local and domestic moves, vehicle shipping, pet relocation, storage, insurance and specialist crating."),
        ("Do you handle customs clearance in-house?",
         f"Yes — our {hubname} team manages customs clearance and documentation directly, including transfer-of-residence claims where applicable."),
        ("How do I start?",
         "Call your local hub number, book a free video survey, or use the Moving Calculator for an instant volume estimate and a fast quote."),
    ]

def route_faqs(fn, tn):
    return [
        (f"How much does moving from {fn} to {tn} cost?",
         "It depends on volume, service (LCL, FCL, air or baggage) and any extras like storage or a vehicle. You get a firm, itemised quote after a free survey — no hidden fees."),
        (f"How long is transit from {fn} to {tn}?",
         "Ocean freight is the economical option and takes several weeks door-to-door; air freight is much faster. Your move manager confirms exact timing for your route."),
        (f"What shipping options do I have for {fn} → {tn}?",
         "LCL (shared container) and baggage shipping for smaller loads, FCL (your own container) for a full home, and air freight when you need it fast. Vehicles and pets can travel too."),
        ("Do you handle customs at both ends?",
         f"Yes — we prepare export paperwork in {fn} and clear customs in {tn}, including transfer-of-residence and duty-relief claims where you qualify."),
        ("Is my shipment insured and tracked?",
         "Yes — all-risk transit insurance is available and you get door-to-door tracking with updates at every stage."),
    ]

# Rich bodies for key functional pages (slug -> (title, html_body_without_prose_wrapper, faqs))
def functional_pages():
    def p(x): return "".join(f"<p>{t}</p>" for t in x)
    return {
        "career": ("Careers at Universal Relocations",
            p(["Moving lives for a living is demanding, people-first work — and we hire for care as much as for skill. Across our hubs in the USA, India and the UAE, our teams plan international relocations, pack irreplaceable belongings, clear customs and look after families through one of life’s biggest transitions.",
               "We’re a FIDI/FAIM-accredited, FMC-licensed company that has been relocating corporate expatriates, diplomats and families for 28+ years. If you take pride in doing things properly and treating customers’ belongings as your own, you’ll fit in here."])
            + "<h2>Where we hire</h2>" + _ul([
                "Move coordination &amp; customer experience", "Packing, crating &amp; warehouse operations",
                "Customs documentation &amp; brokerage", "Sales &amp; corporate accounts",
                "Finance, HR &amp; administration"])
            + "<h2>Why work with us</h2>" + _ul([
                "A global brand with real career progression across three countries",
                "Training in international shipping, customs and FIDI/FAIM standards",
                "A supportive, people-first culture", "Stable, growing company with 28+ years in the industry"])
            + "<h2>How to apply</h2>" + p(["Send your CV and a short note about the role you’re interested in to <a href=\"mailto:contact@universalrelocations.com\">contact@universalrelocations.com</a> and our HR team will be in touch."]),
            [("Do I need moving-industry experience?", "Not always — we value attitude and customer care, and we train on the industry-specific skills. Relevant experience helps for specialist and coordination roles."),
             ("Which locations are you hiring in?", "We hire across our hubs in the USA, India and the UAE. Tell us where you’re based when you apply."),
             ("How do I apply?", "Email your CV to contact@universalrelocations.com with the role and location you’re interested in.")]),
        "referral": ("Refer a Friend — Rewards Program",
            p(["Love how we moved you? Send a friend our way and you both benefit. Our referral program is our way of saying thank you to the customers who recommend us — and most of our business comes from exactly those word-of-mouth introductions.",
               "It’s simple: introduce someone who’s planning a move, and once their move completes, we reward you both."])
            + "<h2>How it works</h2>" + _steps([
                "Tell us who to contact — share their name and the best way to reach them, or have them mention you.",
                "We look after their move with the same care we gave yours.",
                "When their move completes, you both receive your referral reward."])
            + "<h2>Who can refer?</h2>" + p(["Anyone — past customers, friends, family and colleagues. There’s no limit on how many people you can refer."])
            + "<div style=\"margin:20px 0\"><a class=\"btn btn-primary\" href=\"/contact-us/\">Refer someone now</a></div>",
            [("What’s the referral reward?", "Both you and the person you refer receive a reward once their move completes. Contact us for the current offer and terms."),
             ("Is there a limit to how many people I can refer?", "No — refer as many friends, family or colleagues as you like."),
             ("When do I receive my reward?", "After your referral’s move is completed. We’ll be in touch to arrange it.")]),
        "file-a-claim": ("File a Claim",
            p(["We take exceptional care of every shipment — but if something arrives damaged or missing, we’re here to put it right quickly and fairly. Starting a claim is straightforward, and your coordinator guides you through every step.",
               "To help us resolve things as fast as possible, report any issue as soon as you notice it and keep the affected items and their packing until the claim is assessed."])
            + "<h2>How to file a claim</h2>" + _steps([
                "Contact your move coordinator or email contact@universalrelocations.com as soon as possible.",
                "Describe the item(s) affected and the nature of the loss or damage.",
                "Share supporting photos and keep the item and its packaging for inspection.",
                "We assess the claim against your inventory and insurance and confirm the resolution."])
            + "<h2>What you’ll need</h2>" + _ul([
                "Your move reference or inventory number", "A description of the affected item(s)",
                "Photographs of the damage and packaging", "Your transit-insurance details, if applicable"])
            + "<div style=\"margin:20px 0\"><a class=\"btn btn-primary\" href=\"/contact-us/\">Start your claim</a></div>",
            [("How soon should I report damage?", "As soon as you notice it — prompt reporting helps us resolve claims faster and is often required by insurance terms."),
             ("What should I keep for the claim?", "Keep the damaged item and its original packaging until the claim is assessed, and take clear photos."),
             ("Will insurance cover my claim?", "If you took transit insurance, covered loss or damage is handled per your policy. Your coordinator explains coverage and walks you through the process.")]),
        "resources": ("Moving Resources &amp; Guides",
            p(["Everything you need to plan a confident move — practical guides, checklists and glossaries built from 28+ years of moving families and businesses around the world."])
            + "<h2>Guides &amp; tools</h2>" + _ul([
                '<a href="/moving-check-list/">Moving checklist</a> — a week-by-week plan from first survey to final box',
                '<a href="/packing-tips/">Packing tips</a> — movers-approved ways to protect your belongings',
                '<a href="/moving-terms/">Moving terms</a> — plain-English glossary of estimate and paperwork terms',
                '<a href="/shipping-terms/">Shipping terms</a> — ocean and air freight vocabulary explained',
                '<a href="/moving-calculator/">Moving calculator</a> — estimate your volume and get a quote',
                '<a href="/faq/">FAQ</a> — answers to the questions we hear most'])
            + "<h2>Popular hubs</h2>" + _ul([
                '<a href="/usa/">Moving from the USA</a>', '<a href="/india/">Moving from India</a>',
                '<a href="/uae/">Moving from the UAE</a>']),
            [("How far ahead should I start planning?", "For international moves, 4–6 weeks is ideal; for local moves, 1–2 weeks. The earlier you book a survey, the more options you have."),
             ("What’s the best way to estimate my move size?", "Use our online Moving Calculator to add your items room-by-room for a cubic-feet and weight estimate, or book a free video survey."),
             ("Where do I find customs and documentation guidance?", "Your dedicated coordinator provides an exact checklist for your route, including transfer-of-residence paperwork where it applies.")]),
        "company-news": ("Company News",
            p(["The latest announcements, milestones, accreditations and press from Universal Relocations. We’ve been featured across leading business and news outlets for our work moving families and businesses worldwide.",
               "For media enquiries, partnership announcements or company updates, reach us at <a href=\"mailto:contact@universalrelocations.com\">contact@universalrelocations.com</a>."])
            + "<h2>Recognition &amp; accreditations</h2>" + _ul([
                "FIDI / FAIM accredited international mover", "FMC-licensed ocean transportation intermediary",
                "IAM &amp; IAM-DAB member", "IPATA-affiliated pet logistics", "ISO 9001 quality management"]),
            [("Where can I read about Universal Relocations in the press?", "We’ve been featured across major business and news outlets. Contact us for our latest press coverage and media kit."),
             ("How do I make a media enquiry?", "Email contact@universalrelocations.com and our team will respond promptly."),
             ("What accreditations do you hold?", "We’re FIDI/FAIM accredited, FMC-licensed, IAM and IPATA members, and ISO 9001 certified.")]),
    }


# ===========================================================================
# Interior design-system components (v2)
# ===========================================================================
_ICONS = {
  "box":'<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
  "ship":'<path d="M3 14l1.6 6h14.8L21 14M5 14V7l7-3 7 3v7M9 9h6M12 3v4"/>',
  "plane":'<path d="M21 15l-8-4V4a1.5 1.5 0 0 0-3 0v7l-8 4v2l8-2v4l-2 1.5V22l3-1 3 1v-1.5L12 19v-4l8 2z"/>',
  "truck":'<path d="M1 4h14v11H1zM15 8h4l3 3v4h-7M5.5 18a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM18.5 18a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"/>',
  "shield":'<path d="M12 2l8 3v6c0 5-3.5 8.5-8 11-4.5-2.5-8-6-8-11V5z"/><path d="M9 12l2 2 4-4"/>',
  "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  "globe":'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18"/>',
  "home":'<path d="M3 11l9-8 9 8M5 10v10h14V10M9 20v-6h6v6"/>',
  "paw":'<circle cx="7" cy="9" r="1.6"/><circle cx="12" cy="7.5" r="1.6"/><circle cx="17" cy="9" r="1.6"/><path d="M12 12c-3 0-5 2.2-5 4.5C7 18.4 8.6 19 12 19s5-.6 5-2.5C17 14.2 15 12 12 12z"/>',
  "car":'<path d="M3 13l2-5h14l2 5v5h-3v-2H6v2H3zM6 13h12"/><circle cx="7.5" cy="16.5" r="1.3"/><circle cx="16.5" cy="16.5" r="1.3"/>',
  "warehouse":'<path d="M3 21V8l9-4 9 4v13M7 21v-7h10v7"/>',
  "doc":'<path d="M6 2h8l4 4v16H6zM14 2v4h4M9 13h6M9 17h6"/>',
  "pin":'<path d="M12 22s-7-6-7-12a7 7 0 0 1 14 0c0 6-7 12-7 12z"/><circle cx="12" cy="10" r="2.5"/>',
  "star":'<path d="M12 3l2.7 5.5 6 .9-4.3 4.2 1 6-5.4-2.8L6.6 19.6l1-6L3.3 9.4l6-.9z"/>',
  "headset":'<path d="M4 13v-1a8 8 0 0 1 16 0v1M4 13a2 2 0 0 0-2 2v2a2 2 0 0 0 2 2h1v-6zM20 13a2 2 0 0 1 2 2v2a2 2 0 0 1-2 2h-1v-6M19 19a4 4 0 0 1-4 3h-3"/>',
  "award":'<circle cx="12" cy="9" r="6"/><path d="M9 14l-2 7 5-3 5 3-2-7"/>',
  "check":'<circle cx="12" cy="12" r="9"/><path d="M8 12l2.5 2.5L16 9"/>',
  "leaf":'<path d="M4 20C4 10 12 4 20 4c0 10-6 16-16 16zM4 20c3-5 7-8 11-9"/>',
  "cubes":'<path d="M12 2l5 3v6l-5 3-5-3V5zM7 11v6l5 3 5-3v-6"/>',
  "cal":'<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/>',
}
def icon(n):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round">{_ICONS.get(n, _ICONS["check"])}</svg>')

def sec_head(title, intro="", eyebrow=""):
    e = f'<div class="eyebrow">{eyebrow}</div>' if eyebrow else ''
    p = f'<p>{intro}</p>' if intro else ''
    return f'<div class="sec-head">{e}<h2>{title}</h2>{p}</div>'

def feature_cards(items, cols=""):
    cards = "".join(
        f'<div class="fcard"><div class="fic">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></div>'
        for ic, t, d in items)
    return f'<div class="feature-grid {cols}">{cards}</div>'

def media_row(img, title, body_html, reverse=False, illus=False):
    cls = "media-row reverse" if reverse else "media-row"
    imgcls = "mr-img illus" if illus else "mr-img"
    return (f'<div class="{cls}"><div class="mr-txt"><h2>{title}</h2>{body_html}</div>'
            f'<div class="{imgcls}"><img src="{img}" alt="{title}" loading="lazy"></div></div>')

# Themed illustration paths (always render, on-brand)
ILLUS = {k: f"/assets/svg/illus-{k}.svg" for k in
         ("ocean", "air", "global", "packing", "road", "warehouse")}
SVC_ILLUS = {"international":"global","corporate-relocation":"road","pet-relocations":"air",
  "groupage-solution":"ocean","storage":"warehouse","intrastate":"road","baggage-shipping":"packing",
  "insurance":"global","fine-art-relocations":"packing","hospitality-relocations":"warehouse","auto-shipping":"road"}
MODE_ILLUS = {"lcl":"ocean","fcl":"ocean","air-freight":"air","baggage":"packing","auto-shipping":"road","pet":"air"}
MODE_BODY = {"lcl":"PH_SHIP2","fcl":"PH_SHIP2","air-freight":"HERO_LOGISTICS","baggage":"HERO_MOVE2","auto-shipping":"PH_SHIP2","pet":"HERO_SURVEY"}

def lead_split(copy_html, stats):
    s = "".join(f'<div class="ls"><b>{n}</b><span>{l}</span></div>' for n, l in stats)
    return (f'<div class="lead-split"><div class="lead-copy">{copy_html}</div>'
            f'<div class="lead-stats">{s}</div></div>')

def callout(title, text, btn_label="Get a free quote", btn_href="/contact-us/",
            btn2_label="", btn2_href=""):
    b2 = f'<a class="btn btn-ghost" href="{btn2_href}" style="border-color:rgba(255,255,255,.6);color:#fff;margin-left:8px">{btn2_label}</a>' if btn2_label else ''
    return (f'<div class="callout"><div class="co-txt"><h3>{title}</h3><p>{text}</p></div>'
            f'<div><a class="btn btn-accent" href="{btn_href}">{btn_label}</a>{b2}</div></div>')

def step_cards(items):
    # items: list of (title, text)
    c = "".join(f'<div class="sc"><h4>{t}</h4><p>{d}</p></div>' for t, d in items)
    return f'<div class="step-cards">{c}</div>'

def isec(html, alt=False, head=""):
    return f'<section class="isec {"alt" if alt else ""}"><div class="container">{head}{html}</div></section>'

# Standard trust/stat + why-us content reused across pages
STATS = [("28+", "Years of experience"), ("300+", "Professionals worldwide"),
         ("4.5★", "Trustpilot · 2000+ reviews"), ("3", "Global hubs: USA · India · UAE")]
WHY_US = [
    ("award", "28+ years, FIDI/FAIM accredited", "Nearly three decades relocating families, diplomats and corporations — to FIDI/FAIM global quality standards."),
    ("globe", "Our own hubs on both ends", "Offices and crews across the USA, India and the UAE mean one team owns your move door-to-door."),
    ("shield", "FMC-licensed &amp; fully insured", "An FMC-licensed ocean carrier with all-risk transit insurance, so your belongings are protected the whole way."),
    ("headset", "One dedicated coordinator", "A single point of contact plans your timing, paperwork and delivery — and answers when you call."),
    ("doc", "In-house customs &amp; TR", "We prepare every document and clear customs ourselves, including Transfer of Residence and duty relief."),
    ("clock", "Door-to-door tracking", "Live updates at every stage, from survey and packing to customs and final delivery."),
]
# SFL-style dark stat band — every figure is sourced from universalrelocations.com:
#  "28 Years of Expertise" / founded 1998; "300+ skilled professionals globally";
#  offices across 3 countries (USA, India, UAE) each with own crew, warehouse &
#  in-house customs brokers; Trustpilot 4.5 based on 2000+ reviews.
WHY_SHIP = [
    ("28+", "Years of Experience",
     "A one-stop relocation service since 1998 — grown from one man with one truck into a global mover."),
    ("300+", "Professionals Worldwide",
     "A dedicated team of 300+ skilled professionals across our own offices."),
    ("3", "Global Hubs",
     "Own offices, crews, warehouses and in-house customs brokers in the USA, India and the UAE."),
    ("4.5★", "Rated on Trustpilot",
     "A 4.5 rating based on 2000+ customer reviews."),
]
def why_us_band(alt=True):
    cards = "".join(
        f'<div class="ws-card"><div class="ws-top"><span class="ws-num c{i}">{n}</span>'
        f'<h3>{t}</h3></div><p>{d}</p></div>'
        for i, (n, t, d) in enumerate(WHY_SHIP))
    head = ('<div class="ws-head"><div class="eyebrow">Why Universal Relocations</div>'
            '<h2>Why move with Universal Relocations</h2></div>')
    return (f'<section class="isec why-ship"><div class="container">{head}'
            f'<div class="ws-grid">{cards}</div></div></section>')


GEN_STEPS = [
    ("Free survey", "Video or in-home survey to scope your move and give a firm, itemised quote."),
    ("Plan &amp; pack", "A dedicated coordinator plans timing and paperwork; our crews pack to export grade."),
    ("Ship &amp; clear", "We ship by the best method and clear customs at both ends, including TR relief."),
    ("Deliver &amp; settle", "Door delivery, unpacking, reassembly and debris removal at your new home."),
]
def check_grid(items):
    c = "".join(f'<div class="ck">{icon("check")}<span>{t}</span></div>' for t in items)
    return f'<div class="check-grid">{c}</div>'
def faq_isec(faqs, alt=False):
    if not faqs: return ""
    return isec(faq_block(faqs, ""), alt=alt, head=sec_head("Frequently asked questions", "", "FAQ"))
def cta_isec():
    return isec(callout(
        "Ready to plan your move?",
        "Get a free, no-obligation quote from our move consultants — or estimate your volume in minutes.",
        "Get a free quote", "/contact-us/", "Moving Calculator", "/moving-calculator/"))
# Service -> primary icon for cards
SVC_ICON = {"international":"globe","corporate-relocation":"truck","pet-relocations":"paw",
  "groupage-solution":"ship","storage":"warehouse","intrastate":"home","baggage-shipping":"box",
  "insurance":"shield","fine-art-relocations":"star","hospitality-relocations":"cubes","auto-shipping":"car"}


# ===========================================================================
# Deep shared content blocks (to make every page comprehensive)
# ===========================================================================
COST_FACTORS = [
    ("Volume or weight", "The single biggest factor. Sea freight (LCL) is priced on the cubic feet/metres your goods occupy; FCL on the container size; air freight on chargeable weight. The more you move, the more it costs — which is why a pre-move survey and decluttering pay off."),
    ("Service level", "Full-pack (we pack everything), partial-pack, or you-pack change the labour and materials. Specialist crating for art, pianos or marble adds cost but protects irreplaceable items."),
    ("Origin &amp; destination access", "Stairs, long carries, narrow streets, shuttle vehicles for large trucks, parking permits and high-floor deliveries all affect the quote. Tell us about access up front so there are no surprises."),
    ("Shipping mode &amp; speed", "Air is fastest and dearest; sea is slower and cheapest; a split shipment (a little by air, the rest by sea) balances the two."),
    ("Customs, duties &amp; TR", "Household goods often enter duty-free under Transfer of Residence rules if you qualify, but new items, vehicles and certain goods can attract duty. We confirm what applies before you ship."),
    ("Insurance &amp; extras", "All-risk transit insurance, storage, handyman services and vehicle or pet shipping are optional add-ons priced on what you choose."),
]
MOVE_DOCS = [
    "Valid passport (and visa or residence permit for the destination)",
    "A detailed packing inventory / valued inventory for insurance",
    "Transfer of Residence (TR) / returning-resident paperwork where you qualify",
    "Proof of residence at origin and destination (lease, utility bill or similar)",
    "For vehicles: title, registration and purchase documents",
    "For pets: microchip, vaccination record, health certificate and import permit",
]
PROHIBITED = [
    "Cash, jewellery, important documents and other irreplaceables (carry these yourself)",
    "Flammables, aerosols, gas cylinders, paints and solvents",
    "Firearms, ammunition and explosives", "Perishable food and open liquids",
    "Plants, seeds and some foodstuffs (destination quarantine rules vary)",
    "Illegal or restricted substances of any kind",
]
def prose_section(title, paras, eyebrow=""):
    body = "".join(f"<p>{p}</p>" for p in paras)
    return isec(f'<div class="prose">{body}</div>', head=sec_head(title, "", eyebrow))

def cost_timeline_section(subject="your move", alt=True):
    cards = feature_cards([("cubes", t, d) for t, d in COST_FACTORS[:3]] )
    cards2 = feature_cards([("doc", t, d) for t, d in COST_FACTORS[3:]])
    return isec(cards + '<div style="height:20px"></div>' + cards2, alt=alt,
        head=sec_head(f"What affects the cost of {subject}",
            "No two moves are the same — here's what shapes your quote, and why a free survey gives you a firm, honest price.", "Pricing"))

def docs_section(alt=False):
    return isec(
        '<div class="prose" style="max-width:none"><h2>Documents &amp; customs</h2>'
        '<p>We prepare and lodge the paperwork, but having these ready keeps your move on schedule. '
        'Your coordinator sends an exact checklist for your route, including any Transfer of Residence or '
        'duty-relief you qualify for.</p></div>'
        + check_grid(MOVE_DOCS)
        + '<div style="height:30px"></div>' + restrictions_block(),
        alt=alt, head="")

# Expanded FAQ banks (more comprehensive)
EXTRA_FAQS = [
    ("Will you disassemble and reassemble my furniture?", "Yes — our crews dismantle beds, wardrobes, tables and other large items for transit and reassemble them at delivery as part of a full-service move."),
    ("Can I pack some things myself?", "Of course. Owner-packed cartons are fine; note that insurance on self-packed boxes may differ from professionally packed items, which your coordinator will explain."),
    ("What happens on moving day?", "Our team arrives, protects floors and doorways, packs and wraps room by room, labels and inventories every item, and loads carefully. You get a copy of the inventory before we leave."),
    ("Do you offer storage if my dates don’t line up?", "Yes — secure, climate-controlled storage for a few days or several months, with your inventory tracked and redelivery whenever you’re ready."),
    ("How do you protect fragile and valuable items?", "Export-grade materials, double-wall cartons, custom crating for art and high-value pieces, and all-risk insurance so you’re covered door-to-door."),
]


# ===========================================================================
# Competitor-grade polish modules: trust logos, comparison table, rules
# ===========================================================================
def trust_logos(g, alt=True):
    IMG = g["IMG"]
    logos = [("FIDI","01-fidi"),("FAIM","02-faim"),("IAM","03-iamx"),("IAM-DAB","04-iam-dab"),
             ("PAIMA","05-paima"),("IPATA","06-ipata"),("ARA","07-ara"),("FIDI-PCG","08-fidi-pcg"),
             ("FMC","09-fmc"),("ISO 9001","10-iso-9001")]
    imgs = "".join(f'<div class="trust-card"><img src="{IMG}/2026/10/{f}.png" alt="{n}" loading="lazy"></div>' for n, f in logos)
    # duplicate the set so the marquee loops seamlessly (translateX -50%)
    return isec(f'<div class="trust-strip"><div class="trust-track">{imgs}{imgs}</div></div>', alt=alt,
        head=sec_head("Accredited, licensed and trusted",
            "Our work is held to the world’s leading moving and quality standards.", "Credentials"))

# ---- Core Strengths (capabilities; value props from universalrelocations.com) ----
CORE_STRENGTHS = [
    ("award", "28+ years of expertise", "International moving since 1998 — seasoned experts across every kind of relocation."),
    ("globe", "Our own global network", "Offices, crews, warehouses and in-house customs brokers in the USA, India and the UAE."),
    ("ship", "One-stop relocation service", "International, interstate and intrastate moving — packing, shipping, customs and delivery under one roof."),
    ("clock", "Real-time door-to-door tracking", "Follow your shipment at every stage, from survey and packing to customs and final delivery."),
    ("headset", "24/7 online support", "Assistance at every click, whenever you need it, wherever you are."),
    ("shield", "Licensed &amp; accredited", "An FMC-licensed NVOCC, FIDI/FAIM accredited and ISO 9001 certified."),
]
def core_strengths():
    cards = "".join(
        f'<div class="cs-card"><div class="cs-ic">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></div>'
        for ic, t, d in CORE_STRENGTHS)
    return isec(f'<div class="cs-rail">{cards}</div>', alt=False,
        head=sec_head("Our core strengths",
            "What makes Universal Relocations a trusted one-stop relocation partner.", "Why us"))

def prompt_band(chips=None, title="Start your move in seconds",
                sub="Tell us what you’re moving and where — our assistant builds your estimate instantly."):
    if chips is None:
        chips = [("I want to move my 3 bedroom apartment from New York to Delhi", "Move a 3-bedroom, New York → Delhi"),
                 ("I want to ship 5 boxes of 25 kg each from Chennai to San Francisco", "Ship 5 boxes, Chennai → San Francisco"),
                 ("I want to move my car from Dubai to Toronto", "Move a car, Dubai → Toronto"),
                 ("How much will it cost to move 10 boxes from Dallas to Abu Dhabi", "10 boxes, Dallas → Abu Dhabi")]
    chip_html = "".join(f'<button class="hs-chip" data-prompt="{p}">{l}</button>' for p, l in chips)
    return (f'<section class="isec book-band"><div class="container"><div class="book-head">'
            f'<div class="eyebrow">Instant estimate</div><h2>{title}</h2><p>{sub}</p></div>'
            '<form class="hero-prompt" id="hero-prompt-form">'
            '<input id="hero-prompt-input" type="text" autocomplete="off" placeholder="e.g. Move a 3-bedroom from New York to Delhi" aria-label="Describe your move">'
            '<div class="hero-prompt-actions">'
            '<button type="button" class="hp-icon" id="hp-mic" aria-label="Voice input"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0014 0M12 17v4"/></svg></button>'
            '<button type="submit" class="hp-go" aria-label="Start"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>'
            '</div></form>'
            f'<div class="hero-suggest"><span class="hs-label">Try:</span>{chip_html}</div>'
            '</div></section>')

ALLOWED = [
    "Household furniture, appliances and white goods", "Clothing, linens, books and personal effects",
    "Kitchenware, crockery and cookware", "Electronics and home-entertainment equipment",
    "Children’s furniture, toys and sporting goods", "Tools, bicycles and hobby equipment",
    "Artwork, antiques and instruments (with specialist packing)", "Vehicles (as a separate or combined shipment)",
]
def restrictions_block():
    return (
        '<div class="rules-cols">'
        '<div class="rule-card allow"><h3>What you can ship <span class="tag ok">Allowed</span></h3>'
        + "<ul>" + "".join(f"<li>{i}</li>" for i in ALLOWED) + "</ul></div>"
        '<div class="rule-card deny"><h3>What not to ship <span class="tag no">Prohibited / restricted</span></h3>'
        + "<ul>" + "".join(f"<li>{i}</li>" for i in PROHIBITED) + "</ul></div>"
        '</div>')

def compare_table():
    rows = [
        ("LCL (groupage)", "Studios &amp; 1-bed loads", '<span class="pill slow">Weeks (sea)</span>', "Lowest for small loads", "/services/groupage-solution/"),
        ("FCL (full container)", "2-bed homes &amp; larger", '<span class="pill mid">Faster (sea)</span>', "Best value for full homes", "/services/international/"),
        ("Air freight", "Urgent &amp; essential items", '<span class="pill fast">Days</span>', "Priced on weight", "/services/baggage-shipping/"),
        ("Baggage / boxes", "A few boxes or bags", '<span class="pill mid">Air or sea</span>', "Per box, no excess fees", "/services/baggage-shipping/"),
    ]
    body = "".join(
        f'<tr><td>{n}</td><td>{b}</td><td>{t}</td><td>{c}</td><td><a class="more" style="color:var(--blue);font-weight:600" href="{h}">Learn more &rarr;</a></td></tr>'
        for n, b, t, c, h in rows)
    return isec('<div class="cmp-wrap"><table class="cmp">'
        '<thead><tr><th>Shipping option</th><th>Best for</th><th>Transit time</th><th>Cost</th><th></th></tr></thead>'
        f'<tbody>{body}</tbody></table></div>', alt=True,
        head=sec_head("Which shipping option is right for you?",
            "LCL, FCL, air or baggage — compare at a glance, then we’ll confirm the best fit for your volume and timeline.", "Compare"))


# ===========================================================================
# Moving checklist — full week-by-week timeline (content from universalrelocations.com)
# ===========================================================================
CHECKLIST = [
    ("8 Weeks Before", [
        "Inventory your belongings and clear out the attic, basement and storage shed",
        "Use up items you can’t move, such as frozen food and cleaning supplies",
        "Research your new community through the local Chamber of Commerce or tourism bureau",
        "Contact Universal Relocations to arrange your moving day and review insurance coverage"]),
    ("6 Weeks Before", [
        "If your employer is paying, confirm its expense and responsibility terms",
        "Check with the IRS or an accountant about tax-deductible moving expenses",
        "Decide what to sell or donate, and list who needs to be notified of your move",
        "Subscribe to a local paper in your new area; locate vehicle registration and licensing documents",
        "Arrange storage if needed; collect records from schools, doctors, dentists, lawyers and accountants"]),
    ("4 Weeks Before", [
        "Submit a change of address to the post office",
        "Arrange pet relocation if needed",
        "Schedule utility disconnections — but keep phone and utilities on until moving day",
        "Arrange insurance (auto, home, medical, life) for your new home",
        "If packing yourself, buy boxes and start packing items you won’t need"]),
    ("3 Weeks Before", [
        "Book travel, but avoid flights on moving day — closings and delays are common",
        "Gather important papers: insurance policies, wills, deeds and stock certificates",
        "Close local bank accounts and open accounts in your new location"]),
    ("2 Weeks Before", [
        "Have your car serviced and prepared for the weather on your route",
        "Schedule elevator use with building management if applicable",
        "Confirm all arrangements with your relocation consultant"]),
    ("1 Week Before", [
        "Settle outstanding bills with local merchants",
        "Empty your safe deposit box; pick up dry cleaning; return library books and rentals",
        "Take pets for needed immunizations and obtain their veterinary records",
        "Drain fuel and oil from power equipment; give away plants that won’t be moving",
        "Prepare directions, an itinerary and emergency numbers for the moving company"]),
    ("2–3 Days Before", [
        "Defrost the freezer and refrigerator; block open doors to keep pets and children safe",
        "Have major appliances disconnected and prepared",
        "Pack a box of immediately needed items to load last or carry with you",
        "Separate the items you’re taking yourself and confirm the moving van’s arrival time"]),
    ("Moving Day", [
        "Have someone at home to answer the van foreman’s questions",
        "Record utility meter readings for gas, electric and water",
        "Read the bill of lading and inventory carefully before signing",
        "Keep your paperwork until all charges are paid and any claims are settled"]),
]
def checklist_timeline():
    cards = ""
    for i, (when, items) in enumerate(CHECKLIST):
        lis = "".join(f"<li>{x}</li>" for x in items)
        cards += (f'<div class="tl-item"><div class="tl-dot">{i+1}</div>'
                  f'<div class="tl-card"><h3>{when}</h3><ul>{lis}</ul></div></div>')
    return f'<div class="timeline">{cards}</div>'

def build_checklist_page(g):
    interior = g["interior"]; write = g["write"]
    faqs = [
        ("When should I start planning my move?", "Start about eight weeks out for an international or long-distance move — inventorying, decluttering and booking your survey early gives you the most options and the smoothest move."),
        ("Do I need to be home on moving day?", "Yes — have someone at home to answer the crew’s questions, record utility meter readings, and check and sign the inventory and bill of lading before the van leaves."),
        ("What should I carry myself rather than ship?", "Cash, jewellery, important documents, medication and a box of immediately needed items. Keep these with you rather than in the shipment."),
        ("Can Universal Relocations handle the packing for me?", "Absolutely — full and partial packing, materials and specialist crating are all available, so you can hand over as much of this checklist as you like."),
    ]
    inner = (
        isec('<div class="prose" style="max-width:820px;margin:0 auto;text-align:center">'
             '<p style="font-size:1.12rem">A great move is a planned move. This week-by-week checklist — refined over '
             '28+ years of international and domestic relocations — keeps every task on track so nothing is forgotten. '
             'Print it, work down it, and lean on your Universal Relocations coordinator for anything on the list.</p></div>')
        + isec(checklist_timeline(), alt=True, head=sec_head("Your week-by-week moving timeline",
               "From eight weeks out to moving day.", "Countdown"))
        + isec(media_row(g["HERO_MOVE1"], "Let us take the heavy items off your list",
               '<p>Every task on this checklist that involves packing, shipping, customs or delivery, we can handle for you '
               '— so your move is organised, insured and tracked from the first box to the last.</p>'
               + _ul(["Export-grade packing &amp; crating", "Ocean &amp; air freight with customs handled",
                      "Storage if your dates don’t line up", "All-risk transit insurance"])))
        + why_us_band()
        + trust_logos(g, alt=True)
        + faq_isec(faqs)
        + cta_isec())
    write("moving-check-list", interior("Moving Checklist",
          [("Home", "/"), ("Resources", "/resources/"), ("Moving Checklist", "")], inner,
          "A complete week-by-week moving checklist from Universal Relocations — plan your move so nothing is forgotten.",
          hero_img=g["HERO_SURVEY"], extra_head=faq_schema(faqs),
          subtitle="Everything to do, week by week, so nothing is forgotten.", raw=True))
    print("Checklist page built.")


# ---- Orange "by the numbers" band (figures provided by the site owner) ----
BIG_STATS = [("28+", "Years of Experience"), ("100+", "Countries Covered"),
             ("440k+", "Satisfied Clients"), ("52MM+", "Tons Moved")]
def orange_stats():
    cells = "".join(
        f'<div class="os-cell"><div class="os-num">{n}</div>'
        f'<div class="os-label">{l}</div></div>' for n, l in BIG_STATS)
    return f'<section class="os-band"><div class="container"><div class="os-grid">{cells}</div></div></section>'
