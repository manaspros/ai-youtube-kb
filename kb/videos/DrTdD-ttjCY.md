# Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `DrTdD-ttjCY` · [watch](https://youtu.be/DrTdD-ttjCY) · **date:** 2026-09-18 · **length:** 20:39 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Sait Izmit · **orgs:** Snowflake
- **topics:** enterprise-adoption, product-ux, observability, evals · **tags:** go-to-market, sales-agent, quality-over-coverage, staged-rollout, change-management, question-log-analytics, feedback-loop, progressive-disclosure, agent-instructions, semantic-views, snowflake-cowork

> Snowflake's sales-team GTM agent (6,000 users): launch with quality over coverage, stage the rollout, manage activation, and use question logs as the feedback loop.

## Summary
Sait Izmit, who runs internal AI tools for Snowflake's sales org, describes launching a go-to-market assistant that has answered over 1 million questions, about 40,000 a week. He argues for quality over coverage: he wrote about 150 real seller questions before building, and the first version was only about 50% accurate, so the team narrowed scope to questions it could answer very well. The rollout ran as a pilot with AI-native users, then a 10% beta of about 600 people gated on weekly retention, then GA. He says many AI projects fail in activation and change management rather than in the technology, and that the "wow factor" fades so the product has to keep moving. Architecture changed heavily after launch: instructions moved from a Google Doc to CI/CD with tests, skills and MCP connections were added, and progressive disclosure was needed once instructions hit their limit. Finally, he treats LLM-classified question logs as the main feedback loop for product gaps and for generating enablement content, and he recommends building fast on the current stack and expecting constant re-architecture.

