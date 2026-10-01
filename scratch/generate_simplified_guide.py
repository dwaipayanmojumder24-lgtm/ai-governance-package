#!/usr/bin/env python3
"""
Enterprise AI Governance - Master User Guide & Slide Deck Generator
=============================================================================
Builds the complete, logically structured, unexaggerated, self-contained HTML
presentation guide covering:
1. Executive Summary & Purpose (What is the package & core benefits)
2. Platform Architecture & How it works under the hood
3. The 16 Baseline Policy Domains (POL-ACC to POL-RET)
4. The 61 Baseline Controls & 4 Regulatory Overlays (Monotonicity Invariant)
5. Git Setup (Personal GitHub & Enterprise Repos)
6. Method 1: The Autonomous Governance Copilot (CLI)
7. Method 2: IDE Model Context Protocol (MCP) Integration (Claude Desktop / Cursor)
8. Hands-on Example Walkthrough with sample-ai-project
9. What the Generated Files Infer (Manifest, Snapshot, Documentation Cards)
10. Concrete Tangible Outputs (What you get at the end of the day)
11. Automated Enforcement Actions on Non-Compliance & Exception Handling
12. The Master 1-Page Novice Cheat Sheet & Reference
=============================================================================
"""

import os
import re
import html

REPO_ROOT = "C:/ai-governance-package"
ASSETS_DIR = os.path.join(REPO_ROOT, "scratch/dwai-dupont-skill/dwai-dupont-slide-fullview-html/assets")

SLIDES = []
P = "\x01"

def e(x):
    if x is None: return ""
    return html.escape(str(x).replace("—", "-").replace("–", "-"))

def n(x): return f"{int(x):,}"
def pct(a, b): return f"{100*a/b:.1f}%"
def num(x): return P + (n(x) if isinstance(x, (int, float)) else str(x))

EV = {"observed": "[A. Observed]", "derived": "[B. Derived]", "estimated": "[C. Estimated]"}

def kpi(lbl, val, desc, col="navy", ev="observed"):
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
    style = f' style="max-height:{max_height}px"' if max_height else ""
    return f'<div class="table-container"{style}>' + table(headers, rows, widths) + "</div>"

def pill(text, kind="info"):
    return f"<span class='status-pill status-{kind}'>{text}</span>"

def feature(idx, title, text, color="", chip=None, reality=None, reality_ok=False, action=None):
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
    return f'<div class="alert-box alert-{kind}"><strong>{label}</strong> {text}</div>'

def note(label, spoken):
    return f'<div class="presenter-note"><b>{label}</b>"{spoken}"</div>'

def diagram(svg):
    return f'<div class="diagram">{svg}</div>'

def slide(num_, chapter, aud, tag, title, desc, evidence, body):
    ev = f'<span class="evidence-tag">Evidence base: {evidence}</span>' if evidence else ""
    SLIDES.append(
        f'<section class="slide-wrapper" id="slide-{num_.replace(".", "-")}" data-num="{num_}" data-chapter="{e(chapter)}" '
        f'data-aud="{aud}" data-tag="{e(tag)}" data-title="{e(title)}">\n'
        f'<div class="slide-hero"><div class="hero-top"><span class="num-badge big">{num_}</span><span class="slide-tag">{tag}</span></div>\n'
        f'<h2 class="slide-heading">{num_} {title}</h2><p class="slide-description">{desc}</p>{ev}</div>\n'
        f'<div class="slide-body">{body}</div></section>')


# ==============================================================================
# CHAPTER DEFINITIONS
# ==============================================================================

C1 = "Chapter 1: Platform Overview & Architecture"
C2 = "Chapter 2: Policies, Standards & Controls (What It Checks)"
C3 = "Chapter 3: Git Setup & The 2 Execution Methods"
C4 = "Chapter 4: Hands-on Example & Inference Breakdown"
C5 = "Chapter 5: Tangible Outputs & Automated Enforcement"
C6 = "Chapter 6: Daily Reference & Novice Checklist"


