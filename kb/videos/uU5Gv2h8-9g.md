# Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `uU5Gv2h8-9g` · [watch](https://youtu.be/uU5Gv2h8-9g) · **date:** 2026-07-18 · **length:** 51:30 · **format:** interview · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Thariq Shihipar, Cat Wu, Simon Willison · **orgs:** Anthropic
- **topics:** claude-code, pr-code-review, security-guardrails, context-engineering · **tags:** claude-code, claude-tag, claude-fable, auto-mode, code-review, prompt-design, system-prompt, credential-injection, evals, dogfooding, multiplayer-agents, team-memory, remote-control, fireside-chat

> Anthropic's Thariq Shihipar and Cat Wu, with Simon Willison, on how Claude Code and Claude Tag change team workflows, code review, auto mode safety, and prompt design, with internal claims about PR share and prompt size.

## Summary
A fireside chat with two Anthropic Claude Code team members (Thariq Shihipar, Cat Wu) moderated by Simon Willison. They describe how the product team works now: product taste matters more than execution, and rewrites and multiple implementations are cheap enough to try. They explain Claude Tag, a multiplayer Slack agent with channel-level memory, which they say lands 65% of internal product-engineering PRs. On code review, they describe a six-plus-month ramp from human review of everything to letting Claude Code review outer-layer changes, with incident PRs fed back into an eval set. They say frontier models got a system prompt roughly 80% smaller by replacing hard "always/never" rules with context, and they keep separate prompts per model. Auto mode, a classifier that judges each tool call and network escape against the conversation and the user's own instructions, is said to be used by almost everyone internally and to mitigate red-team attacks, with evals promised. Much of the talk is anecdote and vendor claims, but the process details (trust ramp, eval-gated model swaps, prompt softening) are concrete.

