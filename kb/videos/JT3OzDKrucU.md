# Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `JT3OzDKrucU` · [watch](https://youtu.be/JT3OzDKrucU) · **date:** 2026-05-18 · **length:** 18:27 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Pedro Rodrigues · **orgs:** Supabase, Anthropic, OpenAI, Vercel, Braintrust, Lisbon AI Week
- **topics:** skills-self-improvement, mcp-and-tools, evals, context-engineering · **tags:** agent skills, SKILL.md, MCP vs skills, Supabase, RLS, eval design, Braintrust, docs over SSH, skill distribution, Claude Code, Codex

> Pedro Rodrigues (Supabase) on writing a product skill for agents, using a three-condition eval to show skills plus MCP beat MCP alone. Main lesson: agents need guidance, not more context.

## Summary
Pedro Rodrigues from Supabase explains how the team wrote its Supabase agent skill and what they learned. Agents often miss product-specific pitfalls, such as Postgres views that bypass row-level security, and they rely on stale training data. In a test, an agent with MCP plus the skill built a safe view, while MCP alone did not. The speaker gives three principles: point to live docs instead of copying them, put must-not-miss rules directly in SKILL.md because agents skip reference files, and be opinionated about workflows. He describes an eval with six scenarios, four agents from two vendors, and three conditions (baseline, MCP only, MCP plus skill), graded with Braintrust. He reports that MCP plus skill scored highest on every model, though the talk shows no score figures. He ends by saying skill distribution is still unsolved and advises starting minimal and iterating.

## Key ideas
- **Agents are weak at product-specific knowledge and often do not admit it. They default to stale training data, and that causes security mistakes.** — Example: a view over an RLS-protected table exposes rows unless security_invoker is set. The MCP-only agent missed this. The agent with the skill got it right. ([2:20](https://youtu.be/JT3OzDKrucU?t=140))
- **Skills should point to live docs, not copy them. The agent must be told where to fetch fresh information, and the speaker says to be persistent about that.** — Supabase exposes its docs over SSH so agents can browse them with familiar filesystem and bash tools. Semantic search could be layered on top. ([4:57](https://youtu.be/JT3OzDKrucU?t=297))
- **If something can be skipped, the agent will skip it. Agents avoid tool calls and extra reference-file loads.** — They rarely load more than one reference file, and the rules they miss most belong in SKILL.md itself. Keep must-not-miss rules inline and reserve reference files for optional detail. ([7:42](https://youtu.be/JT3OzDKrucU?t=462))
- **Be opinionated about workflow. Encode the way you want your product used.** — For schemas: run DDL freely on dev or staging, run the Supabase advisor for security and performance issues, fix them, and only then write one migration file. This avoids a migration per change. ([8:59](https://youtu.be/JT3OzDKrucU?t=539))
- **Evaluate the skill like code, using an agent eval with three conditions.** — Six scenarios on real Supabase projects, four agents from two vendors, and conditions of baseline, MCP only, and MCP plus skill. Each run gets a graded test-completeness score in Braintrust. ([11:19](https://youtu.be/JT3OzDKrucU?t=679))
- **Guidance is the bottleneck, not context. The MCP server already existed; the skill added the right workflow.** — The speaker says skills plus MCP beat the other conditions on every model tested: Claude Code with Opus 4.6 and Sonnet 4.6, and Codex with GPT-5.4 and GPT-5.4 Mini. The talk shows no score values. ([12:21](https://youtu.be/JT3OzDKrucU?t=741))
- **Start minimal, then iterate and version the skill. Skill distribution is still unsolved.** — Current options are a Vercel skills package, plugins that are specific to each model, and bundling skills inside product repos. ([13:36](https://youtu.be/JT3OzDKrucU?t=816))

## Techniques
- **Three-condition skill eval** — Run the same scenarios under baseline (no tools), tool-only (MCP), and tool-plus-skill. Grade each run with a rubric score in Braintrust, and compare across models and vendors. *When:* Before shipping a skill or doc, to show the skill adds value over tools alone.
- **Inline must-not-miss rules** — Put security checklists and product-defining rules in SKILL.md. Use reference files only for detail the agent can load on demand. *When:* When a rule is important and an agent has been seen skipping it in a reference file.
- **Skill as pointer to live docs** — Do not copy product docs into the skill. Tell the agent where the current docs are and how to search them, and expose them as a navigable filesystem (for example over SSH). *When:* When docs change often or the agent's training data is stale.
- **Dev-first schema workflow with a deferred migration** — Change the schema freely with DDL on dev or staging, run an advisor for security and performance checks, fix findings, then write one migration file. *When:* When an agent edits a database schema and would otherwise create a migration per iteration.
- **Start minimal and iterate** — Ship a short skill first, then expand it in versions as failures show up in evals. *When:* When first writing a skill for a product.

## Numbers
- Eval scope: 6 scenarios on ongoing Supabase projects, 4 agents from 2 vendors (Claude Code with Opus 4.6 and Sonnet 4.6; Codex with GPT-5.4 and GPT-5.4 Mini), 3 conditions. ([11:19](https://youtu.be/JT3OzDKrucU?t=679))
- The skill-plus-MCP condition scored highest on every model tested. The talk gives no numeric score values. ([12:21](https://youtu.be/JT3OzDKrucU?t=741))
- Postgres pitfall: a view without security_invoker=true bypasses the underlying table's RLS policies. ([4:06](https://youtu.be/JT3OzDKrucU?t=246))

## Hot takes
- The bottleneck is guidance, not context.
- Rules that must never be missed belong in SKILL.md, not in reference files, because agents rarely load them.
- Skills are documentation for the agent, so do not duplicate the docs; point to them.
- The MCP-versus-skills debate is settled: they play different roles. The real debate is MCP versus CLI.

## Tools mentioned
Supabase, Supabase advisor, Braintrust, Claude Code, Codex, Vercel skills package, MCP, SSH, Postgres

## Relevance to our work
- **agentos** (2/3): SkillForge mines telemetry into governed skills, and the open question is how to score success. This talk gives a concrete way to score skills: a rubric-graded eval across baseline, tool-only, and tool-plus-skill conditions. → *Add a three-condition rubric eval (no tools, MCP only, MCP plus mined skill) to SkillForge so each candidate skill has a measured success signal before it is promoted.*
- **prosharness** (2/3): ProsHarness already ranks skills and runs Claude Code. The talk offers a concrete test for whether a skill actually changes agent behaviour. → *Run the baseline / tool-only / tool-plus-skill eval on one ProsHarness skill and check whether the skill changes outcomes before relying on skill ranking.*
- **general** (2/3): Two patterns apply to context engineering and agent evals: keep must-not-miss rules inline, and grade agent runs with a rubric. Both fit the cheap-model pipeline work. → *Test whether moving one critical rule from a reference file into the main instruction file changes compliance on a small Haiku eval set.*
