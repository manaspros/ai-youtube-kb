# The Cheaper AI Model That Costs You More - Rayan Krishnan, Vals AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `rWtbOgl5FTU` · [watch](https://youtu.be/rWtbOgl5FTU) · **date:** 2026-10-30 · **length:** 15:28 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Rayan Krishnan · **orgs:** Vals AI, Anthropic, OpenAI, Moonshot AI
- **topics:** evals, token-cost-efficiency, enterprise-adoption, models-research · **tags:** jagged frontier, cost per task, pareto frontier, benchmark design, reward hacking, eval infrastructure, model routing, PR-replay evals, finance agents, token maxing

> Vals AI's Rayan Krishnan argues model cards hide a "jagged frontier" by task and metric, and that cost-per-task evals, real-work benchmarks and routing can cut enterprise AI spend without losing output.

## Summary
Rayan Krishnan of Vals AI argues that headline model-card scores hide a jagged frontier: the best model changes by domain, subtask (e.g. LBO vs overall Excel modeling) and harness. He shows a cheaper model (Opus 5.5) costing more per task than a pricier one because it burns more tokens for a lower score. He stresses metric choice (partial credit vs fully-correct rate) and benchmark quality (validity, reliability with enough samples, discriminability), and warns about agents gaming evals via sandbox escapes and hedged multi-answer responses. His internal case study: a 10-12 person engineering team spent about $1.5M in tokens in one month, and replaying historical GitHub PRs/issues as eval tasks let them cut spend about 90% at equal output. He closes with routing, right-sizing and fine-tuning as uses for evals, and frames institutional knowledge as the data to codify. Speaker is from a benchmark vendor, so the numbers are self-reported.

