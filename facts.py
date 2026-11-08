"""Country-facts content engine for unique, SEO-friendly per-page copy.
Uses real data (country_facts.json from the offline `countryinfo` dataset)
woven into varied templates, plus curated landmarks/industries for major
destinations. Every country/route page gets substantively different text."""
import json, os

_FACTS = json.load(open(os.path.join(os.path.dirname(__file__), "country_facts.json")))

_LANG = {"en":"English","es":"Spanish","fr":"French","de":"German","it":"Italian","pt":"Portuguese",
 "nl":"Dutch","ar":"Arabic","hi":"Hindi","zh":"Chinese","ja":"Japanese","ko":"Korean","ru":"Russian",
 "tr":"Turkish","pl":"Polish","sv":"Swedish","no":"Norwegian","da":"Danish","fi":"Finnish","el":"Greek",
 "he":"Hebrew","th":"Thai","vi":"Vietnamese","ms":"Malay","id":"Indonesian","ta":"Tamil","ur":"Urdu",
 "fa":"Persian","uk":"Ukrainian","ro":"Romanian","hu":"Hungarian","cs":"Czech","sk":"Slovak","bg":"Bulgarian",
 "hr":"Croatian","sl":"Slovenian","et":"Estonian","lv":"Latvian","lt":"Lithuanian","is":"Icelandic",
 "ga":"Irish","ka":"Georgian","kl":"Greenlandic","si":"Sinhala","ne":"Nepali","my":"Burmese","km":"Khmer",
 "sw":"Swahili","am":"Amharic","rw":"Kinyarwanda","mg":"Malagasy","sq":"Albanian","mk":"Macedonian"}
_CUR = {"USD":"US dollar","EUR":"euro","GBP":"pound sterling","INR":"Indian rupee","AED":"UAE dirham",
 "AUD":"Australian dollar","CAD":"Canadian dollar","NZD":"New Zealand dollar","SGD":"Singapore dollar",
 "SAR":"Saudi riyal","QAR":"Qatari riyal","KWD":"Kuwaiti dinar","BHD":"Bahraini dinar","OMR":"Omani rial",
 "JPY":"Japanese yen","CNY":"Chinese yuan","KRW":"South Korean won","CHF":"Swiss franc","SEK":"Swedish krona",
 "ZAR":"South African rand","BRL":"Brazilian real","MXN":"Mexican peso","HKD":"Hong Kong dollar",
 "MYR":"Malaysian ringgit","THB":"Thai baht","PHP":"Philippine peso","IDR":"Indonesian rupiah",
 "LKR":"Sri Lankan rupee","NPR":"Nepalese rupee","GEL":"Georgian lari","GMD":"Gambian dalasi",
 "BMD":"Bermudian dollar","DKK":"Danish krone","NOK":"Norwegian krone","PLN":"Polish zloty","TRY":"Turkish lira"}

