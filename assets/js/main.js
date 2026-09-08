/* Portfolio behaviour: nav, reveals, counters, gallery, lightbox, filters.
   No dependencies. Everything degrades to a readable page without JS. */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- nav ---------- */
  var nav = document.querySelector('.nav');
  if (nav) {
    var onScroll = function () { nav.classList.toggle('stuck', window.scrollY > 12); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  var burger = document.querySelector('.burger');
  var links = document.querySelector('.nav-links');
  if (burger && links) {
    burger.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      burger.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', String(open));
    });
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        links.classList.remove('open');
        burger.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---------- reveal on scroll ----------
     Deliberately rect-based rather than IntersectionObserver: IO can skip
     elements entirely during a fast or programmatic scroll, and the failure
     mode there is invisible content. This check is cheap, runs at most once
     per frame, and unhooks itself once everything has been shown. */
  var pending = Array.prototype.slice.call(document.querySelectorAll('[data-reveal]'));

  if (reduced) {
    pending.forEach(function (el) { el.classList.add('in'); });
    pending = [];
  } else {
    // Stagger siblings so a grid arrives as a wave rather than all at once.
    var groups = {};
    pending.forEach(function (el) {
      var key = el.dataset.revealGroup;
      if (!key) return;
      groups[key] = groups[key] || 0;
      el.style.setProperty('--d', Math.min(groups[key] * 65, 420) + 'ms');
      groups[key]++;
    });

    var ticking = false;
    var sweep = function () {
      ticking = false;
      var limit = window.innerHeight * 0.94;
      pending = pending.filter(function (el) {
        if (el.getBoundingClientRect().top > limit) return true;
        el.classList.add('in');
        return false;
      });
      if (!pending.length) {
        window.removeEventListener('scroll', request);
        window.removeEventListener('resize', request);
      }
    };
    var request = function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(sweep);
    };

    window.addEventListener('scroll', request, { passive: true });
    window.addEventListener('resize', request);
    window.addEventListener('load', request);
    sweep();
  }

  /* ---------- number counters ---------- */
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    var run = function (el) {
      var target = parseFloat(el.dataset.count);
      var decimals = (el.dataset.count.split('.')[1] || '').length;
      if (reduced) { el.textContent = target.toFixed(decimals); return; }
      var started = null, dur = 1400;
      var step = function (now) {
        if (started === null) started = now;
        var p = Math.min((now - started) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = (target * eased).toFixed(decimals);
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    if ('IntersectionObserver' in window) {
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          run(e.target);
          cio.unobserve(e.target);
        });
      }, { threshold: 0.5 });
      counters.forEach(function (el) { cio.observe(el); });
    } else {
      counters.forEach(run);
    }
  }

  /* ---------- per-card gallery strip ---------- */
  document.querySelectorAll('.proj').forEach(function (card) {
    var main = card.querySelector('.proj-shot img');
    var shot = card.querySelector('.proj-shot');
    var thumbs = card.querySelectorAll('.proj-strip button');
    if (!main || !thumbs.length) return;

    thumbs.forEach(function (btn) {
      var swap = function () {
        var src = btn.dataset.src;
        if (!src || main.getAttribute('src') === src) return;
        main.style.opacity = '0';
        window.setTimeout(function () {
          main.src = src;
          main.alt = btn.dataset.alt || main.alt;
          main.style.opacity = '1';
          shot.dataset.index = btn.dataset.index;
        }, reduced ? 0 : 130);
        thumbs.forEach(function (t) { t.setAttribute('aria-current', String(t === btn)); });
      };
      btn.addEventListener('mouseenter', swap);
      btn.addEventListener('focus', swap);
      btn.addEventListener('click', function (e) { e.preventDefault(); swap(); });
    });
    main.style.transition = 'opacity .13s linear, transform .7s cubic-bezier(.16,1,.3,1)';
  });

  /* ---------- lightbox ---------- */
  var lb = document.getElementById('lightbox');
  if (lb) {
    var lbImg = lb.querySelector('img');
    var lbCap = lb.querySelector('figcaption');
    var set = [];
    var at = 0;
    var lastFocus = null;

    var show = function (i) {
      at = (i + set.length) % set.length;
      lbImg.src = set[at].src;
      lbImg.alt = set[at].alt;
      lbCap.textContent = set[at].cap + '  ·  ' + (at + 1) + ' / ' + set.length;
    };
    var open = function (shots, i, title) {
      set = shots.map(function (s) { return { src: s.src, alt: s.alt, cap: title }; });
      lb.classList.add('open');
      document.body.style.overflow = 'hidden';
      lastFocus = document.activeElement;
      show(i);
      lb.querySelector('.lb-close').focus();
    };
    var close = function () {
      lb.classList.remove('open');
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    };

    document.querySelectorAll('.proj').forEach(function (card) {
      var shotBox = card.querySelector('.proj-shot');
      if (!shotBox) return;
      var title = (card.querySelector('h3') || {}).textContent || '';
      var shots = [];
      var mainImg = shotBox.querySelector('img');
      var thumbs = card.querySelectorAll('.proj-strip button');
      if (thumbs.length) {
        thumbs.forEach(function (t) { shots.push({ src: t.dataset.src, alt: t.dataset.alt || title }); });
      } else if (mainImg) {
        shots.push({ src: mainImg.src, alt: mainImg.alt });
      }
      if (!shots.length) return;

      shotBox.addEventListener('click', function () {
        open(shots, parseInt(shotBox.dataset.index || '0', 10), title.trim());
      });
      shotBox.setAttribute('role', 'button');
      shotBox.setAttribute('tabindex', '0');
      shotBox.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          open(shots, parseInt(shotBox.dataset.index || '0', 10), title.trim());
        }
      });
    });

    lb.querySelector('.lb-close').addEventListener('click', close);
    // `set` is empty on pages with no project cards - the about page binds its
    // own handlers to the same buttons, so bail out instead of indexing nothing.
    lb.querySelector('.prev').addEventListener('click', function () { if (set.length) show(at - 1); });
    lb.querySelector('.next').addEventListener('click', function () { if (set.length) show(at + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (!set.length) return;
      if (e.key === 'ArrowLeft') show(at - 1);
      if (e.key === 'ArrowRight') show(at + 1);
    });
  }

  /* ---------- filters ---------- */
  var filterBar = document.querySelector('.filters');
  if (filterBar) {
    var cards = Array.prototype.slice.call(document.querySelectorAll('.proj[data-tags]'));
    filterBar.addEventListener('click', function (e) {
      var btn = e.target.closest('button');
      if (!btn) return;
      var want = btn.dataset.filter;
      filterBar.querySelectorAll('button').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b === btn));
      });
      cards.forEach(function (card) {
        var match = want === 'all' || card.dataset.tags.split(' ').indexOf(want) !== -1;
        card.classList.toggle('hidden', !match);
      });
    });
  }

  /* ---------- contact dialog ----------
     The page is static, so the message goes through FormSubmit, which relays
     it to the inbox. Everything still degrades: if the request fails we hand
     the visitor a mailto link with their text already in it. */
  var modal = document.getElementById('contact');
  if (modal) {
    var form = modal.querySelector('form');
    var status = modal.querySelector('.form-status');
    var submit = modal.querySelector('button[type=submit]');
    var opener = null;

    var openModal = function (e) {
      if (e) e.preventDefault();
      opener = document.activeElement;
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
      window.setTimeout(function () { var f = form.querySelector('input'); if (f) f.focus(); }, 90);
    };
    var closeModal = function () {
      modal.classList.remove('open');
      document.body.style.overflow = '';
      if (opener && opener.focus) opener.focus();
    };

    document.querySelectorAll('[data-contact]').forEach(function (el) {
      el.addEventListener('click', openModal);
    });
    modal.querySelector('.modal-close').addEventListener('click', closeModal);
    modal.addEventListener('click', function (e) { if (e.target === modal) closeModal(); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal.classList.contains('open')) closeModal();
    });

    // keep focus inside the dialog while it is open
    modal.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab') return;
      var f = modal.querySelectorAll('button, input, textarea, a[href]');
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = {
        name: form.name.value.trim(),
        email: form.email.value.trim(),
        subject: form.subject.value.trim() || 'Message from jotunlegion.github.io',
        message: form.message.value.trim(),
        _template: 'table',
        _captcha: 'false'
      };
      if (!data.name || !data.email || !data.message) {
        status.className = 'form-status err';
        status.textContent = 'Please fill in your name, email and message.';
        return;
      }
      status.className = 'form-status';
      status.textContent = 'Sending…';
      submit.setAttribute('aria-busy', 'true');

      fetch(form.action, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(data)
      })
        .then(function (r) { return r.ok ? r.json() : Promise.reject(new Error('HTTP ' + r.status)); })
        .then(function () {
          status.className = 'form-status ok';
          status.textContent = 'Sent — thank you. I read every message and usually reply within a day or two.';
          form.reset();
        })
        .catch(function () {
          var body = encodeURIComponent(data.message + '\n\n— ' + data.name + ' (' + data.email + ')');
          var to = form.dataset.mailto;
          status.className = 'form-status err';
          status.innerHTML = 'That did not go through. You can ' +
            '<a href="mailto:' + to + '?subject=' + encodeURIComponent(data.subject) + '&body=' + body + '">' +
            'send it from your own mail app instead</a>.';
        })
        .then(function () { submit.removeAttribute('aria-busy'); });
    });
  }

  /* ---------- lightbox for the about-page photos ---------- */
  var lb2 = document.getElementById('lightbox');
  if (lb2) {
    var photos = Array.prototype.slice.call(document.querySelectorAll('.shots img'));
    if (photos.length) {
      var img2 = lb2.querySelector('img');
      var cap2 = lb2.querySelector('figcaption');
      var at2 = 0;
      var show2 = function (i) {
        at2 = (i + photos.length) % photos.length;
        img2.src = photos[at2].dataset.full || photos[at2].src;
        img2.alt = photos[at2].alt;
        cap2.textContent = photos[at2].alt;
      };
      photos.forEach(function (im, i) {
        im.addEventListener('click', function () {
          show2(i);
          lb2.classList.add('open');
          document.body.style.overflow = 'hidden';
        });
      });
      lb2.querySelector('.prev').addEventListener('click', function () {
        if (photos.length && lb2.classList.contains('open')) show2(at2 - 1);
      });
      lb2.querySelector('.next').addEventListener('click', function () {
        if (photos.length && lb2.classList.contains('open')) show2(at2 + 1);
      });
    }
  }

  /* ---------- footer year ---------- */
  var y = document.getElementById('year');
  if (y) y.textContent = String(new Date().getFullYear());
})();