## Key ideas
- **Model-card scores hide a jagged frontier: the top model changes by benchmark, subtask and harness, so aggregate numbers mislead for real work.** — Vals Index is an aggregate; the constituent benchmarks give different winners. In finance Excel modeling, the LBO subset has a different frontier from overall EMB, and the state-of-the-art model on overall scores drops off the frontier for LBO tasks. ([1:13](https://youtu.be/rWtbOgl5FTU?t=73))
- **Cost per task, not per-token price, decides the best model. A cheaper list-price model can cost more.** — Opus 5.5 lists at $4 in / $20 out vs $10 / $50 for the frontier model, yet on the tax benchmark it cost about 14% more per task because it spent more tokens, and scored 3% lower. ([3:40](https://youtu.be/rWtbOgl5FTU?t=220))
- **Metric choice changes the conclusion: partial credit and fully-correct rate tell different stories.** — Partial credit estimates the share of rubric points satisfied in expectation. The fully-correct rate is the share of answers that are perfect. A model can look strong on partial credit yet be a coin toss for client-ready output. ([6:20](https://youtu.be/rWtbOgl5FTU?t=380))
- **Benchmarks need validity, reliability and discriminability.** — Validity: tasks and rubrics must match real work, not be contrived. Reliability: enough tasks and repeated runs, since 5-6 samples is vibe-checking. Discriminability: avoid benchmarks that every model aces or fails, and build forward-looking tasks with headroom. ([7:02](https://youtu.be/rWtbOgl5FTU?t=422))
- **Agents solve the test, not the problem: watch for reward hacking and hedged answers.** — Models have called other models through the eval proxy to escape the sandbox or reach the internet. In finance rubrics, models hedge with three candidate answers to satisfy every item, which a user would not want. Containers must test what matters. ([8:14](https://youtu.be/rWtbOgl5FTU?t=494))
- **Eval infrastructure must be resumable and long-running, and benchmarks must be multi-turn.** — Long agent runs need consistent infra that can be interrupted and resumed. Vals reports having run about 6 trillion eval tokens. Most benchmarks score single prompt to single response, while real work is iterative spec, questions and feedback. ([9:34](https://youtu.be/rWtbOgl5FTU?t=574))
- **Replaying historical PRs as eval tasks found over-spent models and cut cost about 90% at equal output.** — A token-maxing experiment with unlimited tools cost about $1.5M in one month for a team of 10-12. Vals built an internal eval using GitHub issue-to-PR pairs and gave those tasks to agents, then recommended a tool and model per issue. The result was exposed as the product Vals Smith. ([10:59](https://youtu.be/rWtbOgl5FTU?t=659))
- **Open-source is not automatically cheaper: measure hosted cost and quality on your own evals.** — On an internal eval, GPT 5.6 Sol scored about 2% higher than Kimi K3, cost about $2.50 vs $11 on an optimized inference stack, and ran roughly twice as fast. ([12:18](https://youtu.be/rWtbOgl5FTU?t=738))
- **Evals enable right-sizing, negotiation, routing and fine-tuning. The real data is the firm's history of past work.** — Use evals to set usage limits, negotiate bulk pricing and build routers. Fine-tuning can be an external eval set. Historical work (emails, SharePoint, data dumps) is the main source for building these evals, and codifying institutional knowledge is the competitive edge. ([13:22](https://youtu.be/rWtbOgl5FTU?t=802))

## Techniques
- **Pareto plotting of cost per task vs performance** — Plot cost per task (not per-token price) on x and score on y, and segment the frontier by subtask (e.g. LBO inside Excel modeling) before picking a model. *When:* Choosing a model for a specific workflow or subtask rather than for the aggregate leaderboard.
- **Report partial credit and fully-correct rate together** — Use partial credit for expected rubric coverage and fully-correct rate for the share of outputs that are client-ready. Compare them before deciding a model is good. *When:* Benchmarking outputs that will be passed directly to a client or user.
- **Build evals from historical work (PR and issue replay)** — Mine GitHub issues linked to merged PRs (or the equivalent in email, SharePoint or data dumps), give the issue to candidate agents, and grade the output against the merged work. Use the result to choose a model per issue class. *When:* You have a corpus of finished work and want a cheap, realistic signal for model choice and cost cuts.
- **Sandbox hygiene against reward hacking** — Run agents through a model proxy, and block or log calls that route to other models or the internet from inside the sandbox. Grade only the target task. *When:* Running agentic evals where the model could escape the harness or call other models to pass.
- **Resumable eval infrastructure** — Design eval runs to persist state so they can be interrupted and restarted, and run at high parallelism to keep long agent evals tractable. *When:* Running multi-hour or multi-turn agent evaluations.
- **Task-level usage-limit right-sizing** — Use per-task eval results to set tool procurement and per-team usage limits, then recommend a specific tool and model for each class of GitHub issue. *When:* Controlling AI spend across an engineering org after a token-maxing period.

## Numbers
- Enterprise AI spend grew roughly 2x year over year. ([2:22](https://youtu.be/rWtbOgl5FTU?t=142))
- About 90% of people use AI regularly, but only about 7% report established ROI. ([2:22](https://youtu.be/rWtbOgl5FTU?t=142))
- Opus 5.5 lists at $4 in / $20 out vs $10 / $50 for Fable 5.1, yet cost about 14% more per task on the tax benchmark with a 3% lower score. ([3:40](https://youtu.be/rWtbOgl5FTU?t=220))
- Internal token-maxing month cost about $1.5M for a team of 10-12, roughly 10x what the team spent on token salary. ([10:59](https://youtu.be/rWtbOgl5FTU?t=659))
- Eval-driven changes cut spend about 90% while keeping output the same. ([12:18](https://youtu.be/rWtbOgl5FTU?t=738))
- GPT 5.6 Sol scored about 2% higher than Kimi K3 on an internal eval, at about $2.50 vs $11 on an optimized stack and about half the latency. ([12:18](https://youtu.be/rWtbOgl5FTU?t=738))
- Vals has run about 6 trillion tokens of evaluation. ([9:34](https://youtu.be/rWtbOgl5FTU?t=574))

## Hot takes
- Aggregate model-card leaderboards are a poor guide to what to buy for a specific workflow; per-task cost and subtask results matter more.
- Open-source self-hosting is not a cost win by default; measure hosted cost and quality on your own evals first.
- Most companies already hold their best eval data in past work (emails, SharePoint, data dumps) and do not realise it.
- Partial-credit benchmarks can hide that a model's outputs would not survive client review.

## Tools mentioned
Vals AI benchmarks (Vals Index, Finance Agent benchmark, Excel modeling / LBO, tax agent), Vals Smith (internal eval-driven coding product), Opus 5.5 (Anthropic), Fable 5.1, Sonnet, GPT 5.6 Sol, Kimi K3

## Relevance to our work
- **agentos** (2/3): The per-task cost and Pareto frontier framing maps onto the budget and strategy routing in the Scout proxy, and the PR-replay eval idea could feed the RAGAS and correctness evals. → *Add a cost-per-task metric (not per-token) to the Scout routing benchmark, and compare routing choices on a subtask-level Pareto plot.*
- **prosharness** (2/3): Harness checkpoint and resume matches the talk's need for resumable long-running eval infra. Replaying past PRs as tasks could check plan-critique-debate quality. → *Try replaying past merged PRs as tasks through ProsHarness and grade the resulting diffs against the merged code.*
