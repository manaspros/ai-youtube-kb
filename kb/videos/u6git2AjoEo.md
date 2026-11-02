# Jsonnet & Grafonnet: Automate & Scale Grafana Dashboards Like a PRO

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `u6git2AjoEo` · [watch](https://youtu.be/u6git2AjoEo) · **date:** 2025-11-02 · **length:** 5:02 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Google, Grafana Labs, Better Stack
- **topics:** observability, dev-tools · **tags:** jsonnet, grafana, grafonnet, dashboards-as-code, prometheus, promql, jsonnet-bundler, node-exporter, infrastructure-as-code

> A five-minute tutorial on defining Grafana dashboards in Jsonnet with the Grafonnet library, so they can be version-controlled, generated and reused instead of hand-built in the UI.

## Summary
The presenter argues that dashboards built in the Grafana UI cannot be version-controlled, wired into CI/CD, or generated per data source, and proposes writing them as Jsonnet, a JSON superset with functions, variables, imports, loops and a standard library. Setup is a Jsonnet binary (C++ or the faster Go build), the jsonnet-bundler package manager, and optionally the VS Code language server. The demo then installs Grafonnet, Grafana's Jsonnet library, and builds a dashboard with two time-series panels (CPU and memory) backed by Prometheus, scraped from node exporter. Repeated panel code is pulled into a lib/ directory of .libsonnet files that expose only the constructor functions. The compiled JSON is pasted into Grafana's import dialog. The closing position is that the UI suits prototyping and Jsonnet suits managing many dashboards at scale, with Grafana Tanker mentioned for Kubernetes manifests. The video contains a short sponsored Better Stack segment and no benchmarks or real-scale evidence.

## Key ideas
- **Grafana UI dashboards cannot be version-controlled, put through CI/CD, or generated dynamically per data source, so define them as code.** — The presenter's core motivation. Jsonnet is described as a JSON superset that compiles to JSON or YAML, with functions, variables, imports, loops, conditionals and a standard library. ([0:00](https://youtu.be/u6git2AjoEo?t=0))
- **Jsonnet tooling is a compiler plus a package manager plus an editor server.** — Install the C++ jsonnet or the Go implementation (the speaker says Go is orders of magnitude faster in some cases), the jsonnet-bundler (jb) package manager, and optionally the VS Code language server. ([0:00](https://youtu.be/u6git2AjoEo?t=0))
- **Grafana dashboards are plain JSON, so Jsonnet output can be imported directly.** — Dashboards can be exported and imported as JSON, which makes a generated JSON file a valid import. Grafonnet is Grafana's library for building dashboards from Jsonnet. ([1:18](https://youtu.be/u6git2AjoEo?t=78))
- **A panel is an object built by a function, and objects are merged with +.** — The presenter's helper methods return JSON objects, and the + operator merges them into one object. Panels are time-series with a title, targets (datasource ID plus PromQL), gridPos-style width and height, and a unit. ([1:18](https://youtu.be/u6git2AjoEo?t=78))
- **Parameterize query targets with a function to avoid copy-paste across modes.** — A function takes the CPU mode as an argument, injects it into the PromQL, and builds the legend from it. A Prometheus datasource variable is then added to the dashboard. ([2:27](https://youtu.be/u6git2AjoEo?t=147))
- **Shared panel code goes in a lib directory of .libsonnet files that export only chosen functions.** — The lib/ directory is added to the jpath so the main file can import panel constructors. The presenter says .libsonnet is the preferred extension, though .json still works. ([3:32](https://youtu.be/u6git2AjoEo?t=212))
- **The presenter's split: UI for prototyping, code for managing many dashboards.** — The argument rests on the hypothetical of changing alert thresholds across tens or hundreds of dashboards after new SLOs. No measurement or real-scale example is shown. ([4:39](https://youtu.be/u6git2AjoEo?t=279))

## Techniques
- **Install the Jsonnet toolchain** — Install the Go jsonnet binary (or the C++ build), then install jsonnet-bundler (jb) as the package manager. Optionally add the Jsonnet language server to VS Code. The speaker shows no exact install commands on screen, so use the upstream docs for those. *When:* Before starting any Jsonnet-based config project.
- **Compile Jsonnet to JSON with a jpath flag** — Create a .jsonnet file, then run jsonnet on it, passing the vendor directory (and later lib/) through the jpath flag (-J) so imports resolve. Pipe or redirect the output to a .json file for Grafana import. *When:* Each time a dashboard is regenerated from its source file.
- **Bootstrap Grafonnet with jb** — Run jb init to create the project's jsonnetfile.json, then run the jb install command for Grafonnet. This creates a vendor/ directory, a jsonnetfile.lock.json, and an entry in jsonnetfile.json. Import it as a variable (the speaker uses grafana) and build with its dashboard and panel helpers. *When:* Starting a new dashboard-as-code project that uses Grafana's helper library.
- **Build a time-series panel with Grafonnet helpers** — Create a dashboard with a description and time settings, then add a timeseries panel with a title, a target that carries the Prometheus datasource UID and a PromQL expression, plus width, height and unit. Merge helper outputs with the + operator. *When:* Defining each panel in code rather than in the UI.
- **Generate repeated targets with a function** — Write a function that takes a parameter (the speaker uses CPU mode), inserts it into the PromQL string, and uses it as the legend. Call the function once per variant, and expose a Prometheus datasource variable for the dashboard. *When:* Multiple series differ only by a label value, such as CPU modes.
- **Factor panels into a lib/*.libsonnet module** — Move reusable panel constructors into lib/<name>.libsonnet, expose only the functions to be used, import the module in the main file, and add the lib directory to the jpath when compiling. Keep the main file as a short composition of panels. *When:* The same panel code appears in more than one place or dashboard.
- **Use the $ and self references in Jsonnet objects** — Inside an object, self refers to the current object's fields, and $ refers to the top-level object. The last expression in a file is the output, so no return keyword is needed. Local variables and functions are declared with local. *When:* Writing reusable Jsonnet objects that reference shared values or nested fields.

## Numbers
- The Go Jsonnet implementation is described as orders of magnitude faster than the C++ one in some use cases. No measurement is shown. ([0:00](https://youtu.be/u6git2AjoEo?t=0))
- The demo produces two dashboard panels, CPU usage and memory usage, with the memory panel querying total RAM and used RAM. ([3:32](https://youtu.be/u6git2AjoEo?t=212))
- Full video runs 5:02 and the sponsored Better Stack segment is at about 2:27 to 2:50. ([2:27](https://youtu.be/u6git2AjoEo?t=147))

## Hot takes
- The Grafana UI cannot be version-controlled or wired into CI/CD (speaker's framing, not demonstrated against any alternative).
- Managing dashboards at scale is faster in code. This is asserted with a hypothetical of threshold changes across hundreds of dashboards, with no timing data.
- Sponsored segment for Better Stack (around 2:27) pitches hosted Grafana-style dashboards, status pages and incidents. Quality is capped at 2 for that reason, and the video is thin, at about 5 minutes with no real-world caveats.

## Tools mentioned
Jsonnet, Go jsonnet, C++ jsonnet, jsonnet-bundler (jb), Jsonnet language server (VS Code), Grafana, Grafonnet, Prometheus, PromQL, Node Exporter, Grafana Tanker, Better Stack, VS Code

## Relevance to our work
- **agentos** (1/3): L4 observability uses Prometheus and Grafana. Dashboards-as-code could manage them, but this is a short, basic intro. → *If AgentOS Grafana dashboards get large, prototype one panel set in Jsonnet and check it into the repo. Compare with a plain JSON export first.*
