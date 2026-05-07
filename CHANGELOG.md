# iRemedy Website v8 — Change Log

**Project:** `iremedy-website-v9`
**Live:** https://antp23.github.io/iremedy-website-v9/
**Local:** `/Users/berniemac/projects/iremedy-website-v9/index.html`
**Repo:** github.com/antp23/iremedy-website-v9 (gh-pages branch)

Use these `CHG-XXX` numbers to reference specific states when picking up work across sessions (WhatsApp, web, etc.).

---

## Active State

**Current:** CHG-045 — Platform page: text size enforcement
**Date:** 2026-05-07

---

## Change History




### CHG-045 — Platform page: text size enforcement
**Date:** 2026-05-07
**Commit:** `b0cda39`
- Hero credential strip: 12px → 14px
- All teal card titles (16 cards, Sec 02/04/05/06): 12px → 16px bold
- Architecture Layer 01-04 prefix labels: 10.4px → 12px
- Layer 03 Sources sub-label: 10.4px → 12px
- Jim Harding Co-Inventor label: 11.2px → 14px

---
### CHG-044 — TradeSpy page: text size enforcement
**Date:** 2026-05-07
**Commit:** `25f0efd`
- **CSS class changes (ts-* classes — TradeSpy page only):**
  - ts-hero-sub credential strip: 12.8px → 14px
  - ts-stat-l stat labels: 8.3px → 12px
  - ts-sec-title all section headlines: clamp min 25.6px → 28px
  - ts-body all body paragraphs: 15.2px → 16px
  - ts-badge visibility warning: 12px → 14px
  - ts-callout body: 14.1px → 16px
  - ts-callout-label: 12.8px → 14px
  - ts-list li: 14.1px → 15px
  - ts-rm-status roadmap badges: 12px → 13px
  - ts-rm-item: 14.1px → 15px
  - ts-cta-sub: 15.2px → 16px
  - ts-cta-footer: 12.8px → 13px
- **SVG pipeline diagram text:** all 5 labels bumped to font-size 13
- **Inline:** 3 fraud capability card titles: 12.8px → 14px bold

---
### CHG-043 — Government page: photo opacity + text size enforcement
**Date:** 2026-05-07
**Commit:** `45db8ab`
- **FIX 1 — Photo:** pharmaceutical-shelf.jpg opacity 0.22 → 0.45, brightness override 0.4 — visible as atmospheric backdrop
- **FIX 2 — Text sizes (Government page only):**
  - Hero credential strip: 12px → 14px
  - Exposure stat labels (4): 11.2px → 12px
  - TradeSpy stat labels (4): 11.2px → 12px
  - Consequence card titles (4): 12px → 16px bold
  - Fraud card titles (6): 12px → 16px bold
  - TradeSpy capability titles (6): 12px → 16px bold
  - Cost comparison column headers: 11.2px → 14px
  - Cost bar items (9): 12px → 14px
  - Cost footer labels (2): 11.2px → 14px
  - Insight callout label: 11.2px → 14px
  - Portfolio column titles (2): 12px → 18px bold
  - Proof block titles (3): 12px → 18px bold (serif)
  - Manufacturer card names (3): 17.6px → 18px
  - Capability card titles (6): 12px → 16px bold

---
### CHG-042 — Photography + Homepage Cleanup + Fixes
**Date:** 2026-05-06
- **PART 1:** Added global CSS photo treatment classes: `.photo-duotone-hero`, `.photo-duotone-container`, `.photo-bw-hero`, `.headshot-bw`, `.nav-wordmark`
- **PART 2 (Placements 1,2,4,5):** Images added to assets/images/ (warehouse-overhead.jpg, warehouse-dramatic.jpg, container-ship.jpg)
  - Homepage hero: warehouse-dramatic.jpg as duotone hero background
  - TradeSpy Doctrine section: container-ship.jpg as duotone hero background
  - Manufacturers hero: warehouse-overhead.jpg as B&W hero background
  - About hero: warehouse-dramatic.jpg as B&W hero background (object-position: center 40%)
  - Placement 3 (Government Exposure stats): PENDING — awaiting government_exposure.jpg (pharmaceutical shelf)
