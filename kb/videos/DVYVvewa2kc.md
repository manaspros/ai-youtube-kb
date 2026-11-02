# PostgREST Deletes 80% of Your Backend Code

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `DVYVvewa2kc` · [watch](https://youtu.be/DVYVvewa2kc) · **date:** 2026-05-02 · **length:** 6:05 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Supabase, PostgreSQL
- **topics:** dev-tools, security-guardrails · **tags:** postgrest, postgres, row-level-security, rest-api, docker-compose, swagger, backend-less, supabase, crud, api-design

> Short Better Stack tutorial showing PostgREST turning a Postgres table into a REST API with Row Level Security and Swagger docs, with no backend code, plus its trade-offs.

## Summary
The presenter argues that a Postgres schema can serve as the API itself, using PostgREST (the engine behind Supabase) so that no controllers, ORM, or custom backend are needed. The demo runs three Docker Compose services (Postgres, PostgREST, Swagger UI) around a simple to-do table. Access control is expressed as a Row Level Security policy in SQL, currently a permissive policy for the anon role. From there, curl calls cover GET with filtering and sorting, POST with a JSON body, and auto-generated interactive API docs. The presenter frames the benefit as less duplicated logic and less maintenance, since the API tracks the schema. The caveats given are that heavy RLS adds database load and that complex logic pushes toward SQL functions and views. The recommendation is prototypes, MVPs, and Postgres-centric apps, with a thin backend layer kept for edge cases. The video is short and light on exact commands, so it is an overview more than a reproducible guide.

## Key ideas
- **Postgres schema as the API: PostgREST exposes tables as REST endpoints, so the database replaces a hand-written backend layer.** — The presenter's pitch is that validation, routing, and response shaping otherwise get duplicated across layers. With PostgREST the schema defines the API, and there is no ORM or controller code to maintain. ([0:00](https://youtu.be/DVYVvewa2kc?t=0))
- **Setup is three containers: Postgres, PostgREST, and Swagger UI, started with one docker compose up.** — The compose file wires three services together, and the to-do table is created directly in the database. No server install or dependency setup is needed. ([1:04](https://youtu.be/DVYVvewa2kc?t=64))
- **Authorization lives in the database as Row Level Security policies written in SQL, not in middleware.** — The presenter's point is that auth rules sit next to the data. The demo policy grants the anon role full access (using true with check true), which is open by design for the demo and not a production policy. ([1:04](https://youtu.be/DVYVvewa2kc?t=64))
- **Full CRUD, filtering, sorting and pagination come with no code: GET, POST with JSON, and generated OpenAPI docs in Swagger UI.** — The presenter claims a working API with docs in under a minute. The exact query-string syntax for filters and sorts is not shown on screen. ([2:29](https://youtu.be/DVYVvewa2kc?t=149))
- **The stated trade-off is that heavy RLS usage increases database load, so the policy design has to be planned.** — Complex logic tends to move into SQL functions and views, which the presenter notes some teams like and others dislike. ([4:45](https://youtu.be/DVYVvewa2kc?t=285))
- **Recommended for prototypes, MVPs and Postgres-centric projects; apps with complex logic should keep a thin BFF layer.** — The presenter argues Postgres can still do most of the heavy lifting under a thin layer, and that the database should be the source of truth from which the API falls out. ([4:45](https://youtu.be/DVYVvewa2kc?t=285))

## Techniques
- **Run PostgREST as a REST layer over Postgres via Docker Compose** — Define three services in a compose file: Postgres (holding the schema), PostgREST (pointed at that database), and Swagger UI (for docs). Start all three with docker compose up. The compose file and env keys are not shown on screen; the video shows only the result. *When:* Fast prototypes or MVPs where the data model is mostly CRUD and Postgres is already the system of record.
- **Enforce access with Row Level Security instead of middleware** — Enable RLS on the table and write SQL policies per role. The demo uses a permissive policy for the anon role (using true with check true) to show the flow. For real use, narrow the policy to the rows and operations each role should see. *When:* When authorization rules map cleanly to row ownership or role, and you want auth defined in one place next to the schema.
- **Query and write through HTTP with curl** — GET the table for JSON rows, add filter and sort parameters for narrowing and ordering, and POST a JSON body to insert a row. Use the auto-generated Swagger UI to explore endpoints and schemas. The exact parameter syntax is not shown in the video; check the PostgREST docs. *When:* Quick exploration and frontend integration while the schema is still changing.
- **Keep a thin backend layer for complex logic** — Put multi-step business rules or edge cases in a small BFF service, and let Postgres handle data access, validation via constraints, and policy checks underneath. *When:* When the app has logic beyond CRUD that is awkward to express as SQL functions or views.

## Numbers
- PostgREST has over 26,000 GitHub stars (presenter's figure). ([0:00](https://youtu.be/DVYVvewa2kc?t=0))
- Demo stack is three containers: Postgres, PostgREST and Swagger UI. ([1:04](https://youtu.be/DVYVvewa2kc?t=64))
- The presenter says a full CRUD API with docs comes up in just under a minute. ([2:29](https://youtu.be/DVYVvewa2kc?t=149))
- Video length is 6:05. ([0:00](https://youtu.be/DVYVvewa2kc?t=0))

## Hot takes
- The title's claim that PostgREST deletes 80% of backend code is not quantified anywhere in the video.
- Presented as a fit for prototypes and MVPs; the demo's anon full-access policy would be unsafe in production, and the video does not show a hardened policy.
- The 'stronger security defaults' claim is asserted, not demonstrated; heavy RLS is also called out as a load risk.
- Sold as low-maintenance, but the trade-off of moving logic into SQL functions and views is only raised, not explored.

## Tools mentioned
PostgREST, PostgreSQL, Docker Compose, Swagger UI, Supabase (named as a production user of PostgREST), curl

## Relevance to our work
- **agentos** (1/3): AgentOS L3 storage is Postgres/pgvector, so a PostgREST-style read API could expose parts of that data. It is not relevant to the Rust proxy hot path or the ClickHouse-based telemetry work. → *Optional: evaluate PostgREST plus RLS only for an internal read-only admin or dashboard API over AgentOS Postgres tables; do not put it in the proxy request path.*
