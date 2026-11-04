// Universal Relocations — site scripts

// Mobile navigation toggle
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.querySelector('.nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      menu.classList.toggle('open');
    });
    // On mobile, let parent links with dropdowns expand instead of navigating
    menu.querySelectorAll('.has-dropdown > a').forEach(function (a) {
      a.addEventListener('click', function (e) {
        if (window.innerWidth <= 760) {
          e.preventDefault();
          a.parentElement.classList.toggle('expanded');
        }
      });
    });
  }
})();

// Animated counters for the stats band
(function () {
  var stats = document.querySelectorAll('[data-count]');
  if (!stats.length) return;
  var run = function (el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var dur = 1600, start = 0, t0 = null;
    var step = function (ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var val = (target * (0.5 - Math.cos(Math.PI * p) / 2));
      el.textContent = (target % 1 === 0 ? Math.round(val) : val.toFixed(0)) + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { run(en.target); io.unobserve(en.target); }
    });
  }, { threshold: 0.5 });
  stats.forEach(function (s) { io.observe(s); });
})();

// Quote form — front-end only (wire to your endpoint / Formspree / API route)
(function () {
  var form = document.getElementById('quote-form');
  if (!form) return;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var btn = form.querySelector('button[type="submit"]');
    var original = btn.textContent;
    btn.textContent = 'Thank you! We will be in touch.';
    btn.disabled = true;
    setTimeout(function () { btn.textContent = original; btn.disabled = false; form.reset(); }, 4000);
  });
})();

// Route finder — navigate to the dedicated route page
(function () {
  var form = document.getElementById('route-form');
  if (!form) return;
  var from = document.getElementById('route-from');
  var to = document.getElementById('route-to');
  var err = document.getElementById('route-error');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var f = from.value, t = to.value;
    if (!f || !t || f === t) { if (err) err.hidden = false; return; }
    if (err) err.hidden = true;
    location.href = '/moving/' + f + '-to-' + t + '/';
  });
})();

// Hero rotating typewriter headline
(function () {
  var el = document.getElementById('hero-rotate');
  if (!el) return;
  var t = el.querySelector('.hr-text');
  var msgs = [
    "Hello,",
    "Welcome to Universal Relocations",
    "One of the largest international movers",
    "28+ years of experience",
    "We're here to help with your international move"
  ];
  var mi = 0, ci = 0, del = false;
  function tick() {
    var full = msgs[mi];
    if (!del) {
      ci++; t.textContent = full.slice(0, ci);
      if (ci >= full.length) { del = true; return setTimeout(tick, 1800); }
      setTimeout(tick, 58);
    } else {
      ci--; t.textContent = full.slice(0, ci);
      if (ci <= 0) { del = false; mi = (mi + 1) % msgs.length; return setTimeout(tick, 320); }
      setTimeout(tick, 28);
    }
  }
  t.textContent = ""; tick();
})();

// Scroll-reveal transitions (applied automatically, respects reduced-motion)
(function () {
  if (!('IntersectionObserver' in window)) return;
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var sel = '.feature, .svc, .hub-card, .review, .info-card, .promise .p, .stat, ' +
            '.route-finder, .logos-slider, .section-title, .section-intro, .eyebrow, ' +
            '.prose h2, .office-table, .country-grid, .related-routes, .ura-estimate';
  var els = Array.prototype.slice.call(document.querySelectorAll(sel)).filter(function (el) {
    return !el.closest('.hello-hero');
  });
  var counts = new Map();
  els.forEach(function (el) {
    el.classList.add('reveal');
    var p = el.parentElement;
    var n = counts.get(p) || 0; counts.set(p, n + 1);
    el.style.transitionDelay = Math.min(n * 60, 360) + 'ms';
  });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add('in-view'); io.unobserve(en.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -7% 0px' });
  els.forEach(function (el) { io.observe(el); });
})();