- **PART 3:** All leadership/board headshots → `headshot-bw` class (16 images)
- **PART 4A:** Nav logo PNG → styled text wordmark `✚iRemedy` (serif, teal cross)
- **PART 4B:** iRemedy cross SVG added above homepage hero headline (80×80px, teal)
- **PART 4C:** Anthony Paquin title → "Chief AI Officer" everywhere (Manufacturers CTA, About, Contact, board section)
- **PART 4:** Footer logo PNG → matching text wordmark
- **PART 5:** Legacy pages already non-routable (page-legacy-* pattern not accessible via showPage or nav)
- **PART 6:** TradeSpy "Built by Operators" patent count: "fifteen patents" → "10 granted U.S. patents"

---

### CHG-031 — Nav dropdown hover fix
**Date:** 2026-05-06
**Commit:** `05cc927`
- Closed gap between nav button and dropdown (top: calc(100%+2px) → top: 100% + padding-top: 4px)
- Dropdowns now stay open when cursor moves from button into menu items

---

### CHG-030 — Board of Directors headshots
**Date:** 2026-05-06
**Commit:** `9d1c231`
- 5 headshots added to assets/: leslie-bernhard, kelly-mccarthy, obie-mckenzie, gary-paquin, tomas-philipson (all .webp)
- Board cards updated from initials placeholders to real circular photos
- Saul Factor still pending

---

### CHG-029 — Board of Directors bios updated
**Date:** 2026-05-06
**Commit:** `5c5b789`
- All 5 director bios updated with final copy from Anthony

---

### CHG-027 — Company pages redesign
**Date:** 2026-05-06
**Commit:** `8636478`
- Nav: Mission + Media removed; About & Leadership + Newsroom added to Company dropdown
- About page: merged Mission + Leadership; hero, company facts, 3 exec bios, 6 board cards, 3 advisor slots, 2007–2026 timeline, CTA
- Contact page: full Formspree form (name/email/phone/org/title/type/topic/message), contact sidebar, quick links
- Newsroom: 3 featured cards, podcast callout, press releases, Tony's books, media contact
- showPage() routing updated for 'about' and 'newsroom'

---

### CHG-026 — Platform page full build
**Date:** 2026-05-06
**Commit:** `8662efc`
- 9 sections: hero, MetaCommerceRx overview, 4-layer architecture diagram, patent portfolio + Jim Harding callout, For Manufacturers, For Buyers, TradeSpy callout, FAQ (6 Qs), CTA

---

### CHG-025 — Fraud detection supplement
**Date:** 2026-05-06
**Commit:** `f3f429b`
- Gov hero subheadline updated with fraud framing
- New Section 02B on Government page: 6 fraud-type cards + closing callout
- TradeSpy fraud framing paragraph added to Section 03
- MIA fraud prevention paragraph added to Section 04
- Homepage FAQ: fraud detection Q added (8th item)

---

