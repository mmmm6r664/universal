/* ==========================================================================
   Universal Relocations — Move Assistant
   Warm, conversational, natural-language lead capture with an instant estimate.
   Full page at /assistant/. Entry points elsewhere navigate there with ?q=.
   ========================================================================== */
(function () {
  "use strict";

  /* ---------- Estimate ranges (PLACEHOLDER — swap for real rate card) -------- */
  var RATES = {
    international: {
      baggage: [600, 1500], studio: [1800, 3000], "1br": [2500, 4500],
      "2br": [4000, 7000], "3br": [6000, 10000], "4br": [9000, 15000], car: [1500, 4000]
    },
    domestic: {
      baggage: [300, 800], studio: [900, 1800], "1br": [1500, 3000],
      "2br": [2500, 4500], "3br": [4000, 7000], "4br": [6000, 10000], car: [600, 1800]
    }
  };
  var SIZE_LABELS = {
    baggage: "Baggage / boxes", studio: "Studio", "1br": "1 bedroom", "2br": "2 bedrooms",
    "3br": "3 bedrooms", "4br": "4+ bedrooms", car: "Vehicle / car"
  };
  var fmt = function (n) { return "$" + n.toLocaleString("en-US"); };

  /* ------------------------------ NL parsing -------------------------------- */
  var US_RE = /\b(usa|u\.?s\.?a?\.?|united states|america|alabama|alaska|arizona|arkansas|california|colorado|connecticut|delaware|florida|georgia|hawaii|idaho|illinois|indiana|iowa|kansas|kentucky|louisiana|maine|maryland|massachusetts|michigan|minnesota|mississippi|missouri|montana|nebraska|nevada|new hampshire|new jersey|new mexico|new york|north carolina|north dakota|ohio|oklahoma|oregon|pennsylvania|rhode island|south carolina|south dakota|tennessee|texas|utah|vermont|virginia|washington|west virginia|wisconsin|wyoming|nyc|los angeles|san francisco|chicago|houston|dallas|miami|atlanta|boston|seattle|denver|phoenix|austin|san diego|jersey)\b/i;
  function isUS(s) { return s && US_RE.test(s); }
  function titleCase(s) { return s.replace(/\s+/g, " ").trim().replace(/\b\w/g, function (c) { return c.toUpperCase(); }); }
  function firstName(n) { return (n || "").trim().split(/\s+/)[0] || "there"; }

  function parsePrompt(text) {
    var t = " " + text.toLowerCase() + " ";
    var out = { from: "", to: "", sizeKey: "", typeLabel: "", route: "" };
    var m = text.match(/from\s+(.+?)\s+to\s+([^.?!,;]+)/i);
    if (m) { out.from = titleCase(m[1]); out.to = titleCase(m[2]); }
    else { var m2 = text.match(/\bto\s+([a-z .'-]{2,40})/i); if (m2) out.to = titleCase(m2[1]); }
    if (/\b(car|vehicle|motorcycle|motorbike|scooter|van|suv|automobile)\b/i.test(t)) {
      out.sizeKey = "car"; out.typeLabel = "vehicle shipment";
    } else if (/\b(box|boxes|carton|cartons|kg|kilo|luggage|baggage|suitcase|suitcases|parcel)\b/i.test(t)) {
      out.sizeKey = "baggage"; out.typeLabel = "baggage / box shipment";
    } else if (/\bstudio\b/i.test(t)) {
      out.sizeKey = "studio"; out.typeLabel = "household move";
    } else {
      var bed = t.match(/(\d+)\s*(?:bed\s*room|bedroom|bed|br|bhk|rk)\b/i);
      if (bed) { var n = parseInt(bed[1], 10); out.sizeKey = n >= 4 ? "4br" : (n <= 1 ? "1br" : n + "br"); out.typeLabel = "household move"; }
      else if (/\b(house|villa|apartment|flat|home|office)\b/i.test(t)) { out.typeLabel = "household move"; }
    }
    if (out.from || out.to) out.route = (isUS(out.from) && isUS(out.to)) ? "domestic" : "international";
    return out;
  }

  /* --------- Route-aware "what to know about your move" guidance ------------ */
  function whatToKnow(d) {
    var intl = d.route !== "domestic";
    var fromto = (d.from && d.to) ? (" from <b>" + d.from + "</b> to <b>" + d.to + "</b>") : "";
    var lead = "Here's what's good to know about your move" + fromto + ":";
    var body;
    if (d.sizeKey === "car") {
      body = intl
        ? "We ship vehicles internationally by container or RoRo (roll-on/roll-off). We handle the export and import paperwork, marine insurance options, and clearance and delivery at the destination — so your car arrives safely and legally."
        : "We move vehicles across the country on insured carriers, with full documentation and door-to-door coordination.";
    } else if (d.sizeKey === "baggage") {
      body = intl
        ? "For baggage and boxes, our groupage / baggage-shipping service is the most cost-effective way to send a few items overseas — door-to-door, fully tracked, and with no airline excess-baggage fees. We consolidate your boxes with other shipments on the same route to keep the price down."
        : "For a few boxes within the country, we offer affordable door-to-door box shipping with full tracking from pickup to delivery.";
    } else {
      body = intl
        ? "Most international household moves travel by ocean freight, door-to-door. We take care of export-grade packing, all customs documentation and clearance at both ends, and delivery right into your new home. Depending on how much you're moving, you can share a container (groupage) to save cost, or take a full container for a faster, dedicated move. Transit time varies by route — your move manager will confirm exact timing."
        : "For a move within the country, our team handles professional packing, loading, licensed transport and delivery — local or long-distance — with transparent, upfront pricing and real-time tracking.";
    }
    return "Thank you for considering <b>Universal Relocations</b> — we'd love to help! 🌍<br><br>" + lead + "<br><br>" + body;
  }

  /* ----------------------------- Message styles ----------------------------- */
  var css = `
  .ura-row{display:flex;gap:9px;align-items:flex-end;max-width:85%}
  .ura-row.ura-bot{align-self:flex-start}
  .ura-row.ura-user{align-self:flex-end;flex-direction:row-reverse}
  .ura-bubble{padding:12px 16px;border-radius:14px;font-size:15px;line-height:1.6;color:#1c2434;box-shadow:0 1px 3px rgba(0,5,110,.08)}
  .ura-bot .ura-bubble{background:#fff;border-bottom-left-radius:4px}
  .ura-user .ura-bubble{background:#2731c9;color:#fff;border-bottom-right-radius:4px}
  .ura-mini{width:30px;height:30px;border-radius:50%;background:linear-gradient(120deg,#00056e,#2731c9);flex:none;display:grid;place-items:center}
  .ura-mini svg{width:17px;height:17px;fill:#fff}
  .ura-typing{display:flex;gap:4px;padding:14px}
  .ura-typing span{width:7px;height:7px;border-radius:50%;background:#9fb0ce;animation:ura-b 1.2s infinite}
  .ura-typing span:nth-child(2){animation-delay:.2s}.ura-typing span:nth-child(3){animation-delay:.4s}
  @keyframes ura-b{0%,60%,100%{opacity:.3;transform:translateY(0)}30%{opacity:1;transform:translateY(-4px)}}
  .ura-quick{display:flex;flex-wrap:wrap;gap:9px;margin-top:2px;align-self:flex-start;max-width:92%}
  .ura-chip{background:#fff;border:1.5px solid #2731c9;color:#2731c9;border-radius:999px;padding:10px 16px;font:500 14px/1 "Lora",serif;cursor:pointer;transition:.15s}
  .ura-chip:hover{background:#2731c9;color:#fff}
  .ura-estimate{background:#fff;border:1px solid #e4e8f0;border-radius:14px;padding:18px;box-shadow:0 2px 10px rgba(0,5,110,.08)}
  .ura-estimate .ura-amt{font-size:27px;font-weight:700;color:#00056e;font-family:"Playfair Display",serif}
  .ura-estimate .ura-lbl{font-size:13px;color:#8a94a6;margin-top:3px}
  .ura-estimate small{display:block;margin-top:11px;font-size:12px;color:#8a94a6;line-height:1.5}
  .ura-input{display:flex;gap:9px}
  .ura-input input{flex:1;border:1.5px solid #e4e8f0;border-radius:999px;padding:13px 17px;font:inherit;font-size:15px;outline:none}
  .ura-input input:focus{border-color:#2731c9}
  .ura-input button{background:#2731c9;border:0;border-radius:50%;width:46px;height:46px;flex:none;cursor:pointer;display:grid;place-items:center}
  .ura-input button:hover{background:#00056e}
  .ura-input button svg{width:19px;height:19px;fill:#fff}
  `;
  var style = document.createElement("style"); style.textContent = css; document.head.appendChild(style);
  var MINI = '<svg viewBox="0 0 24 24"><path d="M3 14l1.5 6h15L21 14M5 14V7l7-3 7 3v7M9 9h6" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';

  var stream = document.getElementById("chat-stream");
  var inbar = document.getElementById("chat-inputbar");
  if (stream && inbar) { runConversation(); } else { setupEntryPoints(); }

  /* --------------------------- Conversation engine -------------------------- */
  function runConversation() {
    var body = stream, foot = inbar;
    var data = freshData();

    function scroll() { body.scrollTop = body.scrollHeight; }
    function botSay(html, cb, delay) {
      var row = document.createElement("div");
      row.className = "ura-row ura-bot";
      row.innerHTML = '<div class="ura-mini">' + MINI + '</div><div class="ura-bubble"><div class="ura-typing"><span></span><span></span><span></span></div></div>';
      body.appendChild(row); scroll();
      setTimeout(function () { row.querySelector(".ura-bubble").innerHTML = html; scroll(); if (cb) cb(); }, delay || 700);
    }
    // say several bot bubbles in sequence
    function botSeq(list, done) {
      if (!list.length) { if (done) done(); return; }
      botSay(list[0], function () { botSeq(list.slice(1), done); });
    }
    function userSay(text) {
      var row = document.createElement("div");
      row.className = "ura-row ura-user";
      row.innerHTML = '<div class="ura-bubble"></div>';
      row.querySelector(".ura-bubble").textContent = text;
      body.appendChild(row); scroll();
    }
    function hint(text) { foot.innerHTML = '<div class="chat-hint">' + text + '</div>'; }
    function chips(options, onPick) {
      var wrap = document.createElement("div");
      wrap.className = "ura-quick";
      options.forEach(function (o) {
        var c = document.createElement("button");
        c.className = "ura-chip"; c.textContent = o.label;
        c.onclick = function () { wrap.remove(); userSay(o.label); onPick(o.value, o.label); };
        wrap.appendChild(c);
      });
      body.appendChild(wrap); scroll();
      hint("Pick an option above ↑");
    }
    function askText(placeholder, type, onSubmit) {
      foot.innerHTML = '<form class="ura-input"><input type="' + (type || "text") + '" placeholder="' + placeholder + '" autocomplete="off">' +
        '<button type="submit" aria-label="Send"><svg viewBox="0 0 24 24"><path d="M3 11l18-8-8 18-2-7-8-3z"/></svg></button></form>';
      var form = foot.querySelector("form"), input = form.querySelector("input");
      input.focus();
      form.onsubmit = function (e) { e.preventDefault(); var v = input.value.trim(); if (!v) return; userSay(v); foot.innerHTML = ""; onSubmit(v); };
    }
    function finish() {
      foot.innerHTML = '<button class="chat-restart" type="button">↺ Start a new estimate</button>';
      foot.querySelector("button").onclick = function () { location.href = "/assistant/"; };
    }

    /* ----- flow ----- */
    function askNext() {
      if (!data.from) return askFrom();
      if (!data.to) return askTo();
      if (!data.route) data.route = (isUS(data.from) && isUS(data.to)) ? "domestic" : "international";
      if (!data.sizeKey) return (data.typeLabel === "household move" || data.typeLabel === "office / commercial move") ? askSize() : askWhat();
      if (!data.infoShown) return showInfo();
      if (!data.date) return askDate();
      if (!data.special) return askSpecial();
      if (!data.estimateShown) return showEstimate();
      if (!data.name) return askName();
      if (!data.email) return askEmail();
      if (!data.phone) return askPhone();
      if (!data.notes) return askNotes();
      return submitLead();
    }

    function askWhat() {
      botSay("And what are you moving?", function () {
        chips([
          { label: "A full home / household", value: "home" },
          { label: "An office / business", value: "office" },
          { label: "Just a few boxes / baggage", value: "baggage" },
          { label: "A car / vehicle", value: "car" }
        ], function (v) {
          if (v === "home") { data.typeLabel = "household move"; return askSize(); }
          if (v === "office") { data.typeLabel = "office / commercial move"; return askSize(); }
          if (v === "baggage") { data.typeLabel = "baggage / box shipment"; data.sizeKey = "baggage"; return askNext(); }
          data.typeLabel = "vehicle shipment"; data.sizeKey = "car"; askNext();
        });
      });
    }
    function askFrom() { botSay("Lovely. So I can tailor everything to you — which city and country are you moving <b>from</b>?", function () { askText("e.g. Dubai, UAE", "text", function (v) { data.from = v; askNext(); }); }); }
    function askTo() { botSay("And where are you headed?", function () { askText("e.g. New York, USA", "text", function (v) { data.to = v; askNext(); }); }); }
    function askSize() {
      botSay("Roughly how big is it? This helps me size the right shipping option.", function () {
        chips(["studio", "1br", "2br", "3br", "4br"].map(function (k) { return { label: SIZE_LABELS[k], value: k }; }),
          function (v) { data.sizeKey = v; askNext(); });
      });
    }
    function showInfo() {
      data.infoShown = true;
      botSeq([ whatToKnow(data), "A few more quick questions and I'll have an instant ballpark estimate for you — then one of our move managers can follow up with an exact, no-obligation quote. 😊" ], askNext);
    }
    function askDate() {
      botSay("When are you hoping to make the move? Even a rough idea helps us plan the best shipping schedule.", function () {
        chips([
          { label: "As soon as possible", value: "ASAP" }, { label: "In 1–3 months", value: "1-3 months" },
          { label: "In 3–6 months", value: "3-6 months" }, { label: "Just exploring for now", value: "Flexible" }
        ], function (v) { data.date = v; askNext(); });
      });
    }
    function askSpecial() {
      botSay("Are there any special items we should plan for? These sometimes need extra care or paperwork.", function () {
        chips([
          { label: "A vehicle / car", value: "Vehicle" }, { label: "A piano", value: "Piano" },
          { label: "Fine art / antiques", value: "Fine art / antiques" }, { label: "Fragile / valuables", value: "Fragile / valuables" },
          { label: "Pets", value: "Pets" }, { label: "Nothing special", value: "None" }
        ], function (v) { data.special = v; askNext(); });
      });
    }
    function showEstimate() {
      data.estimateShown = true;
      botSay("Perfect — let me put a ballpark figure together for you…", function () {
        var table = RATES[data.route] || RATES.international;
        var range = table[data.sizeKey] || table["1br"];
        data.estimate = fmt(range[0]) + " – " + fmt(range[1]);
        var routeWord = data.route === "domestic" ? "interstate" : "international";
        var est = '<div class="ura-estimate"><div class="ura-amt">' + data.estimate + '</div>' +
          '<div class="ura-lbl">Estimated ' + routeWord + ' ' + SIZE_LABELS[data.sizeKey].toLowerCase() + ' move' +
          (data.from && data.to ? ' · ' + data.from + ' → ' + data.to : '') + '</div>' +
          '<small>This is a ballpark to give you a sense — your exact quote depends on volume, access and the services you choose, and it is completely free.</small></div>';
        botSeq([ est,
          "Here's how we'll help from here: a dedicated move manager reviews your details, arranges a quick (virtual or in-person) survey to confirm volume, and sends you a precise, all-inclusive quote — covering packing, shipping, customs and delivery.",
          "Shall I have them prepare your detailed quote? I'll just need a few contact details so we can send it over. 💌"
        ], askNext);
      });
    }
    function askName() { botSay("Wonderful! Who am I speaking with — what's your name?", function () { askText("Your name", "text", function (v) { data.name = v; askNext(); }); }); }
    function askEmail() {
      botSay("Great to meet you, " + firstName(data.name) + "! What's the best email to send your quote and move plan to?", function () {
        askText("you@email.com", "email", function (v) {
          if (!/.+@.+\..+/.test(v)) { botSay("Hmm, that doesn't look quite right — could you pop your email in again?", askEmail); return; }
          data.email = v; askNext();
        });
      });
    }
    function askPhone() { botSay("And the best phone number for your move manager to reach you on? (we'll only use it about your move)", function () { askText("Phone number (with country code)", "tel", function (v) { data.phone = v; askNext(); }); }); }
    function askNotes() {
      botSay("Last one — is there anything else you'd like us to know? Timelines, budget, specific concerns… anything helps. (Or just tap “Nothing for now”.)", function () {
        var skip = document.createElement("div");
        skip.className = "ura-quick";
        var b = document.createElement("button");
        b.className = "ura-chip"; b.textContent = "Nothing for now";
        b.onclick = function () { skip.remove(); userSay("Nothing for now"); data.notes = "—"; submitLead(); };
        body.appendChild(skip); scroll();
        askText("Type anything you'd like to add…", "text", function (v) { skip.remove(); data.notes = v; submitLead(); });
      });
    }

    function submitLead() {
      hint("Sending your details…");
      botSay("Thank you, " + firstName(data.name) + "! Sending everything to our move team now…", function () {
        fetch("/api/lead", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(data) })
          .then(function (r) { return r.json(); }).catch(function () { return { ok: false }; })
          .then(function () {
            var summary = "<b>Your move at a glance</b><br>" +
              "• " + (data.typeLabel ? data.typeLabel.charAt(0).toUpperCase() + data.typeLabel.slice(1) : "Move") +
              (data.from && data.to ? "<br>• " + data.from + " → " + data.to : "") +
              (data.sizeKey ? "<br>• Size: " + SIZE_LABELS[data.sizeKey] : "") +
              (data.date ? "<br>• Timing: " + data.date : "") +
              (data.special && data.special !== "None" ? "<br>• Special: " + data.special : "") +
              (data.estimate ? "<br>• Ballpark: " + data.estimate : "");
            botSeq([
              "🎉 All set, " + firstName(data.name) + " — thank you for choosing Universal Relocations! Your request is in, and a dedicated move manager will reach out very soon with your detailed quote and the exact next steps for your route.",
              summary,
              "Need us sooner? Call <b>1-888-323-7356</b> (USA), <b>1-800-103-7356</b> (India) or <b>800-13-7356</b> (UAE), or <a href='https://portal.universalrelocations.com/moving-calculator/' target='_blank' style='color:#2731c9'>use the full moving calculator</a>. We can't wait to help you move with ease. 🌍"
            ], finish);
          });
      });
    }

    /* ----- entry ----- */
    var q = (new URLSearchParams(location.search)).get("q");
    if (q) {
      userSay(q);
      var p = parsePrompt(q);
      data.from = p.from || ""; data.to = p.to || ""; data.sizeKey = p.sizeKey || "";
      data.typeLabel = p.typeLabel || ""; data.route = p.route || "";
      askNext();
    } else {
      botSeq([
        "Hi, and thank you for considering <b>Universal Relocations</b>! 👋 I'm your Move Assistant.",
        "Tell me about your move in your own words — where you're moving from and to, and roughly what you're shipping — and I'll walk you through it and get you an instant ballpark estimate."
      ], askNext);
    }
  }

  /* ========================= ENTRY POINTS (other pages) ===================== */
  function go(prompt) { location.href = "/assistant/" + (prompt ? "?q=" + encodeURIComponent(prompt) : ""); }

  function setupEntryPoints() {
    document.addEventListener("click", function (e) {
      var t = e.target.closest("[data-open-assistant]");
      if (t) { e.preventDefault(); go(); }
    });
    var form = document.getElementById("hero-prompt-form");
    if (form) {
      var input = document.getElementById("hero-prompt-input");
      form.addEventListener("submit", function (e) { e.preventDefault(); go(input.value.trim() || "I'd like help planning a move."); });
      document.querySelectorAll(".hs-chip").forEach(function (chip) {
        chip.addEventListener("click", function () { go(chip.getAttribute("data-prompt")); });
      });
      var examples = [
        "I want to move my 3 bedroom apartment from New York to Delhi",
        "I want to ship 5 boxes of 25 kg each from Chennai to San Francisco",
        "I want to move my car from Dubai to Toronto",
        "How much will it cost to move 10 boxes from Dallas to Abu Dhabi",
        "Moving a 2 bedroom home from London to Sydney",
        "Ship my motorcycle from Mumbai to Houston"
      ];
      var ei = 0, ci = 0, deleting = false, paused = false, typing = true;
      function tick() {
        if (!typing) return;
        if (document.activeElement === input || input.value) { input.placeholder = "Describe your move…"; setTimeout(tick, 800); return; }
        var full = examples[ei];
        if (paused) { paused = false; deleting = true; setTimeout(tick, 1400); return; }
        if (!deleting) { ci++; input.placeholder = full.slice(0, ci); if (ci >= full.length) { paused = true; setTimeout(tick, 100); return; } setTimeout(tick, 42); }
        else { ci--; input.placeholder = full.slice(0, ci); if (ci <= 0) { deleting = false; ei = (ei + 1) % examples.length; setTimeout(tick, 300); return; } setTimeout(tick, 22); }
      }
      input.addEventListener("focus", function () { typing = false; input.placeholder = "Describe your move…"; });
      tick();
    }
  }

  function freshData() {
    return { typeLabel: "", route: "", from: "", to: "", sizeKey: "", date: "", special: "", name: "", email: "", phone: "", notes: "", estimate: "", infoShown: false, estimateShown: false };
  }
})();
