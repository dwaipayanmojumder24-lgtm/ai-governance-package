"""
Builder helpers for the dwai-dupont-slide-fullview-html deck.

Usage (from any Python script):
    import sys; sys.path.insert(0, "<skill>/scripts")
    from build_deck import *
    slide("1.1", "Chapter 1: Executive Summary", "exec", "Kicker text", "Slide title",
          "One-line description.", "Evidence base text", body_html)
    build("out.html", "Deck title", "Subtitle | snapshot | source | Prepared by ...",
          deck_label="Complete Deck", search_hint="zombie, SAP, owners")

Every helper returns an HTML string. Numbers can be passed through num() to get a
right-aligned monospace table cell. Plain hyphens only - em and en dashes are stripped.
Run this file directly to regenerate assets/template.html (one example of every component).
"""
import html as _html, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
SLIDES = []
P = "\x01"  # marker: cell renders as right-aligned mono number

def e(x):
    if x is None: return ""
    try:
        import math
        if isinstance(x, float) and math.isnan(x): return ""
    except Exception: pass
    return _html.escape(str(x).replace("—", "-").replace("–", "-"))

def n(x): return f"{int(x):,}"
def pct(a, b): return f"{100*a/b:.1f}%"
def num(x): return P + (n(x) if isinstance(x, (int, float)) else str(x))

EV = {"observed": "[A. Observed]", "derived": "[B. Derived]", "estimated": "[C. Estimated]"}

def kpi(lbl, val, desc, col="navy", ev="observed"):
    """KPI card. col: navy|blue|amber|green|purple|red. ev: observed|derived|estimated."""
    return (f'<div class="kpi t-{col}"><div class="kpi-head"><span class="kpi-lbl">{lbl}</span>'
            f'<span class="badge-evidence badge-ev-{ev}">{EV[ev]}</span></div>'
            f'<div class="kpi-val c-{col}">{val}</div><span class="kpi-desc">{desc}</span></div>')

def kpi_grid(cards, four=False):
    return f'<div class="kpi-grid{" four" if four else ""}">' + "".join(cards) + "</div>"

def banner(kicker, heading, text, scope_label=None, scope_value=None):
    right = (f'<div class="scope"><span>{scope_label}</span><strong>{scope_value}</strong></div>'
             if scope_label else "")
    return (f'<div class="banner-executive"><div><span class="kicker">{kicker}</span>'
            f'<h3>{heading}</h3><p>{text}</p></div>{right}</div>')

def table(headers, rows, widths=None):
    """headers: prefix '>' for right-aligned. cells: pass num(x) for right-aligned mono numbers."""
    s = '<table class="presentation-table"><thead><tr>'
    for i, h in enumerate(headers):
        w = f' style="width:{widths[i]}%"' if widths else ""
        r = ' class="r"' if h.startswith(">") else ""
        s += f"<th{w}{r}>{h.lstrip('>')}</th>"
    s += "</tr></thead><tbody>"
    for row in rows:
        s += "<tr>" + "".join(
            f'<td class="r mono">{c[1:]}</td>' if isinstance(c, str) and c.startswith(P) else f"<td>{c}</td>"
            for c in row) + "</tr>"
    return s + "</tbody></table>"

def register(headers, rows, widths, max_height=None):
    """Scrollable table with frozen navy header - for long record-level lists."""
    style = f' style="max-height:{max_height}px"' if max_height else ""
    return f'<div class="table-container"{style}>' + table(headers, rows, widths) + "</div>"

def pill(text, kind="info"):
    """kind: success|warning|danger|info"""
    return f"<span class='status-pill status-{kind}'>{text}</span>"

def feature(idx, title, text, color="", chip=None, reality=None, reality_ok=False, action=None):
    """Numbered feature card. color: ''(blue)|f-red|f-green|f-amber|f-purple|f-navy"""
    head = (f'<div class="feature-head"><span class="feature-title"><span class="dot-num">{idx}</span>{title}</span>'
            + (f'<span class="count-chip">{chip}</span>' if chip else "") + "</div>")
    s = f'<div class="feature {color}">{head}<p>{text}</p>'
    if reality: s += f'<div class="reality{" ok" if reality_ok else ""}">{reality}</div>'
    if action: s += f'<div class="action">{action}</div>'
    return s + "</div>"

def cols(items, n_=2):
    cls = {2: "two-col", 3: "three-col", 4: "four-col"}[n_]
    return f'<div class="{cls}">' + "".join(items) + "</div>"

def box(heading, inner):
    return f'<div class="box"><div class="box-heading">{heading}</div>{inner}</div>'

def alert(label, text, kind="info"):
    """kind: danger|warning|success|info"""
    return f'<div class="alert-box alert-{kind}"><strong>{label}</strong> {text}</div>'

def note(label, spoken):
    """Presenter note - hidden until Notes / N is toggled. First person, spoken cadence."""
    return f'<div class="presenter-note"><b>{label}</b>"{spoken}"</div>'

