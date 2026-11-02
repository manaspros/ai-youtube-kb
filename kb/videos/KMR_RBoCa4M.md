# SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `KMR_RBoCa4M` · [watch](https://youtu.be/KMR_RBoCa4M) · **date:** 2026-08-18 · **length:** 16:29 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Aman Gupta, Shreya Rajpal · **orgs:** Nubank, Snowglobe
- **topics:** evals, enterprise-adoption, data-engineering · **tags:** simulation, synthetic-users, agent-evals, a-b-testing, customer-support-agents, llm-as-judge, sim-to-real-gap, prompt-optimization, eval-data, model-swap

> Nubank and Snowglobe claim simulated personas with mocked tools produce agent eval data on demand, cutting release cycles from weeks to hours, provided the sim-to-real gap is measured.

## Summary
Aman Gupta (principal ML engineer at Nubank) and Shreya Rajpal (CEO of Snowglobe) argue that agent evals are bottlenecked by eval data rather than metrics. Multi-turn agent trajectories with stateful tool calls are expensive to author by hand, and production traces test live customers and block parallel experiments. They propose generating eval data in simulation: wrap the agent, mock its tools, drive it with personas and use cases, and run LLM judges per turn on thousands of conversations. Nubank reports that this shortened its loop from weeks to hours or minutes for changes to harness, prompts or tools. They say simulated and production eval scores correlate highly and that 80% of domain-expert labels found the sims usable. Simulation also caught a regression before launch, let teams screen variants so fewer A/B tests run, and let them sweep open-source models through the same harness. The talk's three takeaways are to generate eval data in simulation, close the sim-to-real gap with offline, online and human metrics, and treat data plus metrics as the core of any self-improving agent loop. The speakers are promoting Snowglobe, and the 20x headline has no stated baseline.

