# Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `gonAewBZxfU` · [watch](https://youtu.be/gonAewBZxfU) · **date:** 2026-10-15 · **length:** 25:02 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Nina Žižakić, Eleonora Drykina · **orgs:** In The Pocket, anonymous Belgian fintech client (payment scheme)
- **topics:** rag-retrieval, evals, agent-architecture, data-engineering · **tags:** rag, hybrid-search, bm25, reciprocal-rank-fusion, table-extraction, section-aware-chunking, agentic-retrieval, citations, promptfoo, llm-as-judge, eval-noise, streaming, pydantic, qdrant, fintech, belgium

> Two In The Pocket engineers describe a RAG assistant over a Belgian payment scheme's rulebooks: section-aware chunking, table flattening, hybrid retrieval, agentic narrow-to-wide tools, and noisy LLM-judge evals.

## Summary
The speakers built a rulebook chatbot for a large Belgian payment scheme, covering about 270 PDFs (roughly 6,000 pages, 3,000 tables) for a fintech client. Answers must cite the exact rulebook, section and page, and must not pull in outside knowledge about other payment schemes. Indexing splits pages into non-overlapping chunks of about 2,000 characters, never splits a table across chunks, tags each chunk with a section path and chunk index, and flattens tables into CSV-like rows so merged cells still map to the right value. Serving runs dense and BM25 retrieval, fuses them with reciprocal rank fusion, and gives the agent four tools ordered narrow to wide, from chunk search up to listing available rulebooks. Guardrails stop oversized rulebooks from being dumped into context, return the available section names on a bad lookup, and ask the agent to avoid repeating failed searches. On the UX side, streaming markdown mattered more than structured UI components, and evals used Promptfoo with an LLM judge, which the speakers found to be noisy. The assistant launched in June to about 34 internal users, with roughly 900 questions across 100-plus conversations.

