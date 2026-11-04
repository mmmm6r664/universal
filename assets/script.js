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