### CHG-024 — Government page full redesign
**Date:** 2026-05-06
**Commit:** `da5306d`
- Replaced 2-column placeholder with full 9-section capability brief
- Section 01: Hero — dark bg, headline, italic subheadline, credential strip, two CTAs (TradeSpy Briefing + MIA Portfolio)
- Section 02: The Exposure — body copy + 4 stat blocks (80% API overseas / 100K+ jobs lost / 300+ shortages / <10% inspected) + 4 red consequence cards
- Section 03: TradeSpy — dark bg, 4 stat blocks (129,140 NDCs / 412 CCP flags / 89 Hormuz critical / 24/7), 6 capability blocks (COO verification, CCP mapping, geopolitical risk, domestic alternatives, OMB M-25-22, legislative intel)
- Section 04: Made in America — reshoring economics argument, cost-stack waterfall visual (foreign 6-layer vs. iRemedy 3-layer), insight callout block
- Section 05: The Portfolio (id=gov-mia) — friction-vs-solution two-column layout, scroll anchor from hero CTA
- Section 06: Track Record — OWS prose + dark 3-column proof bar (OWS / Senate / White House OMB) + 3 domestic manufacturer cards (Oxford / GLVUS / Speranza)
- Section 07: Capabilities — 6-card grid
- Section 08: FAQ — 6 accordion Q&As (toggleFaq added)
- Section 09: CTA — dark centered, two action buttons + tony@iremedy.com

---

### CHG-023 — Leadership page headshots + full board populated
**Date:** 2026-05-05
**Commit:** `d0fa1ee`
- Tony Paquin: real headshot added (assets/tony-paquin.jpg)
- Anthony Paquin: real headshot added (assets/anthony-paquin.jpg)
- Board of Directors: all 6 slots populated
  - Leslie Bernhard: Director, Chair Nexalin (Nasdaq), former Revlon/Disney
  - Kelly McCarthy: Director, CEO InfusionCapital, pediatric practice owner
  - Obie McKenzie: Director, Vice Chair Cordiant Capital, former BlackRock MD
  - Gary Paquin: Director, co-founder iRemedy & Agency One, Stanford/Harvard certified
  - Dr. Tomas Philipson: Director, former White House CEA Chair, health economist
  - Saul Factor: Director, name + title only (photo + bio pending)

---

### CHG-022 — Leadership page executive tile updates
**Date:** 2026-05-05
**Commit:** `3c0849e`
- Tony Paquin: title → "Founder & Chief Executive Officer"; bio updated to short-form
- Anthony Paquin: title → "Chief AI Officer"; bio updated to short-form
- Amanda Somsy: title unchanged (CFO); bio updated to CMA-certified short-form; PHOTO PENDING SVG replaced with real headshot (assets/amanda-somsy.jpg)

---

### CHG-021 — Fraud detection supplement (partial)
**Date:** 2026-05-05
**Commit:** `c8f8b88`
- TradeSpy page: New `// Fraud Detection` section inserted between OMB M-25-22 and Built By Operators — headline, 3-paragraph body copy, 3-card grid (Counterfeit & Origin / Quality & Documentation / Pricing & Intermediary)
- Homepage FAQ: Added 8th question "How does iRemedy help detect supply chain fraud?" — previous last item got border-bottom added
- DEFERRED (needs government page redesign prompt first): Govt hero subheadline update, new Section 02B (6-card fraud section), Section 03 TradeSpy fraud framing paragraph, Section 04 Made in America fraud prevention paragraph

---

### CHG-020 — Pharmacies page full redesign
**Date:** 2026-05-05
**Commit:** `860c052`
- Replaced thin 2-section placeholder with full 11-section pharmacy-specific page
- Section 01: Hero — dark bg, headline, italic subheadline, extended proof strip (Green List + UPS Healthcare Cold Chain), Request Pricing + API Catalog anchor CTAs
- Section 02: Sourcing Problem — two-col, compounding crisis framing + independent pharmacy framing, callout block
- Section 03: API Catalog — 3-col 6-card product grid; GLP-1 card has teal top border + "HIGH DEMAND" badge; all 6 categories with molecules listed
- Section 04: FDA-Credentialed Supply — dark bg, two-col copy, 4 credential blocks (FDA-Registered / Green List / Importer of Record / CoA & Lot Docs), CTA
- Section 05: Cold Chain — bg-3, two-col with 3 stat blocks (−20°C treatment)
- Section 06: Built For — 3-col 6-segment grid (503A, 503B, independent, specialty/mail-order, vet, IV/wellness)
- Section 07: MetaCommerceRx — two-col, 5 arrow-list features, demo CTA
- Section 08: Peptide Hub Teaser — left teal border accent, two-col, peptides.iremedy.com "coming soon" callout card, two CTAs
- Section 09: Transparent Pricing — two-col, no minimums / no lock-in framing
- Section 10: FAQ — 7 pharmacy-specific Q&As (GLP-1, credentialing, cold chain, volume minimums, distributor vs broker, controlled substances, peptides subdomain)
- Section 11: CTA — dark bg, 48-hour sourcing plan promise, compounding@iremedy.com

