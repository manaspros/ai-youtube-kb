# DBX Is Almost the Perfect Free Database Client

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `b6rVCrBPbe8` · [watch](https://youtu.be/b6rVCrBPbe8) · **date:** 2026-10-02 · **length:** 8:51 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Josh (Better Stack) · **orgs:** Better Stack, DBX, Navicat, DataGrip, TablePlus, DBeaver
- **topics:** dev-tools, mcp-and-tools, security-guardrails · **tags:** database-client, mcp, credential-storage, plaintext-secrets, sqlite, mysql, postgres, redis, mongodb, docker-compose, claude-code, dbx

> Hands-on review of DBX, a free desktop database client with an optional MCP server that lets coding agents query saved connections; the reviewer praises the workflow but flags plaintext passwords in its local SQLite file as a blocker for production credentials.

## Summary
Josh from Better Stack reviews DBX, a free, few-months-old desktop database client that claims support for 90+ engines and reached 18,000+ stars. He pitches it against paid clients (Navicat, DataGrip, TablePlus) and highlights its MCP integration, which lets a coding agent query saved connections. He walks through a setup with MySQL, Redis and MongoDB in Docker: install the app, install the MCP server separately, add and test connections, then ask Claude to list connections, describe a table and run cross-engine queries without pasting credentials. He then cautions that a small installer does not mean a small running process, and that most of the 90+ engines are lightly used or untested. The main finding is that saved connections live in a local SQLite file (dbxdb) whose secrets table stores passwords in plain text, tracked as an open bug since June 12. The reviewer concludes the tool is fine to try, but not for production credentials until that is fixed.

## Key ideas
- **DBX is pitched as a free GUI database client covering 90+ engines, priced against paid tools.** — Positioned as a free alternative to Navicat, DataGrip and TablePlus, which cost far more per seat or per year. ([0:00](https://youtu.be/b6rVCrBPbe8?t=0))
- **The MCP server is a separate binary, so installing DBX does not install it.** — The reviewer says the agent integration needs its own install step. TablePlus and DataGrip also now ship MCP tools, so DBX is not unique in this. ([1:10](https://youtu.be/b6rVCrBPbe8?t=70))
- **The agent works through saved connections, not through credentials pasted into the chat.** — Claude receives the DBX tools and uses the saved connections, so the reviewer never gives it a password or connection string. ([4:30](https://youtu.be/b6rVCrBPbe8?t=270))
- **Download size understates the footprint.** — The installer is about 20 MB, but the Linux build is closer to 100 MB. The Mac process can sit at hundreds of MB while idle, and users have reported multiple GB under load. ([5:23](https://youtu.be/b6rVCrBPbe8?t=323))
- **The 90+ engine count is mostly untested in practice.** — Engine support went from 8 at the April launch to 17 in May and kept growing. The reviewer says real use and bug reports concentrate on MySQL, Postgres and DuckDB. ([6:52](https://youtu.be/b6rVCrBPbe8?t=412))
- **Saved connections sit in a local SQLite file, and the secrets table stores passwords in plain text.** — The file is named dbxdb and is not locked. Issue 1081, opened June 12 and still tagged as a bug, reports the plaintext storage. Other leaks were fixed quickly, but this one remains open. ([6:52](https://youtu.be/b6rVCrBPbe8?t=412))
- **The verdict is to avoid production credentials for now.** — The maintainer ships fixes fast, but the reviewer says local credential storage is the one thing that matters before trusting it with production passwords. ([8:02](https://youtu.be/b6rVCrBPbe8?t=482))

## Techniques
- **Stand up a multi-engine local test rig** — Run MySQL, Redis and MongoDB in Docker Compose, load a small dataset into each (basic tables, Redis keys, Mongo events), then point the DB client at all three. The reviewer's setup is MySQL for the app, Redis for sessions and Mongo for events. The exact compose file is not shown. *When:* To test a database client or agent tool against realistic mixed-engine data instead of a single Postgres URL.
- **Add a connection with a test-before-save step** — In DBX, choose the engine from the list, then set the name, host, port, user, password and database name. Run Test, and save only if it passes. Repeat per engine. *When:* When adding each saved connection, so the agent only ever sees connections that already work.
- **Register the DBX MCP server with Claude Code and check it appears** — Install the separate MCP binary (npm install, or ask Claude to install it), then register it with Claude. Run the MCP command in a session and confirm the DBX tools are listed; if not, re-register. The exact registration command is not shown in the video. *When:* To give a coding agent read/query access to saved database connections without exposing credentials.
- **Agent prompts used for smoke testing** — (1) 'use the dbx tools, list my database connections'. (2) 'describe the orders table on demo mysql' and ask for real column names, not guesses. (3) Cross-engine: query shop orders for status and total for paid or shipped orders on demo mysql, find the hoodie event in demo mongo events, read the cart hash from demo redis. *When:* As a staged check: list connections, then schema inspection, then a query that spans several engines.
- **Audit a local client's credential store before storing production secrets** — Open the client's local store directly (here the dbxdb SQLite file) and inspect the secrets table to see whether passwords are encrypted or stored in plain text. The reviewer's check was to open the file in a SQLite viewer. *When:* Before putting production credentials into any desktop client or agent tool with local storage.

## Numbers
- DBX supports more than 90 database engines and has over 18,000 stars. ([0:00](https://youtu.be/b6rVCrBPbe8?t=0))
- Competitor pricing: Navicat Premium $80/month or $1,600 perpetual per seat; DataGrip about $110 for the first year for one person; TablePlus $100 once. ([0:00](https://youtu.be/b6rVCrBPbe8?t=0))
- Installer is around 20 MB, Linux build closer to 100 MB; Mac running process can sit at hundreds of MB idle, with users reporting multiple GB under load. ([5:23](https://youtu.be/b6rVCrBPbe8?t=323))
- Engine count went from 8 at the April launch to 17 in May, and kept rising in later months. ([5:23](https://youtu.be/b6rVCrBPbe8?t=323))
- Plaintext-secrets issue 1081 opened June 12 and was still open at the time of the video. ([6:52](https://youtu.be/b6rVCrBPbe8?t=412))

## Hot takes
- Plaintext passwords in the dbxdb secrets table make it unsafe for production credentials until fixed (the reviewer's main warning).
- The 90+ engine count is marketing; only MySQL, Postgres and DuckDB appear to be used and tested.
- A tiny download does not mean a small app: idle Mac processes can reach hundreds of MB.
- TablePlus, a comparable small client with MCP, stores secrets in the OS keychain, which DBX does not do.

## Tools mentioned
DBX (free desktop database client, version not stated), DBX MCP server (separate binary), Claude Code (used to register and call the MCP tools), Docker Compose, MySQL, Redis, MongoDB, Postgres, SQLite (dbxdb file), DuckDB, Navicat, DataGrip, TablePlus, DBeaver, VS Code, npm, brew, WKWebView

## Relevance to our work
- **agentos** (1/3): Shows an agent-facing DB tool design where the agent gets query tools over saved connections and never sees credentials, a pattern relevant to AgentOS tool access for Postgres, Redis and Mongo. → *When designing AgentOS tool access to data stores, keep connection secrets out of the prompt and expose query tools bound to saved, pre-tested connections.*
- **prosharness** (1/3): The credential-storage finding (plaintext passwords in a local SQLite secrets table) bears directly on ProsHarness's zero-token credential handling. → *Audit ProsHarness's local credential store to confirm secrets are never kept in plaintext on disk, and add a check like the reviewer's: open the store and inspect the secrets table.*
