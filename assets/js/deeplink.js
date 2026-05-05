/**
 * CS Hub — Deep-Linking Script
 * 
 * Handles URL hash navigation:
 * 1. Decodes hash → finds target element
 * 2. If element is inside an inactive tab, opens that tab first
 * 3. Smooth-scrolls to the element
 * 
 * Fires on DOMContentLoaded and on hashchange events.
 * 
 * Dependencies: Expects openTab(tabId, btn?) to exist on pages with tabs.
 */
(function () {
    function handleHash() {
        var hash = window.location.hash;
        if (!hash) return;

        var targetId = decodeURIComponent(hash.substring(1));
        var el = document.getElementById(targetId);
        if (!el) return;

        // If the element is inside an inactive tab, open that tab first
        var tabContent = el.closest ? el.closest('.tab-content') : null;
        if (!tabContent) {
            var parent = el.parentElement;
            while (parent) {
                if (parent.classList && parent.classList.contains('tab-content')) {
                    tabContent = parent;
                    break;
                }
                parent = parent.parentElement;
            }
        }

        if (tabContent && !tabContent.classList.contains('active')) {
            if (typeof openTab === 'function') {
                openTab(tabContent.id);
            }
        }

        // Scroll with slight delay to allow tab CSS transition
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
