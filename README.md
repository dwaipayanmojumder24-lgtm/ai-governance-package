# AI Governance-as-a-Service: Prompt Kit

This kit uses generative AI to build a reusable AI governance package. The package has three parts:

- **Common baseline:** policies, standards and controls that apply to every project. Teams don't rewrite these.
- **Overlays:** add-ons that add or tighten requirements for a sector, geography, risk tier or AI type.
- **Plug-in kit:** reusable integrations for code, CI/CD, continuous training (CT), deployment and agents.

## 1. What's in the kit

| File | Purpose | How often you run it |
|---|---|---|
| `governance-framework-design-prompt.md` | **Design prompt.** The full consultation prompt from your design conversation. It produces the architecture, operating model and roadmap for review board (ARB) approval. | Once, plus when the architecture changes |
| `governance-package-builder-prompt.md` | **Package-builder prompt.** Generates the actual package files, one module at a time (M0–M9). | Module by module, and again for each new overlay |
| `README.md` | This guide | — |

## 2. Before you start

1. **Choose a tool.**
   - **Agentic coding tool (recommended):** for example Claude Code, Codex or Gemini CLI. These can write files straight into a Git repository. Check which tools your organisation has approved.
   - **Chat tool:** ChatGPT, Gemini or Claude. This works too, but you copy each generated file into the repository yourself.
2. **Create an empty Git repository** for the package, for example `ai-governance-package`.
3. **Name your reviewers:** security, privacy, legal, risk and platform engineering. Everything the AI generates is a DRAFT until they approve it.

## 3. Execution steps

### Phase A: Design (optional, run once)

1. Open a new chat or session.
2. Paste `governance-framework-design-prompt.md`. Every input is pre-filled with a default; change only the values you need. Unchanged fields use their defaults (full framework, standard depth, mixed audience, context UNKNOWN).
3. Run Stages 1 to 5. After each stage, reply `continue`.
4. Save each stage's **continuation record**.
5. Take the outputs to your ARB and record the decisions it approves.

Skip Phase A if your architecture is already agreed.

### Phase B: Build the package (core work)

Run the modules in this order. **Use one module per run**; module M2 may need several runs, one per domain group.

| Module | Output |
|---|---|
| M0 | Repository structure, ID scheme, schemas, versioning |
| M1 | Principles charter and baseline policies |
| M2 | Machine-readable control catalogue, built domain by domain |
| M3 | Overlay framework and templates |
| M4 | Project manifest, resolver logic, exception template, quick-start guide |
| M5 | Policy-as-code rules with tests |
| M6 | Plug-ins for pre-commit, PR checks, CI/CD, CT, deployment, agents and LLM gateway |
| M7 | Assessment and evidence templates |
| M8 | Adoption and change-control documentation |
| M9 | Package audit |

**In a chat tool:**

1. **First run:** paste the builder prompt. Inputs are pre-filled with defaults (`MODULE TO GENERATE: M0`, tool-neutral, no overlays); change only what you need, such as your ID prefix or named tools.
2. **Copy the files:** put each `FILE: <path>` block into your repository at that path.
3. **Next module, same chat:** reply `continue`.
4. **Next module, new chat:** if the chat gets long or you change tools, start a new chat. Paste the prompt, then paste the last **continuation record** and the files the next module depends on (for example, the M0 schemas and the M2 catalogue), and set the next module.

**In an agentic coding tool:**

1. Commit `governance-package-builder-prompt.md` to the repository.
2. Instruct the tool: *"Read governance-package-builder-prompt.md and execute module M0. Write the files into this repository."*
3. Review the diff and commit it.
4. Repeat for each module, for example: *"Execute module M1 using the existing files."*

### Phase C: Review and release

1. Have reviewers check the policies and controls. Replace the owner and date placeholders and set the parameter values.
2. Run and fix the policy-as-code tests (M5) and pipeline templates (M6) in a sandbox repository.
3. Apply the approvals: remove the `DRAFT` labels only for items that were approved.
4. Tag the first release, for example `v1.0.0`, and publish it to your package or artifact registry.

### Phase D: Add overlays (as needed)

For each overlay, run the builder prompt with:

- `MODULE TO GENERATE: M3`
- `Overlays wanted in this run:`, naming one overlay, for example `geography: EU`
- `APPROVED BASELINE VERSION:`, for example `v1.0.0`

Run one overlay at a time. Legal review is required before release.

### Phase E: Project adoption (done by development teams)

1. **Declare the project:** add the project manifest (from M4) to the project repository, describing the project's characteristics.
2. **Pin versions:** reference a specific baseline version and the required overlay versions.
3. **Add the plug-ins:** include the M6 templates in the project's pipelines and agent runtime.
4. **Resolve:** run the resolver to produce the effective-policy snapshot for the project.
5. **Supply evidence:** fill in the M7 templates for the controls that apply.

Teams don't write governance policies. They declare, configure and provide evidence.

### Phase F: Maintain

- **Regulatory change:** update the affected overlay and release a new overlay version.
- **Baseline change:** follow the change-control process from M8. A breaking change needs a major version and a migration note.
- **Audits:** re-run M9 after significant changes.

## 4. Tips to avoid losing context

- **One module per run.** Never ask for the whole package at once.
- **Keep every continuation record**, for example in `/governance-runs/` in the repository.
- **Prefer fresh chats with the record** over very long chats. Some tools drop early messages in long conversations.
- **Store the prompt as reusable instructions where your tool supports it**, for example a Claude Project, a ChatGPT Project or Custom GPT, or a Gemini Gem. Feature names change, so check what your tool currently offers.

## 5. Limitations

- **AI output is a draft.** Generated policies, controls and code need expert review and testing.
- **Adopting the package doesn't prove compliance.** It doesn't establish legal compliance or certification on its own.
- **Overlays need legal review.** Regulatory content must be checked against primary sources and by qualified legal reviewers.
- **Tool syntax may change.** Verify named-tool syntax against current documentation.

## 6. Quick run sheet

```
Phase A (optional): Design prompt → Stages 1–5 → ARB approval
Phase B:            Builder prompt → M0 → M1 → M2 (per domain group) → M3 → M4 → M5 → M6 → M7 → M8 → M9
Phase C:            Review → test → approve → tag v1.0.0
Phase D:            Builder prompt → M3 → one overlay per run
Phase E:            Projects: manifest → pin versions → plug-ins → resolve → evidence
Phase F:            Maintain via versioned releases
```
