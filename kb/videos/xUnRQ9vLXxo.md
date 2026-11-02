# Everything we knew about software has changed — Theo Browne, @t3dotgg ​

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `xUnRQ9vLXxo` · [watch](https://youtu.be/xUnRQ9vLXxo) · **date:** 2026-07-18 · **length:** 16:02 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Theo Browne · **orgs:** Y Combinator (referred to as 'a combinator'), Apple, Vercel, Slack, Salesforce, AWS
- **topics:** product-ux, coding-agents, agent-architecture, multi-agent · **tags:** model-eras, orchestration, markdown-as-program, cron, breadth-vs-depth, platform-extensibility, inherited-assumptions, skeuomorphism, startup-tiers

> Theo Browne argues that models have moved coding into an orchestration era, so tools, product tiers and software defaults should be rethought, with a markdown file running on cron as his example.

## Summary
Theo Browne describes model progress as eras: Sonnet 3.5 made tool calls reliable, Opus 4.5 handled long multi-step tasks, and Mythos can split work across sub-models and verify it. He says the models now carry work that used to need custom orchestration, so you can prompt for it instead. He argues developers keep inherited habits (terminal-first UX, committing only code to git, language identity, reluctance to delete code) that no longer serve them. His main example is a personal PR-triage service that is now a markdown prompt run by Claude or Codex on a 9 a.m. cron, which writes a static HTML page and uploads it to S3. He says product tiers have shifted down one level, so what was a startup is now a side project, and that a product should offer enough breadth for users to add missing features themselves, as Slack does through its bot APIs. The talk is mostly opinion and anecdote, with few measured results.

## Key ideas
- **Model progress has come in eras: tool calls, then long-running tasks, then orchestration.** — Sonnet 3.5 was the first model to make tool calls reliably enough for daily codebase work. Opus 4.5 kept track over much longer tasks. Mythos is described as the first model that understands itself well enough to spawn sub-models, split work and verify it afterwards. ([1:14](https://youtu.be/xUnRQ9vLXxo?t=74))
- **Orchestration can be prompted rather than built.** — The speaker claims you no longer need custom tooling or a software factory to get multi-model orchestration. You tell the model to go further and it does, though no measurements are given. ([2:35](https://youtu.be/xUnRQ9vLXxo?t=155))
- **Developers keep inherited habits that may not be right anymore.** — He points to a terminal-as-interface habit, a rule against committing environment files, identity built around languages, and reluctance to delete work. He asks whether each practice is correct or just familiar. ([4:06](https://youtu.be/xUnRQ9vLXxo?t=246))
- **The product tier of a given idea has dropped by one level.** — Ideas that used to be a startup can now be a side project, and a side project can be a markdown file. The gap at the bottom of his tiers is a product that is only a markdown file. ([10:48](https://youtu.be/xUnRQ9vLXxo?t=648))
- **A markdown prompt can run as a recurring service.** — His PR-triage service checks open PRs across four GitHub repos, judges status and priority, regenerates a static HTML page, uploads it to S3 and returns the URL. A cron runs it each morning. ([11:49](https://youtu.be/xUnRQ9vLXxo?t=709))
- **Build enough breadth for users to extend the product themselves.** — Instead of matching a large vendor's depth, a product should cover a wide range of features, with extension points so users can add what is missing. Slack is the example: it became a place people run agents because its bot APIs are a usable shape. ([13:19](https://youtu.be/xUnRQ9vLXxo?t=799))
- **A good new idea should feel too ambitious.** — He says that if an idea does not feel stupid, it is not big enough, and he suggests challenging categories such as Slack, Salesforce and NPM. ([14:47](https://youtu.be/xUnRQ9vLXxo?t=887))

## Techniques
- **Markdown as a recurring program** — Write the job as a markdown prompt with steps: read the sources (e.g. list open PRs in four repos), assess status, prioritise, regenerate a static HTML page, upload it to S3 and return the URL. Run it with Claude or Codex on a daily cron. *When:* Recurring personal or team reporting where a static output is enough and a bespoke service would be overkill.
- **Prompt-driven sub-agent orchestration** — Tell a strong model to split a large task across sub-models and verify the results afterwards, instead of building a custom orchestrator first. *When:* Large, multi-step coding tasks on the newest models. The speaker gives no benchmark, so test it against your own harness before relying on it.
- **Breadth-first product with extension points** — Ship a thin but working version of many adjacent features and expose APIs or bots so users can build the missing parts. Aim for the right shape rather than full depth in each area. *When:* Designing a platform that must compete with a much larger incumbent that cannot match its depth.
- **Assumption audit** — For each inherited practice, ask whether it is right or just habit, for example committing env files, guilt-merging weak PRs, or keeping code you should delete. *When:* Starting a new project or reviewing team workflow with agents in the loop.

## Numbers
- Daily PR-triage markdown job runs on a 9 a.m. cron across four GitHub repos and has its output ready around 9:15 to 9:20. ([11:49](https://youtu.be/xUnRQ9vLXxo?t=709))
- Reddit scraper side project built in about 2 to 3 days. ([9:19](https://youtu.be/xUnRQ9vLXxo?t=559))
- Two of his three example builds were from 2021; the third is current. ([9:19](https://youtu.be/xUnRQ9vLXxo?t=559))
- A database platform feature can be built into a product in a day or two with enough prompting. This is an unmeasured estimate. ([13:19](https://youtu.be/xUnRQ9vLXxo?t=799))
- Most Jira tickets he closed at a previous job could be solved with Opus 4.5. Qualitative, no count given. ([2:35](https://youtu.be/xUnRQ9vLXxo?t=155))

## Hot takes
- Most startups could now be a markdown file.
- Natural language has no place in a terminal, and we keep using terminals because they are familiar.
- Environment files should be committable to git like any other file.
- If your idea does not feel stupid, it is not big enough.
- Building a database into your product in a day or two is now realistic, so you do not need to match RDS-level reliability to start.

## Tools mentioned
Claude Code, Codex, Git, GitHub, S3, Cron, Vercel, Slack bot APIs, Reddit, OBS, tmux, GNU Screen, Vim

## Relevance to our work
- **prosharness** (2/3): ProsHarness already has loops and schedules. The talk shows a concrete case of a markdown prompt run on cron to produce a recurring output, and claims that sub-agent orchestration can be prompted rather than built. → *Define one recurring job as a markdown file in ProsHarness (for example PR triage across repos writing static HTML), run it on a schedule, and compare its time and output quality with a hand-written script.*
- **agentos** (1/3): The breadth-versus-depth framing and the extension-point argument bear on how AgentOS spreads across its pillars. The talk offers no architecture or measured results. → *Write a short note listing which AgentOS pillars must be deep before adding breadth (for example Govrix Scout), using the breadth-versus-depth framing at 13:19.*
