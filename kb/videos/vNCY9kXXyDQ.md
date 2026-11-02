# Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `vNCY9kXXyDQ` · [watch](https://youtu.be/vNCY9kXXyDQ) · **date:** 2026-06-18 · **length:** 24:09 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Marc Klingen · **orgs:** Langfuse, ClickHouse
- **topics:** skills-self-improvement, observability, evals, claude-code · **tags:** agent skills, Claude Code, Langfuse, tracing, LLM-as-judge, auto-research, target function, progressive disclosure, docs for agents, skill staleness, CLI for agents

> Langfuse's founder explains how they built an installable skill that teaches coding agents to add Langfuse tracing and evals, and what they learned about docs, eval checks and auto-tuning skills.

## Summary
Marc Klingen (Langfuse, open-source LLM observability) describes building a skill so coding agents like Claude Code can add Langfuse tracing, prompt management and evals to a user's project. The core problem is that agents rely on stale pretraining knowledge, hallucinate old SDK methods and fix instrumentation only after trial and error. Their fix is a SKILL.md with style rules (such as asking follow-up questions first), per-module reference files loaded on demand, an agent-readable docs sitemap, Markdown doc access, and a docs search endpoint backed by their existing docs RAG. They also wrapped their APIs in a CLI so agents can do what users used to click through in the UI. Evaluation of the skill uses five natural-language checks, judged by an LLM over the file system and trace state before and after the run. Finally, they used an auto-research loop to propose skill edits against a target function, then had humans review the suggestions; the target function had to be carefully defined, since optimising for fewer turns made the agent drop the docs lookups. He closes with open questions about how to keep installed skill copies from going stale.

## Key ideas
- **Skills are a shortcut to reliability** — Skills give an agent a procedure to follow, like a manual for a Rubik's cube. They can replace router-plus-workflow designs, letting one agent pull in context for a problem that spans several domains. ([1:01](https://youtu.be/vNCY9kXXyDQ?t=61))
- **Production traces show what to build next** — Tracing runtime executions reveals use cases nobody expected, such as users wanting to change a password. Traces also show which existing skills are out of date or inefficient. ([3:20](https://youtu.be/vNCY9kXXyDQ?t=200))
- **Pretraining knowledge goes stale for SDK setup** — An agent asked to add tracing from memory writes instrumentation for an old SDK, then tests it, finds it broken, and only then fetches current docs. The fix is to make the agent fetch current information first. ([5:54](https://youtu.be/vNCY9kXXyDQ?t=354))
- **Looking at traces gets about 80% of the detail** — The team instrumented Claude Code and read the traces of their own interactive runs to see where the agent wandered. Their view is that teams over-complicate evals before anyone has read real agent runs. ([8:24](https://youtu.be/vNCY9kXXyDQ?t=504))
- **Fix agent failure modes with cheap, direct changes** — Defaulting to a Europe data region caused problems for US users, so the skill now asks which region applies. Hallucinated CLI flags were reduced by telling the agent to use --help. Markdown doc access and an agent sitemap cut wasted tokens and fetches. ([9:40](https://youtu.be/vNCY9kXXyDQ?t=580))
- **Reference the source instead of copying it** — Copying dynamic docs into a skill creates a second, stale version of the truth. The team prefers pointers to canonical docs and search, with timestamps on any local copy. ([13:25](https://youtu.be/vNCY9kXXyDQ?t=805))
- **Target function decides what auto-research optimises** — Minimising turns led the optimiser to delete doc-fetch steps, which defeated the purpose. Removing the approval gate was also proposed. Three of six suggestions were accepted after human review. ([14:47](https://youtu.be/vNCY9kXXyDQ?t=887))

## Techniques
- **Skill with progressive disclosure** — Keep a short SKILL.md with behaviour rules (e.g. ask follow-up questions before making decisions) and link to per-module reference files that the agent loads only when needed. Let the agent curl live docs for detail. *When:* When one product or library spans many feature areas and a single prompt would be too large or too generic.
- **Agent-facing docs surface** — Expose a sitemap the agent reads first, support Markdown responses via .md suffix or content negotiation, and provide a search endpoint over the existing docs RAG that returns chunks for natural-language queries. Log the search queries to find documentation gaps. *When:* When coding agents waste tokens on HTML pages or click through many pages looking for one answer.
- **Wrap the API as a CLI and advertise --help** — Put every operation a human would do in the UI behind a CLI. Tell the agent to read --help early so it does not invent flags. *When:* When agents need to automate workflows that have only been available through a UI or raw APIs.
- **Natural-language checks for skill evals** — Write about five checks as plain statements, such as 'OpenAI instrumentation was added' or 'retrieval spans appear in the trace'. Judge them with an LLM over the file system and trace state, before and after the skill runs. *When:* When you need a fast regression check for a skill or agent setup across many different application types.
- **Auto-research loop on a skill with human review** — Give an optimiser agent a target function and let it propose skill edits. Review the proposals yourself, since many do not make sense when the target is imperfect. Iterate on the target function if it rewards the wrong behaviour. *When:* When you want to explore many skill variants faster than a small team can by hand.
- **Timestamped skill copies for staleness** — Record the fetch date in an installed skill so the agent can notice when it is old and refresh it. This was the team's leading option; they had not built it yet. *When:* When skills are copied into user environments and cannot be auto-upgraded.

## Numbers
- Langfuse docs were 478 pages, which made them hard for users and agents to navigate ([3:20](https://youtu.be/vNCY9kXXyDQ?t=200))
- Skill evaluated with five natural-language checks run by LLM-as-judge over file system and trace state ([12:09](https://youtu.be/vNCY9kXXyDQ?t=729))
- Auto-research produced six suggested skill improvements; three were accepted ([14:47](https://youtu.be/vNCY9kXXyDQ?t=887))
- Thousands of community members and thousands of Cloud customers were the intended users of the skill ([7:12](https://youtu.be/vNCY9kXXyDQ?t=432))
- Speaker's rule of thumb: looking at traces gets you about 80% of the detail needed ([8:24](https://youtu.be/vNCY9kXXyDQ?t=504))

## Hot takes
- Nobody reads documentation themselves; users just want the agent to add the thing.
- For a small team, plugin marketplaces are not worth it because each agent vendor's integration needs upkeep.
- Asking users permission to install a skill only matters if the skill is more trusted than the public web.
- Minimising turns is the wrong target for skill optimisation, because it removes the steps that keep the agent current.

## Tools mentioned
Claude Code, Langfuse, OpenAI SDK

## Relevance to our work
- **agentos** (2/3): The talk covers using production traces to find skill gaps and auto-research on skills with a target function. This maps onto L2D SkillForge's open question about skill-worthiness and success signals. → *When designing SkillForge's skill-worthiness score, add a guard metric that rewards fresh-doc fetches, so the optimiser does not learn to drop them (the Langfuse target-function lesson at 14:47).*