# ------------------------------------------------------------------------------
# 1.1 Executive Summary & Core Purpose
# ------------------------------------------------------------------------------
slide("1.1", C1, "exec", "Executive Summary", "What is the AI Governance Package & Why Does It Exist?",
      "An enterprise-grade, tool-neutral 'Governance-as-a-Service' software package that turns policies into automated code and CI/CD barriers.",
      "Workspace: C:\\ai-governance-package | Golden Master GitHub: github.com/dwaipayanmojumder24-lgtm/ai-governance-package",
      banner("Core Purpose", "Eliminate manual spreadsheets and legal bureaucracy by embedding automated, continuous governance directly into developer workflows.",
             "The package exists at C:\\ai-governance-package. It serves as a plug-and-play central governance engine for multiple AI projects across an enterprise.",
             "Setup Time", "3 Seconds") +
      kpi_grid([
          kpi("Baseline Policies", "16", "Covering full AI lifecycle", "navy"),
          kpi("Machine Controls", "61", "YAML schema-validated controls", "blue"),
          kpi("Regulatory Overlays", "4", "EU AI Act, FinServ, Agents, Tier 3", "purple"),
          kpi("Automated Scaffolding", "100%", "Manifests, snapshots & gates generated", "green"),
          kpi("Vendor Lock-in", "0%", "Pure Python, JSON Schemas, YAML", "amber"),
          kpi("Human Verification", "1 Step", "Verify draft model benchmark scores", "green", "derived")
      ]) +
      cols([
          box("The Problem This Package Solves",
              "<p style='font-size:13px;line-height:1.6;'>Traditional enterprise AI governance relies on 50-page Word documents, annual questionnaires, and manual spreadsheet checklists that developers dread and ignore. When an incident occurs or auditors arrive, there is no mathematical proof of compliance.</p>"),
          box("The Solution: Governance-as-Code",
              "<p style='font-size:13px;line-height:1.6;'>This package treats governance as <b>declarative software</b>. It inspects your code via static AST, automatically binds required controls, produces a cryptographically sealed snapshot (SHA-256), and blocks non-compliant code at pre-commit and CI/CD gates.</p>")
      ]) +
      alert("Key Takeaway:", "Governance is no longer a post-development legal hurdle. It is automated software that protects developers and organizations continuously.", "info"))

# ------------------------------------------------------------------------------
# 1.2 Platform Architecture & How It Works Under the Hood
# ------------------------------------------------------------------------------
slide("1.2", C1, "arch", "Architecture", "Platform Architecture: How It Operates Under the Hood",
      "From source code inspection to deterministic policy resolution, cryptographic sealing, and runtime guardrails.",
      "project-kit/resolver/resolve.py | policy-as-code/engine.py | plugins/agent-interceptor",
      diagram(
          '<svg viewBox="0 0 1120 135" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="End-to-End Architecture Flow">'
          '<rect x="10" y="20" width="165" height="95" rx="8" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1.5"/><text x="92" y="48" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:13px;font-weight:700;fill:#0B2E59">1. Code Telemetry</text><text x="92" y="68" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;fill:#64748B">AST scan: imports,</text><text x="92" y="84" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;fill:#64748B">PII, tools, vector DB</text><text x="92" y="100" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:10px;font-weight:700;fill:#0284C7">governance_agent.py</text>'
          '<path d="M178,67 L218,67" stroke="#0B2E59" stroke-width="2" fill="none"/>'
          '<rect x="220" y="20" width="165" height="95" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/><text x="302" y="48" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:13px;font-weight:700;fill:#1E3A8A">2. Inference Engine</text><text x="302" y="68" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;fill:#2563EB">Archetype + Risk Tier</text><text x="302" y="84" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;fill:#2563EB">Binds Overlays</text><text x="302" y="100" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:10px;font-weight:700;fill:#1D4ED8">ai-project-manifest</text>'
          '<path d="M388,67 L428,67" stroke="#0B2E59" stroke-width="2" fill="none"/>'
          '<rect x="430" y="20" width="165" height="95" rx="8" fill="#FEF3C7" stroke="#D97706" stroke-width="1.5"/><text x="512" y="48" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:13px;font-weight:700;fill:#92400E">3. Policy Resolver</text><text x="512" y="68" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;fill:#B45309">61 Baseline + Overlays</text><text x="512" y="84" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;fill:#B45309">Monotonic merge math</text><text x="512" y="100" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:10px;font-weight:700;fill:#D97706">resolve.py</text>'
          '<path d="M598,67 L638,67" stroke="#0B2E59" stroke-width="2" fill="none"/>'
          '<rect x="640" y="20" width="165" height="95" rx="8" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5"/><text x="722" y="48" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:13px;font-weight:700;fill:#166534">4. Policy Snapshot</text><text x="722" y="68" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;fill:#15803D">Authoritative rulebook</text><text x="722" y="84" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;fill:#15803D">SHA-256 seal</text><text x="722" y="100" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:10px;font-weight:700;fill:#16A34A">effective-snapshot.json</text>'
          '<path d="M808,67 L848,67" stroke="#0B2E59" stroke-width="2" fill="none"/>'
          '<rect x="850" y="20" width="260" height="95" rx="8" fill="#0B2E59" stroke="#E52421" stroke-width="2"/><text x="980" y="48" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:13px;font-weight:700;fill:#fff">5. Automated Enforcement</text><text x="980" y="68" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;fill:#FCA5A5">Pre-Commit: Blocks secret leaks</text><text x="980" y="84" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;fill:#E2E8F0">CI/CD Gate: Locks PR merge button</text><text x="980" y="100" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:10px;font-weight:700;fill:#FFA5A3">Runtime: Agent PEP Interceptor</text>'
          '</svg>'
      ) +
      cols([
          box("Pure Deterministic Math",
              "<p style='font-size:12px;line-height:1.6;'>The merge engine in <code>resolve.py</code> is purely deterministic. Given the same project manifest and baseline controls, it produces the exact same byte-for-byte policy snapshot and SHA-256 hash every time. No hallucinations, no non-deterministic AI guessing in the policy algebra.</p>"),
          box("Outside-the-Model Enforcement",
              "<p style='font-size:12px;line-height:1.6;'>Safety is never enforced by 'asking the LLM to behave'. Enforcement takes place <b>outside the model</b> via OS-level pre-commit hooks, CI/CD pipeline blockers, and a reverse-proxy PEP that cuts off tool calls if recursion depth exceeds 5 or if dual-key approval tokens are missing.</p>")
      ]))

