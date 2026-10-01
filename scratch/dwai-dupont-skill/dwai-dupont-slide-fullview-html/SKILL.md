---
name: dwai-dupont-slide-fullview-html
description: Dwai's DuPont HTML slide deck: logo header, sliding numbered sidebar, Slide / Presentation / Full View modes, draggable slide controller, navy-red KPI cards and tables. Use when invoked by name or asked for such a deck.
---

# DuPont Slide / Presentation / Full-View Deck (HTML)

A single self-contained `.html` deck in the style of Dwai's "DuPont LeanIX Production Portfolio Analysis" deck and the LeanIX vs ServiceNow CMDB reconciliation deck built from it (Sep 2026). Every generated file must look and behave exactly like that deck: same header, sliding numbered left sidebar, ribbon, slide card, draggable controller, three view modes, palette, fonts, components and print rules.

## Non-negotiables

1. **One self-contained `.html` file.** All CSS in one `<style>`, all JS in one `<script>`. No CDN, no web fonts, no external images, no separate CSS/JS/helper/state files in the deliverable. It must open by double-click, offline.
2. **Use the CSS, JS and page skeleton in the appendices byte-for-byte.** Change only the placeholders and the slides. Class names, element ids, data attributes and `onclick` handlers are the JS contract - renaming any of them breaks navigation.
3. **Three view modes, always:** Slide Mode (default; sidebar + one slide + slide changer), Presentation (browser full-screen, the slide fills the whole screen edge to edge, no header, sidebar, ribbon or slide changer), Full View (every slide on one scrolling page with scroll-spy, no slide changer).
4. **The sliding sidebar is present in Slide Mode and Full View; the draggable slide changer appears in Slide Mode only.** Sidebar: search box, All / Management / Architect filter, chapter headers, numbered items with audience pills, active item in red, auto-scrolls to keep the active item visible. Controller: drag grip, Prev, "Slide X of N" with keyboard hint and red progress bar, Next, jump drop-down.
5. **Palette and type are fixed** (Appendix A `:root`): DuPont navy `#0B2E59` / `#061A33` / `#16437E`, DuPont red `#E52421` for accents, status colours green `#059669`, amber `#D97706`, red `#DC2626`, blue `#0284C7`, purple `#7C3AED`. Fonts: Calibri, Segoe UI, Arial; monospace Consolas. No Google Fonts, no emoji.
6. **Plain hyphens only** - never em or en dashes, anywhere, including SVG text. Grep for them before delivering; the count must be 0.
7. **Logo:** the DuPont logo is embedded as a base64 PNG in the header's white `logo-wrapper` (see "Logo" below). Never hotlink an image.
8. **Every number traceable.** KPI cards carry an evidence badge (`[A. Observed]` raw count, `[B. Derived]` computed, `[C. Estimated]` projection). Every slide can carry an `evidence-tag` naming its source.

## Workflow

1. Gather and verify the content first (data, analysis, figures). Plan chapters and slides (see "Deck structure").
2. Build the file from the skeleton (Appendix C) with the CSS (Appendix A) and JS (Appendix B) inlined. Fastest path: if this skill's folder has `scripts/build_deck.py` and `assets/`, import the helpers (`slide`, `kpi`, `kpi_grid`, `banner`, `table`, `register`, `feature`, `cols`, `box`, `alert`, `note`, `pill`, `diagram`, `stacked_bar`, `num`, `build`) and call `build(path, title, subtitle, deck_label, search_hint)`. Otherwise hand-assemble using the component snippets below. `assets/template.html` shows one of every component.
3. Name the file after the subject, e.g. `DuPont_<Subject>_Deck.html`. Save it next to the source material in the user's folder.
4. Run the QA checklist, render screenshots and look at them before delivering.

## Page anatomy

| Region | Element / class | Behaviour |
|---|---|---|
| Header | `header.deck-header` | Navy gradient, 2px red-tint bottom border. Left: white `logo-wrapper` with logo, `header-title-box` (h1 deck title + p subtitle: domain, snapshot, source, "Prepared by Dwaipayan Mojumder, date"). Right: `view-tabs` pill (Slide Mode / Presentation / Full View, active tab red with glow), `btn-header` Notes, Dark / Light, Export PDF |
| Sidebar | `aside.sidebar-nav` (320px) | Sticky `sidebar-search-box` with filter input + `aud-tabs` (All / Management / Architect). `ul#sidebarMenuList` built by JS: mono uppercase chapter headers, `sidebar-item` cards with navy `num-badge` (red when active) + audience pill (EXEC & TECH green, MGMT amber, ARCH red) + bold title. Hover slides the item 2px right |
| Stage | `main.presentation-stage#stage` | Scrolls independently. Contains `stage-ribbon` then all `section.slide-wrapper` slides |
| Ribbon | `.stage-ribbon` | Mono view pill (All grey, Management blue, Architect pink) + "num title (X of N)" + keyboard shortcut hints |
| Slide | `section.slide-wrapper` | White card, radius 10, large shadow. `slide-hero` (red `num-badge big` + red mono uppercase `slide-tag` kicker, `h2.slide-heading` navy 1.4rem "1.1 Title", `slide-description`, mono `evidence-tag`), then `slide-body` |
| Controller | `.frozen-bottom-controller#frozenPane` | Slide Mode only (hidden in Presentation and Full View). Fixed bottom-right, glassy navy, drag anywhere by the grip or body (buttons and select excluded), clamped to the viewport |
| Exit button | `.exit-present` | Only in Presentation mode, top-right, invisible until hovered |

## Slide data contract

```html
<section class="slide-wrapper" id="slide-1-1" data-num="1.1" data-chapter="Chapter 1: Executive Summary & Method"
  data-aud="exec" data-tag="Kicker text" data-title="Slide Title">
  <div class="slide-hero">
    <div class="hero-top"><span class="num-badge big">1.1</span><span class="slide-tag">Kicker text</span></div>
    <h2 class="slide-heading">1.1 Slide Title</h2>
    <p class="slide-description">One or two sentences: the finding, with the key number.</p>
    <span class="evidence-tag">Evidence base: source | query | date</span>
  </div>
  <div class="slide-body"> ...components... </div>
</section>
```

- `data-num`: `1.1`, `1.2`, `2.1`... by chapter; appendix slides `A.1`, `A.2`. The visible h2 repeats the number.
- `data-chapter`: identical string for every slide in a chapter - the sidebar prints a header whenever it changes.
- `data-aud`: `exec` (shows in every filter, pill "EXEC & TECH"), `mgmt` (Management), `arch` (Architect). Aim for a 6-8 slide Management track.
- `data-tag`: the red kicker; `data-title`: title without the number. Both are searched by the sidebar filter.
- No slide carries `show` in the source - the JS shows the first slide on load.

