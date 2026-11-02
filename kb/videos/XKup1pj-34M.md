# The New Application Layer - Malte Ubl, CTO Vercel

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XKup1pj-34M` · [watch](https://youtu.be/XKup1pj-34M) · **date:** 2026-05-18 · **length:** 18:52 · **format:** keynote · **quality:** 3/5 · **depth:** intro
- **speakers:** Malte Ubl · **orgs:** Vercel, Google, Anthropic, OpenAI
- **topics:** agent-architecture, sandboxing-execution, enterprise-adoption, product-ux · **tags:** application-layer, agent-archetypes, compress-the-research, agents-as-users, harness-vs-execution-separation, model-commoditization, europe, keynote, vercel, elastic-software-demand

> Vercel CTO Malte Ubl argues agents are a new kind of software that makes long-tail automation affordable, names practical agent archetypes, and says harnesses should run apart from the code they generate.

## Summary
Malte Ubl, CTO of Vercel, opens the first AI Engineer conference in Europe with a keynote on the "new application layer." His core claim is that cheap agents make software that was never economically viable to hand-code worth building, so total software demand rises rather than falls. He lists agent archetypes he sees working today: agent-as-a-service for support, "compress the research" for business processes that end in a human decision, surfacing information that already exists in a company, and finding agent use cases by asking staff what they hate about their jobs. He cites Vercel's own numbers: a Contact Sales agent that hands off about 75% of the time, an in-house support agent with a 90% deflection rate, and over 60% of Vercel.com page views in the last seven days coming from AI agents. He argues that infrastructure and UIs need CLI and API surfaces because agents are now users, and that most current agent harnesses are wrongly designed because they run in the same place as the code the agent generates. He ends by saying the application layer should stay stable across models, and that Europe is leading in application-layer work. Much of the talk is anecdote and opinion rather than measured data.

## Key ideas
- **Agents make a large class of software economically viable that was never worth hand-coding.** — Many if-statement-heavy business rules were never built because traditional software was too expensive. Agents lower that cost, so the set of automatable work grows. The speaker frames this as an economics experiment on how elastic the software market is, and argues demand for engineers rises as making software gets cheaper. ([4:12](https://youtu.be/XKup1pj-34M?t=252))
- **Compress the research: keep the business process but let an agent do the research step before a human decides.** — Many processes have the shape event, then research, then human decision. An agent that only does the research phase needs no process change and no added risk, and it saves time at high volume. Example: a sales-contact agent that does the research a person used to do in about 15 minutes. ([8:38](https://youtu.be/XKup1pj-34M?t=518))
- **Surface information the company already has but cannot practically use.** — Issue trackers go stale while the facts sit in Slack threads or meeting recordings. An agent that reads those sources and updates the tracker, or writes the status update a manager asks for, uses information that already exists. ([10:40](https://youtu.be/XKup1pj-34M?t=640))
- **Find agent use cases by asking staff what they hate most about their job.** — The speaker says Vercel's in-house support agent reached a 90% deflection rate, handling most requests in real time. Support staff job satisfaction went up because they no longer had to do repetitive work. ([11:07](https://youtu.be/XKup1pj-34M?t=667))
- **Software is increasingly used by agents, so UIs need CLI and API equivalents.** — The speaker says over 60% of page views in the last seven days were AI agents, and usage is moving from dashboard clicking to API and CLI. He asks of any proposed UI feature: what is the CLI, and how does an agent automate it? ([13:07](https://youtu.be/XKup1pj-34M?t=787))
- **Most current agent harnesses have the wrong architecture because they run in the same place as the code the agent generates.** — The speaker says the harness should be separated from the sandbox where generated code runs. He says Anthropic's new agent product also separates them, and treats this as a security and architecture point. ([14:36](https://youtu.be/XKup1pj-34M?t=876))
- **Build the application layer to be stable across models.** — Model X and model Y trade wins over time. The speaker expects model providers to commoditize and prices to fall, so the durable value sits in the application layer built on top, which he says does not require working at a model lab. ([15:36](https://youtu.be/XKup1pj-34M?t=936))

## Techniques
- **Compress-the-research agent** — Identify a business process shaped as event, then research, then human decision. Build an agent that only does the research step and writes its findings for the human. Leave the decision and the process unchanged. *When:* High-volume processes where research takes minutes to tens of minutes per item and the human decision must stay.
- **Information-surfacing agent** — Point an agent at existing sources (chat threads, meeting recordings, trackers) and have it produce updates, status summaries, or tracker edits on demand, instead of asking people to write them. *When:* When the data exists but is stale or scattered across tools and nobody has time to consolidate it.
- **Ask-what-you-hate discovery** — Ask staff which parts of their job they dislike most, then target those repetitive tasks for agent automation. *When:* Picking the first agent to build inside an organization, where the goal is removing toil rather than replacing judgment.
- **Harness and code execution split** — Run the agent harness (the loop that calls the model and tools) separately from the environment where model-generated code runs, such as an isolated sandbox. *When:* Any agent that executes generated code, to limit the blast radius of security failures.
- **CLI and API first for agent-facing products** — For each UI feature, also expose a CLI or API so agents can drive it. Treat the UI as a thin layer over the same operations. *When:* Products where agent traffic is growing and agents must perform the same actions as people.
- **Lightweight bash sandbox for agents** — The speaker built a TypeScript bash interpreter that gives agents a sandbox with very fast startup, because agents tend to use bash. *When:* Agents that need quick, cheap execution of shell-like commands without a full VM.

## Numbers
- Contact Sales agent on Vercel.com: about 75% of the time the agent decides the visitor just wanted support and hands it to the support team. ([9:38](https://youtu.be/XKup1pj-34M?t=578))
- Example research compression: a task that took a person about 30 minutes can take about 5 minutes with an agent; a Contact Sales lead check took about 15 minutes before. ([8:38](https://youtu.be/XKup1pj-34M?t=518))
- Scale example: a process run 100,000 times a year saves a company a large amount when the research phase is automated. ([8:38](https://youtu.be/XKup1pj-34M?t=518))
- In-house Vercel support agent: 90% deflection rate, meaning it resolves or helps in real time for most cases. ([11:07](https://youtu.be/XKup1pj-34M?t=667))
- Over 60% of page views on Vercel.com in the last seven days came from AI agents (not previously published, per the speaker). ([13:07](https://youtu.be/XKup1pj-34M?t=787))
- Speaker cites the Vercel AI SDK as having reached over $10 million a week. The caption is garbled here, so the metric (likely downloads or spend) is unclear. ([16:37](https://youtu.be/XKup1pj-34M?t=997))

## Hot takes
- The cheaper software gets, the more software gets made, so demand for software engineers goes up.
- SaaS companies will be fine even as companies build more of their own software.
- Most popular agent harnesses have the wrong architecture because they run where generated code runs.
- Model companies are commoditizing. The big value will sit in the application layer, not with the model labs.
- Europe is leading in AI engineering application-layer innovation despite not leading in models.
- Security will get much worse before it gets better, with a 1999-style rude awakening.

## Tools mentioned
Vercel AI SDK, Chat SDK, JustBash, Claude, Codex, Granola, Pi, OpenClaw

## Relevance to our work
- **agentos** (1/3): Speaker's claim that harness and generated-code execution should be separated bears on Crucible's sandboxed code execution, though the talk gives no implementation detail. → *Check whether Crucible runs the agent loop in the same process or host as the code it executes, and if so, split them into separate processes or hosts.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, so the harness-versus-execution split the speaker describes applies to where its loops and generated commands run. → *Audit whether ProsHarness runs generated shell commands in the same environment as the harness; if so, evaluate a separate sandbox boundary.*
