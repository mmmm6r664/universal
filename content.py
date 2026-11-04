"""Rich reconstructed content for key legal/company pages, pulled from the live site.
NOTE: legal pages are reconstructed faithfully from the live site's structure and
substance; confirm exact binding wording before relying on them legally.
Imported by pages.py -> build().  Each value is inner HTML for the .prose block.
"""

def _ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

COMPANY = """
<p style="font-size:1.1rem">Established in 1998, Universal Relocations grew from a local mover into a globally recognized, multi-national relocation company with offices in the USA, India and the UAE. With our own trucks, warehouses and customs brokers, we deliver moves built on efficiency, reliability and client satisfaction.</p>
<p>Today a team of 300+ professionals moves families and businesses across the world, integrating new technology into every relocation to make the experience seamless from first survey to final delivery.</p>
<h2>Our Mission</h2>
<p>To offer seamless, secure and personalized international moving solutions — built on strategic partnerships, smart technology and genuine environmental stewardship.</p>
<h2>Our Vision</h2>
<p>To lead the industry in service quality, innovation and customer satisfaction, and to be a trusted name built on excellence and integrity.</p>
<h2>Our Core Values</h2>
""" + _ul([
    "<b>Passionate Global Connectors</b> — treating every international move as a personal, positive experience.",
    "<b>Precision in Motion</b> — careful planning and execution at every stage.",
    "<b>Innovation Navigators</b> — developing new solutions that set industry standards.",
    "<b>Sustainability Champions</b> — reducing environmental impact through eco-friendly packaging and logistics.",
    "<b>Cultural Bridge Builders</b> — fostering cross-cultural understanding.",
]) + """
<h2>Offices &amp; Credentials</h2>
<p><b>USA:</b> New Jersey, California, Texas, Georgia, Maryland &nbsp; · &nbsp; <b>India:</b> Bangalore, Chennai, Mumbai, Hyderabad, Delhi &nbsp; · &nbsp; <b>UAE:</b> Dubai</p>
<p>Licensed and accredited through the FMCSA, applicable state authorities and the U.S. Federal Maritime Commission, with industry affiliations including FIDI, IAM, PAIMA, IPATA, ARA and ISO 9001.</p>
"""

ABOUT = COMPANY  # about-us mirrors the company narrative

CSR = """
<p style="font-size:1.1rem">Universal Relocations is deeply committed to making a positive impact on society and the environment. Our Corporate Social Responsibility program spans sustainability, community engagement and responsible business practices.</p>
<h2>Our CSR Pillars</h2>
""" + _ul([
    "<b>Community Engagement &amp; Enrichment</b> — supporting education, healthcare and well-being through partnerships, local schools and clean-up campaigns.",
    "<b>Environmental Stewardship</b> — reducing our carbon footprint with eco-friendly packaging and energy-efficient logistics.",
    "<b>Ethical Business Practices</b> — a commitment to business ethics, transparency and accountability.",
    "<b>Supporting Global Causes</b> — disaster relief and humanitarian aid through reputable organizations.",
    "<b>Employee Wellbeing &amp; Development</b> — investing in the people who move lives for a living.",
]) + """
<h2>CSR in Action</h2>
""" + _ul([
    "Beach clean-up drives for World Environment Day, removing waste and plastic from coastlines.",
    "COVID-19 oxygen support — 100 oxygen cylinders shipped from the USA to India free of cost.",
    "Blood donation camps for World Blood Donor Day.",
    "Government school renovation — volunteers painted and refreshed a local school.",
    "School supply kits assembled and distributed to children in orphanages.",
    "Seed Ball Drive to help restore natural habitats.",
]) + """
<h2>Green Moving Tips</h2>
""" + _ul([
    "Use recyclable or biodegradable packing materials.",
    "Downsize before you move.",
    "Choose energy-efficient transport.",
    "Label boxes for smarter, faster unpacking.",
    "Recycle electronics responsibly.",
])

