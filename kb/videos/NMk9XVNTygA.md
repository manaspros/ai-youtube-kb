# This Open-Source Tool Fixes Browser History (Hister)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `NMk9XVNTygA` · [watch](https://youtu.be/NMk9XVNTygA) · **date:** 2026-09-02 · **length:** 8:18 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Unnamed Better Stack host · **orgs:** Better Stack, Google, Readwise
- **topics:** dev-tools, rag-retrieval, security-guardrails · **tags:** hister, browser-history, full-text-search, personal-knowledge, self-hosted, inverted-index, mcp, chrome-extension, firefox-extension, karakeep, archivebox, wallabag, readwise-reader, security-caveats, pre-1.0

> Hister is a self-hosted tool that indexes the full rendered text of every page you read in Chrome or Firefox, so you can search your browsing by content; useful, but pre-1.0 with real security gaps.

## Summary
The host argues that browser history stores only a page's title and URL, so content you read is unrecoverable once you forget the title, and that "recall search" is underserved compared with discovery search. He demos Hister, a local Go server (listening on port 4433) plus a Chrome or Firefox extension that sends each rendered page's URL, title, extracted text and gzipped HTML to the laptop for indexing while you browse. The demo shows phrase search returning a page that Chrome history cannot find, a small query language (domain and text operators that combine), a terminal search command, and browser-history import that revisits old URLs. He notes a built-in MCP endpoint so a coding agent can query your own reading index. The review then lists caveats: an unencrypted index, a Docker compose file that binds 0.0.0.0 with no auth by default, an ad-hoc signed and un-notarized Mac binary, Safari not working, and a pre-1.0 release history with breaking minor releases. Verdict: worth trying for Chrome or Firefox users who are comfortable self-hosting, but configure auth and disk encryption first.

