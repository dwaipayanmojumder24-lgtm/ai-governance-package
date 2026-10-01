#!/usr/bin/env python3
"""
Enterprise AI Governance - Model Context Protocol (MCP) Server
=============================================================================
Exposes the AI Governance Engine as MCP tools for Cursor, Claude Code,
Gemini CLI, and VS Code. Allows AI coding assistants to autonomously inspect,
govern, and verify codebases on the developer's behalf.

Tools exposed:
  1. `ai_governance_inspect`: Scans repo, detects frameworks, PII, and archetype.
  2. `ai_governance_auto_setup`: Autonomously configures manifest, snapshot, and gates.
  3. `ai_governance_verify`: Evaluates codebase against policy-as-code rules.
=============================================================================
"""

import sys
import json
from pathlib import Path

# Add parent directory to import governance agent
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from agents.governance_agent import GovernanceAgent


def handle_request(req: dict) -> dict:
    req_id = req.get("id")
    method = req.get("method")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "enterprise-ai-governance-mcp",
                    "version": "0.1.0"
                }
            }
        }

    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "ai_governance_inspect",
                        "description": "Inspects an AI codebase, detects frameworks, PII, agent tools, and infers risk tier.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "target_dir": {
                                    "type": "string",
                                    "description": "Directory path of the project to inspect (defaults to current dir)."
                                }
                            }
                        }
                    },
                    {
                        "name": "ai_governance_auto_setup",
                        "description": "Autonomously initializes AI governance: generates manifest, resolves policy snapshot, and installs CI/CD PR gates.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "target_dir": {
                                    "type": "string",
                                    "description": "Directory path of the project to onboard."
                                }
                            }
                        }
                    }
                ]
            }
        }

    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        target_dir = arguments.get("target_dir", ".")

        agent = GovernanceAgent(target_dir=target_dir)

        if tool_name == "ai_governance_inspect":
            findings = agent.scan_codebase()
            arch, risk = agent.infer_archetype_and_risk(findings)
            payload = {
                "archetype": arch,
                "risk_tier": risk,
                "telemetry": {k: list(v) if isinstance(v, set) else v for k, v in findings.items()}
            }
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(payload, indent=2)}]
                }
            }

        elif tool_name == "ai_governance_auto_setup":
            result = agent.auto_setup()
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": f"Successfully initialized governance. Archetype: {result['archetype']}, Active Controls: {result['active_controls']}, Hash: {result['snapshot_hash']}"}]
                }
            }

        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Method {tool_name} not found"}
            }

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": {}
    }


def main():
    """Reads JSON-RPC messages from stdin and writes responses to stdout."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32603, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
