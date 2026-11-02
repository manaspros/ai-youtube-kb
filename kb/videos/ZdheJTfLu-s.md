# Shipping complex AI applications — Braintrust & Trainline

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ZdheJTfLu-s` · [watch](https://youtu.be/ZdheJTfLu-s) · **date:** 2026-05-18 · **length:** 1:38:34 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Duran (Braintrust), Osama (Trainline, senior AI/ML engineer), Mayank (Trainline, senior AI engineer) · **orgs:** Braintrust, Trainline, OpenAI
- **topics:** evals, observability, agent-architecture · **tags:** braintrust, tracing, golden-set, llm-as-judge, online-scoring, managed-prompts, multi-stage-agent, model-switching, failure-driven-iteration, trainline, support-triage, hands-on

> Hands-on Braintrust and Trainline workshop on taking a multi-stage LLM support-triage agent from one prompt to a traced, evaluated, managed and failure-driven production loop.

## Summary
Duran (Braintrust) and two Trainline engineers, Osama and Mayank, run a 1h38m hands-on workshop at AI Engineer Europe 2026 in London. They build a fictional support-triage agent in five stages: deterministic context collection, triage, policy review, reply writing, and packaging with an escalation tool call. The talk argues that the gap between demo and production is operational rather than a model-quality problem, and that teams need tracing, golden-set evals, online scoring and a failure-to-fix loop. Trainline describes its real travel assistant, which uses LLM evals to justify switching to cheaper models and to let product staff self-serve on logs. Most of the content is a vendor walkthrough, but the Trainline examples and the eval design advice are concrete and practitioner-grade.

## Key ideas
- **The production gap is operational, not a model-quality problem** — The speaker says models are smart enough; what's missing is operational rigor. Logs say what happened, but tracing is needed to see behaviour. Patching a prompt after each failure is a loop with no system behind it. ([6:47](https://youtu.be/ZdheJTfLu-s?t=407))
- **Break one big prompt into explicit stages** — A single prompt works in a demo but is hard to debug. Split the job into stages, the way a monolith is split into services, so a failure can be located on the stack and fixed where it happens. Target is not 100% coverage but closing the gaps that matter. ([8:01](https://youtu.be/ZdheJTfLu-s?t=481))
- **The flywheel: eval set, failure modes, remediate, ship, monitor, repeat** — Start with a small eval set even for a new app. Pull in production traces where they exist, find failure modes, fix them, ship, then monitor and loop. Production edge cases are the source of the best test cases. ([12:09](https://youtu.be/ZdheJTfLu-s?t=729))
- **Cost pressure drives model switching, which needs evals first** — Trainline says its OpenAI and Anthropic bills forced it to keep switching models. Before any switch, they run offline evals on the cheaper model, then confirm the effect online. The talk says this was not possible before they had scores. ([20:54](https://youtu.be/ZdheJTfLu-s?t=1254))
- **Structure traces as one parent span per interaction with child spans per call** — Flat per-call logs are not enough. Wrap each user interaction in a parent span and nest the LLM and tool calls under it. Record latency, time to first token, tokens, cost, inputs, outputs and filterable metadata. The write path is non-blocking. ([46:40](https://youtu.be/ZdheJTfLu-s?t=2800))
- **Two scorer types: deterministic checks on everything, LLM-as-judge for nuance** — Deterministic scorers (schema, category, escalation reason) are cheap and can run on all traffic. Where nuance such as brand tone or customer satisfaction cannot be written as code, use an LLM judge with a rubric. The stated rule is to use an LLM judge wherever a deterministic check is impossible. ([58:31](https://youtu.be/ZdheJTfLu-s?t=3511))
- **Sample expensive LLM judges down after a baseline** — Start LLM-judge online scoring at a high sampling rate, around 100%, to build a baseline. Once outputs are trusted, drop to 5 to 10% to control cost. Deterministic scores can stay at full rate. Automations can target a single span or the whole trace. ([1:14:31](https://youtu.be/ZdheJTfLu-s?t=4471))
- **Remediate a failure by replaying it, then checking regressions across the full set** — Example: a 'not urgent' ticket where the CFO needs invoices before a board meeting. Turn the production failure into a targeted case, tighten the prompt, replay it, then run the full suite to check for regressions. Compare experiments with a diff. ([1:18:30](https://youtu.be/ZdheJTfLu-s?t=4710))
- **Managed prompts and parameters let non-engineers change configs without code** — Prompts and scorers are pushed to a managed store under stable slugs and pulled by code. Product or SME users can change a model or prompt in the UI and leave a comment, and the code runs the new version. The speaker says this does not replace version control. ([1:08:56](https://youtu.be/ZdheJTfLu-s?t=4136))

## Techniques
- **Staged agent pipeline with a deterministic front end** — Collect context in plain code first, then run narrow LLM stages in sequence (triage, policy review, reply draft, package), with an escalation tool call at the end. Each stage has its own prompt and can be traced and tested separately. *When:* Multi-step workflows such as support triage, where a failure must be localized to one stage and where some steps can be deterministic.
- **Nested tracing per user interaction** — Create one parent span per interaction or conversation. Nest each LLM and tool call as a child span. Attach latency, TTFT, token counts, cost and filterable metadata. Read the timeline view to find slow steps. *When:* Any multi-call agent. Use it to debug production behaviour and to find which step is slow or expensive.
- **Golden set from categorized edge cases** — Write about 10 categorized inputs with expected outputs and metadata, stored as a dataset. Run them as an experiment against the app, then grow the set with production failures. *When:* A new app with no production data yet (cold start), or to guard known failure modes.
- **Two-tier scoring** — Deterministic scorers run on every trace (cheap). LLM-as-judge scorers use a rubric for nuanced qualities, sampled at 5 to 10% once a baseline is set. *When:* Online monitoring where LLM judges are costly, and offline evals where nuance must be checked.
- **Evaluate before swapping models** — Run the candidate cheaper model offline on the eval set against the current baseline, then confirm the same pattern online before shipping. *When:* Cost-driven model changes where quality must not drop.
- **Failure-to-fix loop** — Pick a production failure, save it as a dataset case, replay it in the playground or as a scoped experiment, edit the prompt, then run the whole suite and diff against the previous experiment. *When:* After any production incident or any prompt change, to check for regressions.
- **Prompts and scorers as managed, slugged assets** — Push prompts and parameters to a managed store with stable slugs. Code references the slug. A sync command keeps the local code and the managed version aligned. Use it so SMEs can edit configs without a code change. *When:* Cross-functional teams, including regulated industries that need an audit trail of who changed what.

## Numbers
- Braintrust raised $80M at an $800M valuation, about 3 years old, Series B (company claim, as stated by the speaker) ([9:23](https://youtu.be/ZdheJTfLu-s?t=563))
- Trainline sells about 6.3 billion train tickets across the EU, with 27 million active users ([13:16](https://youtu.be/ZdheJTfLu-s?t=796))
- Eval workshop golden set has 10 categorized inputs; the failure-mode regression set has 5 cases ([59:58](https://youtu.be/ZdheJTfLu-s?t=3598))
- Time to first token is a key latency metric customers track ([46:40](https://youtu.be/ZdheJTfLu-s?t=2800))
- Online LLM-judge sampling: start near 100%, taper to 5 to 10% once outputs are trusted ([1:14:31](https://youtu.be/ZdheJTfLu-s?t=4471))
- Some Braintrust customers push tens of millions of traces in a short window; writes are near-instant and reads follow shortly after ([53:32](https://youtu.be/ZdheJTfLu-s?t=3212))

## Hot takes
- 2 plus 2 equals 10: LLM systems are not like deterministic software, so operational rigor has to be rebuilt.
- If you cannot write a check deterministically, use an LLM as judge where possible.
- The speaker says the managed prompt store is not a replacement for version control, and that teams still need a centralized source of truth.
- Tracing is table stakes: a production app with no tracing should go back to the drawing board.

## Tools mentioned
Braintrust, OpenAI SDK, OpenAI mini model (speaker says 'mini'), TypeScript, pnpm, make, Node 22, Cursor / Codex (suggested for setup)

## Relevance to our work
- **agentos** (2/3): The talk's nested per-interaction tracing with TTFT, tokens, cost and metadata maps to AgentOS L4 observability. The eval and failure-loop advice maps to L2A RAGAS evals. → *In AgentOS L4, make each user conversation one parent OTel span with the LLM and tool calls as children. Record TTFT and per-call cost as span attributes. Then run deterministic checks on all traffic and LLM-judge scoring on a 5 to 10% sample.*
- **prosharness** (2/3): The failure-to-fix loop (take a production failure, replay it as a case, tighten the prompt, rerun the full suite, diff) fits how ProsHarness runs plan, critique and debate on long jobs, and checkpoint/resume gives a natural replay point. → *Save each failed ProsHarness run as a replayable case with its checkpoint state. Run that case plus the existing set after each prompt or skill change, and diff the results before merging.*
- **general** (2/3): The two-tier scoring pattern (cheap deterministic checks on every run, a rubric-based LLM judge on a sample), plus evaluating a cheaper model offline and online before switching, is directly relevant to the cheap-model (Haiku) pipelines and entity-resolution work. → *For the Haiku pipelines, write deterministic checks for format and schema on every output and an LLM-judge rubric on a 5 to 10% sample. Run offline evals before any model downgrade.*
