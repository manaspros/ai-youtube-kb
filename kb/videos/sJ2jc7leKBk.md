# I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `sJ2jc7leKBk` · [watch](https://youtu.be/sJ2jc7leKBk) · **date:** 2026-05-18 · **length:** 19:34 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Radek Sienkiewicz · **orgs:** OpenClaw, Obsidian
- **topics:** memory, context-engineering, agent-architecture · **tags:** openclaw, obsidian, personal-agent, knowledge-base, markdown-memory, discord, scheduled-maintenance, incremental-adoption, llm-vs-scripts, agents-md, critical-rules, attention-filtering, inbox-pattern

> An OpenClaw maintainer shows how he grew a personal agent into a life-running system step by step, using an Obsidian knowledge base, scheduled maintenance and channel-per-job routing, plus its failure modes.

## Summary
Radek Sienkiewicz, an OpenClaw maintainer, describes how he gave a personal agent access to his email, notes, files, calendar and computer over time rather than all at once. He started with one chat channel (WhatsApp, later Telegram, then Discord) and one simple workflow, and added steps only after each breakage was understood and guarded against. The core of the setup is a roughly 3,000-note Obsidian vault of markdown files, which the agent searches, tags and links to, with new links dropped into an inbox folder being enriched automatically. An overnight window (about 3 to 6 am) reindexes memory and notes, backs up, and updates the agent software using scripts that verify before restarting the gateway. He splits work so that LLMs handle judgment (reading emails, making connections) while plain scripts handle if-this-then-that tasks. He also covers memory hygiene: critical rules placed high in the agent instruction file, a memory folder with promotion, and the warning that bad memory compounds as the vault grows. He names failure modes: compounding bad memory, brittle 10-step automations, noisy nodes and weak boundaries. He closes by framing the agent as a helper for "future me." The talk is anecdotal and personal and gives few hard numbers, and he says he won't share his exact setup. He also says he saw an Andrej Karpathy post about LLM knowledge bases and found his own setup matched it.

