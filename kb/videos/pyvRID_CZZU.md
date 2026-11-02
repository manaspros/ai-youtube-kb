# We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `pyvRID_CZZU` · [watch](https://youtu.be/pyvRID_CZZU) · **date:** 2026-10-05 · **length:** 16:19 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Matt Lawler · **orgs:** AssemblyAI, Railway, Pylon, Voyage AI
- **topics:** agent-architecture, context-engineering, voice-multimodal, enterprise-adoption · **tags:** customer-support-agent, claude-agent-sdk, claude-md-guardrails, docs-as-markdown, agentic-file-search, voyage-embeddings, railway-deploy, voice-agent, dogfooding, escalation-backlog, forward-deployed-engineer

> AssemblyAI's FDE team built "Joey," a Claude Agent SDK support agent over local markdown docs, lifting end-to-end ticket resolution from 10% to 80% for about $700/month; the talk also argues for dogfooding your own product.

## Summary
Matt Lawler, a forward-deployed engineer at AssemblyAI, describes replacing an off-the-shelf docs support bot (about 10% resolution) with an in-house agent called Joey. Joey runs on the Claude Agent SDK, keeps all product docs, changelog, pricing and website pages as local markdown that syncs on every docs push, and uses Voyage embeddings for first-pass retrieval plus agentic search over the file system for harder questions. Behavior is steered by a very large CLAUDE.md of guardrails that the team updates after every bad conversation. The agent is packaged in Docker and deployed on Railway, so a merged PR is live in about 30 seconds and bugs seen in live chats can be fixed mid-session. Joey escalates about 20% of tickets, and the escalation reasons serve as a backlog of what to automate next. The team also put a voice front end on Joey using their own voice agent API, which the speaker used to learn latency and barge-in problems first-hand. The talk is partly a product pitch, and the 80% figure is self-reported with no accuracy eval described.

