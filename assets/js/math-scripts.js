(function () {
  function renderMath() {
    if (window.MathJax && typeof window.MathJax.typesetPromise === "function") {
      return window.MathJax.typesetPromise();
    }

    if (window.MathJax && typeof window.MathJax.typeset === "function") {
      window.MathJax.typeset();
    }

    return Promise.resolve();
  }

  window.renderMath = renderMath;

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      renderMath().catch(function () {
        // Leave the page usable even if MathJax is unavailable.
      });
    }, { once: true });
    return;
  }

  renderMath().catch(function () {
    // Leave the page usable even if MathJax is unavailable.
  });
})();
