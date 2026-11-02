# Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `jHMiYtjoJfA` · [watch](https://youtu.be/jHMiYtjoJfA) · **date:** 2026-08-18 · **length:** 19:46 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ben Hylak · **orgs:** Raindrop, Sentry, OpenAI, Vercel, Speak, Framer
- **topics:** evals, observability, product-ux · **tags:** floor-raising, offline-evals, online-evals, issue-detection, trace-classifiers, code-mode, anomaly-detection, vitest, workshop-tracing, raindrop, howtoeval

> Ben Hylak (Raindrop) argues teams should "raise the floor" by finding production agent failures, tracking when they started and how many users they hit, and using code-based classifiers over traces instead of clustering or big eval sets.

## Summary
Hylak, CTO of Raindrop, frames agent work as raising the floor (the worst things an agent can do, like deleting data or emailing a customer by mistake) rather than only pushing the ceiling. He says large static eval sets break whenever the model or harness changes, so evals should be small, local, code-like tests (he points to vitest-based evals and OpenAI's "macro evals"). For production issues, he gives three lessons: clusters of traces are not issues, the two facts to track per issue are when it started and how many users it hits, and agents are poor at detecting anomalies on their own, so you should pick deterministic signals (such as keyword frequency spikes) and have the agent investigate those. He recommends writing classifiers as code and running them in a sandbox over production traces. Experiments and A/B tests only make sense at large user counts, and the talk is mostly a short set of opinions from one vendor's experience, with a large share of time given to plugs for Raindrop, Workshop and howtoeval.com.

## Key ideas
- **Evals should look like tests, not prompt playgrounds** — The prompt is now the whole harness (code, tools, connections), so he says keep evals as code that runs locally, like unit or end-to-end tests. He notes few companies use managed cloud prompt tools anymore. ([11:24](https://youtu.be/jHMiYtjoJfA?t=684))
- **Big static eval sets break when the model or harness changes** — Tool-call evals written for one harness can fail badly after a switch (he jokes that 80% of evals break when moving to Claude Code CLI). He argues teams should not delay model upgrades for weeks to rebuild evals, so evals must be light enough to keep up. ([4:25](https://youtu.be/jHMiYtjoJfA?t=265))
- **Frame improvement as benchmark maxing vs floor raising** — The ceiling is the most impressive thing an agent can do. The floor is the worst thing it can do, such as recommending a competitor, deleting data, or sending a bad email. He says floor failures break user trust more than capability gaps. ([10:00](https://youtu.be/jHMiYtjoJfA?t=600))
- **Track each production issue by onset and by how many users it affects** — For each issue he wants to know when it started (new issues get attention, and a recent start prompts a check of what changed, such as model or downstream changes) and what share of users it touches. Three users and 100,000 users call for different responses. ([12:46](https://youtu.be/jHMiYtjoJfA?t=766))
- **Clusters are not issues** — Clustering all traces is fine for one-off analysis but does not scale. Temporal clusters are hard to track over time, the boundary between issues varies by company, and one cluster (like price issues) can hide different root causes. ([15:14](https://youtu.be/jHMiYtjoJfA?t=914))
- **Use code classifiers on traces, run in a sandbox at production scale** — Write classifiers as code (the code-mode idea from MCP, applied to traces), run them in a sandbox over production traces. He says this scales where clustering does not. ([17:51](https://youtu.be/jHMiYtjoJfA?t=1071))
- **Do not ask agents to find anomalies; ask them to investigate known ones** — He says agents are weak at open-ended anomaly detection. Start with deterministic signals such as keyword frequency spikes, then let the agent investigate the tractable signal it was given. ([17:51](https://youtu.be/jHMiYtjoJfA?t=1071))

## Techniques
- **Evals as local code tests** — Write agent evals with a test runner (he cites vitest with eval sugar and OpenAI's macro evals). Keep them in the repo and run them locally. *When:* When the agent is code plus tools plus harness, and prompt playgrounds no longer describe it.
- **Per-issue onset and affected-user tracking** — For every production issue, record first-seen time and the number of distinct affected users, so a new spike can be separated from a long-standing one. *When:* When triaging many weird agent behaviours and deciding which to fix first.
- **Code-based trace classifiers** — Express each failure pattern as a classifier function, run it over production traces in a sandbox, and count hits over time. *When:* When clustering is too unstable to track issues across time, and you have enough trace volume to justify the setup.
- **Deterministic signal first, agent investigates second** — Compute cheap measurable signals (keyword frequency, spikes) and feed the flagged items to an agent as a concrete investigation task, not an open anomaly search. *When:* When you want agent help with root-cause work without relying on the agent to spot anomalies itself.
- **Scale-dependent experimentation** — Run experiments or A/B tests on a small sample of a large free tier. Avoid them with very few users, where he says they are not worth it. *When:* When you have millions of messages a day. With five or ten users, use direct investigation instead.

## Numbers
- Evals built from a 1,000-example dataset are the advice he says almost nobody follows (anecdotal, not measured). ([3:25](https://youtu.be/jHMiYtjoJfA?t=205))
- Switching to Claude Code CLI broke about 80% of one team's tool-call evals (his anecdote, not a benchmark). ([4:25](https://youtu.be/jHMiYtjoJfA?t=265))
- Customers range from ones with millions of users to ones with about five users. Experiments need very large volume (he gives 10, 20, 100 million messages a day as the range where they pay off). ([13:57](https://youtu.be/jHMiYtjoJfA?t=837))
- Example comparison for issue prioritisation: an issue hitting 3 users vs 100,000 users needs very different responses. ([13:57](https://youtu.be/jHMiYtjoJfA?t=837))
- Workshop is used by thousands of people (self-reported by the speaker's company). ([5:53](https://youtu.be/jHMiYtjoJfA?t=353))

## Hot takes
- Most eval guides for agents are still stuck in the chatbot era, and the 1,000-example eval set is something almost nobody actually builds.
- Investing months in an eval set slows you down, and you should not delay a model upgrade for two weeks to update evals.
- Agents are very bad at anomaly detection, so do not ask the agent to find anomalies.
- Clustering traces is useful for one-off analysis but is the wrong tool for tracking issues over time.
- Floor failures (trust-breaking mistakes) matter more to users than ceiling capability.

## Tools mentioned
Raindrop, Workshop (open-source tracing tool), vitest (vitest evals), howtoeval.com, Sentry (mentioned as a model for issue detection)

## Relevance to our work
- **agentos** (2/3): AgentOS L4 observability and SkillForge mine agent telemetry. The talk's per-issue onset and affected-user tracking, plus code classifiers over traces, map onto that pipeline. → *Add first-seen and distinct-user-count fields to trace-derived issue records in the telemetry layer, and test one deterministic keyword-spike signal before any agent-driven investigation.*
- **prosharness** (1/3): The eval-breaks-on-harness-switch point is relevant to a harness that wraps the Claude Code CLI, but the talk gives no concrete method for it. → *Check whether ProsHarness's own tests drive the real Claude Code CLI path, or only the API layer, before adding more eval cases.*
- **general** (1/3): Evals-as-code and floor-versus-ceiling framing are useful vocabulary for the recurring evals interest, with no new method. → *Skim howtoeval.com for its checklist, if it is cited elsewhere in the knowledge base.*