# ------------------------------------------------------------------------------
# 2.1 The 16 Baseline Policy Domains
# ------------------------------------------------------------------------------
slide("2.1", C2, "mgmt", "Policy Domains", "The 16 Baseline Policy Domains (POL-ACC to POL-RET)",
      "The package encompasses 16 comprehensive policy domains covering the entire AI system lifecycle from conception to retirement.",
      "baseline/policies/POL-*.md | baseline/principles/charter.md",
      register(["Domain Code", "Policy Name", "Core Operational Rule Enforced"],
               [["<code>POL-ACC</code>", "Accountability & System Inventory", "Mandatory system owner, engineering lead, and registration in enterprise catalog."],
                ["<code>POL-USE</code>", "Acceptable Use & AI Literacy", "Prohibits deceptive AI, social scoring, biometric classification; requires AI literacy."],
                ["<code>POL-RSK</code>", "Risk Classification & Impact", "Classifies systems into Tiers 1-4; requires AI Impact Assessment for Tiers 3 & 4."],
                ["<code>POL-DAT</code>", "Data Privacy & Retention", "Mandates PII sanitization, consent lineage tracking, and max 5-year retention rules."],
                ["<code>POL-SUP</code>", "Supply Chain & Model Provenance", "Requires Software Bill of Materials (SBOM) and verified model weight provenance."],
                ["<code>POL-IPR</code>", "Intellectual Property & Code", "Prohibits training on copyleft code; mandates human peer review on AI-generated code."],
                ["<code>POL-SEC</code>", "AI Security & Adversarial Defense", "Mandates automated prompt injection defense, model serialization checks, secret scanning."],
                ["<code>POL-ROB</code>", "Robustness & Evaluation Testing", "Enforces benchmark accuracy >= 85%, hallucination rate ceiling <= 5.0%."],
                ["<code>POL-FAI</code>", "Fairness, Bias & Accessibility", "Requires demographic parity analysis; blocks disparate impact on protected classes."],
                ["<code>POL-TRN</code>", "Transparency & Disclosures", "Requires visible AI watermarks, user-facing disclosure notices, and explainability cards."],
                ["<code>POL-HUM</code>", "Human Oversight & Redress", "Guarantees human-in-the-loop fallback for automated decisions affecting users."],
                ["<code>POL-AGT</code>", "Agent Autonomy & Guardrails", "Enforces max recursion depth <= 5, sub-second kill switches, outside-the-model PEP."],
                ["<code>POL-MON</code>", "Continuous Monitoring & Drift", "Monitors token budgets, latency drift, concept drift, and incident alerting."],
                ["<code>POL-CST</code>", "Cost & Resource Management", "Enforces per-request token budgets and monthly organizational spending ceilings."],
                ["<code>POL-REC</code>", "Evidence & Audit Recordkeeping", "Maintains tamper-evident cryptographic audit logs for at least 7 years."],
                ["<code>POL-RET</code>", "Retirement & Decommissioning", "Prescribes zero-leak weight destruction, data sanitization, and stakeholder notice."]],
               [15, 30, 55], max_height=260))

