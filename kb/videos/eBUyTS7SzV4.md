# Every company should have a Brain — Garry Tan, Y Combinator

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `eBUyTS7SzV4` · [watch](https://youtu.be/eBUyTS7SzV4) · **date:** 2026-07-18 · **length:** 21:08 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Garry Tan · **orgs:** Y Combinator, OpenClaw, Hermes agent
- **topics:** context-engineering, memory, skills-self-improvement, enterprise-adoption · **tags:** company brain, GBrain, skills as employees, resolver table, trigger evals, skillify, memory hygiene, latent vs deterministic compute, context engineering, YC, productivity claims

> Y Combinator's Garry Tan argues that AI productivity comes from how work is wired (skills as employees, routing tables, company memory with hygiene), not the model, and pitches an open-source "company brain" called GBrain.

## Summary
Garry Tan, YC's CEO, describes running YC as an AI-native organization and claims his personal output rose about 400x (self-discounted to roughly 8x at the floor). He says the gap between 2x and 100x users is how they wire the work, since they use the same model. He maps agent setups onto an org: skill files are employees, resolver tables are org charts, filing rules are process, and trigger evals are performance reviews. He separates latent-space work (the LLM for judgment and vague intent) from deterministic work (code), and says large state such as seat assignments should live outside the context window. He frames context engineering as choosing which "three books" are open, with a company brain as library plus librarian. He stresses memory hygiene (provenance, contradiction checks, pruning) because unmaintained memory gives confident stale answers. He closes with "never do one-off work": skillify each finished task so it never has to be asked for twice. Parts of the talk are a pitch for GBrain and YC, and the productivity numbers are self-reported.

## Key ideas
- **Productivity gains come from how the work is wired, not from the model** — He claims his output rose about 400x versus his 2013 baseline of about 14 usable lines a day. After discounting for verbosity he still says 8x at the floor and 80x in the middle. He says 2x and 100x users run the same model, so the leverage is in the surrounding system. ([1:11](https://youtu.be/eBUyTS7SzV4?t=71))
- **Map agent setups onto an organization** — A skill file is an employee with one job written as a procedure. A resolver table is an org chart that routes each task to the right file. Filing rules are process. Trigger evals check whether the right file actually loads, which he compares to performance reviews. He says you are managing a workforce made of markdown, not just writing software. ([3:51](https://youtu.be/eBUyTS7SzV4?t=231))
- **Split computation between latent space (LLM) and deterministic space (code)** — The LLM handles taste, judgment and vague human intent, steered by markdown. Code handles deterministic work. Most bugs he sees come from work sitting on the wrong side of this split. ([8:36](https://youtu.be/eBUyTS7SzV4?t=516))
- **Large state must live outside the context window** — His example is seating 800 people so that neighbours are well matched. The seat layout is stored and computed in code, and the LLM does only the human-judgment part. He says this took about 10 minutes and a couple hundred dollars of tokens, where by hand it would take a month. ([10:01](https://youtu.be/eBUyTS7SzV4?t=601))
- **Context engineering is choosing which few documents are loaded** — A human holds about seven items in working memory, while an agent can hold about a million tokens, roughly three long books. A company is a library, and the hard problem is picking which pieces the agent should have open for a given task. Retrieval is the easy primitive. What is written down, enriched, linked, promoted to hot memory or filed as cold reference, and how disagreements are resolved is the product. ([12:45](https://youtu.be/eBUyTS7SzV4?t=765))
- **Memory needs hygiene or it becomes a confident garbage dump** — He lists three requirements: provenance on every fact, contradiction checks when new facts collide with old ones, and a librarian (human plus agent) whose main job is pruning. Without these, retrieval surfaces stale facts with full confidence and bad skill files encode bad processes permanently. ([13:58](https://youtu.be/eBUyTS7SzV4?t=838))
- **Never do one-off work: skillify each finished task** — After a task you are happy with, turn the steps into a reusable skill. His rule is that if you have to ask for something twice, you failed. He says the organization that captures what it learns gets smarter every day, and that model quality is rented while the brain is owned. ([15:23](https://youtu.be/eBUyTS7SzV4?t=923))
- **The concepts transfer to any stack** — He says his tools are not required. Codex can do about 90% of this, and the principles (where computation lives, skill files as employees, a library and librarian, never doing one-off work) apply to any harness. ([18:20](https://youtu.be/eBUyTS7SzV4?t=1100))

## Techniques
- **Skill file as a single-job employee** — Write one markdown procedure per capability, with one job and steps clear enough that an agent can execute it. Maintain each one like a person's role, with engineers filling in what the skill cannot yet do. *When:* Any recurring procedural work, such as filing, reporting, or test changes, that you currently repeat by prompting.
- **Resolver table for routing context** — Keep a table that maps task types to the context or skill file to load, for example altering a test loads test.md. The resolver decides which file handles each incoming task. *When:* A top-level CLAUDE.md or AGENTS.md is growing too large, so context should be loaded per task type.
- **Trigger evals on routing** — Write tests that check whether the right file loads for a given task, and track misses. He compares this to a performance review for the routing layer. *When:* After adding skills or a resolver table, to confirm that routing works in practice.
- **Skillify at task end** — When the output is accepted, convert the steps taken into a reusable skill file and load it into the harness, so the same request does not need to be repeated. *When:* Any task that you expect to repeat, and especially after you have had to correct the agent.
- **Split latent and deterministic compute** — Use the LLM only for judgment, taste and interpreting vague requests. Put state, combinatorial assignment and exact computation in code or a data store, and keep that state out of the context window. *When:* Tasks that involve large or combinatorial state, such as assignments, matching or ranking across many records.
- **Curated company brain** — Store facts with provenance, check new facts for contradictions against old ones, separate hot memory from cold reference, and run a regular pruning pass with a human and an agent. *When:* Cross-session memory or a shared knowledge store that agents read from.
- **Select a small working set per task** — Retrieve only the few documents that a task needs, and pick them with a deliberate rule rather than loading the whole corpus. *When:* Agents operating over large document or email collections where the context window is limited.

## Numbers
- Self-reported output of about 14 usable logical lines of code per day in 2013 (median about 15 in the literature cited, 15 to 50 range) ([1:11](https://youtu.be/eBUyTS7SzV4?t=71))
- Self-reported output about 400x the 2013 baseline; after a verbosity penalty, about 8x at the floor and 80x in the middle ([1:11](https://youtu.be/eBUyTS7SzV4?t=71))
- In the Winter 25 batch, about a quarter of companies had codebases that were 95% AI-generated (stated as of a year before the talk) ([2:34](https://youtu.be/eBUyTS7SzV4?t=154))
- 94 YC companies have crossed $100M in revenue from a seed check ([2:34](https://youtu.be/eBUyTS7SzV4?t=154))
- Emergence (Summer 24) went from public launch to nine figures of ARR in eight months, and had 15 people at $15M ARR ([6:21](https://youtu.be/eBUyTS7SzV4?t=381))
- A Winter 24 company (captioned as Retail) is at about $60M with about 40 people ([6:21](https://youtu.be/eBUyTS7SzV4?t=381))
- Startup School seating of 800 people at a time for 6,000 attendees, done in about 10 minutes for a couple hundred dollars of tokens versus about a month by hand (speaker's estimate) ([10:01](https://youtu.be/eBUyTS7SzV4?t=601))
- Human working memory is about seven items; a 1M-token agent context is about 1,000 pages, or about three Harry Potter books ([11:18](https://youtu.be/eBUyTS7SzV4?t=678))
- The speaker's personal brain holds about 220,000 pages, written mostly by agents from email, meetings and 20 years of notes ([12:45](https://youtu.be/eBUyTS7SzV4?t=765))
- A friend's repo of 80,000 markdown files serves as a company brain for one child's rare medical condition ([18:20](https://youtu.be/eBUyTS7SzV4?t=1100))

## Hot takes
- The productivity gap is about how work is wired, not about which model is used.
- Every company will need a company brain, and its memory layer is an open opportunity.
- Model quality is rented, but the brain you build is owned.
- If you have to ask for the same thing twice, you failed.
- Non-engineers, such as a finance manager who merged 100 Excel workbooks into one app, are now managers of agents.

## Tools mentioned
Claude Code, Codex, OpenClaw, Hermes agent, GBrain, Postgres, TypeScript, Markdown skill files

## Relevance to our work
- **agentos** (2/3): SkillForge's open question is the success signal and skill-worthiness scoring. The talk's signal is the human accepting output at task end, and MemoryMesh's hot/cold promotion and pruning mirror the library/librarian split. → *Prototype a skillify step in SkillForge: when a session ends with the user accepting the output, draft a skill from its steps, run a trigger eval, and test acceptance as the success signal.*
- **prosharness** (2/3): The resolver table plus trigger-eval pattern maps to ProsHarness's context and skill loading around the Claude Code CLI. → *Add trigger evals to ProsHarness: for a set of task types, assert that the expected context or skill file is loaded, and log misses over time.*
- **general** (2/3): The latent-vs-deterministic split and keeping large state out of the context window apply to entity-resolution and data-quality pipelines. → *In any LLM pipeline with matching, ranking or assignment, keep state and combinatorial logic in code and pass the LLM only the judgment calls; check whether any step currently holds bulk state in the prompt.*
