# Stop Chatting With Spreadsheets — Francesco Galletta & Felippe Felisola Caso, Monzo

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `e9-br9hveRI` · [watch](https://youtu.be/e9-br9hveRI) · **date:** 2026-10-17 · **length:** 1:50:34 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Francesco Galletta, Felippe Felisola Caso · **orgs:** Monzo
- **topics:** agent-architecture, testing-verification, governance-compliance, data-engineering · **tags:** financial-analyst-agent, harness-design, deterministic-calculations, evidence-provenance, human-in-the-loop, branching-conversations, decision-tree-planning, llm-as-challenger, workshop

> Hands-on workshop on building a trustworthy financial-analysis harness around five principles (shared domain, deterministic calculations, evidence, accountability, verification), demoed on a wedding-budget planner.

## Summary
Two Monzo data people (Francesco Galletta and Felippe Felisola Caso) run a workshop arguing that for money-related analysis the bottleneck is trust, not generation speed. They walk attendees through a demo harness that plans a wedding budget: an interview-style planning phase builds a shared decision tree, and calculations are moved out of the model into tested code. The harness tags evidence as fact, assumption, or interpretation, gates only high-impact decisions for human sign-off, and uses a separate challenge agent whose objections feed back into the plan. They present the five principles as a sequence that builds on itself, and stress that the specific UI is one example, not a product. The talk is candid that the principles are the valuable part, and that the demo is deliberately overengineered and imperfect.

## Key ideas
- **Trust, not generation speed, is the bottleneck for money-related agent work.** — The speakers argue that producing an analysis is already fast; the real gap is whether you can trust and check the output. They frame trust as something to design in, rather than something you get from adding traces, evals, or planning on their own. ([5:34](https://youtu.be/e9-br9hveRI?t=334))
- **Calculations belong in code, not in the model's head.** — Arithmetic done in chat is inconsistent: the same question yields different answers across sessions, and a formula that looks right can still produce a wrong result. The fix is to have the harness write and run deterministic code (with unit tests and golden examples) for anything that must repeat. ([9:00](https://youtu.be/e9-br9hveRI?t=540))
- **Prompt-only skills are a weak substitute for a harness.** — Instructions like 'follow these steps, make no mistakes' rely on the model getting it right every time. The speakers say that even 99% reliability is not enough for money, and that the harness should mix non-determinism (planning, interpretation) with deterministic components it controls. ([39:19](https://youtu.be/e9-br9hveRI?t=2359))
- **Tag every input as fact, assumption, or interpretation.** — The model cannot tell hard data from estimates on its own, so the harness must label them. Bank statements count as facts, chat remarks are interpretations, and memory or inferred values are assumptions. A wrong silent assumption, like an unstated guest count, can invalidate the whole model. ([57:00](https://youtu.be/e9-br9hveRI?t=3420))
- **Gate only high-impact decisions; per-change approval and full line-by-line review both fail.** — Reviewing every edit creates toil and low-signal approvals, while going fully autonomous loses accountability. The design goal is a few high-signal gates placed where a decision materially changes the outcome, with code covered by tests rather than manual review. ([1:10:44](https://youtu.be/e9-br9hveRI?t=4244))
- **Verification needs an external reference point and a feedback loop.** — An LLM judge that only reviews output without changing the plan does not improve decisions. The speakers want a challenge agent whose objections can alter plan nodes, plus a dismiss option, and they note that domain experts catch errors by gut-checking against a different domain's numbers. ([1:31:23](https://youtu.be/e9-br9hveRI?t=5483))
- **Use branch-and-rejoin conversations instead of one linear chat.** — In a single linear chat, a stray question or a correction contaminates the whole analysis. The demo lets users branch off a node, then either merge the result back into the plan or dismiss it, so corrections can be made without losing the rest of the work. ([1:16:57](https://youtu.be/e9-br9hveRI?t=4617))
- **Metric and dimension definitions drift, so the harness must adapt.** — Data definitions and source data change over time. The speakers argue the plan should be a versioned spec that the harness can update, and that changed calculation code should be flagged, so users do not silently trust stale results. ([52:25](https://youtu.be/e9-br9hveRI?t=3145))
- **Only build a harness when the use case justifies it.** — For low-stakes or one-off tasks, plain agent use is fine. A harness pays off when the same analysis repeats, when many users depend on it, or when errors are costly, and building harnesses for everything becomes axe-sharpening that wastes time. ([1:34:12](https://youtu.be/e9-br9hveRI?t=5652))

## Techniques
- **Interview-style shared-domain planning with a decision tree** — The agent asks clarifying questions until the user accepts a plan. Each plan step becomes a node in a visual decision graph, and each node shows whether its input came from the user, the agent, or is still open. Users can edit a node's assumption and let the plan re-flow. *When:* At the start of any analysis where the user and model may use the same words to mean different things, such as personal finance or investment questions.
- **Calculation-as-code with tests and golden examples** — The harness generates scripts for calculations, aggregates, and scenarios. It runs unit tests and compares them against golden examples, and it versions the code so a changed function invalidates prior results until re-checked. *When:* For any arithmetic or aggregation that must give the same answer every time, such as budget totals, forecasts, or categorisation rollups.
- **Fact / assumption / interpretation labelling with provenance** — Every input or intermediate value is tagged by type and source, and the UI highlights the chain of evidence behind a figure. Users can hover a number to trace it back to its inputs and see downstream effects of changing one input. *When:* When outputs will be presented or acted on by other people, or when a silent assumption could be costly.
- **Branching challenge agent with merge or dismiss** — A separate agent reviews the plan and assumptions. Its suggestions can be accepted, which rejoins the trunk and changes the plan, or dismissed, which leaves the plan unchanged. Side questions can happen in a branch that does not pollute the main context. *When:* To add a second point of view without a pure LLM-as-judge loop that changes nothing, and to handle asides safely.
- **Tiered accountability gates** — Approval is required only for decisions that materially change outcomes, such as choosing a savings amount or a scenario. Trivial changes and tested code proceed automatically, and a gate sits at the task level rather than per edit. *When:* When you need human accountability but cannot afford to review every change.

## Numbers
- Wedding demo payments include one fixed payment of about $6,000, an unknown amount, and the remainder; the example includes about 150 per guest and 500 for flowers, plus about 5k from a parent. ([26:08](https://youtu.be/e9-br9hveRI?t=1568))
- The speaker's planning conversation took about 10 minutes of back-and-forth before the plan was accepted. ([30:11](https://youtu.be/e9-br9hveRI?t=1811))
- A test count of 95 is shown on screen after running the demo harness's tests. ([47:19](https://youtu.be/e9-br9hveRI?t=2839))
- The speakers say a 5% difference can be a deal breaker for a finance team, so tolerances must be set explicitly. ([1:29:02](https://youtu.be/e9-br9hveRI?t=5342))
- The speakers say a 1% error can still be a large amount of money in finance. ([1:48:57](https://youtu.be/e9-br9hveRI?t=6537))
- The speaker had the same planning conversation three times on a one-hour drive, because voice-based sessions kept losing earlier context. ([1:40:22](https://youtu.be/e9-br9hveRI?t=6022))

## Hot takes
- Writing 'make no mistakes' into skills or instructions is not a harness; for money, the non-determinism has to be fenced off with deterministic code.
- Agents face no real-world consequences; you do, so accountability has to be designed in.
- An LLM-as-judge that does not feed back into the plan is theatre; it will not improve decisions.
- Reviewing every change line by line is unrealistic, and approving every single edit is also a failure mode.
- Waiting for better models will not fix consistency, because agents keep inventing new code on the fly and each run can differ.
- Linear chat is the wrong shape for analysis; branching and rejoining is better.

## Tools mentioned
Claude Code, Codex, Looker Studio, Google Slides, Google Sheets

## Relevance to our work
- **prosharness** (2/3): Its plan -> critique -> debate loop is the same shape as the talk's challenge agent. The talk adds two things ProsHarness may lack: critique outputs that edit specific plan nodes, and a dismiss path that records why a challenge was rejected. → *Make the critique step produce node-level diffs against the plan, with accept (merge) and dismiss (recorded reason) as explicit outcomes, and log which plan nodes changed.*
- **agentos** (1/3): MemoryMesh already has provenance and conflict resolution. The fact / assumption / interpretation labelling from the talk is a cheap extension, but it is not a core change. → *Add an optional epistemic-type field (fact, assumption, interpretation) with source to MemoryMesh records, and check whether retrieval should prefer facts over assumptions.*
- **general** (1/3): The rule 'calculations go in tested code, not in chat' applies to any budget or aggregate work, including agent workflows used on cheap models. → *For any agent workflow that does arithmetic, move the calculation into a tested script and have the agent call it, with golden examples as regression checks.*
