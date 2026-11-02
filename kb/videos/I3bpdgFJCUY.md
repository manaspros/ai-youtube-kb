# LLM Knowledge Bases: a practical guide — Ben Holmes, Warp

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `I3bpdgFJCUY` · [watch](https://youtu.be/I3bpdgFJCUY) · **date:** 2026-08-18 · **length:** 21:17 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ben Holmes · **orgs:** Warp
- **topics:** memory, context-engineering, skills-self-improvement, agent-architecture · **tags:** knowledge-base, obsidian, markdown, voice-dictation, wiki-generation, backlinks, tagging, scheduled-agents, cloud-sandbox, graph-visualization, personal-knowledge-management, warp, oz, hubble

> Ben Holmes (Warp) shows a markdown-first personal knowledge base: voice-dictate raw notes, have an agent enrich and link them, generate wikis, run it on a cloud schedule, and build graph views with HTML.

## Summary
The speaker argues that raw notes, captured quickly by voice dictation, are the input for LLM-built knowledge bases. An agent skill called Enrich Note adds tags, a source lookup, a processing timestamp and backlinks to each markdown file. A second step turns a raw folder plus a focus-area description into a wiki of people, concepts, places and organisations. Both steps run on a cloud schedule: the notes folder is synced into a sandbox with the Obsidian Headless CLI, the skill runs, and the result syncs back. The agent also builds a clickable HTML graph view on request, with no tool to install. The talk is a practical workflow demo with a product plug for Warp and oz.dev, and gives few hard numbers.

## Key ideas
- **Raw, rambling capture is the foundation** — The speaker says LLM-generated wikis and visualisations need a lot of raw material. Scrappy voice notes with no formatting are fine, as long as many thoughts get captured in the moment. ([4:30](https://youtu.be/I3bpdgFJCUY?t=270))
- **Voice dictation is the fastest capture method** — He argues that speaking beats typing for getting thoughts down, and recommends a dictation tool with a hotkey and mobile app. He notes that local, on-device models can do this without a subscription. ([2:30](https://youtu.be/I3bpdgFJCUY?t=150))
- **Enrichment is a skill that adds structure to each note** — An agent skill called Enrich Note adds topic tags, a source URL found by web search, an enrichment timestamp, and backlinks to related notes found by key-term search. Each note ends up linked to others. ([5:30](https://youtu.be/I3bpdgFJCUY?t=330))
- **Constrain the agent's tagging to avoid drift** — Tags come from a fixed reference list in a folder. The skill tells the agent to be reluctant to invent new tags, because agents tend to get creative. A new tag is added only when a real pattern shows up. ([6:39](https://youtu.be/I3bpdgFJCUY?t=399))
- **Use a timestamp marker to make repeated runs incremental** — Each enriched note gets a timestamp. On the next run, the agent processes only notes that lack one, so the job can run again and again without redoing work. ([7:47](https://youtu.be/I3bpdgFJCUY?t=467))
- **Wikis are generated from a raw folder and a focus area** — Giving the agent a focus area, the raw folder, and a gist-style description produces a wiki organised into people, concepts, places and organisations, with backlinks to the raw sources. He credits the idea to Karpathy's public gist. ([9:12](https://youtu.be/I3bpdgFJCUY?t=552))
- **Run the knowledge base on a schedule in the cloud** — A cloud sandbox syncs the markdown folder in with the Obsidian Headless CLI, runs the enrich or wiki skill, and syncs the result back. The speaker prefers this to git push and pull, and says a local automation needs the laptop to be open. ([13:17](https://youtu.be/I3bpdgFJCUY?t=797))
- **Agents can build a custom graph view on demand** — He asked an agent to build an HTML and Tailwind graph view of the notes, with clickable nodes. Graphs can also drive a habit chart of how often each topic is written about. No separate tool needs installing. ([17:24](https://youtu.be/I3bpdgFJCUY?t=1044))

## Techniques
- **Enrich-note skill with a processed-timestamp marker** — Stamp each note when an agent enriches it. On later runs, process only notes missing the stamp, so repeat runs are incremental. *When:* Any recurring agent pass over a growing folder of documents, such as tagging, summarising or linking.
- **Controlled tag vocabulary with a no-invention rule** — Keep a reference file of allowed tags. Tell the agent to use only those, to be reluctant to add new ones, and to propose additions for a human to review. *When:* Agent-written labels or categories that must stay consistent, such as tags, registry categories or taxonomy fields.
- **Backlinks via key-term search over a file tree** — The agent greps related notes by key terms and writes links to them at the bottom of each note, building an interconnected graph without embeddings. *When:* A small or medium corpus of markdown where simple search is good enough for linking.
- **Raw folder to wiki generation** — Give the agent a focus description, the raw note folder, and a wiki-style spec. It produces grouped entity pages with backlinks to the raw sources. *When:* Turning scattered notes or meeting logs into browsable per-topic or per-entity pages.
- **Sync-in, run, sync-out cloud schedule** — A cloud sandbox pulls the notes folder with a sync tool, runs a skill-driven prompt, and pushes the changes back. The schedule is set in a cloud automation tool. *When:* Scheduled agent maintenance of a local file workspace when git pull and push is too heavy.

## Numbers
- Average typing or dictation speed is about 200 words per minute (speaker's belief, stated with 'I believe'). ([2:30](https://youtu.be/I3bpdgFJCUY?t=150))
- A paid dictation app with a lifetime fee of about $20 (named 'Voice Inc.' in the auto-captions, which may be wrong). Free, local, open-source alternative named Handy. ([3:35](https://youtu.be/I3bpdgFJCUY?t=215))

## Hot takes
- Voice dictation is the fastest way to get thoughts onto paper, and not enough people use it.
- Raw, scrappy, unformatted notes are fine. Volume of raw material matters more than structure.
- Local cron-style automations need the laptop open, so cloud-scheduled agents are preferable for daily maintenance.
- You no longer need to install a tool for a graph view; the agent can build one in HTML on request.
- Agents tend to invent new tags, so you must explicitly tell them to be reluctant to add any.

## Tools mentioned
Obsidian, Obsidian Headless CLI, Warp, oz.dev, Hubble, Claude, Codex app, Exa, Tailwind CSS, Whisper Flow, Handy, GLM 5.2

## Relevance to our work
- **agentos** (1/3): MemoryMesh already has knowledge buckets and provenance. The talk's enrich-then-wiki pattern (tags, backlinks, timestamp marker over a raw folder) is a simple, cheap way to build similar structure from raw notes. → *Prototype a nightly enrich pass over a sample raw-notes folder with a processed-timestamp marker, then compare retrieval quality against the current MemoryMesh bucket on the same queries.*
- **prosharness** (1/3): ProsHarness has loops and schedules. The timestamp-marker incremental pattern and the sync-in, run, sync-out flow are simple ideas that might fit scheduled runs. → *Check whether ProsHarness scheduled loops skip items already processed, using a marker written to each item, so a rerun only touches new work.*