## Key ideas
- **Browser history keeps only a page's title and URL, not its content, so once you forget the exact title the page is effectively lost. Recall search (finding something you already read) is underserved compared with discovery search.** — Framing of the problem; Firefox also expires history after roughly 90 days by default (as stated in the video). ([0:00](https://youtu.be/NMk9XVNTygA?t=0))
- **Hister's browser extension builds the index passively while you browse. Nothing has to be bookmarked or saved, unlike read-later apps.** — Pages visited during the demo appeared in Hister's history without any save action. The index captures the rendered page after JavaScript runs, so internal wikis and dashboards are included. ([2:05](https://youtu.be/NMk9XVNTygA?t=125))
- **Phrase search over page bodies finds a page you visited earlier from a sentence buried mid-article, where Chrome's history search returns nothing.** — Result shows the page plus matching text around the hit, and links back to the reading position. ([2:05](https://youtu.be/NMk9XVNTygA?t=125))
- **A small query language narrows results: a domain operator restricts to one site, and a text operator requires a phrase in the page body. The two combine.** — Examples shown: domain github.com; text memory leak; and both together to find a vaguely remembered memory-leak discussion in a GitHub issue without knowing the repo. ([3:10](https://youtu.be/NMk9XVNTygA?t=190))
- **Imported old browser history only has URLs, so Hister must revisit those pages and index what is there now. Only pages seen while the extension runs are captured as they were rendered.** — Import is run from the CLI on current versions and detects local browser databases. ([4:07](https://youtu.be/NMk9XVNTygA?t=247))
- **Architecture is entirely local: the extension posts URL, title, extracted text and full HTML to a server on the laptop, which uses a pure-Go inverted index. HTML is gzipped and stored locally, about 100 KB per page.** — Speaker estimates 10,000 pages at roughly 1 GB, and says storage is not the constraint. ([4:07](https://youtu.be/NMk9XVNTygA?t=247))
- **Hister ships an MCP endpoint, so a coding agent can answer questions from the pages you have read and are authenticated for, instead of from training data or separately connected doc sites.** — The endpoint URL and tool names are not shown in the video. ([5:30](https://youtu.be/NMk9XVNTygA?t=330))
- **The review's main caveats are security and maturity: the index is unencrypted (the docs say so), the compose file binds 0.0.0.0 with no default auth, the Mac binary is ad-hoc signed and not notarized, and the project is pre-1.0 with breaking changes across minor releases.** — Safari is not supported (a proof-of-concept PR open since February has been untouched). Contributor counts are inflated: about 78% of the 47 listed contributors are the maintainer. The host recommends disk encryption and configuring auth before any network exposure. ([6:17](https://youtu.be/NMk9XVNTygA?t=377))

## Techniques
- **Local recall index for your own reading** — Download the release binary for your platform (the demo uses the Darwin ARM64 build), rename it to hister, mark it executable, and run `hister listen`. The server starts on local port 4433. Install the Chrome or Firefox extension, then browse normally. Pages are indexed as they render. *When:* You read a lot of docs, GitHub issues or internal wikis, want to find a page by a phrase from its body, and are comfortable self-hosting on a machine that is not shared.
- **Scoped full-text queries** — Use `domain <host>` to restrict results to one site (for example `domain github.com`) and `text <phrase>` to require the phrase in the page body. Combine them in one query. Use the terminal command (`hister search <query>`, as the demo appears to show) for the same index without leaving the terminal. *When:* You remember a fragment of a page's wording or the site it came from, but not the title or URL.
- **Backfilling from existing browser history** — Run `hister import browser`. It finds local browser databases and imports the URLs. Expect Hister to revisit each URL and index the current content, since old history has no stored page text. *When:* You want the index to cover history from before you installed it. Results for old pages reflect their current content, not what you saw then.
- **Hardening before exposure** — Keep the server bound to localhost, or configure authentication before binding it to a network. Enable full-disk encryption, because the index holds the full text of every page you read. Do not run the bundled compose file unchanged, since it binds 0.0.0.0 with no auth. *When:* Any time the index holds work or internal pages, or you plan to run it in Docker or on a shared network.
- **Agent access to a personal reading index** — Point a coding agent's MCP client at the Hister MCP endpoint so it can search pages you have already read and are logged into. The video does not show the endpoint URL or configuration. *When:* The agent needs context from internal docs or pages that public search and training data do not cover.

## Numbers
- Firefox default history expiry is about 90 days. ([0:00](https://youtu.be/NMk9XVNTygA?t=0))
- Hister's local server listens on port 4433. ([1:00](https://youtu.be/NMk9XVNTygA?t=60))
- Full gzipped HTML is about 100 KB per page; 10,000 pages is roughly 1 GB. ([4:07](https://youtu.be/NMk9XVNTygA?t=247))
- Karakeep (transcribed as 'Para Keep') has about 28,000 GitHub stars. ([5:30](https://youtu.be/NMk9XVNTygA?t=330))
- Readwise Reader costs about $120 per year. ([5:30](https://youtu.be/NMk9XVNTygA?t=330))
- The Safari proof-of-concept PR has been open since February and untouched since. ([6:17](https://youtu.be/NMk9XVNTygA?t=377))
- 18 minor releases in seven months, with breaking changes documented between them. ([6:17](https://youtu.be/NMk9XVNTygA?t=377))
- 47 listed contributors, of whom roughly 78% are the actual maintainer. ([6:17](https://youtu.be/NMk9XVNTygA?t=377))
- Setup from download to a running server took about two seconds after three commands. ([7:39](https://youtu.be/NMk9XVNTygA?t=459))

## Hot takes
- Browser history is the wrong object for recall: it stores title and URL, not content, and that gap is unfilled by the big players.
- Self-hosted full-text capture of everything you read is a sharper security object than browser history, and the default configs are not safe to expose.
- Safari-only Mac users should skip it; the tool does not work there.
- Pre-1.0 with breaking minor releases, and most contributor activity comes from one person: treat it as a personal experiment, not infrastructure.
- The MCP endpoint is the most interesting part: a personal, already-authenticated reading corpus as agent context.

## Tools mentioned
Hister, Chrome extension for Hister, Firefox extension for Hister, Docker (multi-arch image), Nix flake (Darwin module), MCP, Karakeep (transcribed as 'Para Keep', 28k stars), ArchiveBox, Wallabag, Readwise Reader, Gatekeeper (macOS)

## Relevance to our work
- **agentos** (1/3): A captured-rendered-page inverted index exposed over MCP is a small instance of personal-corpus retrieval, loosely adjacent to MemoryMesh's knowledge buckets. Not a direct change. → *Read Hister's MCP endpoint and tool surface as a reference for how a personal-corpus search is exposed to agents, then compare with MemoryMesh's retrieval tool interface.*
- **prosharness** (1/3): Agents could query a local index of docs the user has read via MCP rather than re-fetching them, which is a possible context source for the Claude Code harness. Low priority. → *Note as an idea only: consider a read-only MCP lookup over the user's already-read docs as a context source for ProsHarness runs, and do not build it now.*
