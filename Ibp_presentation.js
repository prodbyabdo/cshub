const pptxgen = require("pptxgenjs");

const pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';
pres.title = 'Integration by Parts';

// ── PALETTE (black & white academic) ──────────────────────────────────────
const BLACK = "000000";
const WHITE = "FFFFFF";
const GRAY1 = "1A1A1A";  // near-black headings
const GRAY2 = "444444";  // body text
const GRAY3 = "888888";  // muted / caption
const LGRAY = "F0F0F0";  // light card background
const MGRAY = "CCCCCC";  // borders / rules
const DGRAY = "222222";  // dark accent blocks

const TITLE_FONT = "Georgia";
const BODY_FONT = "Calibri";

// helper – horizontal rule
function hRule(slide, y, color = MGRAY, width = 1) {
    slide.addShape(pres.shapes.LINE, { x: 0.5, y, w: 9, h: 0, line: { color, width } });
}

// helper – slide number footer
function footer(slide, n) {
    slide.addText(`${n}`, {
        x: 9.2, y: 5.2, w: 0.6, h: 0.3,
        fontSize: 9, color: GRAY3, fontFace: BODY_FONT, align: "right"
    });
}

// helper – section label (top-left small cap)
function sectionLabel(slide, txt) {
    slide.addText(txt.toUpperCase(), {
        x: 0.5, y: 0.18, w: 5, h: 0.25,
        fontSize: 8, color: GRAY3, fontFace: BODY_FONT, bold: true, charSpacing: 2
    });
}

// ─── SLIDE 1 ─ TITLE ─────────────────────────────────────────────────────
{
    const s = pres.addSlide();
    s.background = { color: GRAY1 };

    // large geometric accent – thin vertical bar left
    s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: WHITE } });

    s.addText("Integration by Parts", {
        x: 0.5, y: 1.2, w: 9, h: 1.4,
        fontSize: 48, bold: true, color: WHITE, fontFace: TITLE_FONT, align: "left"
    });
    s.addText("∫ u dv  =  uv  −  ∫ v du", {
        x: 0.5, y: 2.7, w: 9, h: 0.8,
        fontSize: 26, color: MGRAY, fontFace: BODY_FONT, italic: true, align: "left"
    });
    s.addText("Calculus II  ·  MAT 128  ·  Student Seminar Presentation", {
        x: 0.5, y: 3.7, w: 9, h: 0.4,
        fontSize: 13, color: GRAY3, fontFace: BODY_FONT, align: "left"
    });
    s.addText("Dr. Hiba Omer  ·  Faculty of Computer Science & IT", {
        x: 0.5, y: 4.1, w: 9, h: 0.3,
        fontSize: 11, color: GRAY3, fontFace: BODY_FONT, align: "left"
    });
    footer(s, "");
}

// ─── SLIDE 2 ─ AGENDA ────────────────────────────────────────────────────
{
    const s = pres.addSlide();
    s.background = { color: WHITE };
    sectionLabel(s, "Overview");

    s.addText("What We'll Cover", {
        x: 0.5, y: 0.5, w: 9, h: 0.7,
        fontSize: 32, bold: true, color: GRAY1, fontFace: TITLE_FONT
    });
    hRule(s, 1.25);

    const items = [
        ["01", "Prerequisites", "Algebra & Calculus I review"],
        ["02", "Derivation", "Where does ∫u dv = uv − ∫v du come from?"],
        ["03", "LIATE Rule", "How to choose u and dv every time"],
        ["04", "Natural Log Rule", "∫ ln x dx and its family"],
        ["05", "Advanced Techniques", "Substitution inside IBP, recurrent integration,\ninverse hyperbolic functions"],
        ["06", "7 Worked Examples", "From warm-up to the I-trick"],
    ];

    items.forEach(([num, title, desc], i) => {
        const y = 1.4 + i * 0.67;
        s.addText(num, {
            x: 0.5, y, w: 0.45, h: 0.5,
            fontSize: 11, bold: true, color: WHITE, fontFace: BODY_FONT, align: "center", valign: "middle",
            fill: { color: GRAY1 }, margin: 0
        });
        s.addText(title, {
            x: 1.05, y: y + 0.01, w: 2.5, h: 0.25,
            fontSize: 13, bold: true, color: GRAY1, fontFace: BODY_FONT
        });
        s.addText(desc, {
            x: 1.05, y: y + 0.26, w: 8.2, h: 0.28,
            fontSize: 10, color: GRAY2, fontFace: BODY_FONT
        });
    });
    footer(s, 2);
}