## Key ideas
- **Grow the agent one step at a time** — Start with one channel (WhatsApp, then Telegram, then Discord) and one simple workflow. When something breaks, step back, understand why, add a guard so it does not recur, then add the next step. This is why his setup has not bricked on updates. ([1:09](https://youtu.be/sJ2jc7leKBk?t=69))
- **A plain-markdown knowledge base is the agent's memory** — He has about 3,000 Obsidian markdown notes covering work, personal, tasks, projects, research and an inbox of links. The agent searches them (QMD for Obsidian plus its own memory) and the notes are interlinked, which he calls the main source of value. ([4:30](https://youtu.be/sJ2jc7leKBk?t=270))
- **Inbox-to-knowledge-base ingestion replaces bookmark graveyards** — When a link (tweet, thread, article, video) is dropped into the inbox, the agent reads it, adds tags and context, checks related notes in the vault and adds connections. It then resurfaces older notes when a new related item arrives. ([7:20](https://youtu.be/sJ2jc7leKBk?t=440))
- **Overnight maintenance window keeps the agent fresh** — Between roughly 3 and 6 am the agent reindexes search and memory, backs up the vault, and updates the agent software. Scripts tell it what can break and how to verify before restarting the gateway. He wakes to a summary of email and calendar. ([8:41](https://youtu.be/sJ2jc7leKBk?t=521))
- **Split judgment from deterministic work** — Use the LLM for judgment (understanding an email, finding connections). Use scripts for if-this-then-that jobs where no judgment is needed, and skip the LLM entirely for those. ([14:01](https://youtu.be/sJ2jc7leKBk?t=841))
- **Critical rules must sit high in the instruction file** — Rules placed in the instruction or soul file were still forgotten, so he keeps a critical-rules file and mentions it high in the agents file. His memory moved from one file to a folder, with a promotion step he calls dreaming. ([15:24](https://youtu.be/sJ2jc7leKBk?t=924))
- **Failure modes: bad memory compounds, long automations break** — Memory set up badly compounds as the vault grows into the thousands. 10-step automations will break, so split them or add guardrails. Clean noisy nodes regularly and tighten the boundaries in the soul and agent files. ([16:39](https://youtu.be/sJ2jc7leKBk?t=999))
- **Design the agent for future you** — He frames the goal as making the agent a helper for the future self who has to do the work, so the present self needs to do less each day. ([18:05](https://youtu.be/sJ2jc7leKBk?t=1085))

## Techniques
- **Incremental capability ladder** — Begin with one channel and one simple workflow. For each breakage, roll back one step, find the cause, add a guard so it cannot recur, then add the next capability. *When:* Standing up a personal or internal agent that touches many systems, where a big-bang setup would be hard to debug or could break the machine.
- **Channel-per-job-type routing** — Use a general channel for open conversation. Create a dedicated channel only after a type of conversation recurs enough (inbox, briefing, client work, research, social posting, maintainer work). Keep one rotating playground channel for testing models or workspaces, then promote what works and discard the rest. *When:* One agent serves several kinds of jobs and each needs its own context and history.
- **Link-capture enrichment into a markdown vault** — When a link lands in an inbox folder, the agent summarises it, tags it, checks related notes and adds backlinks, then surfaces older related notes. *When:* You want a reading or bookmark queue to become retrievable, linked knowledge instead of a pile.
- **Verified overnight maintenance** — Schedule a window for reindexing, backup and software updates. Encode in scripts what can break, verify health before the gateway restarts, and keep a rollback path. *When:* A long-running agent needs unattended updates without a broken morning.
- **Deterministic scripts beside LLM judgment** — Route rule-like triggers (payment failed, renewal date reached) to plain scripts. Send only ambiguous items, such as reading an email in project context, to the LLM. *When:* Designing any agent pipeline that mixes rules and judgment, to cut cost and brittleness.
- **Critical-rules block high in the instruction file** — Keep a short critical-rules file and reference it near the top of the agent instruction file, since rules buried in prose got skipped. *When:* The agent keeps forgetting hard constraints that are stated in long context files.
- **Draft-don't-send attention filtering** — The agent flags urgent items using project context, and drafts email replies into a drafts folder for the human to accept, edit or delete. *When:* You want proactive help with communication without giving the agent unreviewed send rights.
- **Routine memory hygiene** — Clean noisy notes regularly, promote recurring memories from a folder, and keep memory in inspectable, editable markdown files. *When:* Memory-backed agents whose stored knowledge grows over months.

## Numbers
- About 3,000 markdown notes in the Obsidian vault, used as the agent's knowledge base ([4:30](https://youtu.be/sJ2jc7leKBk?t=270))
- Nightly maintenance window runs roughly 3 to 6 am ([8:41](https://youtu.be/sJ2jc7leKBk?t=521))
- A Netflix payment failure was caught and fixed within about 5 minutes ([11:32](https://youtu.be/sJ2jc7leKBk?t=692))
- Nine Discord channels map to job types (general, inbox, consulting, video research, briefing, Instagram, YouTube, OpenClaw maintainer, rotating playground) ([12:34](https://youtu.be/sJ2jc7leKBk?t=754))

## Hot takes
- Bad memory compounds: a memory setup that is not right at a few hundred notes becomes a serious problem at thousands.
- Ten-step automations will break at some point, so split them or add guardrails.
- Rules written as prose in the agent file still get forgotten, so critical rules need to be placed high and stated explicitly.
- Use scripts for if-this-then-that tasks and skip the LLM, which should be kept for judgment.

## Tools mentioned
OpenClaw, Obsidian, QMD, Discord, Telegram, WhatsApp

## Relevance to our work
- **general** (2/3): Gives a concrete context-engineering data point: critical rules buried in the agent instruction file were still forgotten, so they were moved up and called out. → *Test whether a short critical-rules block placed near the top of CLAUDE.md, instead of in the body, improves rule adherence in our Claude Code runs.*
- **agentos** (1/3): Shows a markdown, inspectable memory and retrieval setup at real scale, and names memory growth and noisy nodes as the failure modes that matter. Relevant to MemoryMesh's tiered memory and retrieval. → *Build a test on a corpus of thousands of notes (not a demo set) for MemoryMesh retrieval quality and duplicate or stale-node growth over time.*
- **prosharness** (1/3): Overnight scheduled runs with verify-before-restart and the advice to split or guard long multi-step automations match ProsHarness loops and schedules. → *Cap each ProsHarness scheduled run at a few steps with a verify-and-rollback step before any restart, and log which step failed.*
