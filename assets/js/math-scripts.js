/* ================================================================
   math-scripts.js — Shared scripts for all CS Hub calc/math pages
   Includes: theme toggle, card reveal, hash scroll, progress bar
   Anti-flash logic is handled by inline <script> in each file's <body>
   ================================================================ */
'use strict';

/* ── 1. Theme Toggle Button — inject if missing, then wire up ── */
document.addEventListener('DOMContentLoaded', function () {

    /* Inject button into header if page doesn't have one */
    var header = document.querySelector('header');
    if (header && !document.getElementById('theme-toggle')) {
        var btn = document.createElement('button');
        btn.id = 'theme-toggle';
        btn.className = 'print-btn no-print';
        btn.type = 'button';
        btn.style.marginLeft = '10px';
        btn.textContent = '\uD83D\uDCDC Manuscript';
        header.appendChild(btn);
    }

    /* Wire up the toggle (works for both injected and hardcoded buttons) */
    var KEY = 'calc2-theme';
    var html = document.documentElement;
    var toggleBtn = document.getElementById('theme-toggle');

    function applyTheme(theme) {
        if (theme === 'manuscript') {
            html.setAttribute('data-theme', 'manuscript');
            if (toggleBtn) toggleBtn.textContent = '\uD83D\uDCBB Terminal';
        } else {
            html.removeAttribute('data-theme');
            if (toggleBtn) toggleBtn.textContent = '\uD83D\uDCDC Manuscript';
        }
    }

    /* Sync label with whatever the anti-flash script already applied */
    var saved = localStorage.getItem(KEY) || 'terminal';
    applyTheme(saved);

    if (toggleBtn) {
        toggleBtn.addEventListener('click', function () {
            var next = html.getAttribute('data-theme') === 'manuscript'
                ? 'terminal'
                : 'manuscript';
            localStorage.setItem(KEY, next);
            applyTheme(next);
        });
    }

    /* ── 2. Card Reveal IntersectionObserver ── */
    var cards = document.querySelectorAll('.lec-card');
    if (cards.length) {
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry, i) {
                if (entry.isIntersecting) {
                    setTimeout(function () {
                        entry.target.classList.add('visible');
                    }, i * 60);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        cards.forEach(function (card) { observer.observe(card); });
    }

    /* ── 3. Reading Progress Bar (supports id="progress-bar" or id="myBar") ── */
    var bar = document.getElementById('progress-bar') || document.getElementById('myBar');
    if (bar) {
        function updateProgress() {
            var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
            var scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            bar.style.width = (scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0) + '%';
        }
        window.addEventListener('scroll', updateProgress, { passive: true });
        updateProgress();
    }

});

/* ── 4. Hash Scroll Handler (runs outside DOMContentLoaded for early hashes) ── */
(function () {
    function handleHash() {
        var hash = window.location.hash;
        if (!hash) return;
        var targetId = decodeURIComponent(hash.substring(1));
        var el = document.getElementById(targetId);
        if (!el) return;
        setTimeout(function () {
            el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 120);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function () {
            setTimeout(handleHash, 50);
        });
    } else {
        setTimeout(handleHash, 50);
    }

    window.addEventListener('hashchange', handleHash);
})();
