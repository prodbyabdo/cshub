Add resources and wiki pages
No tasks in progress


# Minimal-Change Resources + Wiki Plan With Playlist Mapping

## Summary
Keep the current site structure intact. Do not redesign the homepage, do not introduce a new global shell, and do not rearrange the existing year-grid layout.

Implement only additive changes:

- add 2 new homepage cards in the existing card grid:
  - Resources
  - CS Wiki
- create the new pages behind them:
  - resources.html
  - cs-wiki.html
- scaffold a broad set of blank wiki topic/subtopic pages
- wire existing course pages to the relevant tutorial section inside resources.html
- ingest the provided public YouTube playlist and distribute its individual video links into the matching tutorial subcategories where they fit

The resources page should be organized into 2 top-level lanes:
- Videos
- PDFs

Under Videos, use subject-based subcategories tied to the site’s academic subjects. Under PDFs, keep matching subject sections with placeholder slots until you provide the actual PDF links.

## Key Changes
### Homepage
- Keep index.html visually and structurally the same.
- Preserve:
  - centered hero/title block
  - same card styling
  - same general spacing and page flow
- Only extend the existing grid by adding 2 more cards:
  - Resources
  - CS Wiki
- Do not add new explanatory sections, feature summaries, or architecture text.

### resources.html
- Build a standalone static page using the repo’s current visual language.
- Use the same simple page pattern as the existing standalone pages:
  - back link
  - page title
  - short subtitle
- Page structure:
  - intro
  - Videos
  - PDFs
  - optional short Course Mapping / Jump from Courses helper near the bottom
- Videos must be subdivided by subject/course-aligned categories, not just broad CS domains.
- Initial subject-based video sections should cover at least the current visible/future curriculum areas:
  - Computer Applications
  - Introduction to Computer Science
  - Principles of Programming
  - Discrete Mathematics
  - Introduction to Databases
  - Computer Architecture / Maintenance
  - Data Structures & Algorithms
  - Operating Systems
  - Networks
  - Software Engineering
  - AI / Cybersecurity / Specialization
- PDFs should mirror the same subject grouping where practical, but remain placeholder-first until real links are provided.
- Each video/PDF item should use a compact card/list style with:
  - title
  - optional short note
  - difficulty or type badge if useful
  - direct external link
- Add anchor IDs for each subject tutorial block so course pages can link directly into the correct section.

### Playlist ingestion and classification
- Use the provided public playlist URL as the first real video source to populate the resources page.
- Extract the individual video links from that playlist.
- Classify each video into the most relevant subject section in resources.html.
- Do not force every playlist item into the same bucket; distribute them by fit.
- If a playlist item is clearly web-development-specific and not aligned with an existing course title, place it under the closest subject area:
  - default target: Computer Applications or Principles of Programming
- If a video does not cleanly fit any current course/subject bucket, place it in a small fallback section such as:
  - General Web Development
  This fallback should live under Videos, not as a separate top-level page.
- Keep classification rules simple and practical:
  - exact subject fit first
  - nearest curriculum fit second
  - general web-dev fallback last
- Record these classification assumptions in comments only if needed for maintainability; do not surface them as visible explanatory text.

### Existing course-page link additions
- Make minimal edits to existing course pages only where they should link into the new tutorials page.
- Add a small hyperlink or button on relevant course pages pointing to the exact tutorial subsection in resources.html.
- This should be additive only; do not redesign those pages.
- Priority pages to link first:
  - year1.html for subject entry points where useful
  - year1sem1compapp.html
  - year1sem1introcs.html
  - year1sem2introdbms.html
- For subjects without a full course page yet, link from the Year 1 subject card if that is the least invasive insertion point.
- Link labels should be concise and user-facing, e.g. Tutorials, Video Tutorials, or See Tutorials.

### cs-wiki.html
- Build a standalone wiki landing page, not a full wiki app.
- Keep it lightweight and aligned to the repo’s current standalone-page style.
- Include:
  - short intro
  - Core CS Topics
  - Course Notes
  - Quick Revision
- Core topic cards should remain topic-driven and link out to blank stub pages.
- Keep this page informational and navigational, not content-heavy.

### Wiki scaffolding
- In addition to cs-wiki.html, scaffold blank topic and subtopic pages as far as practical from the current CS scope.
- Topic pages should exist for at least:
  - Programming
  - Algorithms
  - Data Structures
  - Computer Architecture
  - Operating Systems
  - Databases
  - Networks
  - Software Engineering
  - AI
  - Cybersecurity
  - Web Development
  - Discrete Mathematics