// ─── SLIDE 3 ─ PREREQUISITES: ALGEBRA ────────────────────────────────────
{
    const s = pres.addSlide();
    s.background = { color: WHITE };
    sectionLabel(s, "Prerequisites");

    s.addText("Algebra Essentials", {
        x: 0.5, y: 0.5, w: 9, h: 0.7,
        fontSize: 30, bold: true, color: GRAY1, fontFace: TITLE_FONT
    });
    hRule(s, 1.25);

    // Two columns
    const col1 = [
        ["Expand before integrating", "(a + b)²  =  a² + 2ab + b²"],
        ["Factor denominators", "Split fractions into simpler terms first"],
        ["Exponent laws", "xᵃ · xᵇ = xᵃ⁺ᵇ,   (xᵃ)ᵇ = xᵃᵇ"],
        ["Negative / frac exponents", "1/xⁿ = x⁻ⁿ,   ⁿ√x = x^(1/n)"],
    ];
    const col2 = [
        ["Log identities", "ln(ab) = ln a + ln b\nln(aⁿ) = n ln a"],
        ["Trig identities", "sin²x + cos²x = 1\nsin 2x = 2 sin x cos x"],
        ["Completing the square", "x² + bx = (x + b/2)² − (b/2)²"],
        ["Partial fractions", "Used when denominator factors nicely"],
    ];

    [[col1, 0.5], [col2, 5.1]].forEach(([items, x]) => {
        items.forEach(([h, d], i) => {
            const y = 1.4 + i * 0.95;
            s.addShape(pres.shapes.RECTANGLE, { x, y, w: 4.4, h: 0.8, fill: { color: LGRAY }, line: { color: MGRAY, width: 0.5 } });
            s.addText(h, { x: x + 0.12, y: y + 0.05, w: 4.2, h: 0.28, fontSize: 11, bold: true, color: GRAY1, fontFace: BODY_FONT });
            s.addText(d, { x: x + 0.12, y: y + 0.34, w: 4.2, h: 0.44, fontSize: 10, color: GRAY2, fontFace: BODY_FONT });
        });
    });
    footer(s, 3);
}

// ─── SLIDE 4 ─ PREREQUISITES: CALCULUS I ─────────────────────────────────
{
    const s = pres.addSlide();
    s.background = { color: WHITE };
    sectionLabel(s, "Prerequisites");

    s.addText("Calculus I Essentials", {
        x: 0.5, y: 0.5, w: 9, h: 0.7,
        fontSize: 30, bold: true, color: GRAY1, fontFace: TITLE_FONT
    });
    hRule(s, 1.25);

    // Derivatives table left, Integrals table right
    const derivs = [
        ["d/dx [xⁿ]", "n xⁿ⁻¹"],
        ["d/dx [eˣ]", "eˣ"],
        ["d/dx [ln x]", "1/x"],
        ["d/dx [sin x]", "cos x"],
        ["d/dx [cos x]", "−sin x"],
        ["d/dx [tan⁻¹x]", "1/(x²+1)"],
        ["d/dx [sinh⁻¹x]", "1/√(x²+a²)  (inverse hyp)"],
        ["Product Rule", "(uv)' = u'v + uv'  ← KEY!"],
    ];
    const intgs = [
        ["∫ xⁿ dx", "xⁿ⁺¹/(n+1) + C,  n ≠ −1"],
        ["∫ x⁻¹ dx", "ln|x| + C"],
        ["∫ eˣ dx", "eˣ + C"],
        ["∫ eᵃˣ dx", "(1/a)eᵃˣ + C"],
        ["∫ sin x dx", "−cos x + C"],
        ["∫ cos x dx", "sin x + C"],
        ["∫ 1/(x²+a²) dx", "(1/a) tan⁻¹(x/a) + C"],
        ["∫ 1/√(x²+a²) dx", "sinh⁻¹(x/a) + C  or  ln|x+√(x²+a²)|+C"],
    ];

    // header row
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.35, w: 4.4, h: 0.3, fill: { color: GRAY1 } });
    s.addText("Derivative", { x: 0.5, y: 1.35, w: 2.2, h: 0.3, fontSize: 10, bold: true, color: WHITE, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0 });
    s.addText("Result", { x: 2.7, y: 1.35, w: 2.2, h: 0.3, fontSize: 10, bold: true, color: WHITE, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0 });

    s.addShape(pres.shapes.RECTANGLE, { x: 5.1, y: 1.35, w: 4.4, h: 0.3, fill: { color: GRAY1 } });
    s.addText("Integral", { x: 5.1, y: 1.35, w: 2.2, h: 0.3, fontSize: 10, bold: true, color: WHITE, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0 });
    s.addText("Result", { x: 7.3, y: 1.35, w: 2.2, h: 0.3, fontSize: 10, bold: true, color: WHITE, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0 });

    derivs.forEach(([f, r], i) => {
        const y = 1.65 + i * 0.47;
        const bg = i % 2 === 0 ? WHITE : LGRAY;
        s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y, w: 4.4, h: 0.45, fill: { color: bg }, line: { color: MGRAY, width: 0.3 } });
        s.addText(f, { x: 0.55, y: y + 0.05, w: 2.1, h: 0.35, fontSize: 9.5, bold: true, color: GRAY1, fontFace: BODY_FONT });
        s.addText(r, { x: 2.7, y: y + 0.05, w: 2.15, h: 0.35, fontSize: 9.5, color: GRAY2, fontFace: BODY_FONT });
    });
    intgs.forEach(([f, r], i) => {
        const y = 1.65 + i * 0.47;
        const bg = i % 2 === 0 ? WHITE : LGRAY;
        s.addShape(pres.shapes.RECTANGLE, { x: 5.1, y, w: 4.4, h: 0.45, fill: { color: bg }, line: { color: MGRAY, width: 0.3 } });
        s.addText(f, { x: 5.15, y: y + 0.05, w: 2.1, h: 0.35, fontSize: 9.5, bold: true, color: GRAY1, fontFace: BODY_FONT });
        s.addText(r, { x: 7.3, y: y + 0.05, w: 2.15, h: 0.35, fontSize: 9.5, color: GRAY2, fontFace: BODY_FONT });
    });
    footer(s, 4);
}