---

### CHG-019 — Providers page full redesign
**Date:** 2026-05-05
**Commit:** `fe4f90a`
- Replaced thin 2-section placeholder with full 10-section procurement-brief page
- Section 01: Hero — dark bg, headline, italic subheadline, proof strip, Request Pricing + See What We Distribute CTAs
- Section 02: The Problem — two-col, GPO layer critique, callout (no rebate games / no hidden markups / no lock-in)
- Section 03: iRemedy Direct — two-col 6-feature cap-list (transparent pricing, direct sourcing, full range, DSCSA, no GPO, COO transparency)
- Section 04: Built For — 7-segment 3-col grid (hospitals, ASCs, 503A, 503B, independents, clinics, government)
- Section 05: The Platform — dark bg, two-col, MetaCommerceRx body + 5 bullet features, Request a Demo CTA
- Section 06: The GPO Question — strategic parallel-channel framing, callout pull-quote
- Section 07: Fulfillment — bg-3, two-col with 3 stat blocks (18M+ sqft / 1–2 day / full cold chain)
- Section 08: Trusted By — 500M units / Senate / 10 patents, 4-logo placeholder bar, testimonial placeholder
- Section 09: FAQ — 7 provider-specific accordion Q&As
- Section 10: CTA — dark bg, “See the pricing for yourself” + sales@iremedy.com

---

### CHG-018 — Manufacturers page international supplement
**Date:** 2026-05-05
**Commit:** `e45e3b0`
- Section 02 (The Gap): Added distinct international framing paragraph (FDA registration, DEA, state licensing, customs complexity for foreign manufacturers)
- Section 03 (Incubator card): Added credibility bridge callout block between bullet list and pricing line
- Section 06 (Built For): Expanded international manufacturers tile to include China, India, Europe, Latin America specificity
- New Section 06B (International Market Entry): Full dedicated section with headline, 2-col 6-feature cap-list, closing italic line, CTA; styled with `bg-3` background + left teal border accent

---

### CHG-017 — Manufacturers page full redesign
**Date:** 2026-05-05
**Commit:** `0a15d50`
- Replaced thin 2-section placeholder with full 10-section conversion page
- Section 01: Hero — dark bg, headline, italic subheadline, proof strip, two CTAs (Get Started + See the Incubator anchor)
- Section 02: The Gap — two-col body copy, callout "iRemedy closes that gap"
- Section 03: Two Paths — Incubator card (full stack, pricing callout $5K–$15K) + DaaS card, side-by-side
- Section 04: Infrastructure — dark bg, 4 stat blocks (18M+ sqft / 95% / 200+ / 24/7), supporting copy
- Section 05: MetaCommerceRx — two-col with 5 numbered cap-list features, demo CTA
- Section 06: Built For — two-col, 6 client type tiles in 2×3 grid
- Section 07: Social Proof — 3-col client grid (Spectrum Medical, GLVUS, FlexGRIP, CathCare, Speranza + "your company here"), testimonial placeholder
- Section 08: Process — 5-step cap-list + timeline callout card (2–6 weeks)
- Section 09: FAQ — 7 manufacturer-specific accordion Q&As
- Section 10: CTA — dark bg, full-width, Get Started + Anthony contact line

---

