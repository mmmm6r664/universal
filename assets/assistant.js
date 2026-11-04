/* ==========================================================================
   Universal Relocations — Move Assistant
   Guided, chat-style lead capture with an instant estimate.
   Self-contained: injects its own styles, launcher, and panel on every page.
   ========================================================================== */
(function () {
  "use strict";

  /* ---------- Estimate ranges (PLACEHOLDER — swap for real rate card) ---------
     Rough door-to-door ranges in USD by move size. Clearly shown as an
     estimate in the chat. Replace these numbers with Universal's real rates. */
  var RATES = {
    international: {
      baggage:  [600, 1500],
      studio:   [1800, 3000],
      "1br":    [2500, 4500],
      "2br":    [4000, 7000],
      "3br":    [6000, 10000],
      "4br":    [9000, 15000]
    },
    domestic: {
      baggage:  [300, 800],
      studio:   [900, 1800],
      "1br":    [1500, 3000],
      "2br":    [2500, 4500],
      "3br":    [4000, 7000],
      "4br":    [6000, 10000]
    }
  };
  var SIZE_LABELS = {
    baggage: "Just baggage / a few boxes", studio: "Studio", "1br": "1 bedroom",
    "2br": "2 bedrooms", "3br": "3 bedrooms", "4br": "4+ bedrooms"
  };
  var fmt = function (n) { return "$" + n.toLocaleString("en-US"); };

  /* ---------------------------------- Styles -------------------------------- */
  var css = `
  .ura-launch{position:fixed;right:20px;bottom:88px;z-index:95;display:inline-flex;align-items:center;gap:10px;
    background:#f4a124;color:#fff;border:0;border-radius:999px;padding:13px 20px;font:600 15px/1 "Poppins",system-ui,sans-serif;
    cursor:pointer;box-shadow:0 10px 30px rgba(11,43,94,.28);transition:transform .2s,box-shadow .2s}
  .ura-launch:hover{transform:translateY(-2px);box-shadow:0 14px 36px rgba(11,43,94,.34)}
  .ura-launch svg{width:20px;height:20px;fill:#fff}
  .ura-launch .ura-dot{position:absolute;top:-4px;right:-4px;width:12px;height:12px;background:#e53e3e;border:2px solid #fff;border-radius:50%}
  @media(max-width:600px){.ura-launch span{display:none}.ura-launch{padding:14px;bottom:84px}}

  .ura-panel{position:fixed;right:20px;bottom:20px;z-index:96;width:390px;max-width:calc(100vw - 32px);height:600px;max-height:calc(100vh - 40px);
    background:#fff;border-radius:18px;box-shadow:0 30px 70px rgba(7,32,74,.34);display:none;flex-direction:column;overflow:hidden;
    font-family:"Poppins",system-ui,sans-serif;opacity:0;transform:translateY(16px) scale(.98);transition:opacity .22s,transform .22s}
  .ura-panel.ura-open{display:flex;opacity:1;transform:none}
  @media(max-width:600px){.ura-panel{right:0;bottom:0;width:100vw;max-width:100vw;height:100vh;max-height:100vh;border-radius:0}}

  .ura-head{background:linear-gradient(120deg,#07204a,#1f5fbf);color:#fff;padding:16px 18px;display:flex;align-items:center;gap:12px}
  .ura-head .ura-ava{width:40px;height:40px;border-radius:50%;background:#fff;display:grid;place-items:center;flex:none}
  .ura-head .ura-ava svg{width:24px;height:24px}
  .ura-head h4{margin:0;font-size:15px;font-weight:600;color:#fff;line-height:1.2}
  .ura-head p{margin:2px 0 0;font-size:12px;color:#c7d6ef}
  .ura-head .ura-x{margin-left:auto;background:rgba(255,255,255,.14);border:0;color:#fff;width:30px;height:30px;border-radius:8px;cursor:pointer;font-size:18px;line-height:1}
  .ura-head .ura-x:hover{background:rgba(255,255,255,.26)}

  .ura-body{flex:1;overflow-y:auto;padding:18px;background:#f6f8fc;display:flex;flex-direction:column;gap:12px}
  .ura-row{display:flex;gap:9px;align-items:flex-end;max-width:85%}
  .ura-row.ura-bot{align-self:flex-start}
  .ura-row.ura-user{align-self:flex-end;flex-direction:row-reverse}
  .ura-bubble{padding:11px 14px;border-radius:14px;font-size:14px;line-height:1.5;color:#1c2434;box-shadow:0 1px 3px rgba(11,43,94,.08)}
  .ura-bot .ura-bubble{background:#fff;border-bottom-left-radius:4px}
  .ura-user .ura-bubble{background:#1f5fbf;color:#fff;border-bottom-right-radius:4px}
  .ura-mini{width:28px;height:28px;border-radius:50%;background:linear-gradient(120deg,#07204a,#1f5fbf);flex:none;display:grid;place-items:center}
  .ura-mini svg{width:16px;height:16px;fill:#fff}

  .ura-typing{display:flex;gap:4px;padding:14px}
  .ura-typing span{width:7px;height:7px;border-radius:50%;background:#9fb0ce;animation:ura-b 1.2s infinite}
  .ura-typing span:nth-child(2){animation-delay:.2s}.ura-typing span:nth-child(3){animation-delay:.4s}
  @keyframes ura-b{0%,60%,100%{opacity:.3;transform:translateY(0)}30%{opacity:1;transform:translateY(-4px)}}

  .ura-quick{display:flex;flex-wrap:wrap;gap:8px;margin-top:2px}
  .ura-chip{background:#fff;border:1.5px solid #1f5fbf;color:#1f5fbf;border-radius:999px;padding:8px 14px;font:500 13px/1 inherit;cursor:pointer;transition:.15s}
  .ura-chip:hover{background:#1f5fbf;color:#fff}

  .ura-estimate{background:#fff;border:1px solid #e4e8f0;border-radius:14px;padding:16px;box-shadow:0 2px 10px rgba(11,43,94,.08)}
  .ura-estimate .ura-amt{font-size:24px;font-weight:800;color:#0b2b5e}
  .ura-estimate .ura-lbl{font-size:12px;color:#8a94a6;margin-top:2px}
  .ura-estimate small{display:block;margin-top:10px;font-size:11px;color:#8a94a6;line-height:1.5}

  .ura-foot{border-top:1px solid #e4e8f0;background:#fff;padding:12px}
  .ura-input{display:flex;gap:8px}
  .ura-input input{flex:1;border:1.5px solid #e4e8f0;border-radius:999px;padding:11px 15px;font:inherit;font-size:14px;outline:none}
  .ura-input input:focus{border-color:#1f5fbf}
  .ura-input button{background:#1f5fbf;border:0;border-radius:50%;width:42px;height:42px;flex:none;cursor:pointer;display:grid;place-items:center}
  .ura-input button:hover{background:#07204a}
  .ura-input button svg{width:18px;height:18px;fill:#fff}
  .ura-input button:disabled{opacity:.5;cursor:not-allowed}
  .ura-consent{display:flex;gap:8px;font-size:11px;color:#8a94a6;line-height:1.45;margin-top:10px}
  .ura-consent a{color:#1f5fbf}
  .ura-foot-note{text-align:center;font-size:10px;color:#b4bdca;margin-top:8px}
  `;
  var style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  var ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="#1f5fbf" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 14l1.5 6h15L21 14M5 14V7l7-3 7 3v7M9 9h6"/></svg>';
  var MINI = '<svg viewBox="0 0 24 24"><path d="M3 14l1.5 6h15L21 14M5 14V7l7-3 7 3v7M9 9h6" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';

  /* --------------------------------- Markup --------------------------------- */
  var launch = document.createElement("button");
  launch.className = "ura-launch";
  launch.setAttribute("aria-label", "Get an instant moving estimate");
  launch.innerHTML = '<span class="ura-dot"></span>' +
    '<svg viewBox="0 0 24 24"><path d="M12 3C6.5 3 2 6.6 2 11c0 2.2 1.1 4.2 2.9 5.6L4 21l4.7-2.3c1 .2 2.1.3 3.3.3 5.5 0 10-3.6 10-8s-4.5-8-10-8z"/></svg>' +
    '<span>Get an instant estimate</span>';

  var panel = document.createElement("div");
  panel.className = "ura-panel";
  panel.innerHTML =
    '<div class="ura-head">' +
      '<div class="ura-ava">' + ICON + '</div>' +
      '<div><h4>Universal Move Assistant</h4><p>Typically replies instantly</p></div>' +
      '<button class="ura-x" aria-label="Close">&times;</button>' +
    '</div>' +
    '<div class="ura-body" id="ura-body"></div>' +
    '<div class="ura-foot" id="ura-foot"></div>';

  document.body.appendChild(launch);
  document.body.appendChild(panel);

  var body = panel.querySelector("#ura-body");
  var foot = panel.querySelector("#ura-foot");
  var closeBtn = panel.querySelector(".ura-x");

  /* --------------------------------- State ---------------------------------- */
  var data = { moveType: "", route: "", from: "", to: "", size: "", date: "", name: "", email: "", phone: "", estimate: "" };
  var started = false;

  /* ------------------------------- Helpers ---------------------------------- */
  function scroll() { body.scrollTop = body.scrollHeight; }

  function botSay(html, cb) {
    var t = document.createElement("div");
    t.className = "ura-row ura-bot";
    t.innerHTML = '<div class="ura-mini">' + MINI + '</div><div class="ura-bubble"><div class="ura-typing"><span></span><span></span><span></span></div></div>';
    body.appendChild(t); scroll();
    setTimeout(function () {
      t.querySelector(".ura-bubble").innerHTML = html;
      scroll();
      if (cb) cb(t);
    }, 650);
  }

  function userSay(text) {
    var u = document.createElement("div");
    u.className = "ura-row ura-user";
    u.innerHTML = '<div class="ura-bubble"></div>';
    u.querySelector(".ura-bubble").textContent = text;
    body.appendChild(u); scroll();
  }

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
  }

  function askText(placeholder, type, onSubmit) {
    foot.innerHTML =
      '<form class="ura-input"><input type="' + (type || "text") + '" placeholder="' + placeholder + '" autocomplete="off">' +
      '<button type="submit" aria-label="Send"><svg viewBox="0 0 24 24"><path d="M3 11l18-8-8 18-2-7-8-3z"/></svg></button></form>';
    var form = foot.querySelector("form");
    var input = form.querySelector("input");
    input.focus();
    form.onsubmit = function (e) {
      e.preventDefault();
      var v = input.value.trim();
      if (!v) return;
      userSay(v); foot.innerHTML = ""; onSubmit(v);
    };
  }

  function clearFoot() { foot.innerHTML = '<div class="ura-foot-note">Powered by Universal Relocations</div>'; }

  /* ------------------------------ Conversation ------------------------------ */
  function start() {
    if (started) return; started = true;
    clearFoot();
    botSay("Hi! 👋 I'm the Universal Move Assistant. I'll ask a few quick questions and give you an instant ballpark estimate — then our team can follow up with an exact quote.", function () {
      botSay("First up — what kind of move are you planning?", function () {
        chips([
          { label: "International move", value: "international" },
          { label: "Interstate / domestic move", value: "interstate" },
          { label: "Ship baggage / boxes", value: "baggage" },
          { label: "Something else", value: "other" }
        ], function (v, label) {
          data.moveType = label;
          data.route = (v === "interstate") ? "domestic" : "international";
          askFrom();
        });
      });
    });
  }

  function askFrom() {
    botSay("Got it. Where are you moving <b>from</b>? (city &amp; country)", function () {
      askText("e.g. New Jersey, USA", "text", function (v) { data.from = v; askTo(); });
    });
  }

  function askTo() {
    botSay("And where are you moving <b>to</b>?", function () {
      askText("e.g. Chennai, India", "text", function (v) { data.to = v; askSize(); });
    });
  }

  function askSize() {
    botSay("How much are you moving?", function () {
      chips([
        { label: SIZE_LABELS.baggage, value: "baggage" },
        { label: SIZE_LABELS.studio, value: "studio" },
        { label: SIZE_LABELS["1br"], value: "1br" },
        { label: SIZE_LABELS["2br"], value: "2br" },
        { label: SIZE_LABELS["3br"], value: "3br" },
        { label: SIZE_LABELS["4br"], value: "4br" }
      ], function (v, label) { data.size = label; askDate(); });
    });
  }

  function askDate() {
    botSay("When are you hoping to move?", function () {
      chips([
        { label: "As soon as possible", value: "ASAP" },
        { label: "In 1–3 months", value: "1-3 months" },
        { label: "In 3–6 months", value: "3-6 months" },
        { label: "Just exploring", value: "Flexible" }
      ], function (v, label) { data.date = label; showEstimate(); });
    });
  }

  function showEstimate() {
    botSay("Thanks! Crunching the numbers for your move…", function () {
      var sizeKey = Object.keys(SIZE_LABELS).find(function (k) { return SIZE_LABELS[k] === data.size; }) || "1br";
      var table = RATES[data.route] || RATES.international;
      var range = table[sizeKey] || table["1br"];
      data.estimate = fmt(range[0]) + " – " + fmt(range[1]);
      var est =
        '<div class="ura-estimate"><div class="ura-amt">' + data.estimate + '</div>' +
        '<div class="ura-lbl">Estimated ' + (data.route === "domestic" ? "interstate" : "international") + ' move · ' + data.from + ' → ' + data.to + '</div>' +
        '<small>Ballpark only, based on a ' + data.size.toLowerCase() + ' move. Your exact quote depends on volume, access and services — our team will confirm it.</small></div>';
      botSay(est, function () {
        botSay("Want us to prepare a <b>detailed, no-obligation quote</b> and lock in your estimate? Just drop your details 👇", function () {
          askName();
        });
      });
    });
  }

  function askName() {
    botSay("What's your name?", function () {
      askText("Your name", "text", function (v) { data.name = v; askEmail(); });
    });
  }
  function askEmail() {
    botSay("Nice to meet you, " + data.name.split(" ")[0] + "! What's the best email for your quote?", function () {
      askText("you@email.com", "email", function (v) {
        if (!/.+@.+\..+/.test(v)) { botSay("Hmm, that doesn't look like an email — mind trying again?", function () { askEmail(); }); return; }
        data.email = v; askPhone();
      });
    });
  }
  function askPhone() {
    botSay("And a phone number our move manager can reach you on?", function () {
      askText("Phone number", "tel", function (v) { data.phone = v; submitLead(); });
    });
  }

  function submitLead() {
    botSay("Perfect — submitting your request…", function () {
      fetch("/api/lead", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json(); }).catch(function () { return { ok: false }; })
        .then(function () {
          botSay("✅ All set, " + data.name.split(" ")[0] + "! Your request is in and a Universal move manager will reach out shortly with your detailed quote.<br><br>Need us sooner? Call <b>1-888-323-7356</b> or <a href='https://portal.universalrelocations.com/moving-calculator/' target='_blank' style='color:#1f5fbf'>use the full moving calculator</a>.", function () {
            clearFoot();
          });
        });
    });
  }

  /* -------------------------------- Open/close ------------------------------ */
  function open() { panel.classList.add("ura-open"); launch.style.display = "none"; start(); }
  function close() { panel.classList.remove("ura-open"); launch.style.display = ""; }
  launch.onclick = open;
  closeBtn.onclick = close;

  // Let any element with [data-open-assistant] open the chat
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-open-assistant]");
    if (t) { e.preventDefault(); open(); }
  });
})();