## View modes and controls (implemented in Appendix B)

- **Slide Mode**: one slide (`.show`) with fade-in; stage scrolls to top on every change.
- **Presentation**: `body.present-mode` + `html.present-root` (root font 17px); header, sidebar, ribbon and slide changer hidden; the slide fills the whole screen (no margin, border, radius or shadow; min-height 100vh); requests browser full-screen; navigate with the keyboard (Right / Left / Space / PgUp / PgDn / Home / End); Esc or leaving full-screen returns to Slide Mode.
- **Full View**: `body.full-mode`; every slide in the current track stacked; slide changer hidden; sidebar clicks and PgUp / PgDn smooth-scroll to a slide; scroll-spy updates ribbon and sidebar.
- **Filters**: audience buttons and the search box rebuild the track (sidebar, jump list, counter, progress); the current slide is kept if it survives the filter.
- **Keys**: Right / PgDn / Space next; Left / PgUp previous; Home / End; F toggles Presentation; Esc exits it; N toggles presenter notes. Keys are ignored while typing in the search box or the select.
- **Notes**: the Notes button (or N) shows or hides the `.presenter-note` speaker cues (`body.notes-on`). They are hidden by default so the audience never sees them; turn them on while rehearsing. If a deck has no presenter notes, leave the Notes button out.
- **Dark mode**: `body.dark-mode` swaps the neutral tokens; diagrams keep a light panel so SVG colours stay legible.
- **Print / Export PDF**: A4 landscape, one slide per page, every slide in the current track (so the Management filter prints the management deck); chrome hidden; registers print in full; colours preserved.

## Components (pick by content shape)

| Content | Component | Snippet |
|---|---|---|
| Headline / recommendation | Executive banner | `<div class="banner-executive"><div><span class="kicker">Headline</span><h3>One sentence</h3><p>Context.</p></div><div class="scope"><span>Scope</span><strong>1,383 x 8,969</strong></div></div>` |
| Headline numbers | KPI grid (3 or `.four` columns) | `<div class="kpi-grid"><div class="kpi t-red"><div class="kpi-head"><span class="kpi-lbl">Label</span><span class="badge-evidence badge-ev-derived">[B. Derived]</span></div><div class="kpi-val c-red">312 <small>(60%)</small></div><span class="kpi-desc">Context line</span></div></div>` - colours `navy blue amber green purple red` via `t-*` (top border) and `c-*` (value) |
| Parallel themes / options | Feature cards in `.three-col` / `.four-col` | `<div class="feature f-green"><div class="feature-head"><span class="feature-title"><span class="dot-num">1</span>Title</span><span class="count-chip">377 apps</span></div><p>Body.</p><div class="reality ok"><b>Use:</b> ...</div><div class="action"><b>Next:</b> ...</div></div>` - variants `f-red f-green f-amber f-purple f-navy` (default blue); `.reality` is a red left-strip note, `.reality.ok` green |
| Grouped prose / list | Box | `<div class="box"><div class="box-heading">Heading</div><ol><li><b>Lead.</b> text</li></ol></div>` |
| Side by side | `.two-col` | wrap two boxes, tables or a table + alert |
| Two-dimensional detail | Presentation table | `<table class="presentation-table"><thead><tr><th style="width:30%">Item</th><th class="r">Count</th></tr></thead><tbody><tr><td><b>Row</b></td><td class="r mono">1,234</td></tr></tbody></table>` - navy header with red underline, uppercase header text, fixed layout, set widths |
| Long record lists | Register | `<div class="table-container">` + presentation table - scrolls at 470px with a frozen header; optional inline `style="max-height:330px"` |
| Status | Pill | `<span class="status-pill status-danger">Zombie</span>` (`success warning danger info`) |
| Callouts | Alert | `<div class="alert-box alert-danger"><strong>Common error - label.</strong> text</div>` - `danger` (errors, corrections), `warning` (read-outs, watch-outs), `success` (controls), `info` (method notes, source status) |
| Speaker cue | Presenter note | `<div class="presenter-note"><b>Opening line</b>"First person, spoken cadence."</div>` - draft in Dwai's voice; tell the user to edit |
| Flow / structure / overlap | Diagram | `<div class="diagram"><svg viewBox="0 0 1120 H" ...>` (see SVG vocabulary) |
| Composition of a total | Stacked bar SVG | full-width bars + legend; green aligned, blue neutral, red defect, amber other |

## SVG vocabulary

- `viewBox="0 0 1120 H"`, `role="img"`, `aria-label`. Text via inline `style` or a `<style>` block: titles Calibri 15px bold `#0B2E59`, sub-lines 12.5px `#475569`, big numbers Consolas 26-38px bold in the status colour.
- Standard node: `fill #E0F2FE`, stroke `#0284C7` 1.5. Emphasis node (the one central element): `fill #0B2E59` + second rect `stroke #E52421` width 3, white text. Outcome / risk node: `fill #FEE4E2`, stroke `#E52421`. Card node: white with `#CBD5E1` stroke and a 5px left colour strip. Boundary / zone: `#F8FAFC` fill, `#94A3B8` dashed `8 6`, mono uppercase label.
- Arrows: navy `#0B2E59` markers for flow, red dashed for evidence or feedback. Unique marker ids per SVG.
- Never let text overflow its rect or cross a connector; check the largest y fits the viewBox.

## Deck structure

- Chapters: 1 Executive Summary & Method, 2-3 Findings, 4 Recommendation & Governance, Appendix (record-level registers, sources & provenance). Chapter strings go in `data-chapter`.
- 1.1 is always the title pattern: executive banner (headline + scope), 6 KPI cards, a two-column read-out, and an "Opening line" presenter note.
- A diagram slide early (flow, overlap or architecture), findings slides with KPI rows + tables + one alert, a position slide (four feature cards + recommendation banner), a backlog table (Priority pill P1 red / P2 amber / P3 blue, Action, Volume, Owner, Definition of done), a decisions + controls slide (Decision / Owner; Failure mode / Control / Trigger / Owner and effectiveness test / Response), then registers and sources.
- Separate fact from judgement: findings slides state what the data shows; the position slide carries the presenter's view.
- Names of decision owners are placeholders unless the user gave them - say so in a presenter note.

## Logo