### CHG-016 — Nav and footer logo replacement
**Date:** 2026-05-05
**Commit:** `56c589a`
- Replaced text "iREMEDY.com" in nav with `iRemedy_Logo_wo_Slogan.png` (36px tall, links to home)
- Replaced text "iREMEDY HEALTHCARE COMPANIES" in footer with same logo (28px tall)
- Both logo files added to `assets/`: `iRemedy_Logo_wo_Slogan.png`, `iRemedy_Logo_White_Text.png`

---

### CHG-015 — Global type scale polish pass
**Date:** 2026-05-05
**Commit:** `cf960ab`
- Panel headline reduced: `clamp(3rem,6.5vw,7rem)` → `clamp(2.5rem,5vw,4.5rem)`
- Body text enforced at 1rem minimum: `.sec-body`, `.cap-body`, `.blist li`, `.callout p`, `.p-text`
- Footer: links → 0.875rem, address → 0.8rem, col headers → 0.8rem, tagline → 0.875rem
- Stats: label → 0.75rem, sub → 0.875rem
- Buttons: 0.65rem → 0.875rem
- Cert badges: 0.52rem → 0.8rem, padding increased
- Eyebrow / panel-eyebrow labels: 0.58rem → 0.8rem
- Hero: max-width 90vw constraint, headline margin-bottom 2.5rem, credential strip → 0.8rem
- Routing cards: body text → 1rem, CTA links → 0.8rem
- Card 3: link updated to Government page, CTA → "See Government Solutions →"
- FAQ: expanded to full content width (removed max-width:820px)
- FAQ questions: 1.05rem → 1.125rem (all 7); answers: 0.9rem → 1rem (all 7)
- Trusted By credential line: 0.56rem → 0.8rem
- Footer: Supply Side Podcast link added below address

---

### CHG-014 — Homepage full redesign
**Date:** 2026-05-05
**Commit:** `5550bed`
- Section 01: New hero — routing cards (Manufacturers / Providers & Pharmacies / Government & Policy), static credential line, ticker moved below cards
- Section 02: "What We Do" — direct distribution copy, hub-spoke SVG, proof line callout
- Section 03A: Technology — MetaCommerceRx, "Patent-protected AI. Running in production.", terminal widget
- Section 03B: TradeSpy dark callout — `#212E3E` background, 3 stat cards (129,140 / 412 / 89)
- Section 04: Trusted By — logo bar (UPS + 4 placeholders), testimonial placeholder cards
- Section 05: Stats updated — `129,140 NDCs Monitored` replaces `<10% Domestic API Mfg.`
- Section 06: FAQ accordion — 7 Q&A pairs

---

### CHG-013 — Add Government nav item and audience page
**Date:** 2026-05-05
**Commit:** `2736c1d`
- New nav item: Manufacturers · Providers · Pharmacies · **Government** · Platform · TradeSpy · Company
- New page `#page-government`: federal distribution + TradeSpy COO callout
- Government added to footer Markets column

---

### CHG-012 — Information architecture restructure
**Date:** 2026-05-05
**Commit:** `1fb68ff`
- Nav rebuilt: Manufacturers · Providers · Pharmacies · Platform · TradeSpy · Company | Login · Get Started
- "Solutions" dropdown removed entirely
- "Engage" → "Get Started" (accent blue button)
- New Platform placeholder page (`#page-platform`): MetaCommerceRx + 10-patent chips
- TradeSpy elevated to top-level nav
- Legacy pages archived: `page-legacy-direct`, `page-legacy-technology`, `page-legacy-logistics`, `page-legacy-incubator` (HTML preserved, removed from routing)
- Footer: Solutions → Platform (MetaCommerceRx + TradeSpy); Services → Markets
- Homepage CTAs relinked: Smart Distribution → Providers ("Learn More →"); Platform → Platform page

---

