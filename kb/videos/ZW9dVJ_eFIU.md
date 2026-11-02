# Prisma founder is solving local-first (LiveStore)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ZW9dVJ_eFIU` · [watch](https://youtu.be/ZW9dVJ_eFIU) · **date:** 2025-11-02 · **length:** 6:25 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed in transcript) · **orgs:** Prisma, Cloudflare, Better Stack
- **topics:** dev-tools, agent-architecture · **tags:** local-first, state-management, sqlite, event-sourcing, crdt-sync, cloudflare-durable-objects, react, web-workers

> Prisma founder's LiveStore: a local-first, reactive-SQLite state manager with an immutable event log and git-style push/pull sync, shown via a to-do app on Cloudflare Durable Objects plus D1.

## Summary
The video is a short tool walkthrough of LiveStore, a state management framework from the founder of Prisma. The demo is a to-do app that stays fast and persistent without optimistic-update code, syncing across a normal browser tab and an incognito window. The speaker walks through the architecture: a schema file defines SQLite tables for derived state and clientDocument for local-only state, events describe data changes, and materializers map events to table writes. Queries are built with queryDb and read through a useStore hook, while writes go through store.commit. Sync pushes new events to a sync backend and pulls remote ones, similar to git. The speaker is enthusiastic and gives little detail on sync conflict handling, scaling, or limits, so the evidence is a single demo rather than a benchmark.

## Key ideas
- **LiveStore is a local-first state manager built on reactive SQLite with git-inspired sync, so UI updates are immediate without optimistic-update code.** — The demo shows adds, toggles and deletes updating instantly, with data persisting across page refreshes. Sync to the server happens later in the background. ([0:00](https://youtu.be/ZW9dVJ_eFIU?t=0))
- **Persistence and multi-client sync are handled by the framework, so the app code does not manage the Cloudflare sockets or D1 storage directly.** — The demo app uses Durable Objects for WebSockets and D1 for storage, and the speaker says he did not have to think about either. ([0:00](https://youtu.be/ZW9dVJ_eFIU?t=0))
- **Two kinds of state: synced tables for derived state, and clientDocument for local-only state that can optionally sync across a user's own sessions.** — The input field text is a clientDocument. It survives refresh and can be kept off the server while still syncing between that user's tabs, or kept local to one client. ([1:01](https://youtu.be/ZW9dVJ_eFIU?t=61))
- **All changes are an immutable, ordered event log, and the SQLite state is a projection of that log, which makes it reconstructable and debuggable like git commits.** — Events are named and versioned (for example v1.todoCreated) and carry a schema. The speaker describes this as a debugging aid because every state change is visible in order. ([2:16](https://youtu.be/ZW9dVJ_eFIU?t=136))
- **Materializers are the reducers that map each event to database writes, similar to a Redux action type plus reducer.** — Each event name has a materializer that receives the event payload and performs SQLite writes. ([3:21](https://youtu.be/ZW9dVJ_eFIU?t=201))
- **Reads use queryDb with a label, and writes use store.commit with type-safe event payloads.** — The visible to-dos query reads a filter from UI state and filters out deleted rows. The component gets the store from a useStore hook provided by a LiveStore provider. ([4:33](https://youtu.be/ZW9dVJ_eFIU?t=273))
- **Sync is git-like: push local events to the sync backend, then pull remote events so the client stays up to date.** — The speaker compares this to pushing and pulling in git. The server applies events to its own database through the sync backend. ([5:45](https://youtu.be/ZW9dVJ_eFIU?t=345))

## Techniques
- **Schema-first LiveStore app structure** — Define SQLite tables with SQLite.table for synced derived state, and SQLite.clientDocument for local state (optionally synced across one user's sessions). Define named events with an argument schema, marking each as synced or local. Write a materializer per event name that performs the SQLite writes. Pass the schema to the web worker and wrap React with a LiveStore provider. *When:* Building a local-first app where the UI should update instantly and survive refresh, and changes must sync across a user's devices or tabs.
- **Event-sourced state with materialized projections** — Record every data change as an immutable event with a versioned name. Derive the queryable SQLite state by replaying events through materializers. Rebuild state from the log, or inspect the log to debug changes. *When:* You want an audit trail, reproducible state, or easy debugging of state transitions in a client-side app.
- **Reactive queries via queryDb and store.useQuery** — Create a query with queryDb that returns rows from a table, filtered by fields such as deleted_at or UI state filters. Give it a label. In the component, call store.useQuery with that query and map over the result as normal React state. Use store.commit with a typed event to update data. *When:* Components need live-updating lists driven by local SQLite, with autocomplete and type checking on event payloads.

## Numbers
- No benchmarks, latency figures, or scale numbers are given; the demo is qualitative. ([0:00](https://youtu.be/ZW9dVJ_eFIU?t=0))

## Hot takes
- Local-first, optimistic-update-free state with git-like sync is presented as a major simplification for apps like Notion or Linear, but the video shows only a single demo and gives no detail on conflict resolution or scaling.
- Sponsored or vendor-style enthusiasm: the video is a Better Stack introduction to a third-party framework with no comparison to alternatives.

## Tools mentioned
LiveStore, SQLite, React, Cloudflare Durable Objects, Cloudflare D1, Cloudflare Workers / WebSockets

## Relevance to our work
- **prosharness** (1/3): Event-sourced, replayable checkpoint state is loosely related to ProsHarness checkpoint/resume of long agent runs, but this talk is about client UI state. → *Optional: look at how an event-log projection could model ProsHarness run checkpoints, reading the LiveStore docs on event replay.*
