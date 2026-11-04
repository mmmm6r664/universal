/* ==========================================================================
   Universal Relocations — Move Assistant
   Natural-language, chat-style lead capture with an instant estimate.
   Opens as a FULL PAGE at /assistant/ (not a popup).
   - Any entry point (hero prompt, suggestion chips, "Get a Quote", chat button)
     navigates to /assistant/?q=<prompt>.
   - On /assistant/ the conversation parses the prompt, fills in missing details,
     shows an estimate, and submits the lead.
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

  function parsePrompt(text) {
    var t = " " + text.toLowerCase() + " ";
    var out = { from: "", to: "", sizeKey: "", typeLabel: "", route: "" };
    var m = text.match(/from\s+(.+?)\s+to\s+([^.?!,;]+)/i);
    if (m) { out.from = titleCase(m[1]); out.to = titleCase(m[2]); }
    else { var m2 = text.match(/\bto\s+([a-z .'-]{2,40})/i); if (m2) out.to = titleCase(m2[1]); }

    if (/\b(car|vehicle|motorcycle|motorbike|scooter|van|suv|automobile)\b/i.test(t)) {
      out.sizeKey = "car"; out.typeLabel = "Auto / vehicle shipping";
    } else if (/\b(box|boxes|carton|cartons|kg|kilo|luggage|baggage|suitcase|suitcases|parcel)\b/i.test(t)) {
      out.sizeKey = "baggage"; out.typeLabel = "Baggage / box shipping";
    } else if (/\bstudio\b/i.test(t)) {
      out.sizeKey = "studio"; out.typeLabel = "Household move";
    } else {
      var bed = t.match(/(\d+)\s*(?:bed\s*room|bedroom|bed|br|bhk|rk)\b/i);
      if (bed) {
        var n = parseInt(bed[1], 10);
        out.sizeKey = n >= 4 ? "4br" : (n <= 1 ? "1br" : n + "br");
        out.typeLabel = "Household move";
      } else if (/\b(house|villa|apartment|flat|home|office)\b/i.test(t)) { out.typeLabel = "Household move"; }
    }
    if (out.from || out.to) out.route = (isUS(out.from) && isUS(out.to)) ? "domestic" : "international";
    return out;
  }

  /* ----------------------------- Message styles ----------------------------- */
  var css = `
  .ura-launch{position:fixed;right:20px;bottom:88px;z-index:95;display:inline-flex;align-items:center;gap:10px;text-decoration:none;
    background:#f4a124;color:#fff;border:0;border-radius:999px;padding:13px 20px;font:600 15px/1 "Lora",system-ui,sans-serif;
    cursor:pointer;box-shadow:0 10px 30px rgba(11,43,94,.28);transition:transform .2s,box-shadow .2s}
  .ura-launch:hover{transform:translateY(-2px);box-shadow:0 14px 36px rgba(11,43,94,.34);color:#fff}
  .ura-launch svg{width:20px;height:20px;fill:#fff}
  .ura-launch .ura-dot{position:absolute;top:-4px;right:-4px;width:12px;height:12px;background:#e53e3e;border:2px solid #fff;border-radius:50%}
  @media(max-width:600px){.ura-launch span{display:none}.ura-launch{padding:14px;bottom:84px}}
  .ura-row{display:flex;gap:9px;align-items:flex-end;max-width:85%}
  .ura-row.ura-bot{align-self:flex-start}
  .ura-row.ura-user{align-self:flex-end;flex-direction:row-reverse}
  .ura-bubble{padding:11px 15px;border-radius:14px;font-size:15px;line-height:1.55;color:#1c2434;box-shadow:0 1px 3px rgba(11,43,94,.08)}
  .ura-bot .ura-bubble{background:#fff;border-bottom-left-radius:4px}
  .ura-user .ura-bubble{background:#1f5fbf;color:#fff;border-bottom-right-radius:4px}
  .ura-mini{width:30px;height:30px;border-radius:50%;background:linear-gradient(120deg,#07204a,#1f5fbf);flex:none;display:grid;place-items:center}
  .ura-mini svg{width:17px;height:17px;fill:#fff}
  .ura-typing{display:flex;gap:4px;padding:14px}
  .ura-typing span{width:7px;height:7px;border-radius:50%;background:#9fb0ce;animation:ura-b 1.2s infinite}
  .ura-typing span:nth-child(2){animation-delay:.2s}.ura-typing span:nth-child(3){animation-delay:.4s}
  @keyframes ura-b{0%,60%,100%{opacity:.3;transform:translateY(0)}30%{opacity:1;transform:translateY(-4px)}}
  .ura-quick{display:flex;flex-wrap:wrap;gap:9px;margin-top:2px;align-self:flex-start;max-width:90%}
  .ura-chip{background:#fff;border:1.5px solid #1f5fbf;color:#1f5fbf;border-radius:999px;padding:10px 16px;font:500 14px/1 "Lora",sans-serif;cursor:pointer;transition:.15s}
  .ura-chip:hover{background:#1f5fbf;color:#fff}
  .ura-estimate{background:#fff;border:1px solid #e4e8f0;border-radius:14px;padding:18px;box-shadow:0 2px 10px rgba(11,43,94,.08)}
  .ura-estimate .ura-amt{font-size:27px;font-weight:800;color:#0b2b5e}
  .ura-estimate .ura-lbl{font-size:13px;color:#8a94a6;margin-top:3px}
  .ura-estimate small{display:block;margin-top:11px;font-size:12px;color:#8a94a6;line-height:1.5}
  .ura-input{display:flex;gap:9px}
  .ura-input input{flex:1;border:1.5px solid #e4e8f0;border-radius:999px;padding:13px 17px;font:inherit;font-size:15px;outline:none}
  .ura-input input:focus{border-color:#1f5fbf}
  .ura-input button{background:#1f5fbf;border:0;border-radius:50%;width:46px;height:46px;flex:none;cursor:pointer;display:grid;place-items:center}
  .ura-input button:hover{background:#07204a}
  .ura-input button svg{width:19px;height:19px;fill:#fff}
  `;
  var style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  var MINI = '<svg viewBox="0 0 24 24"><path d="M3 14l1.5 6h15L21 14M5 14V7l7-3 7 3v7M9 9h6" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';

  /* =========================================================================
     PAGE MODE — the conversation runs here (/assistant/)
     ========================================================================= */
  var stream = document.getElementById("chat-stream");
  var inbar = document.getElementById("chat-inputbar");

  if (stream && inbar) {
    runConversation();
  } else {
    setupEntryPoints();
  }

  /* --------------------------- Conversation engine -------------------------- */
  function runConversation() {
    var body = stream, foot = inbar;
    var data = freshData();

    function freshDataLocal() { return freshData(); }
    function scroll() { body.scrollTop = body.scrollHeight; }

    function botSay(html, cb) {
      var row = document.createElement("div");
      row.className = "ura-row ura-bot";
      row.innerHTML = '<div class="ura-mini">' + MINI + '</div><div class="ura-bubble"><div class="ura-typing"><span></span><span></span><span></span></div></div>';
      body.appendChild(row); scroll();
      setTimeout(function () { row.querySelector(".ura-bubble").innerHTML = html; scroll(); if (cb) cb(); }, 600);
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

    /* ---- flow ---- */
    function askNext() {
      if (!data.typeLabel && !data.sizeKey) return askType();
      if (!data.from) return askFrom();
      if (!data.to) return askTo();
      if (!data.sizeKey) return askSize();
      if (!data.route) data.route = (isUS(data.from) && isUS(data.to)) ? "domestic" : "international";
      if (!data.date) return askDate();
      if (!data.estimateShown) return showEstimate();
      if (!data.name) return askName();
      if (!data.email) return askEmail();
      if (!data.phone) return askPhone();
      return submitLead();
    }
    function askType() {
      botSay("What kind of move are you planning?", function () {
        chips([
          { label: "International move", value: "i|Household move" },
          { label: "Interstate / domestic move", value: "d|Household move" },
          { label: "Ship baggage / boxes", value: "?|Baggage / box shipping" },
          { label: "Ship a car / vehicle", value: "?|Auto / vehicle shipping" }
        ], function (v) {
          var p = v.split("|"); data.typeLabel = p[1];
          if (p[0] === "i") data.route = "international";
          if (p[0] === "d") data.route = "domestic";
          if (/Baggage/.test(p[1])) data.sizeKey = "baggage";
          if (/Auto/.test(p[1])) data.sizeKey = "car";
          askNext();
        });
      });
    }
    function askFrom() { botSay("Where are you moving <b>from</b>? (city &amp; country)", function () { askText("e.g. New York, USA", "text", function (v) { data.from = v; askNext(); }); }); }
    function askTo() { botSay("And where to?", function () { askText("e.g. Delhi, India", "text", function (v) { data.to = v; askNext(); }); }); }
    function askSize() {
      botSay("How much are you moving?", function () {
        chips(["baggage", "studio", "1br", "2br", "3br", "4br"].map(function (k) { return { label: SIZE_LABELS[k], value: k }; }),
          function (v) { data.sizeKey = v; askNext(); });
      });
    }
    function askDate() {
      botSay("When are you hoping to move?", function () {
        chips([
          { label: "As soon as possible", value: "ASAP" }, { label: "In 1–3 months", value: "1-3 months" },
          { label: "In 3–6 months", value: "3-6 months" }, { label: "Just exploring", value: "Flexible" }
        ], function (v) { data.date = v; askNext(); });
      });
    }
    function showEstimate() {
      data.estimateShown = true;
      botSay("Thanks! Crunching the numbers for your move…", function () {
        var table = RATES[data.route] || RATES.international;
        var range = table[data.sizeKey] || table["1br"];
        data.estimate = fmt(range[0]) + " – " + fmt(range[1]);
        var routeWord = data.route === "domestic" ? "interstate" : "international";
        var est = '<div class="ura-estimate"><div class="ura-amt">' + data.estimate + '</div>' +
          '<div class="ura-lbl">Estimated ' + routeWord + ' ' + SIZE_LABELS[data.sizeKey].toLowerCase() + ' move' +
          (data.from && data.to ? ' · ' + data.from + ' → ' + data.to : '') + '</div>' +
          '<small>Ballpark only — your exact quote depends on volume, access and services. Our team will confirm it free of charge.</small></div>';
        botSay(est, function () {
          botSay("Want us to prepare a <b>detailed, no-obligation quote</b> and lock this in? Just drop your details 👇", askNext);
        });
      });
    }
    function askName() { botSay("What's your name?", function () { askText("Your name", "text", function (v) { data.name = v; askNext(); }); }); }
    function askEmail() {
      botSay("Nice to meet you, " + data.name.split(" ")[0] + "! Best email for your quote?", function () {
        askText("you@email.com", "email", function (v) {
          if (!/.+@.+\..+/.test(v)) { botSay("Hmm, that doesn't look like an email — mind trying again?", askEmail); return; }
          data.email = v; askNext();
        });
      });
    }
    function askPhone() { botSay("And a phone number our move manager can reach you on?", function () { askText("Phone number", "tel", function (v) { data.phone = v; askNext(); }); }); }
    function submitLead() {
      hint("Submitting…");
      botSay("Perfect — submitting your request…", function () {
        fetch("/api/lead", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(data) })
          .then(function (r) { return r.json(); }).catch(function () { return { ok: false }; })
          .then(function () {
            botSay("✅ All set, " + data.name.split(" ")[0] + "! Your request is in and a Universal move manager will reach out shortly with your detailed quote.<br><br>Need us sooner? Call <b>1-888-323-7356</b> or <a href='https://portal.universalrelocations.com/moving-calculator/' target='_blank' style='color:#1f5fbf'>use the full moving calculator</a>.", finish);
          });
      });
    }

    /* ---- entry ---- */
    var q = (new URLSearchParams(location.search)).get("q");
    if (q) {
      userSay(q);
      var p = parsePrompt(q);
      data.from = p.from || ""; data.to = p.to || ""; data.sizeKey = p.sizeKey || "";
      data.typeLabel = p.typeLabel || ""; data.route = p.route || "";
      var known = [];
      if (data.sizeKey) known.push(SIZE_LABELS[data.sizeKey].toLowerCase());
      if (data.from) known.push("from " + data.from);
      if (data.to) known.push("to " + data.to);
      var ack = known.length
        ? "Got it — a move " + known.join(" ") + ". Let me fill in a couple of details and get you an estimate."
        : "Great — let me grab a few details to get you an instant estimate.";
      botSay(ack, askNext);
    } else {
      botSay("Hi! 👋 I'm the Universal Move Assistant. I'll ask a few quick questions and give you an instant ballpark estimate — then our team can follow up with an exact quote.", askNext);
    }
  }

  /* =========================================================================
     ENTRY POINTS (all other pages) — navigate to the full page
     ========================================================================= */
  function go(prompt) {
    location.href = "/assistant/" + (prompt ? "?q=" + encodeURIComponent(prompt) : "");
  }

  function setupEntryPoints() {
    // Any [data-open-assistant] element -> /assistant/
    document.addEventListener("click", function (e) {
      var t = e.target.closest("[data-open-assistant]");
      if (t) { e.preventDefault(); go(); }
    });

    // Hero prompt bar
    var form = document.getElementById("hero-prompt-form");
    if (form) {
      var input = document.getElementById("hero-prompt-input");
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        go(input.value.trim() || "I'd like help planning a move.");
      });
      document.querySelectorAll(".hs-chip").forEach(function (chip) {
        chip.addEventListener("click", function () { go(chip.getAttribute("data-prompt")); });
      });

      // Rotating placeholder (typewriter)
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
        if (!deleting) {
          ci++; input.placeholder = full.slice(0, ci);
          if (ci >= full.length) { paused = true; setTimeout(tick, 100); return; }
          setTimeout(tick, 42);
        } else {
          ci--; input.placeholder = full.slice(0, ci);
          if (ci <= 0) { deleting = false; ei = (ei + 1) % examples.length; setTimeout(tick, 300); return; }
          setTimeout(tick, 22);
        }
      }
      input.addEventListener("focus", function () { typing = false; input.placeholder = "Describe your move…"; });
      tick();
    }
  }

  function freshData() {
    return { typeLabel: "", route: "", from: "", to: "", sizeKey: "", date: "", name: "", email: "", phone: "", estimate: "", estimateShown: false };
  }
})();
