/* Shared behaviour: theme, mobile menu, skill bars, project filter, contact form */
(function () {
  'use strict';

  // ---- Theme (remembered between visits) ----
  var root = document.documentElement;
  function safeGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function safeSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  var saved = safeGet('theme');
  var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  root.setAttribute('data-theme', saved || (prefersDark ? 'dark' : 'light'));

  var toggle = document.querySelector('.theme-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      safeSet('theme', next);
    });
  }

  // ---- Mobile menu ----
  var burger = document.querySelector('.burger');
  var nav = document.getElementById('nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // ---- Footer year ----
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // ---- Skill bars fill when scrolled into view ----
  var bars = document.querySelectorAll('.bar i[data-level]');
  function fill(el) { el.style.width = el.getAttribute('data-level') + '%'; }
  if ('IntersectionObserver' in window && bars.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { fill(en.target); io.unobserve(en.target); }
      });
    }, { threshold: 0.3 });
    bars.forEach(function (b) { io.observe(b); });
  } else {
    bars.forEach(fill);
  }

  // ---- Project filter ----
  var chips = document.querySelectorAll('.chip[data-filter]');
  var projects = document.querySelectorAll('.project[data-cat]');
  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      var f = chip.getAttribute('data-filter');
      chips.forEach(function (c) { c.classList.toggle('on', c === chip); c.setAttribute('aria-pressed', String(c === chip)); });
      projects.forEach(function (p) {
        p.hidden = !(f === 'all' || p.getAttribute('data-cat').split(' ').indexOf(f) !== -1);
      });
    });
  });

  // ---- Contact form: validate, then open the visitor's email app ----
  var form = document.getElementById('contact-form');
  if (form) {
    var TO = 'c.sunday4937@miva.edu.ng';
    var rules = {
      name: function (v) { return v.trim() ? (v.trim().length >= 2 ? '' : 'Name must be at least 2 characters.') : 'Enter your name.'; },
      email: function (v) { if (!v.trim()) return 'Enter your email address.'; return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) ? '' : 'Enter a valid email address, like name@example.com.'; },
      phone: function (v) {
        var t = v.trim();
        if (!t) return 'Enter your phone number.';
        return /^\d+$/.test(t) ? '' : 'Use digits only, with no spaces, dashes or + sign.';
      },
      message: function (v) { return v.trim() ? '' : 'Enter a message.'; }
    };
    function check(field) {
      var msg = rules[field.name](field.value);
      field.setAttribute('aria-invalid', msg ? 'true' : 'false');
      var slot = form.querySelector('[data-error-for="' + field.name + '"]');
      if (slot) slot.textContent = msg;
      return !msg;
    }
    Object.keys(rules).forEach(function (n) {
      var f = form.elements[n];
      f.addEventListener('blur', function () { check(f); });
      f.addEventListener('input', function () { if (f.getAttribute('aria-invalid') === 'true') check(f); });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var valid = Object.keys(rules).map(function (n) { return check(form.elements[n]); }).every(Boolean);
      var status = document.getElementById('form-status');
      if (!valid) { status.textContent = 'Fix the highlighted fields and send again.'; status.className = 'error'; return; }
      var subject = encodeURIComponent('Portfolio message from ' + form.elements.name.value.trim());
      var body = encodeURIComponent(form.elements.message.value.trim() + '\n\nFrom: ' + form.elements.name.value.trim() + ' (' + form.elements.email.value.trim() + ', ' + form.elements.phone.value.trim() + ')');
      status.textContent = 'Thanks! Your email app should open with the message ready to send.';
      status.className = 'ok';
      window.location.href = 'mailto:' + TO + '?subject=' + subject + '&body=' + body;
      form.reset();
    });
  }
})();