ENVIRONMENTAL = """
<p style="font-size:1.1rem">Universal Relocations accepts a moral and legal duty to ensure our activities, products and services benefit the environment in the communities where we operate, and to avoid operations that could harm those communities or the environment.</p>
<p>We work with our customers, suppliers and communities on environmental improvement and pollution prevention. Our goals include:</p>
""" + _ul([
    "Reducing waste through better work practices and recycling.",
    "Cutting the pollutants our operations produce.",
    "Limiting our impact on neighboring communities.",
    "Replacing harmful materials, equipment and technology with more environmentally acceptable options.",
    "Requiring suppliers to follow sound environmental policies.",
    "Promoting environmental awareness among staff, clients and the public.",
]) + """
<h2>Responsibilities</h2>
<p>Management holds overall responsibility for environmental sustainability and accountability for carrying out this policy, including:</p>
""" + _ul([
    "Implementing all environmental policies and procedures.",
    "Complying with environmental laws and standards at local, national and international levels.",
    "Setting measurable targets for continuous improvement and the reduction of waste, pollution and environmental harm.",
    "Acting responsibly toward people, communities and resources.",
    "Encouraging consultation and cooperation among management, employees and stakeholders.",
    "Providing adequate resources for these commitments.",
]) + """
<h2>Employee Responsibilities</h2>
<p>Employees are expected to follow all environmental policies and procedures, report hazards that could affect the environment, act responsibly at all times, and help maintain an environmentally friendly workplace.</p>
"""

PRIVACY = """
<p style="font-size:1.1rem">This policy covers the non-public personal information Universal Relocations collects while providing moving and shipping services for personal, family or household purposes.</p>
<h2>How We Collect Personal Information</h2>
<p>We collect information through website forms, support chat, cookies and tracking technologies, emails, offline interactions (phone, mail, in person), transactions with Universal Relocations Group companies, and employers or others you authorize.</p>
<h2>Children</h2>
<p>We do not knowingly collect children's information and will delete it if it is disclosed without proper parental consent.</p>
<h2>Information We Collect</h2>
<p>Names, shipping-from and shipping-to addresses, email addresses, phone numbers, and lists of items to be shipped.</p>
<h2>How We Use Information</h2>
""" + _ul([
    "Sharing with border security, government agencies, shipping partners and affiliates for customs clearance and delivery.",
    "Providing shipping and moving services.",
    "Communicating with you about your services.",
    "Sending shipment tracking information and links.",
    "Improving our website and the user experience.",
]) + """
<h2>Sharing Within the Universal Relocations Group</h2>
<p>Information may be shared among group companies to facilitate customs clearance and delivery, provide the full range of relocation services, and make service recommendations.</p>
<h2>Sharing Outside the Group</h2>
<p>Sharing outside the group is limited to legal or regulatory requirements (such as customs and government disclosures), the shipping partners and agents needed to fulfill your services, and service providers (IT, cloud storage, logistics) who must follow confidentiality and data-protection requirements. We do not sell personal information or share it for unrelated third-party marketing.</p>
<h2>SMS Consent</h2>
<p>Phone numbers and SMS consent are never shared or sold to third parties or affiliates for marketing. SMS data is used only for the purposes you expressly consented to. See our <a href="/sms-terms-of-service/">SMS Terms of Service</a>.</p>
<h2>Verification &amp; Contact</h2>
<p>We use employee training, internal procedures, regular compliance reviews, and a Privacy Officer responsible for implementation. Privacy questions can be sent to <a href="mailto:claims@universalrelocations.com">claims@universalrelocations.com</a> or by phone at 1-888-323-7356.</p>
<h2>Dispute Resolution</h2>
<p>Complaints are first addressed internally. If unresolved, they may be referred to the independent alternative dispute-resolution services of the Moving Authority Associations at (702) 333-2430.</p>
"""

SMS = """
<p style="font-size:1.1rem">By opting in to receive SMS messages from Universal Relocations, you agree to these terms and consent to receive texts. Participation is voluntary and you may opt out at any time.</p>
<h2>Types of Messages</h2>
<p>Shipment reminders, follow-ups, billing inquiries and shipment tracking links.</p>
<h2>Message Frequency</h2>
<p>Frequency varies based on your engagement and message type. You may receive up to 5 messages per week about your shipment, billing or tracking.</p>
<h2>Fees &amp; Charges</h2>
<p>Standard message and data rates may apply based on your mobile carrier plan. Domestic and international rates may differ.</p>
<h2>Opt-In &amp; Opt-Out</h2>
""" + _ul([
    "<b>Opt in</b> by submitting an online form.",
    "<b>Opt out</b> by replying STOP to any message, or by contacting us to be removed.",
    "<b>Help</b> by replying HELP or contacting us for assistance.",
    "To avoid SMS messages entirely, leave the SMS consent box unchecked on our forms.",
]) + """
<h2>Standard Messaging Disclosures</h2>
<p>Message and data rates may apply. Message frequency may vary. Text STOP to opt out, or HELP for assistance. See our <a href="/privacy-policy/">Privacy Policy</a> and <a href="/terms-and-condition/">Terms &amp; Conditions</a>.</p>
<h2>Privacy</h2>
<p>Phone numbers collected for SMS consent are not shared with third parties or affiliates for marketing.</p>
<h2>Changes &amp; Contact</h2>
<p>We may modify these terms at any time; changes take effect immediately once posted. Questions: contact us via the website, call 1-888-323-7356, or email <a href="mailto:claims@universalrelocations.com">claims@universalrelocations.com</a>.</p>
"""