- Subtopic stub pages should be created under those topics where obvious and useful, such as:
  - Programming: variables, control flow, functions, data types, debugging
  - Algorithms: complexity, recursion, sorting, searching
  - Data Structures: arrays, linked lists, stacks, queues, trees, graphs, hash tables
  - Architecture: CPU, memory, buses, instruction cycle
  - Operating Systems: processes, threads, scheduling, memory management, file systems
  - Databases: SQL, ERD, normalization, indexing, transactions
  - Networks: OSI model, TCP/IP, subnetting, routing, switching
  - Software Engineering: SDLC, requirements, UML, testing, version control
  - AI: search, machine learning, neural networks
  - Cybersecurity: cryptography, authentication, network security
  - Web Development: HTML, CSS, JavaScript, HTTP, frontend/backend basics
  - Discrete Mathematics: logic, sets, relations, graphs, proofs
- All stub pages should stay intentionally blank/light:
  - title
  - short placeholder subtitle
  - empty section skeleton only
- No real educational content should be written into those stub pages yet.

## Test Plan
- Verify the homepage still feels like the original homepage, with only 2 extra cards added.
- Verify the new homepage cards open:
  - resources.html
  - cs-wiki.html
- Verify resources.html is split into:
  - Videos
  - PDFs
- Verify Videos is subdivided by subject/course-aligned sections.
- Verify extracted playlist videos are present as individual links in the correct subject sections.
- Verify relevant course pages contain direct links to the correct anchored tutorial subsection in resources.html.
- Verify wiki landing page links resolve to the blank topic/subtopic stubs.
- Verify mobile behavior:
  - homepage grid still works without feeling redesigned
  - resources filters and sections are usable on narrow screens
  - no horizontal overflow
  - buttons/links remain tappable
- Verify all pages remain plain static HTML/CSS/JS and GitHub Pages-safe.

## Assumptions
- The restored repo state is the source of truth, and the new implementation must preserve its current arrangement.
- “Do it again” means follow the original intent but with minimal layout disruption.
- The provided playlist is public and accessible enough to extract individual video links during implementation.
- Playlist items will not necessarily cover every subject; unmatched subjects should remain scaffolded with placeholders.
- Existing course pages should only receive small additive tutorial links, not layout rewrites.



