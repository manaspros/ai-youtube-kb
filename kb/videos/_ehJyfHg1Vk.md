# The Era of Compound Engineering — Kieran Klaassen, Every/Cora

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_ehJyfHg1Vk` · [watch](https://youtu.be/_ehJyfHg1Vk) · **date:** 2026-09-18 · **length:** 20:38 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kieran Klaassen · **orgs:** Every, Cora
- **topics:** skills-self-improvement, claude-code, software-factory, context-engineering · **tags:** compound engineering, knowledge extraction, CLAUDE.md, solution docs, unattended agent loop, PR review, postmortem traces, human-AI sandwich, Claude Code plugin, Cursor, Codex, Rails, React, Linear, Slack, Intercom, GitHub

> Kieran Klaassen (Every/Cora) on compound engineering: extract your judgment and repeated corrections into repo knowledge so each feature makes the next one easier, with a demo of his open-source plugin's commands.

## Summary
Kieran Klaassen, who builds the Cora email client largely alone with AI, argues that implementation is now cheap and the real bottlenecks are judgment, taste, and repeated explanation. He describes a loop of brainstorming, planning, working, reviewing, polishing, compounding, and repeating, where the human's effort sits at the start (choosing the problem) and the end (raising the bar), with the AI doing the middle. His rule is to spend about half of each cycle on the feature and half on teaching the system what went wrong, storing the learnings as solution documents in the repository. He claims this is more token efficient over time because the answers are already in context. The second half is a demo of his open-source Compound Engineering plugin, with commands for ideation, document review, brainstorming, an unattended end-to-end run (/lfg), PR polish, and knowledge capture. The talk is a solid practitioner account, though it leans partly on promotion of his plugin and Cora, and it gives few hard metrics.

## Key ideas
- **The bottleneck has moved from code, to plans, to deciding what to build, and finally to judgment and taste.** — He says code was the first bottleneck, then plans, then deciding what to build. Repeating the same instructions led him to build a memory system, which he calls the origin of compound engineering. He argues implementation is mostly solved, while judgment and taste are not. ([4:08](https://youtu.be/_ehJyfHg1Vk?t=248))
- **Extract judgment into a system so the next run already includes it.** — Brainstorming and taste calls should be captured in the system. Then the next AI pass starts from that thinking, so the human can move on to bigger problems. One engineer with a compounding system, in his view, can beat full teams without one. ([5:29](https://youtu.be/_ehJyfHg1Vk?t=329))
- **Put human judgment at the two ends of the loop and let AI run the middle.** — The human decides the problem at the start and sets the quality bar at the end. The middle should run unattended for hours. He suggests keeping a 50/50 split: half of the time on the feature, half on teaching the system whatever it got wrong. ([6:51](https://youtu.be/_ehJyfHg1Vk?t=411))
- **Store extracted learnings as solution documents in the repo.** — Each lesson is saved in the repository, so future runs can find it. He argues this cuts later review, correction, and deep-research work, which makes it more token efficient in the long run. ([8:15](https://youtu.be/_ehJyfHg1Vk?t=495))
- **Document the reasoning and decision traces, not only the code.** — Reasoning matters because code is only the artifact. Traces of who or what made which decision help in postmortems, and can be turned into learnings that change behavior next time. ([17:01](https://youtu.be/_ehJyfHg1Vk?t=1021))
- **Aim for the next feature to be easier because this one shipped.** — He reverses the usual pattern where each feature adds complexity. The standard he sets is that each shipped change should make the next one easier to build. ([19:39](https://youtu.be/_ehJyfHg1Vk?t=1179))
- **Use the repeat-yourself signal as the trigger for extraction.** — Whenever he repeats an instruction, he asks the system to store it. The stated rule is to extract and never repeat, and to keep doing the manual loop until a multi-hour run comes back good without intervention. ([17:01](https://youtu.be/_ehJyfHg1Vk?t=1021))

## Techniques
- **Compound engineering loop** — Run brainstorm, plan, work, review, polish, compound, and repeat as a cycle. Human judgment comes first and last, and the compound step saves new learnings to the repo after each cycle. *When:* Recurring feature work where the same corrections keep coming up across sessions.
- **Ideation against strategy docs** — Pull open tickets from Linear, GitHub, Slack, or Intercom, then score the candidate ideas against the OKR or strategy document and past learnings stored in the repo. Output a shareable HTML page. *When:* Choosing what to work on next, when the backlog is messy and the team needs a ranked, aligned view.
- **Doc review for sharp questions** — Run a review command on a PRD or design doc to get pointed questions. Answer them, then run the compound step so the answers become part of the knowledge base and are not asked again. *When:* Before implementation starts, to surface gaps in a spec.
- **Brainstorm with minimal questions** — The brainstorm command loads compound knowledge and personas, asks only as many questions as needed, and writes a plan document that is stored in the repo. *When:* Before a large change, when you want a plan without a long interview.
- **Unattended end-to-end run (/lfg)** — A single command runs planning, work, review, and testing for hours, dogfoods the result, fixes problems, and opens a PR with before and after video or screenshots. *When:* Overnight or parallel runs where you review the PR output in the morning.
- **PR polish with explanation** — Give the tool a PR. It explains what the flow introduced and shows the product side by side, so the reviewer can judge the result rather than just the diff. Fixes found this way are captured with the compound step. *When:* Final human review, to set the quality bar on UI and product work.
- **Extract a design rule from a review fix** — When a review finds a problem, such as two logo marks on one page, the compound step records the rule and the file it applies to, so future design work avoids it. *When:* Recurring design or style mistakes that a model keeps making.

## Numbers
- Plugin used by hundreds of thousands of people daily (speaker's figure). ([9:35](https://youtu.be/_ehJyfHg1Vk?t=575))
- Cora rebuild started in January, built by one engineer with design and database support. ([2:46](https://youtu.be/_ehJyfHg1Vk?t=166))
- Speaker has been doing this for about two years. ([0:08](https://youtu.be/_ehJyfHg1Vk?t=8))
- Suggested time split: 50% of effort on the feature, 50% on teaching the system. ([6:51](https://youtu.be/_ehJyfHg1Vk?t=411))
- Unattended runs described as lasting hours, with one example as long as three hours. ([13:23](https://youtu.be/_ehJyfHg1Vk?t=803))

## Hot takes
- He has not written a line of code this year and still ships a product that thousands of people use.
- One engineer with a compounding system beats full teams that use AI without one.
- Research is more token efficient in the long term because the answers are already stored in the context.
- The next feature should be easier to build because you shipped this one, which reverses normal engineering complexity growth.
- Implementation is getting cheaper and judgment is not, so future systems need access to human taste.

## Tools mentioned
Claude Code, Codex, Cursor, Claude Cowork, Linear, GitHub, Slack, Intercom, Rails, React, MCP

## Relevance to our work
- **prosharness** (2/3): The /lfg loop (plan, work, review, test, PR with evidence) and the compound step closely match ProsHarness checkpoint and plan-critique loops, and the speaker's point about extracting learnings from repeated corrections fits a harness that runs for hours. → *Add a compound step to the end of each ProsHarness checkpointed run that writes new learnings to a repo doc, and make the next plan step read that doc; compare the result against the current plan-critique flow.*
- **agentos** (1/3): The compound pattern of storing extracted learnings as repo documents overlaps with the MemoryMesh tiered memory idea, but it is file-based and human-curated rather than retrieval-based, so it is only a weak fit for the AgentOS memory layer. → *Test whether MemoryMesh can ingest a curated solution-doc folder per repo and whether retrieval surfaces those docs before a new task starts.*