def diagram(svg):
    return f'<div class="diagram">{svg}</div>'

def stacked_bar(title, segments, width=1080):
    """segments: list of (value, colour, label). Returns a full-width SVG stacked bar with legend."""
    tot = sum(v for v, _, _ in segments) or 1
    x = 20; bars = ""; leg = ""
    for i, (v, c, l) in enumerate(segments):
        wd = width * v / tot
        bars += f'<rect x="{x:.1f}" y="34" width="{wd:.1f}" height="44" fill="{c}"/>'
        if wd > 60:
            bars += (f'<text x="{x+wd/2:.1f}" y="62" text-anchor="middle" style="font-family:Consolas,monospace;'
                     f'font-size:15px;font-weight:800;fill:#fff">{n(v)}</text>')
        leg += (f'<rect x="{20+i*270}" y="96" width="14" height="14" fill="{c}"/><text x="{40+i*270}" y="108" '
                f'style="font-family:Calibri,Arial,sans-serif;font-size:13px;fill:#0F172A">{l} - {n(v)} ({pct(v,tot)})</text>')
        x += wd
    return diagram(f'<svg viewBox="0 0 1120 122" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{e(title)}">'
                   f'<text x="20" y="22" style="font-family:Calibri,Arial,sans-serif;font-size:14px;font-weight:700;fill:#0B2E59">{title}</text>'
                   f'{bars}{leg}</svg>')

def slide(num_, chapter, aud, tag, title, desc, evidence, body):
    """aud: exec (shown in every view) | mgmt | arch."""
    ev = f'<span class="evidence-tag">Evidence base: {evidence}</span>' if evidence else ""
    SLIDES.append(
        f'<section class="slide-wrapper" id="slide-{num_.replace(".", "-")}" data-num="{num_}" data-chapter="{e(chapter)}" '
        f'data-aud="{aud}" data-tag="{e(tag)}" data-title="{e(title)}">\n'
        f'<div class="slide-hero"><div class="hero-top"><span class="num-badge big">{num_}</span><span class="slide-tag">{tag}</span></div>\n'
        f'<h2 class="slide-heading">{num_} {title}</h2><p class="slide-description">{desc}</p>{ev}</div>\n'
        f'<div class="slide-body">{body}</div></section>')

def build(path, deck_title, subtitle, deck_label="Complete Deck", search_hint="keyword", logo_b64=None):
    rd = lambda f: open(os.path.join(ASSETS, f), encoding="utf-8").read()
    sk = rd("skeleton.html")
    logo = logo_b64 or rd("dupont-logo-base64.txt").strip()
    out = (sk.replace("{{CSS}}", rd("deck.css")).replace("{{JS}}", rd("deck.js"))
             .replace("{{LOGO_BASE64}}", logo).replace("{{DECK_TITLE}}", e(deck_title))
             .replace("{{DECK_LABEL}}", e(deck_label))
             .replace("{{SUBTITLE - domain | data snapshot | source | Prepared by Dwaipayan Mojumder, DD Mon YYYY}}", e(subtitle))
             .replace("{{three keywords}}", e(search_hint))
             .replace("{{SLIDES}}", "\n".join(SLIDES)))
    out = out.replace("—", "-").replace("–", "-")
    assert "{{" not in out, "unfilled placeholder: " + re.findall(r"\{\{[^}]*\}\}", out)[0]
    open(path, "w", encoding="utf-8").write(out)
    return path