Embed the DuPont logo as `data:image/png;base64,...` in `img.dupont-logo-img` (height 30px inside the white wrapper). Source, in order:
1. `assets/dupont-logo-base64.txt` in this skill's folder, if present.
2. Otherwise the user's `DuPont-Logo.jpg` (e.g. `portals/DuPont-Logo.jpg` in the Copilot_LeanIX_Production_Analysis folder): crop the white margin and downscale to 96px high:
   ```python
   from PIL import Image, ImageOps; import base64, io
   im = Image.open("DuPont-Logo.jpg").convert("RGB")
   bb = ImageOps.invert(im.convert("L")).point(lambda v: 255 if v > 30 else 0).getbbox()
   c = im.crop((bb[0]-20, bb[1]-20, bb[2]+20, bb[3]+20)); c = c.resize((int(c.width*96/c.height), 96), Image.LANCZOS)
   buf = io.BytesIO(); c.save(buf, "PNG", optimize=True); b64 = base64.b64encode(buf.getvalue()).decode()
   ```
3. If neither exists, ask the user for the logo file. Never redraw the logo or fetch it from the web.

## QA checklist - run before delivering

- [ ] Exactly one `<style>` and one `<script>`; `grep -o 'https\?://[^"]*'` returns only the SVG namespace; no `<link>`.
- [ ] Em / en dash count is 0.
- [ ] Every slide has `data-num`, `data-chapter`, `data-aud`, `data-tag`, `data-title`; ids unique; h2 number matches `data-num`.
- [ ] Render with Playwright at 1440x900: step through every slide with ArrowRight and screenshot each; no console errors; counter reads `Slide N of N` at the end; no horizontal overflow in `#stage`.
- [ ] Management filter shows the intended 6-8 slides; search filters the list.
- [ ] Slide changer visible in Slide Mode only; Full View shows every slide without it; Presentation fills the screen with no chrome or changer, arrows work and Esc returns to Slide Mode; dark mode legible; Notes toggle shows cues.
- [ ] Diagrams inspected on screenshot: no text overflow, no label crossing a line.
- [ ] Print to PDF (A4 landscape) gives one slide per page.

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1440,'height':900})
    errs = []; pg.on('pageerror', lambda ex: errs.append(str(ex)))
    pg.goto('file:///path/to/deck.html'); pg.wait_for_timeout(500)
    n = pg.evaluate("document.querySelectorAll('.slide-wrapper').length")
    for i in range(n):
        pg.screenshot(path=f's{i+1:02d}.png'); pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(350)
    print(pg.inner_text('#ctrlSlideCounter'), errs)
    pg.click('.view-btn[data-mode=full]'); pg.wait_for_timeout(500); pg.screenshot(path='full.png')
    pg.click('.view-btn[data-mode=present]'); pg.wait_for_timeout(500); pg.screenshot(path='present.png')
    pg.keyboard.press('Escape'); pg.click('text=Dark / Light'); pg.screenshot(path='dark.png')
    b.close()