// ─── SLIDE 5 ─ DERIVATION ────────────────────────────────────────────────
{
    const s = pres.addSlide();
    s.background = { color: WHITE };
    sectionLabel(s, "Derivation");

    s.addText("Where Does IBP Come From?", {
        x: 0.5, y: 0.5, w: 9, h: 0.7,
        fontSize: 30, bold: true, color: GRAY1, fontFace: TITLE_FONT
    });
    hRule(s, 1.25);

    const steps = [
        ["Step 1 — Product Rule",
            "Start from something we already know:\n(uv)' = u'v + uv'"],
        ["Step 2 — Rearrange",
            "Isolate the term we want:\nuv' = (uv)' − u'v"],
        ["Step 3 — Integrate both sides",
            "∫ uv' dx  =  ∫ (uv)' dx  −  ∫ u'v dx"],
        ["Step 4 — Apply FTC on the right term",
            "∫ (uv)' dx  =  uv   (fundamental theorem)"],
        ["Step 5 — Substitute differentials  dv = v'dx,  du = u'dx",
            "∫ u dv  =  uv  −  ∫ v du   ✓"],
    ];

    steps.forEach(([h, d], i) => {
        const y = 1.35 + i * 0.82;
        // step number circle
        s.addShape(pres.shapes.OVAL, { x: 0.5, y: y + 0.07, w: 0.38, h: 0.38, fill: { color: GRAY1 } });
        s.addText(`${i + 1}`, { x: 0.5, y: y + 0.07, w: 0.38, h: 0.38, fontSize: 11, bold: true, color: WHITE, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0 });
        s.addText(h, { x: 1.05, y: y + 0.03, w: 8.4, h: 0.28, fontSize: 12, bold: true, color: GRAY1, fontFace: BODY_FONT });
        s.addText(d, { x: 1.05, y: y + 0.3, w: 8.4, h: 0.45, fontSize: 11, color: GRAY2, fontFace: BODY_FONT, italic: (i === 4) });
    });

    // final boxed formula
    s.addShape(pres.shapes.RECTANGLE, { x: 2.5, y: 5.1, w: 5, h: 0.38, fill: { color: GRAY1 } });
    s.addText("∫ u dv  =  uv  −  ∫ v du", {
        x: 2.5, y: 5.1, w: 5, h: 0.38,
        fontSize: 16, bold: true, color: WHITE, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0
    });
    footer(s, 5);
}