## Key ideas
- **Quality over coverage** — He would rather answer 50 questions at about 95% accuracy than 100 at about 70%, since early trust decides adoption. Losing a user's first few questions is very costly to recover. ([4:37](https://youtu.be/DrTdD-ttjCY?t=277))
- **Seed the eval set from the real job before building** — Before trying the agent he wrote about 150 questions the sellers actually ask, taken from the sales process. The first run scored around 50%, which set the baseline for the team's work. ([3:42](https://youtu.be/DrTdD-ttjCY?t=222))
- **Staged launch with gates** — Pilot with AI-native users to prove accuracy, then a 10% beta (about 600 people) to test whether it is a real MVP and whether users return. GA came only after weekly retention passed about 70%. ([5:57](https://youtu.be/DrTdD-ttjCY?t=357))
- **Activation and change management decide success** — Two weeks after launch only about 20% of the org had tried the product. He spent a large share of his time on demos, dashboards, manager pressure and sponsorship to drive adoption, and says this work mattered more than the technology. ([7:22](https://youtu.be/DrTdD-ttjCY?t=442))
- **The wow factor collapses, so keep raising the bar** — Users go from talk-to-your-data to automation via MCP connections, then to tool building and hyper-personalization. If the team stops at the first stage, a competitor can take users within a month or two. ([8:35](https://youtu.be/DrTdD-ttjCY?t=515))
- **Expect heavy re-architecture; the launch design will not last** — About 80% of the original PRD and architecture no longer matches. Roughly 30-40% of sprint work goes to re-architecting, and he advises not over-investing in the current architecture. ([12:45](https://youtu.be/DrTdD-ttjCY?t=765))
- **Question logs as the feedback loop** — LLMs classify the 1.2 million logged questions into topics and subcategories with examples. Repeated questions and frustrated messages show gaps in real time, and the same data can drive generated battle cards and enablement docs that feed back into the agent. ([14:03](https://youtu.be/DrTdD-ttjCY?t=843))

## Techniques
- **Question bank as the first eval set** — Write 100-150 real user questions from the job process before building, score the agent against them, and use the accuracy number to decide what scope to ship. *When:* Before building an internal assistant for a domain with known workflows, when a low first-run score would damage trust.
- **Narrow-scope, high-accuracy launch** — Ship only the question types that can be answered at about 95% quality. Add coverage (data sources, tables) after launch as the accuracy holds. He says 60% of the data was added after the launch. *When:* When the first impression matters and users will judge the product on their first few questions.
- **Pilot, beta, GA with metric gates** — Pilot with a small group of AI-native users to fix rough edges. Then run a 10% beta and track feature requests (to find MVP gaps) and weekly active retention before GA. *When:* Rolling out an internal AI tool to a large org where bad early experiences are hard to recover from.
- **LLM classification of usage logs** — Run an LLM over the question logs at scale to build a topic and subtopic hierarchy with example questions. Track the rate of repeated questions and frustration (swearing, rephrasing) as signals. *When:* When the agent has real traffic and the team needs to find feature gaps and quality problems without interviewing users one by one.
- **Closed loop from logs to content** — Use the classified gaps to generate enablement content (battle cards, sales docs) from sources such as Confluence, Jira, Slack and PRDs, then feed that content back into the agent's knowledge. *When:* When the knowledge base lags product launches and the team needs fast updates.
- **Agent instructions under version control with tests** — Move instructions out of a shared Google Doc into CI/CD with unit tests and routing tests. Once instructions grow past their limit, move procedures into a skill library and use progressive disclosure. *When:* When the agent's instruction set is changing often and multiple people edit it, or when one prompt can no longer hold all workflows.
- **Build on a managed agent platform with inherited access control** — Put all the data in one platform (first-party, third-party, CRM, call transcripts). Agents inherit role-based access and guardrails, and the platform supplies the chat UI, so no UI code is needed. *When:* When the team wants fast iteration and does not want to build its own access control or UI.

## Numbers
- Internal GTM assistant launched September of last year; over 1 million questions answered so far. ([0:08](https://youtu.be/DrTdD-ttjCY?t=8))
- About 40,000 questions per week. ([0:08](https://youtu.be/DrTdD-ttjCY?t=8))
- Snowflake has about 10,000 employees, almost half in sales. ([1:04](https://youtu.be/DrTdD-ttjCY?t=64))
- Some account executives carry about 1,000 accounts each. ([1:04](https://youtu.be/DrTdD-ttjCY?t=64))
- About 150 seed questions written before the agent was built. ([3:42](https://youtu.be/DrTdD-ttjCY?t=222))
- Initial accuracy on the first test run was about 50%. ([4:37](https://youtu.be/DrTdD-ttjCY?t=277))
- About 60% of the data was added after launch, 6-7 months post-launch. ([4:37](https://youtu.be/DrTdD-ttjCY?t=277))
- Current agent: 15 semantic views, 85 tables, 3,000 columns, 5-6 MCP connections, close to 20 skills. ([4:37](https://youtu.be/DrTdD-ttjCY?t=277))
- Beta: 10% of users, about 600 people; the GA gate was weekly retention above about 70%. ([5:57](https://youtu.be/DrTdD-ttjCY?t=357))
- Two weeks after launch, only about 20% of the organization had tried the product. ([7:22](https://youtu.be/DrTdD-ttjCY?t=442))
- Launch agent instructions were 9 pages long, kept in a Google Doc. ([11:25](https://youtu.be/DrTdD-ttjCY?t=685))
- About 80% of the original PRD and architecture no longer matched the system; 30-40% of sprint work went to re-architecting. ([12:45](https://youtu.be/DrTdD-ttjCY?t=765))
- Question logs classified: 1.2 million questions at about 40,000 per week. ([14:03](https://youtu.be/DrTdD-ttjCY?t=843))

## Hot takes
- Quality over coverage: going for coverage early will shoot you in the foot.
- Activation and change management fail more AI initiatives than the technology does.
- Every time users are happy, be paranoid about what you will show them in a month or two.
- Interviewing 100 sellers a week to find topic gaps is the wrong approach; the question logs show it in real time.

## Tools mentioned
Snowflake Cowork (formerly Snowflake Intelligence), Cortex Analyst, Cortex Search, Snowflake semantic views, MCP connections, Confluence, Jira, Slack, Gmail, Salesforce, Google Docs

## Relevance to our work
- **agentos** (2/3): The talk's log-classification loop, with repeated questions and rephrasing as implicit quality signals, answers part of the open question on SkillForge's success signal. The 150-question seed set also maps to an eval set for agents. → *In SkillForge, test whether repeated-question and rephrase-within-session rates from LLM-classified telemetry predict skill success, and seed a question set from real usage before building new skill features.*
- **prosharness** (1/3): The talk describes progressive disclosure once a single instruction file hits its limit, and moving procedures into a skill library. This is context engineering for the harness's prompts. → *When ProsHarness's prompt or CLAUDE.md grows too large, move workflow-specific instructions into on-demand skill files and load them only when needed.*
