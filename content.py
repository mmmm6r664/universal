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