// ─── SLIDE 6 ─ LIATE ─────────────────────────────────────────────────────
{
    const s = pres.addSlide();
    s.background = { color: WHITE };
    sectionLabel(s, "LIATE Rule");

    s.addText("How to Choose  u  — LIATE", {
        x: 0.5, y: 0.5, w: 9, h: 0.7,
        fontSize: 30, bold: true, color: GRAY1, fontFace: TITLE_FONT
    });
    hRule(s, 1.25);

    s.addText("Pick u as the first function type you see in this priority list — then dv = everything else.", {
        x: 0.5, y: 1.35, w: 9, h: 0.35, fontSize: 12, color: GRAY2, fontFace: BODY_FONT
    });

    const liate = [
        ["L", "Logarithms", "ln x,  log x"],
        ["I", "Inverse Trig", "tan⁻¹x,  sin⁻¹x,  cos⁻¹x,  sinh⁻¹x"],
        ["A", "Algebraic", "xⁿ,  polynomials,  √x"],
        ["T", "Trigonometric", "sin x,  cos x,  tan x"],
        ["E", "Exponential", "eˣ,  aˣ"],
    ];

    const widths = [0.45, 2.4, 5.8];
    const xs = [0.5, 0.95, 3.35];

    // header
    ["", "Category", "Examples"].forEach((h, col) => {
        s.addShape(pres.shapes.RECTANGLE, { x: xs[col], y: 1.78, w: widths[col], h: 0.32, fill: { color: GRAY1 } });
        s.addText(h, { x: xs[col], y: 1.78, w: widths[col], h: 0.32, fontSize: 10, bold: true, color: WHITE, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0 });
    });

    liate.forEach(([letter, cat, ex], i) => {
        const y = 2.1 + i * 0.55;
        const bg = i % 2 === 0 ? WHITE : LGRAY;
        // letter cell
        s.addShape(pres.shapes.RECTANGLE, { x: xs[0], y, w: widths[0], h: 0.52, fill: { color: bg }, line: { color: MGRAY, width: 0.5 } });
        s.addText(letter, { x: xs[0], y: y + 0.05, w: widths[0], h: 0.42, fontSize: 20, bold: true, color: GRAY1, fontFace: TITLE_FONT, align: "center", valign: "middle", margin: 0 });
        // category
        s.addShape(pres.shapes.RECTANGLE, { x: xs[1], y, w: widths[1], h: 0.52, fill: { color: bg }, line: { color: MGRAY, width: 0.5 } });
        s.addText(cat, { x: xs[1] + 0.08, y: y + 0.1, w: widths[1] - 0.1, h: 0.33, fontSize: 12, bold: true, color: GRAY1, fontFace: BODY_FONT });
        // examples
        s.addShape(pres.shapes.RECTANGLE, { x: xs[2], y, w: widths[2], h: 0.52, fill: { color: bg }, line: { color: MGRAY, width: 0.5 } });
        s.addText(ex, { x: xs[2] + 0.1, y: y + 0.1, w: widths[2] - 0.15, h: 0.33, fontSize: 11, color: GRAY2, fontFace: BODY_FONT, italic: true });
    });

    s.addText("Note: LIATE has exceptions — if in doubt, try both ways and see which remaining integral is simpler.", {
        x: 0.5, y: 5.02, w: 9, h: 0.3, fontSize: 9.5, color: GRAY3, fontFace: BODY_FONT, italic: true
    });
    footer(s, 6);
}

// ─── SLIDE 7 ─ EXAMPLE 1 (warm-up: ∫ xe^x dx) ───────────────────────────
{
    const s = pres.addSlide();
    s.background = { color: WHITE };
    sectionLabel(s, "Example 1 — Warm-Up");

    s.addText("Example 1:  ∫ x eˣ dx", {
        x: 0.5, y: 0.5, w: 9, h: 0.65,
        fontSize: 28, bold: true, color: GRAY1, fontFace: TITLE_FONT
    });
    hRule(s, 1.2);

    // LIATE hint box
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.28, w: 3.8, h: 0.75, fill: { color: LGRAY }, line: { color: MGRAY, width: 0.5 } });
    s.addText("LIATE: A before E", { x: 0.6, y: 1.32, w: 3.6, h: 0.28, fontSize: 11, bold: true, color: GRAY1, fontFace: BODY_FONT });
    s.addText("u = x  (Algebraic)\ndv = eˣ dx  (Exponential)", { x: 0.6, y: 1.6, w: 3.6, h: 0.4, fontSize: 10.5, color: GRAY2, fontFace: BODY_FONT });

    const steps = [
        "Identify:  u = x   ⟹   du = dx",
        "           dv = eˣ dx   ⟹   v = eˣ",
        "Apply IBP formula:",
        "∫ x eˣ dx  =  x · eˣ  −  ∫ eˣ · dx",
        "           =  x eˣ  −  eˣ  +  C",
        "           =  eˣ(x − 1)  +  C",
    ];

    steps.forEach((line, i) => {
        s.addText(line, {
            x: 0.6, y: 2.15 + i * 0.5, w: 8.8, h: 0.45,
            fontSize: (i === 2) ? 11 : 13,
            bold: (i === 2),
            color: (i >= 3) ? GRAY1 : GRAY2,
            fontFace: BODY_FONT,
            italic: (i === 2)
        });
    });

    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.05, w: 8.8, h: 0.38, fill: { color: LGRAY }, line: { color: MGRAY, width: 0.5 } });
    s.addText("∫ x eˣ dx  =  eˣ(x − 1)  +  C", {
        x: 0.5, y: 5.05, w: 8.8, h: 0.38,
        fontSize: 15, bold: true, color: GRAY1, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0
    });
    footer(s, 7);
}

