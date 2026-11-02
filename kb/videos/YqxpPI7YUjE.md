# Why a One-Line Change Can Break Your Whole Stack - Cole Gannaway, Qodo

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YqxpPI7YUjE` · [watch](https://youtu.be/YqxpPI7YUjE) · **date:** 2026-10-29 · **length:** 14:51 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Cole Gannaway · **orgs:** Qodo, Bitwarden
- **topics:** pr-code-review, context-engineering, multi-agent, software-factory · **tags:** blast-radius, software-graph, custom-rules, independent-reviewer, ticket-linked-review, mid-run-review, vendor-pitch, qodo

> A Qodo solutions engineer argues PR review is the bottleneck in AI software factories and needs cross-repo blast-radius context, independent reviewers and rules learned from past reviews. Mostly a product demo.

## Summary
Cole Gannaway, a solutions engineer at Qodo, argues that code generation is moving fast but the pull request and review stage has become the bottleneck in AI-first software factories. He uses a one-line rename in Bitwarden's data model as an example: it passes build, unit tests and linters, yet it affects the server, web, mobile, MCP server and CLI components. His proposed fix is a software graph of the repos and their integration surfaces, custom rules, and ticket context fed to review agents, ideally before code is generated. He recommends independent reviewers (different model, different harness, sometimes adversarial) and turning reviewer comments into standing rules automatically. He also suggests running a review at 25/50/75% of an agent's run to catch drift and over-engineering as the context window shrinks. Most of the talk is a live walkthrough of Qodo's PR review UI, and the talk offers no measured results, so treat it as a vendor pitch with a few reusable patterns.

## Key ideas
- **PR review is the bottleneck, not code generation** — Generation is moving very fast, but the review and trust/verification layer is where teams struggle. The speaker says that is where the talk focuses. ([1:18](https://youtu.be/YqxpPI7YUjE?t=78))
- **A one-line change can pass every check and still break many components** — The Bitwarden example is a one-line data model rename that would pass build, unit tests and linters. The blast radius reaches the backend server, web clients, mobile/iOS, MCP servers and CLI, which normal checks miss. ([2:39](https://youtu.be/YqxpPI7YUjE?t=159))
- **Build a software graph of repos and their integration surfaces** — The graph is built automatically and records which components actually connect, not just which repos exist. Review agents can then use it to judge the blast radius of a change. ([4:05](https://youtu.be/YqxpPI7YUjE?t=245))
- **Put human reviewer knowledge into rules the agent can read** — Custom rules encode senior-reviewer taste and tribal knowledge. The example rule: any change to a public API must add a deprecation flag or get extra review. ([5:20](https://youtu.be/YqxpPI7YUjE?t=320))
- **Bring context in before code is generated, not only at review** — The same context (graph, rules, tribal knowledge via MCP or CLI) can guide the coding agent before it writes code. The speaker admits this does not guarantee correct output, but it improves the odds of getting it right the first time. ([5:20](https://youtu.be/YqxpPI7YUjE?t=320))
- **Do not let the implementing agent grade its own work** — A review agent has its own context window and less competing work, and it should be independent of the writer. Varying the model and harness reduces shared bias. ([6:18](https://youtu.be/YqxpPI7YUjE?t=378))
- **Agreement between independent reviewers is a signal** — If reviewers using different models or harnesses find the same issue, it is probably real. If they find completely different things, the code deserves a closer look. ([7:38](https://youtu.be/YqxpPI7YUjE?t=458))
- **Turn review comments into rules that apply to future PRs** — The product suggests a rule from a PR comment, then applies it to every later PR. Blast-radius data can flag a large change to the reviewer. ([8:31](https://youtu.be/YqxpPI7YUjE?t=511))
- **Link tickets and acceptance criteria to the review** — Jira and Linear tickets are attached to PR reviews, and the tool flags requirement gaps against the acceptance criteria. This checks whether the agent is solving the ticket or wandering off. ([11:41](https://youtu.be/YqxpPI7YUjE?t=701))
- **Run a review at 25/50/75% of an agent's run** — A review skill runs at checkpoints during generation so an agent that has lost direction is caught while the run is still in progress. The speaker says a review agent can act as a manager that stops over-engineering. ([12:40](https://youtu.be/YqxpPI7YUjE?t=760))

## Techniques
- **Blast-radius-aware review over a software graph** — Index the repos a team owns and record their integration surfaces (server to web, mobile, MCP, CLI). For each change, compute which components are affected and surface that to the reviewer, human or agent. *When:* Multi-repo systems where a shared model or API change can silently break clients in other repos.
- **Rules learned from review comments** — When a reviewer leaves a comment that encodes a standard, convert it into a stored rule (for example: public API changes need a deprecation flag). Apply the rule to all later PRs and to the coding agent's context. *When:* Teams whose review feedback keeps repeating, and who want tribal knowledge to persist instead of living in people's heads.
- **Pre-generation context injection** — Expose the software graph, custom rules and ticket data to the coding agent through MCP or a CLI before it writes code, so it does not need to discover them in review. *When:* Agents keep breaking the same invariants that a review would catch later.
- **Independent, varied reviewers** — Use a separate review agent that did not write the code. Vary the underlying LLM provider and harness, and optionally run an adversarial reviewer. Compare findings: overlap is high-confidence, and disjoint findings get investigated. *When:* Trust-sensitive changes where a single model or harness may share the same blind spots.
- **Mid-run review checkpoints via skill** — Install a skill that tells the coding agent to trigger a review at roughly 25%, 50% and 75% of its work, to check it is still on the right path. The speaker's stated reason is that the context window shrinks as the run goes on. *When:* Long agent runs where drift or over-engineering appears late. The speaker presents this as advice from his work with clients, not a measured result.
- **Ticket-linked PR review** — Connect Jira or Linear so each PR review shows the linked ticket and its acceptance criteria, then flag requirement gaps against them. *When:* Teams where a PR can look correct but may not complete the ticket.

## Numbers
- The example one-line change affects about 5 component types: backend server, web clients, mobile/iOS, MCP servers and CLI. ([2:39](https://youtu.be/YqxpPI7YUjE?t=159))
- The speaker suggests running the review at about 25%, 50% and 75% of an agent's run. This is advice, not a measured result. ([12:40](https://youtu.be/YqxpPI7YUjE?t=760))

## Hot takes
- Vendor pitch: most of the talk is a live walkthrough of Qodo's product, with a booth call-to-action at the end, so the claims are not independent.
- The speaker says not all review tools or context are equal, but gives no benchmark, false-positive or false-negative rate, or head-to-head comparison to back that up.
- Using a review agent that is separate from the implementer, with different models or harnesses, is presented as the way to cut bias. The talk does not show evidence that this improves outcomes.
- The claim that the review stage is the main bottleneck is plausible and matches common experience, but it is asserted, not measured.

## Tools mentioned
Qodo (spoken as Kodo), Jira, Linear, MCP servers, Claude Code, Anthropic models, OpenAI models, Bitwarden (example repo, open source password manager), CLI

## Relevance to our work
- **prosharness** (2/3): ProsHarness already has plan, critique and debate steps. Scheduled mid-run review checkpoints (25/50/75%) and independent reviewers on Claude Code runs would extend those steps. → *Add a ProsHarness skill that runs a fresh-context critique at 25/50/75% of a Claude Code run, using a different model than the implementer, and records the findings in the checkpoint.*
- **general** (2/3): Turning review comments into persistent rules that feed future agent context matches the user's interest in context engineering and tribal knowledge. → *Write a small pipeline that converts recurring PR review comments into CLAUDE.md-style rules and injects them into the coding agent's context before generation.*
- **agentos** (1/3): The talk covers code review, not infrastructure. Its one reusable idea is that independent reviewers with different models add a useful signal, which applies to LLM-judge evals. → *When adding LLM-judge evals to AgentOS (for example RAGAS-style checks in MemoryMesh), run a second judge model and treat disagreement as a triage signal.*
