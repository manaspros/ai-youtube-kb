# SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `bI8WyG9YB0I` · [watch](https://youtu.be/bI8WyG9YB0I) · **date:** 2026-10-12 · **length:** 41:58 · **format:** demo · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Killian Carlsen-Phelan, Tony (Codex Deployment Engineering, OpenAI; introducer) · **orgs:** OpenAI, Sonar (SonarQube / SonarSource)
- **topics:** testing-verification, coding-agents, security-guardrails, context-engineering · **tags:** codex, sonarqube, verification, definition-of-done, secret-detection, taint-analysis, sql-injection, hooks, mcp, skills, agentic-analysis, context-augmentation, inner-loop, outer-loop, acdc, defense-in-depth

> A Codex deployment engineer and a Sonar developer advocate argue that agent "done" needs evidence, containment is not correctness, and feedback checks belong inside the agent loop, then demo SonarQube hooks, MCP and CLI wired into Codex.

## Summary
The talk opens with three claims: done means completed with evidence, containment is not correctness, and the feedback contract belongs inside the loop. The speaker says cheaper code generation moves the bottleneck to specification and verification, and that an agent's self-critique or its own generated tests are not an independent check. Killian Carlsen-Phelan (Sonar) then presents the Generate, Guide, Verify, Solve cycle, with checks shifted from CI into the IDE/agent loop. The live demo wires a SonarQube Cloud project into Codex via a marketplace plugin, CLI, MCP server and hooks. It shows a secret-blocking hook stopping a fake API key, a taint-analysis SQL injection finding, a fix that is re-verified by a post-edit hook, and a new function generated with context augmentation. The speaker says the post-edit hook reports only new issues in the changed code, not pre-existing ones. Much of the demo was slowed by network problems, and the talk is partly a product walkthrough. Context augmentation and agentic analysis are paid-tier features; the secrets hook and CLI are available on the free tier.