// ─── SLIDE 8 ─ EXAMPLE 2 (Natural Log: ∫ ln x dx) ───────────────────────
{
    const s = pres.addSlide();
    s.background = { color: WHITE };
    sectionLabel(s, "Example 2 — Natural Log Rule");

    s.addText("Example 2:  ∫ ln x dx", {
        x: 0.5, y: 0.5, w: 9, h: 0.65,
        fontSize: 28, bold: true, color: GRAY1, fontFace: TITLE_FONT
    });
    hRule(s, 1.2);

    s.addText("Key insight:  ln x has no obvious dv partner — give it the full integrand role!\nWrite the integrand as  ln x · 1 dx  so we can set  dv = dx.", {
        x: 0.5, y: 1.28, w: 9, h: 0.55, fontSize: 11.5, color: GRAY2, fontFace: BODY_FONT
    });

    // Choice box
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.9, w: 4.2, h: 0.7, fill: { color: LGRAY }, line: { color: MGRAY, width: 0.5 } });
    s.addText("u = ln x   ⟹   du = (1/x) dx\ndv = dx      ⟹   v = x", {
        x: 0.6, y: 1.98, w: 4, h: 0.55, fontSize: 12, color: GRAY1, fontFace: BODY_FONT
    });

    const steps = [
        ["Apply IBP:", "∫ ln x dx  =  x ln x  −  ∫ x · (1/x) dx"],
        ["Simplify:", "           =  x ln x  −  ∫ 1 dx"],
        ["Integrate:", "           =  x ln x  −  x  +  C"],
    ];

    steps.forEach(([label, eq], i) => {
        const y = 2.75 + i * 0.65;
        s.addText(label, { x: 0.5, y, w: 1.5, h: 0.45, fontSize: 11, bold: true, color: GRAY3, fontFace: BODY_FONT, italic: true });
        s.addText(eq, { x: 2.0, y, w: 7.4, h: 0.45, fontSize: 13, color: GRAY1, fontFace: BODY_FONT });
    });

    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 4.72, w: 8.8, h: 0.38, fill: { color: GRAY1 } });
    s.addText("∫ ln x dx  =  x ln x  −  x  +  C", {
        x: 0.5, y: 4.72, w: 8.8, h: 0.38,
        fontSize: 16, bold: true, color: WHITE, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0
    });

    s.addText("Generalisation:  ∫ xⁿ ln x dx — use u = ln x  for any n ≠ −1", {
        x: 0.5, y: 5.18, w: 9, h: 0.25, fontSize: 10, color: GRAY3, fontFace: BODY_FONT, italic: true
    });
    footer(s, 8);
}

// ─── SLIDE 9 ─ EXAMPLE 3 (x² ln x — polynomial × log) ───────────────────
{
    const s = pres.addSlide();
    s.background = { color: WHITE };
    sectionLabel(s, "Example 3 — Log × Polynomial");

    s.addText("Example 3:  ∫ x² ln x dx", {
        x: 0.5, y: 0.5, w: 9, h: 0.65,
        fontSize: 28, bold: true, color: GRAY1, fontFace: TITLE_FONT
    });
    hRule(s, 1.2);

    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.28, w: 4.4, h: 0.7, fill: { color: LGRAY }, line: { color: MGRAY, width: 0.5 } });
    s.addText("LIATE: L before A\nu = ln x   ⟹   du = (1/x) dx\ndv = x² dx   ⟹   v = x³/3", {
        x: 0.6, y: 1.33, w: 4.2, h: 0.6, fontSize: 11, color: GRAY1, fontFace: BODY_FONT
    });

    const lines = [
        "∫ x² ln x dx  =  (x³/3) · ln x  −  ∫ (x³/3) · (1/x) dx",
        "              =  (x³/3) ln x  −  (1/3) ∫ x² dx",
        "              =  (x³/3) ln x  −  (1/3) · (x³/3)  +  C",
        "              =  (x³/3) ln x  −  x³/9  +  C",
        "              =  (x³/9)(3 ln x  −  1)  +  C",
    ];
    lines.forEach((l, i) => {
        s.addText(l, { x: 0.6, y: 2.1 + i * 0.56, w: 8.8, h: 0.5, fontSize: 13, color: i >= 3 ? GRAY1 : GRAY2, fontFace: BODY_FONT });
    });

    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 4.98, w: 8.8, h: 0.38, fill: { color: LGRAY }, line: { color: MGRAY, width: 0.5 } });
    s.addText("∫ x² ln x dx  =  (x³/9)(3 ln x − 1)  +  C", {
        x: 0.5, y: 4.98, w: 8.8, h: 0.38,
        fontSize: 15, bold: true, color: GRAY1, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0
    });
    footer(s, 9);
}

