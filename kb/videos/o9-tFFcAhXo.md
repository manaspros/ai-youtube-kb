# Stop Rebuilding Backends… Just Use Directus

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `o9-tFFcAhXo` · [watch](https://youtu.be/o9-tFFcAhXo) · **date:** 2026-05-02 · **length:** 7:49 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Directus
- **topics:** dev-tools, data-engineering · **tags:** directus, headless-cms, backend-as-a-service, sql, rest-api, graphql, permissions, flows, automation, docker, mailpit, self-hosting, low-code

> Better Stack walkthrough of Directus, an open-source data platform that sits on top of an existing SQL database and adds APIs, permissions, an admin UI and flows, built in about 8 minutes from a blank install.

## Summary
The host builds a small order-management backend in Directus from a blank install. They create an "orders" collection in the UI with typed fields (customer, email, a product dropdown, amount, status), add sample rows, lock the public role to read-only, and create a flow that sends an email when a new order is created. The pitch is that Directus wraps an existing SQL database (Postgres, MySQL, Oracle) instead of duplicating it, so there is no migration step and the database stays the source of truth. The host positions it against code-first tools (Strapi, Payload) and GraphQL-focused Hasura, arguing that Directus bundles APIs, admin UI, permissions, files and automations. Listed tradeoffs are that advanced flows take time, docs can be thin, self-hosting means you own maintenance, and complex local setups get messy. The demo does not connect to an existing database, so the "wrap your SQL" path is asserted rather than shown. Overall it is a short tool tour with no benchmarks.

## Key ideas
- **Directus sits on top of an existing SQL database rather than beside it, so there is no duplicate data layer and no lock-in; the full SQL schema stays usable.** — Framed as the core differentiator versus tools that need schemas defined in code and rebuilt inside the tool. Claimed to suit legacy systems. Not demonstrated in the video, which starts from an empty install. ([0:00](https://youtu.be/o9-tFFcAhXo?t=0))
- **The schema is built in the UI, not via migrations or schema files: create a collection, then add typed fields such as a dropdown with key/value options.** — Demo collection is 'orders' with customer, email, product (dropdown), amount and status fields. Changes save immediately in Directus. ([1:01](https://youtu.be/o9-tFFcAhXo?t=61))
- **Access control is set per role in the permissions screen. The demo locks the public role to read-only on the orders collection and turns off create, update and delete.** — The host calls this the main reason to trust the tool and says the permissions 'just work' with no plugins. No security testing is shown. ([2:13](https://youtu.be/o9-tFFcAhXo?t=133))
- **Flows provide event-driven automation on collections: trigger on item creation, then run an operation such as sending an email with the item data in the body.** — Demo flow triggers on a new item in the orders collection and sends an email. The host says there is no backend code involved. Advanced flows are called time-consuming to build. ([3:19](https://youtu.be/o9-tFFcAhXo?t=199))
- **Positioning: Directus is an admin workspace plus APIs, permissions, files and automations, which the host contrasts with code-first Strapi and Payload and with GraphQL-only Hasura.** — Use cases given: SaaS backends, internal tools, headless CMS, AI agents with controlled data, and modernising legacy systems. The comparison is qualitative only. ([5:24](https://youtu.be/o9-tFFcAhXo?t=324))
- **Tradeoffs and when not to use it: docs are sometimes thin, self-hosting means you manage the ops, complex local setups get messy, and it is a poor fit for strict type-first codebases or teams without an existing database.** — The host recommends Payload when everything should be defined in code from the start. ([6:23](https://youtu.be/o9-tFFcAhXo?t=383))

## Techniques
- **Rapid internal backend on an existing SQL database with Directus** — Connect Directus to Postgres, MySQL or Oracle (connection step not shown in the video). Create collections and fields in the admin UI. Define a dropdown field with key/value options. Add rows in the content view. Set permissions per role in the permissions screen. The public role gets read on the collection, and create/update/delete stay off. *When:* You have an existing SQL database and want CRUD APIs, an admin UI and role-based access without writing a backend. Also useful for internal tools and prototypes.
- **Event-driven email notification with a Directus flow** — Create a flow. Set the trigger to 'item created' on the orders collection. Add a 'send email' operation with a subject, a recipient, and a body that pulls in the item fields. Save the flow. For local testing, add Mailpit to the Docker Compose file so emails are caught without being sent. *When:* You need notifications or simple automations on data changes and want to avoid building a worker or webhook service. The video only shows email, not other operations.
- **Local testing of outbound email with Mailpit** — Add a Mailpit service to the project's Docker Compose file and point the Directus mail settings at it (the mail settings are not shown in the video). Trigger a flow and check the captured message in the Mailpit inbox. *When:* Developing flows or any email-sending feature locally, so no real mail goes out.

## Numbers
- Demo data is three sample order rows, and the whole build from blank install to working flow runs in about 4-5 minutes. This is a demo scale, not a benchmark. ([2:13](https://youtu.be/o9-tFFcAhXo?t=133))

## Hot takes
- Directus 'sits on top of' the database and never duplicates it, which the host presents as an advantage over code-first tools. Not backed by evidence in the video.
- The permissions 'just work' and the tool 'scales really well'. Both are asserted with no test, benchmark or load data.
- The host says Directus is not really competing with n8n or Zapier, even though the flow demo looks like them.

## Tools mentioned
Directus, PostgreSQL, MySQL, Oracle Database, Docker Compose, Mailpit, Strapi, Payload, Hasura, n8n, Zapier

## Relevance to our work
- **agentos** (1/3): Passing mention that Directus can serve AI agents with controlled data. A possible reference for admin UI and role-based field permissions, but not a direct input to MemoryMesh or the proxy. → *Skim Directus's role and field-permission model as a reference for per-bucket access control in AgentOS admin tooling. Low priority.*