REFUND = """
<p style="font-size:1.1rem">This policy covers international, domestic and local moves. A booking is confirmed once a deposit is paid or the quotation is accepted. Cancellation and refund requests must be made in writing by email — verbal or phone cancellations are not valid unless confirmed in writing.</p>
<h2>Cancellation Before Service Commencement</h2>
<p>The refund depends on how far ahead of the pick-up date you cancel:</p>
""" + _ul([
    "<b>More than 7 days:</b> full refund, minus administrative or third-party fees.",
    "<b>4–7 days:</b> 25% of the quotation is retained.",
    "<b>48–72 hours:</b> 50% is retained.",
    "<b>Within 24 hours / pick-up day:</b> 75% is retained.",
    "<b>After packing or collection has started:</b> no refund.",
]) + """
<p>Administrative fees may include survey costs, labor and scheduling, port or trucking reservations, and customs, insurance or documentation fees already processed.</p>
<h2>Cancellation After Service Commencement</h2>
<p>Once packing, loading or transport has begun, no full refund is issued. You pay actual expenses incurred, plus any demurrage, detention or storage costs caused by the cancellation. Shipments already in transit or at port cannot be recalled without carrier approval, and those costs are also your responsibility.</p>
<h2>Refund Process &amp; Timeline</h2>
<p>Approved refunds are processed within 15–20 business days of written management approval, to the original payment method or by bank transfer, and only to the payer of record. Bank charges, wire fees and currency-conversion losses are non-refundable.</p>
<h2>Non-Refundable Items</h2>
""" + _ul([
    "Insurance premiums after coverage activates.",
    "U.S. Customs and international documentation fees.",
    "Third-party and port handling charges.",
    "Billed warehouse or storage fees.",
    "Fuel surcharges and trucking or port booking deposits.",
    "Survey or administrative coordination fees.",
]) + """
<h2>Postponement or Rescheduling</h2>
<p>Postponement requests are accommodated based on crew and equipment availability. Rescheduling within 72 hours of pick-up may incur a fee of 10–15% of the quote. Postponement does not waive cancellation fees unless a new confirmed date is given within 30 days of the original booking.</p>
<h2>Force Majeure</h2>
<p>We are not liable for disruptions beyond our control — natural disasters, strikes, government restrictions, port congestion, carrier delays, or customs and quarantine holds. Refunds in these cases are reviewed case by case.</p>
<h2>Dispute Resolution &amp; Contact</h2>
<p>Disagreements may be filed through the Moving Authority Arbitration Program, a U.S. Department of Transportation-mandated neutral process. Customer Support: 1-888-323-7356 or <a href="mailto:info@universalrelocations.com">info@universalrelocations.com</a>, Monday–Friday, 9:00 AM–6:00 PM local office time.</p>
"""