## Key ideas
- **Product taste now matters more than execution** — The speaker says the gap from idea to shipped feature has shrunk from 6-12 months to maybe a week, so the scarce skill is deciding what is worth building, not building it. ([3:49](https://youtu.be/uU5Gv2h8-9g?t=229))
- **Codebase as the only spec, and rewrites are viable** — With a good test suite, a rewrite forces the test suite to be good. Spinning up several implementations and picking the most accurate one is a workable method. ([4:59](https://youtu.be/uU5Gv2h8-9g?t=299))
- **Claude Tag is multiplayer and proactive** — It lives in Slack channels, several people can steer one session, it can monitor a channel for bug reports for its lifetime, and team preferences given in natural language persist as channel memory. ([6:50](https://youtu.be/uU5Gv2h8-9g?t=410))
- **Trust in AI code review is built in stages** — Start with human review of everything, then drop humans for file areas where review catches all issues. Add incident-causing PRs to an eval set so later changes do not regress. Core code keeps code owners. ([15:13](https://youtu.be/uU5Gv2h8-9g?t=913))
- **Model swaps are gated by the eval suite** — A new model replaces the old one only if it is strictly better on the full eval set. Capability evals come first, then behavioral evals are built from user complaints, ranked by priority. ([17:26](https://youtu.be/uU5Gv2h8-9g?t=1046))
- **Replace absolute prompt rules with conditional context** — An instruction like 'always verify' is true 90% of the time, and the 10% exceptions confuse the model. Rewording to context-conditioned guidance and giving fewer hard constraints worked better, and the system prompt was cut sharply for frontier models. ([23:08](https://youtu.be/uU5Gv2h8-9g?t=1388))
- **Auto mode as a classifier over tool calls and user intent** — A separate classifier judges each turn, bash call, and permission prompt using the tool call plus conversation context, including the user's own stated permissions (e.g. 'don't push'). It also handles sandbox escape requests such as network calls. ([31:22](https://youtu.be/uU5Gv2h8-9g?t=1882))
- **Credential injection at a proxy so the agent never holds secrets** — The agent sends requests without the real credential. A proxy recognizes the destination and swaps in the real token on the fly, so the agent can use Datadog without being able to read the key. ([36:09](https://youtu.be/uU5Gv2h8-9g?t=2169))

## Techniques
- **Staged trust ramp for AI code review** — Begin with human review of all PRs. For each area, when the AI reviewer catches 100% of the issues humans found, drop the human gate for that area. After every incident, add the causing PR to an eval set and update the reviewer. Keep code owners on core paths. *When:* Adopting agent-written code review in a repo where quality bars are high and incidents are tracked.
- **Eval-gated model swap** — Run the full eval set on the current and candidate models. Switch only if the candidate is strictly better on the eval set, not just on a few examples. *When:* Deciding whether a new model can replace the old one in a production agent or reviewer.
- **Behavioral evals built from user complaints** — Turn complaints such as the agent stopping early, saying it is time to sleep, or asking to continue after finishing 2 of 5 parts into evals. Rank them by user priority and add one at a time. *When:* Measuring UX-level agent behavior that capability evals miss.
- **Conditional prompt wording over absolute rules** — Write 'most of the time when doing X, do Y, unless Z' instead of 'always do Y'. Review each instruction for the edge cases where it is false. Prefer context and fewer hard constraints. *When:* Editing system prompts, CLAUDE.md, or skill files that conflict with user instructions.
- **Per-model system prompts** — Maintain different system prompts for frontier and older models. Frontier models get a shorter prompt that relies on judgment; older models keep the full prompt with more guardrails. *When:* Serving a model range where older or cheaper models lack the judgment that frontier models have.
- **Classifier-based permissions using user intent** — Judge each tool call with a classifier that sees the tool call, the conversation, and the user's stated permissions. Prompt the user only when the classifier cannot decide. *When:* Reducing permission prompts while keeping safety, for long-running agents.
- **Credential injection through a proxy** — The agent calls the upstream host with no real secret. A proxy matches the host, adds the real token, and forwards the request. Credentials stay out of the agent's reach and out of its logs. *When:* Giving agents access to third-party APIs such as observability or SaaS tools without exposing the key.
- **Fewer tools with distinct functions** — Keep the tool count low. Each tool should do something no other tool does, so the model can choose reliably. Remove tools that a general shell tool can replace once the trust level is high. *When:* Designing the tool surface for a coding agent.
- **Multiplayer channel agent with shared memory** — Give each channel its own shared memory file. Sessions can write findings back to the channel memory. Team members steer the same session and copy how others use it. *When:* Building team-facing agents where several people share the same context.
- **Dogfooding gate before launch** — Ship first to internal users, then to early customers who give harsh feedback. Launch only when active users and retention cross a clear internal bar. *When:* Deciding whether a feature is ready for external release.

## Numbers
- Claude Tag lands about 65% of Anthropic's product-engineering PRs internally (speaker's figure, product-engineering team only) ([6:50](https://youtu.be/uU5Gv2h8-9g?t=410))
- Idea-to-build time has dropped from 6-12 months to maybe a week ([3:49](https://youtu.be/uU5Gv2h8-9g?t=229))
- Removing humans from code review for outer-layer changes took a six-plus-month trust-building process ([15:13](https://youtu.be/uU5Gv2h8-9g?t=913))
- System prompt for frontier models reduced by about 80% (Fable and Opus 4.8), with older models keeping the full prompt ([20:50](https://youtu.be/uU5Gv2h8-9g?t=1250))
- Auto mode has been used internally since January, and almost everyone at Anthropic uses it ([34:48](https://youtu.be/uU5Gv2h8-9g?t=2088))
- Claude Code launched February of last year (speaker says under a year and a half ago) ([0:08](https://youtu.be/uU5Gv2h8-9g?t=8))

## Hot takes
- The old advice to never rewrite a codebase is out of date when a good test suite and cheap implementations exist.
- Absolute prompt rules like 'always verify' hurt more than they help once models have good judgment.
- Tool design is more like biology than physics: it is hard to predict and needs evals.
- Building your own AI Slack bot is risky because every feedback channel is an injection path.
- Auto mode's claimed safety is better than the average human reviewer for the main risk categories (prompt injection, exfiltration), though not perfect.

## Tools mentioned
Claude Code, Claude Tag, Slack, GitHub, Datadog, FFmpeg, Remotion, Gemini API, Mountain Project, Claude Fable, Claude Opus 4.8, Claude Mythos

## Relevance to our work
- **general** (3/3): Rewriting absolute rules as conditional context, and building evals from complaints, applies to CLAUDE.md, skills, and any agent prompt the user maintains. → *Audit CLAUDE.md and skill files for absolute always/never rules, rewrite them as conditional guidance, and re-run the affected tasks to check for regressions.*
- **agentos** (2/3): The credential-injection proxy and per-call classifier map onto the L1 proxy (Govrix Scout) with budgets and PII/injection scanning, and the sandbox escape handling maps onto Crucible. → *Prototype a placeholder-token swap in Govrix Scout so agent processes never hold upstream API keys, and test it on one third-party tool call.*
- **prosharness** (2/3): ProsHarness has phone-driven approvals. A classifier that reads the user's own stated permissions could cut prompts, and the talk notes that remote-control from a phone is a real workflow. → *Add a first-pass classifier to ProsHarness approvals that reads the user's stated permissions, and send only uncertain calls to the phone.*
