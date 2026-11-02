# Using this will make your AI AGENTS EVEN SMARTER!

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `2G-xavWw1bY` · [watch](https://youtu.be/2G-xavWw1bY) · **date:** 2025-11-02 · **length:** 4:49 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** GitHub, Cursor, DeepSeek, Google
- **topics:** context-engineering, rag-retrieval, token-cost-efficiency · **tags:** github, repo-ingestion, gitingest, long-context, token-count, cursor, mcp-servers, deepseek, gemini

> A 5-minute tip for loading a whole GitHub repo into an LLM, either through a chat tool or a repo-to-text converter (gitingest), to answer questions and find install steps.

## Summary
The presenter argues that reading a long GitHub repo by hand is slow, so the whole repo should be passed to an LLM instead. The first method is a web tool that swaps the GitHub URL for its own domain and gives a file tree, a token count, and a chat box that runs an unnamed backend model. The second method swaps "hub" for "ingest" in the GitHub URL to open gitingest, which turns the repo into a structured text knowledge base with a token count and file-exclusion options, to paste into a model of your choice. The presenter suggests choosing the model from the token count: a Gemini model for very large repos and a DeepSeek model for smaller ones where accuracy matters more. In the example, the repo only documented Claude installation, and the ingested repo let a DeepSeek chat produce Cursor setup steps (a bash script, then a pwd-derived full path). The video shows no measurements or accuracy checks, and the presenter admits the first tool's model is unknown and that a first prompt missed features until it was made explicit.

## Key ideas
- **Pass the whole repository to an LLM instead of searching files by hand** — Rationale given: open source is published on GitHub, and long repos scatter information. The aim is to query the repo through an LLM rather than read it manually. ([0:00](https://youtu.be/2G-xavWw1bY?t=0))
- **Web tool with a built-in model: change the GitHub URL domain to the tool's domain** — The tool shows a file tree, token count and a prompt box. The backend model is not known to the presenter. Results are decent, but the presenter flags two limits: the repo can exceed the token budget, and the model's capability is unknown. ([0:00](https://youtu.be/2G-xavWw1bY?t=0))
- **A first prompt can miss things; an explicit completeness request fixes it** — Asking for a brief list of MCP server features missed some items. Re-prompting with an explicit 'list all features' returned the full list. ([1:38](https://youtu.be/2G-xavWw1bY?t=98))
- **gitingest turns the repo into a structured text knowledge base for any model** — Swap 'hub' for 'ingest' in the GitHub URL. It splits the repo into labelled sections, reports a token count, and lets you exclude files. The output is copied and used in whatever model you like. ([2:36](https://youtu.be/2G-xavWw1bY?t=156))
- **Choose the model from the token count** — A very large repo suggests a Gemini model for its large context window. A smaller repo where accuracy matters suggests a DeepSeek model. ([2:36](https://youtu.be/2G-xavWw1bY?t=156))
- **Use it for setup steps the README does not cover** — The repo documented only Claude installation. With the ingested repo in a DeepSeek chat, the model gave Cursor setup steps: create a bash file, then get the full path via pwd and run the script from Cursor. ([2:36](https://youtu.be/2G-xavWw1bY?t=156))
- **Scope is exploration and setup, not verified answers** — The presenter frames the tools as ways to get a quick overview of unfamiliar or complex repos. There is no accuracy test, no comparison of models, and no discussion of cost or privacy. ([3:56](https://youtu.be/2G-xavWw1bY?t=236))

## Techniques
- **Repo URL swap into a chat-with-repo tool** — Take the GitHub repo URL and change the domain to the tool's domain (the transcript's auto-caption reads 'GG', so the exact host is unclear). Use the file tree to inspect the repo, enter a prompt in the top box, run the analysis, and read the results below. *When:* Fast first look at an unfamiliar repo, when the repo is small enough for the tool's built-in model and the model's identity does not matter.
- **gitingest repo-to-text conversion** — Change 'hub' to 'ingest' in the GitHub URL to open gitingest. Check the token count, exclude files you do not need, then copy the generated structured knowledge base and paste it into any LLM as context. *When:* Long or complex repos, or when you need to control what context a model sees and which model you use.
- **Pick the model by token count** — Read the token count from the ingest output. Use a Gemini model when the repo is very large (largest context window). Use a DeepSeek model when the count is moderate and you want more accurate answers. *When:* Before sending an ingested repo to a model, to avoid exceeding the context window or using a larger model than needed.
- **Explicit completeness prompting** — If the first answer is incomplete (e.g. missing features), re-prompt with an explicit instruction such as 'list all the features' rather than a vague request. *When:* Enumeration or inventory questions about a repo, where the model may stop early.
- **Iterative setup questions on an ingested repo** — Ask for install steps for the target IDE; then follow up for specifics such as the correct path (suggested method: run pwd for the current directory and use the full path in the command). *When:* Installing an MCP server or tool into an IDE that the README does not document.

## Numbers
- No benchmarks, accuracy scores, costs or latencies are given. Token counts are shown on screen, but no values are quoted. ([0:00-2:36](https://youtu.be/2G-xavWw1bY?t=0))
- Video length is 4:49. Model choice is based on context window size: Gemini for the largest repos, DeepSeek for smaller ones. ([2:36](https://youtu.be/2G-xavWw1bY?t=156))

## Hot takes
- The title ('make your AI AGENTS EVEN SMARTER') promises agent improvement, but the video is about loading a repo into a chat model for reading.
- The first tool's backend model is unknown to the presenter, and the presenter does not test accuracy, so 'decent results' is anecdotal.
- The most reusable idea is the ingest step with token counting and file exclusion, not the single anecdote about Cursor setup.
- Quality is capped at 2 because the title is hype and the substance is a short, unevaluated tool tour.

## Tools mentioned
gitingest (named 'git ingest' in the transcript), DeepSeek (model, transcribed as 'DeepSeq'), Gemini (model), Cursor IDE, Claude (install instructions in the repo), GitHub, MCP server (example repo, unnamed)

## Relevance to our work
- **agentos** (1/3): Repo-to-context packing with token counts and exclusion rules is adjacent to knowledge-bucket ingestion in MemoryMesh, but the video does not cover retrieval or evaluation. → *Compare gitingest-style ingestion (token count plus exclude patterns) against MemoryMesh's bucket ingestion before adding a new repo-ingest path.*
- **general** (1/3): Useful background on the practical choice between a chat-with-repo tool and a raw text dump with token counting. → *Check the gitingest output format and exclusion options if you need a repo snapshot for a one-off model session.*
