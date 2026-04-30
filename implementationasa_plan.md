# Implementation Plan - Resources Library Landing State & Search

The goal is to transform `resources.html` into a "search-first" experience. Upon opening, users will see a prominent search bar and a grid of categories. The detailed sidebar and specific resource sections will only be revealed once a user interacts with a category or video.

## User Review Required

> [!IMPORTANT]
> The search bar will allow users to quickly find any video across all 13+ categories. I will implement a "landing mode" that hides the complexity of the library until needed.

## Proposed Changes

### [resources.html](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/resources.html)

#### [MODIFY] CSS Styles
-   Add `.is-landing` state styles for `body`.
-   Hide `.sidebar` and `.mobile-bottom-nav` when in landing mode.
-   Create styles for `#landing-view`:
    -   Centered hero section for search.
    -   Modern grid layout for category cards with SVG icons.
-   Add search results dropdown styling.

#### [MODIFY] HTML Structure
-   Add `<div id="landing-view">` inside `<main class="content">`.
-   Populate it with a search input and a `.category-grid`.
-   Wrap existing library content in a way that it can be toggled.

#### [MODIFY] JavaScript Logic
-   **Landing State**: Default the page to "landing mode" (`body.classList.add('is-landing')`).
-   **Search Engine**:
    -   A script to crawl all `.resource-card` elements on page load to build a search index.
    -   Live filtering as the user types.
-   **Navigation**:
    -   Update `showSection` to exit landing mode.
    -   Handle search result clicks (navigate to section + scroll to video).
-   **Back Navigation**: (Optional but recommended) A way to return to the search landing view.

## Verification Plan

### Manual Verification
-   Open `resources.html` and verify the sidebar is hidden and the search landing is visible.
-   Type in the search bar and verify results appear.
-   Click a category and verify the sidebar appears and the section is displayed.
-   Select a video from search results and verify it navigates to the correct section and highlights the video.
-   Test mobile responsiveness of the landing grid.