# Curated landmarks + industries (accurate general knowledge) for major destinations.
_CUR8 = {
 "australia":("the Sydney Opera House, the Great Barrier Reef and the Outback","mining, agriculture, education, tourism and financial services"),
 "canada":("the Rocky Mountains, Niagara Falls and the CN Tower","energy, mining, manufacturing, technology and agriculture"),
 "uk":("Big Ben, Buckingham Palace and the Scottish Highlands","finance, creative industries, education, pharmaceuticals and aerospace"),
 "germany":("the Brandenburg Gate, Neuschwanstein Castle and the Black Forest","automotive, engineering, chemicals, machinery and manufacturing"),
 "france":("the Eiffel Tower, the French Riviera and the Loire châteaux","aerospace, luxury goods, tourism, agriculture and energy"),
 "singapore":("Marina Bay Sands, Gardens by the Bay and Sentosa","finance, shipping, electronics, biotech and petrochemicals"),
 "saudi-arabia":("the Kaaba in Mecca, the Red Sea coast and the Edge of the World","oil and gas, petrochemicals, construction and finance"),
 "qatar":("the Doha Corniche, Souq Waqif and the Museum of Islamic Art","oil and gas, finance, construction and aviation"),
 "new-zealand":("Milford Sound, the Southern Alps and Hobbiton","agriculture, tourism, film, wine and technology"),
 "japan":("Mount Fuji, Tokyo's skyline and Kyoto's temples","automotive, electronics, robotics, finance and manufacturing"),
 "italy":("the Colosseum, Venice's canals and the Amalfi Coast","fashion, automotive, food and wine, tourism and machinery"),
 "spain":("the Sagrada Família, the Alhambra and the beaches of the Costa del Sol","tourism, automotive, agriculture, renewable energy and finance"),
 "netherlands":("the Amsterdam canals, tulip fields and historic windmills","logistics, agriculture, finance, technology and energy"),
 "switzerland":("the Matterhorn, Lake Geneva and the Swiss Alps","banking, pharmaceuticals, precision engineering and watchmaking"),
 "ireland":("the Cliffs of Moher, the Ring of Kerry and Dublin's Georgian squares","technology, pharmaceuticals, finance and agriculture"),
 "china":("the Great Wall, the Forbidden City and the Shanghai skyline","manufacturing, technology, finance, shipping and construction"),
 "south-africa":("Table Mountain, Kruger National Park and the Garden Route","mining, finance, manufacturing, agriculture and tourism"),
 "brazil":("Christ the Redeemer, the Amazon and Rio's beaches","agriculture, mining, manufacturing, energy and finance"),
 "mexico":("Chichén Itzá, the beaches of Cancún and Mexico City's historic centre","manufacturing, automotive, oil, agriculture and tourism"),
 "thailand":("the Grand Palace, Phuket's beaches and Chiang Mai's temples","tourism, manufacturing, agriculture, automotive and electronics"),
 "malaysia":("the Petronas Towers, Langkawi and the Borneo rainforest","electronics, palm oil, petroleum, tourism and manufacturing"),
 "philippines":("Boracay, the Banaue Rice Terraces and Manila Bay","business process outsourcing, electronics, agriculture and tourism"),
 "japan2":("", ""),
 "sweden":("the Stockholm archipelago, Gamla Stan and Lapland","engineering, technology, automotive, forestry and design"),
 "norway":("the fjords, the Northern Lights and Oslo's harbour","oil and gas, shipping, fishing, renewable energy and technology"),
 "portugal":("Lisbon's trams, the Algarve coast and Porto's riverside","tourism, textiles, cork, wine and technology"),
 "kenya":("the Maasai Mara, Mount Kenya and the Indian Ocean coast","agriculture, tourism, finance, tea and horticulture"),
 "nigeria":("Lagos's skyline, Zuma Rock and the Niger Delta","oil and gas, agriculture, finance, entertainment and telecoms"),
 "egypt":("the Pyramids of Giza, the Nile and the Red Sea resorts","tourism, agriculture, textiles, oil and gas and the Suez Canal"),
 "bahrain":("the Bahrain Fort, the Formula 1 circuit and Manama's skyline","oil and gas, finance, aluminium and tourism"),
 "kuwait":("the Kuwait Towers, the Grand Mosque and the Arabian Gulf coast","oil and gas, finance and petrochemicals"),
 "oman":("the Sultan Qaboos Grand Mosque, Wadi Shab and the Musandam fjords","oil and gas, tourism, fishing and logistics"),
 "usa":("the Statue of Liberty, the Grand Canyon and New York's skyline","technology, finance, healthcare, manufacturing and energy"),
 "india":("the Taj Mahal, the Himalayas and Kerala's backwaters","IT and software, pharmaceuticals, manufacturing, finance and textiles"),
 "uae":("the Burj Khalifa, Sheikh Zayed Grand Mosque and the Palm Jumeirah","oil and gas, finance, real estate, tourism, aviation and logistics"),
}


def has(slug): return slug in _FACTS


