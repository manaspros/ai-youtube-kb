# Agents for Everything Else — swyx

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `zepu8Kk6FBQ` · [watch](https://youtu.be/zepu8Kk6FBQ) · **date:** 2026-05-18 · **length:** 14:10 · **format:** keynote · **quality:** 3/5 · **depth:** intro
- **speakers:** swyx · **orgs:** AI Engineer, Cognition, Figma, Vercel, Anthropic, Notion, Sanity, Supabase, Sessionize
- **topics:** enterprise-adoption, coding-agents, product-ux · **tags:** tiny-teams, devin, claude-cowork, agents-for-everything-else, code-as-source-of-truth, agent-experience, figma-to-website, non-engineer-agent-use, openclaw, etl-agents

> swyx describes how the nine-person AI Engineer team runs its business with coding agents (Devin, Claude Cowork), and argues agents should handle the routine "everything else" work, not just code.

## Summary
swyx, co-founder of AI Engineer, gives a 14-minute keynote on how his tiny team (nine full-time staff, a business of more than $9M) runs the conference with coding agents. A non-technical designer used Devin, hooked to Figma, to produce the AI.engineer site nearly pixel-perfect, and usage then spread across the team because people could start work at any hour without waiting on engineers. The conference CMS was replaced by code as the source of truth, and Devin edits it from plain requests such as forwarded speaker emails. He extends the pattern to ETL against vendor data, to buying services, and to planning and research tasks in a notes-to-doc tool. He argues coding agents are "breaking containment" into general knowledge work, that the main user of software is shifting to agents (his claim: about 60% of Vercel's user base is bots), and that APIs, CLIs and MCP servers matter more than dashboards. The talk is anecdotal, with no benchmarks or failure data, and its main value is as a field report on non-engineering adoption.

## Key ideas
- **Agents save the yak-shaving and dependency-chasing that slows routine work, and parallelism matters as much as autonomy.** — The speaker says productivity models that count only autonomy miss the gain from agents clearing blockers (installs, Python dependency trees) in parallel. ([4:11](https://youtu.be/zepu8Kk6FBQ?t=251))
- **Non-technical staff can drive coding agents directly once the workflow is set up.** — A contract designer in another country got a pixel-accurate site from a Figma page through Devin, then prompted the agent with annotations, without any instruction manual. The speaker says the team has to be comfortable with agents before this works. ([4:11](https://youtu.be/zepu8Kk6FBQ?t=251))
- **Removing the feedback loop with engineers raises output from staff, not just from agents.** — Staff now build throwaway projects and polish on their own because they no longer wait on a developer, which he describes as a shift from agents-for-coding to agents-for-everything-else. ([6:45](https://youtu.be/zepu8Kk6FBQ?t=405))
- **Code can replace a CMS as the source of truth that an agent maintains.** — The schedule and speaker data moved out of a CMS into committed code. Requests such as a speaker change go to the agent as forwarded emails or screenshots, with no further back-and-forth. The speaker reports that nine people can run a 1,000-person event this way. ([8:06](https://youtu.be/zepu8Kk6FBQ?t=486))
- **Agents can do routine ETL with an external vendor and personal errands with web access.** — Vendor data is synced into a single source of truth, and the agent researches and contacts suppliers, such as finding a lobster supplier for an event. The speaker frames this as an open-claw style agent with web access. ([9:21](https://youtu.be/zepu8Kk6FBQ?t=561))
- **Agents are leaving the coding domain and reaching notes, wikis and SaaS replacement.** — He describes turning raw notes into a formatted research doc, and debating whether to build internal tools in place of a paid SaaS product. His stated method is to list the top concerns of skeptical staff and reduce them one by one. ([10:44](https://youtu.be/zepu8Kk6FBQ?t=644))
- **Agent experience is becoming the main design target: APIs, CLIs and MCP servers matter more than human dashboards.** — He cites a Vercel keynote saying most of its platform users are bots, and an MCP-apps talk about shipping UI inside another app. His conclusion is that dashboards matter less to him now that an agent does the reading. ([12:06](https://youtu.be/zepu8Kk6FBQ?t=726))

## Techniques
- **Figma-to-site via coding agent** — Connect the coding agent to the design tool, have it build the page from the design file, and let the designer iterate on annotated requests. *When:* Marketing or landing pages where a designer owns the design and engineers are a bottleneck.
- **Code as the CMS source of truth, maintained by an agent** — Store structured content (schedules, speaker lists) as committed code. Have the agent apply changes from emails, screenshots or plain requests, so the repo stays canonical and no separate CMS UI is needed. *When:* Small teams with frequent but simple content edits, and where a traditional CMS adds overhead.
- **Agent as ops triage for routine requests** — Forward messy inputs (emails, screenshots, notes) to a coding agent with a short instruction like handle it, and let it make the edits and reply. *When:* High-volume, low-risk admin work where the team can review the diff.
- **Prioritised concern reduction for AI adoption** — Collect the top three objections from skeptical colleagues and address each with a concrete step, rather than dismissing their concerns. *When:* Rolling out agents to a team with mixed enthusiasm.

## Numbers
- Business revenue of more than $9M run by nine full-time staff ([2:01](https://youtu.be/zepu8Kk6FBQ?t=121))
- Cost of AI falling roughly 100x every 12 to 18 months (speaker's restated claim from earlier keynotes) ([1:02](https://youtu.be/zepu8Kk6FBQ?t=62))
- A thread of 207 replies on the agent-driven site work ([4:11](https://youtu.be/zepu8Kk6FBQ?t=251))
- 127 replies on a throwaway design project in a later thread ([5:35](https://youtu.be/zepu8Kk6FBQ?t=335))
- About 130 speakers and a couple dozen sponsors coordinated by a small team, with about 6,000 attendees expected in San Francisco ([8:06](https://youtu.be/zepu8Kk6FBQ?t=486))
- Speaker's claim that about 60% of Vercel's user base is now bots and agents (cited from a Vercel keynote) ([12:06](https://youtu.be/zepu8Kk6FBQ?t=726))

## Hot takes
- Every company can be a tiny team, and the one-person billionaire framing is an ego trap.
- The most valuable agent use is for non-coding knowledge work that an executive assistant or junior hire would otherwise do.
- Dashboards matter less as agents become the main users; APIs, CLIs and MCP servers matter more.
- Internal tools can replace paid SaaS when agents make building them cheap.

## Tools mentioned
Devin, Claude Cowork, Figma, Sanity, Notion, Google Sheets, Sessionize, Supabase, React, OpenClaw, tldraw

## Relevance to our work
- **agentos** (1/3): The talk treats agents as the primary consumer of software surfaces, which loosely matches the self-hosted agent infra thesis, but offers no technical detail that changes AgentOS design. → *Note the agent-experience framing (APIs and CLIs over dashboards) when writing up the AgentOS product surface; no code change required yet.*
- **prosharness** (1/3): The talk describes agents taking routine requests and running scheduled ops work from plain text, which is close to ProsHarness loops and schedules, though anecdotal. → *Skim the Figma-to-site and ops-via-agent workflow for ideas on how non-engineers could trigger ProsHarness runs; low priority.*
- **general** (1/3): Relevant to team-level adoption and the claim that non-technical staff can work with coding agents, but there is no evidence beyond the speaker's experience. → *Read only if planning a team rollout; otherwise skip.*
