# Iteration 1 — Toggleable Theme: `year1sem2calc2.html` Only

## Goal
Ship the Manuscript theme toggle **entirely inside `year1sem2calc2.html`** — no shared files touched. Proves the concept, fully functional and persistent.

---

## Theme Definitions

### Theme A: **Terminal** (default — unchanged visually)
| Token | Value |
|---|---|
| `--bg` | `#000000` |
| `--surface` | `#0a0a0a` |
| `--accent` | `#00ff88` |
| `--text` | `#ffffff` |
| `--text-muted` | `#cccccc` |
| `--border` | `#1a1a1a` |
| `--border-strong` | `#333333` |
| `--font-body` | `'Inter', sans-serif` |
| `--font-mono` | `'JetBrains Mono', monospace` |

### Theme B: **Manuscript** (new — LaTeX parchment)
Inspired by the `integration_problems.tex` file: `12pt a4paper`, `geometry{margin=1in}`, academic article structure.

| Token | Value | Rationale |
|---|---|---|
| `--bg` | `#f5f0e8` | Warm parchment — aged LaTeX paper |
| `--surface` | `#faf7f2` | Off-white card/section surface |
| `--accent` | `#8b1a1a` | Deep academic red — annotation ink |
| `--text` | `#1a1a1a` | Near-black typeset ink |
| `--text-muted` | `#5a5a4a` | Sepia secondary — footnote-style |
| `--border` | `#d4c9b0` | Aged paper crease |
| `--border-strong` | `#a09070` | Heavier ruled line |
| `--font-body` | `Georgia, serif` | LaTeX Computer Modern feel |
| `--font-mono` | `'Courier New', monospace` | Typewriter / TeX verbatim |

---

## Step-by-Step Changes

### Step 1 — Add CSS custom properties
At the top of the `<style>` block, add two rule sets:

```css
:root {
  --bg:           #000000;
  --surface:      #0a0a0a;
  --accent:       #00ff88;
  --text:         #ffffff;
  --text-muted:   #cccccc;
  --border:       #1a1a1a;
  --border-strong:#333333;
  --font-body:    'Inter', sans-serif;
  --font-mono:    'JetBrains Mono', monospace;
}

[data-theme="manuscript"] {
  --bg:           #f5f0e8;
  --surface:      #faf7f2;
  --accent:       #8b1a1a;
  --text:         #1a1a1a;
  --text-muted:   #5a5a4a;
  --border:       #d4c9b0;
  --border-strong:#a09070;
  --font-body:    Georgia, 'Times New Roman', serif;
  --font-mono:    'Courier New', Courier, monospace;
}
```

### Step 2 — Refactor all hardcoded values → `var()`

Every hardcoded colour/font in the existing CSS gets replaced:

| Find | Replace with |
|---|---|
| `background: #000000` | `background: var(--bg)` |
| `background: #0a0a0a` | `background: var(--surface)` |
| `color: #00ff88` | `color: var(--accent)` |
| `border-color: #00ff88` | `border-color: var(--accent)` |
| `color: #ffffff` | `color: var(--text)` |
| `color: #cccccc` | `color: var(--text-muted)` |
| `border: 1px solid #1a1a1a` | `border: 1px solid var(--border)` |
| `border-bottom: 1px solid #333333` | `border-bottom: 1px solid var(--border-strong)` |
| `font-family: 'Inter'...` | `font-family: var(--font-body)` |
| `font-family: 'JetBrains Mono'...` | `font-family: var(--font-mono)` |
| rgba greens e.g. `rgba(0,255,136,0.08)` | keep as-is in Terminal; override for manuscript below |

### Step 3 — Manuscript-specific overrides (inside `[data-theme="manuscript"]`)

```css
[data-theme="manuscript"] .lec-card {
  border-top-color: var(--accent);
  background: var(--surface);
  box-shadow: 0 1px 4px rgba(0,0,0,0.08);
}

[data-theme="manuscript"] .lec-link--notes {
  background: rgba(139,26,26,0.07);
  color: var(--accent);
  border-color: rgba(139,26,26,0.3);
}

[data-theme="manuscript"] .formula-box {
  border-left-color: var(--accent);
}

[data-theme="manuscript"] .lec-card__badge {
  border-color: var(--accent);
  color: var(--accent);
}

[data-theme="manuscript"] tr:hover {
  background: #ede8dc;
}

/* Paper grain texture — CSS only, no image */
[data-theme="manuscript"] body {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23noise)' opacity='0.035'/%3E%3C/svg%3E");
}
```

### Step 4 — Toggle button in header HTML

Add alongside the existing print/video buttons:

```html
<button id="theme-toggle" class="print-btn no-print" type="button" 
        style="margin-left: 10px;">
  📜 Manuscript
</button>
```

### Step 5 — JS toggle logic (add to existing `<script>` block)

```js
(function () {
  const KEY = 'calc2-theme';
  const html = document.documentElement;
  const btn  = document.getElementById('theme-toggle');

  function apply(theme) {
    if (theme === 'manuscript') {
      html.setAttribute('data-theme', 'manuscript');
      btn.textContent = '💻 Terminal';
    } else {
      html.removeAttribute('data-theme');
      btn.textContent = '📜 Manuscript';
    }
  }

  // Restore on load (before paint to avoid flash)
  const saved = localStorage.getItem(KEY) || 'terminal';
  apply(saved);

  btn.addEventListener('click', function () {
    const next = html.getAttribute('data-theme') === 'manuscript'
      ? 'terminal'
      : 'manuscript';
    localStorage.setItem(KEY, next);
    apply(next);
  });
})();
```

> [!IMPORTANT]
> Apply the saved theme **before** first paint by placing the restore call at the top of `<body>` in an inline `<script>` (not deferred) to prevent a flash of the wrong theme.

---

## Deliverable
- Single file changed: `year1sem2calc2.html`
- Toggle button in header
- `localStorage` persistence
- No regressions to print styles (`.no-print` class already hides button)

---

## What's NOT in Iteration 1
- No changes to lecture sub-pages (`lec1.html`, `lec2sol.html`, etc.)
- No shared CSS/JS files created
- → That is Iteration 2
