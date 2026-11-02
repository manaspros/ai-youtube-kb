# I Tried the Tool Trying to Kill Apache Airflow (Kestra)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `b8-surdRWKo` · [watch](https://youtu.be/b8-surdRWKo) · **date:** 2026-07-02 · **length:** 5:06 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack, Kestra, Apache Airflow, n8n, Zapier, Make, Apple, JPMorgan, Toyota, Bloomberg
- **topics:** dev-tools, data-engineering · **tags:** workflow-orchestration, airflow-alternative, yaml-config, declarative-pipelines, self-hosted, docker, open-core, cron-replacement

> Quick tour of Kestra, a self-hosted, YAML-first workflow orchestrator pitched against Airflow: pipelines as config and live visual runs, but JVM memory cost, weak dynamic branching, and paywalled SSO.

## Summary
Better Stack gives a five-minute overview of Kestra, a workflow orchestrator that defines pipelines as YAML config rather than Python code. A flow is a list of tasks plus a trigger, and tasks can be in any language (Python, Node, bash, SQL, containers) in the same flow. The browser editor keeps code and a visual diagram in sync, shows live step execution, a timeline, and per-step logs. Triggers include schedules, webhooks, file arrival in a bucket, and API calls. The pitch is that config is easier for non-Python readers and PR review than Airflow DAGs, and that retries, timeouts and a dependency map beat plain cron. The presenter flags real costs: it is a Java app wanting about 4 GB RAM, YAML gets awkward for heavy dynamic branching, and SSO, RBAC and audit logs sit behind the open-core paywall. Growth and customer figures come from the company and are not independently verified. Local setup is a single Docker run command with a dashboard on localhost. No AI-specific content.

## Key ideas
- **Pipelines become YAML configuration instead of Python programs** — Airflow requires each pipeline to be a Python program to write, maintain and debug. Kestra's premise is that a workflow should be config; the presenter argues this makes pipelines readable and approvable by people who do not write Python. ([0:00](https://youtu.be/b8-surdRWKo?t=0))
- **A flow is a list of tasks plus a trigger, with a live visual editor** — The demo runs a two-step flow (a Python script and a shell command) from the browser editor. The diagram lights up step by step during execution, a timeline shows per-step duration, and each step links to its log. ([1:02](https://youtu.be/b8-surdRWKo?t=62))
- **Tasks are language-agnostic and triggers are built in** — One flow can mix Python, Node, bash, SQL and a container. Triggers include a schedule, a webhook, a file landing in a bucket, or an API call. Code and visual builder stay in sync: edits in one update the other. ([2:06](https://youtu.be/b8-surdRWKo?t=126))
- **Versus cron and Zapier/Make: retries, timeouts, dependency map and UI** — Compared with cron, you get retries, timeouts, a real dependency graph and a UI out of the box. Compared with Zapier and Make, there is no SaaS per-task billing; it is built for developers and is self-hosted. ([3:10](https://youtu.be/b8-surdRWKo?t=190))
- **Claimed scale and customers are company-sourced** — The company says it ran 2 billion workflows in 2025, about 20x the prior year, and names Apple, JPMorgan, Toyota and Bloomberg. The presenter explicitly says these numbers are not from an outside audit. ([3:10](https://youtu.be/b8-surdRWKo?t=190))
- **Real catches: JVM footprint, branching limits, open-core paywall** — The server is a Java app that wants about 4 GB RAM and a couple of cores. YAML is good for linear pipelines but fights heavy dynamic branching, where Python-based tools do better. The engine is open source, but SSO, rule-based access control and audit logs are paid; the free tier has one shared login. ([3:10](https://youtu.be/b8-surdRWKo?t=190))
- **Local run on Apple Silicon is one Docker command** — The presenter says it runs natively on Apple Silicon and that starting it is a single Docker run command, with the dashboard served on localhost. The exact image and flags are not shown on screen. ([4:20](https://youtu.be/b8-surdRWKo?t=260))

## Techniques
- **Declarative flow: list of tasks plus a trigger (YAML)** — Define each workflow as a YAML document with a task list and one or more triggers (schedule, webhook, bucket file arrival, API). Mix task types (Python, Node, bash, SQL, container) in one flow. Exact YAML keys are not shown in the video; check Kestra's docs for the schema. *When:* Linear or mostly linear data pipelines where non-Python people need to read or approve the pipeline, and the flow should be reviewed in pull requests.
- **Run a local instance with one Docker command** — Start the Kestra server with a single docker run command (the video does not show the image name or flags) and open the dashboard on localhost to build and execute flows in the browser editor. *When:* Evaluating the tool on a laptop before committing to a self-hosted deployment. Expect roughly 4 GB RAM for the JVM server.
- **Debug runs in the visual timeline and per-step logs** — Execute a flow from the browser editor, watch the diagram highlight steps as they run, open the timeline to compare step durations, then open the log for a specific step. *When:* Debugging multi-step jobs where cron gives no retry, log or failure context.

## Numbers
- Kestra raised $25 million (presenter's framing of the company) ([0:00](https://youtu.be/b8-surdRWKo?t=0))
- Company says it ran 2 billion workflows in 2025, about 20x the year before (company-reported, unverified) ([3:10](https://youtu.be/b8-surdRWKo?t=190))
- Server wants about 4 GB RAM and a couple of cores to run comfortably (Java/JVM) ([3:10](https://youtu.be/b8-surdRWKo?t=190))

## Hot takes
- The 'kill Airflow' framing is marketing; the presenter notes the growth and customer numbers come from the company, not an outside audit.
- Config-first orchestration is pitched as where the field is heading, but YAML is a poor fit for heavy dynamic branching, which the presenter says Python tools handle better.
- Open-core model paywalls SSO, RBAC and audit logs, so the free tier gives one shared login, which the presenter flags as a problem for multi-user teams.
- The claim that reviewers find the engine parallelizes better than Airflow's scheduler is unsourced in the video.

## Tools mentioned
Kestra, Apache Airflow, n8n, Zapier, Make, cron, Docker, Java / JVM, Python, Node.js, bash, SQL, Apple Silicon (Mac)

## Relevance to our work
- **prosharness** (1/3): ProsHarness has loops and schedules and checkpoint/resume for long runs; Kestra's trigger and retry model is a comparable design for schedules. → *Compare ProsHarness's schedule and loop definitions with Kestra's trigger plus retry and timeout config, and check whether its declarative flow format suggests a schema for schedules.*
