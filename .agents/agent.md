# Agent Rules and Memory

## Print to PDF Button

When creating or updating pages, ALWAYS remember to add the "Print Full PDF" button, the associated print Javascript, and the correct `@media print` CSS block.

The CSS should reset backgrounds to white, set text to black, hide unnecessary UI elements, and prevent page breaks inside cards using `break-inside: avoid; page-break-inside: avoid;`.

Example CSS:

```css
        .print-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border: 1px solid #00ff88;
            background: rgba(0, 255, 136, 0.1);
            color: #00ff88;
            border-radius: 6px;
            padding: 8px 14px;
            font-family: 'SF Mono', 'Monaco', 'Inconsolata', 'Fira Code', 'Consolas', monospace;
            font-size: 0.88rem;
            font-weight: 700;
            cursor: pointer;
            transition: transform 0.2s ease, border-color 0.2s ease, background 0.2s ease;
            margin-top: 15px;
        }

        .print-btn:hover {
            border-color: #ffffff;
            background: rgba(255, 255, 255, 0.06);
            transform: translateY(-1px);
        }

        @media print {
            @page { margin: 14mm; }
            * {
                box-shadow: none !important;
                text-shadow: none !important;
            }
            body { background: white !important; color: black !important; padding: 0; }
            .container, .section, .formula-box, table, th, td, .note, .step-block, .exam-q, .card, .problem-card { 
                background: white !important; 
                color: black !important; 
                border-color: #777777 !important;
                break-inside: avoid;
                page-break-inside: avoid;
            }
            header { background: white !important; color: black !important; border-bottom: 2px solid black !important; }
            h1, h2, h3, h4, p, li, strong, label, .step-label, .q-label, summary, .solution { color: black !important; }
            .nav-back, .print-btn, .solutions-link { display: none !important; }
            details { display: block !important; }
            details[open] .solution, details:not([open]) .solution { display: block !important; }
        }
```

Example Button:

```html
<button class="print-btn" type="button" onclick="window.print()">Print Full PDF</button>
```

## Design System & Theming Rules

- **Color Palette**: Use the established dark mode UI. Backgrounds should be dark, text should be light, and use the specific "greenish" neon accent color (`#00ff88`) for highlights and borders.
- **Typography**: Headings and body text should use sans-serif fonts, while code, buttons, and technical snippets should use monospace fonts (`'SF Mono', 'Monaco', 'Inconsolata', 'Fira Code', 'Consolas', monospace`).
- **Micro-interactions**: All interactive elements (buttons, interactive cards) must have hover states with subtle animations (e.g., `transform: translateY(-1px); transition: 0.2s ease;`).

## Layout & Mobile-First Constraints

- **Responsive Grids**: Always use CSS Grid for card layouts. Default to mobile-friendly grids (e.g., 2 columns on mobile) and scale up for desktop views.
- **Mobile Navigation**: Use a fixed, scrollable "Bottom Nav" chip strip on mobile viewports instead of relying on full-width sidebars.
- **Card Constraints**: On small breakpoints, use compact card styling. This includes line-clamping text, shrinking thumbnails, and hiding secondary links to maximize usability.

## Iconography Standards

- **SVG Policy**: Do not use text emojis, Font Awesome, or other font-based icons. All new icons must be SVGs sourced from the `assets/icons/` directory.
- **SVG Styling**: SVGs should generally use `fill="currentColor"` or `stroke="currentColor"` to automatically inherit text or accent colors and match the active theme dynamically.

## Educational Hub Architecture

- **Lecture Pages**: Must contain embedded PDF/PPT viewers and prominently feature direct navigation links to their corresponding problem-solution HTML pages.
- **Solutions Pages**: Provide step-by-step mathematical solutions. When populating from JSON datasets (like `context/lec1q.json`), strictly follow the established HTML structures (`problem-card`, `problem-statement`, `solution-details`, `solution-step`, `final-answer`).

## Search-First Philosophy

- For resource libraries and large hubs (like `resources.html`), the initial load state should present a "search-first" interface with a search bar and suggested topics.
- Detailed navigation and full category lists should be hidden on initial load and only displayed after the user selects a category or initiates a search.
