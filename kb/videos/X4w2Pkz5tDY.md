# Grep or Embeddings? Agentic Search Over Company Documents — George He, LlamaIndex

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `X4w2Pkz5tDY` · [watch](https://youtu.be/X4w2Pkz5tDY) · **date:** 2026-10-07 · **length:** 23:22 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** George He · **orgs:** LlamaIndex
- **topics:** rag-retrieval, context-engineering, data-engineering · **tags:** agentic-search, grep, hybrid-search, bm25, reranking, document-parsing, multimodal-documents, page-screenshots, metadata-filtering, permissions, index-freshness, llamaindex, llamaparse, turbopuffer, claude-code

> George He (LlamaIndex) argues that agent document search should be a harness of primitives (list, grep, read by offset, semantic search, page screenshots) chosen by corpus scale, not a single RAG pipeline.

## Summary
George He, head of engineering at LlamaIndex, compares grep-style local file traversal with embedding and pre-indexed retrieval for enterprise document search. He says Claude Code works without an index because code is small, text-based and well-linked, but company data (mixed PDFs, slides, scans, schematics, permissions) breaks that assumption. His rule of thumb is that 100 to 1,000 files can be searched locally, while thousands or millions need an index. He recommends a harness that gives the agent a few tools, with hybrid BM25 plus vector retrieval as a compass, then grep and offset reads to ground answers. Documents should be parsed once into markdown, with page screenshots stored alongside, and metadata tagged at ingest. The live demo searched 135 Alphabet financial report files and showed the agent reading chunks by offset rather than downloading whole files. The talk is a vendor-flavored practitioner walkthrough (LlamaParse, Turbopuffer), with few hard benchmark numbers.

## Key ideas
- **Agents do not need a vector index for small local code, and Claude Code dropped one.** — The speaker says Claude Code tried a vector database and dropped it, mainly for sync and maintenance reasons. Code is small, text-based, and full of import and test breadcrumbs, so grep and read work well. ([2:59](https://youtu.be/X4w2Pkz5tDY?t=179))
- **Company document sets break the code assumptions.** — Company data has no clean folder structure to grep, mixes PDFs, images and slides, has complex access rules, and changes often. Freshness is hard to keep when indexing complex files, which he says is one reason some companies have given up on pre-indexing. ([4:00](https://youtu.be/X4w2Pkz5tDY?t=240))
- **Corpus scale decides the retrieval approach.** — His rough guide: 100 to 1,000 files can stay with local file search inside the agent's context. Thousands or millions of files need a retrieval index so the agent does not burn tokens iterating over names or reading files each time. ([5:25](https://youtu.be/X4w2Pkz5tDY?t=325))
- **Give the agent a harness of primitives instead of choosing a method by hand.** — Rather than deciding between hybrid RAG and file traversal, expose tools: list or filter files by metadata, semantic search to narrow the set, grep for keywords, read with offset and length, and view page screenshots. The agent then picks the path for each query. ([8:09](https://youtu.be/X4w2Pkz5tDY?t=489))
- **Use retrieval as a compass and file reads for grounding.** — Semantic or keyword search gives the rough direction. The agent then greps and reads inside the chosen files so answers are grounded in actual text instead of hallucinated. Fusion of keyword and vector results is preferred over either alone, with an LLM rerank of the top candidates. ([10:52](https://youtu.be/X4w2Pkz5tDY?t=652))
- **Pre-parse documents once and keep screenshots next to the text.** — Charts, scans and schematics are not plain text. He recommends parsing to markdown or another structured form that keeps table and spatial layout, and storing a rendered page image for each page so the agent can check what a human would see. ([13:19](https://youtu.be/X4w2Pkz5tDY?t=799))
- **Sync has three stages, and metadata and permissions go into the vector store at ingest.** — Pipeline stages: ingestion into one synchronized system, parsing to a standard format, then indexing and export. Layered storage (persist to disk, serve from a memory layer) scales to tens of millions of documents in his multi-tenant experience, and metadata tags are written at ingest so filtering and permissions happen in the store. ([16:08](https://youtu.be/X4w2Pkz5tDY?t=968))
- **Remote files can be read in chunks without downloading the corpus.** — In the demo, grep finds a pattern in a file, then a read with an offset and a max length returns just that slice (his example: skip 500 characters, read 1,000). The agent works against remote storage without pulling whole files into context. ([19:41](https://youtu.be/X4w2Pkz5tDY?t=1181))

## Techniques
- **Agent retrieval harness with a small primitive set** — Expose list-by-metadata, semantic search, grep, read-with-offset-and-length, and page-screenshot view as tools. Let the agent chain them, narrowing from metadata to semantic results to grep to exact reads. *When:* Corpus is large or mixed-format, and you do not want to hard-code whether a query goes to RAG or to file traversal.
- **Hybrid retrieval with weighted fusion and LLM rerank** — Run keyword (BM25) and vector search, fuse the results with an adjustable weight, take around the top 100, and rerank them with an LLM or a deeper model. *When:* Enterprise search where neither exact keywords nor semantic similarity alone is reliable; the speaker recommends hybrid as the default.
- **Parse once, persist, and store page screenshots** — During pre-parsing, convert each document to markdown or text that keeps tables and layout, and save a rendered image of each page. Store both so the agent never re-reads raw binaries. *When:* Documents are PDFs, slides, scans or schematics where text extraction loses layout or meaning.
- **Metadata tagging at ingest** — Attach fields such as year, company and access permissions when documents are ingested, and push them into the vector store so filtering happens before retrieval. *When:* Corpus is large and multi-tenant, or users have different access rights to documents.
- **Chunked reads with grep then offset and length** — Grep for a regex to locate a passage, then read a slice at a given offset with a maximum length, rather than loading the whole file. *When:* Files are large or remote and the agent needs exact context around a match.
- **Evaluate parsers on table and layout fidelity** — Check whether the OCR or parsing output keeps table structure and the original layout, since downstream LLM reasoning depends on it. *When:* Choosing or comparing OCR and document-parsing tools such as Textract, Tesseract or LlamaParse.

## Numbers
- Local file search is appropriate for roughly 100 to 1,000 files; thousands to millions need retrieval. ([5:25](https://youtu.be/X4w2Pkz5tDY?t=325))
- Context windows have grown from 100K to 200K to 1M tokens (the speaker's recollection of model progress). ([5:25](https://youtu.be/X4w2Pkz5tDY?t=325))
- Hybrid retrieval is combined with a rerank of about the top 100 results. No benchmark figures are given. ([10:52](https://youtu.be/X4w2Pkz5tDY?t=652))
- Layered storage was tested at the multi-tenant level, scaling to millions to tens of millions of documents. ([16:59](https://youtu.be/X4w2Pkz5tDY?t=1019))
- Demo corpus: 135 files derived from Alphabet financial reports, mixing HTML and PDF. ([18:22](https://youtu.be/X4w2Pkz5tDY?t=1102))
- Example read: offset 500 characters, then read 1,000 characters. ([19:41](https://youtu.be/X4w2Pkz5tDY?t=1181))

## Hot takes
- Keyword search still has a place for AI agents, not only for developers.
- Claude Code's no-index approach works because code is small and well structured, not because grep beats embeddings in general.
- Pre-indexing is hard mainly because of freshness and sync, and many companies have stopped trying to pre-index complex data.
- Sub-agents for search are token- and latency-heavy, so a pre-built index can be cheaper than repeated sub-agent reads.

## Tools mentioned
LlamaIndex, LlamaParse, LightParse, Turbopuffer, Claude Code, grep, BM25, Textract, Tesseract, MCP, Google Drive, SharePoint

## Relevance to our work
- **agentos** (2/3): MemoryMesh already plans hybrid retrieval (BM25 plus pgvector). The talk's fused-weight and rerank pattern, and the grep and offset-read tools, are direct design inputs for knowledge buckets. → *Add a grep-plus-read-with-offset tool over MemoryMesh buckets and test whether BM25/vector fusion with a top-100 LLM rerank beats the current hybrid on a labelled query set.*
- **prosharness** (1/3): ProsHarness wraps Claude Code, and the talk's advice is to give the agent search primitives instead of a fixed retrieval pipeline. → *When a ProsHarness run has to search a repo or documents, expose grep and offset reads as tools rather than building an index first.*
