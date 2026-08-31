/* iRemedy cookie consent (C-09).
   Google Consent Mode v2 defaults to denied; analytics/marketing tags fire only after acceptance.
   The consent choice is stored for 12 months and can be changed from the footer "Cookie settings" link. */
(function () {
  'use strict';

  var KEY = 'iremedy_cookie_consent';
  var MAX_AGE_DAYS = 365;

  function read() {
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw) return null;
      var v = JSON.parse(raw);
      if (!v || !v.ts || (Date.now() - v.ts) / 86400000 > MAX_AGE_DAYS) return null;
      return v;
    } catch (e) {
      return null;
    }
  }

  function save(status) {
    try {
      localStorage.setItem(KEY, JSON.stringify({ status: status, ts: Date.now() }));
    } catch (e) {}
  }

  function apply(status) {
    var granted = status === 'accepted' ? 'granted' : 'denied';
    if (typeof window.gtag === 'function') {
      window.gtag('consent', 'update', {
        analytics_storage: granted,
        ad_storage: granted,
        ad_user_data: granted,
        ad_personalization: granted
      });
    }
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: 'cookie_consent_' + status });
  }

  function globalPrivacyControl() {
    return navigator.globalPrivacyControl === true;
  }

  var STYLE =
    '#ir-cookie{position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#0C2340;color:#F2EDE4;' +
    'padding:1.1rem 6vw;display:flex;gap:1.25rem;align-items:center;justify-content:space-between;' +
    'flex-wrap:wrap;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;' +
    'font-size:0.875rem;line-height:1.6;box-shadow:0 -2px 18px rgba(0,0,0,0.25)}' +
    '#ir-cookie p{margin:0;max-width:70ch;color:rgba(242,237,228,0.92)}' +
    '#ir-cookie a{color:#E0577A}' +
    '#ir-cookie .ir-cc-actions{display:flex;gap:0.6rem;flex-wrap:wrap}' +
    '#ir-cookie button{font-family:"IBM Plex Mono",monospace;font-size:0.78rem;font-weight:600;' +
    'letter-spacing:0.12em;text-transform:uppercase;padding:10px 20px;cursor:pointer;border:1px solid #B31942;' +
    'transition:all .18s}' +
    '#ir-cookie .ir-cc-accept{background:#B31942;color:#fff}' +
    '#ir-cookie .ir-cc-accept:hover{background:#8E142F;border-color:#8E142F}' +
    '#ir-cookie .ir-cc-reject{background:transparent;color:#E0577A;border-color:#E0577A}' +
    '#ir-cookie .ir-cc-reject:hover{background:#B31942;border-color:#B31942;color:#fff}';

  function banner() {
    if (document.getElementById('ir-cookie')) return;
    var s = document.createElement('style');
    s.textContent = STYLE;
    document.head.appendChild(s);

    var el = document.createElement('div');
    el.id = 'ir-cookie';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-live', 'polite');
    el.setAttribute('aria-label', 'Cookie consent');
    el.innerHTML =
      '<p>We use strictly necessary cookies to run iremedy.com, and analytics cookies to understand how the ' +
      'site is used. Analytics cookies are set only if you accept. See our ' +
      '<a href="/privacy-policy">Privacy Policy</a>.</p>' +
      '<div class="ir-cc-actions">' +
      '<button type="button" class="ir-cc-reject">Reject non-essential</button>' +
      '<button type="button" class="ir-cc-accept">Accept all</button>' +
      '</div>';
    document.body.appendChild(el);

    function choose(status) {
      save(status);
      apply(status);
      el.remove();
    }
    el.querySelector('.ir-cc-accept').addEventListener('click', function () { choose('accepted'); });
    el.querySelector('.ir-cc-reject').addEventListener('click', function () { choose('rejected'); });
  }

  window.iremedyCookieSettings = function () {
    try { localStorage.removeItem(KEY); } catch (e) {}
    banner();
    return false;
  };

  function init() {
    var stored = read();
    if (stored) { apply(stored.status); return; }
    if (globalPrivacyControl()) { save('rejected'); apply('rejected'); return; }
    banner();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