// ─── SLIDE 10 ─ EXAMPLE 4 (∫ tan⁻¹x dx — IBP + substitution) ────────────
{
    const s = pres.addSlide();
    s.background = { color: WHITE };
    sectionLabel(s, "Example 4 — Inverse Trig with Substitution");

    s.addText("Example 4:  ∫ tan⁻¹x dx", {
        x: 0.5, y: 0.5, w: 9, h: 0.65,
        fontSize: 28, bold: true, color: GRAY1, fontFace: TITLE_FONT
    });
    hRule(s, 1.2);

    // highlight note
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.28, w: 5.5, h: 0.62, fill: { color: LGRAY }, line: { color: MGRAY, width: 0.5 } });
    s.addText("LIATE: I comes first!\nu = tan⁻¹x   ⟹   du = dx / (x²+1)\ndv = dx           ⟹   v = x", {
        x: 0.6, y: 1.33, w: 5.3, h: 0.52, fontSize: 11, color: GRAY1, fontFace: BODY_FONT
    });

    const lines = [
        "∫ tan⁻¹x dx  =  x tan⁻¹x  −  ∫ x / (x²+1) dx",
        "Now handle the remaining integral using substitution:",
        "   Let w = x²+1   ⟹   dw = 2x dx   ⟹   x dx = dw/2",
        "   ∫ x/(x²+1) dx  =  (1/2) ∫ dw/w  =  (1/2) ln|w|  =  (1/2) ln(x²+1)",
        "Substituting back:",
        "∫ tan⁻¹x dx  =  x tan⁻¹x  −  (1/2) ln(x²+1)  +  C",
    ];
    lines.forEach((l, i) => {
        s.addText(l, {
            x: 0.6, y: 2.02 + i * 0.52, w: 8.8, h: 0.47,
            fontSize: (i === 1 || i === 4) ? 11 : 12.5,
            bold: (i === 1 || i === 4),
            color: [1, 4].includes(i) ? GRAY3 : GRAY1,
            fontFace: BODY_FONT, italic: [1, 4].includes(i)
        });
    });

    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.07, w: 8.8, h: 0.38, fill: { color: GRAY1 } });
    s.addText("∫ tan⁻¹x dx  =  x tan⁻¹x  −  ½ ln(x²+1)  +  C", {
        x: 0.5, y: 5.07, w: 8.8, h: 0.38,
        fontSize: 15, bold: true, color: WHITE, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0
    });
    footer(s, 10);
}

// ─── SLIDE 11 ─ EXAMPLE 5 (∫ x sin x dx — du focus) ─────────────────────
{
    const s = pres.addSlide();
    s.background = { color: WHITE };
    sectionLabel(s, "Example 5 — Focus on du");

    s.addText("Example 5:  ∫ x sin x dx", {
        x: 0.5, y: 0.5, w: 9, h: 0.65,
        fontSize: 28, bold: true, color: GRAY1, fontFace: TITLE_FONT
    });
    hRule(s, 1.2);

    // Tip box
    s.addShape(pres.shapes.RECTANGLE, { x: 5.5, y: 1.28, w: 4.0, h: 0.9, fill: { color: LGRAY }, line: { color: MGRAY, width: 0.5 } });
    s.addText("Focus on du", { x: 5.6, y: 1.32, w: 3.8, h: 0.28, fontSize: 11, bold: true, color: GRAY1, fontFace: BODY_FONT });
    s.addText("We pick u = x so that du = dx\neliminates the polynomial factor in\nthe remaining ∫ v du.", { x: 5.6, y: 1.6, w: 3.8, h: 0.55, fontSize: 10, color: GRAY2, fontFace: BODY_FONT });

    const main = [
        "u = x     du = dx",
        "dv = sin x dx     v = −cos x",
        "",
        "∫ x sin x dx  =  x(−cos x)  −  ∫ (−cos x) dx",
        "              =  −x cos x  +  ∫ cos x dx",
        "              =  −x cos x  +  sin x  +  C",
    ];
    main.forEach((l, i) => {
        if (l === "") return;
        s.addText(l, {
            x: 0.6, y: 1.32 + i * 0.6, w: 4.7, h: 0.55,
            fontSize: i >= 3 ? 13 : 12,
            bold: i === 0 || i === 1,
            color: i >= 3 ? GRAY1 : GRAY2,
            fontFace: BODY_FONT
        });
    });

    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.02, w: 8.8, h: 0.38, fill: { color: LGRAY }, line: { color: MGRAY, width: 0.5 } });
    s.addText("∫ x sin x dx  =  −x cos x  +  sin x  +  C", {
        x: 0.5, y: 5.02, w: 8.8, h: 0.38,
        fontSize: 15, bold: true, color: GRAY1, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0
    });
    footer(s, 11);
}