# ---------------------------------------------------------------------------
# Demo: one example of every component -> assets/template.html
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    C1 = "Chapter 1: Executive Summary & Method"; C2 = "Chapter 2: Findings"; C3 = "Chapter 3: Recommendation & Governance"; CA = "Appendix: Record-Level Registers"
    slide("1.1", C1, "exec", "Illustrative sample", "Title Slide: Banner + KPI Grid",
          "Opening slide pattern: executive banner with the headline, six KPI cards with evidence badges, then a two-column read-out.",
          "Source system A | Source system B | snapshot date",
          banner("Headline", "The one sentence leadership should repeat afterwards",
                 "Two lines of context: what was measured, against what, and why the headline matters.", "Scope", "1,234 x 5,678") +
          kpi_grid([kpi("Population", "1,234", "Records in scope"), kpi("Comparison set", "5,678", "Second system", "blue"),
                    kpi("Matched", '520 <small>(42.1%)</small>', "Derived figure", "purple", "derived"),
                    kpi("Critical defect", "312", "Needs action", "red", "derived"), kpi("Aligned", "200", "Healthy", "green", "derived"),
                    kpi("Quick win", "189", "Can be fixed now", "amber", "estimated")]) +
          cols([box("What this means", "<ol><li><b>Finding one.</b> Short explanation.</li><li><b>Finding two.</b> Short explanation.</li></ol>"),
                box("Outcome split", table(["Outcome", ">Count", ">Share"], [[pill("Aligned", "success"), num(187), num("36.0%")], [pill("Defect", "danger"), num(312), num("60.0%")]], [56, 22, 22]))]) +
          note("Opening line", "What the presenter says out loud to open - first person, spoken cadence."))
    slide("1.2", C1, "arch", "Method", "Diagram + Method Table",
          "Inline SVG diagram in the house palette, then a method table with status pills.", "",
          diagram('<svg viewBox="0 0 1120 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Pipeline">'
                  '<defs><marker id="pa" markerWidth="10" markerHeight="10" refX="9" refY="3.6" orient="auto"><path d="M0,0 L9,3.6 L0,7.2 z" fill="#0B2E59"/></marker></defs>'
                  '<rect x="20" y="40" width="240" height="70" rx="10" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5"/><text x="140" y="72" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:15px;font-weight:700;fill:#0B2E59">Standard node</text><text x="140" y="92" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12.5px;fill:#475569">supporting line</text>'
                  '<rect x="440" y="34" width="260" height="82" rx="10" fill="#0B2E59"/><rect x="440" y="34" width="260" height="82" rx="10" fill="none" stroke="#E52421" stroke-width="3"/><text x="570" y="70" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:15px;font-weight:700;fill:#fff">Emphasis node</text><text x="570" y="92" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12.5px;fill:#E2E8F0">the one central element</text>'
                  '<rect x="880" y="40" width="220" height="70" rx="10" fill="#FEE4E2" stroke="#E52421" stroke-width="1.5"/><text x="990" y="80" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:15px;font-weight:700;fill:#0B2E59">Outcome node</text>'
                  '<path d="M262,75 L436,75" stroke="#0B2E59" stroke-width="2" fill="none" marker-end="url(#pa)"/><path d="M702,75 L876,75" stroke="#0B2E59" stroke-width="2" fill="none" marker-end="url(#pa)"/></svg>') +
          table(["Tier", "Confidence", "Rule", ">Count"], [["<b>T1</b>", pill("High", "success"), "Strict rule", num(273)], ["<b>T4</b>", pill("Review", "warning"), "Looser rule", num(110)], ["<b>None</b>", pill("None", "danger"), "No rule passed", num(863)]], [20, 17, 48, 15]) +
          alert("Method note:", "Information callout for a caveat or definition.", "info"))
    slide("2.1", C2, "mgmt", "Findings", "Feature Cards + Stacked Bar",
          "Three numbered feature cards with count chips, a reality strip and an action line; then a stacked outcome bar.", "Register A.1",
          cols([feature(1, "High confidence", "Body text.", "f-green", "377 apps", "<b>Use:</b> act directly.", True),
                feature(2, "Needs review", "Body text.", "f-amber", "143 apps", "<b>Risk:</b> false matches."),
                feature(3, "No match", "Body text.", "f-red", "863 apps", action="<b>Next:</b> obtain the missing export.")], 3) +
          stacked_bar("Outcome of 520 matched records", [(187, "#059669", "Aligned - live"), (13, "#0284C7", "Aligned - retired"), (312, "#DC2626", "Defect"), (8, "#D97706", "Other")]) +
          alert("Common error -", "a mistake the audience is likely to make, stated at the point it matters.", "danger"))
    slide("3.1", C3, "exec", "For decision", "Position, Backlog & Decisions",
          "Four-column position cards, a recommendation banner, a prioritised backlog and the decisions table.", "",
          cols([feature(i, t, "One or two sentences of judgement.", c) for i, (t, c) in enumerate([("Observation one", "f-red"), ("Observation two", "f-green"), ("Observation three", "f-navy"), ("Observation four", "f-purple")], 1)], 4) +
          banner("Recommendation", "The single action this group should approve", "One line on what happens until it is done.", "Target", "0 defects") +
          table(["Priority", "Action", ">Volume", "Owner", "Definition of done"], [[pill("P1", "danger"), "<b>Action</b>", num(225), "Owner", "Done when..."], [pill("P2", "warning"), "<b>Action</b>", num(143), "Owner", "Done when..."], [pill("P3", "info"), "<b>Action</b>", num(189), "Owner", "Done when..."]], [9, 27, 10, 19, 35]) +
          alert("Control -", "how we will know the fix held.", "success") + alert("Watch-out -", "a warning callout.", "warning"))
    slide("A.1", CA, "arch", "Register", "Scrollable Register",
          "Record-level list in a scrolling container with a frozen navy header. Prints in full.", "Match register",
          register(["Record", "ID", "Status", "Detail"], [[f"<b>Record {i}</b>", f"A{1000+i}", pill("High", "success") if i % 3 else pill("Review", "warning"), "Detail text"] for i in range(1, 41)], [30, 15, 15, 40]))
    print(build(os.path.join(ASSETS, "template.html"), "Deck Title - Subject", "Domain | snapshot DD Mon YYYY | source | Prepared by Dwaipayan Mojumder, DD Mon YYYY",
                deck_label="Complete Deck", search_hint="keyword, topic, owner"))