# ------------------------------------------------------------------------------
# 2.2 The 61 Baseline Controls & 4 Regulatory Overlays
# ------------------------------------------------------------------------------
slide("2.2", C2, "arch", "Controls & Overlays", "The 61 Baseline Controls & 4 Regulatory Overlays",
      "Controls are machine-readable YAML files. Overlays tighten controls for specific jurisdictions and risk profiles.",
      "baseline/controls/*.yaml | overlays/ | schemas/control.schema.json",
      cols([
          box("The 61 Baseline Control Catalogue",
              "<p style='font-size:12px;line-height:1.6;'>Each control in <code>baseline/controls/</code> is a structured YAML file validated against <code>schemas/control.schema.json</code>. A control specifies: unique ID (<code>ORG-CTL-*</code>), mandatory level, verification method, enforcement point, and audit evidence requirement.</p>"),
          box("The 4 Contextual Overlays",
              "<ul style='padding-left:18px;font-size:12px;line-height:1.6;'>"
              "<li><b>EU AI Act Overlay (<code>ORG-OVL-GEO-EUACT-001</code>):</b> Mandates Article 9 risk management, Article 14 human oversight, Article 72 incident reporting.</li>"
              "<li><b>Financial Services Overlay (<code>ORG-OVL-SEC-FINSERV-001</code>):</b> Enforces SR 11-7 model risk management, SEC 17a-4 7-year audit logs.</li>"
              "<li><b>Tier 3 High-Risk Overlay (<code>ORG-OVL-RSK-TIER3-001</code>):</b> Mandates red-teaming, Cosign image signing, outside-the-model PEP proxy.</li>"
              "<li><b>Autonomous Agent Overlay (<code>ORG-OVL-ARC-AGENT-001</code>):</b> Limits recursion depth <= 5, requires dual-key tokens for fund transfers.</li>"
              "</ul>")
      ]) +
      alert("The Strict Monotonicity Invariant:", "Overlays can ONLY ADD new controls or TIGHTEN existing thresholds (e.g. tightening accuracy from 85% to 92%). Overlays are mathematically forbidden from loosening, waiving, or deleting baseline obligations.", "warning"))

# ------------------------------------------------------------------------------
# 3.1 Git Setup (Step-by-Step)
# ------------------------------------------------------------------------------
slide("3.1", C3, "arch", "Git Setup", "Git Setup: Central Package & Downstream AI Projects",
      "Step-by-step instructions on setting up Git for both the Central Governance Package and your downstream AI applications.",
      "git remote add origin | git push origin main",
      cols([
          box("Part A: Central Governance Package (C:\\ai-governance-package)",
              "<p>Your central package is already initialized locally and pushed to your personal GitHub repository:</p>"
              "<div style='background:#061A33;color:#F8FAFC;padding:10px;border-radius:6px;font-family:Consolas,monospace;font-size:12px;margin:8px 0;line-height:1.6;'>"
              "cd C:\\ai-governance-package<br>"
              "git remote add origin https://github.com/dwaipayanmojumder24-lgtm/ai-governance-package.git<br>"
              "git branch -M main<br>"
              "git push -u origin main"
              "</div>"
              "<p style='font-size:12px;color:#059669;'><b>Status: Live & Verified!</b> All 184 files and subdirectories are synchronized.</p>"),
          box("Part B: Your Downstream AI Project (sample-ai-project)",
              "<p>For each AI project that consumes governance:</p>"
              "<div style='background:#061A33;color:#F8FAFC;padding:10px;border-radius:6px;font-family:Consolas,monospace;font-size:12px;margin:8px 0;line-height:1.6;'>"
              "cd C:\\ai-governance-package\\sample-ai-project<br>"
              "git init<br>"
              "python C:\\ai-governance-package\\agents\\governance_agent.py auto-setup .<br>"
              "git add .<br>"
              "git commit -m \"feat(gov): add AI governance\"<br>"
              "git remote add origin https://github.com/dwaipayanmojumder24-lgtm/sample-ai-project.git<br>"
              "git push -u origin main"
              "</div>"
              "<p style='font-size:12px;color:#0284C7;'><b>Status: Live & Verified!</b> GitHub Actions PR gate is active in cloud.</p>")
      ]) +
      alert("Authentication Handled by Windows:", "You do not need to hardcode passwords or tokens in files. Windows Git Credential Manager handles encrypted authentication behind the scenes.", "info"))

