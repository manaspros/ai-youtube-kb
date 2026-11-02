# Build A RAG AI System in 5 Minutes with Cloudflare + Firecrawl!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `YxC1zEz5TDY` · [watch](https://youtu.be/YxC1zEz5TDY) · **date:** 2025-11-02 · **length:** 4:05 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Cloudflare, Firecrawl
- **topics:** rag-retrieval, mcp-and-tools · **tags:** cloudflare, autorag, firecrawl, r2, mcp, cursor, bun, markdown-ingestion, vector-search

> Four-minute tutorial wiring Firecrawl-scraped docs into R2, indexing them with Cloudflare AutoRAG, and exposing the index to Cursor through Cloudflare's MCP server.

## Summary
The video builds a small RAG pipeline from a documentation site. Firecrawl crawls up to 15 pages and exports them as Markdown with metadata. A Bun script using the S3-compatible client uploads each page to a Cloudflare R2 bucket, with the title from the page metadata used as the file name. Cloudflare AutoRAG (beta) is then pointed at the bucket, using the "auto" models for embedding and generation, and it builds the vector index for you. The index can be queried by API, from a Worker, or in the playground, which shows per-file relevance scores. Finally, Cloudflare's AutoRAG MCP server is added as a global MCP server in Cursor, so the editor can pull the indexed docs into context. The presenter's test corpus is a small, obscure package's docs, chosen so the base model is unlikely to know it. The video offers no retrieval quality measurements and no latency or cost numbers.

## Key ideas
- **The pipeline is scrape, then Markdown, then object storage, then a managed index, so you skip writing your own embedding and vector-store code.** — The presenter argues the usual chunk-embed-store-retrieve steps are handled by AutoRAG after the data lands in R2. The Markdown conversion happens before indexing, not raw HTML. ([0:00](https://youtu.be/YxC1zEz5TDY?t=0))
- **Firecrawl is used to crawl the docs site and turn each page into Markdown with metadata.** — The crawl is capped at 15 pages and exported as Markdown. Each result has the Markdown body plus metadata such as title, description, language and Open Graph description. The metadata title is used to name the stored file. ([0:00](https://youtu.be/YxC1zEz5TDY?t=0))
- **R2 is the document store because it speaks the S3 API, so the Bun S3 client works with it.** — The client must be given Cloudflare's endpoint explicitly, since it defaults to AWS. The presenter uploads each Markdown page as a separate object. ([1:22](https://youtu.be/YxC1zEz5TDY?t=82))
- **AutoRAG takes the R2 bucket as its source and does the vectorization.** — Setup is a short wizard: connect the bucket, accept the default 'auto' embedding model, accept the default 'auto' retrieval/generation model, then name the RAG. AutoRAG is in beta, and the presenter notes a built-in web crawler is coming and may make Firecrawl unnecessary. ([2:00](https://youtu.be/YxC1zEz5TDY?t=120))
- **The playground shows which files were retrieved and their scores for a query, which helps debug retrieval.** — Results can be read via API or a Worker too, but the playground's per-file scores are the main inspection tool the presenter demonstrates. ([2:47](https://youtu.be/YxC1zEz5TDY?t=167))
- **Cloudflare's MCP servers, including one for AutoRAG, let an editor query the index directly.** — The AutoRAG MCP server is added as a global MCP server in Cursor, after signing in to Cloudflare. The presenter says the answers beat what Claude gives without the docs, but shows only one example. The use cases he names are internal docs, customer conversations exported as JSON, and up-to-date library docs. ([2:47](https://youtu.be/YxC1zEz5TDY?t=167))

## Techniques
- **Crawl a docs site to Markdown with page metadata** — Install the Firecrawl Node package, call its crawl-URL method with the site root, cap the crawl (the example uses a 15-page maximum), and set the output format to Markdown. Keep the metadata title for naming each stored file. *When:* When the source is a documentation site that the base model likely does not know, and you want clean text rather than HTML for indexing.
- **Use R2 as the S3-compatible document store for RAG** — Create an R2 bucket and generate an API token from the dashboard. In Bun, import the S3 client, pass the access key, secret and Cloudflare's R2 endpoint (not the AWS default), then upload each Markdown page with a name derived from its title. *When:* When you want Cloudflare to manage the index and you need a simple bucket that AutoRAG can read from.
- **Index an R2 bucket with AutoRAG using the auto models** — In the Cloudflare dashboard under the AI menu, create an AutoRAG instance, connect it to the bucket, keep the defaults for the embedding model and the generation model, and name it. The index builds from the bucket contents. *When:* When you want managed chunking, embedding and vector storage and can accept beta-level stability and limited control over the models.
- **Expose an AutoRAG index to Cursor as a global MCP server** — Copy the AutoRAG MCP server config from Cloudflare's MCP server list, add it as a global MCP server in Cursor, sign in to Cloudflare when prompted, then prompt Cursor to query the index. The exact config file and keys are not shown in the video. *When:* When an editor agent needs fresh, private, or niche documentation that is not in the base model's training data.

## Numbers
- Firecrawl crawl capped at a maximum of 15 pages in the example. ([0:00](https://youtu.be/YxC1zEz5TDY?t=0))
- Presenter says the whole build takes under five minutes. The video runs 4:05. ([0:00](https://youtu.be/YxC1zEz5TDY?t=0))
- Cloudflare recently released about 30 new MCP servers, one of them for AutoRAG. ([2:47](https://youtu.be/YxC1zEz5TDY?t=167))
- AutoRAG uses the 'auto' model for both embedding and retrieval/generation. No model names, dimensions, chunk sizes or costs are given. ([2:00](https://youtu.be/YxC1zEz5TDY?t=120))

## Hot takes
- The title says 'in 5 minutes' and the presenter says Cloudflare made RAG 'insanely simple'. That is a sales-style claim. The video skips account setup, API token scopes, pricing and beta limits.
- The claim that the AutoRAG answers are 'more accurate than the data coming out of Claude' rests on one query in one Cursor session, with no baseline or eval.
- Test corpus is a tiny, unpopular package's docs, so it shows that retrieval works on new knowledge, not how it behaves on a large or noisy corpus.
- Presenter says a built-in web crawler is coming and 'might replace the need for Firecrawl', so the Firecrawl step may become obsolete.
- Quality is capped at 2: hype title, mostly a vendor product walkthrough, no measurements, and no retrieval quality checks beyond the playground score display.

## Tools mentioned
Firecrawl (Node package, crawl-URL method, Markdown export), Cloudflare R2 (S3-compatible object storage), Bun S3 client, Cloudflare AutoRAG (beta), Cloudflare vector database (used by AutoRAG; not named in the video), Cloudflare Workers, Cloudflare MCP servers (AutoRAG server, one of about 30 released recently), Cursor, Claude (comparison point only), Tailwind CSS (only referenced as an example doc set and a separate video)

## Relevance to our work
- **agentos** (1/3): Shows a managed alternative to self-built RAG (scrape, object store, auto-embed, MCP exposure). It is a useful comparison for the MemoryMesh knowledge-bucket design, but gives no retrieval quality or latency data. → *Compare the scrape-to-Markdown ingestion step and per-result scoring against MemoryMesh knowledge-bucket ingestion on the same docs corpus, recording retrieval quality rather than taking the video's accuracy claim.*
