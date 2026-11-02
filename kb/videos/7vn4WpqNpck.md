# Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `7vn4WpqNpck` · [watch](https://youtu.be/7vn4WpqNpck) · **date:** 2026-08-18 · **length:** 18:08 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Denys Linkov · **orgs:** Wisedocs, Anthropic, Spotify, Stripe, Google, OpenAI, METR
- **topics:** coding-agents, evals, enterprise-adoption · **tags:** monorepo, refactor, tech-debt, time-horizon, agent-reliability, orchestrator-evaluation, subagents, plan-mode, pr-review, legacy-code, data-pipeline

> Denys Linkov (Wisedocs) on whether a six-month monorepo refactor of a medical-claims ML pipeline was worth it when coding agents keep improving, and how to measure agent reliability.

## Summary
Denys Linkov describes Wisedocs, which processes medical claim PDFs of 10,000+ pages through an ML pipeline spread over more than 10 legacy repos. The team chose a six-month refactor into a monorepo to fix slow delivery, a pipeline that was hard to change, and code nobody wanted to touch. Before coding, they benchmarked five open-source orchestrators against 17 criteria, a process he says could now be mostly agentic with deep research and per-criterion subagents. He warns that agent reliability is still far from "kick off and walk away": he argues for measuring task success at 80 to 99 percent, not the usual 50 percent, because a 50-percent-likely hour is mostly wasted. He reports that newer models and harnesses (Sonnet 4.6, Opus) now do in one or two passes what an earlier o3 run needed hours of corrections for. The monorepo then gave steeper velocity and more developers committing, and he says the outcomes were lower pipeline time and cost, support for larger files, and features that used to take months shipping in under a week. He is honest that a zero-shot full refactor by GPT-5.5 produced scaffolding without working models, so the models cannot yet self-validate big refactors. His conclusion is that the refactor paid off, and the decision depends on business value and the trade-off of doing it now versus later.