// ─── SLIDE 12 ─ EXAMPLE 6 (Recurrent: ∫ e³ˣ cos 2x dx) ──────────────────
{
    const s = pres.addSlide();
    s.background = { color: WHITE };
    sectionLabel(s, "Example 6 — Recurrent Integration (Calling I)");

    s.addText("Example 6:  ∫ e³ˣ cos 2x dx", {
        x: 0.5, y: 0.5, w: 9, h: 0.65,
        fontSize: 26, bold: true, color: GRAY1, fontFace: TITLE_FONT
    });
    hRule(s, 1.2);

    // tip
    s.addShape(pres.shapes.RECTANGLE, { x: 6.2, y: 1.28, w: 3.3, h: 0.7, fill: { color: LGRAY }, line: { color: MGRAY, width: 0.5 } });
    s.addText("The I-Trick\nThe original integral reappears — collect it on one side!", {
        x: 6.3, y: 1.3, w: 3.1, h: 0.62, fontSize: 9.5, color: GRAY2, fontFace: BODY_FONT
    });

    const lines = [
        "Let  I  =  ∫ e³ˣ cos 2x dx",
        "1st IBP:  u = e³ˣ, dv = cos 2x dx  ⟹  v = (1/2) sin 2x",
        "I  =  (1/2) e³ˣ sin 2x  −  (3/2) ∫ e³ˣ sin 2x dx",
        "2nd IBP on the new integral:  u = e³ˣ, dv = sin 2x dx  ⟹  v = −(1/2) cos 2x",
        "I  =  (1/2) e³ˣ sin 2x  −  (3/2)[−(1/2) e³ˣ cos 2x + (3/2) ∫ e³ˣ cos 2x dx]",
        "I  =  (1/2) e³ˣ sin 2x  +  (3/4) e³ˣ cos 2x  −  (9/4) I",
        "(1 + 9/4) I  =  (1/2) e³ˣ sin 2x  +  (3/4) e³ˣ cos 2x",
        "(13/4) I  =  (e³ˣ/4)(2 sin 2x + 3 cos 2x)",
        "I  =  e³ˣ/13 · (2 sin 2x + 3 cos 2x)  +  C",
    ];

    lines.forEach((l, i) => {
        s.addText(l, {
            x: 0.5, y: 2.05 + i * 0.38, w: 9.2, h: 0.36,
            fontSize: [0, 5, 6, 7, 8].includes(i) ? 11.5 : 10.5,
            bold: [0, 8].includes(i),
            color: i >= 5 ? GRAY1 : GRAY2,
            fontFace: BODY_FONT
        });
    });

    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.45, w: 8.8, h: 0.0, fill: { color: MGRAY }, line: { color: MGRAY, width: 0.5 } });
    footer(s, 12);
}

