# How I automate my own job at Hugging Face using agents — Niels Rogge, Hugging Face

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `FLUoowDJg4I` · [watch](https://youtu.be/FLUoowDJg4I) · **date:** 2026-09-18 · **length:** 20:37 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Niels Rogge · **orgs:** Hugging Face, Anthropic, Cursor, Modal, Langfuse, GitHub, Slack, Google DeepMind, Apple
- **topics:** software-factory, agent-architecture, observability, models-research · **tags:** hugging-face, outreach-automation, cron, github-actions, modal, batch-containers, claude-agent-sdk, glm-5.2, open-models, langfuse, tracing, skills, workflow-vs-agent, community-science, papers-with-code

> Hugging Face's Niels Rogge shows how nightly agents open outreach GitHub issues and PRs to move researchers' artifacts onto the Hub, moving from a fixed workflow to an autonomous agent loop.

## Summary
Niels Rogge describes automating the outreach part of Hugging Face's community science team, whose job is moving research weights and datasets from Google Drive, Dropbox and similar hosts onto the Hub. He began in 2024 with a deterministic pipeline of plain LLM API calls, no framework, run as a nightly cron job on GitHub Actions, with Langfuse for tracing. Later he replaced the follow-up step with an autonomous agent loop built on the Claude Agent SDK, running on Modal in parallel containers, one container per GitHub issue. The agent uses bash and the Hugging Face CLI as its main tools, with an open model (GLM 5.2) served through Hugging Face inference providers, and posts its results to Slack. He reports that many issues got positive replies, a few negative ones, and that the agent does not disclose it is a bot. He concludes that for this use case agents beat workflows, that a CLI, a skill and a sandbox are enough, and that evals still matter. He ends with a side project, an X account for daily papers, and a revival of Papers with Code.

## Key ideas
- **Start with a deterministic workflow that copies the human steps** — He first built a fixed pipeline that followed his manual steps (find repo, read README, check Hub, open PR or issue, follow up). Each step was one LLM API call with no agent framework, which gave him control. He credits Anthropic's 'start simple, avoid frameworks' advice. ([4:05](https://youtu.be/FLUoowDJg4I?t=245))
- **Nightly cron is enough for background agent work** — The pipeline runs as a Python script with LLM API calls on a schedule. He uses GitHub Actions cron, which is free at his volume and easy to manage in the UI. It reads hundreds of new arXiv papers each night and opens issues or PRs. ([6:53](https://youtu.be/FLUoowDJg4I?t=413))
- **Follow-ups are where the workflow broke and an agent loop fit** — Replies to the generated issues were unpredictable, so he moved the follow-up step to a fully autonomous agent (a loop that calls tools until done). He says models are now good enough that agents can replace workflows, and cites Cursor replacing 12,000 lines of custom code with a 200-line skill. ([9:08](https://youtu.be/FLUoowDJg4I?t=548))
- **Minimal toolset: one CLI, one skill, one sandbox** — The agent mainly uses bash and the Hugging Face CLI, with the matching HF CLI skill. It runs in a sandbox. He argues that these are all it needs, with no custom tool layer. ([10:30](https://youtu.be/FLUoowDJg4I?t=630))
- **Batch parallel containers, one per work item** — On Modal, each GitHub issue gets its own container running one agent loop, and hundreds run in parallel. Cold starts are fast, which suits overnight background runs. He runs the follow-up step by hand by invoking a Cursor skill that fans out to other agents, then posts results to Slack. ([11:50](https://youtu.be/FLUoowDJg4I?t=710))
- **Trace every LLM step to see inputs, prompts, cost and latency** — Langfuse records the inputs, outputs, prompts, cost and latency of each LLM call. He uses it to see what the model is doing across hundreds of nightly runs. ([7:52](https://youtu.be/FLUoowDJg4I?t=472))
- **Do not disclose the bot, and judge by reply quality** — He says he does not disclose that the outreach is an agent, because people would close issues. Most replies say the request makes sense. He reports only two negative comments in thousands of issues. Some replies are also written by other agents. He says the agent posts the same content he used to write by hand. ([13:19](https://youtu.be/FLUoowDJg4I?t=799))
- **Evaluate the agent before trusting it at scale** — He ends by saying evals matter, and points to Hamel Husain's free LLM evals FAQ as a guide to avoid agent slop. His evidence for quality is the reactions, not a formal eval set in the talk. ([17:09](https://youtu.be/FLUoowDJg4I?t=1029))

## Techniques
- **Deterministic LLM pipeline mirroring the manual process** — Break the human routine into fixed steps, call an LLM API once per step, skip agent frameworks, and run it as a plain Python script. *When:* Use it first for a repetitive task with known steps where you want control and predictability.
- **Cron for overnight background agents** — Schedule the script with GitHub Actions cron. Each run reads a batch of new inputs (for example, the day's papers) and writes outputs (issues or PRs). *When:* Use it when work arrives in batches on a daily rhythm and nobody has to watch it run.
- **Promote a step to an autonomous loop only where outputs are unpredictable** — Keep the stable steps as a workflow. Give the step with unpredictable follow-ups an agent with a CLI tool, a skill and a sandbox, and let it call tools until done. *When:* Use it when the next action depends on free-text replies from outside, which fixed branching cannot handle.
- **One container per work item for parallel agents** — Use a batch container service (Modal here). Each container runs one full agent loop on one item, for example one GitHub issue, and the platform runs many in parallel. *When:* Use it for many independent items that each need a long agent run and must not share state.
- **Skill as a manual trigger that fans out to subagents** — Package the workflow as a skill in the editor. Invoking it starts an orchestrating agent, which in turn starts the per-item agents and posts a summary to Slack. *When:* Use it when a human should decide when a batch runs but the batch itself is large.
- **Open-model routing through one OpenAI-compatible endpoint** — Point the SDK at Hugging Face inference providers, which front several hosts (Together, Fireworks and others) behind one API, then pick an open model such as GLM 5.2. *When:* Use it when you want to cut cost or swap models without changing the agent code.
- **Template completion from source material** — Give the agent a fixed template (such as a model card template) plus the paper PDF and README, and have it fill the template from those sources only. *When:* Use it for structured documentation that must follow a schema.

## Numbers
- Hundreds of new research papers read each night by the cron job ([6:53](https://youtu.be/FLUoowDJg4I?t=413))
- Cursor replaced a 12,000-line custom workflow with a 200-line skill (cited, not measured by the speaker) ([9:08](https://youtu.be/FLUoowDJg4I?t=548))
- GLM 5.2 is reported to beat Opus 4.8 on PostTrainBench and to be cheaper (cited claim) ([10:30](https://youtu.be/FLUoowDJg4I?t=630))
- Thousands of issues created on the Hub by the agents; only two negative comments so far ([13:19](https://youtu.be/FLUoowDJg4I?t=799))
- Most-upvoted agent-created issue (tiny recursive models) got more than 60 upvotes, and the model was then released on the Hub ([15:47](https://youtu.be/FLUoowDJg4I?t=947))
- Daily Papers X account has more than 90,000 followers and posts every four hours ([18:35](https://youtu.be/FLUoowDJg4I?t=1115))
- One tweet from the account about an NVIDIA GLM 5.2 release got more than 2,000 likes ([18:35](https://youtu.be/FLUoowDJg4I?t=1115))

## Hot takes
- Agents are better than workflows for this kind of outreach, and most custom orchestration code can be replaced by a CLI, a skill and a sandbox.
- Outreach agents should not disclose they are bots, because disclosure makes maintainers close the issue.
- Open models such as GLM 5.2 can now replace closed models for agent work.

## Tools mentioned
Claude Agent SDK, Cursor, Modal, GitHub Actions, Langfuse, Hugging Face CLI, Hugging Face inference providers, Slack, Gemini, Claude Code

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs long agent jobs. The talk's pattern of one container per work item, run nightly by cron with per-item results, maps to ProsHarness checkpoint and resume runs. → *Prototype running one ProsHarness long run per task item in its own container, with a per-item checkpoint, and compare it with a single long run.*
- **general** (2/3): The talk gives a clear rule for choosing between workflow and agent: fixed steps stay deterministic, and only the unpredictable step becomes an autonomous loop. This applies to any agent design. → *Before the next agent build, write the deterministic version of the pipeline first, then move only the steps whose outputs cannot be predicted into an agent loop.*
- **agentos** (1/3): AgentOS is an OpenAI-compatible proxy with strategy routing. The talk's single OpenAI-compatible endpoint that fronts several inference hosts is a related pattern, but the talk does not discuss proxies. → *Read how Hugging Face inference providers expose one OpenAI-compatible endpoint across hosts, and note it as a reference point for AgentOS strategy routing.*