TERMS = """
<p style="font-size:1.1rem">In these terms, "you" means the Customer and "we" means the Remover. The clauses below govern our quotation, each party's responsibilities, liability for loss or damage, and the handling of your goods.</p>
<h2>1. Our Quotation</h2>
<p>Quotes exclude customs duties and government fees, and may change for circumstances such as quotes not accepted within 28 days, currency or freight changes, weekend or out-of-hours work, and access problems.</p>
<h2>2. Work Not Included</h2>
<p>Excludes tasks such as dismantling flat-pack furniture, disconnecting appliances, lifting fitted floor coverings, and moving items from lofts unless access is safe.</p>
<h2>3. Your Responsibility</h2>
<p>You must declare goods' value in writing, obtain permits, be present or represented during collection and delivery, sign documents, protect goods left in unattended premises, and prepare appliances.</p>
<h2>4. Our Responsibility</h2>
<p>Goods should be delivered in the condition they were packed. Liability depends on the liability option chosen and on negligence or breach of contract.</p>
<h2>5. Prohibited &amp; Restricted Items</h2>
<p>Hazardous items such as gas bottles are never moved. Valuables, perishables, animals and goods needing export licenses are excluded or require your own arrangements.</p>
<h2>6. Ownership of Goods</h2>
<p>You warrant that you own the goods or have authority from the owners, and will cover claims arising from a breach of this warranty.</p>
<h2>7. Postponement or Cancellation Charges</h2>
<p>Fees depend on notice given, ranging from no charge with more than 10 working days' notice to a higher percentage of the removal charge with short notice. See our <a href="/cancel-and-refund-policy/">Cancellation &amp; Refund Policy</a>.</p>
<h2>8. Payment</h2>
<p>Payment in cleared funds is due in advance, and no part of the agreed price may be withheld.</p>
<h2>9. Liability Limits</h2>
<p>Standard Liability (with a declared value and additional fee) and Limited Liability (a per-item cap) apply, with separate rules for international shipments.</p>
<h2>10–12. Damage, Exclusions &amp; Claim Time Limits</h2>
<p>Liability for damage to property other than goods is limited to repairing the affected area, and must be noted on the paperwork or reported in writing within five days. Exclusions include fire, war and similar events under Limited Liability. Concealed damage must be reported within three days of delivery; written claims within nine months; and legal action within two years of a declined claim.</p>
<h2>13–25. Further Terms</h2>
<p>Additional clauses cover transit delays, our right to hold goods until charges are paid (lien), subcontracting, choice of route and method (including shared vehicle or container space), international removals advice, applicable law, forwarding address, inventories, storage-charge revisions, a war clause, sale or disposal of goods after non-payment, termination, and declined card authorizations.</p>
<p style="font-size:.86rem;color:var(--muted);margin-top:24px">For the complete, binding wording of any clause, please contact us.</p>
"""

# ---------------------------------------------------------------------------
# Destinations — countries served + the standard move process
# ---------------------------------------------------------------------------
PROCESS = _ul([
    "<b>Request a free quote</b> — tell us your origin, destination, move date and shipment size.",
    "<b>Talk to a move consultant</b> — we go over your route, priorities and service options.",
    "<b>Complete a survey</b> — virtual or in person, so we can confirm volume and an exact price.",
    "<b>We pack &amp; collect</b> — export-grade packing and careful collection of your goods.",
    "<b>Shipping &amp; documentation</b> — we coordinate ocean/air freight and all customs paperwork for your route.",
    "<b>Destination delivery</b> — door-to-door delivery and unpacking, per the service you choose.",
])

SHIP_NOTE = ("<p>Universal Relocations Inc. is a New Jersey corporation licensed by the US Federal "
             "Maritime Commission (FMC-OTI No. NF025083) to operate an NVOCC service for international "
             "household goods to and from the USA. The U.S. Shipping Act of 1984 requires Ocean "
             "Transportation Intermediaries to be licensed and bonded — protection for you as a consumer.</p>")

def _dest(region, intro, countries):
    chips = "".join('<span class="country-chip">%s</span>' % c for c in countries)
    return ('<p style="font-size:1.1rem">%s</p>'
            '<h2>Countries we serve in %s</h2>'
            '<p>From your door to theirs, we move households and businesses to %d destinations across %s:</p>'
            '<div class="country-grid">%s</div>'
            '<h2>How your move works</h2>%s'
            '<h2>Services for your %s move</h2>%s'
            '<h2>Shipping &amp; licensing</h2>%s'
            % (intro, region, len(countries), region, chips, PROCESS, region,
               _ul(["International (door-to-door) relocation", "Groupage / shared-container shipping",
                    "Baggage &amp; box shipping", "Transit insurance", "Storage &amp; warehousing",
                    "Pet relocation", "Fine-art relocation", "Corporate &amp; office moves", "Auto / vehicle shipping"]),
               SHIP_NOTE))