// ─── SLIDE 13 ─ EXAMPLE 7 (Inverse Hyperbolic: ∫√(x²+a²) dx) ────────────
{
    const s = pres.addSlide();
    s.background = { color: WHITE };
    sectionLabel(s, "Example 7 — Inverse Hyperbolic & Recurrent IBP");

    s.addText("Example 7:  ∫ √(x²+a²) dx", {
        x: 0.5, y: 0.5, w: 9, h: 0.65,
        fontSize: 26, bold: true, color: GRAY1, fontFace: TITLE_FONT
    });
    hRule(s, 1.2);

    // recall box
    s.addShape(pres.shapes.RECTANGLE, { x: 6.2, y: 1.28, w: 3.3, h: 0.72, fill: { color: LGRAY }, line: { color: MGRAY, width: 0.5 } });
    s.addText("Recall:\n∫ dx/√(x²+a²)  =  sinh⁻¹(x/a)  +  C\n(or  ln|x + √(x²+a²)|  + C)", {
        x: 6.3, y: 1.32, w: 3.1, h: 0.63, fontSize: 9, color: GRAY2, fontFace: BODY_FONT
    });

    const lines = [
        "Let  I  =  ∫ √(x²+a²) dx",
        "IBP:  u = √(x²+a²)   ⟹   du = x/√(x²+a²) dx",
        "       dv = dx             ⟹   v = x",
        "I  =  x√(x²+a²)  −  ∫ x²/√(x²+a²) dx",
        "Write x² = (x²+a²) − a²  inside the integral:",
        "I  =  x√(x²+a²)  −  ∫ (x²+a²)/√(x²+a²) dx  +  a² ∫ dx/√(x²+a²)",
        "I  =  x√(x²+a²)  −  I  +  a² sinh⁻¹(x/a)",
        "Collect I on the left:",
        "2I  =  x√(x²+a²)  +  a² sinh⁻¹(x/a)",
        "I   =  (1/2) x√(x²+a²)  +  (a²/2) sinh⁻¹(x/a)  +  C",
    ];

    lines.forEach((l, i) => {
        s.addText(l, {
            x: 0.5, y: 2.04 + i * 0.37, w: 9.0, h: 0.35,
            fontSize: [0, 9].includes(i) ? 12 : 10.5,
            bold: [0, 9].includes(i),
            color: i >= 6 ? GRAY1 : GRAY2,
            italic: [4, 7].includes(i),
            fontFace: BODY_FONT
        });
    });

    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.08, w: 8.8, h: 0.38, fill: { color: GRAY1 } });
    s.addText("∫ √(x²+a²) dx  =  ½ x√(x²+a²)  +  (a²/2) sinh⁻¹(x/a)  +  C", {
        x: 0.5, y: 5.08, w: 8.8, h: 0.38,
        fontSize: 13, bold: true, color: WHITE, fontFace: BODY_FONT, align: "center", valign: "middle", margin: 0
    });
    footer(s, 13);
}

// ─── SLIDE 14 ─ SUMMARY ───────────────────────────────────────────────────
{
    const s = pres.addSlide();
    s.background = { color: GRAY1 };

    s.addText("Summary", {
        x: 0.5, y: 0.5, w: 9, h: 0.65,
        fontSize: 34, bold: true, color: WHITE, fontFace: TITLE_FONT
    });
    hRule(s, 1.2, MGRAY);

    const cards = [
        ["IBP Formula", "∫ u dv  =  uv  −  ∫ v du\nDerived from the Product Rule"],
        ["LIATE", "L  I  A  T  E\nPick u as the highest-priority type"],
        ["Natural Log Rule", "∫ ln x dx = x ln x − x + C\nAlways let u = ln x (L comes first)"],
        ["IBP + Substitution", "After applying IBP, the ∫v du may need\na u-substitution to finish"],
        ["Recurrent / I-trick", "If original ∫ reappears, name it I,\ncollect and solve algebraically"],
        ["Inv. Hyperbolic", "∫√(x²+a²)dx uses IBP twice + I-trick\nFinal answer involves sinh⁻¹"],
    ];

    cards.forEach(([h, d], i) => {
        const col = i % 2, row = Math.floor(i / 2);
        const x = 0.5 + col * 4.75, y = 1.35 + row * 1.4;
        s.addShape(pres.shapes.RECTANGLE, { x, y, w: 4.4, h: 1.28, fill: { color: "2A2A2A" }, line: { color: MGRAY, width: 0.5 } });
        s.addText(h, { x: x + 0.15, y: y + 0.12, w: 4.1, h: 0.35, fontSize: 12, bold: true, color: WHITE, fontFace: BODY_FONT });
        s.addText(d, { x: x + 0.15, y: y + 0.5, w: 4.1, h: 0.7, fontSize: 10, color: MGRAY, fontFace: BODY_FONT });
    });

    s.addText("Integration by Parts  ·  MAT 128  ·  Student Seminar", {
        x: 0.5, y: 5.25, w: 9, h: 0.25,
        fontSize: 9, color: GRAY3, fontFace: BODY_FONT, align: "center"
    });
    footer(s, "");
}

pres.writeFile({ fileName: "Integration_by_Parts.pptx" })
    .then(() => console.log("Done: Integration_by_Parts.pptx"))
    .catch(console.error);