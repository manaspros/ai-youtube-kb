# Your Agreements Are a Database You Can't Query — Hiral Shah, Docusign & Sean Sodha, NVIDIA

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_gvamfT8H-w` · [watch](https://youtu.be/_gvamfT8H-w) · **date:** 2026-09-18 · **length:** 18:22 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Hiral Shah, Sean Sodha · **orgs:** DocuSign, NVIDIA
- **topics:** data-engineering, inference-serving, enterprise-adoption · **tags:** document-extraction, table-extraction, VLM, OCR, hybrid-pipeline, agreements, Nemotron, NIM, vLLM, quantization, NVFP4, FP8, CSV-export, batch-vs-latency

> DocuSign and NVIDIA on turning enterprise agreement PDFs into queryable data, using a small layout-aware table extraction VLM (Nemotron Parse) inside a hybrid OCR pipeline.

## Summary
Hiral Shah (DocuSign) and Sean Sodha (NVIDIA) describe how DocuSign's Agreement Manager extracts pricing tables, SLAs and other key terms from unstructured agreements at scale. They argue generic VLMs and text-line extractors break on tables, so DocuSign uses NVIDIA's Nemotron Parse, a roughly 850-900M parameter single-shot model that outputs layout, text, reading order and table structure. The pipeline is hybrid: the table model handles layout and tables, while OCR covers other fields and clauses. They split compute by use case, doing heavy OCR and extraction up front for corpus-wide queries and keeping per-document latency low for ad hoc Q&A. They report the model is about 20x faster than other open models at extracting tables per second, and that a smaller purpose-built model also cut latency and cost. Current deployment is FP16, with FP8 and NVFP4 quantization and multi-token generation named as next steps, and accuracy is being tuned before performance. The talk is partly a product demo and carries some vendor framing, but it gives concrete architecture choices and scale figures.

## Key ideas
- **Generic VLMs and text-line extractors fail on enterprise tables** — Pricing tiers, SKUs, SLAs and rate cards are table-shaped. Line-by-line text readers break the table structure, and the speaker says they tested this. ([3:45](https://youtu.be/_gvamfT8H-w?t=225))
- **Table extraction needs a model built for it** — Nested tables, merged rows and columns and other layout permutations make table parsing hard. NVIDIA and DocuSign built Nemotron Parse focused on table extraction. ([6:14](https://youtu.be/_gvamfT8H-w?t=374))
- **Use a small single-shot extractor, not a large generative VLM** — The model is about 850-900M parameters. One pass takes a document and returns layout, text, reading order and table structure. The speaker calls it an extractor, not a generator, and says it can be served via NIM or vLLM. ([7:21](https://youtu.be/_gvamfT8H-w?t=441))
- **Split compute by use case** — For corpus-wide queries over petabytes, pay the OCR and extraction cost up front so queries are fast later. For single-contract Q&A, process on demand with lower concurrency. Batch sizes, concurrency and where compute is spent change between the two. ([14:56](https://youtu.be/_gvamfT8H-w?t=896))
- **Hybrid pipeline with two routes** — The table model handles layout and tables. OCR still handles other fields, metadata and clauses. Each document goes through both routes. ([14:56](https://youtu.be/_gvamfT8H-w?t=896))
- **Lower context and smaller model mean lower latency and cost at scale** — The speaker ties the smaller model to lower latency and cost when serving millions of agreements. Purpose-built smaller models also reach market faster. ([11:01](https://youtu.be/_gvamfT8H-w?t=661))
- **Accuracy first, then performance** — The model is FP16 today. FP8, NVFP4 (Blackwell), and multi-token generation are the planned speed-ups, but the team is focusing on accuracy first and will push the accuracy-performance Pareto curve after. ([16:09](https://youtu.be/_gvamfT8H-w?t=969))

## Techniques
- **Purpose-built small table-extraction VLM** — Use a small single-shot model that takes a page image and emits layout, text, reading order and table structure in one pass, instead of chaining YOLO-style element detectors with OCR. *When:* Documents are table-heavy and the output must keep table structure, at high throughput.
- **Hybrid two-route document pipeline** — Send each page through a layout/table model for tables and through OCR for free text, fields and clauses, then merge the outputs into one structured agreement record. *When:* Documents mix tables with long prose that still needs text extraction.
- **Offline-heavy vs online-light compute split** — For large corpora, run OCR and extraction in batch ahead of time so queries hit preprocessed data. For ad hoc single-document Q&A, run extraction on demand with a different batch and concurrency profile. *When:* The system serves both bulk analytics across a corpus and low-latency questions about one document.
- **Structured export and API over extracted data** — Store extracted tables against an organization-level data model and expose them as CSV downloads and an API for finance and procurement tools. *When:* Downstream teams need the extracted pricing or SLA tables in spreadsheets or other systems, not just as search results.
- **Benchmark on table extraction and track accuracy vs speed** — Compare open models on a table-extraction benchmark (the speaker names RD-TableBench), and judge each change by accuracy-performance tradeoff. *When:* Choosing or tuning an extraction model before optimizing quantization or decoding.

## Numbers
- DocuSign processes about 1 million agreements per day, with 1.9M paying customers and about 1B users ([1:07](https://youtu.be/_gvamfT8H-w?t=67))
- Deloitte study cited by the speaker: about $2 trillion in negotiated agreement value that no one captures ([1:07](https://youtu.be/_gvamfT8H-w?t=67))
- Nemotron Parse is about 850-900M parameters, a single-shot model ([7:21](https://youtu.be/_gvamfT8H-w?t=441))
- Nemotron Parse extracts tables about 20x faster per second than other open-source models tested ([12:07](https://youtu.be/_gvamfT8H-w?t=727))
- Customer agreement repositories range from about 1,000 agreements to millions ([10:05](https://youtu.be/_gvamfT8H-w?t=605))
- Current model runs at FP16, with FP8 and NVFP4 quantization planned ([16:09](https://youtu.be/_gvamfT8H-w?t=969))

## Hot takes
- Generic VLMs and multimodal LLMs fail on enterprise tables, so a purpose-built small extraction model is the better choice.
- A smaller, purpose-built model is better for enterprises than a large general model because it wins on latency, cost and time to market.
- Agreements are hierarchical, since one agreement governs another, so flat document extraction misses the answer.

## Tools mentioned
Nemotron Parse, Nemotron Retriever, NVIDIA NIM, vLLM, C-RADIO, NVFP4, FP8, Coupa

## Relevance to our work
- **agentos** (1/3): MemoryMesh ingests knowledge buckets from documents. Table-heavy PDFs could be poorly handled by text-only ingestion, and this talk gives one architecture for layout-aware ingestion. It is not a direct change to AgentOS. → *When MemoryMesh ingestion meets table-heavy PDFs, compare a layout-aware extractor against the current text path on a small set of pricing or SLA tables and record the accuracy.*
- **general** (1/3): The offline-heavy versus online-light split is a reusable design choice for any pipeline that serves both corpus queries and single-document questions. → *For any ingestion pipeline that serves both bulk and per-document queries, separate the preprocessing budget from the query-time budget and set batch and concurrency settings separately for each.*
