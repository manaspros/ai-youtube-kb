# The Open-Source Firebase Alternative Might Be Better (AppWrite)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `PuH4Wq5Smwg` · [watch](https://youtu.be/PuH4Wq5Smwg) · **date:** 2026-04-02 · **length:** 6:30 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Appwrite, Google (Firebase), Supabase, Cloudflare
- **topics:** dev-tools, infra-cost-scaling · **tags:** appwrite, firebase-alternative, self-hosting, baas, docker, docker-compose, mariadb, realtime-database, auth, flutter

> Better Stack walkthrough of self-hosting Appwrite, an open-source Firebase alternative, with a Docker Compose setup, a to-do app sync demo, and trade-offs versus Supabase and Firebase.

## Summary
The video presents Appwrite as an open-source, self-hostable replacement for Firebase, covering auth, a realtime database, storage, serverless functions, and messaging. The host starts Appwrite with a Docker Compose command (the exact command is not shown in the transcript), creates a project, adds a localhost web platform, and builds a to-do collection with role-based permissions. A two-tab demo shows data syncing between a logged-in and a logged-out client. The pitch is cost control and data ownership with no per-seat pricing. The stated trade-offs are no built-in global CDN or edge functions (use Cloudflare), a MariaDB backend rather than Postgres, and the need for monitoring at scale. The video names cost-sensitive devs, privacy-focused teams, and Flutter/mobile developers as the audience. It contains no benchmarks or cost figures.

## Key ideas
- **Motivation: Firebase costs rise as an app grows, and the backend is not under your control. Appwrite is pitched as a self-hosted alternative with the same core building blocks.** — Auth, database, storage, realtime and functions are the parts devs keep; the difference is that you run the server (your VPS) and own the data. ([0:00](https://youtu.be/PuH4Wq5Smwg?t=0))
- **Feature set: auth (email, OAuth, magic links, anonymous, MFA), a realtime database mixing document and relational structure, storage with file transforms, serverless functions in 13+ languages, and push/email/SMS messaging.** — Self-hosted or Appwrite Cloud. Teams and AI tools are also mentioned. ([1:05](https://youtu.be/PuH4Wq5Smwg?t=65))
- **Self-hosting is presented as the easy part: a single Docker Compose command brings up the backend, with the dashboard then used to create an account and a project.** — The exact Compose command is not shown in the transcript; the description says to check the video's linked docs. ([1:05](https://youtu.be/PuH4Wq5Smwg?t=65))
- **Backend configuration is done in the dashboard: create a project, add a localhost web platform, create a collection (table) with columns, and set permissions per role.** — The demo uses email, title, content and user ID columns. Permissions are 'any' read-only, with logged-in users getting the remaining CRUD operations. ([2:12](https://youtu.be/PuH4Wq5Smwg?t=132))
- **Client wiring is a few environment variables (endpoint, project ID, database ID, collection/table name) in the app's env file. The demo shows sign-up, task creation, and realtime sync across a logged-in and a logged-out tab.** — No client SDK code is shown on screen; the video says the SDKs are good for React and Flutter. ([3:16](https://youtu.be/PuH4Wq5Smwg?t=196))
- **Pitch: data ownership, no per-seat pricing, and most Firebase/Supabase features are already present. Trade-offs: no built-in global CDN or edge functions (add Cloudflare), a MariaDB base rather than Postgres, and monitoring needed at scale.** — The host positions it between Firebase (expensive as you grow) and Supabase (more moving parts). ([4:25](https://youtu.be/PuH4Wq5Smwg?t=265))
- **Target audience: cost-conscious startups, privacy-focused teams, and Flutter/mobile developers. Requires comfort with Docker.** — The host concedes it is still open source and needs some work to polish, but says the gaps are fixable. ([5:36](https://youtu.be/PuH4Wq5Smwg?t=336))

## Techniques
- **Self-host Appwrite with Docker Compose** — Start Docker, run the Appwrite Docker Compose command (not shown in the transcript; use the linked docs), open the local dashboard, create an account, and create a project. Copy the project ID into the app's env file. *When:* When you want a self-hosted Firebase-style BaaS for a prototype or cost-sensitive app.
- **Register a localhost web platform** — In the project's Web Apps section, add a platform with hostname localhost so that the browser client is allowed to call the backend during development. *When:* Before connecting a local web or React client to a self-hosted Appwrite instance.
- **Per-role collection permissions** — Create a collection (table) with columns such as email, title, content and user ID. Grant 'Any' read access, and give the logged-in role create/update/delete access. The demo uses this to build a shared to-do list. *When:* For simple per-user CRUD data without writing server-side authorization code.
- **Wire the client through env variables** — Store the endpoint, project ID, database ID and table/collection name in the app's env file, then use them in the client SDK configuration. *When:* When connecting a frontend to the backend without hardcoding IDs.

## Numbers
- Serverless functions are supported in over 13 languages. ([1:05](https://youtu.be/PuH4Wq5Smwg?t=65))
- Setup is described as taking only a few minutes, with no benchmark or cost figures given. ([5:36](https://youtu.be/PuH4Wq5Smwg?t=336))
- Appwrite has no per-seat pricing; the host says the Firebase and Supabase features are already present and costs grow with usage. No dollar amounts are given. ([4:25](https://youtu.be/PuH4Wq5Smwg?t=265))

## Hot takes
- The video is a thin tutorial: the Docker Compose command, env var names, and client SDK code are never shown on screen, so the walkthrough is not reproducible from the video alone.
- The cost argument against Firebase and Supabase is qualitative only; no pricing comparison or load numbers are given.
- The host frames Appwrite as the middle option between Firebase and Supabase, but gives no evidence for the 'going into 2026' adoption claim.

## Tools mentioned
Appwrite, Docker, Docker Compose, Firebase, Supabase, Cloudflare, MariaDB, PostgreSQL, React, Flutter, Better Stack
