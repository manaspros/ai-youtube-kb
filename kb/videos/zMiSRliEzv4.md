# Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `zMiSRliEzv4` · [watch](https://youtu.be/zMiSRliEzv4) · **date:** 2026-06-18 · **length:** 15:39 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Joshua Snyder · **orgs:** PostHog, Modal, Anthropic
- **topics:** software-factory, agent-architecture, evals, observability · **tags:** self-driving product, signals, report grouping, query-based embedding matching, actionability gate, sandbox snapshot rehydrate, Claude Agent SDK, Modal, MCP, PR automation, distillation of agent behavior, feature flags

> PostHog's Joshua Snyder describes a pipeline that turns product signals (errors, replays, Slack, experiments) into grouped reports, runs a Claude Agent SDK research agent in sandboxes, and opens PRs that are iterated until green.

## Summary
Joshua Snyder from PostHog describes a self-driving product pipeline that replaces dashboard-driven debugging with background agents that open pull requests. Incoming signals pass an LLM safety classifier, are normalized into one structure with a weight, and are embedded. Related signals are grouped into reports, and a report is promoted to a research agent once its weight crosses a threshold. The research agent runs the Claude Agent SDK in a Modal sandbox with PostHog's MCP server, the codebase, and external MCPs such as Linear and Notion, then outputs a summary, a priority, and a git-blame-based reviewer. An actionability gate sends each report to one of three places: back to the pool for more evidence, a morning inbox for product decisions, or straight to a fix. Fix runs snapshot the sandbox after pushing a PR and rehydrate it when CI fails or a comment arrives. The speaker stresses evals on production-like data, the need to gate vague problems, and the idea that repeated agent runs can be distilled into cheaper one-shot calls. The pipeline is in alpha.