EUROPE = ["Iceland","Norway","Sweden","Finland","Russia","Estonia","Latvia","Ireland","United Kingdom","Denmark","Portugal","Spain","France","Switzerland","Luxembourg","Belgium","Netherlands","Germany","Italy","Malta","Poland","Czech Republic","Slovakia","Austria","Hungary","Slovenia","Croatia","Greece","Bulgaria","Romania","Ukraine"]
NORTH_AMERICA = ["Canada","United States","Mexico","Guatemala","El Salvador","Honduras","Costa Rica","Nicaragua","Panama","Jamaica","Dominican Republic","Barbados","Trinidad & Tobago"]
ASIA = ["India","Oman","UAE","Qatar","Bahrain","Saudi Arabia","Kuwait","Jordan","Israel","Turkey","Pakistan","China","Hong Kong","Nepal","Sri Lanka","Bangladesh","Myanmar","Thailand","Cambodia","Vietnam","Malaysia","Singapore","Philippines","South Korea","Japan"]
AFRICA = ["Morocco","Algeria","Tunisia","Egypt","Mauritania","Senegal","Guinea","Sierra Leone","Ghana","Ethiopia","Uganda","Kenya","Rwanda","Tanzania","Zambia","Malawi","Mozambique","Namibia","Botswana","Zimbabwe","South Africa","Madagascar","Mauritius"]
OCEANIA = ["Australia","New Zealand","Papua New Guinea","Fiji"]
SOUTH_AMERICA = ["Colombia","Venezuela","Brazil","Ecuador","Peru","Bolivia","Paraguay","Chile","Argentina","Uruguay"]

DEST = {
    "moving-to-europe": (None, _dest("Europe",
        "Relocating to Europe? From the historic streets of Spain to the vibrant markets of Poland, our tailored European moving service gives you a seamless transition to this diverse and culturally rich continent — with secure packing, ocean and groupage shipping, and full customs coordination.", EUROPE)),
    "moving-to-north-america": (None, _dest("North America",
        "Whether you're headed to New York, Vancouver or anywhere across the continent, our North America moving service makes your relocation stress-free — expert packing, door-to-door shipping and smooth customs clearance from start to finish.", NORTH_AMERICA)),
    "moving-to-asia": (None, _dest("Asia",
        "Moving to Asia? We provide professional packing, secure door-to-door sea shipping and smooth customs clearance across the Middle East, South Asia, Southeast Asia and the Far East — backed by our own hubs in India and the UAE.", ASIA)),
    "moving-to-africa": (None, _dest("Africa",
        "From the markets of Morocco to the sights of Egypt and beyond, our specialized Moving to Africa service delivers a seamless, stress-free relocation with reliable door-to-door container transport, packing and shipping.", AFRICA)),
    "moving-to-oceania": (None, _dest("Oceania",
        "Relocating to Australia, New Zealand or the Pacific? Our dedicated Oceania service manages every step of your international move — packing, ocean freight, documentation and destination delivery.", OCEANIA)),
    "moving-to-south-america": (None, _dest("South America",
        "Our specialized Moving to South America service is built to keep your relocation smooth and low-stress — from export packing and ocean shipping to customs and final delivery across the continent.", SOUTH_AMERICA)),
    "shipping-worldwide": (None,
        '<p style="font-size:1.1rem">From local moves to international relocations, Universal Relocations ships to and from destinations across six continents — Africa, Asia, Europe, North America, Oceania and South America — backed by our own operating hubs in the USA, India and the UAE.</p>'
        '<h2>How a worldwide move works</h2>' + PROCESS +
        '<h2>Explore moving guides by region</h2>' +
        '<div class="country-grid">'
        '<a class="country-chip" href="/moving-to-africa/">Africa</a>'
        '<a class="country-chip" href="/moving-to-asia/">Asia</a>'
        '<a class="country-chip" href="/moving-to-europe/">Europe</a>'
        '<a class="country-chip" href="/moving-to-north-america/">North America</a>'
        '<a class="country-chip" href="/moving-to-oceania/">Oceania</a>'
        '<a class="country-chip" href="/moving-to-south-america/">South America</a></div>'
        '<h2>Shipping &amp; licensing</h2>' + SHIP_NOTE),
}

