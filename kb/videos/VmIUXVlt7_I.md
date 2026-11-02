# This AI Tool Maps Any Codebase Before You Touch It (Understand-Anything)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `VmIUXVlt7_I` · [watch](https://youtu.be/VmIUXVlt7_I) · **date:** 2026-06-02 · **length:** 7:23 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack, Google
- **topics:** claude-code, context-engineering, dev-tools · **tags:** understand-anything, codebase-onboarding, knowledge-graph, static-analysis, guided-tour, impact-analysis, token-cost, claude-max, microservices

> Walkthrough of Understand-Anything, a Claude Code plugin that builds an interactive knowledge graph of a repo for onboarding and pre-change impact checks; the speaker also flags its heavy token cost.

## Summary
The Better Stack host presents Understand-Anything, an MIT-licensed open-source Claude Code plugin (also usable with Cursor, Copilot and Gemini CLI) that scans a repository and turns it into a queryable, interactive knowledge graph using static analysis plus multi-agent LLM processing. The demo runs on a small Google microservices sample repo: after installing the plugin and reloading, the host runs the scan command and then a dashboard command. The scan took about 30 minutes and used roughly 25% of the host's Claude Max rate allowance. The dashboard offers zoom from high-level architecture down to modules and code, search (e.g. "payments"), and a guided tour that walks an entry point, validation, logic, database, external APIs and error handling in order. The host pitches three uses: onboarding onto legacy code, giving coding agents structured architecture context instead of a few guessed-at files, and checking what a change depends on before refactoring. The main claimed difference from IDE dependency graphs is that it explains flows and meaning, not just import edges. The host is skeptical about GitHub-driven hype and stresses that the token cost is real and that the tool does not replace reading the code.

## Key ideas
- **Target use case is onboarding onto an unfamiliar or legacy codebase where docs are stale and the expert has left; a navigable map is pitched as faster than reading 12 pages and asking around.** — The host frames the problem as a large repo that is hard to orient in, and presents the plugin as a way to get a map of flows, architecture layers and business concepts. ([0:00](https://youtu.be/VmIUXVlt7_I?t=0))
- **The plugin builds a queryable interactive knowledge graph from static analysis plus multi-agent LLM processing, not a single-prompt summary.** — The host says the important part is the problem solved (understanding legacy code), not the stack, but describes the pipeline as static analysis combined with several LLM agents. ([0:55](https://youtu.be/VmIUXVlt7_I?t=55))
- **Scanning is expensive: the first full run took about 30 minutes and consumed a large share of a subscription's usage window.** — On a Claude Max plan the scan used about 25% of the rate allowance. The host advises having a strong plan before running it. ([2:00](https://youtu.be/VmIUXVlt7_I?t=120))
- **The dashboard combines architecture zoom, code breakdown, search and a guided tour, so the reader moves from system level down to implementation.** — Search for a concept such as payments pulls routes, services, models and handlers together. The guided tour orders the walkthrough as entry point, validation, logic, database, external APIs, error handling. ([2:00](https://youtu.be/VmIUXVlt7_I?t=120))
- **The claimed differentiator over IDE graph tools is explaining why things connect (which flow, where a request starts, what breaks) rather than only showing that one file imports another.** — The host lists IDE graphs and dependency visualizers as showing structure without meaning, and positions the plugin as adding the flow layer. ([5:17](https://youtu.be/VmIUXVlt7_I?t=317))
- **Feeding the graph to a coding agent is pitched as better context than dumping random files, so the agent is less likely to guess at changes.** — The host argues that an agent that sees three files guesses, while one with a structured map of domains, flows and dependencies has a better chance of a correct first change. ([4:18](https://youtu.be/VmIUXVlt7_I?t=258))
- **Before a refactor, the graph is used to answer what a piece of code depends on, which flow it belongs to, and what might break if it moves.** — This is framed as avoiding turning a one-line change into a large incident. Impact analysis is one of the features people are most excited about. ([4:18](https://youtu.be/VmIUXVlt7_I?t=258))
- **The host's caveats are token cost, the risk that GitHub star counts drive interest, and the fact that the graph is an overview, not a substitute for reading code.** — The project is MIT-licensed, free and incremental, and the host notes it works across several dev environments. ([6:26](https://youtu.be/VmIUXVlt7_I?t=386))

## Techniques
- **Install and run Understand-Anything in Claude Code** — Install via Claude Code's plugin command (the transcript reads as 'plugin, install, understand anything'). Reload plugins, then run the 'understand' command to scan the repo. Afterwards run the dashboard command to open the UI. Exact command spelling is not shown on screen in the transcript. *When:* First run on an unfamiliar repo. Expect a long scan and high token use on the first run; use a plan with headroom.
- **Onboarding order: map, then tour, then questions** — Open the graph and zoom out to the architecture layers. Drill into modules. Run the guided tour (entry point, validation, logic, database, external APIs, error handling). Only then ask the agent targeted questions. *When:* Joining a large or legacy codebase where the docs are outdated.
- **Use the graph as agent context** — Point the coding agent at the generated structured architecture knowledge (domains, flows, dependencies, explanations) rather than pasting random files into the prompt. *When:* Asking an agent to make a change in a codebase it does not yet understand well.
- **Pre-refactor impact check** — Before touching code, query what the module depends on, which flow it belongs to, and what would break if it moved. *When:* Planning a move, rename or refactor in shared code paths.

## Numbers
- Project has over 14,000 GitHub stars within weeks of release. ([0:00](https://youtu.be/VmIUXVlt7_I?t=0))
- Full initial repo scan took about 30 minutes. ([2:00](https://youtu.be/VmIUXVlt7_I?t=120))
- The scan used about 25% of the host's Claude Max rate allowance. ([2:00](https://youtu.be/VmIUXVlt7_I?t=120))
- Demo framing refers to a 200,000-line codebase as a typical onboarding problem; the demo itself used a small-to-medium sample repo. ([0:00](https://youtu.be/VmIUXVlt7_I?t=0))

## Hot takes
- The host asks whether the project is useful or just benefited from the GitHub algorithm, and leaves it open.
- Dependency-graph and IDE visualizers show structure but not meaning, so an LLM-generated flow layer is the real value.
- The tool does not replace reading code; it gives an overview that still needs engineering judgment.
- Token cost is a real drawback; the first run is expensive.

## Tools mentioned
Understand-Anything (open-source Claude Code plugin, MIT license), Claude Code, Claude Max (subscription plan referenced for rate usage), Cursor, GitHub Copilot, Gemini CLI, Google microservices sample repo (demo target)

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI and plans long runs; a repo map could serve as planning context, but the token cost is high. → *Run the plugin once on a ProsHarness repo, record token use, and test whether the generated flow graph improves the plan or critique step enough to justify its cost.*
