# I Spent Two Years Building the Median — Hariprasad Sudharshan

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `0JZy5AuuQzc` · [watch](https://youtu.be/0JZy5AuuQzc) · **date:** 2026-10-15 · **length:** 36:11 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Hariprasad Sudharshan · **orgs:** Anthropic, Mistral, Cursor, Lovable, Replit, LlamaIndex, GitHub
- **topics:** product-ux, agent-architecture, infra-cost-scaling · **tags:** novelty, median, build-first, harness-vs-model, distribution-moat, open-weights, inference-cost, product-strategy, opinionated-design

> Hariprasad Sudharshan argues that with rented models and harnesses, most AI-built products converge on a "median," so durable value needs a deliberate novelty, a strong opinion, and distribution.

## Summary
The speaker, a product person with about two decades in software, opens by arguing that the world still runs on deterministic, hand-built software and that AI's main roles are to speed up building that software and to tackle problems that were previously too costly. He separates the model (the engine), the harness (tools, context, memory, orchestration), and the product, and says comparisons like Claude Code vs Cursor are harness comparisons, not model comparisons. Because everyone can rent the same models and harnesses, output converges on a "median" product that gets better with each release but is hard to tell apart from competitors. He says that once a solution is free, distribution becomes the moat. He describes his own two years of "build-first" projects (including a RAG system that duplicated existing open-source work) and proposes a "novelty budget" to name one truly novel element before building. He offers four rules (be opinionated, accept that prompt-to-production is a median path for internal tools, treat the agent's "done" as the starting point, and look for the next foundational building block) and three questions (who has done this, what do we have that others lack, where will it live). He closes with a plug for a calculator comparing self-hosting open weights against token API pricing, noting the many serving layers (KV cache, batching, parallelism) that open weights alone do not provide.