```

## Appendix A - CSS (inline verbatim in the `<style>` block)

```css
:root{
  --dupont-navy:#0B2E59;--dupont-navy-dark:#061A33;--dupont-navy-light:#16437E;
  --dupont-red:#E52421;--dupont-red-soft:#FEE4E2;
  --success-green:#059669;--success-soft:#D1FAE5;--warning-amber:#D97706;--warning-soft:#FEF3C7;
  --danger-red:#DC2626;--danger-soft:#FEE2E2;--info-blue:#0284C7;--info-soft:#E0F2FE;--purple-ai:#7C3AED;--purple-soft:#EDE9FE;
  --bg-page:#F8FAFC;--bg-card:#FFFFFF;--bg-sidebar:#FFFFFF;--border-light:#CBD5E1;--border-dark:#94A3B8;
  --text-primary:#0F172A;--text-secondary:#334155;--text-muted:#475569;
  --shadow-sm:0 1px 3px rgba(0,0,0,.06),0 1px 2px rgba(0,0,0,.04);
  --shadow-md:0 4px 6px -1px rgba(0,0,0,.08),0 2px 4px -2px rgba(0,0,0,.04);
  --shadow-lg:0 12px 24px -4px rgba(11,46,89,.12),0 4px 6px -2px rgba(0,0,0,.05);
  --shadow-float:0 16px 36px -4px rgba(6,26,51,.32),0 6px 12px -2px rgba(6,26,51,.18);
  --radius-sm:6px;--radius-md:10px;--radius-lg:16px;--radius-full:9999px;
  --transition:all .22s cubic-bezier(.4,0,.2,1);
  --mono:Consolas,"Cascadia Mono","Courier New",monospace;
  --sans:Calibri,"Segoe UI",Arial,sans-serif;
}
body.dark-mode{
  --bg-page:#0A0F1D;--bg-card:#131E32;--bg-sidebar:#0E1726;--border-light:#2A3F60;--border-dark:#3B537E;
  --text-primary:#F1F5F9;--text-secondary:#CBD5E1;--text-muted:#94A3B8;--dupont-navy:#16437E;--dupont-navy-dark:#0A1324;
  --success-soft:rgba(5,150,105,.16);--warning-soft:rgba(217,119,6,.16);--danger-soft:rgba(220,38,38,.16);--info-soft:rgba(2,132,199,.16);--dupont-red-soft:rgba(229,36,33,.16)
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{font-family:var(--sans);background:var(--bg-page);color:var(--text-primary);line-height:1.5;height:100vh;display:flex;flex-direction:column;overflow:hidden;transition:background-color .3s,color .3s}

/* header */
header.deck-header{background:linear-gradient(135deg,var(--dupont-navy-dark) 0%,var(--dupont-navy) 100%);color:#fff;padding:.7rem 1.6rem;display:flex;align-items:center;justify-content:space-between;gap:1rem;position:sticky;top:0;z-index:1000;box-shadow:var(--shadow-md);border-bottom:2px solid rgba(229,36,33,.55);flex-wrap:wrap}
.header-left{display:flex;align-items:center;gap:1.1rem}
.logo-wrapper{background:#fff;padding:.3rem .6rem;border-radius:var(--radius-sm);display:flex;align-items:center;box-shadow:var(--shadow-sm)}
.dupont-logo-img{height:30px;width:auto;display:block}
.header-title-box h1{font-size:1.15rem;font-weight:700;color:#fff;letter-spacing:-.01em}
.header-title-box p{font-size:.76rem;color:#A9B8CC}
.header-right{display:flex;align-items:center;gap:.7rem;flex-wrap:wrap}
.view-tabs{background:rgba(11,46,89,.45);padding:.25rem;border-radius:var(--radius-full);display:flex;gap:.3rem;border:1px solid rgba(255,255,255,.25)}
.view-btn{background:transparent;border:none;color:#E2E8F0;padding:.4rem .95rem;font-size:.78rem;font-weight:700;border-radius:var(--radius-full);cursor:pointer;transition:all .2s;font-family:inherit}
.view-btn:hover{background:rgba(255,255,255,.15);color:#fff}
.view-btn.active{background:var(--dupont-red);color:#fff;box-shadow:0 0 10px rgba(229,36,33,.5)}
.btn-header{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.22);color:#fff;padding:.42rem .85rem;font-size:.76rem;font-weight:600;border-radius:var(--radius-sm);cursor:pointer;transition:var(--transition);font-family:inherit}
.btn-header:hover{background:rgba(255,255,255,.24)}
.btn-header.on{background:rgba(229,36,33,.85);border-color:var(--dupont-red)}

/* layout */
.app-body-layout{display:grid;grid-template-columns:320px 1fr;flex:1 1 auto;min-height:0;overflow:hidden}
.app-body-layout>*{min-height:0}
aside.sidebar-nav{position:relative;background:var(--bg-sidebar);border-right:1px solid var(--border-light);display:flex;flex-direction:column;overflow-y:auto;z-index:50}
.sidebar-search-box{padding:.85rem 1rem;border-bottom:1px solid var(--border-light);background:var(--bg-card);position:sticky;top:0;z-index:10;display:flex;flex-direction:column;gap:.55rem}
.sidebar-search-box input{width:100%;padding:.5rem .85rem;border-radius:var(--radius-sm);border:1px solid var(--border-light);background:var(--bg-page);color:var(--text-primary);font-size:.8rem;font-family:inherit;outline:none}
.sidebar-search-box input:focus{border-color:var(--info-blue);box-shadow:0 0 0 2px rgba(2,132,199,.15)}
.aud-tabs{display:flex;gap:.3rem}
.aud-btn{flex:1;background:var(--bg-page);border:1px solid var(--border-light);color:var(--text-secondary);font-size:.7rem;font-weight:700;padding:.32rem .2rem;border-radius:var(--radius-sm);cursor:pointer;font-family:inherit}
.aud-btn.active{background:var(--dupont-navy);color:#fff;border-color:var(--dupont-navy)}
.sidebar-menu{list-style:none;padding:.7rem;display:flex;flex-direction:column;gap:.4rem}
.sidebar-category-header{font-family:var(--mono);font-size:.68rem;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:.08em;padding:.6rem .5rem .2rem}
.sidebar-item{padding:.65rem .8rem;border-radius:var(--radius-md);cursor:pointer;border:1px solid transparent;transition:var(--transition);display:flex;flex-direction:column;gap:.25rem;background:var(--bg-card)}
.sidebar-item:hover{background:var(--bg-page);border-color:var(--border-light);transform:translateX(2px)}
.sidebar-item.active{background:rgba(11,46,89,.08);border-color:var(--dupont-navy-light);box-shadow:var(--shadow-sm)}
body.dark-mode .sidebar-item.active{background:rgba(2,132,199,.16);border-color:var(--info-blue)}
.sidebar-item-header{display:flex;align-items:center;justify-content:space-between}
.num-badge{font-family:var(--mono);font-size:.75rem;font-weight:800;color:#fff;background:#0B2E59;padding:.2rem .55rem;border-radius:4px;border:1px solid #2A5A9E;letter-spacing:.04em;display:inline-block;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.sidebar-item.active .num-badge,.slide-wrapper .num-badge.big{background:var(--dupont-red);border-color:#FFA5A3;box-shadow:0 0 8px rgba(229,36,33,.4)}
.sidebar-item-title{font-size:.88rem;font-weight:700;color:var(--text-primary);line-height:1.25}

/* stage */
main.presentation-stage{overflow-y:auto;padding:1.4rem 2rem 7rem;display:flex;flex-direction:column;gap:1.2rem;background:var(--bg-page)}
.stage-ribbon{background:var(--bg-card);border:1px solid var(--border-light);border-radius:var(--radius-md);padding:.7rem 1.2rem;display:flex;align-items:center;justify-content:space-between;gap:1rem;box-shadow:var(--shadow-sm);flex-wrap:wrap}
.ribbon-meta{display:flex;align-items:center;gap:.8rem;font-size:.84rem}
.pill-badge{font-family:var(--mono);font-size:.68rem;font-weight:700;padding:.2rem .55rem;border-radius:var(--radius-full);text-transform:uppercase}
.pill-all{background:#F3F4F6;color:#374151;border:1px solid #E5E7EB}
.pill-mgmt{background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE}
.pill-arch{background:#FDF2F8;color:#BE185D;border:1px solid #FBCFE8}
body.dark-mode .pill-all{background:#1E293B;color:#CBD5E1;border-color:#334155}
body.dark-mode .pill-mgmt{background:rgba(29,78,216,.2);color:#93C5FD;border-color:rgba(147,197,253,.3)}
body.dark-mode .pill-arch{background:rgba(190,24,93,.2);color:#F472B6;border-color:rgba(244,114,182,.3)}
.kbd-hint{font-family:var(--mono);font-size:.68rem;color:#94A3B8;background:rgba(148,163,184,.14);padding:.15rem .35rem;border-radius:4px}

/* slides */
.slide-wrapper{background:var(--bg-card);border:1px solid var(--border-light);border-radius:var(--radius-md);padding:1.35rem 1.75rem 1.6rem;box-shadow:var(--shadow-lg);display:none;flex-direction:column;gap:.9rem;position:relative;scroll-margin-top:1rem}
.slide-wrapper.show{display:flex;animation:slideIn .25s ease-out}
body.full-mode .slide-wrapper.in-track{display:flex;animation:none}
@keyframes slideIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.slide-hero{border-bottom:2px solid var(--border-light);padding-bottom:.75rem;display:flex;flex-direction:column;gap:.3rem}
.hero-top{display:flex;align-items:center;gap:.6rem;margin-bottom:.3rem}
.num-badge.big{font-size:.85rem;padding:.25rem .65rem}
.slide-tag{font-family:var(--mono);font-size:.74rem;font-weight:700;color:var(--dupont-red);letter-spacing:.08em;text-transform:uppercase}
.slide-heading{font-size:1.4rem;font-weight:800;color:var(--dupont-navy);line-height:1.18}
body.dark-mode .slide-heading{color:#fff}
.slide-description{font-size:.86rem;color:var(--text-secondary);font-weight:500;line-height:1.45;max-width:1150px}
.evidence-tag{display:inline-flex;align-items:center;gap:.35rem;font-family:var(--mono);font-size:.7rem;color:#475569;background:#F1F5F9;border:1px solid #CBD5E1;padding:.2rem .55rem;border-radius:var(--radius-sm);margin-top:.3rem;width:fit-content}
body.dark-mode .evidence-tag{background:#1E293B;border-color:#334155;color:#94A3B8}
.slide-body{display:flex;flex-direction:column;gap:1rem}

/* executive banner */
.banner-executive{background:linear-gradient(135deg,#0B2E59 0%,#16437E 100%);color:#fff;padding:1rem 1.25rem;border-radius:8px;border-left:5px solid var(--dupont-red);box-shadow:0 4px 12px rgba(0,0,0,.15);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:.75rem}
.banner-executive .kicker{background:var(--dupont-red);color:#fff;font-family:var(--mono);font-size:.7rem;padding:.15rem .55rem;border-radius:4px;font-weight:800;letter-spacing:.05em;text-transform:uppercase}
.banner-executive h3{font-size:1.12rem;font-weight:800;margin:.35rem 0 .15rem;color:#fff}
.banner-executive p{font-size:.82rem;color:#E2E8F0;max-width:860px;line-height:1.45}
.banner-executive .scope{text-align:right}
.banner-executive .scope span{display:block;font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;color:#CBD5E1;font-weight:700}
.banner-executive .scope strong{font-family:var(--mono);font-size:1.35rem;font-weight:800;color:#fff}

/* kpi cards */
.kpi-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:.75rem}
.kpi-grid.four{grid-template-columns:repeat(4,1fr)}
.kpi{background:var(--bg-card);padding:.85rem 1rem;border-radius:8px;border:1px solid var(--border-light);border-top:3px solid var(--dupont-navy);display:flex;flex-direction:column;justify-content:space-between;gap:.15rem;transition:var(--transition)}
.kpi:hover{transform:translateY(-2px);box-shadow:var(--shadow-md)}
.kpi-head{display:flex;justify-content:space-between;align-items:center;gap:.4rem}
.kpi-lbl{font-size:.72rem;text-transform:uppercase;color:var(--text-secondary);font-weight:800;letter-spacing:.05em}
.kpi-val{font-family:var(--mono);font-size:1.65rem;font-weight:800;color:var(--dupont-navy);margin:.15rem 0}
body.dark-mode .kpi-val.c-navy{color:#93C5FD}
.kpi-val small{font-size:.95rem}
.kpi-desc{font-size:.76rem;color:var(--text-secondary);font-weight:600}
.t-navy{border-top-color:#0B2E59}.t-blue{border-top-color:#0284C7}.t-amber{border-top-color:#D97706}.t-green{border-top-color:#059669}.t-purple{border-top-color:#7C3AED}.t-red{border-top-color:#DC2626}
.c-navy{color:#0B2E59}.c-blue{color:#0284C7}.c-amber{color:#D97706}.c-green{color:#059669}.c-purple{color:#7C3AED}.c-red{color:#DC2626}
.badge-evidence{display:inline-flex;align-items:center;font-family:var(--mono);font-size:.66rem;font-weight:700;padding:.15rem .45rem;border-radius:4px;letter-spacing:.03em;white-space:nowrap}
.badge-ev-observed{background:#0B2E59;color:#fff;border:1px solid #1E4E8C}
.badge-ev-derived{background:#1E3A8A;color:#BFDBFE;border:1px solid #3B82F6}
.badge-ev-estimated{background:#78350F;color:#FDE68A;border:1px solid #D97706}

/* layout helpers */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1.1rem;align-items:start}
.three-col{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
.four-col{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem}
.box{background:var(--bg-page);border:1px solid var(--border-light);border-radius:var(--radius-md);padding:1.1rem 1.2rem;display:flex;flex-direction:column;gap:.6rem}
.box-heading{font-size:1rem;font-weight:800;color:var(--text-primary);display:flex;align-items:center;gap:.5rem}
.box p,.box li{font-size:.84rem;color:var(--text-secondary);line-height:1.5}
.box ul,.box ol{padding-left:1.1rem;display:flex;flex-direction:column;gap:.3rem}
.feature{background:var(--bg-card);border:1px solid var(--border-light);border-top:4px solid var(--info-blue);border-radius:var(--radius-md);padding:1rem 1.1rem;display:flex;flex-direction:column;gap:.5rem;transition:var(--transition)}
.feature:hover{transform:translateY(-2px);box-shadow:var(--shadow-md);border-color:var(--dupont-navy-light)}
.feature.f-red{border-top-color:#DC2626}.feature.f-green{border-top-color:#059669}.feature.f-amber{border-top-color:#D97706}.feature.f-purple{border-top-color:#7C3AED}.feature.f-navy{border-top-color:#0B2E59}
.feature-head{display:flex;align-items:center;justify-content:space-between;gap:.5rem}
.feature-title{font-size:.98rem;font-weight:800;color:var(--text-primary);display:flex;align-items:center;gap:.5rem}
.dot-num{width:22px;height:22px;border-radius:50%;background:var(--info-blue);color:#fff;font-size:.72rem;font-weight:800;display:inline-flex;align-items:center;justify-content:center;flex:none}
.f-red .dot-num{background:#DC2626}.f-green .dot-num{background:#059669}.f-amber .dot-num{background:#D97706}.f-purple .dot-num{background:#7C3AED}.f-navy .dot-num{background:#0B2E59}
.count-chip{font-family:var(--mono);font-size:.72rem;font-weight:800;background:#0B2E59;color:#fff;padding:.18rem .5rem;border-radius:4px;white-space:nowrap}
.feature p{font-size:.83rem;color:var(--text-secondary);line-height:1.5}
.reality{background:var(--bg-page);border-left:3px solid #DC2626;padding:.5rem .7rem;border-radius:0 6px 6px 0;font-size:.8rem;color:var(--text-secondary)}
.reality b{color:#DC2626}
.reality.ok{border-left-color:#059669}.reality.ok b{color:#059669}
.action{border-top:1px dashed var(--border-light);padding-top:.5rem;font-size:.8rem;color:var(--text-secondary)}
.action b{color:var(--text-primary)}

/* alerts */
.alert-box{border-radius:var(--radius-md);padding:.9rem 1.1rem;font-size:.86rem;line-height:1.5}
.alert-box strong{font-weight:800}
.alert-danger{background:var(--danger-soft);color:#991B1B;border-left:4px solid var(--danger-red)}
.alert-warning{background:var(--warning-soft);color:#92400E;border-left:4px solid var(--warning-amber)}
.alert-success{background:var(--success-soft);color:#065F46;border-left:4px solid var(--success-green)}
.alert-info{background:var(--info-soft);color:#075985;border-left:4px solid var(--info-blue)}
body.dark-mode .alert-danger{color:#FCA5A5}body.dark-mode .alert-warning{color:#FCD34D}body.dark-mode .alert-success{color:#6EE7B7}body.dark-mode .alert-info{color:#7DD3FC}

/* presenter notes */
.presenter-note{display:none;background:var(--bg-page);border:1px dashed var(--border-dark);border-left:4px solid var(--dupont-navy);border-radius:var(--radius-md);padding:.7rem 1rem;font-size:.84rem;color:var(--text-secondary);font-style:italic}
.presenter-note b{display:block;font-style:normal;font-family:var(--mono);font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;color:var(--dupont-red);margin-bottom:.2rem}
body.notes-on .presenter-note{display:block}

/* tables */
table.presentation-table{width:100%;border-collapse:separate;border-spacing:0;font-size:.82rem;text-align:left;border-radius:8px;overflow:hidden;border:1px solid var(--border-light);box-shadow:var(--shadow-sm);table-layout:fixed}
table.presentation-table th{background:#0B2E59;color:#fff;font-weight:800;padding:.7rem .9rem;border-bottom:2px solid var(--dupont-red);text-transform:uppercase;font-size:.72rem;letter-spacing:.06em}
table.presentation-table td{padding:.62rem .9rem;border-bottom:1px solid var(--border-light);color:var(--text-primary);background:var(--bg-card);vertical-align:top;word-wrap:break-word}
table.presentation-table tr:nth-child(even) td{background:rgba(11,46,89,.025)}
table.presentation-table tr:last-child td{border-bottom:none}
table.presentation-table tr:hover td{background:rgba(2,132,199,.07)}
body.dark-mode table.presentation-table tr:nth-child(even) td{background:#18263E}
body.dark-mode table.presentation-table tr:hover td{background:#203354}
td.r,th.r{text-align:right}
td.mono{font-family:var(--mono);font-weight:700}
.status-pill{display:inline-flex;align-items:center;font-size:.7rem;font-weight:800;padding:.14rem .5rem;border-radius:var(--radius-full);white-space:nowrap}
.status-danger{background:var(--danger-soft);color:var(--danger-red)}
.status-warning{background:var(--warning-soft);color:var(--warning-amber)}
.status-success{background:var(--success-soft);color:var(--success-green)}
.status-info{background:var(--info-soft);color:var(--info-blue)}

/* scrollable registers with frozen headers */
.table-container{overflow:auto;position:relative;border:1px solid var(--border-light);border-radius:8px;box-shadow:var(--shadow-sm);max-height:470px;scrollbar-width:thin;scrollbar-color:#0B2E59 var(--bg-page)}
.table-container table.presentation-table{border:none;border-radius:0;box-shadow:none;margin:0}
.table-container thead th{position:sticky;top:0;z-index:5;border-bottom:3px solid var(--dupont-red);box-shadow:0 4px 6px -1px rgba(0,0,0,.35)}
.table-container td{font-size:.78rem;padding:.42rem .7rem}
.reg-meta{display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;font-size:.78rem;color:var(--text-secondary)}

/* diagrams */
.diagram{background:var(--bg-card);border:1px solid var(--border-light);border-radius:var(--radius-md);padding:.6rem;box-shadow:var(--shadow-sm)}
.diagram svg{width:100%;height:auto;display:block}
body.dark-mode .diagram{background:#F8FAFC}
.fig-note{font-size:.78rem;color:var(--text-muted)}

/* controller */
.frozen-bottom-controller{position:fixed;bottom:22px;right:24px;z-index:9999;background:rgba(6,26,51,.94);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.22);border-radius:var(--radius-lg);padding:.6rem .9rem;display:flex;align-items:center;gap:.7rem;box-shadow:var(--shadow-float);color:#fff;cursor:grab;user-select:none;touch-action:none;transition:border-color .2s,box-shadow .2s,opacity .3s}
.frozen-bottom-controller:hover{border-color:rgba(255,255,255,.42)}
.drag-handle-grip{color:rgba(255,255,255,.45);font-size:1.1rem;letter-spacing:-2px;cursor:grab;padding:0 .15rem}
.drag-handle-grip:hover{color:#fff}
.controller-nav-btn{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.22);color:#fff;padding:.45rem .85rem;border-radius:var(--radius-sm);font-size:.82rem;font-weight:700;cursor:pointer;transition:var(--transition);font-family:inherit}
.controller-nav-btn:hover:not(:disabled){background:var(--dupont-red);border-color:var(--dupont-red)}
.controller-nav-btn:disabled{opacity:.35;cursor:not-allowed}
.controller-info{display:flex;flex-direction:column;gap:.2rem;min-width:140px}
.controller-slide-text{font-size:.85rem;font-weight:700;color:#fff;display:flex;align-items:center;gap:.4rem}
.controller-progress-bar{width:100%;height:4px;background:rgba(255,255,255,.2);border-radius:var(--radius-full);overflow:hidden}
.controller-progress-fill{height:100%;background:var(--dupont-red);width:0;transition:width .25s}
.controller-select{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25);color:#fff;padding:.42rem .7rem;border-radius:var(--radius-sm);font-size:.76rem;font-family:inherit;font-weight:600;cursor:pointer;outline:none;max-width:230px}
.controller-select option{background:#061A33;color:#fff}

/* presentation mode */
body.present-mode header.deck-header,body.present-mode aside.sidebar-nav,body.present-mode .stage-ribbon{display:none}
body.present-mode .app-body-layout{grid-template-columns:1fr}
html.present-root{font-size:17px}
body.present-mode main.presentation-stage{padding:0;gap:0;background:var(--bg-card)}
body.present-mode .slide-wrapper{max-width:none;width:100%;min-height:100vh;margin:0;border:none;border-radius:0;box-shadow:none;padding:2.2rem 3rem 2.4rem}
body.present-mode .frozen-bottom-controller,body.full-mode .frozen-bottom-controller{display:none}
.exit-present{display:none;position:fixed;top:10px;right:14px;z-index:9999;background:rgba(6,26,51,.85);color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:var(--radius-sm);padding:.35rem .75rem;font-size:.75rem;font-weight:700;cursor:pointer;opacity:0;transition:opacity .2s;font-family:inherit}
.exit-present:hover,.exit-present:focus{opacity:.95}
body.present-mode .exit-present{display:block}

@media(max-width:1180px){.kpi-grid.four,.four-col{grid-template-columns:repeat(2,1fr)}}
@media(max-width:1024px){.app-body-layout{grid-template-columns:1fr}aside.sidebar-nav{display:none}.two-col,.three-col,.kpi-grid{grid-template-columns:1fr 1fr}}
@media(max-width:720px){.two-col,.three-col,.kpi-grid,.kpi-grid.four,.four-col{grid-template-columns:1fr}}

@media print{
  html,body{height:auto}
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  body{overflow:visible;display:block;background:#fff}
  header.deck-header,.frozen-bottom-controller,.stage-ribbon,aside.sidebar-nav,.exit-present{display:none!important}
  .app-body-layout{display:block;height:auto;overflow:visible}
  main.presentation-stage{overflow:visible;padding:0;background:#fff}
  .slide-wrapper.in-track{display:flex!important;page-break-after:always;break-after:page;box-shadow:none;border:1px solid #CBD5E1;margin-bottom:1rem;zoom:1}
  .table-container{max-height:none;overflow:visible}
  .table-container thead{display:table-header-group}
  tr{break-inside:avoid}
  @page{size:A4 landscape;margin:10mm}
}
```

## Appendix B - JavaScript (inline verbatim in the `<script>` block)

`AUDLABEL.all` reads `data-deck-label` from `<body>`; set it to the deck's name, e.g. "Complete Reconciliation Deck".

```javascript
(function(){
"use strict";
var slides=Array.prototype.slice.call(document.querySelectorAll('.slide-wrapper'));
var mode='slide', aud='all', track=[], cur=0;
var AUDLABEL={all:(document.body.dataset.deckLabel||'Complete Deck'),mgmt:'Management View',arch:"Architect's View"};
function audOk(s){if(aud==='all')return true;var a=s.dataset.aud;return a==='exec'||a===aud;}
function searchOk(s){var q=(document.getElementById('sidebarSearch').value||'').toLowerCase().trim();if(!q)return true;return (s.dataset.num+' '+s.dataset.title+' '+s.dataset.tag+' '+s.dataset.chapter).toLowerCase().indexOf(q)>-1;}
function rebuild(){
  track=slides.filter(function(s){return audOk(s)&&searchOk(s);});
  slides.forEach(function(s){s.classList.toggle('in-track',track.indexOf(s)>-1);});
  var sel=document.getElementById('ctrlJumpSelect');sel.innerHTML='';
  track.forEach(function(s,i){var o=document.createElement('option');o.value=i;o.textContent=s.dataset.num+' '+s.dataset.title;sel.appendChild(o);});
  renderSidebar();
}
function pill(a){if(a==='mgmt')return '<span class="status-pill status-warning">MGMT</span>';if(a==='arch')return '<span class="status-pill status-danger">ARCH</span>';return '<span class="status-pill status-success">EXEC &amp; TECH</span>';}
function renderSidebar(){
  var ul=document.getElementById('sidebarMenuList');ul.innerHTML='';var last='';
  track.forEach(function(s,i){
    if(s.dataset.chapter!==last){var h=document.createElement('li');h.className='sidebar-category-header';h.textContent=s.dataset.chapter;ul.appendChild(h);last=s.dataset.chapter;}
    var li=document.createElement('li');li.className='sidebar-item'+(i===cur?' active':'');li.tabIndex=0;li.setAttribute('role','button');
    li.innerHTML='<div class="sidebar-item-header"><span class="num-badge">'+s.dataset.num+'</span>'+pill(s.dataset.aud)+'</div><span class="sidebar-item-title">'+s.dataset.title+'</span>';
    li.onclick=function(){go(i,true);};li.onkeydown=function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();go(i,true);}};
    ul.appendChild(li);
  });
}
function updateChrome(){
  var n=track.length, s=track[cur];
  document.getElementById('ctrlSlideCounter').textContent=n?('Slide '+(cur+1)+' of '+n):'No slides';
  document.getElementById('ctrlProgressBar').style.width=(n?Math.round((cur+1)/n*100):0)+'%';
  document.getElementById('ctrlPrevBtn').disabled=cur<=0;
  document.getElementById('ctrlNextBtn').disabled=cur>=n-1;
  document.getElementById('ctrlJumpSelect').value=cur;
  document.getElementById('ribbonSlideTitle').textContent=s?(s.dataset.num+' '+s.dataset.title+' ('+(cur+1)+' of '+n+')'):'';
  var p=document.getElementById('ribbonViewPill');p.className='pill-badge pill-'+aud;p.textContent=AUDLABEL[aud]+' ('+n+' slides)';
  document.querySelectorAll('#sidebarMenuList .sidebar-item').forEach(function(li,i){li.classList.toggle('active',i===cur);if(i===cur){var sb=document.querySelector('aside.sidebar-nav');var lt=li.offsetTop, lb=lt+li.offsetHeight;if(lt<sb.scrollTop+90||lb>sb.scrollTop+sb.clientHeight-10){sb.scrollTop=Math.max(0,lt-sb.clientHeight/3);}}});
}
function go(i,fromNav){
  if(!track.length)return;
  cur=Math.max(0,Math.min(i,track.length-1));
  var stage=document.getElementById('stage');
  if(mode==='full'){
    if(fromNav!==false){lockSpy=true;track[cur].scrollIntoView({behavior:'smooth',block:'start'});setTimeout(function(){lockSpy=false;},700);}
  }else{
    slides.forEach(function(s){s.classList.remove('show');});
    track[cur].classList.add('show');stage.scrollTop=0;document.documentElement.scrollTop=0;document.body.scrollTop=0;
  }
  updateChrome();
}
window.stepSlide=function(d){go(cur+d,true);};
window.jumpToSlide=function(v){go(parseInt(v,10),true);};
window.setAudience=function(a){
  var keep=track[cur];aud=a;
  document.querySelectorAll('.aud-btn').forEach(function(b){b.classList.toggle('active',b.dataset.aud===a);});
  rebuild();var k=track.indexOf(keep);go(k>-1?k:0,true);
};
window.filterSidebarSlides=function(){var keep=track[cur];rebuild();var k=track.indexOf(keep);go(k>-1?k:0,true);};
function setTabs(){document.querySelectorAll('.view-btn').forEach(function(b){b.classList.toggle('active',b.dataset.mode===mode);});}
window.setMode=function(m){
  if(m==='present'){enterPresent();return;}
  if(mode==='present'){exitFs();}
  mode=m;document.body.classList.remove('present-mode');document.documentElement.classList.remove('present-root');
  document.body.classList.toggle('full-mode',m==='full');
  slides.forEach(function(s){s.classList.remove('show');});
  setTabs();
  if(m==='full'){setTimeout(function(){go(cur,true);},30);}else{go(cur,false);}
};
function enterPresent(){
  mode='present';document.body.classList.remove('full-mode');document.body.classList.add('present-mode');document.documentElement.classList.add('present-root');setTabs();go(cur,false);
  var el=document.documentElement;
  try{if(el.requestFullscreen&&!document.fullscreenElement){el.requestFullscreen().catch(function(){});}}catch(e){}
}
function exitFs(){try{if(document.fullscreenElement&&document.exitFullscreen){document.exitFullscreen().catch(function(){});}}catch(e){}}
window.exitPresent=function(){setMode('slide');};
document.addEventListener('fullscreenchange',function(){if(!document.fullscreenElement&&mode==='present'){setMode('slide');}});
window.toggleDarkMode=function(){document.body.classList.toggle('dark-mode');};
window.toggleNotes=function(){var on=document.body.classList.toggle('notes-on');document.getElementById('btnNotes').classList.toggle('on',on);};
/* scroll spy for full view */
var lockSpy=false;
document.getElementById('stage').addEventListener('scroll',function(){
  if(mode!=='full'||lockSpy)return;
  var st=this.getBoundingClientRect().top, best=0;
  track.forEach(function(s,i){if(s.getBoundingClientRect().top-st<160)best=i;});
  if(best!==cur){cur=best;updateChrome();}
},{passive:true});
document.addEventListener('keydown',function(e){
  var t=e.target.tagName;if(t==='INPUT'||t==='SELECT'||t==='TEXTAREA')return;
  if(e.key==='ArrowRight'||e.key==='PageDown'||(e.key===' '&&mode!=='full')){e.preventDefault();stepSlide(1);}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();stepSlide(-1);}
  else if(e.key==='Home'){e.preventDefault();go(0,true);}
  else if(e.key==='End'){e.preventDefault();go(track.length-1,true);}
  else if(e.key==='f'||e.key==='F'){e.preventDefault();if(mode==='present')setMode('slide');else setMode('present');}
  else if(e.key==='Escape'&&mode==='present'){setMode('slide');}
  else if(e.key==='n'||e.key==='N'){toggleNotes();}
});
window.addEventListener('beforeprint',function(){document.body.classList.add('printing');});
/* draggable controller */
(function(){
  var pane=document.getElementById('frozenPane');var drag=false,sx,sy,il,it;
  pane.addEventListener('pointerdown',function(e){
    if(e.target.closest('button')||e.target.closest('select'))return;
    drag=true;sx=e.clientX;sy=e.clientY;var r=pane.getBoundingClientRect();il=r.left;it=r.top;
    pane.style.bottom='auto';pane.style.right='auto';pane.style.left=il+'px';pane.style.top=it+'px';pane.style.cursor='grabbing';
    document.addEventListener('pointermove',mv);document.addEventListener('pointerup',up);
  });
  function mv(e){if(!drag)return;var nl=il+e.clientX-sx,nt=it+e.clientY-sy;
    nl=Math.max(10,Math.min(nl,window.innerWidth-pane.offsetWidth-10));nt=Math.max(10,Math.min(nt,window.innerHeight-pane.offsetHeight-10));
    pane.style.left=nl+'px';pane.style.top=nt+'px';}
  function up(){drag=false;pane.style.cursor='grab';document.removeEventListener('pointermove',mv);document.removeEventListener('pointerup',up);}
})();
rebuild();go(0,false);
})();
```

## Appendix C - Page skeleton

Replace `{{CSS}}`, `{{JS}}`, `{{LOGO_BASE64}}`, `{{DECK_TITLE}}`, `{{DECK_LABEL}}`, the subtitle, the search hint and `{{SLIDES}}` (the concatenated `section.slide-wrapper` blocks). Nothing else changes.

```html
<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{DECK_TITLE}}</title>
<style>{{CSS}}</style></head>
<body data-deck-label="{{DECK_LABEL}}">
<header class="deck-header">
 <div class="header-left"><div class="logo-wrapper"><img src="data:image/png;base64,{{LOGO_BASE64}}" alt="DuPont" class="dupont-logo-img"></div>
 <div class="header-title-box"><h1>{{DECK_TITLE}}</h1><p>{{SUBTITLE - domain | data snapshot | source | Prepared by Dwaipayan Mojumder, DD Mon YYYY}}</p></div></div>
 <div class="header-right">
  <div class="view-tabs" role="tablist" aria-label="View mode">
   <button class="view-btn active" data-mode="slide" onclick="setMode('slide')" title="One slide at a time with navigation sidebar">Slide Mode</button>
   <button class="view-btn" data-mode="present" onclick="setMode('present')" title="Full-screen presentation (F). Esc to exit">Presentation</button>
   <button class="view-btn" data-mode="full" onclick="setMode('full')" title="All slides on one scrolling page">Full View</button>
  </div>
  <button class="btn-header" id="btnNotes" onclick="toggleNotes()" title="Show presenter notes (N)">Notes</button>
  <button class="btn-header" onclick="toggleDarkMode()">Dark / Light</button>
  <button class="btn-header" onclick="window.print()">Export PDF</button>
 </div>
</header>
<div class="app-body-layout">
 <aside class="sidebar-nav">
  <div class="sidebar-search-box">
   <input type="text" id="sidebarSearch" placeholder="Filter slides (e.g. {{three keywords}})..." oninput="filterSidebarSlides()">
   <div class="aud-tabs"><button class="aud-btn active" data-aud="all" onclick="setAudience('all')">All</button><button class="aud-btn" data-aud="mgmt" onclick="setAudience('mgmt')">Management</button><button class="aud-btn" data-aud="arch" onclick="setAudience('arch')">Architect</button></div>
  </div>
  <ul class="sidebar-menu" id="sidebarMenuList"></ul>
 </aside>
 <main class="presentation-stage" id="stage">
  <div class="stage-ribbon"><div class="ribbon-meta"><span id="ribbonViewPill" class="pill-badge pill-all">{{DECK_LABEL}}</span><span style="color:var(--text-muted)">|</span><span id="ribbonSlideTitle" style="font-weight:700;color:var(--text-primary)"></span></div>
  <div style="font-size:.8rem;color:var(--text-secondary)">Shortcuts: <span class="kbd-hint">&#9664; / &#9654;</span> <span class="kbd-hint">PgUp / PgDn</span> <span class="kbd-hint">F</span> present <span class="kbd-hint">N</span> notes</div></div>
{{SLIDES}}
 </main>
</div>
<button class="exit-present" onclick="exitPresent()">Exit presentation (Esc)</button>
<div class="frozen-bottom-controller" id="frozenPane" title="Drag to reposition">
 <div class="drag-handle-grip">&#8942;&#8942;</div>
 <button class="controller-nav-btn" id="ctrlPrevBtn" onclick="stepSlide(-1)">&#9664; Prev</button>
 <div class="controller-info"><div class="controller-slide-text"><span id="ctrlSlideCounter">Slide 1</span><span class="kbd-hint">[&larr; / &rarr;]</span></div><div class="controller-progress-bar"><div class="controller-progress-fill" id="ctrlProgressBar"></div></div></div>
 <button class="controller-nav-btn" id="ctrlNextBtn" onclick="stepSlide(1)">Next &#9654;</button>
 <select class="controller-select" id="ctrlJumpSelect" onchange="jumpToSlide(this.value)"></select>
</div>
<script>{{JS}}</script>
</body></html>
```