def _langs(f):
    ls = [_LANG.get(x, x.upper()) for x in (f.get("languages") or [])][:3]
    if not ls: return ""
    if len(ls) == 1: return ls[0]
    return ", ".join(ls[:-1]) + " and " + ls[-1]


def _curr(f):
    cs = f.get("currencies") or []
    if not cs: return ""
    return _CUR.get(cs[0], cs[0])


def _pop(f):
    p = f.get("population") or 0
    if p >= 1_000_000: return f"{p/1_000_000:.1f} million".replace(".0 ", " ")
    if p: return f"{p:,}"
    return ""


def dname(slug):
    """Display name with article, e.g. 'the USA'."""
    f = _FACTS.get(slug)
    return f["name"] if f else slug.replace("-", " ").title()


def about_section(slug):
    """A unique 'About {country}' fact paragraph (prose + quick-facts), or '' if unknown."""
    f = _FACTS.get(slug)
    if not f: return ""
    nm = f["name"]; cap = f.get("capital"); pop = _pop(f); area = f.get("area") or 0
    lang = _langs(f); cur = _curr(f); sub = f.get("subregion") or f.get("region") or ""
    land, ind = _CUR8.get(slug, ("", ""))
    p1 = []
    if cap: p1.append(f"{nm.capitalize() if nm.islower() else nm} is in {sub}, with its capital at {cap}")
    if pop: p1.append(f"a population of around {pop}")
    if area: p1.append(f"a land area of about {area:,} km²")
    lead = ", ".join(p1) + "." if p1 else ""
    p2 = []
    if lang: p2.append(f"The main language is {lang}")
    if cur: p2.append(f"the currency is the {cur}")
    line2 = ", and ".join(p2) + "." if p2 else ""
    p3 = ""
    if land:
        p3 = f" {nm[0].upper()+nm[1:] if not nm.startswith('the') else nm} is known for {land}, and its economy is driven by {ind}."
    body = f"<p>{lead} {line2}{p3}</p>"
    # quick-facts strip
    rows = []
    if cap: rows.append(("Capital", cap))
    if pop: rows.append(("Population", pop))
    if area: rows.append(("Land area", f"{area:,} km²"))
    if lang: rows.append(("Language", lang))
    if cur: rows.append(("Currency", cur))
    chips = "".join(f'<div class="qf"><span>{k}</span><b>{v}</b></div>' for k, v in rows)
    return body + f'<div class="quick-facts">{chips}</div>'


def move_intro(slug, direction="to"):
    """A localized opening line unique to the country."""
    f = _FACTS.get(slug)
    if not f: return ""
    nm = f["name"]; cap = f.get("capital"); lang = _langs(f)
    bits = []
    if cap: bits.append(f"whether you're heading for {cap} or beyond")
    extra = f" Settling into a {lang}-speaking country" if lang and lang != "English" else ""
    return (f"Planning a move {direction} {nm}? {('Relocating ' + direction + ' ' + nm).capitalize()} means "
            f"coordinating ocean or air freight, export-grade packing and customs clearance at both ends — "
            f"{bits[0] if bits else 'door to door'}.{extra}")


def route_angle(from_slug, to_slug):
    """A unique 'why people move from X to Y' paragraph using both countries' facts."""
    a = _FACTS.get(from_slug); b = _FACTS.get(to_slug)
    if not a or not b: return ""
    an = a["name"]; bn = b["name"]; bcap = b.get("capital"); bind = _CUR8.get(to_slug, ("", ""))[1]
    dem = a.get("demonym") or ""
    who = f"{dem} expats" if dem else f"people from {an}"
    why = []
    if bind:
        why.append(f"{who} move {('to ' + bn)} for work in {bind}")
    else:
        why.append(f"{who} relocate to {bn} for work, study and family")
    tail = f" {bcap} is a common landing point, and we move households of every size along the {an}-to-{bn} corridor." if bcap else ""
    return f"{why[0]}.{tail}"