## Key ideas
- **Forward-deployed engineering does not scale to high inbound volume** — At about 1,000 API signups a day, one onboarding engineer cannot take every call. The speaker's advice is that FTEs should automate their own job, since they should not be the bottleneck to a good customer experience. ([2:35](https://youtu.be/pyvRID_CZZU?t=155))
- **Deflection bots fail when you cannot change the system prompt, tools or RAG** — The bought support bot resolved only about 10%, and the vendor's roadmap was the only route to fixes. Owning the prompt, tools and retrieval is what made fast iteration possible. ([3:32](https://youtu.be/pyvRID_CZZU?t=212))
- **Keep the product docs as local markdown the agent can search like a filesystem** — Docs, changelog, pricing and website pages are synced to the agent's repo on every update, so it can cite source URLs. Embeddings give a fast first pass, and agentic search over the files handles multi-hop questions. ([5:59](https://youtu.be/pyvRID_CZZU?t=359))
- **Behavior is tuned with a large guardrail file that grows from observed failures** — The CLAUDE.md is about 30,000 lines of rules and advice. After a bad conversation or wrong answer, the team edits it and every later conversation benefits. ([11:54](https://youtu.be/pyvRID_CZZU?t=714))
- **Container-to-PaaS deploys make prompt and code fixes live within seconds** — The agent ships as a Dockerfile on Railway. A merged PR goes live in about 30 seconds, and the team has patched a live conversation and saved the session without the customer noticing. ([7:21](https://youtu.be/pyvRID_CZZU?t=441))
- **Escalations are a roadmap of what to automate next** — Joey escalates about 20% of tickets, such as rate changes, data opt-outs and signed agreements. Each category is a list of capabilities still to build, for example giving Joey a BAA link or letting him quote pricing. ([8:28](https://youtu.be/pyvRID_CZZU?t=508))
- **Dogfooding a voice agent teaches the latency and turn-taking problems first-hand** — The same tools were wired to a voice front end on one speech-to-text, LLM and TTS WebSocket. Building it gave the team direct experience with latency, interruptions and barge-in, which they say improves customer advice. ([9:43](https://youtu.be/pyvRID_CZZU?t=583))

## Techniques
- **Docs-as-markdown synced into the agent's workspace** — Convert docs, changelog, pricing and web pages to markdown in a repo. Sync it on every docs push, keep the source URLs so the agent can cite them, and let the agent grep or read the files directly. *When:* When the agent must answer product questions that change often and must stay accurate even if the docs site is down.
- **Two-stage retrieval: embeddings first, then agentic file search** — Use an embedding model to pre-fetch the most relevant docs into context. For confusing or multi-part questions, let the agent search the file system itself and combine resources. *When:* When the corpus is small enough to browse as files, and some questions need several documents joined together.
- **Guardrail CLAUDE.md as the behavior-tuning loop** — Keep a single instructions file for the agent. After each bad interaction, add or change a rule and ship it. Judge the change by how later conversations behave. *When:* For a customer-facing agent where prompt and policy changes must take effect without retraining or a model swap.
- **Escalation reason taxonomy as a product backlog** — Log every handoff to a human with a reason category. Treat each recurring category as a capability gap and automate them one at a time. *When:* When you want to know which parts of the human workload to automate next.
- **PaaS deploy from a Dockerfile for fast fix cycles** — Containerize the agent and deploy on a managed platform, so a merged PR is live in about 30 seconds without manual ops. *When:* When the team wants to patch live agent behavior quickly and avoid running its own infrastructure.
- **Monitoring through the existing support tool** — Make the agent a member of the support team inside the ticketing tool, so it has the same conversation access, memory of past customers and metrics tracking as a human. *When:* When the agent should be measured and managed like a support agent rather than a separate chatbot.

## Numbers
- About 1,000 API signups per day at the time of the talk ([1:20](https://youtu.be/pyvRID_CZZU?t=80))
- Off-the-shelf docs support bot resolved about 10% of conversations, leaving about 900 tickets a day for the human team ([3:32](https://youtu.be/pyvRID_CZZU?t=212))
- End-to-end resolution rose from 10% to 80% in the first week with a naive implementation, self-reported as no human in the loop ([7:21](https://youtu.be/pyvRID_CZZU?t=441))
- Total token and infrastructure cost of about $700 per month ([7:21](https://youtu.be/pyvRID_CZZU?t=441))
- A PR-to-live deploy takes about 30 seconds on Railway ([7:21](https://youtu.be/pyvRID_CZZU?t=441))
- Joey escalates about 20% of tickets to a human ([8:28](https://youtu.be/pyvRID_CZZU?t=508))
- The guardrail CLAUDE.md is about 30,000 lines ([11:54](https://youtu.be/pyvRID_CZZU?t=714))

## Hot takes
- Automate yourself out of the FTE job: every forward-deployed engineer should build the agent that replaces their repeated work.
- Owning the system prompt, tools and RAG matters more than the vendor's deflection rate, because you cannot iterate on a black box.
- Dogfood your own product by building what your customers build, not only teaching it.

## Tools mentioned
Claude Agent SDK, Claude Code, CLAUDE.md, Railway, Docker, Pylon, Voyage AI embeddings, AssemblyAI voice agent API, Slack, WebSocket

## Relevance to our work
- **prosharness** (2/3): Shows a Claude Agent SDK agent that improves through a versioned guardrail file and fast redeploys. This matches ProsHarness's checkpoint and loop model, but the talk gives no checkpoint or approval details. → *Add a rule to ProsHarness: each failed run adds one guardrail line to the project CLAUDE.md, and the next N runs are scored against that change.*
- **agentos** (1/3): Shows a production docs-QA agent that mixes embedding prefetch with agentic file search over a markdown corpus. This overlaps with MemoryMesh hybrid retrieval but gives no retrieval numbers. → *Run a small A/B on a docs QA set comparing MemoryMesh BM25+pgvector retrieval against agentic file grep over the same markdown, and record resolution and cost.*
- **general** (1/3): Relevant to the context-engineering interest. The 30,000-line guardrail file is an unmeasured scale data point, and the talk gives no measure of its effect. → *Read the Claude Agent SDK docs on large CLAUDE.md and instruction loading, then decide whether a line-count or staleness check belongs in the context-engineering notes.*
