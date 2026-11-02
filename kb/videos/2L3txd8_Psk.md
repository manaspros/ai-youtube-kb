# Why Developers Are Quietly Switching to This Note App (SiYuan)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `2L3txd8_Psk` · [watch](https://youtu.be/2L3txd8_Psk) · **date:** 2026-05-02 · **length:** 5:18 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host · **orgs:** Better Stack, SiYuan, Notion, Obsidian
- **topics:** dev-tools · **tags:** note-taking, knowledge-management, self-hosting, docker, block-references, sql, obsidian-alternative, notion-alternative, open-source

> Better Stack reviews SiYuan, a self-hosted, open-source, block-based note app, arguing that permanent block IDs, built-in databases and SQL suit developer documentation better than file-based Obsidian or cloud Notion.

## Summary
The host presents SiYuan as a local-first, open-source note tool that links individual blocks (paragraphs, list items, code blocks) rather than whole files, so moved content keeps its references. He runs it self-hosted via Docker Compose, which he says was up in about a minute, then demos a code block embedded in a second location that survives a move. He builds a small bug-tracking database with status and priority fields, queries it with built-in SQL, and shows the graph view of linked blocks. He contrasts this with Obsidian (file-based) and Notion (cloud-only, same structure but not local). The downsides he names are a proprietary .sy storage format where Markdown is only an export, a smaller plugin ecosystem especially in English, a UI he calls dated, and the need for optimization in very large workspaces. His verdict: switch if your notes are becoming documentation or systems, but not if you are already deeply invested in Notion. The transcript is auto-captioned and misspells the product name as "CUN" and "C1"; the title confirms SiYuan.

## Key ideas
- **Block-level linking instead of file-level linking** — Each paragraph, list item and code block gets a permanent ID, so a block can be moved and its references still resolve. The speaker frames this as the main reason it suits docs, bug tracking and architecture notes. ([0:00](https://youtu.be/2L3txd8_Psk?t=0))
- **Self-hosted via Docker Compose** — He pulled the repo from its Docker Compose file and launched it with Docker Compose, with the app running in about a minute. Exact commands are not shown. ([0:56](https://youtu.be/2L3txd8_Psk?t=56))
- **Databases with built-in SQL inside notes** — He builds a bug-tracking table with status and priority fields and queries it directly with SQL in the note, without plugins. ([0:56](https://youtu.be/2L3txd8_Psk?t=56))
- **Graph view over blocks** — The graph view shows how blocks and database entries connect, and it is interactive. ([2:22](https://youtu.be/2L3txd8_Psk?t=142))
- **Block-based versus file-based mental model** — Obsidian links files, so you link a page; SiYuan links the exact decision, bug or snippet inside it. He describes Obsidian as a strong folder of notes and SiYuan as a more structured system. ([2:22](https://youtu.be/2L3txd8_Psk?t=142))
- **Downsides: proprietary storage format and small plugin ecosystem** — Notes are stored in a custom .sy format rather than plain Markdown, and Markdown is available only as an export. The plugin market is smaller, especially for English users. He also notes the UI can feel dated and very large workspaces may need optimization. ([3:19](https://youtu.be/2L3txd8_Psk?t=199))
- **Decision rule for switching** — Stay with Obsidian if your notes are mostly Markdown files plus plugins. Consider SiYuan if they are turning into documentation and systems. Switching is a pain if you are already heavily invested in Notion. ([4:19](https://youtu.be/2L3txd8_Psk?t=259))

## Techniques
- **Block-reference notes for moving content safely** — Give each block a permanent ID, then embed or reference it in other notes. Moving the original block leaves references intact, so you can reorganize without breaking links. *When:* Structuring project docs, architecture notes or code snippets that get reshuffled often.
- **Lightweight bug tracker inside a notes app** — Create a database note with status and priority columns for each bug, then query it with built-in SQL from within a note. *When:* Tracking issues or tasks alongside documentation without a separate tool or plugin.
- **Local self-hosting with Docker Compose** — Clone the repo, use its Docker Compose file, and start it with Docker Compose so the data stays on your own machine. The video does not show the exact commands or config. *When:* You want a local-first, self-hosted notes system and do not want cloud storage.

## Numbers
- Self-hosted SiYuan was up and running in about one minute via Docker Compose (speaker's estimate; he also says self-hosting takes a minute or two). ([0:56](https://youtu.be/2L3txd8_Psk?t=56))
- Video length is 5:18. ([0:00](https://youtu.be/2L3txd8_Psk?t=0))

## Hot takes
- Block-level linking is a real differentiator over file-based Obsidian for structured documentation.
- The proprietary .sy format is a real lock-in risk, since Markdown is only an export.
- Switching from a heavily used Notion setup is not worth it, so keep Notion or Obsidian in that case.
- The UI looks like Notion, and the speaker says some find it dated.
- The plugin ecosystem is much smaller than Obsidian's, especially for English users.

## Tools mentioned
SiYuan, Obsidian, Notion, Docker, Docker Compose, SQL, Python (incidental code block)
