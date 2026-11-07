/* Universal Relocations — native Moving Calculator (volume + weight estimator)
   Rebuilt from the portal calculator: room tabs, item catalog with +/- steppers,
   live cubic-feet + weight totals, move-detail fields and lead submit. */
(function () {
  var root = document.getElementById('calc-root');
  if (!root) return;

  // ---- Item catalog: [name, cubic feet, pounds] ----
  var BEDROOM = [
    ["King bed", 70, 180], ["Queen bed", 55, 150], ["Double / Full bed", 45, 120],
    ["Single / Twin bed", 30, 80], ["Mattress (Q/K)", 28, 70], ["Bed frame / headboard", 20, 90],
    ["Wardrobe / Almirah", 50, 200], ["Dresser", 30, 120], ["Chest of drawers", 25, 100],
    ["Nightstand", 6, 30], ["Dressing table / vanity", 20, 80], ["Mirror", 4, 20],
    ["Blanket box / trunk", 10, 40], ["Bedroom chair", 10, 35]
  ];
  var CATALOG = {
    "Boxes": [
      ["Small box (books/files)", 1.5, 30], ["Medium box", 3.0, 40],
      ["Large box", 4.5, 50], ["Extra-large box", 6.0, 60],
      ["Wardrobe box", 10.0, 60], ["Dish pack / crockery box", 5.2, 55],
      ["Suitcase (large)", 4.0, 50], ["Suitcase (medium)", 2.5, 35]
    ],
    "Living Room / Foyer": [
      ["Sofa — 3 seat", 50, 160], ["Sofa — 2 seat", 35, 110], ["Sectional sofa", 70, 250],
      ["Armchair", 25, 70], ["Recliner", 30, 90], ["Coffee table", 10, 40],
      ["Side / end table", 5, 25], ["TV stand / console", 18, 80], ["Bookshelf", 20, 70],
      ["Display cabinet", 30, 120], ["Ottoman / pouffe", 8, 25], ["Floor lamp", 4, 15],
      ["Area rug (rolled)", 8, 35], ["Wall art / mirror", 3, 15]
    ],
    "Bed Room 1": BEDROOM, "Bed Room 2": BEDROOM, "Bed Room 3": BEDROOM, "Bed Room 4": BEDROOM,
    "Dining Room": [
      ["Dining table", 30, 120], ["Dining chair", 6, 20], ["Buffet / sideboard", 35, 150],
      ["China cabinet", 40, 160], ["Bar stool", 6, 18], ["Serving cart", 12, 45]
    ],
    "Kitchen": [
      ["Refrigerator (double door)", 60, 280], ["Refrigerator (single door)", 35, 160],
      ["Washing machine", 25, 170], ["Clothes dryer", 25, 125], ["Dishwasher", 25, 150],
      ["Gas range / stove", 18, 120], ["Microwave", 3, 35], ["Kitchen trolley", 12, 50],
      ["Cookware box", 3, 40], ["Small-appliance box", 3, 30]
    ],
    "Garage / Storage": [
      ["Bicycle", 12, 30], ["Tool chest", 15, 90], ["Workbench", 25, 120],
      ["Storage shelf / rack", 20, 60], ["Ladder", 8, 30], ["Lawn mower", 20, 80],
      ["Treadmill", 30, 220], ["Exercise bike", 15, 90], ["Box of tools", 4, 50]
    ],
    "Outdoor / Patio": [
      ["Patio table", 20, 70], ["Patio chair", 8, 25], ["BBQ grill", 20, 90],
      ["Garden bench", 18, 70], ["Sun lounger", 12, 40], ["Large planter", 6, 40],
      ["Parasol / umbrella", 6, 20]
    ],
    "Electronics": [
      ['TV up to 43"', 6, 30], ['TV 44–60"', 10, 45], ['TV 65"+', 14, 60],
      ["Desktop computer", 4, 35], ["Printer", 3, 25], ["Soundbar / speaker", 3, 15],
      ["Home theatre system", 6, 40], ["Gaming console", 1, 10]
    ],
    "Toiletries": [
      ["Toiletries box", 1.5, 20], ["Linen box", 3, 25], ["Towels box", 3, 25]
    ],
    "Home Office": [
      ["Office desk", 25, 110], ["Office chair", 12, 40], ["Filing cabinet", 12, 90],
      ["Bookcase", 20, 70], ["Document box", 1.5, 35], ["Small safe", 6, 120]
    ],
    "Pooja Room": [
      ["Pooja mandir / temple unit", 20, 90], ["Pooja box", 1.5, 25], ["Idol / statue (crated)", 4, 40]
    ],
    "Crating Items": [
      ["Marble / glass table top (crated)", 15, 150], ["Artwork / painting (crated)", 6, 40],
      ["Chandelier (crated)", 10, 50], ["Large mirror (crated)", 8, 45],
      ["Upright piano (crated)", 70, 400], ["Statue (crated)", 10, 120]
    ],
    "Customize Items": [] // user-added
  };
  var ROOMS = Object.keys(CATALOG);
  var counts = {};            // key "room|idx" -> qty
  var custom = [];            // user-added items {n,cft,lbs}

  // ---- Build DOM ----
  root.innerHTML =
    '<div class="calc">' +
      '<div class="calc-totals" id="calc-totals">' +
        '<div class="ct"><span class="n" id="ct-vol">0.00</span><span class="l">Cubic Feet</span></div>' +
        '<div class="ct"><span class="n" id="ct-wt">0</span><span class="l">Estimated lbs</span></div>' +
        '<div class="ct"><span class="n" id="ct-items">0</span><span class="l">Items</span></div>' +
      '</div>' +
      '<div class="calc-main">' +
        '<aside class="calc-tabs" id="calc-tabs"></aside>' +
        '<div class="calc-panel"><div class="calc-items" id="calc-items"></div></div>' +
      '</div>' +
      '<form class="calc-form" id="calc-form">' +
        '<h3>Your move details</h3>' +
        '<div class="cf-grid">' +
          '<label>First name*<input name="first" required></label>' +
          '<label>Last name*<input name="last" required></label>' +
          '<label>Email*<input type="email" name="email" required></label>' +
          '<label>Phone*<input type="tel" name="phone" required></label>' +
          '<label>Moving from*<input name="from" required></label>' +
          '<label>Moving to*<input name="to" required></label>' +
          '<label>Move size<select name="size"><option>Pooja Room</option><option>Baggage</option><option>Studio</option><option selected>1 Bedroom</option><option>2 Bedroom</option><option>3 Bedroom</option><option>4 Bedroom</option><option>Family Home</option></select></label>' +
          '<label>Estimated pickup date<input type="date" name="date"></label>' +
          '<label>Origin floor<select name="ofloor">' + floorOpts() + '</select></label>' +
          '<label>Destination floor<select name="dfloor">' + floorOpts() + '</select></label>' +
          '<label class="full">Delivery / pickup instructions<textarea name="notes" rows="2"></textarea></label>' +
        '</div>' +
        '<button type="submit" class="btn btn-primary">Get my estimate &amp; quote</button>' +
        '<p class="cf-note">This volume is an estimate for unpacked items (Cft = L × W × H in inches ÷ 1728). Your final quote is based on the actual packed volume, which is often lower thanks to our professional packing.</p>' +
      '</form>' +
    '</div>';

  function floorOpts() {
    var o = ['Ground floor', '1st floor', '2nd floor', '3rd floor', '4th floor', '5th floor',
             '6th–10th floor', 'Above 10th floor'];
    return o.map(function (x) { return '<option>' + x + '</option>'; }).join('');
  }

  var tabsEl = document.getElementById('calc-tabs');
  var itemsEl = document.getElementById('calc-items');
  var active = ROOMS[0];

  tabsEl.innerHTML = ROOMS.map(function (r) {
    return '<button type="button" class="calc-tab" data-room="' + r + '">' + r +
      '<span class="badge" data-badge="' + r + '"></span></button>';
  }).join('');
  tabsEl.addEventListener('click', function (e) {
    var b = e.target.closest('.calc-tab'); if (!b) return;
    active = b.getAttribute('data-room'); renderItems(); markTabs();
  });

  function key(room, i) { return room + '|' + i; }

  function renderItems() {
    var list = CATALOG[active];
    var html = '';
    if (active === 'Customize Items') {
      html += '<div class="add-custom">' +
        '<input id="cu-name" placeholder="Item name"><input id="cu-cft" type="number" min="0" step="0.5" placeholder="Cu ft">' +
        '<button type="button" class="btn btn-ghost" id="cu-add">Add item</button></div>';
      custom.forEach(function (c, i) { html += row('Customize Items', i, c[0], c[1], c[2], true); });
      if (!custom.length) html += '<p class="muted" style="padding:8px 2px">Add any item we didn\'t list, with its approximate size.</p>';
    } else {
      list.forEach(function (it, i) { html += row(active, i, it[0], it[1], it[2], false); });
    }
    itemsEl.innerHTML = html;
    if (active === 'Customize Items') {
      document.getElementById('cu-add').onclick = function () {
        var n = document.getElementById('cu-name').value.trim();
        var cft = parseFloat(document.getElementById('cu-cft').value) || 0;
        if (!n || cft <= 0) return;
        custom.push([n, cft, Math.round(cft * 7)]);
        counts[key('Customize Items', custom.length - 1)] = 1;
        renderItems(); update();
      };
    }
  }

  function row(room, i, name, cft, lbs, isCustom) {
    var q = counts[key(room, i)] || 0;
    return '<div class="calc-row' + (q ? ' on' : '') + '" data-k="' + room + '|' + i + '">' +
      '<div class="ci"><span class="nm">' + name + '</span><span class="sz">' + cft + ' cu ft · ' + lbs + ' lbs</span></div>' +
      '<div class="stp"><button type="button" class="mn" aria-label="less">−</button>' +
      '<span class="q">' + q + '</span>' +
      '<button type="button" class="pl" aria-label="more">+</button></div></div>';
  }

  itemsEl.addEventListener('click', function (e) {
    var row = e.target.closest('.calc-row'); if (!row) return;
    var k = row.getAttribute('data-k');
    if (e.target.classList.contains('pl')) counts[k] = (counts[k] || 0) + 1;
    else if (e.target.classList.contains('mn')) counts[k] = Math.max(0, (counts[k] || 0) - 1);
    else return;
    row.querySelector('.q').textContent = counts[k];
    row.classList.toggle('on', counts[k] > 0);
    update(); markTabs();
  });

  function itemData(room, i) {
    if (room === 'Customize Items') return custom[i];
    return CATALOG[room][i];
  }

  function update() {
    var vol = 0, wt = 0, items = 0;
    Object.keys(counts).forEach(function (k) {
      var q = counts[k]; if (!q) return;
      var p = k.split('|'); var d = itemData(p[0], parseInt(p[1], 10));
      if (!d) return;
      vol += d[1] * q; wt += d[2] * q; items += q;
    });
    document.getElementById('ct-vol').textContent = vol.toFixed(2);
    document.getElementById('ct-wt').textContent = Math.round(wt).toLocaleString();
    document.getElementById('ct-items').textContent = items;
  }

  function markTabs() {
    ROOMS.forEach(function (r) {
      var n = 0;
      Object.keys(counts).forEach(function (k) { if (k.indexOf(r + '|') === 0) n += counts[k]; });
      var b = tabsEl.querySelector('[data-badge="' + r + '"]');
      if (b) { b.textContent = n || ''; b.style.display = n ? 'inline-flex' : 'none'; }
      var tab = tabsEl.querySelector('[data-room="' + r + '"]');
      if (tab) tab.classList.toggle('active', r === active);
    });
  }

  // ---- Submit -> lead ----
  document.getElementById('calc-form').addEventListener('submit', function (e) {
    e.preventDefault();
    var f = e.target, btn = f.querySelector('button[type=submit]');
    var items = [];
    Object.keys(counts).forEach(function (k) {
      var q = counts[k]; if (!q) return;
      var p = k.split('|'); var d = itemData(p[0], parseInt(p[1], 10));
      if (d) items.push({ room: p[0], item: d[0], qty: q, cft: d[1] });
    });
    var payload = {
      source: 'moving-calculator',
      name: (f.first.value + ' ' + f.last.value).trim(),
      email: f.email.value, phone: f.phone.value,
      from: f.from.value, to: f.to.value, size: f.size.value, date: f.date.value,
      originFloor: f.ofloor.value, destFloor: f.dfloor.value, notes: f.notes.value,
      volumeCft: document.getElementById('ct-vol').textContent,
      weightLbs: document.getElementById('ct-wt').textContent,
      items: items
    };
    btn.disabled = true; var orig = btn.textContent; btn.textContent = 'Sending…';
    fetch('/api/lead', { method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload) })
      .catch(function () {})
      .finally(function () {
        root.querySelector('.calc').innerHTML =
          '<div class="calc-done"><h2>Thank you, ' + (f.first.value || 'there') + '!</h2>' +
          '<p>Your estimated volume is <b>' + payload.volumeCft + ' cu ft</b> (~' + payload.weightLbs +
          ' lbs). One of our move consultants will review your list and send a firm, competitive quote shortly.</p>' +
          '<p><a class="btn btn-primary" href="/">Back to home</a> ' +
          '<a class="btn btn-ghost" href="/contact-us/" style="margin-left:8px">Contact us</a></p></div>';
        window.scrollTo({ top: root.offsetTop - 80, behavior: 'smooth' });
      });
  });

  renderItems(); markTabs(); update();
})();
