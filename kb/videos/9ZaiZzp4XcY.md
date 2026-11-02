# Microsoft Just Solved Document Ingestion for AI Devs (MarkItDown)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `9ZaiZzp4XcY` · [watch](https://youtu.be/9ZaiZzp4XcY) · **date:** 2026-05-02 · **length:** 6:17 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Microsoft, Microsoft Research
- **topics:** rag-retrieval, data-engineering, mcp-and-tools · **tags:** markitdown, document-ingestion, pdf-to-markdown, rag, markdown, llm-preprocessing, image-description, pandoc, docling, unstructured, mcp, python, openai

> Short intro to Microsoft's MarkItDown, an MIT-licensed Python tool and CLI that converts Office files, PDFs, images and audio into LLM-friendly Markdown, with a trade-off note against Pandoc, Unstructured and Docling.

## Summary
The presenter argues that RAG and agent failures often come from document ingestion, not the model: stacked per-format libraries lose table structure and headings and inflate token counts. He demos MarkItDown, a Microsoft Research Python tool (MIT licensed, 110k+ GitHub stars), which converts Word, PowerPoint, Excel, PDF, audio, images and links to Markdown with a single call. The CLI example converts a PDF to a .md file, and a Python example passes a PNG chart through an OpenAI client so an LLM describes it as Markdown. The video says MarkItDown also ships an MCP server for clients such as Claude Desktop. He positions it against Pandoc (built for human publishing), and against Unstructured and Docling (heavier ML-based tools better for complex scans). The stated limits are that dense tables and odd layouts still break it, and that image description needs an LLM plugged in. No benchmarks or measured token savings are shown.

## Key ideas
- **Most RAG and agent quality problems start at ingestion: bad extraction produces bad Markdown, which produces bad answers.** — The presenter frames the problem as fixing the input, not swapping the model. The claim is that better inputs yield better outputs. ([0:00](https://youtu.be/9ZaiZzp4XcY?t=0))
- **Stacking one library per file format is fragile and costly.** — Per-format scripts lose table structure and headings, token usage grows, and the developer ends up debugging ingestion instead of shipping. ([0:59](https://youtu.be/9ZaiZzp4XcY?t=59))
- **MarkItDown provides one tool for many formats.** — It covers Word, PowerPoint, Excel, PDF, audio, images and links, is MIT licensed, comes from Microsoft Research, and has an MCP server. ([3:05](https://youtu.be/9ZaiZzp4XcY?t=185))
- **Output is token-efficient Markdown that keeps structure.** — The claim is less noise in the context window and better downstream answers. The video shows structure surviving on one PDF but gives no measurements. ([4:18](https://youtu.be/9ZaiZzp4XcY?t=258))
- **MarkItDown trades extraction depth for speed and simplicity.** — Pandoc targets human publishing, and Unstructured and Docling use ML models with more setup. The presenter picks MarkItDown for most files and the heavier tools for complex scanned documents. ([4:18](https://youtu.be/9ZaiZzp4XcY?t=258))
- **Known limits remain.** — Complex PDFs, dense tables and unusual layouts can still break extraction. Image descriptions require plugging in an LLM. ([5:20](https://youtu.be/9ZaiZzp4XcY?t=320))
- **Charts and images can be turned into Markdown summaries through an LLM.** — The demo passes a PNG chart with an OpenAI client into MarkItDown, which returns a text summary of the chart's data for retrieval. ([1:58](https://youtu.be/9ZaiZzp4XcY?t=118))

## Techniques
- **Single-tool ingestion to Markdown (CLI)** — Install with pip in a virtualenv, then run the CLI on a file and write the output. The caption reads 'markitdown doc.pdf -o output.md'; the -o flag is inferred from the auto-captions and is not confirmed. Check the README for exact syntax. *When:* A mixed set of Office files, PDFs and similar documents feeds a RAG index or agent knowledge base, and you want to avoid maintaining per-format parsers.
- **Python conversion with an LLM for images and charts** — Create an OpenAI client with an API key and model, create a MarkItDown object wired to that client and model, then call the convert function on a PNG. The output is a Markdown description of the chart's content. The exact constructor argument names are not spoken in the video. *When:* Documents contain charts or images with no usable text layer, and you can afford an extra LLM call per image.
- **Pick the extractor by document difficulty** — Use MarkItDown by default for speed and low setup. For messy scans or dense tables, switch to a heavier ML-based parser such as Docling or Unstructured, or combine them. *When:* Deciding the ingestion layer for a RAG or agent pipeline. The presenter recommends MarkItDown for most files and heavier parsers for complex PDFs.

## Numbers
- MarkItDown has over 110,000 GitHub stars. ([0:08](https://youtu.be/9ZaiZzp4XcY?t=8))
- Integration is described as roughly one line of code. ([0:08](https://youtu.be/9ZaiZzp4XcY?t=8))
- The tool is MIT licensed, from Microsoft Research, and built for LLM workflows. ([3:05](https://youtu.be/9ZaiZzp4XcY?t=185))
- Speaker says the tool takes hours of wasted time per week off developers. This is an unquantified claim, not a measurement. ([0:59](https://youtu.be/9ZaiZzp4XcY?t=59))

## Hot takes
- The title says Microsoft 'solved' document ingestion, but the video is a six-minute demo with no benchmarks for extraction accuracy or token savings. Quality is capped at 2 for hype title plus thin substance.
- 'Better inputs equals better outputs' is the central thesis and is asserted, not tested.
- Image description requires an LLM call per image, so the cost is not zero.

## Tools mentioned
MarkItDown, Pandoc, Unstructured, Docling, OpenAI Python client, Claude Desktop (transcript says 'Claw Desktop', auto-caption error), pip, MCP server (MarkItDown's)

## Relevance to our work
- **agentos** (2/3): MemoryMesh ingests knowledge buckets for hybrid BM25 and pgvector retrieval. A lightweight normalizer to Markdown before chunking is directly relevant, though the video offers no measurements. → *Benchmark MarkItDown as a pre-chunk normalizer for MemoryMesh knowledge buckets. Compare its output with the current extractor on a set of table-heavy PDFs, measuring retrieval quality (for example RAGAS faithfulness) and tokens per document.*
