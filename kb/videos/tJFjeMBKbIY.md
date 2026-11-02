# Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `tJFjeMBKbIY` · [watch](https://youtu.be/tJFjeMBKbIY) · **date:** 2026-08-18 · **length:** 24:23 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Shawn Chan · **orgs:** China Resources Holdings
- **topics:** product-ux, governance-compliance, rag-retrieval · **tags:** trust, provenance, audit-trail, contradictions, fact-vs-guess, finance, human-in-the-loop, demo-vs-memo

> A finance investor argues AI products should be built as auditable memos, not impressive demos. He lists six ways trust breaks and five plumbing fixes: provenance, number agreement, surfaced contradictions, fact/guess labels and human approval.

## Summary
Shawn Chan, who has spent 15 years on cross-border finance deals, says most AI finance products are built to impress in a five-minute demo rather than to survive an investment committee. He contrasts a demo (one clean input, one fluent output) with a memo (built from many conflicting sources and challenged before money moves). He describes six quiet failure modes: treating all sources as equally trustworthy, letting numbers disagree across pages, smoothing over contradictions, blending guesses into facts, having no traceable source for claims, and having no accountable human at the end. His anecdotes (a demo factual error tied to a stock drop, a pricing model that led to a large write-off, fabricated legal citations, an airline chatbot's invented policy) make each point concrete. His five fixes are click-through provenance with source trust levels, separate labels for facts and guesses, automatic number reconciliation, surfaced contradictions, and a locked human approval gate with an audit log. He closes by saying the same discipline that makes a product trustworthy is what gets a founder funded, because investors check the pitch against the data room.

## Key ideas
- **Build for the memo, not the demo** — A demo is one clean document in and one fluent answer out. A memo is built from hundreds of pages of conflicting sources and must survive a skeptical committee. Once real money is watching, every sentence is held to memo standards. ([5:08](https://youtu.be/tJFjeMBKbIY?t=308))
- **Not all sources deserve the same trust** — An audited filing, an analyst note and an internal group-chat message carry different weight. Most retrieval systems grab whatever text is closest to the question and treat it as equally authoritative. The system should know which tier a claim comes from. ([9:00](https://youtu.be/tJFjeMBKbIY?t=540))
- **Numbers must agree with each other** — A growth figure on page 1 that differs from a table on page 11 damages trust in the whole document, even if the gap is small. Consistency checks must be built into the machinery, not left to a human at 2 a.m. ([11:33](https://youtu.be/tJFjeMBKbIY?t=693))
- **Contradictions are signal, not noise to smooth over** — When a CEO's earnings-call number differs from the filing, that gap is the most useful thing to examine. Fluent models tend to pick the nicer version silently. The speaker says the disagreement was caught only because one person had both documents open, which he calls luck, not a control. ([12:34](https://youtu.be/tJFjeMBKbIY?t=754))
- **Keep facts and guesses in separate, visible boxes** — Fluent output melts estimates into fact-shaped sentences, and across rewrites a guess can become an approved fact. The cheap fix is a visible tag on guesses that survives being copied into other documents. ([15:07](https://youtu.be/tJFjeMBKbIY?t=907))
- **A claim must be traceable in one click** — Lawyers filed a brief with six invented court cases, and the chatbot confirmed they were real when asked. The test is whether someone can click from a sentence to its exact source paragraph. The speaker calls that click-through the real product feature. ([17:27](https://youtu.be/tJFjeMBKbIY?t=1047))
- **Every decision needs an accountable human** — An airline tried to blame its chatbot for an invented discount policy and lost at a tribunal. Accountability cannot be outsourced to software, so the architecture should be built around a named person who signs off, with an audit log of who approved what and what changed. ([18:52](https://youtu.be/tJFjeMBKbIY?t=1132))

## Techniques
- **Click-through provenance with source trust levels** — Attach each claim to its exact source paragraph and show the trust level of that source, so any sentence can be verified in one click rather than by searching multiple tabs. *When:* Any AI output that will feed a decision, a document or a report that someone else will read.
- **Fact vs guess labelling** — Tag estimates visibly (colour, marker or text) and make the tag survive copy-paste into other documents. *When:* Generated summaries or memos that mix sourced data with model inference or forecasts.
- **Automatic cross-document number reconciliation** — Compare the same figures across sources and refuse to produce a document where they disagree, instead of relying on a human to catch the mismatch. *When:* Financial or metric-heavy documents assembled from several filings or reports.
- **Surface contradictions instead of resolving them silently** — When sources disagree, raise the conflict to a human reviewer and show both values, rather than letting the model choose the smoother one. *When:* Retrieval over multiple sources where the sources may conflict, such as earnings calls versus filings.
- **Locked human approval gate with audit log** — Require a named human to approve the output, and record who approved it, when, and what changed. *When:* Any agent output where money, legal exposure or a customer commitment depends on it.
- **Accountability-first architecture** — Design the system so a person owns the final decision, rather than framing the model as the decision-maker. *When:* Enterprise or regulated products where liability must sit with a human or organisation.

## Numbers
- A company's stock dropped around 8% in a day after a factual error in a demo, which the speaker puts at roughly $100 billion of value. ([7:58](https://youtu.be/tJFjeMBKbIY?t=478))
- Speaker has sat in about 200 investment committee meetings over 15 years of cross-border deals. ([2:38](https://youtu.be/tJFjeMBKbIY?t=158))
- Example mismatch: revenue growth stated as 18% on page 1 versus 17.4% in a table on page 11. ([11:33](https://youtu.be/tJFjeMBKbIY?t=693))
- A real-estate company's pricing algorithm led to a write-off of around half a billion dollars, the unit was shut down and about a quarter of staff were let go. ([12:34](https://youtu.be/tJFjeMBKbIY?t=754))
- A legal brief cited six court cases that did not exist, all generated by a chatbot. ([17:27](https://youtu.be/tJFjeMBKbIY?t=1047))
- The speaker says six trust-breaking failure modes and five fixes are covered in the talk. ([9:00](https://youtu.be/tJFjeMBKbIY?t=540))

## Hot takes
- A smarter model will not fix trust; plumbing and honesty will decide which AI products win.
- Fluent and confident is not the same as right.
- Luck is not a control: catching a contradiction only because someone had two documents open is not a process.
- The same discipline that makes an AI product trustworthy is what gets a founder funded.

## Relevance to our work
- **agentos** (2/3): MemoryMesh already plans provenance and conflict resolution; the talk's per-source trust tiers, surfaced contradictions and click-through to source are a concrete design checklist for its retrieval output. → *Add a source-trust tier to MemoryMesh retrieval results and have the answer path flag disagreeing sources rather than silently choosing one, then test it with a dataset that contains a deliberate conflict.*
- **prosharness** (1/3): The talk's audit-trail point (who approved what and what changed) maps loosely onto ProsHarness's phone-driven approvals. → *Record approver identity, timestamp and the diff approved for each phone-driven approval in the run log so approvals can be audited later.*
- **general** (1/3): The 'show me where this came from' test and the fact/guess split are cheap review checks for any agent output that feeds a decision. → *Ask for a source link per claim in one agent report and mark model-inferred sentences separately, then check whether the split survives a copy into another document.*
