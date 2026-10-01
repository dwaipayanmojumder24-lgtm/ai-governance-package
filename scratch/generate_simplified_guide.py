#!/usr/bin/env python3
"""
Generates the simplified, step-by-step, plain-English HTML slide deck for novices,
focusing directly on:
1. "This is what I need to do" -> Step-by-step clarity.
2. Context of C:\\ai-governance-package on the user's C: drive.
3. The sample project C:\\ai-governance-package\\sample-ai-project for hands-on testing.
4. Method 1: The Autonomous Governance Copilot (agents/governance_agent.py).
5. Method 2: Model Context Protocol (MCP) IDE integration (Cursor, Claude, VS Code).
6. DuPont logo deleted as requested by user.
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

C1 = "Chapter 1: Start Here - What You Have & Your Goal"
C2 = "Chapter 2: Method 1 - The 1-Line Autonomous Copilot"
C3 = "Chapter 3: Method 2 - IDE Integration via Model Context Protocol (MCP)"
C4 = "Chapter 4: What Happened & What to Check"
CA = "Appendix: Everyday Rules & Troubleshooting"

# ------------------------------------------------------------------------------
# 1.1 Start Here: What You Have & The Layman Goal
# ------------------------------------------------------------------------------
slide("1.1", C1, "exec", "Start Here", "The Situation: What You Have & What You Need To Do",
      "You do not need to know governance laws or read 61 control documents. Here is the exact situation and the simple outcome you need.",
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
          box("What Exists on Your Computer Right Now",
              "<ul><li><b>1. The Governance Engine:</b> Located at <code>C:\\ai-governance-package</code>. This has all 61 controls, policies, and automation tools.</li>"
              "<li><b>2. The Test Project:</b> Located at <code>C:\\ai-governance-package\\sample-ai-project</code>. This is a simple customer support AI app (with <code>app.py</code> and <code>requirements.txt</code>) ready for testing.</li></ul>"),
          box("The Two Ways You Can Do This",
              "<ol><li><b>Method 1 (Autonomous Copilot):</b> Open your terminal and run 1 command. The copilot scans the code and sets up everything in 3 seconds.</li>"
              "<li><b>Method 2 (IDE MCP Integration):</b> Open Cursor, Claude Code, or VS Code, and simply type: <i>&ldquo;Set up AI governance for this project.&rdquo;</i></li></ol>")
      ]) +
      note("Opening line", "Welcome. If you are new to this and feel overwhelmed, don't worry. You have two files already on your computer, and you only need to run one command today."))

# ------------------------------------------------------------------------------
# 1.2 The Sample Project Walkthrough
# ------------------------------------------------------------------------------
slide("1.2", C1, "arch", "Sample Project", "Your Playground: The Sample AI Project Explained",
      "We created a realistic, small sample project so you can test governance immediately without touching production code.",
      "C:\\ai-governance-package\\sample-ai-project\\app.py",
      cols([
          feature(1, "The Application File (app.py)", 
                  "A simple customer support AI script. It accepts customer questions, uses an LLM (OpenAI) to generate answers, and checks a local database.", "f-navy", "Code"),
          feature(2, "The Dependencies (requirements.txt)", 
                  "Lists standard AI libraries: <code>openai</code> (for text generation) and <code>chromadb</code> (for vector knowledge search).", "f-green", "Libraries"),
          feature(3, "Personal Data (customer_email)", 
                  "The script handles a customer's email address. Enterprise policy requires that personal data (PII) must be recognized and protected.", "f-amber", "PII")
      ], 3) +
      diagram(
          '<svg viewBox="0 0 1120 140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sample Project Flow">'
          '<defs><marker id="arr" markerWidth="10" markerHeight="10" refX="9" refY="3.6" orient="auto"><path d="M0,0 L9,3.6 L0,7.2 z" fill="#0B2E59"/></marker></defs>'
          '<rect x="20" y="25" width="280" height="85" rx="8" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5"/><text x="160" y="55" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:15px;font-weight:700;fill:#0B2E59">sample-ai-project/</text><text x="160" y="75" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;fill:#475569">app.py + requirements.txt</text><text x="160" y="93" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;font-weight:700;fill:#0284C7">Ungoverned Starter Code</text>'
          '<path d="M302,67 L398,67" stroke="#0B2E59" stroke-width="2" fill="none" marker-end="url(#arr)"/>'
          '<rect x="400" y="15" width="320" height="105" rx="8" fill="#0B2E59"/><rect x="400" y="15" width="320" height="105" rx="8" fill="none" stroke="#E52421" stroke-width="2"/><text x="560" y="48" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:16px;font-weight:700;fill:#fff">Governance Copilot (M0-M9)</text><text x="560" y="72" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;fill:#FCA5A5">Scans imports, detects OpenAI & ChromaDB</text><text x="560" y="90" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;fill:#E2E8F0">Calculates exact matching controls</text>'
          '<path d="M722,67 L818,67" stroke="#0B2E59" stroke-width="2" fill="none" marker-end="url(#arr)"/>'
          '<rect x="820" y="25" width="280" height="85" rx="8" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5"/><text x="960" y="55" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:15px;font-weight:700;fill:#166534">Governed & Compliant</text><text x="960" y="75" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;fill:#15803D">Manifest + Snapshot + CI Gates</text><text x="960" y="93" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:11px;font-weight:700;fill:#16A34A">Ready for Production Deploy</text>'
          '</svg>'
      ) +
      alert("Test Sandbox Ready:", "You can run tests safely against <code>sample-ai-project</code> without worrying about breaking anything. Let's see how to do it in Method 1.", "info"))

# ------------------------------------------------------------------------------
# 2.1 Method 1: The Autonomous Copilot (Step-by-Step)
# ------------------------------------------------------------------------------
slide("2.1", C2, "exec", "Method 1", "Method 1: Run the Copilot (Exactly What You Need To Do)",
      "This is the fastest method. Open your terminal and run one command. The copilot does all the setup in 3 seconds.",
      "C:\\ai-governance-package\\agents\\governance_agent.py",
      cols([
          box("Step 1: Open Your Terminal",
              "<p>Open <b>PowerShell</b> or <b>Command Prompt</b> on your Windows machine.</p>"
              "<p>You can be in any directory.</p>"),
          box("Step 2: Copy and Paste This Command",
              "<div style='background:#061A33;color:#F8FAFC;padding:12px;border-radius:6px;font-family:Consolas,monospace;font-size:13px'>"
              "<span style='color:#4ADE80'>python</span> C:\\ai-governance-package\\agents\\governance_agent.py auto-setup C:\\ai-governance-package\\sample-ai-project"
              "</div>")
      ]) +
      box("Step 3: Watch What the Copilot Outputs Automatically",
          "<div style='background:#061A33;color:#F8FAFC;padding:14px;border-radius:8px;font-family:Consolas,monospace;font-size:13px;line-height:1.6'>"
          "<span style='color:#38BDF8'>[AGENT]</span> Scanning repository at: C:\\ai-governance-package\\sample-ai-project<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Code Telemetry Inferred:<br>"
          "  * Frameworks Detected: chromadb, openai<br>"
          "  * PII Indicators: DETECTED (customer_email found)<br>"
          "  * Inferred Archetype: rag_knowledge (Risk Tier: tier_2_moderate)<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Generating declarative project manifest...<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Resolving deterministic policy snapshot (40 controls active)...<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Installing pre-commit hooks and CI/CD PR gate...<br>"
          "<span style='color:#38BDF8'>[AGENT]</span> Pre-populating starter Model Card & Data Card...<br>"
          "<span style='color:#4ADE80'>[SUCCESS] AUTONOMOUS GOVERNANCE SETUP COMPLETE!</span>"
          "</div>") +
      alert("That is literally it!", "The copilot analyzed the code, wrote your manifest, ran the rule engine, set up your PR gates, and drafted your documentation cards. You typed zero lines of YAML.", "success"))

# ------------------------------------------------------------------------------
# 2.2 What the Copilot Created (Verification)
# ------------------------------------------------------------------------------
slide("2.2", C2, "mgmt", "Method 1 Result", "What Was Created in Your Project Folder",
      "Look inside C:\\ai-governance-package\\sample-ai-project. Here are the 5 items created automatically and what they do.",
      "sample-ai-project/ | ai-project-manifest.yaml | effective-policy-snapshot.json",
      table(["File Created by Copilot", "What It Is in Plain English", "Why It Matters to You"],
            [["<b>ai-project-manifest.yaml</b>", "Your AI system's ID card", "Declares that your system is a RAG chatbot touching customer email."],
             ["<b>effective-policy-snapshot.json</b>", "Your personalized rulebook", "Lists the 40 exact rules (out of 61) that apply to this project, with a SHA-256 tamper-proof seal."],
             ["<b>.pre-commit-config.yaml</b>", "Workstation safety check", "Stops you from accidentally committing plain-text OpenAI API keys."],
             ["<b>.github/workflows/ai-governance-gate.yaml</b>", "Pull Request security gate", "Ensures all AI code has human review and blocks copyleft license legal issues."],
             ["<b>governance-cards/</b>", "Ready-made auditor documentation", "Contains pre-filled <code>model-card.yaml</code> and <code>data-card.yaml</code>."]],
            [30, 25, 45]) +
      cols([
          box("Step 4: Commit These Files to Git",
              "<div style='background:#061A33;color:#F8FAFC;padding:12px;border-radius:6px;font-family:Consolas,monospace;font-size:13px'>"
              "cd C:\\ai-governance-package\\sample-ai-project<br>"
              "<span style='color:#4ADE80'>git add</span> .<br>"
              "<span style='color:#4ADE80'>git commit</span> -m \"feat: add enterprise AI governance\""
              "</div>"),
          box("You Are Now 100% Compliant",
              "<p>Your project is now officially registered in enterprise inventory, protected against security leaks, and ready for audit review.</p>")
      ]))

# ------------------------------------------------------------------------------
# 3.1 Method 2: IDE MCP in Cursor
# ------------------------------------------------------------------------------
slide("3.1", C3, "arch", "Method 2: Cursor", "Method 2: IDE Model Context Protocol in Cursor",
      "If you use Cursor IDE, you never even have to open a terminal. Just chat with your AI assistant.",
      "C:\\ai-governance-package\\agents\\mcp_server.py | Cursor MCP Settings",
      cols([
          box("Step 1: Open Cursor MCP Settings",
              "<ol><li>Open <b>Cursor</b>.</li>"
              "<li>Press <code>Ctrl + Shift + J</code> (or click the Settings gear icon in the top right).</li>"
              "<li>Click <b>Features</b> on the left menu, then select <b>MCP Servers</b>.</li>"
              "<li>Click the <b>+ Add New MCP Server</b> button.</li></ol>"),
          box("Step 2: Enter These Exact Details",
              "<p><b>Name:</b> <code>ai-governance</code></p>"
              "<p><b>Type:</b> <code>command</code></p>"
              "<p><b>Command:</b></p>"
              "<div style='background:#061A33;color:#F8FAFC;padding:10px;border-radius:6px;font-family:Consolas,monospace;font-size:12px'>"
              "python C:/ai-governance-package/agents/mcp_server.py"
              "</div>")
      ]) +
      box("Step 3: Use It in the Cursor Chat Window (The Magic Step!)",
          "<ol><li>Open your project folder in Cursor (e.g. <code>C:\\ai-governance-package\\sample-ai-project</code>).</li>"
          "<li>Press <code>Ctrl + L</code> to open the Cursor Chat.</li>"
          "<li>Type this exact sentence:</li></ol>"
          "<div style='background:#F1F5F9;padding:12px;border-radius:6px;border-left:5px solid #0284C7;font-size:15px;font-weight:700;color:#0B2E59'>"
          "&ldquo;Set up AI governance for this project.&rdquo;"
          "</div>"
          "<p style='margin-top:10px'>Cursor will call the <code>ai_governance_auto_setup</code> tool, inspect your files, generate the manifest and snapshot, and report back that your project is governed!</p>") +
      alert("Zero Terminal Commands:", "With MCP configured in Cursor, governance is literally a 1-sentence chat prompt. The assistant does 100% of the work.", "success"))

# ------------------------------------------------------------------------------
# 3.2 Method 2: IDE MCP in Claude Desktop & Claude Code
# ------------------------------------------------------------------------------
slide("3.2", C3, "arch", "Method 2: Claude", "Method 2: IDE Model Context Protocol in Claude Desktop",
      "If you use Claude Desktop or Claude Code, configure the MCP server in your configuration file.",
      "%APPDATA%\\Claude\\claude_desktop_config.json",
      cols([
          box("Step 1: Open Your Claude Desktop Config",
              "<p>Press <code>Win + R</code>, paste this path, and press Enter:</p>"
              "<div style='background:#061A33;color:#F8FAFC;padding:8px;border-radius:4px;font-family:Consolas,monospace;font-size:12px'>"
              "%APPDATA%\\Claude\\claude_desktop_config.json"
              "</div>"
              "<p style='margin-top:8px'>Open the file in Notepad or VS Code.</p>"),
          box("Step 2: Paste This JSON Snippet",
              "<div style='background:#061A33;color:#F8FAFC;padding:10px;border-radius:6px;font-family:Consolas,monospace;font-size:12px'>"
              "{\n"
              '  "mcpServers": {\n'
              '    "ai-governance": {\n'
              '      "command": "python",\n'
              '      "args": ["C:/ai-governance-package/agents/mcp_server.py"]\n'
              "    }\n"
              "  }\n"
              "}"
              "</div>")
      ]) +
      box("Step 3: Restart Claude & Run It",
          "<ol><li>Close Claude Desktop and reopen it.</li>"
          "<li>Look for the small hammer icon in the bottom right corner showing that <code>ai-governance</code> is active.</li>"
          "<li>Type in the chat:</li></ol>"
          "<div style='background:#F1F5F9;padding:12px;border-radius:6px;border-left:5px solid #059669;font-size:15px;font-weight:700;color:#0B2E59'>"
          "&ldquo;Scan C:/ai-governance-package/sample-ai-project and set up enterprise AI governance.&rdquo;"
          "</div>"
          "<p style='margin-top:8px'>Claude executes the tool and sets up your project files automatically.</p>") +
      alert("Platform Portability:", "The exact same MCP server script works across Cursor, Claude, and VS Code. You never rewrite any governance code.", "info"))

# ------------------------------------------------------------------------------
# 3.3 Method 2: IDE MCP in VS Code (Roo Code / Continue / Cline)
# ------------------------------------------------------------------------------
slide("3.3", C3, "arch", "Method 2: VS Code", "Method 2: IDE Model Context Protocol in VS Code",
      "For VS Code users running AI extensions like Roo Code, Continue, or Cline, configure the MCP tool in your extension settings.",
      "VS Code MCP Settings | agents/mcp_server.py",
      cols([
          feature(1, "Roo Code / Cline", "Open the extension settings, click MCP Servers, and add <code>ai-governance</code> pointing to the python script.", "f-navy", "Settings"),
          feature(2, "Continue Extension", "Add the server to your <code>config.json</code> under the <code>mcpServers</code> section.", "f-green", "Config"),
          feature(3, "Command Path", "Always point to: <code>C:/ai-governance-package/agents/mcp_server.py</code>.", "f-amber", "Path")
      ], 3) +
      box("The Universal MCP Configuration Snippet (Copy-Paste Ready)",
          "<div style='background:#061A33;color:#F8FAFC;padding:14px;border-radius:8px;font-family:Consolas,monospace;font-size:13px;line-height:1.6'>"
          "{\n"
          '  "mcpServers": {\n'
          '    "ai-governance": {\n'
          '      "command": "python",\n'
          '      "args": ["C:/ai-governance-package/agents/mcp_server.py"]\n'
          "    }\n"
          "  }\n"
          "}"
          "</div>") +
      alert("What It Gives You:", "Your AI coding assistant becomes an active Governance Officer that protects your code while you develop.", "success"))

# ------------------------------------------------------------------------------
# 4.1 Everyday Rules & What Happens Next
# ------------------------------------------------------------------------------
slide("4.1", CA, "mgmt", "Everyday Rules", "Everyday Development: The 3 Rules You Need To Know",
      "Once governance is set up, what do you need to keep in mind while writing code? Just these 3 simple rules.",
      "baseline/policies/ | plugins/pull-request/ai_code_review_gate.py",
      cols([
          feature(1, "Rule 1: Never Hardcode API Keys", 
                  "Always use environment variables for OpenAI, Anthropic, or Hugging Face tokens. The pre-commit scanner will stop you if you accidentally leave one in a file.", "f-red", "Secret Safety"),
          feature(2, "Rule 2: Have a Teammate Review AI Code", 
                  "If you use Copilot, Cursor, or Claude to generate code, at least 1 human engineer must approve your Pull Request before merging (ORG-CTL-IPR-002).", "f-navy", "Human Review"),
          feature(3, "Rule 3: Keep Your Snapshot in Git", 
                  "Whenever you change your project settings, re-run the copilot or resolver so your <code>effective-policy-snapshot.json</code> stays in sync with your code.", "f-green", "Snapshot Sync")
      ], 3) +
      table(["If You Encounter This...", "Why It Happened", "The 1-Step Fix"],
            [["<b>Pre-commit warning about API key</b>", "You wrote <code>sk-...</code> in a file", "Move the key to a <code>.env</code> file."],
             ["<b>PR blocked on human review</b>", "AI generation markers detected", "Ask a teammate to click 'Approve' on your PR."],
             ["<b>CI failed on snapshot hash</b>", "You edited manifest without re-running resolver", "Run <code>python project-kit/resolver/resolve.py</code> and commit."],
             ["<b>Need an exception for legacy code</b>", "A control cannot be met immediately", "Fill <code>project-kit/exception-request.template.yaml</code>."]],
            [30, 35, 35]))

# ------------------------------------------------------------------------------
# 5.1 The Novice Checklist
# ------------------------------------------------------------------------------
slide("5.1", CA, "exec", "Checklist", "The 1-Page Layman Checklist: Pin This to Your Desk",
      "Everything you need to remember on a single slide. Follow these 4 steps every time you build an AI application.",
      "C:\\ai-governance-package",
      table(["Step Number", "What You Do", "Command / Action", "Time Needed"],
            [["<b>Step 1</b>", "Run the Copilot on your project", "<code>python C:\\ai-governance-package\\agents\\governance_agent.py auto-setup .</code>", "3 seconds"],
             ["<b>Step 2</b>", "Check that files were created", "Look for <code>ai-project-manifest.yaml</code> and <code>effective-policy-snapshot.json</code>", "10 seconds"],
             ["<b>Step 3</b>", "Commit files to Git", "<code>git add . && git commit -m 'feat: add AI governance'</code>", "5 seconds"],
             ["<b>Step 4</b>", "Push your branch and open PR", "<code>git push origin feature/my-ai-feature</code>", "5 seconds"]],
            [15, 30, 43, 12]) +
      cols([
          box("If You Ever Get Stuck",
              "<p><b>Read the docs:</b> <a href='file:///C:/ai-governance-package/README.md'>C:\\ai-governance-package\\README.md</a><br>"
              "<b>Detailed manual:</b> <a href='file:///C:/ai-governance-package/docs/onboarding-guide.md'>docs/onboarding-guide.md</a><br>"
              "<b>Agentic guide:</b> <a href='file:///C:/ai-governance-package/docs/agentic-governance.md'>docs/agentic-governance.md</a></p>"),
          box("You Are Ready To Ship!",
              "<p style='font-size:15px;color:#059669;font-weight:700'>No more legal questionnaires. No more 50-page spreadsheets.</p>"
              "<p>Governance is now automated code that runs in seconds.</p>")
      ]) +
      note("Closing line", "That is the complete process. Step 1, run the copilot. Step 2, check the files. Step 3, commit to Git. You are done."))


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
             .replace("{{three keywords}}", "copilot, mcp, sample")
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