## Key ideas
- **Tech debt should be judged like financial debt, with an ROI check.** — Speaker says bad code compounds in unexpected ways, and added complexity can quickly outrun the ROI a feature or customer brings in. The question is whether the debt was taken on deliberately. ([1:23](https://youtu.be/7vn4WpqNpck?t=83))
- **Shipping speed has not meant better product quality.** — He says teams ship faster while maintainability and reliability have slipped, and shows uptime figures from two large companies that he says are below the target reliability. He is making a point, not giving a precise number. ([2:21](https://youtu.be/7vn4WpqNpck?t=141))
- **Measure agent success at 80-99 percent, not 50 percent.** — The usual time-horizon graph uses 50 percent accuracy. He argues the useful bar is 90 to 99 percent, because a long task with only a coin-flip chance of success wastes the compute and the engineer's attention. ([6:55](https://youtu.be/7vn4WpqNpck?t=415))
- **Newer models and harnesses changed the work from manual to mostly autonomous.** — An earlier o3 run in Cursor took three hours of back-and-forth and made 10 major mistakes. Sonnet 4.6 needed one more iteration, and Opus one-shot the same task. Modern harnesses use subagents, plan calls, shell commands and verification steps. Each run costs more, but takes far less human effort. ([4:42](https://youtu.be/7vn4WpqNpck?t=282))
- **Agentic evaluation of tools can replace a manual scoring doc.** — The orchestrator study used a team of three, five open-source projects and 17 criteria, all held in a Confluence doc. He says the same work could now start with deep research, check it against problem statements, run a subagent per criterion, and then build proofs of concept. ([4:42](https://youtu.be/7vn4WpqNpck?t=282))
- **Beware of trusting long agent-written reports.** — He calls it AI psychosis when a 20-page research report looks good but the features it describes do not exist in the product. Checking claims against the real codebase or a proof of concept is still needed. ([4:42](https://youtu.be/7vn4WpqNpck?t=282))
- **A monorepo helps agents with end-to-end testing and deployment more than navigation.** — Models navigate several repos well when they sit under one parent folder. Cross-repo end-to-end tests, deployment and sandbox setup, which involve cloning and configuring many repos, are still much harder. ([14:58](https://youtu.be/7vn4WpqNpck?t=898))
- **A zero-shot refactor can look finished and not be.** — GPT-5.5 extra high finished a refactor prompt in 10 minutes 22 seconds, but wrote about 2,000 lines of mostly scaffolding with no real models and no bootstrap command. He expects consistent large one-shot refactors in about six months. ([11:44](https://youtu.be/7vn4WpqNpck?t=704))

## Techniques
- **Time-horizon reliability check before long runs** — Measure how long tasks of a given type can run before success falls below 90 to 99 percent, and only hand off tasks that meet that bar. Do not schedule a long run with roughly 50 percent odds. *When:* Deciding whether an unattended agent run is worth starting, or choosing task size for an agent queue.
- **Agentic tool-evaluation pipeline** — Deep research gathers candidate tools, then one subagent per criterion scores each tool against the requirements, then short proofs of concept validate the top picks. Human review sits at the end. *When:* Comparing frameworks, orchestrators or libraries against a fixed set of criteria.
- **Monorepo consolidation for agent-driven work** — Merge many service repos into one tree so the agent can read cross-service code and run end-to-end tests and deployments in one place. *When:* A system spans many repos and agents or developers need to change schemas, APIs and the stack together.
- **Human PRs as a context-building step** — During a big refactor with few contributors, keep human PR review so the team learns what changed. Add plan mode and local skill-based review gradually as trust grows. *When:* Early in an agent-driven rebuild of a codebase, before automated review is trusted.
- **Check hidden assumptions in dependencies** — Before building on a library feature, confirm it is stable, since one assumed feature was in beta. Put this check into the POC and validation stage. *When:* Building a refactor or proof of concept on top of third-party libraries.
- **Layered refactor instead of a full rewrite** — Isolate parts of the codebase and refactor them in layers, while putting guardrails on the AI-written code, rather than rewriting the whole system at once. *When:* A full refactor is too costly, but parts of the system need to become easier for agents to change.

## Numbers
- Medical claim PDFs exceed 10,000 pages; some are larger than video files. ([0:08](https://youtu.be/7vn4WpqNpck?t=8))
- Legacy system had more than 10 repos, aged more than six years; refactor ran about six months starting April. ([3:18](https://youtu.be/7vn4WpqNpck?t=198))
- Orchestrator benchmark: 5 open-source projects, 17 criteria, team of 3, about two months of evaluation. ([3:18](https://youtu.be/7vn4WpqNpck?t=198))
- Earlier o3 refactor in Cursor: about 3 hours of back-and-forth, 10 major mistakes. Sonnet 4.6 needed one extra iteration; Opus one-shot it. ([4:42](https://youtu.be/7vn4WpqNpck?t=282))
- Rebuilding the same task on modern models is estimated at about one-fifth of the earlier time. ([5:59](https://youtu.be/7vn4WpqNpck?t=359))
- Meter (METR) time-horizon graph: 50 percent-accuracy line exceeds 18 hours of human work; speaker argues for 80 to 99 percent. Mythos Preview success declines sharply around the 4-hour mark and some tasks fail well before 15 minutes. ([8:19](https://youtu.be/7vn4WpqNpck?t=499))
- Zero-shot GPT-5.5 extra-high refactor finished in 10 min 22 s with about 2,000 lines, mostly scaffolding. ([11:44](https://youtu.be/7vn4WpqNpck?t=704))
- Speaker said 15 of 17 requirements were right at the start of the refactor. ([16:22](https://youtu.be/7vn4WpqNpck?t=982))
- After refactor, features that took multiple months ship in under a week; pipeline time and cost were reduced and larger files are supported (no figures given). ([13:53](https://youtu.be/7vn4WpqNpck?t=833))

## Hot takes
- Teams are shipping faster while product quality, maintainability and reliability have degraded.
- Measure agent reliability at 90 to 99 percent accuracy, not 50 percent; a 50 percent task is a waste of time.
- AI psychosis: a long, confident research report is easy to trust without checking that the features exist.
- Refactoring later is getting easier, but a big refactor was still worth doing now for this team.
- Models can navigate multiple repos fine, but a monorepo is still easier for end-to-end testing and deployment.

## Tools mentioned
Cursor, Temporal, Claude Sonnet 4.6, Claude Opus 4.8, o3, GPT-5.5, Confluence, Claude Code plan mode

## Relevance to our work
- **prosharness** (2/3): Checkpoint/resume and plan-to-run loops in ProsHarness depend on whether a long agent run will finish; the talk's time-horizon and doom-loop points apply directly to when to kick off unattended runs. → *Add a success-rate estimate per task type to ProsHarness plan approval, so long runs are kicked off only above a chosen reliability threshold (for example 90 percent).*
- **agentos** (1/3): Speaker's point on 80-99 percent time-horizon reliability applies to agent eval reporting, but it is a general observation, not an AgentOS design change. → *Report AgentOS eval results at 80 and 90 percent task-success horizons, not only averages.*
