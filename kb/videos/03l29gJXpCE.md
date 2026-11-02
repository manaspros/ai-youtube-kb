# Guide, Verify, Solve — Anirban Chatterjee, Sonar

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `03l29gJXpCE` · [watch](https://youtu.be/03l29gJXpCE) · **date:** 2026-08-18 · **length:** 22:31 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Anirban Chatterjee · **orgs:** Sonar, Carnegie Mellon University, Wharton, Anthropic, OpenAI
- **topics:** testing-verification, pr-code-review, coding-agents, governance-compliance · **tags:** verification, verification-debt, zero-trust, ACDC, agentic-loops, static-analysis, PR-gate, bounded-autonomy, vendor-talk

> Sonar's product marketer argues AI-written code needs zero-trust, multilayered verification inside agent loops and in CI/CD, framed as a Guide-Verify-Solve (ACDC) cycle, with vendor product pitches throughout.

## Summary
The speaker argues that AI coding tools gave only a temporary productivity lift (about three months, per a cited CMU GitHub study) while static-analysis warnings and code complexity stayed higher. He says the gap between AI-default quality and the quality a production system needs is what he calls "verification debt", and that humans must close it or automated verification must. He cites a Wharton study in which people followed deliberately wrong AI advice nearly 80% of the time, and argues code review is being rubber-stamped. His proposed fix is verification that is zero-trust (same regime regardless of who or what wrote the code, using a different method than the writer) and multilayered (computational plus LLM-based review). He frames the workflow as an ACDC loop: guide the agent with context and constraints, verify its output, then let the agent solve the issues it finds. Verification runs both inside the agent's write loop and as a gate in the PR/CI pipeline. Most of the talk is a walkthrough of his company's products (SonarQube, Sonar Vortex, a recently acquired AI code-review tool, and a remediation agent), so the reusable ideas are more useful than the product claims.

## Key ideas
- **AI coding gives a short productivity spike that reverses** — Per the cited CMU study, AI-assisted projects on GitHub got a productivity bump lasting about three months, then it fell back. Static-analysis warnings and code complexity stayed higher for longer, and the speaker says these slow developers down later. ([1:14](https://youtu.be/03l29gJXpCE?t=74))
- **Required quality depends on how critical the app is** — For a prototype or a one-person tool, the gap between AI output quality and what is needed is small and can be accepted. For apps with many users, large codebases, and adversarial users, the gap becomes large and must be closed before shipping. ([2:38](https://youtu.be/03l29gJXpCE?t=158))
- **Verification debt is the gap humans or tools must close** — Models still make mistakes and lack broader project and business context. Without verification, errors reach production. The speaker says verification is the enabler for AI-driven development at scale. ([3:38](https://youtu.be/03l29gJXpCE?t=218))
- **Human review is unreliable under AI load** — He cites a Wharton study where participants trusted deliberately wrong AI advice nearly 80% of the time. He argues the same rubber-stamping happens in code review when many agents produce code at once, so automated verification has to backstop it. ([6:16](https://youtu.be/03l29gJXpCE?t=376))
- **Verification must be zero-trust and multilayered** — Code is treated the same whether a human or an AI wrote it. The checker should use a different method from the writer, and the process should be auditable and repeatable. Use several layers, computational checks plus LLM-based review, because no single method catches everything. ([9:04](https://youtu.be/03l29gJXpCE?t=544))
- **The ACDC loop is Guide, Verify, Solve** — Guide gives the agent context, guardrails, and constraints before it writes. Verify is multilayer, reasoning-based, and covers quality, security, and compliance. Solve lets the agent fix the issues it finds with its own tools, then the loop repeats. The speaker says verification is the fastest step for teams to adopt now. ([10:13](https://youtu.be/03l29gJXpCE?t=613))
- **Encode specs and quality thresholds up front, and give the agent only task-relevant context** — Architecture constraints, allowed dependencies, coding and logging standards, and acceptable quality, security, and maintainability levels should be written down and enforced. Context should be scoped per task, since dumping the whole codebase wastes tokens and time. ([16:11](https://youtu.be/03l29gJXpCE?t=971))
- **Run verification in both the inner agent loop and the outer PR/CI gate** — Inside the loop, the agent calls the verifier after each write and fixes issues before they spread into later steps. In the PR flow, an LLM reviewer and a deterministic scanner grade the change, and failing grades block merge. Auto-fix and auto-merge are switched on only after the team trusts the reviewer. ([17:29](https://youtu.be/03l29gJXpCE?t=1049))

## Techniques
- **In-loop verifier callback with fix-and-rerun** — After the agent finishes a write, it calls a verification tool, gets the list of issues, fixes them, and reruns the check. It does not continue until the check passes. The speaker demos this with Cursor and says similar integrations exist for Claude Code, Codex, and Antigravity. *When:* Any agentic coding loop where bad output would otherwise carry into later steps of a multi-step build.
- **Task-scoped context retrieval for agents** — Before a coding task starts, the agent asks a context service for only the guardrails and code relevant to that task, instead of loading the whole repo up front. *When:* Large codebases where full-repo context burns tokens and slows the agent down.
- **Machine-enforced quality rulebook** — Architecture rules, dependency allow/deny lists, coding and logging standards, and quality thresholds are written as one standard and applied the same way to every team and every AI tool. *When:* Organisations where several teams or tools write code and need consistent verification.
- **Dual PR gate: LLM review plus deterministic scan** — The PR is graded by an LLM reviewer for judgment-based issues and by a rule-based static analyser for quality, security, and maintainability grades. Failing grades block merge, and a fix agent can attempt repairs. *When:* Teams that want an auditable merge gate for agent-written PRs.
- **Cross-model or cross-method review** — Do not use the same model or method to check code that it wrote. Verify with a different model or with non-LLM tools. *When:* Multi-agent or mixed-tool development where one model's blind spots could go unchecked.
- **Graduated automation of review bots** — Start the bot in comment-only mode. Turn on auto-fix, then auto-approve and auto-merge only as the team gains confidence in its results. *When:* Introducing an AI reviewer into a team that does not yet trust it.
- **Remediation agent for backlog debt** — Point an agent at a list of old issues or legacy code and let it fix them in the background while humans work on new features. *When:* Tech-debt backlogs larger than the team has time to fix.
- **Per-task model choice from a quality profile** — Compare models on correctness, complexity, maintainability, security, and token cost, then choose per task. The speaker says Sonnet was strong on correctness and reliability while Opus did better on maintainability, security, and complexity. *When:* Balancing token burn against code quality on specific task types.

## Numbers
- AI-assisted GitHub projects showed a productivity spike lasting about 3 months, then fell back; static-analysis warnings and complexity stayed persistently higher (CMU study, per speaker) ([1:14](https://youtu.be/03l29gJXpCE?t=74))
- Wharton study: participants followed AI advice 92.7% of the time when it was correct and nearly 80% of the time when it was wrong ([6:16](https://youtu.be/03l29gJXpCE?t=376))
- Sonar's LLM leaderboard runs each new model on about 4,000 coding tasks, scored on correctness, complexity, task completion, maintainability, reliability, and security (vendor data) ([4:52](https://youtu.be/03l29gJXpCE?t=292))
- Sonar reports over 7 million developers use its tools and about 750 billion lines of code are analysed per day (vendor claim) ([20:01](https://youtu.be/03l29gJXpCE?t=1201))

## Hot takes
- Software cannot be proven correct the way code can, so automated verification is a control that must stay in the loop.
- Human code review is already being rubber-stamped, and a bot is needed to backstop it.
- The model that writes code should not be the one that checks it.

## Tools mentioned
SonarQube, Sonar Vortex, Guitar (AI code-review tool, name from captions), Cursor, Claude Code, Codex, Antigravity

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs checkpointed Claude Code steps. The talk's verify-fix-rerun gate before a checkpoint is accepted maps directly onto that harness design. → *Add a verify-and-fix gate after each checkpointed step in ProsHarness: run an independent static check, return the issues to the agent, and checkpoint only after the check passes.*
- **agentos** (1/3): AgentOS Crucible has exec-gate guardrails. The idea of a deterministic static check on generated code could fit there, though the talk is a vendor pitch with no open design. → *Consider a static-analysis rule in Crucible's exec-gate that scans generated code before it runs. Keep it optional and log the results.*
