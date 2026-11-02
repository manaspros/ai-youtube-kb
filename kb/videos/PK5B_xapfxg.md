# AFFiNE: The Open-Source Alternative for Notion, Miro and Airtable

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `PK5B_xapfxg` · [watch](https://youtu.be/PK5B_xapfxg) · **date:** 2026-04-02 · **length:** 7:31 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, AFFiNE, Notion, Obsidian, Miro, AppFlowy, AnyType, Figma, GitHub
- **topics:** dev-tools · **tags:** affine, open-source, local-first, self-hosted, docker-compose, crdt, blocksuite, edgeless-mode, kanban, notion-alternative, whiteboard, architecture-docs, productivity

> Better Stack walkthrough of AFFiNE, an open-source, local-first, self-hostable workspace that combines docs, databases and an infinite whiteboard canvas, with a candid list of its rough edges.

## Summary
The presenter introduces AFFiNE as a single open-source workspace that merges rich documents, relational databases and an infinite whiteboard (called edgeless mode) in one place. The pitch rests on local-first design: CRDT-based sync that lets you work offline and come back without merge conflicts, and a stack that starts with one Docker Compose command. The demo builds a small project page: a markdown API spec, a code snippet, an architecture sketch in edgeless mode, sticky notes converted into a Kanban database, and an embedded GitHub issue and Figma design. The comparison positions AFFiNE against Notion (cloud-only, limited canvas), Obsidian (needs plugins for diagrams and databases), Miro (visual only, no structured docs) and AppFlowy/AnyType. The speaker credits BlockSuite, the extensible web-component block editor, as the main differentiator for developers who want to fork it or write custom blocks. Downsides are stated plainly: performance on large workspaces, immature advanced database relations and subtasks, no native mobile app, and self-hosting quirks around image proxy config and ARM. The verdict is that it suits people who value data ownership, self-hosting and architecture docs, but not those needing polished UX or heavy mobile use.

## Key ideas
- **AFFiNE combines documents, relational databases and an infinite whiteboard in one workspace, so specs, diagrams and tasks don't need separate tools.** — The 'edgeless mode' turns a page into an infinite canvas where docs sit alongside shapes and arrows. The speaker positions this as the core difference from tools that split docs, diagrams and planning. ([0:00](https://youtu.be/PK5B_xapfxg?t=0))
- **Local-first design with CRDT sync means offline work without merge conflicts.** — The speaker says sync is powered by Y-Octo and a Rust backend named Octobase (as captioned). The stack starts with a single Docker Compose command, and the workspace can be self-hosted. ([0:00](https://youtu.be/PK5B_xapfxg?t=0))
- **BlockSuite is the real differentiator for developers: an extensible block editor built on web components.** — Developers can build custom blocks, such as ones that render API responses or custom data views, and plugins on top of it. Third-party blocks are already appearing in the community. The speaker does not show building one. ([1:09](https://youtu.be/PK5B_xapfxg?t=69))
- **Keeping the spec, the architecture diagram and the tasks in one page removes exporting and app switching.** — Demo sequence: markdown API spec, then a code snippet, then switch to edgeless mode and sketch shapes and arrows around the code. Sticky notes are converted into a database with a Kanban view. A GitHub issue and a Figma design are embedded alongside. ([2:31](https://youtu.be/PK5B_xapfxg?t=151))
- **Compared with alternatives, the main trade-off is breadth and self-hosting against polish.** — Notion is polished but cloud-only with a limited canvas. Obsidian needs plugins for diagrams and databases. Miro is visual only. AppFlowy and AnyType are similar, but the speaker says AFFiNE's canvas, BlockSuite and CRDT sync are ahead for developer workflows. ([3:36](https://youtu.be/PK5B_xapfxg?t=216))
- **Known weak spots: large-workspace performance, advanced database features, mobile, and self-hosting edge cases.** — Large workspaces can buffer poorly and feel less smooth than Figma. Advanced relations and subtasks are not there yet. There is no native mobile app, only browser use on tablets. Self-hosting has issues with image proxy configuration and ARM setups. ([5:50](https://youtu.be/PK5B_xapfxg?t=350))

## Techniques
- **Self-host AFFiNE with Docker Compose** — Clone the repo, then run the Docker Compose command to bring up the stack. Create a workspace in the browser. The video does not show exact commands or config keys, and the repo link is only in the video description. *When:* When you want a self-hosted Notion/Miro-style workspace and need data kept off third-party servers.
- **Doc plus architecture diagram on one canvas** — Write the spec in a markdown block and add the code snippet. Switch the page to edgeless mode. Place shapes such as API gateway, auth service and database, and connect them with arrows. The diagram stays next to the doc it describes. *When:* When specs and architecture diagrams drift apart in separate tools and you want them to stay together.
- **Sticky notes to Kanban database** — Add task sticky notes on the canvas, select them, and convert them into a database. The result shows as a Kanban board in the same workspace. *When:* For lightweight task tracking next to design material, when you don't want a separate project tool.
- **Embed external context in the page** — Embed a GitHub issue directly in the page, and place a Figma design next to it, so tasks, design references and architecture live together. *When:* When a planning page should link to live issues and design files.
- **Custom blocks with BlockSuite** — Build custom blocks and plugins as web components on the BlockSuite editor framework. The speaker describes this as the way to add API-response blocks or custom data views. Not demonstrated. *When:* When you need a domain-specific view inside a docs workspace and are willing to fork or extend the open-source editor.

## Numbers
- Over 63,000 GitHub stars for AFFiNE, with a new version just shipped. ([1:09](https://youtu.be/PK5B_xapfxg?t=69))
- The 63,000+ star figure is repeated when discussing stability. ([5:50](https://youtu.be/PK5B_xapfxg?t=350))
- The full stack starts with a single Docker Compose up command. ([0:00](https://youtu.be/PK5B_xapfxg?t=0))

## Hot takes
- AFFiNE can replace Notion, Miro and parts of a dev workflow in one tool. The speaker's own caveats (performance, database features, mobile, self-hosting) limit that claim.
- Local-first CRDT sync means no merge conflicts and no lost work. This is stated, not tested in the video.
- BlockSuite's extensibility matters more than the workspace UI for developers. The speaker says this but does not demonstrate building a block.

## Tools mentioned
AFFiNE, BlockSuite, Y-Octo (CRDT sync, as captioned), Octobase (Rust backend, as captioned), Docker Compose, Notion, Obsidian, Miro, AppFlowy, AnyType, Figma, GitHub

## Relevance to our work
- **agentos** (1/3): Self-hosted, local-first workspace for specs and architecture docs. Only a tangential fit for the AgentOS build; it is not an agent or infra tool. → *Optional: try a self-hosted AFFiNE instance as a spec and architecture-diagram workspace for AgentOS. Low priority.*
