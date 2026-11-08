"""Standalone pages harvested from universalrelocations.com (real content).
Built via build_extra_pages(g, cta_block). Also creates redirect pages for
landing/duplicate slugs so no sitemap URL 404s."""
import expand as X


def _p(*paras):
    return "".join(f"<p>{t}</p>" for t in paras)


def _table(headers, rows):
    h = "".join(f"<th>{c}</th>" for c in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return (f'<div class="cmp-wrap"><table class="cmp"><thead><tr>{h}</tr></thead>'
            f"<tbody>{body}</tbody></table></div>")


def build_extra_pages(g, cta_block):
    interior = g["interior"]; write = g["write"]
    I = X.isec; SH = X.sec_head; FC = X.feature_cards; FAQ = X.faq_isec
    CTA = X.cta_isec; WB = X.why_us_band; TL = lambda: X.trust_logos(g, alt=True)
    OS = X.orange_stats; PB = X.prompt_band
    SHIP = g["HERO_SHIP"]; LOG = g["HERO_LOGISTICS"]; CONT = g["PH_CONT1"]

    def page(slug, title, subtitle, hero, sections, faqs, desc, crumbs=None):
        body = sections
        if faqs:
            body += FAQ(faqs)
            eh = X.faq_schema(faqs)
        else:
            eh = ""
        body += CTA()
        write(slug, interior(title, crumbs or [("Home", "/"), (title, "")], body,
              desc, hero_img=hero, extra_head=eh, subtitle=subtitle, raw=True))

    # ---------------------------------------------------------------- car-shipping
    page("car-shipping", "Car Shipping",
         "Ship cars, motorbikes, yachts &amp; ATVs worldwide — safely and on time.", CONT,
         I(f'<div class="prose">{_p("Looking to ship your car with precision and care, safely to its destination? Universal Relocations provides specialized vehicle shipping for cars, motorbikes, yachts and ATVs — by container or RoRo — with secure loading, full customs handling and door-to-door delivery anywhere in the world.")}</div>')
         + OS()
         + PB(title="Get a vehicle shipping estimate")
         + I(FC([("car","Cars &amp; motorbikes","Collected, securely loaded and promptly delivered through our full managed process."),
                 ("ship","Yacht shipping","Safe transport across oceans or to a nearby marina, handled end-to-end."),
                 ("car","ATV shipping","Tailored crating and transport for ATVs and recreational vehicles.")], 'two'),
             head=SH("Our comprehensive car shipping services", "Cars to yachts — handled by trained specialists.", "What we ship"))
         + I(FC([("globe","Global reach","A worldwide network ships your vehicle to virtually any destination."),
                 ("shieldcheck","Secure loading &amp; unloading","Trained staff use damage-prevention techniques at every step."),
                 ("doc","Customs clearance expertise","We handle all customs formalities at origin and destination."),
                 ("shield","Insurance coverage","Cover tailored to your vehicle's value for peace of mind."),
                 ("globe","Advanced tracking","Real-time location and status updates throughout transit."),
                 ("star","Professional handling","From luxury cars to yachts, handled by experienced staff.")], 'two'),
             head=SH("Why choose Universal Relocations for car shipping?", "", "Why us"))
         + WB() + TL(),
         [("How are vehicles shipped?","By container (fully enclosed, most secure) or RoRo (roll-on/roll-off), depending on the vehicle and destination. We advise the best method at booking."),
          ("Do you handle customs for my vehicle?","Yes — our in-house brokers handle all export and import formalities, duties and documentation at both ends."),
          ("Can I ship a car with my household goods?","Yes — a vehicle can be loaded in the same container as your household FCL shipment for a combined, cost-effective move.")],
         "Reliable international car shipping — cars, motorbikes, yachts and ATVs by container or RoRo, with customs and door-to-door delivery.")

    # ---------------------------------------------------------------- customs-broker
    tor_rows = [("Used personal &amp; household articles","Up to Rs 5,00,000 aggregate","Duty-free"),
                ("Jewellery (gentleman)","Up to Rs 50,000","Duty-free"),
                ("Jewellery (lady)","Up to Rs 1,00,000","Duty-free"),
                ("Refrigerator (up to 300 L), washing machine, cooking range","One unit each per family","Duty-free"),
                ("Desktop &amp; laptop computer","One each","Duty-free"),
                ("Major appliances (TV, AC, dishwasher, fridge &gt;300 L, etc.)","On assessed value","36% duty")]
    page("customs-broker", "Customs Broker",
         "Clear your shipment in minutes — licensed brokers for India &amp; USA.", LOG,
         I(f'<div class="prose">{_p("A customs brokerage must know each country&#39;s import and export rules inside out. Universal Relocations&#39; licensed brokers act as the intermediary between you and government agencies — clearing your goods under Indian customs and import regulations, determining tariff classification and duty value, and applying every free-trade and tariff-reduction programme you qualify for. We provide household-goods customs clearance at all major Indian ports.")}</div>')
         + OS()
         + I(FC([("doc","Transfer of Residence","Full ToR and non-ToR clearance for returning residents."),
                 ("globe","Efficient import process","Streamlined clearance that avoids costly delays."),
                 ("shield","Customs compliance","We manage compliance and documentation end-to-end."),
                 ("doc","On-time filing","EDI and online documentation filed accurately and on time."),
                 ("home","Relationships with customs","Established working relationships at major ports."),
                 ("globe","24/7 operational support","Support whenever your shipment needs it.")], 'two'),
             head=SH("Our customs services", "", "What we handle"))
         + I(f'<div class="prose"><h2>Transfer of Residence — customs duty</h2>{_p("For NRIs and PIOs returning to India for an extended period. You must have stayed abroad for at least two years immediately before returning, and not claimed a ToR concession in the previous three years. Short visits to India in the prior two years must total no more than six months. Qualifying personal and household articles can be imported duty-free, with certain items at a concessional rate.")}</div>')
         + I(_table(["Item","Limit","Duty"], tor_rows), alt=True, head=SH("Duty-free items under Transfer of Residence","Combined value up to Rs 5 lakh; maximum one unit of each per family.","ToR allowance"))
         + I(f'<div class="prose"><h2>Documents required</h2><ul><li>Original passport</li><li>Original OCI card or work permit</li><li>English packing list</li><li>Bill of lading or airway bill</li><li>Power of attorney</li><li>Unaccompanied baggage declaration</li><li>Electronics list (model, make, value — with original receipts where possible)</li></ul><h2>How customs duty is calculated on used items</h2>' + _p("Used items are depreciated before duty is assessed — 16% in year one, 12% in year two and 10% in year three. For example, a four-year-old item is valued at its new price less around 38%.") + '<p><em>Note: drones are on India&#39;s prohibited list and are not duty-free under ToR.</em></p></div>')
         + WB() + TL(),
         [("What is Transfer of Residence?","A customs scheme that lets returning NRIs/PIOs import personal and household goods duty-free (within limits) after at least two years abroad."),
          ("Can you clear a non-Transfer-of-Residence shipment?","Yes — we handle both ToR and standard dutiable clearances, calculating and minimising duty where the law allows."),
          ("Which ports do you cover?","We provide household-goods customs clearance at all major Indian ports, with established relationships at each.")],
         "Licensed customs brokers for India and the USA — Transfer of Residence, duty calculation, documentation and clearance at every major port.")

    # ---------------------------------------------------------------- fcl-shipping
    page("fcl-shipping", "FCL Shipping",
         "Full Container Load — your own 20ft or 40ft container, sealed door to door.", CONT,
         I(f'<div class="prose">{_p("Full Container Load (FCL) is one of our core services for US customers. Your goods get the sole use of a sealed 20ft or 40ft container — loaded at your door, never shared or re-handled in transit, and opened only at destination.", "FCL is the right choice when your shipment fills a container or your goods are too fragile for repeated handling. We suggest a 20ft container for a smaller or electronics-heavy load and a 40ft for a full home of furniture.")}</div>')
         + OS()
         + PB(title="Get an FCL container quote")
         + I(FC([("ship","Faster &amp; direct","No repeated handling means FCL is far faster than shared shipping — one of the fastest FCL services in the US."),
                 ("shieldcheck","Container quality &amp; safety","Every container is inspected for leaks and quality; fragile items get specialised compartments and are never overloaded."),
                 ("shield","Insurance &amp; money-back","Optional all-risk insurance with a money-back guarantee for any mishap."),
                 ("doc","Transparent pricing","Best-in-class FCL charges with no hidden fees — see your full cost in our online calculator before you book.")], 'two'),
             head=SH("Why ship FCL with Universal Relocations", "", "Why FCL"))
         + I(f'<div class="prose">{_p("Our FCL rates stay constant year-round — no General Rate Increase and no peak-season pricing — and loyalty discounts apply across FCL and LCL. Book two to three weeks ahead, confirm your dock height matches the truck, and our team packs, transports and unloads at the locations you choose. 24/7 support throughout.")}</div>', alt=True)
         + WB() + TL(),
         [("When should I choose FCL over LCL?","Choose FCL when your goods fill a 20ft/40ft container or are fragile enough to avoid repeated handling. LCL (shared) is more economical for smaller loads."),
          ("How far ahead should I book?","Two to three weeks ahead is ideal so we can confirm the sailing and schedule packing and collection."),
          ("Are your FCL rates seasonal?","No — our FCL rates are constant year-round with no General Rate Increase or peak-season surcharges, and loyalty discounts apply.")],
         "Reliable FCL shipping from the USA — your own sealed 20ft/40ft container, door to door, with transparent year-round rates and no hidden fees.")

    # ---------------------------------------------------------------- lcl-shipping
    page("lcl-shipping", "LCL Shipping",
         "Less-than-Container-Load — pay only for the space your goods use.", SHIP,
         I(f'<div class="prose">{_p("LCL (Less-than-Container-Load) is for shipments too large to hand-carry but too small to fill a container. Many carriers push customers to book a whole container that then travels mostly empty — with LCL from Universal Relocations you ship from the USA to any destination and pay only for the cubic metres (CBM) you actually use.")}</div>')
         + OS()
         + PB(title="Get an LCL (groupage) quote")
         + I(FC([("ship","Choose your consolidator","Pick a consolidator by date, available space, container type and route from our online database — with stuffing dates, vessel schedules and ETAs."),
                 ("doc","Transparent CBM pricing","Quotes by the cubic metre with no hidden charges, covering haulage and ocean freight by lane; all charges confirmed in writing."),
                 ("shieldcheck","Cargo safety","No overloading, fragile items in protected spots, and cargo insurance for LCL/FCL with an online calculator."),
                 ("globe","Support &amp; tracking","A service team by phone and email, a container vessel tracker, and a survey report of your cargo volume on request.")], 'two'),
             head=SH("How LCL works with Universal Relocations", "", "How it works"))
         + I(f'<div class="prose">{_p("If a forwarder misses the required stuffing date, we offer a discount on your next booking or change the forwarder. Loyalty points earned on LCL and FCL can be used for future discounts, and we are continually adding routes, lower rates and wider container options.")}</div>', alt=True)
         + WB() + TL(),
         [("How is LCL priced?","By the volume your goods occupy, in cubic metres (CBM) — so you only pay for the space you use, far cheaper than a full container for smaller loads."),
          ("Can I choose my consolidator?","Yes — our online database lets you pick by date, available space, container type and route, with vessel schedules and ETAs shown."),
          ("Is my LCL cargo insured and tracked?","Yes — all-risk cargo insurance is available with an online calculator, and a container vessel tracker lets you follow your shipment.")],
         "LCL / groupage shipping from the USA — pay only for the CBM you use, choose your consolidator, with transparent pricing, insurance and tracking.")

    # ---------------------------------------------------------------- freight-forwarding
    page("freight-forwarding", "Freight Forwarding",
         "Ocean &amp; air freight forwarding — USA to India and worldwide.", SHIP,
         I(f'<div class="prose">{_p("Our Ocean Freight Division bundles forwarding, packing, consolidation and transport by air, sea and rail — with competitive rates, reliable transit times and full documentation support. We run a weekly direct groupage schedule between the USA and India in both directions.")}</div>')
         + OS()
         + PB(title="Get a freight forwarding quote")
         + I(f'<div class="prose"><h2>The complexities of ocean freight forwarding</h2>{_p("Freight forwarding is hard to navigate alone — customs documentation and bills of lading are an involved part of the process. Our experienced, quality-accredited team helps you avoid shipping problems and keeps your cargo moving. Our FMC licence number is NF025083.")}</div>')
         + I(FC([("globe","Save time &amp; money","Optimised routing and consolidation keep your costs down."),
                 ("shield","All-risk marine insurance","Full cover for your goods across the whole journey."),
                 ("doc","In-house customs broker","Clearance handled directly, with no third-party hand-offs."),
                 ("box","Packing &amp; haulage","Export-grade packing and inland haulage included."),
                 ("ship","Direct USA–India groupage","A weekly direct groupage service in both directions."),
                 ("globe","24/7 service &amp; guarantee","Round-the-clock support and a satisfaction guarantee.")], 'two'),
             head=SH("The Universal advantage", "", "Why us"), alt=True)
         + WB() + TL(),
         [("Do you handle customs documentation?","Yes — our in-house customs broker prepares bills of lading and all documentation, so you avoid common clearance problems."),
          ("How often do you sail between the USA and India?","We run a weekly direct groupage service between the USA and India in both directions."),
          ("Is marine insurance included?","All-risk marine insurance is available and arranged with your shipment for end-to-end cover.")],
         "Freight forwarding from the USA to India and worldwide — ocean and air freight, in-house customs, weekly direct groupage, FMC-licensed.")

    # ---------------------------------------------------------------- liftvan-service
    page("liftvan-service", "Liftvan Service",
         "You pack, we move — guaranteed door-to-door delivery to India within 90 days.", CONT,
         I(f'<div class="prose">{_p("Our liftvan service is the cost-saving way to ship to India: you pack your own shipment at your own pace and call us when you&#39;re ready. We collect from your door, handle customs clearance and deliver to your home in India exactly as you packed it — our destination team carries, unpacks and removes the debris.", "Liftvans are built from triple-wall carbox material with a weather-proof plastic shroud, and a Total Loss Insurance package is available.")}</div>')
         + OS()
         + PB(title="Get a liftvan quote")
         + I(FC([("box","Pack at your own pace","Load your liftvan on your schedule and keep it organised your way."),
                 ("shield","Fewer hands on your boxes","Avoid third-party courier handling and the repacking charges that come with it."),
                 ("doc","No hidden costs","No overflow or pallet charges and a price guaranteed up front."),
                 ("home","Door-to-door in 90 days","Guaranteed delivery to your home in India within 90 days.")], 'two'),
             head=SH("Why pack your own liftvan?", "", "Benefits"))
         + WB() + TL(),
         [("How does the liftvan service work?","You pack your liftvan at your own pace; we collect from your door, clear customs and deliver to your home in India as packed — carrying, unpacking and removing debris at destination."),
          ("How long does delivery take?","Door-to-door delivery to India is guaranteed within 90 days."),
          ("Is insurance available?","Yes — a Total Loss Insurance package is available; ask our team for details.")],
         "Liftvan / sharing-container service to India — you pack at your own pace, we collect, clear customs and deliver door-to-door within 90 days.")

    # ---------------------------------------------------------------- destination-services
    page("destination-services", "Destination Services",
         "Settle in faster — orientation, home &amp; school search, cultural training.", LOG,
         I(f'<div class="prose">{_p("An international move is an exciting change — but finding housing from a distance and adjusting to an unfamiliar language, currency and culture is a real challenge. Our global mobility experts give you and your family personal support with visas, cultural training, home searches and more, backed by worldwide partnerships, so you can focus on your new life abroad.", "Families have to weigh schools, transport, housing and healthcare. A good destination-services provider knows the location in detail — from traffic patterns to the local economy — and coordinates with everyone involved. Reaching out early makes settling in far smoother.")}</div>')
         + OS()
         + I(FC([("globe","Area orientation","Get to know your new city — neighbourhoods, transport and essentials."),
                 ("home","Home search","Find the right home for your family and budget, from a distance."),
                 ("doc","School search","Identify and secure the right schools for your children."),
                 ("globe","Cultural &amp; language training","Settle into a new culture and language with confidence."),
                 ("shield","Spouse &amp; partner support","Help for partners finding their feet in a new country."),
                 ("doc","Visa &amp; settling-in","Guidance through visas and the practicalities of arrival.")], 'two'),
             head=SH("What destination services cover", "Pricing is itemised — you choose only what you need.", "What we cover"), alt=True)
         + WB() + TL(),
         [("What are destination services?","Support that helps you settle into a new country — area orientation, home and school search, cultural and language training, and spouse/partner support."),
          ("How is it priced?","Services are itemised and priced to what you need — not everyone needs the full package."),
          ("When should I engage a provider?","As early as possible — early contact gives more time to secure housing, schools and the essentials before you arrive.")],
         "International destination services — area orientation, home and school search, cultural and language training, and settling-in support for your family.")

    # ---------------------------------------------------------------- international-air-freight
    page("international-air-freight", "International Air Freight",
         "Fast, reliable air freight for personal and commercial shipments worldwide.", SHIP,
         I(f'<div class="prose">{_p("When you need your shipment to arrive quickly, our international air freight service moves personal belongings, commercial cargo and sensitive equipment worldwide. We work directly with airlines, offer expedited options and tracking, and keep every shipment customs-compliant.", "As a freight forwarder for household-goods imports and exports, we offer both ocean and air options to suit your timeline and budget. Our FMC-OTI licence (NF025083) authorises our NVOCC service for international household goods to and from the USA.")}</div>')
         + OS()
         + PB(title="Get an air freight quote")
         + I(FC([("doc","Customs filing","All air-freight customs documentation prepared and filed."),
                 ("box","Air liftvan &amp; packing","We pack your items and collect from your door."),
                 ("plane","Air freight to destination","Direct air freight to your final destination."),
                 ("home","Door delivery","Delivery to the door at the destination."),
                 ("shield","Transit insurance","All-risk cover for fast-moving air shipments."),
                 ("globe","24/7 customer service","Support at every stage of the journey.")], 'two'),
             head=SH("What's included", "", "Air freight service"))
         + WB() + TL(),
         [("How is air freight charged?","On chargeable weight — the greater of the actual (gross) weight or the volumetric (dimensional) weight. To convert cubic inches to dimensional kilograms, divide the cubic-inch figure by 366."),
          ("Is sea or air cheaper?","Sea is usually cheaper for larger, heavier shipments. For smaller shipments the gap narrows and air can sometimes cost less — contact us for a quote."),
          ("Do you pack and collect for air freight?","Yes — we pack your items and collect from your door before air freighting to the destination.")],
         "International air freight — fast, reliable, customs-compliant shipping for personal and commercial cargo worldwide, with packing, insurance and door delivery.")

    # ---------------------------------------------------------------- packing-service
    pack_rows = [("Non-fragile box — Small","$15"),("Non-fragile box — Medium","$20"),("Non-fragile box — Large","$30"),("Non-fragile box — Extra Large","$50"),
                 ("Fragile box — Small","$25"),("Fragile box — Medium","$35"),("Fragile box — Large","$45"),("Fragile box — Extra Large","$60"),
                 ("Art/mirror — Small frame","$30"),("Art/mirror — Medium frame","$50"),("Art/mirror — Large frame","$70"),("Art/mirror — XL frame","$80"),
                 ("TV packing — up to 65\"","$100"),("TV packing — above 75\"","$150"),("TV packing — 85\"","$175"),("TV packing — 90\"","$200"),
                 ("TV crating — up to 65\"","$150"),("TV crating — 75\"","$200"),("TV crating — 85\"+","$300"),
                 ("Dish pack","$17"),("Wardrobe packing","$40"),("Books","$12"),("Cosmetics","$15"),("Clothes","$15")]
    page("packing-service", "Packing Service",
         "Professional, export-grade packing — at our Box Store or your home.", CONT,
         I(f'<div class="prose">{_p("Our packing service handles everything from everyday objects to musical instruments, bicycles, sports equipment and fine artwork — using the right method for each category so your items arrive secure and intact. Packing can be arranged at our Box Store or at your home, on a schedule that suits you.")}</div>')
         + OS()
         + PB(title="Book a packing service")
         + I(_table(["Service","Price (USD)"], pack_rows), head=SH("Packing &amp; crating price list", "Transparent per-item pricing — no surprises on moving day.", "Pricing"))
         + I(FC([("box","Non-fragile &amp; fragile boxes","Small to extra-large, packed to protect the contents."),
                 ("star","Art, mirror &amp; TV crating","Custom crating for frames and large-screen TVs."),
                 ("home","Dish packs &amp; wardrobes","Specialised cartons for kitchens and hanging clothes.")], 'two'),
             head=SH("What we pack", "", "Box &amp; item types"), alt=True)
         + WB() + TL(),
         [("Where does packing take place?","Either at our Box Store or at your home — whichever is more convenient, on a schedule that fits your move."),
          ("Do you pack fragile and special items?","Yes — fragile boxes, art and mirror framing, TV packing and crating, dish packs and wardrobe cartons are all available at the prices listed."),
          ("Can I pack some items myself?","Absolutely — pack what you like and we'll professionally pack the rest, ready for moving day.")],
         "Professional packing service with transparent per-item pricing — boxes, fragile items, art, TV crating, dish packs and wardrobes, at our Box Store or your home.")

    # ---------------------------------------------------------------- moving-tips
    page("moving-tips", "Moving Tips",
         "Room-by-room tips for a smooth move from the US to Europe &amp; India.", LOG,
         I(f'<div class="prose">{_p("Packing early makes unpacking easier. Use this room-by-room guide to prepare your home for an international move.")}'
           '<h2>Bedroom, nursery &amp; bathroom</h2>' + _p("Start with guest rooms. Let children pack their own toys and books with labelled stickers. Keep hanging clothes on hangers in wardrobe cartons; fold the rest into suitcases or lined cartons. Keep fine jewellery with you. Discard or carry aerosol cans; tape other bottles shut and wrap them. Mattresses go in mattress cartons and mirrors in special cartons or crates.")
           + '<h2>Dining room</h2>' + _p("Wrap fragile china and crystal individually in dish-pack cartons with cellular dividers. List items worth over $100/lb on a High Value Inventory form for valuation coverage. Lamp shades go in tissue inside sturdy cartons marked &#39;TOP LOAD ONLY&#39; — never newspaper. Chandeliers, large glass, marble and oil paintings need professional crating.")
           + '<h2>Garage, hobby &amp; storage</h2>' + _p("These rooms take longest. Dispose of hazardous, non-shippable items — pesticides, fertilisers, oil and gas. Drain oil and fuel from power tools, mowers and grills. Keep vehicles at a quarter tank or less. Large outdoor items like swing sets and hot tubs need a consultation with your mover.")
           + '<h2>Home office &amp; den</h2>' + _p("Keep important documents and legal papers with you. Label and disconnect computer cables, remove printer cartridges and back up your files. Pack books flat or spine-down and bag furniture hardware together.")
           + '<h2>Living &amp; family room</h2>' + _p("Pictures and mirrors go in telescoping mirror cartons. Lock CD/DVD lasers and secure turntable tone arms. Large or plasma TVs may need crating. Store DVDs, CDs and records on edge. Grand pianos and pool tables need qualified third-party disassembly and crating.")
           + '<h2>Kitchen &amp; laundry</h2>' + _p("Start with rarely-used items and keep everyday dishes until the final week. Use up or dispose of perishables and cleaning chemicals. In dish-packs, layer large flat pieces at the bottom and smaller plates above. Empty irons of water and wrap small appliances individually.")
           + '</div>')
         + X.callout("Planning an international move?", "Book a free survey and let our team handle the heavy lifting.", "Get a free quote", "/contact-us/", "Estimate volume", "/moving-calculator/")
         + WB() + TL(),
         [("How early should I start packing?","As early as possible, room by room — packing early makes unpacking at destination much easier."),
          ("What can't I ship?","Hazardous and non-shippable items — pesticides, fertilisers, oil, gas, aerosols — must be disposed of or carried separately; drain fuel and oil from equipment and vehicles."),
          ("How are high-value items covered?","List anything worth over $100/lb on a High Value Inventory form so it's covered at its declared value; fragile art and pianos get professional crating.")],
         "Room-by-room moving tips for a smooth international relocation from the US to Europe and India — packing, fragile items, hazardous goods and high-value coverage.")

    # ---------------------------------------------------------------- baggage-shipping-tips
    page("baggage-shipping-tips", "Baggage Shipping Tips",
         "Easy tips for safe, affordable baggage shipping to India and beyond.", SHIP,
         I(f'<div class="prose">{_p("We want your shipment to arrive on time and undamaged. Follow these tips to ship luggage and boxes safely.")}'
           '<h2>How to ship luggage &amp; boxes</h2><ul>'
           '<li><b>Use sturdy luggage or double-wall boxes</b> — avoid packing too full or too light.</li>'
           '<li><b>Recommended boxes</b> — keep each box 45–50 lbs: Large (24&quot;×18&quot;×18&quot;) and Medium (18&quot;×18&quot;×16&quot;) heavy-duty double-wall boxes.</li>'
           '<li><b>Seal with an &quot;H&quot; tape pattern</b> on the top and bottom; don&#39;t lock luggage on international shipments as customs may need to open it.</li>'
           '<li><b>Attach shipping labels securely</b> — use a label pouch or clear tape on the side of the box, and place a copy inside.</li>'
           '</ul><h2>Labelling matters</h2>' + _p("Around 90% of lost or delayed luggage cases are caused by improper labelling. You are responsible for label accuracy and secure attachment — photograph each labelled item with the tracking number and barcode visible. Don&#39;t use Scotch tape (labels come off), wrinkled labels, or hard-to-read low-ink labels.")
           + '<h2>Transit times to India</h2>' + _p("South India: 75–90 days. North, East and West India: 90–120 days.")
           + '<h2>Sports equipment</h2>' + _p("Ship skis and bags directly to the resort. Pack golf clubs in a hard or soft travel case with padding around the heads; cushion ski and snowboard bindings and tips; disassemble bicycles into a bike case or sturdy corrugated box and fill empty space.")
           + '</div>')
         + X.callout("Ready to ship your baggage?", "Confirm your box count and we'll schedule pickup within 24–48 hours (Mon–Fri).", "Get a quote", "/contact-us/", "Estimate volume", "/moving-calculator/")
         + WB() + TL(),
         [("How heavy can each box be?","Keep each box to about 45–50 lbs and use heavy-duty double-wall boxes — Large (24×18×18) or Medium (18×18×16)."),
          ("How long does baggage take to reach India?","South India takes about 75–90 days; North, East and West India about 90–120 days."),
          ("Why is labelling so important?","Around 90% of lost or delayed cases come from poor labelling — use a label pouch or clear tape, put a copy inside, and photograph each item with the tracking number visible.")],
         "Baggage shipping tips — sturdy boxes, correct weights, secure labelling and transit times for safe, affordable shipping to India and worldwide.")

    # ---------------------------------------------------------------- how-to-seal-container
    page("how-to-seal-container", "How to Seal a Container",
         "A simple guide to sealing and photographing your shipping container.", CONT,
         I(f'<div class="prose">{_p("When closing a shipping container, shut the left door first, then the right. The seal goes on the right door (the one opened first) — it can go on one or both lock rods of that door.", "A seal number is a unique identification number for each container seal. Bolt seals act as a one-time-use padlock; most bolt seals from ISO 17712:2013 certified manufacturers are classed as high-security seals, which is one requirement for C-TPAT compliance.")}'
           '<h2>Photograph the seal and container number after closing</h2><ul>'
           '<li>The container number is the most important door marking — a unique alphanumeric sequence of four letters and seven numbers used internationally.</li>'
           '<li>Seals should <b>not</b> be removed by border security or truck drivers — only by the recipient at destination.</li>'
           '<li>Because seals are tough to break, a bolt cutter is the best removal method at destination.</li>'
           '</ul></div>')
         + WB() + TL(),
         [("Which door do I seal?","Close the left door first, then the right; the seal goes on the right door, on one or both lock rods."),
          ("What is a high-security seal?","A bolt seal from an ISO 17712:2013 certified manufacturer — a one-time-use lock that is one requirement for C-TPAT compliance."),
          ("Who should remove the seal?","Only the recipient at destination — not border security or the truck driver. A bolt cutter is the best removal tool.")],
         "How to seal a shipping container — door order, seal placement, container numbers and photographing the seal for secure, compliant shipping.")

    # ---------------------------------------------------------------- book-a-virtual-survey
    page("book-a-virtual-survey", "Book a Virtual Survey",
         "Start your move with a quick video survey — no in-person visit needed.", LOG,
         I(f'<div class="prose">{_p("Start your move without giving up much of your time. In a virtual survey, our surveyors use current technology to assess your belongings remotely — you pick a convenient time, a team member walks you through it on a video call, covers your requirements, answers your questions and gives you an estimate. You save time and skip the in-person visit.")}</div>')
         + PB(title="Book your virtual survey")
         + OS()
         + X.callout("Prefer an instant number?", "Use our Moving Calculator for an instant volume-based estimate, any time.", "Open Moving Calculator", "/moving-calculator/", "Talk to us", "/contact-us/")
         + WB() + TL(),
         [("What is a virtual survey?","A video call where our surveyor assesses your belongings remotely, covers your requirements and gives you an estimate — no in-person visit required."),
          ("How do I book one?","Pick a convenient time and our team walks you through it on a video call; you can also use the Moving Calculator for an instant estimate."),
          ("Is it accurate?","Yes — our surveyors use current technology to assess volume reliably, and a move manager follows up with a firm, itemised quote.")],
         "Book a free virtual survey with Universal Relocations — a quick video call to assess your belongings and get a moving estimate, no in-person visit needed.")

    # ---------------------------------------------------------------- storage-bay-area
    page("storage-bay-area", "Storage in the Bay Area",
         "Secure, climate-controlled storage in Newark, CA — pickup and delivery included.", LOG,
         I(f'<div class="prose">{_p("Bay Area homes often don&#39;t have room for everything — especially for students and professionals working in Silicon Valley, or anyone moving into a smaller apartment. Our storage at 7401 Morton Avenue, Suite B, Newark, CA 94560 is the easy answer: we pick up, store and deliver your belongings back whenever you need them, with no rental truck and no packing, loading or unloading on your part.", "Moving blankets protect your items, a dolly is provided, and our facilities are climate-controlled, regularly cleaned and pest-controlled.")}</div>')
         + OS()
         + PB(title="Get a storage quote")
         + WB() + TL(),
         [("How much does storage cost?","Storage is priced by the volume of your shipment — request a quote. Affordable storage matters in the expensive Bay Area."),
          ("Do I need climate-controlled storage?","Our facilities are climate-controlled, which suits household goods and protects temperature-sensitive furniture, antiques, instruments and art."),
          ("Is my stored property insured and secure?","Storage insurance is available through a third-party provider at an additional premium of 1% of declared value. Facilities have premium surveillance, on-site managers, unit alarms and fire protection."),
          ("When can I access my items?","With two days&#39; notice, Mon–Sat 9am–5pm PST (excluding major holidays), with rent current; same-day drop-ins are possible for an additional retrieval fee.")],
         "Secure, climate-controlled storage in the Bay Area (Newark, CA) — pickup, storage and delivery with surveillance, insurance options and flexible access.")

    # ---------------------------------------------------------------- pet-relocation-to-usa
    page("pet-relocation-to-usa", "Pet Relocation to the USA",
         "Moving dogs &amp; cats from India to the USA — done right, with compassion.", g["PH_PET"],
         I(f'<div class="prose">{_p("Our pet relocation service moves dogs and cats from India to the USA — transport, paperwork and travel coordination handled by IPATA-certified specialists. US import rules, airline policies and documentation are strict and time-sensitive; we manage all of it so your companion&#39;s journey is calm, safe and stress-free.")}</div>')
         + OS()
         + PB(title="Plan your pet's move to the USA")
         + I(FC([("doc","Documentation &amp; compliance","Health certificates, vaccination records, microchip compliance, import/export permits and airline approvals — managed to avoid delays."),
                 ("paw","Comfort-first handling","Preparation, familiarity and gentle handling keep pets calm from departure to arrival."),
                 ("plane","Airline &amp; cargo coordination","Pet-friendly airlines and cargo partners, flight selection and airport coordination at both ends."),
                 ("shieldcheck","IATA-approved crates","Crates sized to your pet&#39;s breed and weight, with crate-training guidance."),
                 ("globe","Updates throughout","Regular updates so you always know where your pet is."),
                 ("home","Door-to-door or door-to-airport","Flexible delivery to suit your needs.")], 'two'),
             head=SH("How we move your pet", "", "Our service"))
         + WB() + TL(),
         [("How long does pet relocation to the USA take?","It depends on documents, vaccinations, airline availability and compliance — most moves need several weeks of preparation."),
          ("Which pets can be relocated?","Dogs and cats are most common; other household pets may be allowed depending on US rules and airline policy."),
          ("Are vaccinations required?","Yes — your pet must meet US vaccination and health-certificate requirements, including rabies vaccination and veterinary clearance."),
          ("Is quarantine needed?","Usually not, provided documentation and health requirements are met before travel."),
          ("Is crate training necessary?","It's strongly recommended — it helps pets feel secure and reduces stress in transit.")],
         "Pet relocation from India to the USA — IPATA-certified, airline-approved moves for dogs and cats, with documentation, crates and compassionate handling.")

    # ---------------------------------------------------------------- india/transfer-of-residence
    tor2 = [("Used personal &amp; household goods","Up to Rs 5,00,000 total","Duty-free"),
            ("Jewellery (gentleman / lady)","Rs 50,000 / Rs 1,00,000","Duty-free"),
            ("Foodstuff (foreign nationals)","Up to Rs 50,000 in main shipment","Duty-free"),
            ("Used electronics","Depreciated 16%/12%/10% over 3 years","Concessional"),
            ("Motor car","On CIF value","208%"),
            ("Motorbike","On CIF value","185%"),
            ("Alcohol / spirits","Not advised","~160% + penalties")]
    page("india/transfer-of-residence", "Transfer of Residence (India)",
         "Resettling in India? Import your home under Transfer of Residence rules.", g["PH_INDIA_HUB"],
         I(f'<div class="prose">{_p("Former Indian citizens and NRIs planning to resettle in India can use Transfer of Residence (ToR) rules, which relax the limits on importing personal belongings. You qualify after a stay abroad of at least two years, with duty-free import of personal and household articles and concessional duty on certain items — with no minimum stay required in India.")}</div>', )
         + OS()
         + I(_table(["Category","Limit / basis","Duty"], tor2), head=SH("Transfer of Residence — duty at a glance", "Combined duty-free value up to Rs 5 lakh; one unit of each per family.", "ToR allowance"))
         + I(f'<div class="prose"><h2>Important notes</h2><ul>'
             '<li><b>Exemptions:</b> officers can condone a stay shortfall of up to two months; longer absences may be condoned in special circumstances, with reasons in writing.</li>'
             '<li><b>Customs examination:</b> import consignments are generally inspected 100%.</li>'
             '<li><b>Alcohol:</b> duties are very high (~160% plus fines); shipping alcohol is not advised. If unavoidable, complete the Alcohol Declaration Form, pack it separately and load it at the front of the container.</li>'
             '<li><b>Pets:</b> two pets per passenger, with veterinary certificates and health documents — call before shipping.</li>'
             '<li><b>Restricted / prohibited:</b> obscene material, narcotics, wildlife products (ivory, horns), and firearms/weapons. Contact us before shipping if unsure.</li>'
             '</ul><p><em>Information is based on customs data at the time of writing and may change; the owner/importer is responsible for compliance. Check your destination consulate or embassy.</em></p></div>', alt=True)
         + WB() + TL(),
         [("Who qualifies for Transfer of Residence?","Returning NRIs and Indian citizens who have stayed abroad for at least two years immediately before returning, with no ToR concession claimed in the previous three years."),
          ("How is duty on used electronics calculated?","Used electronics are depreciated before duty — 16% in year one, 12% in year two and 10% in year three."),
          ("Can I ship my car under ToR?","Cars are dutiable at 208% of CIF value and bikes at 185%; non-Indian-spec motorbikes may face penalties up to 100% of duty. We advise before you ship.")],
         "Transfer of Residence to India — duty-free allowances, used-electronics depreciation, car and alcohol rules, and documentation for returning NRIs.")

    # ---------------------------------------------------------------- universal-prestige-relocations
    page("universal-prestige-relocations", "Universal Prestige Relocations",
         "White-glove relocation for a class that expects more.", LOG,
         I(f'<div class="prose">{_p("Prestige is a step beyond traditional white-glove service — for clients who expect more. For 28+ years we have built a reputation for a calm, immaculate, meticulous move. Door-to-door is our specialty, and our newer home-to-home option goes further still.", "A Prestige move is coordinated by our US Manager or President, with premium third-party services: custom crating, maid service, wine and art collections, fine piano handling, grandfather-clock disassembly and storage. High-end furniture, china, appliances and sentimental items are hand-wrapped in premium materials.")}'
           '<ul><li>Prestige is calm.</li><li>Prestige is immaculate.</li><li>Prestige is peace.</li><li>Prestige is meticulous.</li></ul>'
           + _p("Door-to-door packs your origin home and sets up the new one; Prestige home-to-home goes further so you settle in from day one. The only significant effort you make is the Prestige Application — we handle everything else.")
           + '</div>')
         + OS()
         + X.callout("Expect more from your move?", "Start with the Prestige Application and let us handle the rest.", "Get a free quote", "/contact-us/", "Estimate volume", "/moving-calculator/")
         + WB() + TL(),
         [("What is Universal Prestige Relocations?","A first-class relocation service coordinated by our US Manager or President, with custom crating, specialist handling for pianos, art and wine, and premium hand-wrapping of high-value items."),
          ("What is home-to-home service?","It goes beyond door-to-door — we don't just deliver and set up your new home, we make sure you can settle in and live from day one."),
          ("How do I start a Prestige move?","Begin with the Prestige Application — it's the only significant step you need to take; we manage everything from there.")],
         "Universal Prestige Relocations — white-glove, first-class international moving with custom crating, specialist handling and premium home-to-home service.")

    # ---------------------------------------------------------------- disputeprocedures
    page("disputeprocedures", "Dispute Procedures",
         "Demurrage &amp; detention (D&amp;D) dispute, mitigation, refund and waiver procedures.", CONT,
         I(f'<div class="prose">{_p("Universal Relocations Inc. is licensed by the US Federal Maritime Commission (FMC-OTI No. NF025083). The following Demurrage and Detention (D&amp;D) Tariff standard operating procedures explain how to seek fee mitigation, refund or waiver. Source: NRA Rules Tariff No. 002, Rule 2-220 (US and World).")}'
           '<h2>D&amp;D invoices from VOCCs, MTOs and pass-through procedures</h2><ul>'
           '<li>Pass-through invoices must be passed through immediately by the Carrier (NVOCC) to the party whose account it served (for example, the ultimate recipient).</li>'
           '<li>Pass-through charges not specifically covered by an agreement or the NVOCC&#39;s tariff must be passed on without a mark-up.</li>'
           '<li>An NVOCC receiving a D&amp;D invoice may seek relief within 30 days of receipt — grounds include untimely issuance of the invoice, missing required invoice contents under 46 C.F.R. §341.6, failure to be the right party to receive the invoice, or any other lawful reason.</li>'
           '<li>An NVOCC passing on a disputed invoice must request relief within 30 days of receiving the pass-through invoice and inform the billing party of the dispute; the billing party then gets an additional 30 days to dispute, and the party the invoice was passed to has 30 days to raise circumstances justifying waiver, mitigation or refund.</li>'
           '</ul></div>')
         + TL(),
         [("How long do I have to dispute a D&D invoice?","Within 30 days of receiving the invoice (or the pass-through invoice), with the dispute communicated to the billing party."),
          ("Can pass-through charges include a mark-up?","No — pass-through charges not covered by an agreement or the NVOCC's tariff must be passed on without a mark-up."),
          ("What are valid grounds for relief?","Untimely issuance, missing invoice contents under 46 C.F.R. §341.6, being the wrong party billed, or any other lawful reason.")],
         "Universal Relocations demurrage and detention (D&D) dispute procedures — fee mitigation, refund and waiver under NRA Rules Tariff No. 002, Rule 2-220.")

    # ---------------------------------------------------------------- press
    press_logos = "".join(f'<img height="40" src="{g["IMG"]}/2025/08/{n}" alt="{a}">' for n, a in [
        ("Forbes.png","Forbes"),("Fox-News.png","Fox News"),("Yahoo.png","Yahoo Finance"),("MSN.png","MSN"),
        ("MSNBC.png","MSNBC"),("Associated-Press.png","Associated Press"),("Bussiness-Insider.png","Business Insider"),
        ("Zee-News.png","Zee News"),("DNA-India.png","DNA India"),("Gulf-News.png","Gulf News"),
        ("Khaleej-Times.png","Khaleej Times"),("Mid-Day.png","Mid-Day"),("ThePrint.In_.png","ThePrint"),
        ("Tribune-India.png","Tribune India"),("Up18news.png","Up18 News")])
    page("press", "Press &amp; Media",
         "Universal Relocations in the global media.", LOG,
         I(f'<div class="prose">{_p("Universal Relocations is one of the most recognised names in international moving — featured across global business and news media. Our expansion into the Middle East, including a successful first year in Dubai, has been covered widely.")}</div>')
         + I(f'<div class="logos-slider"><div class="logos-track press">{press_logos}{press_logos}</div></div>',
             head=SH("As seen on", "Featured by leading business and news outlets worldwide.", "In the media"), alt=True)
         + OS() + WB() + TL(),
         None,
         "Universal Relocations in the press — featured by Forbes, Fox News, Yahoo Finance, Associated Press, Gulf News, Khaleej Times and more.")

    # ---------------------------------------------------------------- redirects (landing / duplicate slugs)
    REDIRECTS = {
        "moving-to-dubai": "/uae/", "london": "/moving-to-uk/", "washington-dc": "/usa/",
        "northamerica": "/moving-to-north-america/", "southamerica": "/moving-to-south-america/",
        "relocate-to-asia": "/moving-to-asia/", "relocate-to-australia": "/moving-to-australia/",
        "relocate-to-europe": "/moving-to-europe/", "moving": "/services/", "local": "/services/intrastate/",
        "interstate-move": "/services/intrastate/", "president": "/sai-dattani/",
        "backup-fmc-rules-tariff": "/fmc-rules-tariff/", "backup-historic-fmc-rules-tariff": "/historic-fmc-rules-tariff/",
        "shipping-furniture-to-the-usa": "/moving-to-north-america/", "baggage-shipping-deal": "/services/baggage-shipping/",
        "universal-prestige-relocations/apply": "/contact-us/",
    }
    import os as _os
    for slug, target in REDIRECTS.items():
        html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
                f'<title>Universal Relocations</title><meta name="robots" content="noindex">'
                f'<link rel="canonical" href="https://ur.macrohype.com{target}">'
                f'<meta http-equiv="refresh" content="0; url={target}">'
                f'<script>location.replace("{target}")</script></head>'
                f'<body>Redirecting to <a href="{target}">{target}</a>…</body></html>')
        d = _os.path.join(g["ROOT"] if isinstance(g.get("ROOT"), str) else str(g["ROOT"]), slug)
        _os.makedirs(d, exist_ok=True)
        with open(_os.path.join(d, "index.html"), "w") as f:
            f.write(html)
    print(f"Extra pages built: 20 content pages + {len(REDIRECTS)} redirects.")
