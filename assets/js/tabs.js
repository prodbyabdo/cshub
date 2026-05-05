/**
 * CS Hub — Tab System
 * 
 * Shared tab-switching logic used on subject content pages.
 * Each page has .tab-btn buttons and .tab-content panels.
 * 
 * Usage:
 *   <button class="tab-btn active" onclick="openTab('summary', this)">Summary</button>
 *   <div id="summary" class="tab-content active">...</div>
 */
function openTab(tabId, btn) {
    // Hide all tab content
    document.querySelectorAll('.tab-content').forEach(function (tc) {
        tc.classList.remove('active');
    });

    // Deactivate all tab buttons
    document.querySelectorAll('.tab-btn').forEach(function (tb) {
        tb.classList.remove('active');
    });

    // Activate the target tab
    var target = document.getElementById(tabId);
    if (target) {
        target.classList.add('active');
    }

    // Activate the clicked button (if provided)
    if (btn) {
        btn.classList.add('active');
    } else {
        // If no button passed (called programmatically), find the matching one
        document.querySelectorAll('.tab-btn').forEach(function (tb) {
            var onclick = tb.getAttribute('onclick') || '';
            if (onclick.indexOf("'" + tabId + "'") !== -1) {
                tb.classList.add('active');
            }
        });
    }
}

/**
 * Print helpers for subject pages with tab-based content.
 */
function printFullPdf() {
    document.body.setAttribute('data-print-mode', 'full');
    window.print();
    document.body.removeAttribute('data-print-mode');
    document.body.removeAttribute('data-print-tab');
}

function printCurrentTab(tabId) {
    document.body.setAttribute('data-print-mode', 'tab');
    document.body.setAttribute('data-print-tab', tabId);
    window.print();
    document.body.removeAttribute('data-print-mode');
    document.body.removeAttribute('data-print-tab');
}