(# Minimal-Change Resources + Wiki Plan With Context

## Context
This repo is a simple static GitHub Pages site in plain HTML/CSS with no backend, no build step, and no shared component system.

Current repo state:
- Homepage is the original centered 4-card grid in index.html linking to year1.html through year4.html.
- Existing live course/resource pages are mostly Year 1 pages such as:
  - year1sem1compapp.html
  - year1sem1introcs.html
  - year1sem2introdbms.html
  - year1sem2english.html
- year2.html, year3.html, and year4.html are still minimal “coming soon” style pages.
- The user explicitly rejected a previous attempt because it rearranged the homepage and overexplained the site. That was wrong.
- The correct constraint is: preserve the homepage arrangement and existing site feel; only add the new items and minimal supporting links/pages.
- The user wants to implement this in another chat, so this context must be treated as part of the spec.

User-confirmed constraints:
- Do not redesign the homepage.
- Only add the missing pieces rather than restructuring the site.
- Add 2 new homepage cards using the current card style:
  - Resources
  - CS Wiki
- Existing pages should receive only minimal additive changes.
- Wiki scaffolding should go beyond one sample page: create topic pages plus subtopic stub pages.
- A public YouTube playlist was provided:
  - Playlist URL
- The user wants the individual videos from that playlist extracted and distributed into the matching tutorial subject sections, not just linked as one playlist.
- The resources page should be split into 2 top-level parts:
  - Videos
  - PDFs
- Under Videos, sections should be grouped by subjects/course areas.
- Relevant existing course pages should link to the correct anchored tutorial section in resources.html.
- Mobile access should be lean and practical.

## Summary
Keep the original site structure intact and implement only additive changes:

- add 2 homepage cards in the existing grid:
  - Resources
  - CS Wiki
- create:
  - resources.html
  - cs-wiki.html
- scaffold a broad set of blank wiki topic/subtopic pages
- extract and classify individual video links from the supplied playlist into the correct subject sections in resources.html
- add small direct links from relevant existing course pages to the matching tutorial anchors in resources.html

## Key Changes
### Homepage
- Preserve index.html layout, spacing, hero, typography, and card styling.
- Do not add new sections, explanatory panels, maintainer-facing text, or architecture summaries.
- Extend only the existing grid by adding 2 cards:
  - Resources
  - CS Wiki
- Match the existing card pattern exactly:
  - icon block
  - title
  - short description
  - same hover behavior
- Keep the original 4 year cards intact.

### resources.html
- Build as a standalone static page in the current site’s dark/neon style.
- Use the same lightweight standalone-page pattern already seen in current pages:
  - back link
  - page title
  - subtitle
- Page structure:
  - intro
  - Videos
  - PDFs
  - optional short course-mapping helper section
- Videos must be grouped by subject/course-aligned sections.
- PDFs should mirror the same subject grouping where practical, but remain placeholder-first until real PDF links are available.
- Add anchor IDs for each subject section so existing course pages can deep-link to them.

Initial video/PDF subject sections should cover:
- Computer Applications
- Introduction to Computer Science
- Principles of Programming
- Discrete Mathematics
- Introduction to Databases
- Computer Architecture / Maintenance
- Data Structures & Algorithms
- Operating Systems
- Networks
- Software Engineering
- AI / Cybersecurity / Specialization
- General Web Development
  This is needed because the provided playlist seed video is web-development-focused and may not map cleanly to one current course title.

Each resource entry should include:
- title
- optional short note
- type/difficulty badge if useful
- direct external link

### Playlist extraction and classification
- Use the provided playlist URL as the first real data source for Videos.
- Extract individual video links from the playlist.
- Do not add only the playlist URL; add the individual videos.
- Classify each extracted video into the most relevant subject section.
- Classification rule order:
  1. direct subject fit
  2. closest curriculum fit
  3. General Web Development fallback
- If a video is about beginner web/programming foundations, it can reasonably map to:
  - Computer Applications
  - Principles of Programming
  - or General Web Development
  depending on title/content fit.
- Do not create visible explanation text about the classification logic for end users.

### Existing page link additions
- Make only small additive edits to relevant existing pages.
- Add concise links/buttons pointing to the correct anchored tutorial block in resources.html.
- Do not redesign those pages.

Priority targets:
- year1.html
- year1sem1compapp.html
- year1sem1introcs.html
- year1sem2introdbms.html

Preferred link labels:
- Tutorials
- Video Tutorials
- See Tutorials

### cs-wiki.html
- Build a standalone wiki landing page, not a wiki system/app.
- Keep it lightweight and navigational.
- Include:
  - short intro
  - Core CS Topics
  - Course Notes
  - Quick Revision
- Topic cards should link to blank topic/subtopic stub pages.
- Keep visible copy user-facing and concise.

### Wiki scaffolding
Create blank topic pages for at least:
- Programming
- Algorithms
- Data Structures
- Computer Architecture
- Operating Systems
- Databases
- Networks
- Software Engineering
- AI
- Cybersecurity
- Web Development
- Discrete Mathematics

Create blank subtopic pages for at least:
- Programming:
  - variables
  - control flow
  - functions
  - data types
  - debugging
- Algorithms:
  - complexity
  - recursion
  - sorting
  - searching
- Data Structures:
  - arrays
  - linked lists
  - stacks
  - queues
  - trees
  - graphs
  - hash tables
- Computer Architecture:
  - CPU
  - memory
  - buses
  - instruction cycle
- Operating Systems:
  - processes
  - threads
  - scheduling
  - memory management
  - file systems
- Databases:
  - SQL
  - ERD
  - normalization
  - indexing
  - transactions
- Networks:
  - OSI model
  - TCP/IP
  - subnetting
  - routing
  - switching
- Software Engineering:
  - SDLC
  - requirements
  - UML
  - testing
  - version control
- AI:
  - search
  - machine learning
  - neural networks
- Cybersecurity:
  - cryptography
  - authentication
  - network security
- Web Development:
  - HTML
  - CSS
  - JavaScript
  - HTTP
  - frontend/backend basics
- Discrete Mathematics:
  - logic
  - sets
  - relations
  - graphs
  - proofs

All stub pages should stay intentionally blank/light:
- title
- short placeholder subtitle
- empty section skeleton only
- no real educational content yet

## Test Plan
- Verify homepage still looks like the original page, with only 2 extra cards added.
- Verify new homepage cards open:
  - resources.html
  - cs-wiki.html
- Verify resources.html is split into:
  - Videos
  - PDFs
- Verify Videos is subdivided by subject/course-aligned sections.
- Verify individual video links from the supplied playlist appear in the correct sections.
- Verify relevant course pages contain direct links to the correct anchored tutorial subsection in resources.html.
- Verify cs-wiki.html links to blank topic and subtopic stubs.
- Verify mobile behavior:
  - homepage arrangement remains unchanged
  - new cards remain readable
  - resources filters/sections remain usable
  - no horizontal page overflow
  - links/buttons are tappable on narrow screens
- Verify all pages remain plain static HTML/CSS/JS and GitHub Pages-safe.

## Assumptions
- The restored original repo state is the source of truth.
- “Do it again” means follow the original intent with minimal disruption.
- The provided playlist is public enough to extract individual video links during implementation.
- Not every subject will have playlist coverage on day one; uncovered sections should remain scaffolded.
- Existing course pages should receive only small additive tutorial links, not rewrites.
 ) 