# ---------------------------------------------------------------------------
# Resources — packing tips, checklist, glossaries
# ---------------------------------------------------------------------------
PACKING = (
    '<p style="font-size:1.1rem">Good packing is the single biggest factor in a damage-free move. '
    'Here are our movers\' tried-and-tested tips — or let our team handle it all for you.</p>'
    '<h2>Materials</h2>' + _ul([
        "Start with professional supplies: plain newsprint, masking tape, scissors, permanent markers and heavy-duty double-wall boxes.",
        "Use newsprint only for cushioning — never directly against fine china, as ink can transfer.",
        "Stretch wrap protects furniture from snags, tears and dirt.",
    ]) +
    '<h2>Choosing the right carton</h2>' + _ul([
        "<b>Dishpacks / china barrels</b> — dishes, china, crystal and glassware.",
        "<b>Double-wall cartons</b> — fine china and high-value, hard-to-replace items.",
        "<b>1.5 cu. ft.</b> — heavy items like books, files and CDs/DVDs.",
        "<b>3.0 cu. ft.</b> — pots, pans, toys and small appliances.",
        "<b>4.5 cu. ft.</b> — bulky items like linens and towels.",
        "<b>6.0 cu. ft.</b> — large, light items like pillows and lampshades.",
        "<b>Wardrobe cartons</b> — clothes and draperies on a built-in bar.",
        "<b>Mirror &amp; mattress cartons</b> — framed pictures, mirrors, glass and bedding.",
    ]) +
    '<h2>Packing basics</h2>' + _ul([
        "Finish packing the evening before moving day; leave only essentials for last.",
        "Start with items you won't need soon — basement, garage, attic.",
        "Pack room by room, and keep each carton under 50 lbs.",
        "Cushion the bottom of each box with crumpled newsprint; wrap every breakable.",
        "Pack heavy items first, then lighter ones, filling gaps with newsprint.",
        "Use sturdy cartons and tape the seams — never plastic containers.",
        "Let our movers handle marble/glass tops, mirrors 40\"×60\"+, pianos, pool tables, chandeliers and major appliances.",
    ]) +
    '<h2>Electronics</h2>' + _ul([
        "Back up computer files before the move; label and disconnect all cables.",
        "Remove toner/ink cartridges; wrap monitors; use several medium boxes rather than one overloaded one.",
        "Mark boxes “Fragile” / “This Side Up” and pad with bubble wrap or blankets.",
    ]) +
    '<h2>Labeling</h2>' + _ul([
        "Label every carton with room and contents using a felt-tipped marker.",
        "Mark fragile boxes “FRAGILE” and upright ones “THIS END UP.”",
        "Number your cartons and keep a matching list; mark first-needed boxes with a 1 or A.",
    ]) +
    '<h2>What NOT to pack</h2>'
    '<p>Carry valuables and irreplaceables yourself. Never ship hazardous materials — paints, thinners, '
    'lighter fluid, gasoline, fireworks, propane/oxygen cylinders, matches, automotive chemicals or firearms — '
    'or perishable food and prescription medication you need right away.</p>'
)

CHECKLIST = (
    '<p style="font-size:1.1rem">Stay organized from the first box to moving day with our step-by-step timeline.</p>'
    '<h2>8 weeks before</h2>' + _ul([
        "Take a full inventory of your belongings and clear out attic, basement and storage.",
        "Use up items you can't move (frozen food, cleaning supplies).",
        "Contact Universal Relocations to arrange your move date and details, and review your insurance.",
    ]) +
    '<h2>6 weeks before</h2>' + _ul([
        "Confirm which expenses your employer covers (if a work move); check tax-deductible costs.",
        "Decide what to sell or donate; list everyone who needs your new address.",
        "Request personal records from schools, doctors, dentists and accountants.",
    ]) +
    '<h2>4 weeks before</h2>' + _ul([
        "File a change of address with the post office; tell us if you're bringing pets.",
        "Arrange utility disconnection (keep phone/utilities until moving day).",
        "Update insurance for your new home; start packing non-essentials.",
    ]) +
    '<h2>3–2 weeks before</h2>' + _ul([
        "Book travel (avoid flying on moving day); gather key papers — policies, wills, deeds.",
        "Close/open bank accounts; have your car serviced; schedule building elevators if needed.",
        "Confirm all arrangements with your relocation consultant.",
    ]) +
    '<h2>1 week before</h2>' + _ul([
        "Settle local bills; empty your safe deposit box; pick up dry cleaning.",
        "Take pets to the vet for records; drain fuel from power equipment.",
        "Prepare directions, itinerary and emergency numbers for the moving team.",
    ]) +
    '<h2>2–3 days before &amp; moving day</h2>' + _ul([
        "Defrost the fridge/freezer; have major appliances disconnected.",
        "Pack a “open-first” box and load it last (or carry it yourself).",
        "On moving day, record meter readings and read the bill of lading and inventory carefully before signing.",
    ])
)

