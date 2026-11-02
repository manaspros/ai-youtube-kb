# GitHub Actions are DEAD. (Use Agentic Workflows instead)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `-DXkF2Q69Jw` · [watch](https://youtu.be/-DXkF2Q69Jw) · **date:** 2026-03-02 · **length:** 7:07 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Andres (Better Stack host) · **orgs:** GitHub, GitHub Next, Microsoft Research, Better Stack
- **topics:** software-factory, pr-code-review, security-guardrails · **tags:** github-actions, agentic-workflows, ci-cd, continuous-ai, pull-request-review, copilot, guardrails, permissions

> Walkthrough of GitHub Agentic Workflows: write a natural-language agent.md, compile it to a locked-down Actions workflow, and use it as a PR audit bot. Research prototype, one demo.

## Summary
The video introduces GitHub Agentic Workflows, a project from GitHub Next and Microsoft Research under a "continuous AI" vision. The pitch is that deterministic Actions cannot handle judgment tasks like triage, doc updates, or spotting architectural flaws, so the workflow is described in plain markdown instead. The speaker stresses guardrails: the agent inherits GitHub Actions logging, secrets and auditable permissions, runs with minimal permissions by default, and can only write through predefined sanitized paths with approval. Setup is a markdown file under .github/workflows/ with a header for permissions and the AI engine (Copilot in the demo), compiled with a ghaw CLI command into a lock file, then pushed with the engine token stored as a secret. The demo configures a "big O auditor" that runs on new pull requests; a deliberately O(n^2) function triggers a roughly three-minute run that returns a markdown table of findings, an optimized version, and an estimated performance gain. The speaker closes by calling it a research prototype with latency and a need for human verification. The single demo is anecdotal, and the video ends with a short plug for Better Stack's AI SRE product.

## Key ideas
- **Agentic Workflows target judgment work that deterministic Actions cannot do** — The project is from GitHub Next and Microsoft Research under a 'continuous AI' vision. The speaker frames the goal as 'productive ambiguity': tasks like bug triage, doc updates, or catching architectural flaws, described in plain markdown instead of if-X-then-Y rules. ([0:00](https://youtu.be/-DXkF2Q69Jw?t=0))
- **Built on Actions, with minimal permissions by default** — It inherits Actions logs, secrets management and auditable permissions. Agents can analyze code and suggest changes by default, but write operations need explicit approval through predefined sanitized pathways. ([1:10](https://youtu.be/-DXkF2Q69Jw?t=70))
- **Two-step authoring: markdown source, then compile to a locked-down workflow** — You write the agent instructions as markdown and run the ghaw compile command. It generates a hardened GitHub Actions workflow (a lock .yaml file, which the auto-captions render as '.log.yaml'). Pushing the repo activates the agent. ([1:57](https://youtu.be/-DXkF2Q69Jw?t=117))
- **The markdown file has a permissions/engine header and a free-form natural-language body** — The file lives under .github/workflows/. The header sets the agent's permissions and AI provider (Copilot here). The body is ordinary prose describing the job, such as the demo's big-O auditor that reviews new commits and proposes faster versions. ([3:00](https://youtu.be/-DXkF2Q69Jw?t=180))
- **Demo: a PR-triggered complexity auditor catches a deliberately slow function** — The workflow runs on new pull requests. The demo adds an O(n^2) record-matching function, and the agent flags it after a run of roughly three minutes. ([4:17](https://youtu.be/-DXkF2Q69Jw?t=257))
- **Output is structured, quantified feedback on the PR** — The agent returns a markdown table of findings as requested in the prompt, explains why the function is inefficient, proposes a better implementation, and estimates the performance gain from the change. ([5:27](https://youtu.be/-DXkF2Q69Jw?t=327))
- **Speaker's own caveats: research prototype, latency, and human review still required** — He says it is still a GitHub Next research prototype, that latency is noticeable, and that a human must verify the final checks. He presents it as an early step toward autonomous CI/CD monitoring. ([6:32](https://youtu.be/-DXkF2Q69Jw?t=392))

## Techniques
- **Natural-language agent file compiled into an Actions workflow** — Create .github/workflows/agent.md. Put the permissions and AI engine in the header, then write the task in plain prose. Install the ghaw CLI via the GitHub CLI extension (exact extension name not shown). Run 'ghaw compile' from the repo root; it writes a .lock.yaml workflow plus an 'aw' folder of logs. Commit and push. Store the engine's token (Copilot GitHub token in the demo) as a repo secret. The speaker does not show the exact header key names, so check the project docs for them. *When:* Use for review or triage jobs that need judgment and cannot be expressed as deterministic if/then Actions steps, and where you want the generated YAML to be reviewable and committed.
- **PR-triggered read-only audit agent with a structured output format** — Configure the workflow to trigger on pull_request events. In the prose body, name the role (for example 'big O auditor'), the diff scope (new commits), the analysis (estimate complexity, flag inefficiency, propose an optimized version), and the output format (a markdown table). Keep the default minimal permissions so the agent only reads and comments. *When:* Use for quality gates on agent-written or human PRs where you want advisory findings, not automatic merges or writes.
- **Gated write path for agent actions** — Do not give the agent direct write access. Route any change through predefined, sanitized outputs that need explicit approval, as the speaker describes. *When:* Use whenever an agent that reads untrusted repo content could push code, comment, or change settings. This is the guardrail model to copy for any agent write action.

## Numbers
- The PR-triggered agent pipeline took roughly three minutes to finish on the demo PR ([4:17](https://youtu.be/-DXkF2Q69Jw?t=257))
- The demo function was deliberately written at O(n^2) complexity to be caught by the auditor ([4:17](https://youtu.be/-DXkF2Q69Jw?t=257))

## Hot takes
- The title 'GitHub Actions are DEAD' is hype; the video itself says Actions still underpin the workflow.
- The speaker calls it a research prototype, notes latency, and says human verification is still required.
- The evidence is one contrived demo with a planted O(n^2) bug. There are no false-positive rates, costs, or real-repo results.
- The video ends with a sponsored plug for Better Stack's AI SRE, which caps quality at 2 under the rules.

## Tools mentioned
GitHub Agentic Workflows, ghaw (compile CLI), GitHub Actions, GitHub CLI (gh extension), GitHub Copilot (engine), GitHub Next, Microsoft Research, Better Stack AI SRE (sponsor plug)

## Relevance to our work
- **agentos** (1/3): Its permissions-by-default, approval-gated write path, and auditable action logs parallel AgentOS's exec-gate guardrails and audit log, but this is a CI product, not a proxy or runtime. → *Compare GitHub's minimal-default permission model and sanitized-write pathway with the exec-gate design in Crucible before adding any agent write action.*
- **prosharness** (1/3): The approval-gated write path for agent actions is close to ProsHarness's phone-driven approvals and scheduled loops, though the video offers no mechanism detail. → *Check whether ProsHarness's approval gate matches the 'predefined sanitized output then approve' pattern, and whether a PR-triggered audit loop fits its scheduled runs.*