use the skills (
$build-web-apps:frontend-skill  Spec Miner ) but keep the rules in the prompts above 

Show less
4:01 PM


71 previous messages
Implemented the additive pass without changing the homepage structure. index.html now keeps the original layout and styling, with only two extra cards added for resources.html and cs-wiki.html.

resources.html is split into Videos and PDFs, uses anchored subject sections, and includes 24 individual links extracted from the provided playlist, distributed across the matching sections plus small fallback sections where needed. I also added minimal tutorial links from year1.html, year1sem1compapp.html, year1sem1introcs.html, and year1sem2introdbms.html to the correct anchors.

The wiki scaffold is in place under C:\Users\ben.arthur\Downloads\new backup\cshub-main\wiki\ with a shared stylesheet, 12 topic pages, and 56 subtopic stub pages. I verified local link resolution across the HTML files and checked the resource anchor targets. I did not run a live browser/mobile visual pass, so that part is still unverified.





4:29 PM
78 files changed
+2813
-10
Undo

index.html
year1.html
cs-wiki.html
resources.html
wiki.css
year1sem1compapp.html
year1sem1introcs.html
year1sem2introdbms.html
ai.html
algorithms.html
computer-architecture.html
cybersecurity.html
data-structures.html
databases.html
discrete-mathematics.html
networks.html
operating-systems.html
programming.html
software-engineering.html
web-development.html
complexity.html
recursion.html
searching.html
sorting.html
buses.html
cpu.html
instruction-cycle.html
memory.html
control-flow.html
data-types.html
debugging.html
functions.html
variables.html
arrays.html
graphs.html
hash-tables.html
linked-lists.html
queues.html
stacks.html
trees.html
erd.html
indexing.html
normalization.html
sql.html
transactions.html
file-systems.html
memory-management.html
processes.html
scheduling.html
threads.html
machine-learning.html
neural-networks.html
search.html
osi-model.html
routing.html
subnetting.html
switching.html
tcp-ip.html
requirements.html
sdlc.html
testing.html
uml.html
version-control.html
authentication.html
cryptography.html
network-security.html
graphs.html
logic.html
proofs.html
relations.html
sets.html
css.html
frontend-backend-basics.html
html.html
http.html
javascript.html
tcp-ip.html
frontend-backend-basics.html
no set layout that resembles wikipidea in any way, and for the resourse hub for pdfs and tutprial , mkae it only for videos, divided by semester and subject 
4:29 PM


18 previous messages
Updated resources.html to be videos-only. The PDF lane is removed, and the page is now grouped as Semester One, Semester Two, and Future Semesters, with subjects nested inside each semester. I kept the existing subject anchor IDs so the Year 1 tutorial links still work.

Updated cs-wiki.html and the shared wiki.css so the topic area reads like a visual topic hub rather than anything encyclopedia-like. The topic and subtopic stub pages inherit that new styling automatically.

I also verified that:

the old PDFs section is gone
the existing resources.html#... links still target real anchors
local HTML links still resolve
I did not run a browser/mobile visual pass, so if you want, I can do one more pass focused just on tightening the CS Wiki visuals further.





4:36 PM
3 files changed
+930
-0
Undo

cs-wiki.html
resources.html
wiki.css
we are studyuing intro to programming i added the lectures, make the normal page for year1sem2introprog.html same as other subjects, and make an exam, and a tab for java tuorials (links to relevant page in the youtube )
4:42 PM



You’re out of Codex messages
Your rate limit resets on Apr 28, 2026, 11:52 PM. To continue using Codex, upgrade to Plus today.
Upgrade








