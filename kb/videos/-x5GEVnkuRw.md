# Structuring the Unstructured - Cedric Clyburn, Red Hat

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `-x5GEVnkuRw` · [watch](https://youtu.be/-x5GEVnkuRw) · **date:** 2026-07-18 · **length:** 20:41 · **format:** demo · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Cedric Clyburn · **orgs:** Red Hat, Linux Foundation, NVIDIA, Hugging Face, IBM, Ollama
- **topics:** data-engineering, rag-retrieval, mcp-and-tools, context-engineering · **tags:** docling, pdf-parsing, document-extraction, layout-analysis, ocr, chunkless-rag, agentic-rag, pydantic, vlm-enrichment, docling-serve, mcp-server, open-source, local-inference

> Red Hat's Cedric Clyburn demos Docling, an open-source local tool that converts messy PDFs into layout-aware Markdown, JSON, or Pydantic data, plus chunkless RAG over a document outline.

## Summary
Cedric Clyburn (Red Hat) argues that most enterprise context is locked in unstructured documents such as PDFs, scans, tables, and diagrams, and that the way these are parsed determines whether downstream RAG or agents answer correctly. He shows failure cases: a simple PDF parser merges columns and truncates tables, and an OCR-garbled term spread into published papers. He presents Docling (a Linux Foundation open-source project) as a local, CPU-capable alternative that combines OCR, layout analysis, and table models to output Markdown, JSON, or Pydantic objects. Live demos cover table export to dataframes, image extraction, bounding-box layout checks, VLM-based figure descriptions via a local Granite model in Ollama, and structured field extraction from an invoice. He then demos "chunkless" agentic RAG, where the index is a Markdown outline of section summaries and the LLM iteratively selects sections to read instead of using embeddings or a vector database. Finally he covers deployment as a docling-serve REST/container service and a Docling MCP server used from a local Qwen model in VS Code. Cost and accuracy claims are mostly the speaker's own, including a relayed Hugging Face comparison.

## Key ideas
- **Context quality is bounded by document parsing. Unstructured enterprise data is the new context layer, and parsing errors propagate into wrong answers.** — Speaker cites a viral case where OCR merged two words from different columns, and the nonsense term then appeared in several published papers. ([2:35](https://youtu.be/-x5GEVnkuRw?t=155))
- **Cheap simple PDF-to-text parsers lose structure. Merged columns, truncated text, and linearised tables make the output unreliable for extraction or validation.** — The speaker shows a fast CPU parser output that is not trustworthy for table questions. Sending raw output to a frontier model is also costly at scale and still non-deterministic. ([3:54](https://youtu.be/-x5GEVnkuRw?t=234))
- **Layout-aware conversion (OCR plus layout analysis plus table and vision models) keeps tables, captions, and figures intact, and runs locally without a GPU.** — Docling exports to Markdown, HTML, JSON, dict, or a Pydantic document model, so structure survives into the data your application uses. ([5:07](https://youtu.be/-x5GEVnkuRw?t=307))
- **Use the parsed document model for targeted extraction. Define a Pydantic schema and pull only the fields you need, such as invoice number, total, and sender.** — This avoids headings and noise in the output when you only need a few values from a long document. ([9:19](https://youtu.be/-x5GEVnkuRw?t=559))
- **Chunkless (agentic) RAG: use the document's Markdown outline with section summaries as the entire index. The LLM picks relevant sections and reads their full text, with no chunker, embeddings, or vector DB.** — On a demo paper with 20 sections, one answer came from a single retrieval iteration. The speaker also tried a 418-section IBM annual report, looping over several rounds. ([14:56](https://youtu.be/-x5GEVnkuRw?t=896))
- **Serve document conversion as a service and expose it via MCP. A REST endpoint in a container or Kubernetes handles bulk ingestion, and an MCP server lets coding agents call conversion tools.** — The MCP server offers conversion, generation, and manipulation tools. The demo connects it to a local Qwen model in VS Code. ([16:22](https://youtu.be/-x5GEVnkuRw?t=982))
- **Cost argument: Hugging Face's comparison (as relayed) reports about 50x lower cost for CPU-based Docling than naive OCR or VLM pipelines when preparing web-scale PDF training data.** — This is the speaker's relayed figure, not independently verified in the talk. ([6:33](https://youtu.be/-x5GEVnkuRw?t=393))

## Techniques
- **Layout-aware PDF to structured document conversion** — Run Docling's pipeline (OCR, layout detection, table structure models) and work with the returned Pydantic document object. Export Markdown, JSON, or DataFrames from it, and use bounding boxes to visually check layout. *When:* Enterprise PDFs with tables, figures, or multi-column layouts, where simple text extraction garbles content, and where data must stay local or air-gapped.
- **Picture enrichment with a local vision-language model** — Configure a picture-description pipeline that sends extracted figures to a local VLM (the demo uses Granite via Ollama's OpenAI-compatible endpoint). Store the description with the figure's caption and embedded text. *When:* Documents where diagrams or photos carry information that retrieval would otherwise miss.
- **Chunkless agentic RAG over a document outline** — Build the index as the Markdown outline with one-line section summaries. On each query, let the LLM choose sections, fetch full section text from the structured document, decide whether it is enough, and iterate (about five rounds in the demo). *When:* Documents with clear heading structure, a bounded corpus, and questions that map onto sections. Speaker presents it as an alternative to vector search, not as a benchmarked replacement.
- **Schema-driven extraction from parsed documents** — Define a Pydantic model for the target fields, run the parsed document through the LLM with that schema, and get typed output instead of free text. *When:* Pulling a few known fields (invoice numbers, totals, party names) from long or noisy documents at scale.
- **Document conversion as a microservice plus MCP tool** — Deploy docling-serve as a container or Kubernetes service with options for OCR, backend, and image annotation. Expose the same conversions to coding agents through the Docling MCP server, registered in the agent's MCP config. *When:* Bulk ingestion of thousands of documents, or when agents such as Claude Code or Cursor need to read PDFs without custom glue code.
- **PII removal model before ingestion** — Run a PII detection model on the parsed document and strip sensitive spans before the content reaches the application or the LLM. *When:* Customer documents that must be scrubbed before indexing or training.

## Numbers
- Frontier model output cost cited as about $30 per million output tokens, used to show how sending raw PDF text to a model gets expensive at scale ([3:54](https://youtu.be/-x5GEVnkuRw?t=234))
- Hugging Face comparison (relayed by speaker): CPU-based Docling extraction is about 50x cheaper than VLM or naive OCR for preparing PDF training data ([6:33](https://youtu.be/-x5GEVnkuRw?t=393))
- Demo PDF (Docling's own research paper, 8 pages): 8 tables extracted ([10:39](https://youtu.be/-x5GEVnkuRw?t=639))
- Chunkless RAG demo: index is an outline of 20 sections on the demo paper; the IBM 2025 annual report has 418 sections ([14:56](https://youtu.be/-x5GEVnkuRw?t=896))
- Agentic retrieval loop runs about 5 iterations in the demo before answering ([14:56](https://youtu.be/-x5GEVnkuRw?t=896))
- Speaker's team at Red Hat processes thousands of product-documentation PDFs with this approach ([6:33](https://youtu.be/-x5GEVnkuRw?t=393))

## Hot takes
- Vector databases and embedding chunkers are not needed for document RAG when the document's own structure can serve as the index.
- A fast, cheap PDF parser is a false economy: its merged and truncated output can make downstream answers wrong without any visible error.
- Open-source CPU-capable pipelines can match or beat VLM-heavy OCR on cost for document ingestion at scale.

## Tools mentioned
Docling, docling-serve, Docling MCP server, Pydantic, Ollama, Granite (IBM model), Qwen (via MLX), Jupyter, VS Code, Kubernetes, uvx

## Relevance to our work
- **agentos** (2/3): MemoryMesh already does knowledge buckets and hybrid BM25 plus pgvector retrieval. Docling offers a layout-preserving ingestion front end and a no-vector outline retrieval pattern that could be compared against it. → *Benchmark Docling conversion on a sample of our own PDFs against the current MemoryMesh ingestion path (table and column fidelity, run time on CPU), and prototype an outline-based retrieval baseline on the same documents.*
- **general** (1/3): Structured extraction to Pydantic and a Haiku-class local model for enrichment fit the cheap-model and data-quality interests, but the talk does not evaluate extraction accuracy. → *If any entity-resolution source data is in PDF form, test Docling plus a small local model to produce typed records, and compare the extracted fields against a text-only parse.*