def _glossary(pairs):
    return "".join('<p><b>%s</b> — %s</p>' % (t, d) for t, d in pairs)

MOVING_TERMS = (
    '<p style="font-size:1.1rem">A plain-English glossary of the moving terms you\'ll see on your estimate and paperwork.</p>'
    + _glossary([
        ("Accessorial (Additional) Services", "Extra services such as packing, appliance prep or unpacking, billed separately from transportation."),
        ("Advanced Charges", "Fees for third-party work the mover pays on your behalf and adds to your bill."),
        ("Bill of Lading", "The receipt for your goods and the contract for their transport — review it before signing."),
        ("Binding / Non-Binding Estimate", "A binding estimate fixes the total in advance; a non-binding estimate is an approximation, with final charges based on actual weight and tariff."),
        ("Carrier", "The mover that transports your household goods."),
        ("Change Order", "A form that amends the original estimate when items or services change."),
        ("Destination / Origin Agent", "Agents near your destination and origin who handle services and paperwork at each end."),
        ("High Value Article", "An item worth more than $100 per pound — disclose these for proper protection."),
        ("Inventory", "A detailed list of your goods, with the number and condition of each item."),
        ("Linehaul Charges", "Fees for the vehicle-transport portion of your move."),
        ("Long Carry / Flight Charge", "Extra fees for carrying items a long distance, or up and down stairs."),
        ("Storage-In-Transit (SIT)", "Temporary warehouse storage before final delivery — must be requested, limited to 90 days, with added charges."),
        ("Valuation", "The level of liability the mover assumes beyond the base transport charge."),
        ("Van Foreman", "The driver responsible for loading, transporting and unloading your belongings."),
    ])
)

SHIPPING_TERMS = (
    '<p style="font-size:1.1rem">Key ocean and air freight terms, explained simply.</p>'
    + _glossary([
        ("Ad Valorem", "A charge calculated according to the value of the goods."),
        ("Arrival Notice", "The carrier's notice that a ship has arrived, sent to the consignee and named parties."),
        ("Bill of Lading (B/L)", "A contract between shipper and carrier that is also a document of title and a receipt for goods."),
        ("Bonded Warehouse", "A Customs-authorized facility where duties are deferred until goods leave storage."),
        ("CIF (Cost, Insurance, Freight)", "The seller pays for goods, insurance and freight to a named destination port."),
        ("Consignee / Consignor", "The party receiving the shipment / the shipper named on the bill of lading."),
        ("Container", "A detachable trailer body for ship, rail or truck — typically 20, 40 or 45 ft."),
        ("Customs Entry", "A declaration an importer files for incoming foreign goods, usually with duty payment."),
        ("Demurrage / Detention", "Penalties for holding cargo at port, or a carrier's equipment, beyond the free time allowed."),
        ("Door-to-Door", "Transport of a container and its contents all the way from consignor to consignee."),
        ("Drayage", "Local hauling of containers or cargo by truck."),
        ("FCL / LCL", "Full Container Load fills a whole container; Less-than-Container Load is consolidated with other shipments."),
        ("NVOCC", "A Non-Vessel Operating Common Carrier consolidates cargo space and issues its own bills of lading without operating ships."),
        ("Reefer", "A refrigerated container."),
        ("Ro/Ro (Roll-On/Roll-Off)", "A method where wheeled vehicles drive on and off a ship without cranes — common for auto shipping."),
    ])
)

RESOURCES = {
    "packing-tips": (None, PACKING),
    "moving-check-list": (None, CHECKLIST),
    "moving-terms": (None, MOVING_TERMS),
    "shipping-terms": (None, SHIPPING_TERMS),
}

# ---------------------------------------------------------------------------
# Hubs — USA, India, UAE (real offices, routes, services)
# ---------------------------------------------------------------------------
HUB_SERVICES = _ul([
    "International relocation &amp; household-goods shipping", "Baggage shipping",
    "Groupage (shared-container) shipping", "Corporate &amp; office relocation",
    "Pet relocation", "Auto / vehicle shipping", "Storage &amp; warehousing",
    "Transit insurance", "Fine-art relocation", "Packing &amp; unpacking",
])

