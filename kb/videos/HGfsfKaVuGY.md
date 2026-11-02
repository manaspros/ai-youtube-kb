# Parsing the Epstein Files for JMail — Palak Agarwal & Omar Alhait, Reducto

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `HGfsfKaVuGY` · [watch](https://youtu.be/HGfsfKaVuGY) · **date:** 2026-10-12 · **length:** 29:29 · **format:** workshop · **quality:** 2/5 · **depth:** intro
- **speakers:** Palak Agarwal, Omar Alhait · **orgs:** Reducto, Harvey, Scale, Benchmark, NVIDIA
- **topics:** data-engineering, evals, product-ux · **tags:** document-parsing, structured-extraction, ocr, schema-design, redaction, entity-linking, citations, benchmarking, epstein-files, jmail, reducto

> Reducto staff show how their parse-then-extract pipeline turned 3M+ messy Epstein-file PDFs into the JMail sites, then run a hands-on extraction exercise.

## Summary
Palak Agarwal (Reducto developer relations) and Omar Alhait (Reducto founding engineer) present Reducto as a document-parsing layer that sits before an LLM and turns scanned, rotated, handwritten or chart-heavy PDFs into structured data. They describe how Reducto parsed the Epstein-file corpus for JMail, a Gmail-style site built in about five hours, and how the same parsed corpus was reused for several spin-off products such as a flights tracker. The core workflow they show is parse first, then write an extraction schema, check results on a few documents in Reducto Studio, and deploy the pipeline as an API call. They explain that Reducto rasterizes pages like a human reader and uses an agentic OCR loop that flags and corrects uncertain spots, plus a separate citation step that links extracted values back to their source location. Their advice on evaluation is to start with vibe checks in Studio, then move to 100 and 1,000 documents with systematic measurement, and to build your own benchmark because public numbers will not reflect your documents. The talk is mostly product demo and sales framing, with a few concrete details on schema limits and failure modes, and it ends with a 30-minute hands-on exercise.

## Key ideas
- **Parse first, then extract many products from one parsed corpus** — Reducto parses each document once, then runs separate extraction configs on the parsed output. The speaker says one ground-truth corpus was reused to launch several products, including JMail, a flights tracker, and others. ([5:04](https://youtu.be/HGfsfKaVuGY?t=304))
- **Rasterize the page and read it like a human, with an agentic OCR loop** — The approach works on page images rather than the embedded text layer. The model flags uncertain regions, corrects them, and then moves on, instead of making one pass and committing to an answer. ([1:23](https://youtu.be/HGfsfKaVuGY?t=83))
- **Schema-first workflow with visual checking before deploy** — Write an extraction schema, run it on a few real documents in Studio, judge whether the output looks right, then deploy as an API call or pipeline snippet. The speaker calls the schema the main lever that shapes the output. ([9:15](https://youtu.be/HGfsfKaVuGY?t=555))
- **Generate the schema after parsing for nuanced documents** — The default schema generator is a quick LLM call from the prompt alone. For more nuance, parse the documents first, then generate schema descriptions tailored to their actual content. The speaker recommends the default for a quick look and the enhanced path for accuracy. ([13:00](https://youtu.be/HGfsfKaVuGY?t=780))
- **A box drawn over a PDF is not redaction** — Redacted PDFs can still carry the original text or metadata underneath. The Gmail team had to do their own re-redaction on some files, and the speaker says the parser's ability to read through these was a problem for them. ([13:00](https://youtu.be/HGfsfKaVuGY?t=780))
- **Source attribution is a separate model pass** — After extraction, a separate citation model works out where each extracted value came from in the document. The speaker also points to an NVIDIA paper on speeding up citation lookup. They describe this as post-processing that links entities together. ([16:05](https://youtu.be/HGfsfKaVuGY?t=965))
- **Long-context extraction is many needles, not one** — The speaker says extraction across long documents is a harder problem than needle-in-a-haystack retrieval because every field may be a needle. Reducto trains on data types where long-context recall performs poorly. ([21:11](https://youtu.be/HGfsfKaVuGY?t=1271))
- **Eval ladder from vibe checks to systematic benchmarks** — Start with a small set and check outputs by eye in Studio. Scale to 100, then 1,000 documents with a systematic measure. Customers usually run their own head-to-head bake-offs, and the speaker says wrong configs often skew those results. ([22:15](https://youtu.be/HGfsfKaVuGY?t=1335))

## Techniques
- **Parse-then-extract pipeline** — Run a layout-aware parse once to get structured content, then attach extraction schemas or other downstream steps (split, classify, edit) to that parsed output instead of re-reading the raw PDF each time. *When:* Several products or extraction tasks need the same messy document corpus, or you want to change extraction logic without re-parsing.
- **Agentic OCR with self-correction** — Let the vision model flag low-confidence regions, correct them in a second step, and only then continue, instead of a single pass that commits to its first reading. *When:* Scans, handwriting, rotated pages or dense tables where a single OCR pass produces errors that propagate downstream.
- **Schema review in a playground before deploy** — Draft a JSON-style schema, run it on a handful of real files, inspect the output by eye, adjust field descriptions, then export the working config as an API call or pipeline snippet. *When:* Designing extraction for a new document type, before scaling to large batches.
- **Content-aware schema generation** — Parse the documents first, then have an LLM write field descriptions based on what the parsed content contains, rather than generating the schema from the prompt alone. *When:* Documents vary in layout or vocabulary and generic field descriptions give poor results.
- **Separate citation pass** — Keep extraction and source-location as two model calls, where the second maps each extracted value back to a region of the page. *When:* Users need to verify each extracted value against its source in the document.
- **Per-use-case prompts on specialized sub-models** — Attach custom system prompts to specific pipeline stages, such as a layout prompt for construction blueprints or a figure prompt for logo images, so each document type gets tailored processing. *When:* A single generic pipeline underperforms on one document family, such as drawings or logos.
- **Tiered evaluation with your own benchmark** — Begin with a few documents and manual inspection, move to 100 documents, then 1,000 with systematic metrics. Test with the exact config you will ship, since the speaker says wrong configs distort vendor comparisons. *When:* Choosing or validating a document extraction provider on your own data.

## Numbers
- Reducto has raised $108M over the last three years and has processed over 2 billion documents ([0:12](https://youtu.be/HGfsfKaVuGY?t=12))
- The Gmail-style JMail site was built in about five hours after the files were released ([1:23](https://youtu.be/HGfsfKaVuGY?t=83))
- JMail reached over 450M visits and 18M users by February ([2:28](https://youtu.be/HGfsfKaVuGY?t=148))
- Reducto parsed over 3M pages of redacted, scanned and messy government PDFs for JMail ([2:28](https://youtu.be/HGfsfKaVuGY?t=148))
- One customer-style extraction schema had 156 fields, and the speaker says nesting depth is limited to roughly 4 to 5 layers ([14:38](https://youtu.be/HGfsfKaVuGY?t=878))
- The hands-on exercise was given about 30 minutes ([27:10](https://youtu.be/HGfsfKaVuGY?t=1630))

## Hot takes
- Vendor claim: rasterizing the page and reading it like a human beats relying on the embedded text layer for messy enterprise documents.
- Speaker advice: build your own benchmark, because customers' head-to-head tests on the wrong configs often mislead them and public benchmarks will not show how a tool performs on your documents.
- Speaker quote on the Gmail work: the parser was working a little too well, which exposed weak redactions in the source files.

## Tools mentioned
Reducto Studio, Reducto parse, split, extract, edit and classify APIs, Claude Code or Codex (paste-in setup instructions via a QR code, per the speaker)

## Relevance to our work
- **agentos** (1/3): The parse-then-extract split is a possible ingestion stage in front of MemoryMesh knowledge buckets for scanned or messy documents, but the talk does not address retrieval or memory. → *Note the parse, then schema extraction, then citation sequence as a candidate ingestion design for MemoryMesh; no change needed until document ingestion is on the roadmap.*
- **general** (1/3): Entity linking, source citation and tiered eval ladders apply to the entity-resolution and data-quality work the user follows, but the talk is about documents, not record matching. → *Borrow the 100-then-1,000-document eval ladder and per-value source-location check when measuring LLM extraction quality on the entity-resolution work.*