## Key ideas
- **Done means complete with evidence, not just 'fixed'** — A task is done when there is a reviewable diff plus tool output (compiler, tests, analysis) that supports the claim. The speaker recommends actively looking for disconfirming evidence and says a human still owns the ship decision. ([0:14](https://youtu.be/bI8WyG9YB0I?t=14))
- **Self-critique and agent-written tests are not an independent oracle** — Agents tend to fail in correlated ways: incomplete context, a local fix that breaks a global invariant, or generated tests that repeat the same mistake. Agent and verifier results can be orthogonal, so both must be checked. ([1:38](https://youtu.be/bI8WyG9YB0I?t=98))
- **Cheaper generation moves the bottleneck to specification and verification** — The speaker says that once code is cheap to produce, the scarce work becomes writing precise specs and checking the output. This is the reason the talk focuses on verification. ([1:38](https://youtu.be/bI8WyG9YB0I?t=98))
- **Containment is not correctness; layer controls across execution and artifacts** — The execution layer defines what the agent may do (tools, scope, approvals). The artifact layer judges the result (tests, analyses, policy, intent). A sandbox can contain a write but cannot prove a query is safe, so the speaker recommends layered guardrails. ([2:59](https://youtu.be/bI8WyG9YB0I?t=179))
- **The feedback contract: skills, MCP tools and hooks inside the loop** — Skills hold procedures, MCP servers expose structured tools and context, and lifecycle hooks run checks such as secret detection. The speaker wants these wired into the agent loop itself. ([2:59](https://youtu.be/bI8WyG9YB0I?t=179))
- **Verification shifts left from CI into the agent/IDE inner loop** — In the outer loop, code is pushed, CI fails, and the developer goes back to fix it. The speaker wants the same checks to run as soon as code is generated, before any push, using context injection before generation and analysis after each edit. ([10:13](https://youtu.be/bI8WyG9YB0I?t=613))
- **Secret blocking at the prompt and tool boundary** — A hook on prompt submission and tool use blocked a fake API key in a commit request and refused to read a file containing a secret. The speaker admits this does not cover a script that reads the file, because the hook may not fire. ([26:53](https://youtu.be/bI8WyG9YB0I?t=1613))
- **Post-edit analysis checks only the code that changed** — After a fix, the post-edit hook re-scans the changed code server-side. It flagged a pre-existing issue in the same file but did not try to fix unrelated code, and the fixed issue no longer appeared. The speaker says this stops fixes from creating new vulnerabilities. ([36:50](https://youtu.be/bI8WyG9YB0I?t=2210))

## Techniques
- **Evidence-backed definition of done** — Define a task as done only when the agent provides a reviewable diff plus tool output (compiler, tests, static analysis, policy checks). Actively look for disconfirming evidence before accepting the claim. *When:* Any autonomous coding task whose output will be merged, especially when agents write both the code and its tests.
- **Layered execution and artifact controls** — Separate controls on what the agent can do (tools, file scope, approvals, sandbox) from checks on what it produced (tests, analysis, policy). Treat each layer as a different oracle and combine them. *When:* Designing a guardrail stack for agents that touch production code or data, where a sandbox alone is not enough.
- **Secret-blocking lifecycle hook** — Install a hook on user-prompt submission and tool use that scans for hard-coded secrets and blocks commits or file reads containing them. Note that scripts reading the file may bypass it. *When:* Agents that can commit code or read the filesystem and might pick up credentials.
- **Guide, verify, solve loop (ACDC)** — Inject project rules and architecture before generation (guide), run analysis immediately after each edit (verify), and feed findings back so the agent fixes them (solve). Iterate until clean. *When:* Agent coding sessions where recurring issues or architecture drift cause rework.
- **Taint analysis across files** — Trace data from untrusted sources (for example sys.argv) through functions and files to sensitive sinks (for example a SQL execute call). Use the trace to find injection paths that a single-file scan misses. *When:* Reviewing agent-written code that handles external input, such as database queries or shell calls.
- **Changed-code-only verification for agent edits** — Scan only the lines an edit touched and report only new issues in them. Keep pre-existing findings in the backlog so the agent's fix loop does not expand in scope. *When:* Agents editing a large existing codebase where a full re-scan on each edit would flood the agent with old findings.
- **Custom rules targeting agent-written code** — Write analysis rules for patterns that agents produce and other agents could exploit, such as parameter-binding failures in queries. Enforce them alongside general rules. *When:* Teams whose agents tend to produce a specific recurring defect class.

## Numbers
- Survey of over 1,000 developers: 42% of committed code is AI-generated or AI-assisted ([7:20](https://youtu.be/bI8WyG9YB0I?t=440))
- 96% of developers do not fully trust AI-generated code ([7:20](https://youtu.be/bI8WyG9YB0I?t=440))
- Fewer than half of developers say they fully verify code before pushing and merging ([7:20](https://youtu.be/bI8WyG9YB0I?t=440))
- Average remediation time for a secret exposed in a public repository is 90 days (speaker's figure) ([15:55](https://youtu.be/bI8WyG9YB0I?t=955))
- Demo project is under 200 lines across four files with four planted issues (three security, one code smell); the scan reported a security rating of E ([14:25](https://youtu.be/bI8WyG9YB0I?t=865))
- Speaker says the provisioning script takes under a minute on his own connection ([29:09](https://youtu.be/bI8WyG9YB0I?t=1749))
- Speaker says a verification step could take about 15 seconds (hypothetical, stated as an illustration) ([34:20](https://youtu.be/bI8WyG9YB0I?t=2060))

## Hot takes
- Self-critique is not an independent oracle, and agent-written tests can carry the same errors as the code.
- Containment is not correctness: a sandbox can limit a write but cannot prove a query is safe.
- Done without evidence is not done; 'fixed' alone is not an acceptable completion report.
- The human owns intent, exceptions and the ship decision, and cannot be removed from the review cycle.
- Verification, not code generation, is now the bottleneck for AI-written code.

## Tools mentioned
Codex (OpenAI coding agent CLI), SonarQube Cloud, SonarQube CLI, SonarQube MCP server, SonarQube Codex plugin / marketplace, Docker, Git Bash (for setup script)

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code with checkpoint/resume and plan, critique and debate steps. The talk's done-with-evidence rule, feedback contract and secret-blocking hook map directly onto those features. → *Require stored evidence (diff plus test or analysis output) before a ProsHarness checkpoint is marked complete, and test a prompt- and file-read secret hook as a harness-level guard.*
- **agentos** (1/3): Crucible's exec-gate and Govrix's PII/injection scan are containment-style layers. The talk's point that containment is not correctness applies, but the talk gives no AgentOS-specific design. → *When reviewing Crucible's sandboxed execution, add an artifact-level check (tests or static analysis on the agent's output) so a contained write is also verified.*