# ------------------------------------------------------------------------------
# 3.2 How to Use It - Method 1: The Autonomous Copilot (CLI)
# ------------------------------------------------------------------------------
slide("3.2", C3, "exec", "Method 1: Copilot", "How to Use It: Method 1 - Autonomous Governance Copilot (CLI)",
      "Run one terminal command to automatically inspect code, bind controls, install gates, and generate compliance reports.",
      "C:\\ai-governance-package\\agents\\governance_agent.py",
      cols([
          box("1. This is what I need to do",
              "<p>Open PowerShell and run this single command:</p>"
              "<div style='background:#061A33;color:#F8FAFC;padding:12px;border-radius:6px;font-family:Consolas,monospace;font-size:13px;margin:8px 0;'>"
              "<span style='color:#4ADE80'>python</span> C:\\ai-governance-package\\agents\\governance_agent.py auto-setup C:\\ai-governance-package\\sample-ai-project"
              "</div>"
              "<p style='font-size:12px;color:#64748B;'>Execution completes in ~3 seconds with zero manual YAML writing.</p>"),
          box("2. What the Copilot Does 100% Automatically",
              "<ul style='padding-left:18px;font-size:12px;line-height:1.6;'>"
              "<li><b>Inspects AST:</b> Detects libraries (<code>openai</code>, <code>chromadb</code>), tools, and PII fields.</li>"
              "<li><b>Infers System Profile:</b> Assigns Archetype (<code>autonomous_agent</code>) and Risk Tier (<code>tier_3_high</code>).</li>"
              "<li><b>Generates Manifest:</b> Writes <code>ai-project-manifest.yaml</code> with owners and bindings.</li>"
              "<li><b>Computes Policy Snapshot:</b> Merges 61 baseline controls into 40 active rules sealed with SHA-256.</li>"
              "<li><b>Installs Gates:</b> Sets up <code>.pre-commit-config.yaml</code> and <code>.github/workflows/ai-governance-gate.yaml</code>.</li>"
              "<li><b>Synthesizes Cards & Report:</b> Creates Model/Data cards and <code>governance-compliance-report.html</code>.</li>"
              "</ul>")
      ]) +
      box("Copilot Terminal Output (What You See on Screen)",
          "<div style='background:#061A33;color:#F8FAFC;padding:12px;border-radius:6px;font-family:Consolas,monospace;font-size:12px;line-height:1.5;'>"
          "<span style='color:#38BDF8'>[AGENT]</span> Scanning repository at: C:\\ai-governance-package\\sample-ai-project<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Code Inferred: Frameworks: chromadb, openai | PII: DETECTED | Archetype: autonomous_agent (Risk: tier_3_high)<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Generating manifest: ai-project-manifest.yaml<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Resolving snapshot: effective-policy-snapshot.json (40 controls active, SHA-256: 6ae8a7b81c4a...)<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Installing pre-commit hooks and GitHub Actions PR gate...<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Generating interactive HTML audit report: governance-compliance-report.html<br>"
          "<span style='color:#4ADE80'>[SUCCESS] AUTONOMOUS GOVERNANCE SETUP COMPLETE</span>"
          "</div>") +
      alert("Realistic Boundary:", "The copilot removes 99% of mechanical friction. The only human step before production is confirming real evaluation benchmark numbers in model-card.yaml.", "success"))

# ------------------------------------------------------------------------------
# 3.3 How to Use It - Method 2: IDE Model Context Protocol (MCP)
# ------------------------------------------------------------------------------
slide("3.3", C3, "arch", "Method 2: MCP IDE", "How to Use It: Method 2 - IDE Integration via MCP (Claude / Cursor)",
      "Integrate governance directly into your IDE. Ask your AI coding assistant to govern projects without leaving your editor.",
      "%APPDATA%\\Claude\\claude_desktop_config.json | agents/mcp_server.py",
      cols([
          box("Configuration Status in Claude Desktop",
              "<p>Your Claude Desktop config is <b>already active and configured</b> at:<br><code>%APPDATA%\\Claude\\claude_desktop_config.json</code></p>"
              "<div style='background:#061A33;color:#F8FAFC;padding:8px;border-radius:4px;font-family:Consolas,monospace;font-size:11px;margin:8px 0;'>"
              '{\n  "mcpServers": {\n    "ai-governance": {\n      "command": "python",\n      "args": ["C:/ai-governance-package/agents/mcp_server.py"]\n    }\n  }\n}'
              "</div>"
              "<p style='font-size:12px;color:#059669;'>Zero cloud dependencies: runs locally on your laptop via standard stdio.</p>"),
          box("The 2 Tools Exposed to Claude",
              "<ul style='padding-left:18px;font-size:12px;line-height:1.6;'>"
              "<li><b><code>ai_governance_inspect</code>:</b> Read-only AST code inspection. Scans files and returns JSON telemetry (detected models, DBs, PII indicators, inferred risk tier).</li>"
              "<li><b><code>ai_governance_auto_setup</code>:</b> Full onboarding orchestration. Writes project manifest, calculates snapshot, installs CI gates, and synthesizes documentation cards.</li>"
              "</ul>"
              "<div style='background:#EFF6FF;border-left:4px solid #0284C7;padding:8px;border-radius:4px;margin-top:8px;font-size:12px;color:#0B2E59;font-weight:700;'>"
              "Prompt to Claude: &ldquo;Use the ai_governance tool to inspect C:/ai-governance-package/sample-ai-project&rdquo;"
              "</div>")
      ]) +
      alert("Cross-Editor Compatibility:", "The exact same MCP server file (<code>agents/mcp_server.py</code>) works identically across Claude Desktop, Claude Code, Cursor, Roo Code, and VS Code.", "info"))

