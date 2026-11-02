# The UX of AI: Making AI-Powered Apps Your Users Don't Hate - Kathryn Grayson Nanz, Progress Software

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `L3RuP_q8Bwc` · [watch](https://youtu.be/L3RuP_q8Bwc) · **date:** 2026-08-18 · **length:** 35:59 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kathryn Grayson Nanz · **orgs:** Progress Software
- **topics:** product-ux, security-guardrails · **tags:** ux, trust, citations, human-in-the-loop, streaming, undo-checkpoints, permissions, agent-approval, cost-estimates, ai-labeling

> Kathryn Grayson Nanz (Progress Software) on designing AI features users trust. Organizes UX problems into five areas (trust, clarity, control, transparency, meaningful benefit) and gives concrete UI patterns for each.

## Summary
The speaker argues that AI's non-deterministic output and unfamiliar interaction patterns create a wide gap between developers and users, and that poor AI UX makes users disengage after a few bad results. She compares the situation to early Macintosh UI history, saying AI UX is roughly at "System 3", and says users' existing mental models (such as chat bubbles) can be reused but need adapting. She argues AI cannot design these patterns for us because it only remixes existing ones, and AI-generated UI looks average. The core of the talk is five user-challenge categories, each with patterns: citations and source links for trust, live streaming and visible reasoning for clarity, action-plan approval, a prominent stop button and scaled undo/checkpoints for control, granular and revocable permissions with cost/time estimates for transparency, and examples, templates and next-step actions for meaningful benefit. The talk gives no benchmarks or adoption data; it is design guidance from user research and experience.

## Key ideas
- **Trust is the biggest adoption hurdle, and honesty about limits earns more trust than claims of superiority.** — Users see AI as a black box and have seen hallucinations. Saying 'ours is more reliable' is hard to back up, so build patterns that let users check and correct output. ([10:38](https://youtu.be/L3RuP_q8Bwc?t=638))
- **Cite sources and link back to them so users can verify and reuse content with a trail of accuracy.** — Tooltips with quotes suit credibility, inline links suit external sources, and a side panel suits research tools (AI as librarian). Citations also protect the user's own reputation when they reuse the output. ([11:58](https://youtu.be/L3RuP_q8Bwc?t=718))
- **Show an action plan and get approval before an agent acts, and label AI-generated content.** — Plan-then-confirm flows (as in Claude or ChatGPT agent modes) build trust. Toggles for always-allow are needed so repeat users are not forced to babysit. Marking AI content (disclaimer, watermark, asterisk) avoids the sense of being tricked. ([14:51](https://youtu.be/L3RuP_q8Bwc?t=891))
- **Clarity beats 'magic': stream output and show reasoning so users can act early and stay engaged.** — Streaming hides latency and lets users interrupt or refine early. Visible chain-of-thought lets users find where a result went wrong and give more precise corrections. Highlight new or changed content so autonomous changes get noticed. ([18:58](https://youtu.be/L3RuP_q8Bwc?t=1138))
- **Control means a prominent stop button and undo/checkpoints sized to the task.** — The stop control must be visible, not hidden in a menu. Simple chat may need no history, a document editor needs about 10 steps of undo/redo, and advanced work needs checkpoints. Granular revert matters because output quality is mixed. ([23:15](https://youtu.be/L3RuP_q8Bwc?t=1395))
- **Transparency means granular, revocable permissions with history, plus time and cost estimates and a visible signal when an agent is acting.** — Permissions are not yes/no: scope by resource (read vs delete, one folder vs all) and by notification level. Users need to see what was granted and when, and to revoke it. Show rough time and token or credit cost before approval, and show a banner or outline when an agent drives the browser. ([27:22](https://youtu.be/L3RuP_q8Bwc?t=1642))

## Techniques
- **Source citations with graded surfaces** — Pick the citation UI by context: tooltip with a short quote for credibility, inline link for external sources, side panel for research tools where the AI acts as a librarian. Link each claim to its source. *When:* Any generated answer that users will reuse or verify, such as RAG answers or research summaries.
- **Plan approval before agent execution** — Show the agent's step list first and wait for confirmation. Offer a toggle to skip or always-allow for repeat flows. *When:* Agentic tools whose actions are hard to roll back or whose steps users need to understand.
- **AI content labeling** — Mark AI-generated text, images or video (disclaimer, watermark, or a small marker). Indicate which parts need manual checking. *When:* Any product that shows generated content to users who may distrust it.
- **Streaming and visible reasoning** — Stream partial output as it is generated and surface the model's rationale in chat so users can read, interrupt or follow up early. *When:* Long or slow generations and chat-based interactions where users might otherwise leave the tab.
- **Change highlighting** — When content is added or revised, mark it (color change, box, highlight, or diff-style lines for code) and move focus to it when needed. *When:* Agents that edit content while the user is not watching.
- **Prominent kill switch** — Put an always-visible stop control that halts generation, workflow steps, or scripts at any point. Do not bury it in a menu or require a command. *When:* Any autonomous or long-running AI action.
- **Task-scaled version history** — Use simple conversation rephrasing for chat, about 10 steps of undo/redo for editing tools, and named checkpoints or save states for advanced work. Let users keep some changes and revert others. *When:* Products where AI rewrites user content and output quality varies across steps.
- **Granular revocable permissions** — Offer scoped grants (per resource, per action type, once vs ongoing, notify each time). Show a history of what was granted and when, with a revoke control. Support memory forget as well as remember. *When:* Agents that access user data, tools, or accounts.
- **Pre-approval cost and time estimates** — Show a rough estimate of time and cost (money, tokens or credits) in the same step as the plan approval, so users can adjust scope. *When:* Agent or batch tasks with variable cost.
- **Guided starts and next-step actions** — Provide templates, example prompts and guided workflows. After output, offer next-step buttons and integrations (export, send, open ticket, push code) so results get used. *When:* AI features where users do not know what to ask or what to do with the result.

## Numbers
- No benchmarks, latency figures, costs or adoption statistics are given. The talk is qualitative and based on user research and experience. It names five user-challenge categories (trust, clarity, control, transparency, meaningful benefit). ([9:17](https://youtu.be/L3RuP_q8Bwc?t=557))

## Hot takes
- AI-generated UI tends to look pretty average, so it works as a starting point but not as an ending point.
- The differentiator for AI-powered software is no longer model performance but the quality of the experience built around the model.
- Honesty about current limits will earn more user trust than claims that our AI is more trustworthy.
- Developers' technical literacy is always higher than users', so UX is the bridge; AI's non-determinism widens that gap.

## Tools mentioned
Claude, ChatGPT, Microsoft Copilot, Microsoft Teams

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs long Claude Code jobs with plan, critique and approval steps. The talk's plan-approval, kill-switch and checkpoint patterns map directly onto its run controls and phone approvals. → *Add an always-visible stop control and a per-run cost/time estimate to the plan-approval step in the phone approval flow, and check how checkpoint/resume is presented to the user.*
- **agentos** (1/3): AgentOS governs agents with budgets, PII scans and exec gates. The talk's permission-scoping, revocation history and cost-visibility advice is relevant to how those controls are shown to the user, but it is not core to the infra. → *Read the permissions and transparency section (27:22) when designing how Crucible exec-gate and budget decisions are surfaced to a user.*
- **general** (1/3): The five-category checklist (trust, clarity, control, transparency, meaningful benefit) is a usable review checklist for any AI feature UI. → *Use the five categories as a pre-ship review checklist for any AI-facing feature in our projects.*
