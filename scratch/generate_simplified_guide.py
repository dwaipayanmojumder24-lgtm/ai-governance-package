#!/usr/bin/env python3
"""
Generates the simplified, step-by-step, plain-English HTML slide deck for novices,
focusing directly on:
1. "This is what I need to do" -> Step-by-step clarity.
2. Setting up Git for the Governance Package & the AI project.
3. What the generated YAML files infer (Archetype, Risk Tier, Snapshot seal).
4. The interactive HTML Compliance Audit Report (governance-compliance-report.html).
5. Automated Actions taken when non-compliance is detected.
6. Method 1: The Autonomous Governance Copilot (agents/governance_agent.py).
7. Method 2: Model Context Protocol (MCP) IDE integration (Cursor, Claude, VS Code).
8. The sample project C:\\ai-governance-package\\sample-ai-project for hands-on testing.
9. Zero DuPont logo.
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
# SLIDES: SIMPLIFIED STEP-BY-STEP NOVICE GUIDE
# ==============================================================================

C1 = "Chapter 1: Orientation & Git Setup"
C2 = "Chapter 2: The Two Ways to Run Governance (Copilot & IDE MCP)"
C3 = "Chapter 3: Testing with the Sample Project & What Files Infer"
C4 = "Chapter 4: The HTML Compliance Report & Automated Enforcement Actions"
CA = "Appendix: The Novice Cheat Sheet"

# ------------------------------------------------------------------------------
# 1.1 Start Here: What You Have & Your 2 Goals
# ------------------------------------------------------------------------------
slide("1.1", C1, "exec", "Start Here", "The Situation: What You Have on Your C: Drive & Your 2 Goals",
      "You do not need to read 61 legal policies. Here is exactly what is on your computer and the two goals you need to achieve.",
      "Workspace: C:\\ai-governance-package | Sample Project: C:\\ai-governance-package\\sample-ai-project",
      banner("Your Goal as a Novice", "Take an AI application and make it 100% compliant with enterprise rules in 3 seconds.",
             "The governance package already exists on your C: drive at C:\\ai-governance-package. You now have a project (like our sample app) that needs governance. Here are the exact steps to connect them.",
             "Effort", "1 Command") +
      kpi_grid([
          kpi("Governance Package", "C:\\ai-gov", "Already on your C: drive", "navy"),
          kpi("Sample AI Project", "Ready", "sample-ai-project for testing", "blue"),
          kpi("Manual Policies to Write", "0", "Zero documentation to write", "green"),
          kpi("Time Required", "3 Seconds", "Fully automated by Copilot", "purple", "derived"),
          kpi("Two Easy Methods", "CLI or IDE", "Copilot command OR Cursor/Claude chat", "amber"),
          kpi("Compliance Result", "100%", "Emits audit-ready snapshot & gates", "green", "derived")
      ]) +
      cols([
          box("1. This is what you already have on your C: drive",
              "<ul><li><b>The Central AI Governance Package:</b> Located at <code>C:\\ai-governance-package</code>. This is the master library containing all 61 enterprise controls, policy rules, and automation agents.</li>"
              "<li><b>The Hands-on Test Project:</b> Located at <code>C:\\ai-governance-package\\sample-ai-project</code>. A realistic starter AI app (Python, OpenAI, ChromaDB) where you can safely test everything.</li></ul>"),
          box("2. This is what you need to do (Your 2 Choices)",
              "<ol><li><b>Choice 1 (Autonomous Governance Copilot):</b> Run 1 command in your terminal. The copilot inspects the code, sets up your governance files, and generates a visual HTML audit report.</li>"
              "<li><b>Choice 2 (IDE Integration via MCP):</b> Open Cursor, Claude Desktop, or VS Code, and configure our Model Context Protocol server once. Then simply ask the AI chat to govern your project!</li></ol>")
      ]) +
      note("Opening line", "Welcome. You have two files already on your computer, and you only need to run one command today."))

# ------------------------------------------------------------------------------
# 1.2 Git Setup: How to Set Up Git for the Governance Package & Projects
# ------------------------------------------------------------------------------
slide("1.2", C1, "arch", "Git Setup", "Git Setup: How to Set Up Git Locally & Push to GitHub",
      "Step-by-step instructions on setting up Git for both the Central Governance Package and your downstream AI projects.",
      "git status | git commit | git push origin main",
      cols([
          box("Part A: Setting Up Git for the Central Governance Package (C:\\ai-governance-package)",
              "<p>Your local package at <code>C:\\ai-governance-package</code> is already a committed Git repository. To share it with your company on GitHub:</p>"
              "<ol style='padding-left:18px;margin-top:8px;line-height:1.7'>"
              "<li>Open PowerShell and navigate to the package:<br><code>cd C:\\ai-governance-package</code></li>"
              "<li>Create a new empty repository on your company GitHub (e.g., <code>https://github.com/your-org/ai-governance-package.git</code>).</li>"
              "<li>Link your local folder to GitHub:<br><code>git remote add origin https://github.com/your-org/ai-governance-package.git</code></li>"
              "<li>Push the master branch to GitHub:<br><code>git branch -M main</code><br><code>git push -u origin main</code></li>"
              "</ol>"
              "<p style='margin-top:8px;font-size:12px;color:#059669'><b>Done!</b> Now all engineering teams in your company can clone or reference this repository.</p>"),
          box("Part B: Setting Up Git for Your AI Project (sample-ai-project or Any Project)",
              "<p>When you start or work on an AI project that needs governance:</p>"
              "<ol style='padding-left:18px;margin-top:8px;line-height:1.7'>"
              "<li>Navigate into your project directory:<br><code>cd C:\\ai-governance-package\\sample-ai-project</code></li>"
              "<li>If it is a new folder, initialize Git:<br><code>git init</code></li>"
              "<li>Run the Governance Copilot (see next slide) to create your governance files.</li>"
              "<li>Stage and commit all files including the governance snapshot:<br><code>git add .</code><br><code>git commit -m \"feat(gov): add enterprise AI governance\"</code></li>"
              "<li>Push your branch to GitHub:<br><code>git push origin feature/governed-ai-app</code></li>"
              "</ol>"
              "<p style='margin-top:8px;font-size:12px;color:#0284C7'><b>Notice:</b> The pre-commit scanner will automatically protect you from committing plain-text secrets!</p>")
      ]) +
      alert("Why Git Matters for Governance:", "Git commits provide an immutable audit trail. The cryptographic SHA-256 snapshot hash committed to Git proves to regulators exactly which policies were active when code was written.", "info"))

# ------------------------------------------------------------------------------
# 2.1 Point 1: Autonomous Governance Copilot
# ------------------------------------------------------------------------------
slide("2.1", C2, "exec", "Point 1: Copilot", "Point 1: The Autonomous Governance Copilot (Terminal Command)",
      "This is the fastest method. Open your terminal, run 1 single command, and the Copilot does 100% of the governance work in 3 seconds.",
      "C:\\ai-governance-package\\agents\\governance_agent.py",
      cols([
          box("1. This is what I need to do",
              "<p>Open <b>PowerShell</b> or <b>Command Prompt</b> on your Windows machine.</p>"
              "<p style='margin-top:6px;'>Copy and paste this exact command:</p>"
              "<div style='background:#061A33;color:#F8FAFC;padding:12px;border-radius:6px;font-family:Consolas,monospace;font-size:13px;margin-top:8px;'>"
              "<span style='color:#4ADE80'>python</span> C:\\ai-governance-package\\agents\\governance_agent.py auto-setup C:\\ai-governance-package\\sample-ai-project"
              "</div>"
              "<p style='margin-top:10px;font-size:12px;color:#64748B;'>Tip: To run it on any other project, just replace the last folder path with your project's folder!</p>"),
          box("2. This is what the Copilot does automatically (Zero Manual Work)",
              "<ul style='padding-left:18px;line-height:1.7'>"
              "<li><b>Scans Code:</b> Analyzes imports, vector DBs (ChromaDB), models (OpenAI), and PII fields.</li>"
              "<li><b>Infers Identity:</b> Automatically assigns the Archetype (<code>autonomous_agent</code>) and Risk Tier (<code>tier_3_high</code>).</li>"
              "<li><b>Generates Manifest:</b> Creates <code>ai-project-manifest.yaml</code> with project owners and bindings.</li>"
              "<li><b>Resolves Policy Snapshot:</b> Merges baseline controls with overlays into <code>effective-policy-snapshot.json</code> sealed with SHA-256.</li>"
              "<li><b>Installs Gates:</b> Sets up <code>.pre-commit-config.yaml</code> and <code>.github/workflows/ai-governance-gate.yaml</code>.</li>"
              "<li><b>Generates HTML Report:</b> Creates <code>governance-compliance-report.html</code>.</li>"
              "</ul>")
      ]) +
      box("Copilot Terminal Output (What You See on Screen)",
          "<div style='background:#061A33;color:#F8FAFC;padding:14px;border-radius:8px;font-family:Consolas,monospace;font-size:12px;line-height:1.6'>"
          "<span style='color:#38BDF8'>[AGENT]</span> Scanning repository at: C:\\ai-governance-package\\sample-ai-project<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Code Telemetry Inferred: Frameworks: chromadb, openai | PII: DETECTED | Archetype: autonomous_agent (Assigned Risk: tier_3_high)<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Generating declarative project manifest... ai-project-manifest.yaml<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Resolving deterministic policy snapshot... effective-policy-snapshot.json (40 controls active, SHA-256: 6ae8a7b81c4a...)<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Installing pre-commit hooks and CI/CD PR gate...<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Pre-populating starter Model Card & Data Card...<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Generating interactive HTML compliance audit report... governance-compliance-report.html<br>"
          "<span style='color:#4ADE80'>=================================================================</span><br>"
          "<span style='color:#4ADE80'>  AUTONOMOUS GOVERNANCE SETUP COMPLETE (0 MANUAL WORK)</span><br>"
          "<span style='color:#4ADE80'>=================================================================</span>"
          "</div>") +
      alert("No Forms to Fill:", "You did not write a single line of YAML or policy documentation. The copilot inspected your code and configured everything.", "success"))

# ------------------------------------------------------------------------------
# 2.2 Point 2: IDE Model Context Protocol (MCP) Integration
# ------------------------------------------------------------------------------
slide("2.2", C2, "arch", "Point 2: MCP IDE", "Point 2: IDE Integration via Model Context Protocol (MCP)",
      "If you use Cursor, Claude Desktop, or VS Code, you don't even have to open a terminal. Just ask your AI assistant in chat.",
      "C:\\ai-governance-package\\agents\\mcp_server.py | Cursor / Claude / VS Code",
      cols([
          box("Step 1: Configure MCP in Your Editor (One-Time Setup)",
              "<p><b>In Cursor:</b></p>"
              "<ol style='padding-left:18px;margin-bottom:8px;font-size:12px;line-height:1.6'>"
              "<li>Open Cursor > Settings (Ctrl+Shift+J) > Features > MCP Servers > Add New.</li>"
              "<li>Name: <code>ai-governance</code> | Type: <code>command</code></li>"
              "<li>Command: <code>python C:/ai-governance-package/agents/mcp_server.py</code></li>"
              "</ol>"
              "<p><b>In Claude Desktop:</b></p>"
              "<div style='background:#061A33;color:#F8FAFC;padding:8px;border-radius:4px;font-family:Consolas,monospace;font-size:11px'>"
              '{\n  "mcpServers": {\n    "ai-governance": {\n      "command": "python",\n      "args": ["C:/ai-governance-package/agents/mcp_server.py"]\n    }\n  }\n}'
              "</div>"),
          box("Step 2: How to Use It in Chat (The Layman Experience)",
              "<p>Open any AI project folder in your editor, open the chat sidebar, and type:</p>"
              "<div style='background:#EFF6FF;border-left:4px solid #0284C7;padding:12px;border-radius:4px;margin:10px 0;font-size:14px;font-weight:700;color:#0B2E59'>"
              "&ldquo;Set up AI governance for this project.&rdquo;"
              "</div>"
              "<p style='font-size:13px;line-height:1.6;color:#334155'>The AI assistant automatically discovers the MCP tool <code>ai_governance_auto_setup</code>, invokes it, generates all manifest files, and reports back:<br>"
              "<i style='color:#059669'>\"Governance configured: Inferred High-Risk Agent, 40 active controls bound, CI/CD gates and HTML audit report generated.\"</i></p>")
      ]) +
      alert("Universal Editor Support:", "The exact same MCP server file (<code>agents/mcp_server.py</code>) works seamlessly across Cursor, Claude Desktop, Claude Code, Roo Code, and VS Code.", "info"))

# ------------------------------------------------------------------------------
# 3.1 Testing with the Sample Project
# ------------------------------------------------------------------------------
slide("3.1", C3, "exec", "Testing Sandbox", "Hands-on Testing: Walkthrough Using sample-ai-project",
      "We built a small, realistic sample project so you can verify how governance works without touching any production systems.",
      "C:\\ai-governance-package\\sample-ai-project",
      cols([
          feature(1, "What the Sample App Does (app.py)", 
                  "A simple customer support assistant. It takes a customer query, looks up knowledge in ChromaDB, calls OpenAI, and handles customer email.", "f-navy", "Code"),
          feature(2, "The Libraries (requirements.txt)", 
                  "Contains <code>openai</code> and <code>chromadb</code>. Standard dependencies found in thousands of modern generative AI projects.", "f-green", "Dependencies"),
          feature(3, "Safe Sandbox", 
                  "You can test, delete, modify, or regenerate files inside <code>sample-ai-project</code> freely without any risk.", "f-purple", "Sandbox")
      ], 3) +
      table(["Step Number", "Action You Perform", "Expected Result"],
            [["<b>Test Step 1</b>", "Open <code>sample-ai-project\\app.py</code> in Notepad or your editor.", "Notice it uses OpenAI, ChromaDB, and references customer email."],
             ["<b>Test Step 2</b>", "Run: <code>python agents\\governance_agent.py auto-setup sample-ai-project</code>", "Generates manifest, snapshot, PR gate, cards, and HTML report."],
             ["<b>Test Step 3</b>", "Double click <code>sample-ai-project\\governance-compliance-report.html</code>.", "Interactive compliance report opens in your browser with all checks green."],
             ["<b>Test Step 4</b>", "Run: <code>python agents\\governance_agent.py audit sample-ai-project</code>", "Validates that all governance artifacts are intact and compliant."]],
            [15, 45, 40]) +
      alert("Try it right now:", "You can run <code>python agents/governance_agent.py audit sample-ai-project</code> anytime to verify your project's governance health.", "success"))

# ------------------------------------------------------------------------------
# 3.2 What the Generated YAML Files Infer
# ------------------------------------------------------------------------------
slide("3.2", C3, "mgmt", "YAML Inference", "What Does It Infer Once the YAML Files Are Generated?",
      "When the copilot runs, it creates several YAML and JSON files. Here is what they actually mean and infer in plain English.",
      "ai-project-manifest.yaml | effective-policy-snapshot.json | governance-cards/",
      cols([
          box("1. What the Copilot Inferred from Your Code",
              "<ul style='padding-left:18px;line-height:1.7'>"
              "<li><b>Archetype:</b> It detected OpenAI + ChromaDB + tool execution, so it inferred: <code>autonomous_agent</code>.</li>"
              "<li><b>Risk Tier:</b> Because autonomous agents can execute tools and touch PII, it inferred: <code>tier_3_high</code>.</li>"
              "<li><b>Applicable Overlays:</b> It inferred that the system requires both the <b>High-Risk Tier Overlay</b> (<code>ORG-OVL-RSK-TIER3-001</code>) and the <b>Autonomous Agent Overlay</b> (<code>ORG-OVL-ARC-AGENT-001</code>).</li>"
              "</ul>"),
          box("2. What the Generated Files Actually Represent",
              "<ul style='padding-left:18px;line-height:1.7'>"
              "<li><b>ai-project-manifest.yaml:</b> The identity card of your AI system. It formally records who owns the system, what technology it uses, and which regulatory overlays apply.</li>"
              "<li><b>effective-policy-snapshot.json:</b> The authoritative rulebook. It merges the 61 baseline enterprise controls with the overlays to produce exactly <b>40 active obligations</b>, sealed with an immutable SHA-256 digest.</li>"
              "<li><b>governance-cards/model-card.yaml:</b> Documents the model's accuracy benchmark (>85%) and hallucination ceiling (<4%).</li>"
              "<li><b>governance-cards/data-card.yaml:</b> Documents PII sanitization and 5-year retention rules.</li>"
              "</ul>")
      ]) +
      diagram(
          '<svg viewBox="0 0 1120 130" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Inference Pipeline">'
          '<rect x="20" y="20" width="220" height="90" rx="8" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1.5"/><text x="130" y="50" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:14px;font-weight:700;fill:#0B2E59">Source Code & Imports</text><text x="130" y="70" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;fill:#64748B">openai, chromadb, PII</text><text x="130" y="90" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;font-weight:700;fill:#0284C7">AST Telemetry</text>'
          '<path d="M242,65 L318,65" stroke="#0B2E59" stroke-width="2" fill="none"/>'
          '<rect x="320" y="20" width="220" height="90" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/><text x="430" y="50" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:14px;font-weight:700;fill:#1E3A8A">Automated Inference</text><text x="430" y="70" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;fill:#2563EB">Archetype: Agent</text><text x="430" y="90" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;font-weight:700;fill:#1D4ED8">Risk Tier: Tier 3 High</text>'
          '<path d="M542,65 L618,65" stroke="#0B2E59" stroke-width="2" fill="none"/>'
          '<rect x="620" y="20" width="220" height="90" rx="8" fill="#FEF3C7" stroke="#D97706" stroke-width="1.5"/><text x="730" y="50" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:14px;font-weight:700;fill:#92400E">Rule Merger (resolve.py)</text><text x="730" y="70" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;fill:#B45309">61 Baseline + Overlays</text><text x="730" y="90" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;font-weight:700;fill:#D97706">Monotonic Tightening</text>'
          '<path d="M842,65 L918,65" stroke="#0B2E59" stroke-width="2" fill="none"/>'
          '<rect x="920" y="20" width="180" height="90" rx="8" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5"/><text x="1010" y="50" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:14px;font-weight:700;fill:#166534">Effective Snapshot</text><text x="1010" y="70" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;fill:#15803D">40 Active Obligations</text><text x="1010" y="90" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;font-weight:700;fill:#16A34A">SHA-256 Sealed</text>'
          '</svg>'
      ))

# ------------------------------------------------------------------------------
# 4.1 The Interactive HTML Compliance Audit Report
# ------------------------------------------------------------------------------
slide("4.1", C4, "mgmt", "HTML Audit Report", "The Compliance Report: What Was Done & What Was Checked",
      "Whenever the copilot or audit command runs, it automatically generates a visual, interactive HTML report that anyone can open.",
      "sample-ai-project\\governance-compliance-report.html",
      cols([
          box("How to Open and View the Report",
              "<p>Navigate to your project folder and double-click:</p>"
              "<div style='background:#F1F5F9;padding:10px;border-radius:6px;border:1px solid #CBD5E1;font-family:Consolas,monospace;font-size:13px;font-weight:700;color:#0B2E59;margin:8px 0;'>"
              "sample-ai-project\\governance-compliance-report.html"
              "</div>"
              "<p style='font-size:13px;color:#475569;'>It opens instantly in Chrome, Edge, or Firefox. No web server required!</p>"),
          box("How to Re-generate or Refresh Anytime",
              "<p>To re-run the compliance audit and refresh the report at any time:</p>"
              "<div style='background:#061A33;color:#F8FAFC;padding:10px;border-radius:6px;font-family:Consolas,monospace;font-size:12px;margin:8px 0;'>"
              "python agents/governance_agent.py audit sample-ai-project"
              "</div>"
              "<p style='font-size:13px;color:#475569;'>The audit tool inspects all files and updates the HTML report in 1 second.</p>")
      ]) +
      table(["Check Item in Report", "What Was Checked", "Status", "Automated Action"],
            [["<b>Project Manifest</b>", "Verified <code>ai-project-manifest.yaml</code> exists with system ID & owners.", pill("PASSED", "success"), "CI build proceeds"],
             ["<b>Policy Snapshot</b>", "Verified <code>effective-policy-snapshot.json</code> with SHA-256 integrity seal.", pill("PASSED", "success"), "Enforced at all gates"],
             ["<b>Pre-Commit Scanner</b>", "Verified secret scanning hook is installed in <code>.pre-commit-config.yaml</code>.", pill("PASSED", "success"), "Blocks unencrypted keys"],
             ["<b>CI/CD PR Gate</b>", "Verified GitHub Actions workflow is present in <code>.github/workflows/</code>.", pill("PASSED", "success"), "Locks PR merge on error"],
             ["<b>Model Documentation</b>", "Verified <code>governance-cards/model-card.yaml</code> has benchmark targets.", pill("PASSED", "success"), "Registry promotion cleared"],
             ["<b>Data Documentation</b>", "Verified <code>governance-cards/data-card.yaml</code> has PII & retention rules.", pill("PASSED", "success"), "Legal audit cleared"],
             ["<b>AST Vulnerability Scan</b>", "Scanned Python files for dangerous tool calls and unredacted PII.", pill("PASSED", "success"), "Runtime PEP active"]],
            [22, 43, 15, 20]) +
      alert("Executive & Engineering Friendly:", "This HTML report can be exported as a PDF or printed directly to hand to enterprise auditors, legal teams, or risk committees.", "info"))

# ------------------------------------------------------------------------------
# 4.2 Automated Actions on Non-Compliance
# ------------------------------------------------------------------------------
slide("4.2", C4, "arch", "Automated Enforcement", "What Actions Does It Take If Standards Are Not Followed?",
      "The system does not just write notes; it actively enforces compliance and blocks non-compliant code from reaching production.",
      "plugins/pre-commit | plugins/pull-request | plugins/admission-controller",
      table(["Enforcement Point", "Trigger (What Violates the Rule?)", "Automated Action Taken by System"],
            [["<b>1. Developer Machine (Pre-Commit)</b>", "Developer accidentally stages an OpenAI/Anthropic API key in code.", "<span style='color:#DC2626;font-weight:700'>ABORTS GIT COMMIT</span> (Exit Code 1). Secret cannot leave the workstation."],
             ["<b>2. Pull Request Gate (CI/CD)</b>", "Benchmark accuracy < 85%, hallucination rate > 5%, or copyleft GPL license.", "<span style='color:#DC2626;font-weight:700'>FAILS BUILD & LOCKS PR MERGE</span>. Code cannot be merged into main."],
             ["<b>3. Model Registry Gate</b>", "Model serialized in unsafe Python <code>pickle</code> format or missing Model Card.", "<span style='color:#DC2626;font-weight:700'>BLOCKS MODEL PROMOTION</span> to staging/production registry."],
             ["<b>4. Kubernetes Cluster (Admission)</b>", "Container image lacks cryptographic Cosign signature or is Tier 4 Prohibited.", "<span style='color:#DC2626;font-weight:700'>REJECTS DEPLOYMENT</span> with HTTP 403 Forbidden."],
             ["<b>5. Runtime Agent Interceptor (PEP)</b>", "Agent executes tool > 5 recursive depth or does sensitive action without token.", "<span style='color:#DC2626;font-weight:700'>BLOCKS TOOL CALL</span> in real-time and logs security audit trail."]],
            [28, 37, 35]) +
      cols([
          box("What If You Need an Exception? (The Lawful Fallback)",
              "<p>If legacy code or an emergency hotfix cannot meet a rule immediately, developers <b>cannot</b> bypass the system. Instead, they must submit:</p>"
              "<div style='background:#F1F5F9;padding:8px;border-radius:4px;font-family:Consolas,monospace;font-size:12px;margin:6px 0;'>"
              "project-kit/exception-request.template.yaml"
              "</div>"
              "<p style='font-size:12px;color:#475569;'>Requires compensating controls, max 90-day expiry, and AI Safety Board approval.</p>"),
          box("The Golden Rule: Zero Silent Failures",
              "<p style='font-size:13px;line-height:1.6;'>Every enforcement action gives developers a clear error message explaining exactly which policy failed and the 1-step fix required.</p>")
      ]))

# ------------------------------------------------------------------------------
# 5.1 The Novice Checklist: Pin This to Your Desk
# ------------------------------------------------------------------------------
slide("5.1", CA, "exec", "Checklist", "The 1-Page Novice Cheat Sheet: Everything You Need to Know",
      "Summary of all steps. Follow this simple reference every time you work on an AI project.",
      "C:\\ai-governance-package",
      table(["Step", "What I Need To Do", "Exact Command / Action", "Time"],
            [["<b>1. Setup Git</b>", "Initialize Git in project", "<code>git init</code> (or clone project)", "5s"],
             ["<b>2. Run Copilot</b>", "Execute governance agent", "<code>python C:\\ai-governance-package\\agents\\governance_agent.py auto-setup .</code>", "3s"],
             ["<b>3. Check Report</b>", "View visual audit", "Double-click <code>governance-compliance-report.html</code>", "10s"],
             ["<b>4. Commit to Git</b>", "Save governed state", "<code>git add . && git commit -m \"feat(gov): add AI governance\"</code>", "5s"],
             ["<b>5. Push to GitHub</b>", "Open Pull Request", "<code>git push origin feature/my-feature</code>", "5s"]],
            [12, 28, 48, 12]) +
      cols([
          box("Direct File Links for Quick Reference",
              "<p><b>Master Overview:</b> <a href='file:///C:/ai-governance-package/README.md'>C:\\ai-governance-package\\README.md</a><br>"
              "<b>Sample App Code:</b> <a href='file:///C:/ai-governance-package/sample-ai-project/app.py'>sample-ai-project/app.py</a><br>"
              "<b>HTML Audit Report:</b> <a href='file:///C:/ai-governance-package/sample-ai-project/governance-compliance-report.html'>sample-ai-project/governance-compliance-report.html</a><br>"
              "<b>Copilot Agent Script:</b> <a href='file:///C:/ai-governance-package/agents/governance_agent.py'>agents/governance_agent.py</a><br>"
              "<b>MCP IDE Server:</b> <a href='file:///C:/ai-governance-package/agents/mcp_server.py'>agents/mcp_server.py</a></p>"),
          box("Summary for Leadership & Engineering",
              "<p style='font-size:14px;color:#059669;font-weight:700'>AI Governance is no longer friction.</p>"
              "<p style='font-size:13px;line-height:1.6;margin-top:6px;'>It is fully automated software that runs in 3 seconds, protects your company from legal and security liabilities, and gives developers complete peace of mind.</p>")
      ]) +
      note("Closing line", "That is the complete process. Step 1, setup Git. Step 2, run copilot or MCP. Step 3, view report and commit. You are done."))


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
             .replace("{{DECK_TITLE}}", "Enterprise AI Governance: The Simple Step-by-Step Novice Guide")
             .replace("{{DECK_LABEL}}", "Novice Guide")
             .replace("{{SUBTITLE - domain | data snapshot | source | Prepared by Dwaipayan Mojumder, DD Mon YYYY}}",
                      "Enterprise AI Governance Platform | Step-by-Step Practical Walkthrough | Workspace: C:\\ai-governance-package | October 2026")
             .replace("{{three keywords}}", "copilot, mcp, git, report, actions")
             .replace("{{SLIDES}}", "\n".join(SLIDES)))

    out = out.replace("—", "-").replace("–", "-")
    out = out.replace("dupont", "gov").replace("DuPont", "Gov")
    
    output_path = os.path.join(REPO_ROOT, "AI_Governance_Novice_Guide.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(out)
    
    print(f"[SUCCESS] Generated simplified novice guide HTML at: {output_path}")
    print(f"Total Slides: {len(SLIDES)}")
    return output_path

if __name__ == "__main__":
    build_deck()