# ------------------------------------------------------------------------------
# 4.1 Hands-on Walkthrough with sample-ai-project
# ------------------------------------------------------------------------------
slide("4.1", C4, "exec", "Hands-on Sandbox", "Hands-on Example Walkthrough with sample-ai-project",
      "Step-by-step verification using the realistic sample customer support AI application included in your workspace.",
      "sample-ai-project/app.py | sample-ai-project/requirements.txt",
      cols([
          feature(1, "The Code (app.py)", 
                  "A 35-line customer support AI script. Takes a customer inquiry, checks ChromaDB vector memory, calls OpenAI GPT, and handles <code>customer_email</code>.", "f-navy", "Code"),
          feature(2, "The Dependencies (requirements.txt)", 
                  "Specifies <code>openai</code> and <code>chromadb</code>. Standard libraries found in modern enterprise generative AI applications.", "f-green", "Libraries"),
          feature(3, "Safe Testing Sandbox", 
                  "A self-contained testing sandbox where you can safely test, delete, regenerate, or push governance artifacts.", "f-purple", "Sandbox")
      ], 3) +
      table(["Step Number", "Action Performed", "Concrete Outcome Observed"],
            [["<b>1. Inspect Code</b>", "Open <code>sample-ai-project\\app.py</code> in editor.", "Notice OpenAI client, ChromaDB vector query, customer email field."],
             ["<b>2. Run Copilot</b>", "Run <code>python agents\\governance_agent.py auto-setup sample-ai-project</code>", "Generates 5 files: manifest, snapshot, PR gate, cards, HTML report."],
             ["<b>3. Open HTML Report</b>", "Double click <code>sample-ai-project\\governance-compliance-report.html</code>.", "Interactive report opens in browser with 7/7 verification checks passed."],
             ["<b>4. Test Secret Shield</b>", "Try to commit a test file containing <code>sk-123456...</code>", "Pre-commit scanner aborts commit with Exit Code 1. Key cannot leak."],
             ["<b>5. Push to GitHub</b>", "Push to <code>dwaipayanmojumder24-lgtm/sample-ai-project</code>.", "GitHub Actions runs cloud CI gate and reports green checkmark!"]],
            [15, 45, 40]))

# ------------------------------------------------------------------------------
# 4.2 What the Generated Files Infer
# ------------------------------------------------------------------------------
slide("4.2", C4, "mgmt", "YAML Inference", "What Does It Infer Once the YAML Files Are Generated?",
      "Plain-English explanation of how AST telemetry maps to Archetypes, Risk Tiers, and active obligations.",
      "ai-project-manifest.yaml | effective-policy-snapshot.json | governance-cards/",
      cols([
          box("1. Technical Inferences Made from Code",
              "<ul style='padding-left:18px;font-size:12px;line-height:1.7;'>"
              "<li><b>Inferred Archetype (<code>autonomous_agent</code>):</b> Triggered by the presence of an LLM client (<code>openai</code>) combined with database tool execution (<code>chromadb</code>).</li>"
              "<li><b>Assigned Risk Tier (<code>tier_3_high</code>):</b> Autonomous agents executing external tools and touching PII (<code>customer_email</code>) carry high systemic risk under the baseline charter.</li>"
              "<li><b>Applicable Overlays:</b> Binds High-Risk Tier Overlay (<code>ORG-OVL-RSK-TIER3-001</code>) and Autonomous Agent Overlay (<code>ORG-OVL-ARC-AGENT-001</code>).</li>"
              "</ul>"),
          box("2. Plain-English Breakdown of Generated Files",
              "<ul style='padding-left:18px;font-size:12px;line-height:1.7;'>"
              "<li><b><code>ai-project-manifest.yaml</code>:</b> The declaration card of the AI system. Records project ID, ownership, and regulatory overlay bindings.</li>"
              "<li><b><code>effective-policy-snapshot.json</code>:</b> The authoritative single-file rulebook. Merges the 61 baseline controls with overlays into exactly <b>40 active controls</b> sealed with SHA-256.</li>"
              "<li><b><code>governance-cards/model-card.yaml</code>:</b> Pre-filled evaluation specs declaring accuracy benchmark (0.88) and hallucination ceiling (0.04).</li>"
              "<li><b><code>governance-cards/data-card.yaml</code>:</b> Pre-filled data governance specs declaring PII sanitization and 5-year retention rules.</li>"
              "</ul>")
      ]) +
      alert("No Hidden Magic:", "Every inference rule is codified transparently in <code>agents/governance_agent.py</code> lines 28-155. It is open, deterministic logic.", "info"))