## Key ideas
- **Citations and grounding are the hard requirements in a regulated RAG** — Every answer must cite the exact rulebook, section and page. The model also has general world knowledge, so the team had to decide which knowledge counts: definitions are fine, but facts about other payment schemes must not appear unless the rulebooks state them. ([2:31](https://youtu.be/gonAewBZxfU?t=151))
- **Keep section structure in the chunks** — Chunks are packed by paragraph to about 2,000 characters with no overlap, so a section is simply its chunks in order. Regex-detected headers give each chunk a section path, which serves both citations and fetching a whole section later. ([7:32](https://youtu.be/gonAewBZxfU?t=452))
- **Tables need their own processing** — Plain PDF text extraction garbled merged cells, so a fee could be read from the wrong row or column. Flattening each table into CSV-like rows with the merged fields duplicated made the agent fetch the correct row and noticeably improved answer correctness. ([10:14](https://youtu.be/gonAewBZxfU?t=614))
- **Hybrid retrieval beats dense-only on this corpus** — Dense embeddings handle meaning but treat rulebook codes and message names as noise, while BM25 handles exact tokens but not paraphrase. Taking the top 50 from each, fusing with RRF (no score calibration needed), reranking for section coherence and passing 10 chunks to the agent raised hit rate from 92% to 97% on 63 questions without losing any dense hit. ([12:55](https://youtu.be/gonAewBZxfU?t=775))
- **Agentic narrow-to-wide retrieval replaces a fixed pipeline** — Some questions span chained rulebooks or need every fee, so a single retrieve-then-generate step is not enough. The agent has four tools, from chunk search to section fetch to full rulebook to a list of available rulebooks, and it usually makes 2 to 4 calls per question. Moving from single-shot to agentic retrieval raised the eval scores by a clear margin. ([13:54](https://youtu.be/gonAewBZxfU?t=834))
- **Tool guardrails make the agent recover instead of spiral** — Rulebooks over about 100k tokens are refused for full-dump and return a section list instead. A wrong section name returns the valid names so the agent can retry. The prompt also asks the agent to check whether a new call is genuinely new or just a rephrased failed search, a fix based on real traces of the agent repeating searches. ([14:47](https://youtu.be/gonAewBZxfU?t=887))
- **Streaming matters more than structured UI** — A first design used Pydantic UI components inside the answer, but a partial Pydantic object is not valid JSON until the last token, so users saw about 38 seconds of nothing. The fix streams markdown prose token by token and appends only the source card, which needs no streaming, after the answer completes. ([16:04](https://youtu.be/gonAewBZxfU?t=964))
- **LLM-judge evals have a noise floor, and the rubric can be the bug** — In one rerun 5 of 12 apparent flips did not reproduce, so the delta must be rerun before it is trusted. A judge also repeatedly punished a date that was real text in the rulebook, so the rubric itself needed fixing. ([18:28](https://youtu.be/gonAewBZxfU?t=1108))

## Techniques
- **Section-path chunking without overlap** — Pack paragraphs into roughly 2,000-character chunks, never split a table across chunks, detect headers with regex to build a section path, and store a chunk index so sections can be rebuilt in order. *When:* Long, structured, cross-referencing documents where citations need section and page, and where the agent sometimes needs a whole section.
- **Table flattening for merged cells** — Convert each table to CSV-like rows and copy the merged-cell values into every row they cover, so each row is self-contained. *When:* Documents where fees, limits or rules sit in tables with spanning cells that plain text extraction garbles.
- **Hybrid dense plus BM25 with RRF** — Query dense and BM25 in parallel (top 50 each) in Qdrant, fuse with reciprocal rank fusion, rerank for section coherence, and keep the top 10. *When:* Corpora that mix paraphrased natural-language questions with exact identifiers such as codes or message names.
- **Narrow-to-wide agent tool ladder** — Expose tools in order: search chunks, fetch a section by path, fetch a full document only if small, and list available documents. The agent starts narrow and widens only when needed. *When:* Questions that need anywhere from one passage to a whole rulebook, where a fixed top-k would miss context.
- **Tool-level recovery guardrails** — Refuse oversized dumps and return a table of contents instead, return valid names on a bad lookup, and add a prompt rule to check whether a repeated search is new before repeating it. *When:* Agent loops where the model otherwise retries the same failing call or invents names.
- **Stream prose, render structured parts last** — Stream markdown token by token and render any structured UI component (such as a source card) after the answer finishes, instead of putting structured output inside the streamed text. *When:* Slow multi-step agent answers, where structured output would otherwise block the whole reply until the end.
- **Lightweight feedback logging** — Store each question, thumbs feedback, UI events such as source click or copy, and the last 20 messages in a plain table, and infer sentiment from follow-up behaviour (thanks or topic change is positive, repeat question is negative). *When:* Early products where thumbs feedback is sparse and usage analytics are enough.
- **Promptfoo end-to-end evals plus retrieval-only eval** — Run about 86 full-agent tests with an LLM judge against a rubric, add a check that the correct source document was cited, and run a separate retrieval-only hit-rate eval. Build test questions from user interviews and behaviour guidelines. *When:* Agent products where answers must be correct, cited and policy-compliant.

## Numbers
- About 270 PDF rulebooks, roughly 6,000 pages and about 3,000 tables in the corpus ([2:31](https://youtu.be/gonAewBZxfU?t=151))
- About 4,000 chunks after indexing; the agent works from about 10 retrieved chunks per query ([11:33](https://youtu.be/gonAewBZxfU?t=693))
- Hybrid dense plus BM25 with RRF raised retrieval hit rate from 92% to 97% on 63 questions, losing no question that dense alone found ([12:55](https://youtu.be/gonAewBZxfU?t=775))
- Dense top 50 plus BM25 top 50 are fused down to 30, then reranked and cut to 10 ([11:33](https://youtu.be/gonAewBZxfU?t=693))
- Median answer latency is about 38 seconds, with 2 to 4 tool calls typical per question ([13:54](https://youtu.be/gonAewBZxfU?t=834))
- Full-rulebook tool refuses rulebooks over roughly 100k tokens ([14:47](https://youtu.be/gonAewBZxfU?t=887))
- About 86 end-to-end Promptfoo tests run with an LLM judge; in one eval 5 of 12 flips did not reproduce on rerun ([18:28](https://youtu.be/gonAewBZxfU?t=1108))
- Launched in June to internal users; about 900 questions across more than 100 conversations from about 34 active people ([19:55](https://youtu.be/gonAewBZxfU?t=1195))
- Conversation context is capped at the last 20 messages ([17:27](https://youtu.be/gonAewBZxfU?t=1047))
- By month 3, more than 90% of questions were real questions rather than red-team attempts ([20:48](https://youtu.be/gonAewBZxfU?t=1248))

## Hot takes
- LLM-judge eval deltas have a noise floor: rerun before trusting any change (5 of 12 flips did not reproduce).
- Sometimes the eval rubric is the bug, not the model: a judge kept punishing a date that was real rulebook text.
- For slow agent answers, streaming plain markdown beats structured Pydantic UI components, which show nothing until the full JSON arrives.
- Agentic multi-call retrieval beat single-shot retrieve-then-generate on their evals by a clear margin.

## Tools mentioned
Qdrant, BM25, Reciprocal Rank Fusion, Promptfoo, Pydantic, LLM-as-judge

## Relevance to our work
- **agentos** (2/3): MemoryMesh already plans hybrid BM25 plus pgvector retrieval. The talk gives measured evidence for RRF fusion, section-path metadata and whole-section fetch, and it shows that exact identifiers need BM25. → *Add a section-path field and a whole-section fetch to MemoryMesh chunks, then measure hit rate for dense-only against RRF hybrid on a small labelled set of questions.*
- **general** (2/3): Two directly reusable practices: rerun LLM-judge evals before trusting deltas, and check the rubric before blaming the model. Both apply to any eval loop. Agentic narrow-to-wide retrieval is also a useful pattern. → *Add a rerun-to-measure-noise step to any LLM-judge eval before accepting a score change, and check the judge rubric against the source text when it flags a fact.*