## Key ideas
- **Most of the world still runs on deterministic software, and AI's real roles are speeding up that software and tackling problems that were too costly before.** — The speaker treats software as the infrastructure of modern life and says the AI-assisted part is the probabilistic process used to produce reliable deterministic artifacts, not the final product. ([0:38](https://youtu.be/0JZy5AuuQzc?t=38))
- **Model, harness and product are separate layers, and comparing harnesses is not comparing models.** — He calls the model the engine, the harness the tools, context, memory and orchestration around it, and the product the end user value. Leaderboard Elo gaps are relative to one evaluation, not absolute intelligence. ([9:03](https://youtu.be/0JZy5AuuQzc?t=543))
- **Shared models and harnesses make output converge on a 'median' that is good enough to ship but hard to tell apart.** — Because the same capability is available to everyone, teams that start from the same problem reach similar solutions, and each model release moves the median up. ([12:27](https://youtu.be/0JZy5AuuQzc?t=747))
- **When the median is free, distribution becomes the moat rather than the product.** — Similar products flood the market, so the speaker argues that reach to customers decides the winner, not the build itself. ([13:00](https://youtu.be/0JZy5AuuQzc?t=780))
- **The 'build-first reflex' produces duplicate systems, such as his own 4,000th-style RAG build.** — An agent can produce a demo in hours, but the speaker found he had rebuilt a solved problem that mature open-source projects already covered. He says he used to search more than build and now it is reversed. ([18:31](https://youtu.be/0JZy5AuuQzc?t=1111))
- **A novelty budget: name the one novel element before the spend begins, and review it like a project budget.** — If no novel element can be named, the speaker says the project should be treated as a learning exercise. He also says every project needs a stated novelty in the roadmap. ([24:05](https://youtu.be/0JZy5AuuQzc?t=1445))
- **Four rules to beat the median: be opinionated, accept a median path for internal tools, treat the agent's 'done' as the starting line, and look for the next foundational building block.** — He says an opinion is the cheapest novelty and that the coding agent gives 'the last great design for free', so the human job is to find what comes next. ([26:21](https://youtu.be/0JZy5AuuQzc?t=1581))
- **Three questions to ask before building: who has done this, what do we have that others lack, and where will it live?** — The first forces a search, the second forces a novelty statement, and the third forces distribution thinking before a demo is built. ([28:37](https://youtu.be/0JZy5AuuQzc?t=1717))
- **Open weights are not the same as open inference; many serving layers sit between the weights and a usable token service.** — He lists precision, KV cache, batching, execution parallelism and utilization as layers that need specialist skills. He says some of these, such as utilization, cannot be bought off the shelf. ([31:28](https://youtu.be/0JZy5AuuQzc?t=1888))

## Techniques
- **Novelty budget** — Before building, write down the one thing that is novel about the project. Put it in the roadmap and review it like spend. If none can be named, label the work a learning exercise. *When:* Starting any project that might compete in an open market or with many similar tools.
- **Three-question pre-build check** — Ask who has already done this (forces a search), what do we have that others do not (forces novelty), and where will this live (forces a distribution plan) before building or demoing. *When:* Before an agent-built demo turns into a product plan, especially on a team using the same tools as competitors.
- **Separate model, harness and product in comparisons** — When comparing AI tools, name which layer you are testing: the model, the harness (tools, context, memory, orchestration) or the product. Do not read a harness comparison as a model comparison. *When:* Evaluating tools or writing benchmark or roadmap arguments that mention a model.
- **Treat agent done as a median baseline** — Take the output the agent calls finished as a starting draft, then add the opinionated design and novel parts yourself. *When:* Deciding how much human work is left after an agent says a task is complete.
- **Self-hosting break-even calculator** — Compare the cost of running identical open weights inside your own infrastructure with the cost of paying per token to a hosted provider. The speaker built this calculator for enterprises. *When:* Deciding whether to self-host open-weight models or keep paying for tokens.

## Numbers
- Software industry described as driving a 125 trillion dollar economy ([1:45](https://youtu.be/0JZy5AuuQzc?t=105))
- Anthropic scored 1503 vs Mistral 1460 on a relative rating, which the speaker says is an 87-point gap in one comparison and not an absolute intelligence gap ([9:03](https://youtu.be/0JZy5AuuQzc?t=543))
- Stanford study cited for a gap of a few dozen Elo points between models ([8:30](https://youtu.be/0JZy5AuuQzc?t=510))
- Speaker says about 100,000 repos and millions of AI-built apps now exist, and he counts the success of an app by its creator's goal ([15:11](https://youtu.be/0JZy5AuuQzc?t=911))
- Demo in about 2 hours, with a launch possible in about 4 weeks for a real product ([19:03](https://youtu.be/0JZy5AuuQzc?t=1143))
- Speaker searched 244 calculators and found none that compared self-hosted open weights with token API costs ([32:33](https://youtu.be/0JZy5AuuQzc?t=1953))
- Two years of build projects used several million tokens across multiple Max plans ([25:13](https://youtu.be/0JZy5AuuQzc?t=1513))
- Speaker says a team of several people and a quarter of time is what a comparable product used to take, and new engineers now claim to match it quickly ([29:13](https://youtu.be/0JZy5AuuQzc?t=1753))
- Speaker cites a total software-economy figure of 100 trillion dollars later in the talk, which differs from the 125 trillion he gave earlier ([35:20](https://youtu.be/0JZy5AuuQzc?t=2120))

## Hot takes
- 'AI slop' is a lazy label; the success of a product should be judged against its creator's goal, not expert taste.
- The median is free, so distribution is the real moat.
- Comparing Claude Code with Cursor is a harness comparison, not a model comparison.
- Leaders cannot calibrate by reading or watching; they have to build to develop intuition.
- Open weights are not open inference, because serving layers are hard to buy.

## Tools mentioned
Claude Code, Codex, Cursor, Lovable, Replit, LlamaIndex, vLLM, Max plan

## Relevance to our work
- **agentos** (2/3): The talk's point that self-hosting open weights requires many serving layers, and its break-even framing against per-token API cost, bears directly on InferCraft on one RTX 5090. → *Write a break-even check: the cost per million tokens of running the model mix AgentOS serves on the 5090 vs paying per token for the same models, then decide whether InferCraft work is justified.*
- **agentos** (1/3): The talk argues that a project needs a named novelty and that open-source alternatives should be searched first. MemoryMesh's RAG layer is an example of a crowded area. → *Name AgentOS's one novel element in writing and check existing open-source RAG and memory projects before adding more retrieval code.*
- **prosharness** (1/3): The talk locates differentiation in the harness, which is ProsHarness's layer, and says harness features are converging. → *Identify which ProsHarness feature (checkpoint/resume or plan-critique-debate) is hard to copy and state it as the project's novelty.*
