# Jsonnet & Grizzly: The ULTIMATE Grafana Dashboard Duo!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `E1wi-8w2xdA` · [watch](https://youtu.be/E1wi-8w2xdA) · **date:** 2025-11-02 · **length:** 5:54 · **format:** tutorial · **quality:** 2/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Grafana Labs, Better Stack
- **topics:** observability, dev-tools · **tags:** grafana, grizzly, jsonnet, dashboards-as-code, docker-compose, prometheus, grafana-cloud

> Tutorial on managing Grafana dashboards as code with Grizzly, a CLI that watches Jsonnet source and pushes dashboard changes to Grafana live, with a short Better Stack product plug.

## Summary
The speaker walks through running Grizzly, Grafana's CLI for managing dashboards and alerts from code, in a Docker Compose service that watches a Jsonnet project and updates Grafana on every save. The project builds a two-panel dashboard (CPU and memory) with Jsonnet. Setup needs a Grafana service account with the Admin role and a token passed in as an environment variable. Grizzly is then added to the Jsonnet project through the Jsonnet bundler, the dashboard is exported as an array, and each dashboard gets a UID that Grizzly uses to match it. Edits to panels then show up in Grafana without a refresh or copy-pasting JSON. The video closes by noting that Grizzly can also manage folders, data sources and Prometheus rules on Grafana Cloud. About 2.5 minutes of the 5:54 runtime is a promo for Better Stack's hosted Grafana-style dashboards and incident tooling.

## Key ideas
- **UI-built Grafana dashboards cannot be version controlled and are hard to update across many dashboards, so dashboards should live in code.** — The speaker argues that the Grafana UI does not scale for managing many dashboards. Compiling Jsonnet to JSON and pasting the output into the UI is also clumsy. Grizzly closes that loop by pushing compiled dashboards to Grafana. ([0:00](https://youtu.be/E1wi-8w2xdA?t=0))
- **Run Grizzly as a watcher in Docker (for example in CI) rather than installing the binary locally.** — The docs suggest a different install method, but the speaker prefers Docker because Grizzly fits best in a CI pipeline. The container runs a watch command that recompiles Jsonnet and pushes on any change in the source directory. ([1:10](https://youtu.be/E1wi-8w2xdA?t=70))
- **The Grizzly image has an entrypoint for the grr command, so the Compose command can start with watch.** — The speaker notes that the docs use grr for every command. The image's entrypoint already supplies that, so the Compose command starts with watch. The image also installs Jsonnet and the Jsonnet bundler, so Grizzly can compile a project with its dependencies. ([1:10](https://youtu.be/E1wi-8w2xdA?t=70))
- **Authenticate with a Grafana service account token that has the Admin role.** — The speaker creates a service account in Grafana under Administration, Users and Access, Service Accounts, gives it the Admin role, and generates a token. The token goes into an env file or a secrets store, not into the compose file in plain text. ([2:35](https://youtu.be/E1wi-8w2xdA?t=155))
- **Grizzly needs the project to be laid out as a Jsonnet library, and it errors until the Grizzly library is added.** — The first save produces an error because the project does not match the format Grizzly expects. Installing the Grizzly library with the Jsonnet bundler fixes this and places Grizzly under the vendor directory. ([4:01](https://youtu.be/E1wi-8w2xdA?t=241))
- **Each dashboard needs a UID, and that UID must match the name used in grizzly dashboard new.** — The speaker exports a dashboards array and creates each entry with grizzly dashboard new plus an ID. The UID is set on the dashboard itself so the dashboard can be matched, and then edits to panels appear in Grafana in near real time. ([4:01](https://youtu.be/E1wi-8w2xdA?t=241))
- **Dashboard source can be split into separate files, with UIDs kept apart from dashboard code.** — The speaker suggests keeping each dashboard in its own Jsonnet file, with UIDs in a separate variable. This keeps the main file small. Panel definitions and PromQL expressions sit in their own file, panels.libsonnet, in this project. ([1:10](https://youtu.be/E1wi-8w2xdA?t=70))

## Techniques
- **Grizzly watch loop in Docker Compose** — Define a service from the Grizzly image with GRAFANA_URL (the speaker uses localhost:5000) and the Grafana token as environment variables. Mount the project root to the source directory inside the container. Set network_mode to host so the container can reach localhost. Set the command to watch so every change under the source directory is recompiled and pushed. Add depends_on only when Grafana runs in the same compose file. Then run docker compose up. *When:* Use it when dashboards are edited locally and need to land in a running Grafana with no manual import, or when a CI job should keep Grafana in sync with the repo.
- **Grafana service account token for Grizzly** — In Grafana, open the side menu, go to Administration, then Users and Access, then Service Accounts. Click Add service account, give it a name, set the role to Admin, then click Add service account token, name the token, and generate it. Copy the token into a secrets store or env file and pass it to the container. *When:* Use it when the Grizzly container needs API access to Grafana. The speaker's flow uses Admin, which is the broadest role. Narrower roles are not covered in the video.
- **Add the Grizzly library through the Jsonnet bundler** — Run the Jsonnet bundler install command for the Grizzly library, which the transcript does not show on screen. Confirm the library lands in the vendor directory. Import it in the main Jsonnet file, create a variable for the dashboard, and export a dashboards array. Each entry calls grizzly dashboard new with an ID and the dashboard variable. Set the dashboard's uid to the same name that appears in the ID. *When:* Use it when Grizzly reports that the project is not in a format it understands. The bundler also brings in project dependencies, so Jsonnet compiles correctly.
- **Split dashboard definitions from the main file** — Keep one Jsonnet file per dashboard, or keep UIDs in a separate variable. Move panel definitions and PromQL expressions into a library file such as panels.libsonnet. Import those files into the main file. *When:* Use it once a project grows past a few dashboards, so the main file holds only composition and UIDs.

## Numbers
- Video length is 5:54. About 2.5 minutes is spent on the Better Stack product plug. ([2:35-4:01](https://youtu.be/E1wi-8w2xdA?t=0))
- The example dashboard has two panels, one for CPU usage and one for memory usage. ([0:00](https://youtu.be/E1wi-8w2xdA?t=0))
- The Grafana URL used in the example is localhost port 5000. ([1:10](https://youtu.be/E1wi-8w2xdA?t=70))

## Hot takes
- Roughly 40 percent of the video is a promo for Better Stack's own hosted dashboard, status page and incident product. That caps quality at 2.
- The tutorial is useful as a short walkthrough, but it skips the exact bundler and Compose snippets, so a reader needs the Grizzly docs to reproduce it.
- The speaker describes Grizzly as fitting best in CI, but the video only shows a local watch loop.

## Tools mentioned
Grizzly (Grafana CLI for dashboards and alerts), Jsonnet, Jsonnet bundler, Grafana, Docker Compose, Prometheus, Grafana Cloud, Better Stack

## Relevance to our work
- **agentos** (1/3): AgentOS L4 uses Prometheus and Grafana, so dashboards-as-code could keep those dashboards versioned. The video shows no agent-specific observability work. → *If Grafana dashboards for AgentOS L4 are built in the UI, try moving one into Jsonnet and Grizzly and check it into the repo.*