## Key ideas
- **Eval data, not metrics, is the real bottleneck for agents** — Metrics can be built with LLM judges aligned to human labels. Data is harder: each multi-turn trajectory with stateful tool calls is costly to generate and annotate, and scaling a sample set is harder still. ([3:33](https://youtu.be/KMR_RBoCa4M?t=213))
- **Both usual sources of eval data hurt** — Hand-authoring trajectories with consistent state is slow. Production traces are cheap but test on live users, which makes many parallel experiments hard. ([4:50](https://youtu.be/KMR_RBoCa4M?t=290))
- **Simulation compresses the release loop** — The speakers claim a change plus offline eval that took weeks, or days with hand-curated data, can take hours. A/B tests that took forever for sparse, noisy feedback can give a direction in hours. ([6:13](https://youtu.be/KMR_RBoCa4M?t=373))
- **How a simulation works** — The SDK wraps the agent with no code changes. You identify which tools to mock, then supply personas and use cases. The output is thousands of multi-turn conversations with mocked tools, and per-turn judges feed the eval pipeline on demand. ([7:24](https://youtu.be/KMR_RBoCa4M?t=444))
- **Synthetic users need persistent grounding state** — Each persona has a profile, tone and voice, plus grounding data such as an address, card and account. The same data is reused across the run, so the agent's tool lookups can be verified. ([9:28](https://youtu.be/KMR_RBoCa4M?t=568))
- **A closed loop of ship, observe, eval, simulate, optimize** — Robust evals come from automated prompt optimization (captioned 'JEPA' in the transcript, likely GEPA). Simulation and real data are both piped through the evals, the harness is optimized on that signal, and the change ships once verified. ([10:50](https://youtu.be/KMR_RBoCa4M?t=650))
- **Sim-to-real gap has to be measured** — Sim and production eval scores show a 'pretty high' correlation, with no figure given. Domain experts confirmed sim data was usable in 80% of labels. The speakers want offline, online and human-review metrics to decide when to trust sims. ([10:50](https://youtu.be/KMR_RBoCa4M?t=650))
- **Sims catch regressions and pre-screen A/B tests** — One regression was caught before production. Teams run many variants through sim and launch only the best as an A/B test, which skips the weaker ones. Self-service rate did not drop, and one case improved by 4%. ([12:16](https://youtu.be/KMR_RBoCa4M?t=736))
- **Sims as a model-swap harness** — Open-source models are run through the same agent harness, eval and sim setup, and the best ones are compared. The speakers say this saved multiple weeks, and A/B tests were running on the result. ([13:40](https://youtu.be/KMR_RBoCa4M?t=820))

## Techniques
- **Simulated-user eval set generation** — Wrap the agent with an SDK and no code changes. Mock the tools it calls. Define personas and use cases. Run thousands of multi-turn conversations, then score each turn with LLM judges. *When:* When you need many agent eval trajectories quickly and production data is slow, sparse or risky to test on.
- **Persona-consistent grounding state** — Generate one fixed profile per persona (identity, address, card, account data). Reuse it across the whole run and in the mocked tool responses, so the agent's lookups can be checked. *When:* When the agent calls stateful tools and the eval must check that outputs match the user's real state.
- **Sim pre-screening before A/B tests** — Run many candidate harness, prompt or tool variants through sim evals. Launch a live A/B test only for the top candidate. *When:* When A/B tests are expensive or slow to reach significance, and you run many variants per quarter.
- **Sim-to-real calibration** — Compare sim eval scores with production scores, and sample domain-expert review to check that sim conversations are usable. Track offline, online and human metrics together. *When:* Before trusting sim results for ship decisions, and when adding a new agent.
- **Same-harness model sweep** — Swap candidate models, including open-source ones, into an unchanged harness, eval and sim setup. Compare them on the same metrics. *When:* When a new model is released and you want to know whether it can replace a frontier model for one workflow.

## Numbers
- Nubank serves 135 million customers in Brazil, Mexico and Colombia, with a US launch coming; quarterly revenue passed $5B in Q1 2026 ([0:08](https://youtu.be/KMR_RBoCa4M?t=8))
- Headline claim: agents ship about 20x faster when eval data comes from simulation (no baseline stated) ([1:08](https://youtu.be/KMR_RBoCa4M?t=68))
- Five AI agents in production were shown with TNPS improving over months of work ([1:08](https://youtu.be/KMR_RBoCa4M?t=68))
- Hand-curated offline evals take a few days, and harness changes take a few hours ([4:50](https://youtu.be/KMR_RBoCa4M?t=290))
- Simulation shortens the change-and-eval cycle from weeks to under a day, sometimes hours or minutes ([6:13](https://youtu.be/KMR_RBoCa4M?t=373))
- Each simulation run produces thousands of multi-turn conversations ([7:24](https://youtu.be/KMR_RBoCa4M?t=444))
- Sim vs production eval correlation described as 'pretty high' (no figure given) ([10:50](https://youtu.be/KMR_RBoCa4M?t=650))
- 80% of domain-expert labels confirmed simulated data is usable ([10:50](https://youtu.be/KMR_RBoCa4M?t=650))
- One agent's TNPS doubled (2x) with simulation, robust evals and principled optimization ([12:16](https://youtu.be/KMR_RBoCa4M?t=736))
- Self-service rate improved by 4% in one particular case, and was not sacrificed overall ([12:16](https://youtu.be/KMR_RBoCa4M?t=736))
- Open-source model testing via sim saved multiple weeks of effort ([13:40](https://youtu.be/KMR_RBoCa4M?t=820))

## Hot takes
- If you generate eval data in simulation instead of waiting on production data, you can ship agents 20x faster.
- Production traces are almost free, but testing on live users makes parallel experiments very hard.
- In an enterprise setting, building an agent comes down to two things: data and metrics.
- You can short-circuit most A/B tests by running variants through sim first and launching only the best one.

## Tools mentioned
Snowglobe SDK, LLM-as-judge, Automated prompt optimization (captioned 'JEPA', likely GEPA)

## Relevance to our work
- **general** (2/3): Agent evals and simulated data are a recurring interest. The talk gives a concrete loop: personas, mocked tools, per-turn judges, and a check of sim against real scores. The grounding-state idea could also apply to ER test sets. → *Build one sim-driven eval set for a single agent workflow, with grounded personas and per-turn judges, and check its correlation with real outcomes before using it for decisions.*
- **agentos** (1/3): AgentOS already sits as an OpenAI-compatible proxy, which is the no-code-change wrap the speakers describe. Persona-driven sim evals could regression-test agent changes behind that proxy, but nothing here is specific to our architecture. → *Try a small persona-driven sim suite pointed at the AgentOS proxy, with a few mocked tools, to see whether it catches a regression that RAGAS evals miss.*
- **prosharness** (1/3): ProsHarness changes its plan, critique and debate prompts and loops. Sim-based pre-screening could compare those variants before real runs, but the talk does not cover checkpoint/resume or approvals. → *Build a few scripted persona runs of the ProsHarness plan step to compare two prompt variants before a live run.*
