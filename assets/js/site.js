/* Command Line Studios — small helper script (no libraries).
   Only does something on pages that contain the matching markup:
   1. App shelf      → .shelf-tile[data-app] switches between .showcase[data-app] blocks
   2. Gallery reel   → copies each .track's screenshots once so the sideways loop is seamless
   3. Device switch  → .seg[data-device] buttons swap the iPhone / iPad tracks
   4. Lightbox       → clicking a screenshot (.frame) opens it full screen
   See README.md → "How the pages work" for the markup each part expects. */
(function () {
  'use strict';

  /* 1. App shelf ---------------------------------------------------------- */
  var tiles = Array.prototype.slice.call(document.querySelectorAll('.shelf-tile[data-app]'));
  var shows = Array.prototype.slice.call(document.querySelectorAll('.showcase[data-app]'));

  function selectApp(id, updateHash) {
    var found = shows.some(function (s) { return s.getAttribute('data-app') === id; });
    if (!found) return false;
    shows.forEach(function (s) { s.hidden = s.getAttribute('data-app') !== id; });
    tiles.forEach(function (t) { t.setAttribute('aria-selected', t.getAttribute('data-app') === id ? 'true' : 'false'); });
    if (updateHash && history.replaceState) history.replaceState(null, '', '#' + id);
    return true;
  }
  if (tiles.length && shows.length) {
    tiles.forEach(function (t) {
      t.addEventListener('click', function () { selectApp(t.getAttribute('data-app'), true); });
    });
    // Deep link: categories/education.html#launchpad opens that app
    var start = (location.hash || '').slice(1);
    if (!selectApp(start, false)) selectApp(shows[0].getAttribute('data-app'), false);
  }

  /* 2. Gallery reel: duplicate the screenshots so the loop never shows a gap */
  document.querySelectorAll('.track').forEach(function (track) {
    Array.prototype.slice.call(track.children).forEach(function (frame) {
      var copy = frame.cloneNode(true);
      copy.setAttribute('data-clone', '');
      copy.setAttribute('aria-hidden', 'true');
      copy.setAttribute('tabindex', '-1');
      track.appendChild(copy);
    });
  });

  /* 3. iPhone / iPad switch (one per gallery) ------------------------------ */
  document.querySelectorAll('[data-gallery]').forEach(function (gallery) {
    var buttons = gallery.querySelectorAll('.seg[data-device]');
    var reel = document.getElementById(gallery.getAttribute('data-gallery'));
    if (!reel) return;
    buttons.forEach(function (b) {
      b.addEventListener('click', function () {
        var device = b.getAttribute('data-device');
        buttons.forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
        reel.querySelectorAll('.track').forEach(function (t) { t.hidden = !t.classList.contains(device); });
      });
    });
  });

  /* 4. Lightbox ------------------------------------------------------------ */
  var lb = document.getElementById('lightbox');
  if (!lb) return;
  var img = document.getElementById('lb-img');
  var count = document.getElementById('lb-count');
  var list = [], idx = 0, lastFocus = null;

  function show() {
    var el = list[idx];
    img.src = el.getAttribute('src');
    img.alt = el.getAttribute('alt');
    count.textContent = (idx + 1) + ' / ' + list.length;
  }
  function open(track, i) {
    list = Array.prototype.slice.call(track.querySelectorAll('.frame:not([data-clone]) img'));
    idx = i % list.length;
    lastFocus = document.activeElement;
    show();
    lb.hidden = false;
    document.body.style.overflow = 'hidden';
    document.getElementById('lb-close').focus();
  }
  function close() {
    lb.hidden = true;
    document.body.style.overflow = '';
    if (lastFocus) lastFocus.focus();
  }
  function step(d) { idx = (idx + d + list.length) % list.length; show(); }

  document.querySelectorAll('.track').forEach(function (track) {
    track.querySelectorAll('.frame').forEach(function (f, i) {
      f.addEventListener('click', function () { open(track, i); });
    });
  });
  document.getElementById('lb-close').addEventListener('click', close);
  document.getElementById('lb-prev').addEventListener('click', function () { step(-1); });
  document.getElementById('lb-next').addEventListener('click', function () { step(1); });
  lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
  document.addEventListener('keydown', function (e) {
    if (lb.hidden) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') step(-1);
    else if (e.key === 'ArrowRight') step(1);
  });
})();