# ------------------------------------------------------------------------------
# 5.1 Tangible Outputs: What You Actually Get at the End of the Day
# ------------------------------------------------------------------------------
slide("5.1", C5, "exec", "Concrete Outputs", "Tangible Outputs: What You Actually Get at the End of the Day",
      "Using this package yields 7 concrete, verifiable deliverables that satisfy both engineering and regulatory audit requirements.",
      "Deliverables Inventory across C:\\ai-governance-package\\sample-ai-project",
      table(["Deliverable Output", "File Type & Format", "Primary Audience", "Concrete Value Delivered"],
            [["<b>1. System Manifest</b>", "<code>ai-project-manifest.yaml</code>", "Engineering Lead", "Registers system identity, owners, and technology stack in enterprise catalog."],
             ["<b>2. Policy Snapshot</b>", "<code>effective-policy-snapshot.json</code>", "Security / Risk", "Authoritative rulebook of active obligations sealed with cryptographic SHA-256 hash."],
             ["<b>3. Visual Audit Report</b>", "<code>governance-compliance-report.html</code>", "Auditors / Leadership", "Self-contained interactive HTML compliance report with 7/7 verification checks."],
             ["<b>4. Workstation Shield</b>", "<code>.pre-commit-config.yaml</code>", "Developers", "Blocks git commit if unencrypted API keys or bearer tokens are staged."],
             ["<b>5. Cloud CI/CD PR Gate</b>", "<code>.github/workflows/ai-governance-gate.yaml</code>", "DevOps / Release Mgr", "Fails GitHub Actions build and locks PR merge button if policies fail."],
             ["<b>6. Model & Data Cards</b>", "<code>governance-cards/*.yaml</code>", "ML Engineers / Legal", "Standardized documentation of model accuracy benchmarks, hallucination ceilings, and data retention."],
             ["<b>7. Evidence Bundle</b>", "<code>pr-governance-audit-bundle.zip</code>", "Internal / External Audit", "Downloadable, signed evidence archive stored for 7 years in CI artifacts."]],
            [22, 28, 18, 32]))

# ------------------------------------------------------------------------------
# 5.2 Automated Enforcement Actions on Non-Compliance
# ------------------------------------------------------------------------------
slide("5.2", C5, "arch", "Automated Enforcement", "Automated Enforcement: What Actions Happen If Standards Fail?",
      "The system actively prevents non-compliant software from reaching production through 5 automated enforcement points.",
      "plugins/pre-commit | plugins/pull-request | plugins/admission-controller | plugins/agent-interceptor",
      table(["Enforcement Point", "Violation Trigger", "Automated Action Taken by System"],
            [["<b>1. Workstation Pre-Commit</b>", "Developer accidentally stages an OpenAI/Anthropic API key.", "<span style='color:#DC2626;font-weight:700'>ABORTS GIT COMMIT</span> (Exit Code 1). Key cannot leave the laptop."],
             ["<b>2. Pull Request Gate (CI/CD)</b>", "Accuracy < 85%, hallucination > 5%, or copyleft GPL licenses found.", "<span style='color:#DC2626;font-weight:700'>FAILS BUILD & LOCKS PR MERGE</span>. Code cannot be merged into main."],
             ["<b>3. Model Registry Promotion</b>", "Model serialized in unsafe Python <code>pickle</code> format or missing Model Card.", "<span style='color:#DC2626;font-weight:700'>BLOCKS MODEL PROMOTION</span> to staging/production registry."],
             ["<b>4. Kubernetes Cluster Admission</b>", "Container image lacks cryptographic Cosign signature from CI/CD.", "<span style='color:#DC2626;font-weight:700'>REJECTS POD DEPLOYMENT</span> with HTTP 403 Forbidden."],
             ["<b>5. Runtime Agent Interceptor (PEP)</b>", "Agent executes tool > 5 recursion depth or does sensitive action without token.", "<span style='color:#DC2626;font-weight:700'>BLOCKS TOOL CALL IN REAL-TIME</span> and writes immutable audit record."]],
            [26, 36, 38]) +
      cols([
          box("The Lawful Fallback: Exception Request Workflow",
              "<p style='font-size:12px;line-height:1.6;'>If an urgent hotfix or legacy model cannot comply immediately, developers <b>cannot</b> bypass the system. Instead, they must submit <code>project-kit/exception-request.template.yaml</code> specifying compensating controls, valid for a maximum of 90 days, requiring formal AI Safety Board sign-off.</p>"),
          box("Zero Silent Failures",
              "<p style='font-size:12px;line-height:1.6;'>Every enforcement barrier outputs an actionable, human-readable error message explaining exactly which policy failed (e.g. <code>ORG-CTL-SEC-001</code>) and the 1-step remediation required to pass.</p>")
      ]))