### CHG-011 — Brand color palette update
**Date:** 2026-05-05
**Commit:** `2024f58`
- `--teal` → `#0064A5` (Medium Persian Blue — primary headings/links)
- `--cerulean: #00ACE6` added (Vivid Cerulean — hover states, badges)
- `--ink` → `#212E3E` (Imperial Primer — body text + hero bg)
- `--ink-2` → `#3D4D5E`
- `--hero-bg` → `#212E3E`
- All inline SVG hex codes updated to match
- `btn-teal:hover` → cerulean

---

### CHG-010 — Media page: press releases section
**Date:** 2026-05-04
**Commit:** `8e18572`
- 20 press releases from iremedy.com/news added below media tiles
- Real dates, titles, URLs, category tags (newest → oldest: Feb 2026 → 2023)

---

### CHG-009 — Media page: Supply Side Podcast tile
**Date:** 2026-05-04
**Commit:** `a1c42be`
- Replaced Operation Warp Speed tile with The Supply Side Podcast tile

---

### CHG-008 — Mission page: "(and then everything)" parenthetical
**Date:** 2026-05-04
**Commit:** `eeb3b59`
- Added "(and then everything)" after "healthcare supply chain." in hero headline

---

### CHG-007 — Leadership page redesign
**Date:** 2026-05-04
**Commits:** `6f038ca`, `a414715`
- 3-section layout: Executive Team (Tony, Anthony, Amanda) + 6 board placeholders + Special Advisors (Murray, Willem)
- 4-column grid, 90px avatar silhouettes ("PHOTO PENDING")

---

### CHG-006 — Smart Distribution SVG & layout
**Date:** 2026-05-04
**Commits:** `1d0fb52`, `2ef87e9`, `fcbcc03`
- Animated hub-and-spoke SVG added (iRemedy Direct → 6 endpoints)
- SVG max-width 850px, column ratio 1.6:1
- Homepage reordered: Smart Distribution (02) before Platform (03)

---

### CHG-005 — TradeSpy page redesign
**Date:** 2026-05-04
**Commits:** `6b91285`, `842273a`
- Light background replacing dark intel-briefing aesthetic
- American flag SVG in hero
- Animated pipeline SVG (ORCHESTRATOR → FIELD/SCORING AGENTS → RECONCILER)
- Full content sections: Three Layers, Architecture, Live Today, Federal Governance, CTA

---

### CHG-004 — Homepage hero update
**Date:** 2026-05-04
**Commits:** `565e0cb`, `d1c448b`, `3463e7d`
- Headline: "AI Distribution. / Smarter supply. Better care."
- Platform section headline and description expanded
- Panel 3 (The Network) and Panel 4 (The Position) removed — homepage now 3 panels

---

### CHG-003 — Nav: audience items to top nav
**Date:** 2026-05-04
**Commits:** `a153f99`, `a4dcf6e`
- Manufacturers, Providers, Pharmacies moved to top-level nav
- Nav font size increased 0.6rem → 0.9rem

---

### CHG-002 — v8 initial build
**Date:** 2026-05-03 (approx)
**Commit:** `56d8e49`
- Dark editorial design, credibility strip, stats strip
- Homepage panels: Mission, Platform, Network, Position
- Incubator promoted, audience subpages scaffolded

---

### CHG-001 — v8 project created
**Date:** 2026-05-03 (approx)
**Commit:** `56d8e49`
- Repo created: github.com/antp23/iremedy-website-v8
- gh-pages branch, single-file HTML SPA
- Base design system: Playfair Display + IBM Plex Mono + Inter, cream/dark palette

---

## Pending / Known TODOs

- Leadership board: 6 director names, bios, photos needed
- All executive headshots: "PHOTO PENDING" throughout
- Testimonials (Section 04): 2 real quotes needed
- Logo bar (Section 04): 4 client logos needed
- Trusted By / Logo placeholders: [Client Logo 2–5]
- Platform page: full MetaCommerceRx content pass needed
- Chloride RV Park: Formspree endpoint needs real account before going external
