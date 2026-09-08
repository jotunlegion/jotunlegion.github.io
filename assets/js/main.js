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
    lb.querySelector('.prev').addEventListener('click', function () { show(at - 1); });
    lb.querySelector('.next').addEventListener('click', function () { show(at + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
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

  /* ---------- footer year ---------- */
  var y = document.getElementById('year');
  if (y) y.textContent = String(new Date().getFullYear());
})();