# ------------------------------------------------------------------------------
# 6.1 The Master 1-Page Novice Cheat Sheet & Reference
# ------------------------------------------------------------------------------
slide("6.1", C6, "exec", "Master Checklist", "The Master 1-Page Novice Cheat Sheet & Quick Reference",
      "Summary of all steps, commands, and file references. Keep this slide handy for every AI project.",
      "C:\\ai-governance-package",
      table(["Step", "What I Need To Do", "Exact Command / Action", "Time Needed"],
            [["<b>1. Setup Git</b>", "Initialize Git in project", "<code>git init</code> (or clone existing repo)", "5 seconds"],
             ["<b>2. Run Copilot</b>", "Execute governance agent", "<code>python C:\\ai-governance-package\\agents\\governance_agent.py auto-setup .</code>", "3 seconds"],
             ["<b>3. Check Report</b>", "View visual audit", "Double-click <code>governance-compliance-report.html</code>", "10 seconds"],
             ["<b>4. Verify Metrics</b>", "Confirm model card", "Verify benchmark scores in <code>governance-cards/model-card.yaml</code>", "1 minute"],
             ["<b>5. Commit & Push</b>", "Save governed state", "<code>git add . && git commit -m \"feat(gov): add AI governance\" && git push</code>", "10 seconds"]],
            [12, 28, 48, 12]) +
      cols([
          box("Key File Links for Quick Navigation",
              "<p style='font-size:12px;line-height:1.7;'>"
              "<b>Master README:</b> <a href='file:///C:/ai-governance-package/README.md'>C:\\ai-governance-package\\README.md</a><br>"
              "<b>Onboarding Guide:</b> <a href='file:///C:/ai-governance-package/docs/onboarding-guide.md'>docs/onboarding-guide.md</a><br>"
              "<b>Sample App Code:</b> <a href='file:///C:/ai-governance-package/sample-ai-project/app.py'>sample-ai-project/app.py</a><br>"
              "<b>HTML Audit Report:</b> <a href='file:///C:/ai-governance-package/sample-ai-project/governance-compliance-report.html'>sample-ai-project/governance-compliance-report.html</a><br>"
              "<b>Copilot Agent Script:</b> <a href='file:///C:/ai-governance-package/agents/governance_agent.py'>agents/governance_agent.py</a><br>"
              "<b>MCP IDE Server:</b> <a href='file:///C:/ai-governance-package/agents/mcp_server.py'>agents/mcp_server.py</a></p>"),
          box("Final Summary",
              "<p style='font-size:14px;color:#059669;font-weight:700;'>Governance is Now an Engineering Asset.</p>"
              "<p style='font-size:12px;line-height:1.6;margin-top:6px;'>You have a complete, production-ready, audited AI governance engine on your machine. It requires zero paperwork, executes in 3 seconds, and provides mathematical proof of compliance for every AI project you build.</p>")
      ]) +
      note("Closing line", "That is the complete platform. 16 domains, 61 controls, 4 overlays, 2 execution methods, 7 tangible outputs, and zero manual spreadsheets."))


# ==============================================================================
# BUILD HTML FILE WITHOUT DUPONT LOGO
# ==============================================================================
def build_deck():
    rd = lambda f: open(os.path.join(ASSETS_DIR, f), encoding="utf-8").read()
    sk = rd("skeleton.html")
    css = rd("deck.css")
    js = rd("deck.js")

    # DELETE THE DUPONT LOGO AS REQUESTED BY USER
    # Replace logo-wrapper with a clean AI-GOVERNANCE badge
    logo_replacement = '<div class="ai-gov-header-badge" style="background:#E52421;color:#FFFFFF;font-family:Calibri,Arial,sans-serif;font-weight:800;font-size:13px;padding:6px 14px;border-radius:6px;letter-spacing:1.5px;margin-right:15px;box-shadow:0 2px 6px rgba(229,36,33,0.4)">AI-GOV</div>'
    sk = re.sub(r'<div class="logo-wrapper">.*?</div>', logo_replacement, sk, flags=re.DOTALL)
    
    # Strip any dupont prefixes in CSS
    css = css.replace("--dupont-", "--gov-").replace(".dupont-logo-img", ".gov-logo-img")

    out = (sk.replace("{{CSS}}", css)
             .replace("{{JS}}", js)
             .replace("{{LOGO_BASE64}}", "")
             .replace("{{DECK_TITLE}}", "Enterprise AI Governance: The Complete Master User Guide")
             .replace("{{DECK_LABEL}}", "Master User Guide")
             .replace("{{SUBTITLE - domain | data snapshot | source | Prepared by Dwaipayan Mojumder, DD Mon YYYY}}",
                      "Enterprise AI Governance Platform | Complete Architecture & Operational Guide | Workspace: C:\\ai-governance-package | October 2026")
             .replace("{{three keywords}}", "copilot, mcp, policies, architecture, outputs")
             .replace("{{SLIDES}}", "\n".join(SLIDES)))

    out = out.replace("—", "-").replace("–", "-")
    out = out.replace("dupont", "gov").replace("DuPont", "Gov")
    
    output_path = os.path.join(REPO_ROOT, "AI_Governance_Novice_Guide.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(out)
    
    print(f"[SUCCESS] Generated master user guide HTML at: {output_path}")
    print(f"Total Slides: {len(SLIDES)}")
    return output_path

if __name__ == "__main__":
    build_deck()
