# This Free Go Alternative to Firebase is Just One File

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `WZoC1HA1vec` · [watch](https://youtu.be/WZoC1HA1vec) · **date:** 2026-08-02 · **length:** 7:49 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Warren · **orgs:** Better Stack
- **topics:** dev-tools, infra-cost-scaling · **tags:** pocketbase, backend-as-a-service, sqlite, self-hosting, firebase-alternative, supabase-alternative, realtime, auth, vps, hooks

> Walkthrough of PocketBase, a single Go binary with embedded SQLite giving realtime DB, auth and file storage, tested on a React bug tracker, with a VPS deployment and pre-v1 caveats.

## Summary
Warren from Better Stack introduces PocketBase as a self-hosted alternative to Supabase or Firebase: one Go binary with SQLite embedded, providing a realtime database, authentication, file storage and an admin UI for collections. He builds a small React bug tracker against it, covering the JS SDK client, auth state, realtime list updates, and file uploads with a screenshot. Security is handled through per-collection API rules that reference the authenticated user. Extension is done with hooks written in Go or in JavaScript/TypeScript, with a demo hook that emails on record create. He then covers deployment: because SQLite needs persistent disk, he recommends a VPS over ephemeral platforms like Render or Railway, and explains that pb_data holds data.db and uploaded files. He closes by noting the project is pre-v1, so users must follow changelogs and run manual migrations.

## Key ideas
- **PocketBase is a single Go binary with SQLite embedded, offering a realtime database, auth, file storage and an admin UI, positioned as a simpler alternative to Supabase or Firebase.** — Backend can be extended with JavaScript/TypeScript as well as Go. Frontends connect with the JS SDK and can access the database directly, with access controlled by API rules. ([0:00](https://youtu.be/WZoC1HA1vec?t=0))
- **The frontend pattern is a single client module (pb.ts) that instantiates the client once and is imported everywhere.** — The auth hook seeds state from the current auth record and listens to auth store changes; the issues hook loads the full list on mount and subscribes to collection changes so dragged, created or deleted cards update state without refetching. ([1:05](https://youtu.be/WZoC1HA1vec?t=65))
- **Security is enforced in per-collection API rules rather than in app code.** — Rules reference the caller via @request.auth.id; the speaker's example requires a non-empty auth ID and restricts update/delete on users to the record owner. He compares this to the Supabase pattern. ([2:23](https://youtu.be/WZoC1HA1vec?t=143))
- **File uploads go through the same collection API: the client builds form data with the fields and the screenshot and calls create on the issues collection.** — Shown in the bug tracker as a submit function that appends all form data before the create call. ([2:23](https://youtu.be/WZoC1HA1vec?t=143))
- **Custom logic is added with hooks; 82 unique hooks existed at filming, and events include bootstrap and record create.** — PocketBase natively runs only JavaScript, so TypeScript hooks are compiled into the pb_hooks folder first. The demo hook sends an email via the app's new mail client whenever an issue record is created. ([3:33](https://youtu.be/WZoC1HA1vec?t=213))
- **Because it runs SQLite, the deployment needs persistent disk; ephemeral-filesystem hosts such as Render or Railway would lose data on each redeploy.** — The recommended path is a VPS. The pb_data folder holds data.db (all database rows) and storage/ (uploaded files), so the speaker says a real backup strategy is needed rather than leaving it as one file on disk. ([5:27](https://youtu.be/WZoC1HA1vec?t=327))
- **Static frontend files can be served from pb_public, and dynamic routes can be rendered with templates, which the speaker suggests for things like email templates.** — This supports a single-box setup with the React build and the backend on one server. ([6:47](https://youtu.be/WZoC1HA1vec?t=407))
- **The big caveat is that PocketBase is pre-v1, so it fits only teams willing to read changelogs and run manual migrations from time to time.** — The speaker says production-grade features such as migrations, job scheduling and logging are included, and the system is extensible. ([6:47](https://youtu.be/WZoC1HA1vec?t=407))

## Techniques
- **Singleton SDK client module** — Create one module (the speaker's pb.ts) that imports the PocketBase class, instantiates it once against the backend URL, and export it; import that instance in every hook and component. *When:* Any React or other front-end app talking to a PocketBase backend.
- **Auth state from the auth store** — Initialize user state from the auth store's current record, then register a change listener (onChange) that writes the new user into state. Logged-in state then stays in sync without polling. *When:* Auth-aware UI where the current user drives rendering and permissions.
- **Load-then-subscribe for live lists** — On mount, fetch the full collection (getFullList) to pre-populate state; then subscribe to the collection and append or update records as events arrive. Local drag-and-drop changes reflect automatically because they are writes to the same collection. *When:* Kanban boards, trackers or any list that must stay live across clients.
- **Multipart create with a file attachment** — Build a FormData object, append each text field and the file (e.g. a screenshot), then call the collection's create method with that FormData instead of a JSON body. *When:* Records that carry file attachments, such as issues with screenshots.
- **Collection API rules for access control** — In the admin UI, open each collection's API rules tab and set rules per action. Require a non-empty auth ID to access the collection, and for update/delete compare the record to the caller using the @request.auth.id expression. Exact rule syntax for other cases was not shown. *When:* Any multi-user data where clients talk to the database directly from the browser.
- **Hooks for server-side side effects** — Write hooks in JavaScript (or TypeScript compiled to JavaScript) and place them in the pb_hooks folder. Register handlers for events such as on-bootstrap or on-record-create; the demo sends an email with the app's new mail client's send call when an issue is created. *When:* Side effects that must run on the server, like notifications, when the default API is not enough.
- **Single-VPS deployment with persistent data** — Run the PocketBase binary on a VPS (the speaker cites plans from about $4/month) so pb_data persists. Back up data.db and the storage folder regularly. Serve the frontend build from pb_public. *When:* Small SaaS or internal apps where cost matters more than horizontal scale.

## Numbers
- PocketBase ships as one Go binary with SQLite embedded. ([0:00](https://youtu.be/WZoC1HA1vec?t=0))
- 82 unique hooks at the time of filming. ([3:33](https://youtu.be/WZoC1HA1vec?t=213))
- Supabase basic tier starts at $25 (per the speaker); a VPS for PocketBase can be as little as $4, and runs as many projects as you like. ([5:27](https://youtu.be/WZoC1HA1vec?t=327))

## Hot takes
- The 'just one file' framing understates ops: the data lives in pb_data (data.db plus storage/), so backups and persistent disk are the operator's job.
- The pricing comparison sets a Supabase tier against a bare VPS with no stated workload match, so the 'basically free' claim is unquantified.
- The speaker calls it production-ready for a modern SaaS, but also says it is pre-v1 and needs manual migrations. The demo is a small bug tracker and does not test scale, which the speaker himself raises as a question.
- No sponsorship is disclosed. The only self-promotion is a pointer to another Better Stack video and channel subscribe prompts.

## Tools mentioned
PocketBase, SQLite, Go, JavaScript, TypeScript, React, Supabase, Firebase, Render, Railway, OpenCode, Claude Code

## Relevance to our work
- **prosharness** (1/3): If ProsHarness ever needs a small hosted backend for phone-driven approvals, PocketBase's auth, API rules and realtime subscriptions are a plausible fit. Nothing in the talk is about agents. → *Only if the phone-approval UI needs a tiny hosted backend: evaluate PocketBase's realtime subscribe and API rules against the current approach. Not a priority.*
