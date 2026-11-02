# How to Build a RAG System That Actually Works

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `pvCabUerwss` · [watch](https://youtu.be/pvCabUerwss) · **date:** 2026-02-02 · **length:** 12:48 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus (Better Stack) · **orgs:** Better Stack, LangChain, OpenAI, Qdrant
- **topics:** rag-retrieval, context-engineering · **tags:** rag, chunking, recursive-text-splitter, embeddings, vector-database, qdrant, langchain, prompt-grounding, prompt-injection, text-embedding-3-small, gpt-4o, uv, beautifulsoup

> Better Stack walkthrough of building a RAG system over Star Wars scripts with LangChain, OpenAI embeddings and local Qdrant, focused on scene-aware chunking and prompt grounding.

## Summary
The presenter builds a question-answering RAG over the original Star Wars screenplays, scraped from a script site with requests and BeautifulSoup and loaded as LangChain documents. The main argument is that chunking matters: ingesting a whole script as one document dilutes retrieval, so the splitter is set to break on scene headings (INT./EXT.) first, with 2,500-character chunks and 250-character overlap. Embeddings use OpenAI text-embedding-3-small, stored in a locally persisted Qdrant collection that is only rebuilt when missing. Retrieval pulls the top 15 chunks into a GPT-4o chain at temperature 0. The main practical lesson is that a strict "use only the excerpts" prompt made the bot refuse answerable questions (Luke Skywalker), and the fix was a single line allowing partial answers, which the presenter then re-tested against out-of-scope and prompt-injection questions. The tutorial is short, code-light, and entertaining, with no sponsor segment; it is a solid beginner-to-intermediate primer rather than a benchmarked study.

## Key ideas
- **Do not ingest a whole document as one chunk; the retriever then hands the model too much text and the answer can be missed (lost in the middle).** — Whole-script ingestion dilutes the signal and raises token cost and latency. Chunking is the first real design decision. ([3:28](https://youtu.be/pvCabUerwss?t=208))
- **Split on the document's natural units (scene headings) rather than generic paragraphs.** — RecursiveCharacterTextSplitter with INT./EXT. scene markers first in the separator list, then double newline, single newline and spaces as fallbacks. Target 2,500 characters with 250 overlap so transitions between scenes are not lost. ([4:17](https://youtu.be/pvCabUerwss?t=257))
- **Persist the vector index locally and only rebuild it when the collection is missing.** — Qdrant runs locally, so the indexed scripts survive reruns. The code tries to load the existing collection first and falls back to from_documents only when it is not found. ([6:31](https://youtu.be/pvCabUerwss?t=391))
- **A strict grounding prompt can cause false refusals when the answer is spread across chunks instead of stated in one place.** — 'Who is Luke Skywalker' got a refusal even though the character is everywhere in the scripts; no single chunk defines him. Adding a line to give the best partial answer from the context fixed it. ([9:52](https://youtu.be/pvCabUerwss?t=592))
- **Grounding prompts are tuned by testing, not by reasoning about them in advance; the presenter calls it vibe-based.** — After loosening the prompt, the presenter re-checked an out-of-scope question (Darth Maul should be refused) and a prompt-injection string to confirm the scope still held. ([11:03](https://youtu.be/pvCabUerwss?t=663))
- **Scope limits and prompt-injection resistance in this demo come from the prompt and the retrieval setup, checked by a handful of manual questions.** — The video runs one in-scope, one out-of-scope and one injection probe. It is not a systematic eval set, and it does not measure retrieval recall. ([10:20](https://youtu.be/pvCabUerwss?t=620))

## Techniques
- **Scene-aware recursive chunking** — RecursiveCharacterTextSplitter(chunk_size=2500, chunk_overlap=250) with separators ordered as the scene markers INT. and EXT. first, then double newline, single newline, and space. Loop over each script document, split, and append the chunks to one list. *When:* Screenplays, transcripts, or any structured source where section headings mark self-contained units. Use overlap so boundary content is not lost.
- **Persist-or-build vector store** — Create a local Qdrant client with a fixed path and collection name. Try to open the existing collection first. If it is not found, close any open client and call from_documents with the chunks and the embedding model. *When:* Local prototypes, or any ingestion step that is costly to redo. Avoids re-embedding on every run.
- **Fixed-k retrieval with a deterministic chat model** — Use the vector store as retriever with k=15. Build a template that gives the model the excerpts and the question, then compose the retriever, prompt, model and parser into an LCEL chain. Use GPT-4o with temperature 0. *When:* Grounded Q&A where you want repeatable answers and do not need the model to be creative.
- **Prompt grounding tuned with a scope test set** — Start with a strict instruction: use only the excerpts, and say when the answer is not present. Then add a line allowing the best partial answer from the context. After each change, re-run an in-scope question, an out-of-scope question and an injection string (for example, ignore all previous instructions) to confirm both behaviours. *When:* Any domain-restricted RAG where too-strict refusals and scope leaks are both failure modes. Turn the three probes into a small regression set.

## Numbers
- Chunk size 2,500 characters with 250-character overlap between chunks. ([4:17](https://youtu.be/pvCabUerwss?t=257))
- Retriever returns the top 15 most similar chunks per question. ([7:36](https://youtu.be/pvCabUerwss?t=456))
- Generation temperature set to 0, model GPT-4o. ([7:36](https://youtu.be/pvCabUerwss?t=456))
- Embeddings from OpenAI text-embedding-3-small. ([6:31](https://youtu.be/pvCabUerwss?t=391))
- Video is 12:48 long; three manual probes are run (in-scope, out-of-scope, injection), with no benchmark or quantitative measurement. ([8:25](https://youtu.be/pvCabUerwss?t=505))

## Hot takes
- Strict 'use only the excerpts' prompts over-refuse; a one-line allowance for partial answers is needed in practice.
- RAG prompt tuning is 'vibe-based' and needs repeated manual checks, not a principled method.
- Scene-level chunking beats generic paragraph splitting for structured, narrative sources.
- Whole-document ingestion is a 'strategic error' because of lost-in-the-middle and token cost (asserted, not measured in the video).

## Tools mentioned
LangChain, langchain-openai, langchain-qdrant, qdrant-client, langchain-text-splitters, BeautifulSoup4, requests, uv, Qdrant (local vector database, written in Rust), OpenAI text-embedding-3-small, GPT-4o

## Relevance to our work
- **agentos** (2/3): MemoryMesh knowledge buckets use hybrid retrieval; the scene-aware separator list and overlap idea applies to structured source chunking, and the strict-vs-partial prompt test pattern applies to bucket Q&A. → *Add a small golden set (in-scope, out-of-scope, injection probe) for a MemoryMesh knowledge bucket, and test whether chunk separators that follow the document's own structure beat a fixed-size splitter on it.*
