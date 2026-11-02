# This Open-Source Tool Replaces Bubble and Retool (Appsmith)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `8O7AjZIAkpk` · [watch](https://youtu.be/8O7AjZIAkpk) · **date:** 2026-04-02 · **length:** 5:04 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Appsmith, Retool, Bubble, Webflow, ToolJet
- **topics:** dev-tools, vibe-coding-app-building · **tags:** low-code, internal-tools, appsmith, self-hosted, open-source, postgres, retool-alternative, git, docker, kubernetes

> Short Better Stack walkthrough of Appsmith, a self-hostable open-source low-code tool for internal dashboards, showing a Postgres employee search and CRUD-style table in about two minutes, with an honest list of limits and a Retool comparison.

## Summary
The presenter pitches Appsmith as an open-source, self-hostable alternative to building internal tools (forms and tables) by hand with React, API layers, and auth. He demos connecting the preset Postgres datasource, binding a table widget to the employees table, adding an input form and a search query, wiring a button trigger to a toast, and deploying. He stresses that JavaScript is available in queries and triggers, that apps are Git-backed, and that the product can be self-hosted with Docker or Kubernetes. He then lists real limits: client-side rendering of large datasets slows down so server-side pagination is needed, mobile layouts need manual tweaks, state management can confuse no-code users, and the UI trails Retool for fancy dashboards. His positioning is Appsmith versus Retool (more polished but expensive and closed) and ToolJet (closer comparison), with Bubble and Webflow treated as customer-facing tools that are not really comparable. The verdict is that Appsmith is a good trade-off for shipping internal tools quickly. The evidence is a single small demo with no performance or security testing.

## Key ideas
- **Internal tools (forms and tables) don't need a full React stack, API layer, and auth build; a low-code builder can ship them faster** — Pitch framing: Appsmith is open source (speaker cites 39,000+ GitHub stars), free to self-host, with unlimited users. It targets internal tools, not customer-facing apps. ([0:00](https://youtu.be/8O7AjZIAkpk?t=0))
- **The core build loop is datasource, then widgets bound to it, then queries and triggers** — Connect a datasource (the demo uses the preset Postgres), drop a Table widget bound to a table, add an input and a submit button, then write a query driven by the input to search. Triggers handle actions such as a toast on click. Deploy is one click. ([1:17](https://youtu.be/8O7AjZIAkpk?t=77))
- **JavaScript is the escape hatch that keeps low-code from trapping you** — Queries can be SQL, REST, or JavaScript. Widgets handle the UI and data sources cover databases, APIs, SaaS tools, and LLMs. The speaker argues that most low-code tools hide logic, while Appsmith exposes it. ([2:24](https://youtu.be/8O7AjZIAkpk?t=144))
- **Ops-friendly deployment and governance are built in** — Git branching, merging, and CI/CD work normally. Self-host with Docker or Kubernetes. Custom components can be built with React or plain JS. RBAC, audit logs, and SSO are presented as included. ([2:24](https://youtu.be/8O7AjZIAkpk?t=144))
- **Large datasets and mobile layouts are the known weak points** — Rendering big datasets on the client slows the page, so server-side pagination is required. Mobile layouts are not automatic. Users coming from no-code state management may find it confusing at first. ([3:29](https://youtu.be/8O7AjZIAkpk?t=209))
- **Appsmith's real competitor is Retool, and the trade-off is polish versus cost and openness** — Retool is more polished with stronger features but is expensive and closed source. Appsmith is less polished but open, and costs zero if self-hosted. ToolJet is the closest comparison. Bubble and Webflow are mostly customer-facing and not directly comparable. ([4:32](https://youtu.be/8O7AjZIAkpk?t=272))
- **Git integration is Appsmith's differentiator over ToolJet** — The speaker's verdict is that Appsmith is usually the better trade-off for shipping internal tools quickly, with stronger Git integration than ToolJet. ([4:32](https://youtu.be/8O7AjZIAkpk?t=272))

## Techniques
- **Bind a Postgres table to a low-code table widget** — Launch Appsmith and create an account. Start a new app from a blank canvas. Choose the preset Postgres datasource and link it. Drop a Table widget onto the canvas and connect it to the target table (the demo uses the employees table, which has dummy users). The table populates immediately from the datasource. *When:* Internal CRUD or lookup screens over an existing Postgres database where you want to skip the React and API layers.
- **Search query driven by an input widget** — Add an input field and a submit button. Create a query against the datasource that reads the input's value (the demo searches the employees table by the typed term). Point the table's data at that query. Add an onClick trigger on the button for follow-up actions such as a toast notification. Deploy. *When:* Search-and-filter admin views where the query needs to react to user input without writing a backend endpoint.
- **Keep logic in JS and source in Git** — Put custom logic in query or trigger JavaScript rather than hiding it in visual config. Use Git branching, merging, and CI/CD on the app source. Self-host with Docker or Kubernetes if data control matters. *When:* When the team wants low-code speed but needs an escape hatch, code review, and control over where data and costs live.
- **Server-side pagination for large tables** — The speaker advises paginating on the server instead of loading big datasets into the client, since client-side rendering slows down. *When:* Any table over a few thousand rows that is backed by a live datasource.

## Numbers
- Appsmith has over 39,000 GitHub stars (speaker's figure) ([0:00](https://youtu.be/8O7AjZIAkpk?t=0))
- Self-hosting is free with unlimited users (speaker's claim) ([0:00](https://youtu.be/8O7AjZIAkpk?t=0))
- The demo CRUD-style app took about a minute or two to build (speaker's estimate, not timed) ([2:24](https://youtu.be/8O7AjZIAkpk?t=144))
- Retool is more expensive and closed source versus Appsmith's zero cost when self-hosted (qualitative, no prices) ([4:32](https://youtu.be/8O7AjZIAkpk?t=272))

## Hot takes
- The title 'replaces Bubble and Retool' overstates the video: the presenter's own comparison says Retool is more polished and stronger, and that Bubble is not really comparable.
- The build-time claim (a minute or two, no React, no auth wiring) rests on one search-and-table demo with no timing and no performance or security checks.
- The RBAC, audit log, and SSO claims are presented as built in but are not shown in the video.
- Quality is capped at 2 because the title is hype-driven and the substance is a short, shallow demo, although the limits section is honest.

## Tools mentioned
Appsmith, PostgreSQL, React, Docker, Kubernetes, Git, Retool, Bubble, Webflow, ToolJet