def _offices(rows):
    head = "<tr><th>Office</th><th>Phone</th><th>Hours</th></tr>"
    body = "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % r for r in rows)
    return '<div class="table-wrap"><table class="office-table">%s%s</table></div>' % (head, body)

def _hub(intro, routes, offices, tollfree):
    return (('<p style="font-size:1.1rem">%s</p>' % intro) +
            '<h2>Popular routes</h2>' + _ul(routes) +
            '<h2>Services from this hub</h2>' + HUB_SERVICES +
            '<h2>How your move works</h2>' + PROCESS +
            '<h2>Our offices</h2>' + offices +
            ('<p style="margin-top:14px"><b>Toll-free:</b> %s &nbsp;·&nbsp; <b>Email:</b> '
             '<a href="mailto:contact@universalrelocations.com">contact@universalrelocations.com</a></p>' % tollfree) +
            '<h2>Licensed &amp; accredited</h2>' + SHIP_NOTE)

USA_HUB = _hub(
    "Established in 1998 with 28+ years of experience, Universal Relocations moves families, corporate expatriates, diplomats and businesses across the United States and around the world. We offer domestic (local &amp; interstate) moves, popular routes to India and the UAE, and worldwide shipping.",
    ["Domestic moves within the USA (local &amp; interstate)", "USA → India (our most popular route)",
     "USA → UAE", "USA → worldwide destinations"],
    _offices([
        ("New Jersey — Parsippany, NJ", "973-227-5964", "Mon–Fri 9–5"),
        ("Maryland — Gaithersburg, MD", "1-972-318-9646", "Mon–Fri 9–5"),
        ("Georgia — Alpharetta, GA", "1-917-277-3639", "Mon–Fri 9–7"),
        ("Texas — Addison, TX", "1-803-220-0045", "Mon–Fri 9–5"),
        ("California — Newark, CA", "1-510-500-4466", "Mon–Fri 9–5"),
    ]),
    "1-888-323-7356")

INDIA_HUB = _hub(
    "International moving and shipping services from India, backed by 28+ years of experience. We coordinate packing, shipping, documentation and delivery for moves within India and to destinations worldwide.",
    ["Moves within India (local &amp; interstate)", "India → USA (a popular route)",
     "India → UAE (Dubai &amp; beyond)", "India → worldwide destinations"],
    _offices([
        ("Chennai", "+91-44-40408800", "Mon–Sat 9–5"),
        ("Bengaluru", "+91-44-40408800", "Mon–Sat 9–5"),
        ("Hyderabad", "+91-9080954113", "Mon–Fri 9–5, Sat 10–4"),
        ("Mumbai", "+91-7395813329", "Mon–Fri 9–5"),
        ("New Delhi", "+91-9599312595", "Mon–Fri 9–5"),
    ]),
    "1-800-103-7356")

UAE_HUB = _hub(
    "International moving, packing, shipping and delivery from the UAE, with 28+ years of experience. We move households and businesses across the Emirates and to destinations worldwide.",
    ["Within the UAE (Dubai, Abu Dhabi, Sharjah, Ajman, Fujairah, RAK, Umm Al-Quwain)",
     "UAE → USA", "UAE → India", "UAE → worldwide (Europe, Asia, Africa, Oceania)"],
    _offices([
        ("Dubai — Warehouse 63, Dubai Investment Park First (DIP-1)", "800-13-7356", "Mon–Fri 9–5"),
    ]),
    "800-13-7356")

HUBS = {
    "usa": ("USA Hub", USA_HUB),
    "india": ("India Hub", INDIA_HUB),
    "uae": ("UAE Hub", UAE_HUB),
}

# slug -> (optional title override, inner html)
RICH = {
    "company": (None, COMPANY),
    "about-us": (None, ABOUT),
    "corporate-social-responsibility": (None, CSR),
    "environmental-policy": (None, ENVIRONMENTAL),
    "privacy-policy": (None, PRIVACY),
    "sms-terms-of-service": (None, SMS),
    "cancel-and-refund-policy": (None, REFUND),
    "terms-and-condition": (None, TERMS),
}
RICH.update(DEST)
RICH.update(RESOURCES)
RICH.update(HUBS)