## Key ideas
- **Product signals should become PRs, not dashboards.** — The speaker contrasts today's loop (signal changes a dashboard, a human notices hours or days later, files an issue, writes a PR) with a background agent that investigates each signal and opens a PR for review or a feature-flagged ship. He says the current loop takes hours to days. ([2:06](https://youtu.be/zMiSRliEzv4?t=126))
- **Ingest, classify, normalize, embed, then group signals into weighted reports.** — Public-facing sources pass an LLM classifier that drops hostile signals. Each signal is normalized to a shared structure (source product, type, content, weight) and embedded. Signals are then grouped into reports, and a report is promoted to research when its weight crosses a threshold. ([3:05](https://youtu.be/zMiSRliEzv4?t=185))
- **Embedding raw signals groups by format, not meaning.** — Off-the-shelf embeddings put all errors together and all Slack messages together, even when an error and a Slack complaint describe the same checkout bug. The fix was to have an LLM generate queries from each signal and match those queries in embedding space. The speaker says this worked much better. ([5:57](https://youtu.be/zMiSRliEzv4?t=357))
- **The research agent gets extra context through MCP and a sandbox.** — The Claude Agent SDK runs in a Modal sandbox. It can pull more data through PostHog's own MCP server (for example logs linked to a replay), read the code, and use external MCPs such as Linear and Notion. Its output is a problem summary, a priority, and a reviewer chosen with git blame. ([7:20](https://youtu.be/zMiSRliEzv4?t=440))
- **Gate reports three ways: not actionable, needs a human, or fix now.** — Reports without enough evidence go back to the pool. Product-level decisions go to a morning inbox. Actionable reports get a fix. Error-tracking signals are the easiest to act on. Slack and session replay produce generic problems that are harder to turn into a single fix. ([8:47](https://youtu.be/zMiSRliEzv4?t=527))
- **Snapshot the sandbox and rehydrate it to keep a PR green.** — The fix agent clones the repo, pushes a PR, and snapshots the sandbox. When CI fails or a review comment arrives, the snapshot is restored and the run continues until the PR is green. The goal is that the developer wakes up to green PRs. ([10:18](https://youtu.be/zMiSRliEzv4?t=618))
- **Expensive agent runs can be distilled once their behavior repeats.** — Early on, the team avoided agents to save cost, which the speaker calls a mistake. After about a hundred runs on the same kind of problem, similar solutions appeared. Those steps could then be replaced by a one-shot LLM call or a trained smaller model. ([13:12](https://youtu.be/zMiSRliEzv4?t=792))

## Techniques
- **Generate queries from a signal, then embed the queries** — Ask an LLM what a heterogeneous signal (stack trace, Slack message, replay) is about, produce several queries, and match those queries in embedding space instead of matching the raw signals. *When:* Clustering or linking records from sources with different structures, where raw embeddings group by format instead of meaning.
- **Safety classifier at the ingestion edge** — Run an LLM classifier on every signal from public-facing sources before anything else, and drop any signal that looks like an attack. *When:* Inputs can be written by anyone on the internet and will later reach an agent with tools.
- **Weighted report promotion with a threshold** — Give each grouped report a running weight from its member signals. Promote it to an expensive research step only when the weight crosses a set threshold. *When:* Many cheap signals arrive and only a few are worth an agent run.
- **Three-way actionability gate** — After research, label each report as not actionable (keep gathering evidence), needs human input (queue for review), or actionable (run the fix agent). *When:* An agent could act on vague problems and produce noisy changes. A gate keeps it to specific, fixable problems.
- **Snapshot and rehydrate the sandbox for CI and review loops** — After the agent pushes a PR, snapshot the sandbox. When CI fails or a review comment appears, restore the snapshot and continue the same run. *When:* Agent-written PRs need repeated fix cycles and you do not want to restart from zero each time.
- **Distill repeated agent behavior into a one-shot call** — Log many agent runs on the same kind of task, find the steps that keep recurring, and replace that agent step with a single LLM call or a small trained model. *When:* An agent works but is too costly at volume, and its solutions show a consistent pattern.
- **Evaluate on production-representative data** — Test pipeline changes on real, varied customer data rather than a local vibe check. *When:* Customer data is more varied than the developer's own data, and changes need to be measured before rollout.

## Numbers
- PostHog ingests trillions of events a month, and the pipeline must filter a large amount of noise. ([3:05](https://youtu.be/zMiSRliEzv4?t=185))
- The current manual loop from signal to shipped fix takes a few hours to a few days. ([2:06](https://youtu.be/zMiSRliEzv4?t=126))
- The pipeline is in alpha, with a wider rollout planned over the next few months. ([13:12](https://youtu.be/zMiSRliEzv4?t=792))

## Hot takes
- Off-the-shelf embeddings match on structure, so an error and a Slack complaint about the same bug will not cluster together.
- Throwing an agent at a vague problem makes it fix something, which produces noisy PRs. Gate on specificity first.
- Tokens are not free, but running an agent 100 times reveals a pattern you can replace with a cheap one-shot call.

## Tools mentioned
Claude Agent SDK, Modal, MCP, Linear, Notion, Sentry, git blame, PostHog, feature flags

## Relevance to our work
- **agentos** (2/3): SkillForge's open question is how to score skill-worthiness from telemetry. The talk describes detecting repeated agent behavior across many runs and then distilling it into a cheaper call, which is a concrete mechanism for that signal. → *Read the distillation part of the talk, then test whether SkillForge can detect repeated successful agent traces across runs and promote them to a one-shot call or skill.*
- **prosharness** (2/3): ProsHarness provides checkpoint/resume for long Claude Code runs. The talk's snapshot-and-rehydrate loop, which resumes a finished run when CI fails or a PR comment arrives, is a concrete trigger pattern for resume. → *Compare ProsHarness checkpoint/resume with the snapshot-rehydrate loop, and check whether a resume can be triggered by an external event such as a CI failure webhook instead of a manual command.*
- **general** (2/3): The query-generation-before-embedding method applies to entity resolution across heterogeneous records, and the distill-repeated-agent-runs idea applies to cheap Haiku pipelines. → *Try generating match queries with an LLM from each record before embedding in the ER pipeline, and compare recall against raw embedding matching on the dev set.*
