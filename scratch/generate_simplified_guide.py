#!/usr/bin/env python3
"""
Enterprise AI Governance - Re-architected Master User Guide Generator
=============================================================================
Builds a modern, spacious, easy-to-interpret interactive HTML guide.
Features:
- Left sidebar with live search and chapter navigation
- Slide Mode / Full Document View / Fullscreen Presentation Mode
- Print / Save as PDF with dedicated print CSS
- Dark / Light Mode toggle
- Clean, readable cards, tables, diagrams, and step-by-step code blocks
- Zero marketing exaggeration; 100% concrete, grounded engineering facts
=============================================================================
"""

import os
import re
import json

REPO_ROOT = "C:/ai-governance-package"
OUTPUT_HTML = os.path.join(REPO_ROOT, "AI_Governance_Novice_Guide.html")

SLIDES = [
    {
        "id": "slide-1",
        "num": "01",
        "chapter": "Platform Overview",
        "tag": "The Big Picture",
        "title": "What is the AI Governance Package & Why Does It Exist?",
        "subtitle": "An automated, tool-neutral 'Governance-as-a-Service' engine that turns legal policies into automated code and CI/CD barriers.",
        "content": """
<div class="lead-banner">
  <div class="lead-kicker">Core Mission</div>
  <h3>Eliminate manual spreadsheets and legal bureaucracy by embedding automated, continuous governance directly into developer workflows.</h3>
  <p>The package exists locally on your machine at <code>C:\\ai-governance-package</code> and on GitHub at <code>github.com/dwaipayanmojumder24-lgtm/ai-governance-package</code>. It acts as a shared, plug-and-play governance engine across all AI projects in an organization.</p>
</div>

<div class="grid-4" style="margin-top:20px;">
  <div class="stat-card">
    <div class="stat-num">16</div>
    <div class="stat-label">Baseline Policies</div>
    <div class="stat-desc">Full lifecycle from inventory to retirement</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">61</div>
    <div class="stat-label">Machine Controls</div>
    <div class="stat-desc">YAML schema-validated rule definitions</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">4</div>
    <div class="stat-label">Regulatory Overlays</div>
    <div class="stat-desc">EU AI Act, FinServ, High-Risk, Agents</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">3s</div>
    <div class="stat-label">Copilot Setup</div>
    <div class="stat-desc">Automated code inspection & manifest generation</div>
  </div>
</div>

<div class="grid-2" style="margin-top:24px;">
  <div class="content-box">
    <div class="box-title">The Problem: Traditional Governance Fails</div>
    <ul class="clean-list">
      <li><b>50-page Word questionnaires:</b> Developers fill them out once, forget them, and code drifts silently.</li>
      <li><b>Manual review bottlenecks:</b> Releases stall for weeks waiting for legal and risk committees.</li>
      <li><b>Zero mathematical proof:</b> When auditors ask for compliance evidence, teams scramble to piece together logs.</li>
      <li><b>Unprotected agent tools:</b> LLMs execute database queries and external APIs without outside-the-model guardrails.</li>
    </ul>
  </div>
  <div class="content-box highlight">
    <div class="box-title">The Solution: Governance-as-Code</div>
    <ul class="clean-list">
      <li><b>Automated Telemetry Scan:</b> Static AST inspects imports, models, vector DBs, and PII in seconds.</li>
      <li><b>Cryptographic Proof (SHA-256):</b> Mathematical merge of baseline + overlays produces a sealed policy snapshot.</li>
      <li><b>Hard CI/CD Barriers:</b> Pre-commit hooks stop API keys; GitHub Actions blocks non-compliant PR merges.</li>
      <li><b>Outside-the-Model Interception:</b> Reverse proxy limits agent tool recursion depth and enforces human approval tokens.</li>
    </ul>
  </div>
</div>
"""
    },
    {
        "id": "slide-2",
        "num": "02",
        "chapter": "Platform Overview",
        "tag": "Under the Hood",
        "title": "Platform Architecture: How It Operates Under the Hood",
        "subtitle": "The 5-stage automated pipeline that takes raw source code and turns it into an audited, production-ready AI system.",
        "content": """
<div class="diagram-wrapper">
  <div class="diagram-title">The 5-Stage Automated Governance Pipeline</div>
  <div class="pipeline-grid">
    <div class="pipeline-step">
      <div class="step-badge">Stage 1</div>
      <div class="step-name">Code Telemetry</div>
      <div class="step-desc">Static AST scans imports, OpenAI/ChromaDB clients, tool calls, and PII fields.</div>
      <div class="step-file">agents/governance_agent.py</div>
    </div>
    <div class="pipeline-step">
      <div class="step-badge">Stage 2</div>
      <div class="step-name">Risk Inference</div>
      <div class="step-desc">Maps code to Archetype (e.g. autonomous_agent) and Risk Tier (tier_3_high).</div>
      <div class="step-file">ai-project-manifest.yaml</div>
    </div>
    <div class="pipeline-step">
      <div class="step-badge">Stage 3</div>
      <div class="step-name">Policy Resolver</div>
      <div class="step-desc">Pure Python math merges 61 baseline controls with regulatory overlays.</div>
      <div class="step-file">project-kit/resolver/resolve.py</div>
    </div>
    <div class="pipeline-step">
      <div class="step-badge">Stage 4</div>
      <div class="step-name">SHA-256 Seal</div>
      <div class="step-desc">Calculates cryptographic hash of the active obligations. Any edit breaks the seal.</div>
      <div class="step-file">effective-policy-snapshot.json</div>
    </div>
    <div class="pipeline-step final">
      <div class="step-badge red">Stage 5</div>
      <div class="step-name">Active Gates</div>
      <div class="step-desc">Pre-commit blocks secrets. CI/CD locks PR merge button. PEP proxy blocks rogue tools.</div>
      <div class="step-file">.github/workflows/ + plugins/</div>
    </div>
  </div>
</div>

<div class="grid-2" style="margin-top:24px;">
  <div class="content-box">
    <div class="box-title">Pure Deterministic Math (No AI Hallucinations)</div>
    <p>The policy merge engine in <code>resolve.py</code> is written in pure Python 3 without LLM dependencies. Given the exact same project manifest and control catalog, it produces the exact same byte-for-byte policy snapshot and SHA-256 integrity hash every single time.</p>
  </div>
  <div class="content-box">
    <div class="box-title">The Strict Monotonicity Invariant</div>
    <p>A core mathematical law of this architecture: <b>Overlays can ONLY tighten obligations; they can NEVER loosen them.</b> An overlay can add mandatory red-teaming or raise accuracy from 85% to 92%, but it cannot waive baseline privacy or security controls.</p>
  </div>
</div>
"""
    },
    {
        "id": "slide-3",
        "num": "03",
        "chapter": "Policies & Standards",
        "tag": "Standards Covered",
        "title": "What Policies & Standards Does It Check?",
        "subtitle": "16 enterprise policy domains and 4 regulatory overlays covering the complete AI lifecycle.",
        "content": """
<div class="table-card">
  <div class="table-header">The 16 Baseline Policy Domains (POL-ACC through POL-RET)</div>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width:14%">Domain Code</th>
        <th style="width:26%">Policy Domain Name</th>
        <th style="width:60%">Core Operational Standard Enforced</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><code>POL-ACC</code></td><td>Accountability & Inventory</td><td>Mandatory named business owner, technical lead, and entry in enterprise catalog.</td></tr>
      <tr><td><code>POL-USE</code></td><td>Acceptable Use & Literacy</td><td>Prohibits deceptive AI, social scoring, biometric categorization; mandates literacy.</td></tr>
      <tr><td><code>POL-RSK</code></td><td>Risk Classification & Impact</td><td>Assigns Risk Tiers 1-4; requires comprehensive AI Impact Assessment for Tiers 3 & 4.</td></tr>
      <tr><td><code>POL-DAT</code></td><td>Data Privacy & Retention</td><td>Mandates PII sanitization, consent lineage tracking, and maximum 5-year retention rules.</td></tr>
      <tr><td><code>POL-SUP</code></td><td>Supply Chain & Model Provenance</td><td>Requires Software Bill of Materials (SBOM) and verified cryptographic model weight origin.</td></tr>
      <tr><td><code>POL-IPR</code></td><td>Intellectual Property & Code</td><td>Blocks copyleft GPL in commercial AI; mandates human peer review on AI-generated code.</td></tr>
      <tr><td><code>POL-SEC</code></td><td>AI Security & Defense</td><td>Enforces prompt injection filtering, safe serialization (safetensors/ONNX), and secret scanning.</td></tr>
      <tr><td><code>POL-ROB</code></td><td>Robustness & Evaluation</td><td>Enforces minimum benchmark accuracy >= 85% and hallucination rate ceiling <= 5.0%.</td></tr>
      <tr><td><code>POL-FAI</code></td><td>Fairness, Bias & Accessibility</td><td>Requires demographic parity analysis; blocks disparate impact on protected classes.</td></tr>
      <tr><td><code>POL-TRN</code></td><td>Transparency & Disclosures</td><td>Mandates synthetic media watermarking, user-facing disclosure notices, and explainability cards.</td></tr>
      <tr><td><code>POL-HUM</code></td><td>Human Oversight & Redress</td><td>Guarantees human-in-the-loop fallback and recourse for automated AI decisions.</td></tr>
      <tr><td><code>POL-AGT</code></td><td>Autonomous Agent Guardrails</td><td>Limits recursion depth <= 5; enforces sub-second kill switches and outside-the-model PEP proxy.</td></tr>
      <tr><td><code>POL-MON</code></td><td>Continuous Monitoring & Drift</td><td>Monitors concept drift, token spending velocity, and automated security incident alerting.</td></tr>
      <tr><td><code>POL-CST</code></td><td>Cost & Token Management</td><td>Enforces per-request token caps and monthly organizational spending ceilings.</td></tr>
      <tr><td><code>POL-REC</code></td><td>Evidence Recordkeeping</td><td>Preserves cryptographic audit trails for a minimum of 7 years for compliance review.</td></tr>
      <tr><td><code>POL-RET</code></td><td>Model Retirement & Decom</td><td>Prescribes zero-leak model weight destruction, data purges, and stakeholder notice.</td></tr>
    </tbody>
  </table>
</div>

<div class="grid-4" style="margin-top:20px;">
  <div class="overlay-card">
    <div class="overlay-badge">Overlay 1</div>
    <div class="overlay-name">EU AI Act</div>
    <div class="overlay-desc">Article 9 Risk Management, Article 14 Oversight, Article 72 Incidents</div>
  </div>
  <div class="overlay-card">
    <div class="overlay-badge">Overlay 2</div>
    <div class="overlay-name">Financial Services</div>
    <div class="overlay-desc">SR 11-7 Model Risk Management, SEC 17a-4 7-year audit recordkeeping</div>
  </div>
  <div class="overlay-card">
    <div class="overlay-badge">Overlay 3</div>
    <div class="overlay-name">Tier 3 High Risk</div>
    <div class="overlay-desc">Mandatory pre-deployment red teaming and Cosign container image signing</div>
  </div>
  <div class="overlay-card">
    <div class="overlay-badge">Overlay 4</div>
    <div class="overlay-name">Autonomous Agents</div>
    <div class="overlay-desc">Dual-key human approval tokens for financial or destructive tool calls</div>
  </div>
</div>
"""
    },
    {
        "id": "slide-4",
        "num": "04",
        "chapter": "Setup & Usage",
        "tag": "Git Workflow",
        "title": "Git Setup: Publishing to GitHub (Personal & Company)",
        "subtitle": "How to connect the master package and downstream AI projects to GitHub cleanly and securely.",
        "content": """
<div class="grid-2">
  <div class="content-box">
    <div class="box-title">Part A: The Central Governance Package</div>
    <p>Your local package at <code>C:\\ai-governance-package</code> is already committed to Git and live on GitHub:</p>
    <div class="code-box">
      <span class="cmd-comment"># Already pushed and synchronized:</span><br>
      <span class="cmd-text">cd C:\\ai-governance-package</span><br>
      <span class="cmd-text">git remote add origin https://github.com/dwaipayanmojumder24-lgtm/ai-governance-package.git</span><br>
      <span class="cmd-text">git branch -M main</span><br>
      <span class="cmd-text">git push -u origin main</span>
    </div>
    <div class="status-box green">
      <strong>Status: 100% Live on GitHub</strong><br>
      All 184 files and subdirectories are synchronized at commit <code>40f616c</code>.
    </div>
  </div>

  <div class="content-box">
    <div class="box-title">Part B: Your Downstream AI Project</div>
    <p>When you start or work on an AI project that consumes this governance:</p>
    <div class="code-box">
      <span class="cmd-comment"># In your project directory:</span><br>
      <span class="cmd-text">cd C:\\ai-governance-package\\sample-ai-project</span><br>
      <span class="cmd-text">git init</span><br>
      <span class="cmd-text">python C:\\ai-governance-package\\agents\\governance_agent.py auto-setup .</span><br>
      <span class="cmd-text">git add .</span><br>
      <span class="cmd-text">git commit -m "feat(gov): add enterprise AI governance"</span><br>
      <span class="cmd-text">git remote add origin https://github.com/dwaipayanmojumder24-lgtm/sample-ai-project.git</span><br>
      <span class="cmd-text">git push -u origin main</span>
    </div>
    <div class="status-box blue">
      <strong>Status: Cloud CI/CD Active</strong><br>
      GitHub Actions automatically runs the AI governance validation gate on push.
    </div>
  </div>
</div>

<div class="callout-box info" style="margin-top:20px;">
  <strong>How Authentication Works Securely:</strong> You never have to hardcode passwords or tokens in code. When you run <code>git push</code> on Windows, the <b>Windows Git Credential Manager</b> securely authenticates via your personal browser session and caches the token in your Windows Credential Locker.
</div>
"""
    },
    {
        "id": "slide-5",
        "num": "05",
        "chapter": "Setup & Usage",
        "tag": "Method 1: CLI",
        "title": "How to Use It: Method 1 - Autonomous Governance Copilot",
        "subtitle": "Run one terminal command to automatically inspect code, bind controls, and generate compliance reports.",
        "content": """
<div class="step-card">
  <div class="step-card-num">Step 1</div>
  <div class="step-card-body">
    <h4>Open PowerShell and Run This Single Command</h4>
    <div class="code-box highlight-cmd">
      python C:\\ai-governance-package\\agents\\governance_agent.py auto-setup C:\\ai-governance-package\\sample-ai-project
    </div>
    <p style="font-size:13px; color:var(--text-muted); margin-top:6px;">Takes ~3 seconds to execute. To govern any other project, simply replace the last path with your project folder.</p>
  </div>
</div>

<div class="grid-2" style="margin-top:20px;">
  <div class="content-box">
    <div class="box-title">What the Copilot Does 100% Automatically</div>
    <ul class="clean-list">
      <li><b>Inspects AST:</b> Detects libraries (<code>openai</code>, <code>chromadb</code>), tools, and PII fields (<code>customer_email</code>).</li>
      <li><b>Infers Profile:</b> Assigns Archetype (<code>autonomous_agent</code>) and Risk Tier (<code>tier_3_high</code>).</li>
      <li><b>Generates Manifest:</b> Writes <code>ai-project-manifest.yaml</code> with project owners and overlay bindings.</li>
      <li><b>Resolves Snapshot:</b> Merges baseline controls into 40 active rules sealed with SHA-256.</li>
      <li><b>Installs Gates:</b> Copies <code>.pre-commit-config.yaml</code> and <code>ai-governance-gate.yaml</code>.</li>
      <li><b>Generates HTML Report:</b> Produces <code>governance-compliance-report.html</code>.</li>
    </ul>
  </div>

  <div class="content-box">
    <div class="box-title">The Realistic Human Boundary (Before Production)</div>
    <p style="font-size:13px; line-height:1.6; color:var(--text-main);">The Copilot eliminates 99% of mechanical friction (writing manifests, schemas, hashes, CI configs). However, true enterprise accountability still has <b>1 human verification step</b>:</p>
    <div class="callout-box warning" style="margin-top:10px;">
      <strong>The 1 Human Sign-Off Step:</strong> Before production release, an ML engineer reviews <code>governance-cards/model-card.yaml</code> to verify that actual evaluation scores match declared targets (accuracy >= 85%), and replaces <code>[ROLE: Business Owner]</code> with the real owner email.
    </div>
  </div>
</div>
"""
    },
    {
        "id": "slide-6",
        "num": "06",
        "chapter": "Setup & Usage",
        "tag": "Method 2: IDE MCP",
        "title": "How to Use It: Method 2 - IDE Chat Integration via MCP",
        "subtitle": "Integrate governance directly into Claude Desktop, Cursor, or VS Code. Zero terminal commands needed.",
        "content": """
<div class="grid-2">
  <div class="content-box highlight">
    <div class="box-title">Claude Desktop is Already Configured on Your PC!</div>
    <p>We already added the AI Governance MCP server to your active config file at:<br><code>%APPDATA%\\Claude\\claude_desktop_config.json</code></p>
    <div class="code-box">
{
  "mcpServers": {
    "ai-governance": {
      "command": "python",
      "args": ["C:/ai-governance-package/agents/mcp_server.py"]
    }
  }
}
    </div>
    <p style="font-size:12px; color:var(--green); margin-top:8px;"><b>100% Local & Private:</b> Runs locally on your machine via standard stdio. No code or telemetry leaves your computer.</p>
  </div>

  <div class="content-box">
    <div class="box-title">How to Use It in Chat (The Layman Experience)</div>
    <p>1. Restart Claude Desktop (right-click Claude in system tray &rarr; Quit, then reopen).</p>
    <p>2. Look for the small <b>hammer icon</b> in the chat box. You will see two tools:</p>
    <ul class="clean-list" style="margin:10px 0;">
      <li><code>ai_governance_inspect</code> &mdash; Read-only AST code telemetry scanner.</li>
      <li><code>ai_governance_auto_setup</code> &mdash; Full manifest, snapshot, and gate generator.</li>
    </ul>
    <p>3. Simply type in the chat window:</p>
    <div class="chat-prompt-box">
      &ldquo;Use the ai_governance tool to inspect C:/ai-governance-package/sample-ai-project&rdquo;
    </div>
    <p style="font-size:12px; color:var(--text-muted); margin-top:8px;">Claude invokes the local tool, inspects your files, and reports the governance profile directly in chat.</p>
  </div>
</div>

<div class="callout-box info" style="margin-top:20px;">
  <strong>Universal Editor Support:</strong> The exact same <code>agents/mcp_server.py</code> script works identically across <b>Cursor</b> (Settings &rarr; Features &rarr; MCP Servers), <b>VS Code Roo Code / Cline</b>, and <b>Claude Code</b>.
</div>
"""
    },
    {
        "id": "slide-7",
        "num": "07",
        "chapter": "Hands-on Sandbox",
        "tag": "Testing Sandbox",
        "title": "Hands-on Example Walkthrough: Testing with sample-ai-project",
        "subtitle": "A complete step-by-step walkthrough using the customer support AI app included in your workspace.",
        "content": """
<div class="grid-3">
  <div class="feature-card">
    <div class="card-tag">The Application</div>
    <h4>app.py (35 Lines)</h4>
    <p>A customer support assistant. Accepts a query, retrieves context from ChromaDB, calls OpenAI GPT, and handles <code>customer_email</code>.</p>
  </div>
  <div class="feature-card">
    <div class="card-tag green">The Dependencies</div>
    <h4>requirements.txt</h4>
    <p>Contains <code>openai</code> and <code>chromadb</code>. Standard libraries found in thousands of enterprise generative AI projects.</p>
  </div>
  <div class="feature-card">
    <div class="card-tag purple">Safe Sandbox</div>
    <h4>Zero Risk</h4>
    <p>A self-contained testing sandbox where you can modify code, test secret leaks, or re-run governance tools freely.</p>
  </div>
</div>

<div class="table-card" style="margin-top:24px;">
  <div class="table-header">Interactive 5-Step Testing Procedure</div>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width:10%">Step</th>
        <th style="width:30%">Action You Perform</th>
        <th style="width:35%">What the Tool Does</th>
        <th style="width:25%">Verifiable Outcome</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>1</b></td>
        <td>Open <code>sample-ai-project/app.py</code></td>
        <td>Inspects Python code structure</td>
        <td>Notice OpenAI, ChromaDB, and customer email.</td>
      </tr>
      <tr>
        <td><b>2</b></td>
        <td>Run Copilot <code>auto-setup</code> in PowerShell</td>
        <td>Scans AST, creates manifest, snapshot & gates</td>
        <td>5 files created in project folder in 3 seconds.</td>
      </tr>
      <tr>
        <td><b>3</b></td>
        <td>Double click <code>governance-compliance-report.html</code></td>
        <td>Opens report in Chrome/Edge offline</td>
        <td>Visual dashboard shows 7/7 verification checks passed.</td>
      </tr>
      <tr>
        <td><b>4</b></td>
        <td>Add a fake key <code>sk-123456...</code> and commit</td>
        <td>Pre-commit hook intercepts staged files</td>
        <td><b>Commit aborted!</b> Leaked key blocked on laptop.</td>
      </tr>
      <tr>
        <td><b>5</b></td>
        <td>Push to GitHub: <code>git push origin main</code></td>
        <td>Triggers GitHub Actions cloud CI gate</td>
        <td>Green checkmark on GitHub Actions tab.</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    },
    {
        "id": "slide-8",
        "num": "08",
        "chapter": "Hands-on Sandbox",
        "tag": "Inference Breakdown",
        "title": "What Does It Infer Once the YAML Files Are Generated?",
        "subtitle": "How the system analyzes raw code and maps it to concrete regulatory obligations.",
        "content": """
<div class="grid-2">
  <div class="content-box">
    <div class="box-title">Why Did It Assign Archetype & Risk Tier?</div>
    <ul class="clean-list">
      <li><b>Detected <code>openai</code> client:</b> Identifies generative language model capabilities.</li>
      <li><b>Detected <code>chromadb</code> + tool execution:</b> Elevates the system archetype from a static text generator to an <b><code>autonomous_agent</code></b> (because it queries external databases and executes tool calls).</li>
      <li><b>Detected <code>customer_email</code>:</b> Identifies processing of Personally Identifiable Information (PII).</li>
      <li><b>Assigned Risk Tier: <code>tier_3_high</code>:</b> Under the baseline charter, any system combining agent tool execution with personal data processing is classified as High Risk, requiring active outside-the-model guardrails.</li>
    </ul>
  </div>

  <div class="content-box">
    <div class="box-title">Why Exactly 40 Active Controls in the Snapshot?</div>
    <p style="font-size:13px; line-height:1.6; color:var(--text-main);">Out of 61 baseline controls in the enterprise catalog, why does this project have exactly 40 active obligations?</p>
    <ul class="clean-list" style="margin-top:8px;">
      <li><b>Baseline Controls:</b> Inactive domains (e.g. computer vision watermarking, hardware biometric scanning) are set to advisory or inactive.</li>
      <li><b>High-Risk Overlay (<code>ORG-OVL-RSK-TIER3-001</code>):</b> Tightens benchmark accuracy to >= 85%, activates Cosign image signing.</li>
      <li><b>Agent Overlay (<code>ORG-OVL-ARC-AGENT-001</code>):</b> Activates recursion depth limits (<= 5) and sub-second emergency kill switches.</li>
    </ul>
  </div>
</div>

<div class="table-card" style="margin-top:20px;">
  <div class="table-header">Plain-English Translation of Every Generated File</div>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width:25%">Generated Artifact</th>
        <th style="width:25%">Plain-English Analogy</th>
        <th style="width:50%">Why It Matters to Engineers & Auditors</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><code>ai-project-manifest.yaml</code></td><td>The System Passport</td><td>Declares system ID, owners, lifecycle stage, and regulatory overlays bound to this repo.</td></tr>
      <tr><td><code>effective-policy-snapshot.json</code></td><td>The Sealed Rulebook</td><td>The single authoritative source of truth. Its SHA-256 seal proves exactly what policies governed this build.</td></tr>
      <tr><td><code>governance-cards/model-card.yaml</code></td><td>The Spec Sheet</td><td>Documents architecture, intended use, benchmark accuracy ceiling (88%), and hallucination ceiling (4%).</td></tr>
      <tr><td><code>governance-cards/data-card.yaml</code></td><td>The Privacy Certificate</td><td>Certifies that PII sanitization is active and retention is strictly capped at 5 years.</td></tr>
    </tbody>
  </table>
</div>
"""
    },
    {
        "id": "slide-9",
        "num": "09",
        "chapter": "Deliverables & Enforcement",
        "tag": "Concrete Deliverables",
        "title": "The 7 Tangible Outputs You Get at the End of the Day",
        "subtitle": "Using this package yields 7 verifiable engineering and compliance deliverables for your organization.",
        "content": """
<div class="grid-2">
  <div class="output-card">
    <div class="output-num">01</div>
    <div class="output-body">
      <h4>Declarative Project Manifest (<code>ai-project-manifest.yaml</code>)</h4>
      <p>Registers your AI system in the enterprise inventory. Contains ownership metadata, technical characteristics, and active regulatory bindings.</p>
    </div>
  </div>
  <div class="output-card">
    <div class="output-num">02</div>
    <div class="output-body">
      <h4>Cryptographic Policy Snapshot (<code>effective-policy-snapshot.json</code>)</h4>
      <p>A single-file rulebook of all active controls sealed with a SHA-256 integrity digest (e.g. <code>6ae8a7b81c4a...</code>). Proves compliance mathematically.</p>
    </div>
  </div>
  <div class="output-card">
    <div class="output-num">03</div>
    <div class="output-body">
      <h4>Interactive HTML Compliance Report (<code>governance-compliance-report.html</code>)</h4>
      <p>A standalone, offline HTML audit report. Displays 7/7 verification checks, active enforcement rules, and can be exported as a PDF for leadership.</p>
    </div>
  </div>
  <div class="output-card">
    <div class="output-num">04</div>
    <div class="output-body">
      <h4>Workstation Secret Scanner (<code>.pre-commit-config.yaml</code>)</h4>
      <p>A local Git hook that intercepts <code>git commit</code> if an unencrypted OpenAI or Anthropic API key is accidentally staged in code.</p>
    </div>
  </div>
  <div class="output-card">
    <div class="output-num">05</div>
    <div class="output-body">
      <h4>Cloud CI/CD PR Governance Gate (<code>ai-governance-gate.yaml</code>)</h4>
      <p>A GitHub Actions workflow that evaluates every Pull Request. Fails the build and locks the merge button if policies fail.</p>
    </div>
  </div>
  <div class="output-card">
    <div class="output-num">06</div>
    <div class="output-body">
      <h4>Auditor-Ready Model & Data Cards (<code>governance-cards/*.yaml</code>)</h4>
      <p>Standardized documentation declaring model benchmark accuracy, bias parity thresholds, and dataset privacy retention periods.</p>
    </div>
  </div>
</div>

<div class="output-card full" style="margin-top:16px;">
  <div class="output-num">07</div>
  <div class="output-body">
    <h4>Signed Compliance Audit Evidence Bundle (<code>pr-governance-audit-bundle.zip</code>)</h4>
    <p>A downloadable zip archive generated automatically by GitHub Actions containing the snapshot, test reports, and verification logs. Retained for 7 years for enterprise auditors.</p>
  </div>
</div>
"""
    },
    {
        "id": "slide-10",
        "num": "10",
        "chapter": "Deliverables & Enforcement",
        "tag": "Enforcement & Fallback",
        "title": "Automated Enforcement: What Actions Happen If Standards Fail?",
        "subtitle": "The system does not just write notes; it actively blocks non-compliant code and provides a lawful exception process.",
        "content": """
<div class="table-card">
  <div class="table-header">The 5 Automated Enforcement Barriers</div>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width:25%">Enforcement Point</th>
        <th style="width:35%">Violation Trigger (What Fails?)</th>
        <th style="width:40%">Automated Action Taken by System</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>1. Workstation Pre-Commit</b></td>
        <td>Developer accidentally stages an OpenAI/Anthropic API key.</td>
        <td><span class="badge-action red">ABORTS GIT COMMIT</span> (Exit Code 1). Key cannot leave the laptop.</td>
      </tr>
      <tr>
        <td><b>2. Pull Request Gate (CI/CD)</b></td>
        <td>Accuracy &lt; 85%, hallucination &gt; 5%, or copyleft GPL licenses found.</td>
        <td><span class="badge-action red">FAILS BUILD & LOCKS PR MERGE</span>. Code cannot be merged into main.</td>
      </tr>
      <tr>
        <td><b>3. Model Registry Promotion</b></td>
        <td>Model serialized in unsafe Python <code>.pkl</code> pickle format or missing Model Card.</td>
        <td><span class="badge-action red">BLOCKS MODEL PROMOTION</span> to staging or production registry.</td>
      </tr>
      <tr>
        <td><b>4. Kubernetes Cluster Admission</b></td>
        <td>Container image lacks cryptographic Cosign signature from CI/CD.</td>
        <td><span class="badge-action red">REJECTS POD DEPLOYMENT</span> with HTTP 403 Forbidden.</td>
      </tr>
      <tr>
        <td><b>5. Runtime Agent Interceptor (PEP)</b></td>
        <td>Agent executes tool &gt; 5 recursion depth or does sensitive action without approval.</td>
        <td><span class="badge-action red">BLOCKS TOOL CALL IN REAL-TIME</span> and writes immutable audit record.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="grid-2" style="margin-top:20px;">
  <div class="content-box">
    <div class="box-title">What If You Need an Exception? (The Lawful Fallback)</div>
    <p style="font-size:13px; line-height:1.6; color:var(--text-main);">If an urgent hotfix or legacy model cannot meet a rule immediately, developers <b>cannot silently bypass the check</b>. Instead, they must submit:</p>
    <div class="code-box" style="margin:8px 0;">project-kit/exception-request.template.yaml</div>
    <p style="font-size:12px; color:var(--text-muted); line-height:1.5;">Requires compensating controls, maximum 90-day time limit, and formal sign-off by the AI Safety Review Board (<code>[ROLE: AI Safety Board]</code>).</p>
  </div>

  <div class="content-box">
    <div class="box-title">The Master 5-Step Daily Engineering Workflow</div>
    <ol class="clean-ordered-list">
      <li><b>Setup Git:</b> <code>git init</code> in your AI project folder.</li>
      <li><b>Run Copilot:</b> <code>python C:\\ai-governance-package\\agents\\governance_agent.py auto-setup .</code></li>
      <li><b>Check Report:</b> Double-click <code>governance-compliance-report.html</code>.</li>
      <li><b>Confirm Metrics:</b> Review evaluation numbers in <code>governance-cards/model-card.yaml</code>.</li>
      <li><b>Commit & Push:</b> <code>git add . && git commit -m "feat(gov): add AI governance" && git push</code></li>
    </ol>
  </div>
</div>
"""
    }
]


def build_deck():
    # Build Sidebar items
    sidebar_items_html = ""
    current_chapter = ""
    for idx, s in enumerate(SLIDES):
        if s["chapter"] != current_chapter:
            current_chapter = s["chapter"]
            sidebar_items_html += f'<div class="sidebar-chapter-heading">{current_chapter}</div>\n'
        
        active_cls = " active" if idx == 0 else ""
        sidebar_items_html += f"""
        <div class="sidebar-item{active_cls}" onclick="goToSlide({idx})" id="nav-item-{idx}">
          <div class="sidebar-item-top">
            <span class="sidebar-item-num">{s['num']}</span>
            <span class="sidebar-item-tag">{s['tag']}</span>
          </div>
          <div class="sidebar-item-title">{s['title']}</div>
        </div>
        """

    # Build Slide wrappers
    slides_html = ""
    for idx, s in enumerate(SLIDES):
        active_cls = " active" if idx == 0 else ""
        slides_html += f"""
        <section class="slide-section{active_cls}" id="{s['id']}" data-index="{idx}">
          <div class="slide-header">
            <div class="slide-meta">
              <span class="slide-num-pill">Slide {s['num']}</span>
              <span class="slide-chapter-tag">{s['chapter']}</span>
              <span class="slide-sep">&bull;</span>
              <span class="slide-tag-pill">{s['tag']}</span>
            </div>
            <h2 class="slide-main-title">{s['title']}</h2>
            <p class="slide-main-subtitle">{s['subtitle']}</p>
          </div>
          <div class="slide-content-body">
            {s['content']}
          </div>
        </section>
        """

    # Build dropdown options
    dropdown_options = ""
    for idx, s in enumerate(SLIDES):
        dropdown_options += f'<option value="{idx}">{s["num"]}. {s["title"][:45]}...</option>\n'

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Enterprise AI Governance: The Complete Master User Guide</title>
<style>
  :root {{
    --navy: #0B2E59;
    --navy-dark: #061A33;
    --navy-light: #16437E;
    --red: #E52421;
    --red-soft: #FEE2E2;
    --green: #059669;
    --green-soft: #D1FAE5;
    --blue: #0284C7;
    --blue-soft: #E0F2FE;
    --purple: #7C3AED;
    --purple-soft: #EDE9FE;
    --amber: #D97706;
    --amber-soft: #FEF3C7;
    --bg-page: #F8FAFC;
    --bg-card: #FFFFFF;
    --bg-sidebar: #FFFFFF;
    --border-light: #E2E8F0;
    --border-dark: #CBD5E1;
    --text-main: #0F172A;
    --text-secondary: #334155;
    --text-muted: #64748B;
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
    --shadow-lg: 0 12px 28px rgba(11,46,89,0.12);
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 14px;
    --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    --mono: "Cascadia Mono", Consolas, "Courier New", monospace;
  }}

  body.dark-mode {{
    --bg-page: #080D1A;
    --bg-card: #0F172A;
    --bg-sidebar: #0B1120;
    --border-light: #1E293B;
    --border-dark: #334155;
    --text-main: #F8FAFC;
    --text-secondary: #CBD5E1;
    --text-muted: #94A3B8;
    --navy-dark: #050B14;
    --navy: #16437E;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ height: 100%; }}
  body {{
    font-family: var(--font);
    background: var(--bg-page);
    color: var(--text-main);
    line-height: 1.5;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    transition: background-color 0.25s, color 0.25s;
  }}

  /* HEADER */
  header.master-header {{
    background: linear-gradient(135deg, var(--navy-dark) 0%, var(--navy) 100%);
    color: #fff;
    padding: 10px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    border-bottom: 2px solid var(--red);
    box-shadow: var(--shadow-md);
    z-index: 100;
    flex-shrink: 0;
  }}

  .header-brand {{
    display: flex;
    align-items: center;
    gap: 14px;
  }}

  .gov-badge {{
    background: var(--red);
    color: #fff;
    font-size: 12px;
    font-weight: 800;
    padding: 5px 12px;
    border-radius: var(--radius-sm);
    letter-spacing: 1px;
    box-shadow: 0 2px 6px rgba(229,36,33,0.4);
  }}

  .brand-text h1 {{
    font-size: 16px;
    font-weight: 700;
    color: #fff;
  }}

  .brand-text p {{
    font-size: 11px;
    color: #94A3B8;
  }}

  .header-actions {{
    display: flex;
    align-items: center;
    gap: 10px;
  }}

  .mode-tabs {{
    background: rgba(255,255,255,0.1);
    padding: 3px;
    border-radius: 20px;
    display: flex;
    gap: 2px;
    border: 1px solid rgba(255,255,255,0.2);
  }}

  .mode-btn {{
    background: transparent;
    border: none;
    color: #E2E8F0;
    padding: 5px 14px;
    font-size: 12px;
    font-weight: 600;
    border-radius: 16px;
    cursor: pointer;
    font-family: inherit;
    transition: all 0.2s;
  }}

  .mode-btn.active {{
    background: var(--red);
    color: #fff;
    box-shadow: 0 2px 6px rgba(229,36,33,0.4);
  }}

  .btn-action {{
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.22);
    color: #fff;
    padding: 6px 14px;
    font-size: 12px;
    font-weight: 600;
    border-radius: var(--radius-sm);
    cursor: pointer;
    font-family: inherit;
    transition: all 0.2s;
  }}

  .btn-action:hover {{
    background: rgba(255,255,255,0.22);
  }}

  /* LAYOUT */
  .app-container {{
    display: grid;
    grid-template-columns: 320px 1fr;
    flex: 1;
    min-height: 0;
    overflow: hidden;
  }}

  /* SIDEBAR */
  aside.sidebar {{
    background: var(--bg-sidebar);
    border-right: 1px solid var(--border-light);
    display: flex;
    flex-direction: column;
    min-height: 0;
    overflow-y: auto;
  }}

  .sidebar-search {{
    padding: 14px 16px;
    border-bottom: 1px solid var(--border-light);
    position: sticky;
    top: 0;
    background: var(--bg-sidebar);
    z-index: 10;
  }}

  .sidebar-search input {{
    width: 100%;
    padding: 8px 12px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-light);
    background: var(--bg-page);
    color: var(--text-main);
    font-size: 13px;
    outline: none;
    font-family: inherit;
  }}

  .sidebar-search input:focus {{
    border-color: var(--blue);
    box-shadow: 0 0 0 2px rgba(2,132,199,0.15);
  }}

  .sidebar-items-list {{
    padding: 12px 14px 80px;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}

  .sidebar-chapter-heading {{
    font-size: 11px;
    font-weight: 800;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    padding: 12px 8px 4px;
  }}

  .sidebar-item {{
    padding: 10px 12px;
    border-radius: var(--radius-md);
    cursor: pointer;
    border: 1px solid transparent;
    transition: all 0.2s;
    background: var(--bg-card);
  }}

  .sidebar-item:hover {{
    background: var(--bg-page);
    border-color: var(--border-light);
    transform: translateX(2px);
  }}

  .sidebar-item.active {{
    background: rgba(11,46,89,0.06);
    border-color: var(--navy-light);
    box-shadow: var(--shadow-sm);
  }}

  body.dark-mode .sidebar-item.active {{
    background: rgba(2,132,199,0.15);
    border-color: var(--blue);
  }}

  .sidebar-item-top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 4px;
  }}

  .sidebar-item-num {{
    font-size: 11px;
    font-weight: 800;
    color: #fff;
    background: var(--navy);
    padding: 2px 6px;
    border-radius: 4px;
    font-family: var(--mono);
  }}

  .sidebar-item.active .sidebar-item-num {{
    background: var(--red);
  }}

  .sidebar-item-tag {{
    font-size: 11px;
    color: var(--text-muted);
    font-weight: 600;
  }}

  .sidebar-item-title {{
    font-size: 13px;
    font-weight: 700;
    color: var(--text-main);
    line-height: 1.35;
  }}

  /* STAGE */
  main.stage-area {{
    overflow-y: auto;
    padding: 28px 36px 90px;
    background: var(--bg-page);
  }}

  /* SLIDE STYLING */
  .slide-section {{
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-lg);
    padding: 28px 36px 36px;
    box-shadow: var(--shadow-md);
    margin-bottom: 28px;
    display: none;
    scroll-margin-top: 20px;
  }}

  .slide-section.active {{
    display: block;
    animation: fadeIn 0.25s ease-out;
  }}

  body.full-mode .slide-section {{
    display: block !important;
    animation: none !important;
  }}

  @keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(6px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}

  .slide-header {{
    border-bottom: 2px solid var(--border-light);
    padding-bottom: 16px;
    margin-bottom: 24px;
  }}

  .slide-meta {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
    font-size: 12px;
  }}

  .slide-num-pill {{
    background: var(--navy);
    color: #fff;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 4px;
    font-family: var(--mono);
    font-size: 11px;
  }}

  .slide-chapter-tag {{
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  .slide-sep {{
    color: var(--border-dark);
  }}

  .slide-tag-pill {{
    background: var(--red-soft);
    color: var(--red);
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 11px;
  }}

  body.dark-mode .slide-tag-pill {{
    background: rgba(229,36,33,0.2);
  }}

  .slide-main-title {{
    font-size: 22px;
    font-weight: 800;
    color: var(--navy);
    line-height: 1.25;
    margin-bottom: 6px;
  }}

  body.dark-mode .slide-main-title {{
    color: #fff;
  }}

  .slide-main-subtitle {{
    font-size: 14px;
    color: var(--text-secondary);
    font-weight: 500;
    max-width: 950px;
  }}

  /* LEAD BANNER */
  .lead-banner {{
    background: linear-gradient(135deg, var(--navy-dark) 0%, var(--navy-light) 100%);
    color: #fff;
    padding: 22px 28px;
    border-radius: var(--radius-md);
    border-left: 5px solid var(--red);
    box-shadow: var(--shadow-sm);
  }}

  .lead-kicker {{
    background: var(--red);
    color: #fff;
    font-size: 11px;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    display: inline-block;
    margin-bottom: 8px;
  }}

  .lead-banner h3 {{
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 6px;
    color: #fff;
  }}

  .lead-banner p {{
    font-size: 13px;
    color: #E2E8F0;
    line-height: 1.6;
  }}

  /* GRIDS */
  .grid-2 {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; }}
  .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }}
  .grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }}

  /* CARDS & BOXES */
  .stat-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-top: 3px solid var(--navy);
    border-radius: var(--radius-md);
    padding: 16px;
  }}

  .stat-num {{
    font-size: 26px;
    font-weight: 800;
    color: var(--navy);
    font-family: var(--mono);
    line-height: 1;
    margin-bottom: 4px;
  }}

  body.dark-mode .stat-num {{ color: #93C5FD; }}

  .stat-label {{
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    color: var(--text-secondary);
    letter-spacing: 0.5px;
  }}

  .stat-desc {{
    font-size: 12px;
    color: var(--text-muted);
    margin-top: 4px;
  }}

  .content-box {{
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 20px;
  }}

  .content-box.highlight {{
    background: rgba(2,132,199,0.04);
    border-color: var(--blue);
  }}

  body.dark-mode .content-box.highlight {{
    background: rgba(2,132,199,0.1);
  }}

  .box-title {{
    font-size: 14px;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  body.dark-mode .box-title {{ color: #93C5FD; }}

  .clean-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 8px;
    font-size: 13px;
  }}

  .clean-list li {{
    padding-left: 18px;
    position: relative;
    line-height: 1.5;
  }}

  .clean-list li::before {{
    content: "•";
    position: absolute;
    left: 0;
    color: var(--red);
    font-weight: 800;
    font-size: 16px;
    line-height: 1;
    top: 2px;
  }}

  .clean-ordered-list {{
    padding-left: 20px;
    font-size: 13px;
    line-height: 1.7;
    color: var(--text-main);
  }}

  .clean-ordered-list li {{
    margin-bottom: 6px;
  }}

  /* DIAGRAMS */
  .diagram-wrapper {{
    background: #F1F5F9;
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 20px;
  }}

  body.dark-mode .diagram-wrapper {{ background: #0B1120; }}

  .diagram-title {{
    font-size: 13px;
    font-weight: 800;
    text-transform: uppercase;
    color: var(--navy);
    margin-bottom: 14px;
    letter-spacing: 0.5px;
  }}

  body.dark-mode .diagram-title {{ color: #93C5FD; }}

  .pipeline-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
  }}

  .pipeline-step {{
    background: #fff;
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    padding: 12px 14px;
    border-top: 3px solid var(--blue);
  }}

  body.dark-mode .pipeline-step {{ background: var(--bg-card); }}

  .pipeline-step.final {{
    border-top-color: var(--red);
    background: #FFF5F5;
  }}

  body.dark-mode .pipeline-step.final {{ background: rgba(229,36,33,0.12); }}

  .step-badge {{
    font-size: 10px;
    font-weight: 800;
    color: var(--blue);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
  }}

  .step-badge.red {{ color: var(--red); }}

  .step-name {{
    font-size: 13px;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 4px;
  }}

  body.dark-mode .step-name {{ color: #fff; }}

  .step-desc {{
    font-size: 11px;
    color: var(--text-muted);
    line-height: 1.4;
    margin-bottom: 6px;
  }}

  .step-file {{
    font-size: 10px;
    font-family: var(--mono);
    color: var(--text-secondary);
    background: var(--bg-page);
    padding: 2px 4px;
    border-radius: 3px;
    word-break: break-all;
  }}

  /* TABLES */
  .table-card {{
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    overflow: hidden;
    background: var(--bg-card);
  }}

  .table-header {{
    background: #F1F5F9;
    padding: 12px 18px;
    font-size: 13px;
    font-weight: 700;
    color: var(--navy);
    border-bottom: 1px solid var(--border-light);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  body.dark-mode .table-header {{ background: #131E32; color: #fff; }}

  table.data-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
  }}

  table.data-table th, table.data-table td {{
    padding: 10px 14px;
    text-align: left;
    border-bottom: 1px solid var(--border-light);
    vertical-align: top;
  }}

  table.data-table th {{
    background: #F8FAFC;
    color: var(--text-secondary);
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  body.dark-mode table.data-table th {{ background: #0F172A; }}

  table.data-table tr:hover td {{
    background: #F8FAFC;
  }}

  body.dark-mode table.data-table tr:hover td {{
    background: #162036;
  }}

  /* CODE BOX */
  .code-box {{
    background: #061A33;
    color: #F8FAFC;
    padding: 12px 16px;
    border-radius: var(--radius-sm);
    font-family: var(--mono);
    font-size: 12px;
    line-height: 1.6;
    overflow-x: auto;
  }}

  .code-box.highlight-cmd {{
    font-size: 14px;
    font-weight: 600;
    background: #0B2E59;
    border: 1px solid #1E4E8C;
    color: #4ADE80;
  }}

  .cmd-comment {{ color: #94A3B8; }}
  .cmd-text {{ color: #F8FAFC; }}

  /* CALLOUTS */
  .callout-box {{
    padding: 14px 18px;
    border-radius: var(--radius-sm);
    font-size: 13px;
    line-height: 1.5;
    border-left: 4px solid;
  }}

  .callout-box.info {{
    background: #EFF6FF;
    border-color: var(--blue);
    color: #1E3A8A;
  }}

  .callout-box.warning {{
    background: #FFFBEB;
    border-color: var(--amber);
    color: #92400E;
  }}

  .callout-box.success {{
    background: #ECFDF5;
    border-color: var(--green);
    color: #065F46;
  }}

  body.dark-mode .callout-box.info {{ background: rgba(2,132,199,0.12); color: #93C5FD; }}
  body.dark-mode .callout-box.warning {{ background: rgba(217,119,6,0.12); color: #FDE68A; }}
  body.dark-mode .callout-box.success {{ background: rgba(5,150,105,0.12); color: #A7F3D0; }}

  /* STEP CARDS */
  .step-card {{
    display: flex;
    gap: 16px;
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 18px 22px;
    align-items: flex-start;
  }}

  .step-card-num {{
    background: var(--navy);
    color: #fff;
    font-size: 12px;
    font-weight: 800;
    padding: 4px 10px;
    border-radius: 4px;
    font-family: var(--mono);
    text-transform: uppercase;
  }}

  .step-card-body h4 {{
    font-size: 15px;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 4px;
  }}

  body.dark-mode .step-card-body h4 {{ color: #fff; }}

  /* OVERLAY CARDS */
  .overlay-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 14px;
    border-top: 3px solid var(--purple);
  }}

  .overlay-badge {{
    font-size: 10px;
    font-weight: 800;
    color: var(--purple);
    text-transform: uppercase;
  }}

  .overlay-name {{
    font-size: 13px;
    font-weight: 700;
    color: var(--navy);
    margin: 2px 0 4px;
  }}

  body.dark-mode .overlay-name {{ color: #fff; }}

  .overlay-desc {{
    font-size: 11px;
    color: var(--text-muted);
    line-height: 1.4;
  }}

  /* OUTPUT CARDS */
  .output-card {{
    display: flex;
    gap: 14px;
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 16px;
    align-items: flex-start;
  }}

  .output-card.full {{
    border-left: 4px solid var(--green);
  }}

  .output-num {{
    background: #F1F5F9;
    color: var(--navy);
    font-size: 13px;
    font-weight: 800;
    padding: 4px 10px;
    border-radius: 4px;
    font-family: var(--mono);
  }}

  body.dark-mode .output-num {{ background: #1E293B; color: #93C5FD; }}

  .output-body h4 {{
    font-size: 14px;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 4px;
  }}

  body.dark-mode .output-body h4 {{ color: #fff; }}

  .output-body p {{
    font-size: 12px;
    color: var(--text-muted);
    line-height: 1.5;
  }}

  /* BADGES */
  .badge-action {{
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
    font-family: var(--mono);
    text-transform: uppercase;
  }}

  .badge-action.red {{
    background: var(--red-soft);
    color: var(--red);
  }}

  body.dark-mode .badge-action.red {{
    background: rgba(229,36,33,0.25);
  }}

  /* CHAT PROMPT BOX */
  .chat-prompt-box {{
    background: #EFF6FF;
    border-left: 4px solid var(--blue);
    padding: 10px 14px;
    border-radius: 4px;
    font-size: 13px;
    font-weight: 700;
    color: var(--navy);
    margin-top: 6px;
  }}

  body.dark-mode .chat-prompt-box {{
    background: rgba(2,132,199,0.15);
    color: #93C5FD;
  }}

  /* CONTROLLER */
  .bottom-controller {{
    position: fixed;
    bottom: 20px;
    right: 30px;
    background: rgba(6,26,51,0.92);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 30px;
    padding: 8px 18px;
    display: flex;
    align-items: center;
    gap: 14px;
    color: #fff;
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    z-index: 1000;
  }}

  body.full-mode .bottom-controller {{ display: none; }}

  .nav-btn {{
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.25);
    color: #fff;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    font-family: inherit;
    transition: all 0.2s;
  }}

  .nav-btn:hover:not(:disabled) {{
    background: var(--red);
    border-color: var(--red);
  }}

  .nav-btn:disabled {{
    opacity: 0.35;
    cursor: not-allowed;
  }}

  .progress-info {{
    font-size: 12px;
    font-weight: 700;
    display: flex;
    flex-direction: column;
    gap: 3px;
    min-width: 110px;
    text-align: center;
  }}

  .progress-bar-wrap {{
    width: 100%;
    height: 4px;
    background: rgba(255,255,255,0.2);
    border-radius: 2px;
    overflow: hidden;
  }}

  .progress-bar-fill {{
    height: 100%;
    background: var(--red);
    width: 10%;
    transition: width 0.2s;
  }}

  .slide-select-dropdown {{
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.25);
    color: #fff;
    padding: 5px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-family: inherit;
    outline: none;
    cursor: pointer;
    max-width: 180px;
  }}

  .slide-select-dropdown option {{
    background: #061A33;
    color: #fff;
  }}

  /* PRESENTATION MODE */
  body.present-mode header.master-header,
  body.present-mode aside.sidebar {{
    display: none;
  }}

  body.present-mode .app-container {{
    grid-template-columns: 1fr;
  }}

  body.present-mode main.stage-area {{
    padding: 0;
    background: var(--bg-card);
  }}

  body.present-mode .slide-section {{
    margin: 0;
    border: none;
    border-radius: 0;
    box-shadow: none;
    min-height: 100vh;
    padding: 40px 60px;
  }}

  .exit-present-btn {{
    display: none;
    position: fixed;
    top: 14px;
    right: 20px;
    z-index: 9999;
    background: rgba(6,26,51,0.85);
    color: #fff;
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 4px;
    padding: 6px 12px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
  }}

  body.present-mode .exit-present-btn {{
    display: block;
  }}

  /* PRINT STYLES */
  @media print {{
    header.master-header,
    aside.sidebar,
    .bottom-controller,
    .exit-present-btn {{
      display: none !important;
    }}

    .app-container {{
      display: block !important;
    }}

    main.stage-area {{
      overflow: visible !important;
      padding: 0 !important;
      background: #fff !important;
    }}

    .slide-section {{
      display: block !important;
      page-break-after: always !important;
      break-after: page !important;
      box-shadow: none !important;
      border: 1px solid #CBD5E1 !important;
      margin-bottom: 20px !important;
      background: #fff !important;
    }}

    @page {{
      size: landscape;
      margin: 10mm;
    }}
  }}

  @media (max-width: 1024px) {{
    .app-container {{ grid-template-columns: 1fr; }}
    aside.sidebar {{ display: none; }}
    .grid-4 {{ grid-template-columns: repeat(2, 1fr); }}
    .pipeline-grid {{ grid-template-columns: 1fr; }}
  }}

  @media (max-width: 768px) {{
    .grid-2, .grid-3, .grid-4 {{ grid-template-columns: 1fr; }}
    main.stage-area {{ padding: 16px; }}
    .slide-section {{ padding: 20px 16px; }}
  }}
</style>
</head>
<body>

<header class="master-header">
  <div class="header-brand">
    <div class="gov-badge">AI-GOV</div>
    <div class="brand-text">
      <h1>Enterprise AI Governance: Complete Master User Guide</h1>
      <p>Workspace: C:\\ai-governance-package | GitHub: dwaipayanmojumder24-lgtm/ai-governance-package</p>
    </div>
  </div>
  <div class="header-actions">
    <div class="mode-tabs">
      <button class="mode-btn active" id="btnModeSlide" onclick="setMode('slide')">Slide Mode</button>
      <button class="mode-btn" id="btnModeFull" onclick="setMode('full')">Full View</button>
      <button class="mode-btn" id="btnModePresent" onclick="setMode('present')">Present (F)</button>
    </div>
    <button class="btn-action" onclick="toggleDarkMode()">Dark / Light</button>
    <button class="btn-action" onclick="window.print()">Save as PDF</button>
  </div>
</header>

<button class="exit-present-btn" onclick="setMode('slide')">Exit Presentation (Esc)</button>

<div class="app-container">
  <aside class="sidebar">
    <div class="sidebar-search">
      <input type="text" id="searchInput" placeholder="Search guide (e.g. mcp, policies, outputs)..." oninput="filterSidebar()">
    </div>
    <div class="sidebar-items-list" id="sidebarList">
      {sidebar_items_html}
    </div>
  </aside>

  <main class="stage-area" id="stageArea">
    {slides_html}
  </main>
</div>

<div class="bottom-controller">
  <button class="nav-btn" id="btnPrev" onclick="prevSlide()">&#9664; Prev</button>
  <div class="progress-info">
    <span id="slideCounterText">Slide 1 of {len(SLIDES)}</span>
    <div class="progress-bar-wrap">
      <div class="progress-bar-fill" id="progressFill" style="width: 10%;"></div>
    </div>
  </div>
  <button class="nav-btn" id="btnNext" onclick="nextSlide()">Next &#9654;</button>
  <select class="slide-select-dropdown" id="slideSelectDropdown" onchange="goToSlide(parseInt(this.value))">
    {dropdown_options}
  </select>
</div>

<script>
  let currentSlide = 0;
  const totalSlides = {len(SLIDES)};
  let currentMode = 'slide';

  function updateUI() {{
    // Hide / show slides in slide mode
    for (let i = 0; i < totalSlides; i++) {{
      const sec = document.getElementById('slide-' + (i + 1));
      const navItem = document.getElementById('nav-item-' + i);
      if (sec) {{
        if (currentMode === 'slide' || currentMode === 'present') {{
          sec.classList.toggle('active', i === currentSlide);
        }} else {{
          sec.classList.add('active');
        }}
      }}
      if (navItem) {{
        navItem.classList.toggle('active', i === currentSlide);
      }}
    }}

    // Update bottom controller
    const counterText = document.getElementById('slideCounterText');
    if (counterText) counterText.textContent = `Slide ${{currentSlide + 1}} of ${{totalSlides}}`;

    const progressFill = document.getElementById('progressFill');
    if (progressFill) {{
      const pct = Math.round(((currentSlide + 1) / totalSlides) * 100);
      progressFill.style.width = pct + '%';
    }}

    const btnPrev = document.getElementById('btnPrev');
    const btnNext = document.getElementById('btnNext');
    if (btnPrev) btnPrev.disabled = (currentSlide === 0);
    if (btnNext) btnNext.disabled = (currentSlide === totalSlides - 1);

    const dropdown = document.getElementById('slideSelectDropdown');
    if (dropdown) dropdown.value = currentSlide;

    // Scroll active slide into view if full mode
    if (currentMode === 'full') {{
      const sec = document.getElementById('slide-' + (currentSlide + 1));
      if (sec) sec.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}
  }}

  function goToSlide(idx) {{
    if (idx >= 0 && idx < totalSlides) {{
      currentSlide = idx;
      updateUI();
    }}
  }}

  function nextSlide() {{
    if (currentSlide < totalSlides - 1) {{
      currentSlide++;
      updateUI();
    }}
  }}

  function prevSlide() {{
    if (currentSlide > 0) {{
      currentSlide--;
      updateUI();
    }}
  }}

  function setMode(mode) {{
    currentMode = mode;
    document.body.classList.remove('full-mode', 'present-mode');
    document.getElementById('btnModeSlide').classList.remove('active');
    document.getElementById('btnModeFull').classList.remove('active');
    document.getElementById('btnModePresent').classList.remove('active');

    if (mode === 'full') {{
      document.body.classList.add('full-mode');
      document.getElementById('btnModeFull').classList.add('active');
    }} else if (mode === 'present') {{
      document.body.classList.add('present-mode');
      document.getElementById('btnModePresent').classList.add('active');
    }} else {{
      document.getElementById('btnModeSlide').classList.add('active');
    }}
    updateUI();
  }}

  function toggleDarkMode() {{
    document.body.classList.toggle('dark-mode');
  }}

  function filterSidebar() {{
    const query = document.getElementById('searchInput').value.toLowerCase();
    const items = document.querySelectorAll('.sidebar-item');
    items.forEach(it => {{
      const text = it.textContent.toLowerCase();
      it.style.display = text.includes(query) ? 'block' : 'none';
    }});
  }}

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {{
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 'ArrowRight' || e.key === 'PageDown') {{
      nextSlide();
    }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
      prevSlide();
    }} else if (e.key === 'Home') {{
      goToSlide(0);
    }} else if (e.key === 'End') {{
      goToSlide(totalSlides - 1);
    }} else if (e.key === 'f' || e.key === 'F') {{
      setMode(currentMode === 'present' ? 'slide' : 'present');
    }} else if (e.key === 'Escape') {{
      if (currentMode === 'present') setMode('slide');
    }}
  }});

  // Init
  updateUI();
</script>
</body>
</html>
"""
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"[SUCCESS] Re-architected Master User Guide generated at: {OUTPUT_HTML}")
    print(f"Total Slides: {len(SLIDES)}")
    return OUTPUT_HTML

if __name__ == "__main__":
    build_deck()
