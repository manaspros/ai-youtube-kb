# This Open-Source Tool Makes Claude Create Architecture Diagrams

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `iuJszJuiuSg` · [watch](https://youtu.be/iuJszJuiuSg) · **date:** 2026-10-02 · **length:** 7:27 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Josh (Better Stack) · **orgs:** Better Stack
- **topics:** coding-agents, context-engineering, dev-tools · **tags:** archify, architecture-diagrams, agent-skills, claude-code, structured-output, json-schema, mermaid, code-review, prs, repo-evidence

> Better Stack walkthrough of Archify, an open-source agent skill where the coding agent emits validated typed JSON that a local compiler renders into HTML architecture diagrams; useful for PR and design-review artifacts, not for READMEs or mapping huge repos.

## Summary
Josh from Better Stack installs Archify, an agent skill (one npx command, no model weights) that works from Claude Code, Cursor and Codex. The agent describes the system as strict typed JSON, Archify validates it (failing closed with diagnostics, rule codes and supported repairs), and only then a local compiler produces self-contained HTML. He tests it with a narrow question about a cache-miss path in a repo, asking for 8-12 nodes and only components that can be proven. Nodes can carry repo evidence (commit plus line range), and the UI supports search, upstream/downstream inspection, route playback, PNG export and a share card. He also shows diffing two validated snapshots to see added, removed, moved or rerouted nodes, and recommends committing the JSON so the architecture survives into later sessions. His caveats: it cannot know your real architecture, a valid graph can still describe the wrong system, it does not render inside a README (Mermaid is better there), and it should not be pointed at a huge repo with "map everything". His rule of thumb is one question per diagram file.

## Key ideas
- **The model should not draw the diagram. It emits a typed graph as JSON, that is validated, and only then compiled to HTML. Invalid graphs fail instead of producing a pretty but wrong picture.** — Archify is framed as LLVM for system maps: the agent is the front end, the JSON is the IR, and the HTML is the compiled output. Strict schemas reject unknown fields. ([0:00](https://youtu.be/iuJszJuiuSg?t=0))
- **Ask a narrow question, not for a whole-repo map.** — The example prompt asks for 8-12 nodes about what happens on a cache miss, only boxes that exist in the repo, and omits anything it cannot prove. ([0:53](https://youtu.be/iuJszJuiuSg?t=53))
- **Repo evidence is what separates a checked node from a plausible one.** — Nodes can reference a commit and a line range. Without that proof, a node gets no SRC badge, however convincing the label sounds. ([2:00](https://youtu.be/iuJszJuiuSg?t=120))
- **The layout is left to the compiler, not the model.** — The speaker says a themed Mermaid version with automatic layout was no better than plain Mermaid. ([3:49](https://youtu.be/iuJszJuiuSg?t=229))
- **Diffing validated snapshots is the stronger use case for code review.** — Given a before-state and an after-state (for example, adding a retry worker), Archify reports added, removed, moved and rerouted nodes, rather than two independently generated pictures. ([3:49](https://youtu.be/iuJszJuiuSg?t=229))
- **Commit the JSON to keep the architecture alive across sessions.** — The JSON is the editable source of truth. The HTML and PNG are outputs. The speaker prefers to keep the JSON in version control. ([3:49](https://youtu.be/iuJszJuiuSg?t=229))
- **Clear limits: Archify does not know your architecture, and it does not render in READMEs.** — A valid graph can still describe the wrong system. GitHub renders Mermaid inside a README, but not Archify HTML. Pointing it at a huge repo with a vague question produces garbage. ([4:59](https://youtu.be/iuJszJuiuSg?t=299))
- **Rule of thumb: one question per diagram file.** — If you cannot say which question the diagram answers, do not generate it. ([6:07](https://youtu.be/iuJszJuiuSg?t=367))

## Techniques
- **Schema-validated diagram IR** — Have the agent emit architecture as strict typed JSON (unknown fields fail). Validate it with a separate step that returns diagnostics (rule codes plus supported repairs). Only a valid graph is compiled to HTML by a local compiler. Commit the JSON as the editable source. *When:* When the diagram will be reviewed, shared or reused in later agent sessions, and you need it to stay accurate rather than just look good.
- **Evidence-gated nodes** — Require each node to cite repo evidence (commit plus line range). Nodes without it are not given the verified badge, regardless of how plausible the label is. *When:* When the architecture answer has to be checkable against code, for example in a PR.
- **Narrow architecture question prompt** — Prompt along these lines: 'Use Archify, architecture diagram 8 to 12 nodes max. What happens on a cache miss in this service? Only include boxes that exist in this repo. If you can't prove a component, omit it. Deliver a self-contained HTML.' Keep to one question per file. *When:* Whenever you ask an agent for a diagram. Constrain node count, scope and proof requirements up front.
- **Diff two architecture snapshots** — Generate a validated snapshot before the change and another after it (for example, after adding a retry worker). Compare the two to get added, removed, moved and rerouted nodes and edges, then review that delta. *When:* In code review or design review, to see what a change does to the system's shape.
- **Install as an agent skill** — Install with a single npx command. Since it is a skill rather than an app, the same skill runs from Claude Code, Cursor or Codex. *When:* When you want a diagram tool that fits into the coding agent you already use, with no separate editor.

## Numbers
- Archify has picked up 44,000 GitHub stars in a few months (stated by the speaker). ([0:00](https://youtu.be/iuJszJuiuSg?t=0))
- Typical diagram size target: 8 to 12 nodes for one question. ([0:53](https://youtu.be/iuJszJuiuSg?t=53))
- Share card export is described as 1200 by 36 (as spoken; likely 1200x630). ([2:58](https://youtu.be/iuJszJuiuSg?t=178))
- There are five diagram modes: architecture, workflow, sequence, data flow and life cycle. ([3:49](https://youtu.be/iuJszJuiuSg?t=229))
- Install is a single npx command; there are no model weights, and Node is the only requirement. ([6:07](https://youtu.be/iuJszJuiuSg?t=367))

## Hot takes
- Mermaid is better for README diagrams, since Archify HTML does not render on GitHub.
- A validated architecture graph can still describe the wrong system. You still have to read it.
- Auto-generated architecture from a huge repo is 'a bad question', not a tool failure.
- Do not install Archify just for prettier versions of diagrams you already have. Use it for checked, shareable artifacts in PRs and design docs.

## Tools mentioned
Archify, Claude Code, Cursor, Codex, Mermaid, GitHub

## Relevance to our work
- **agentos** (1/3): Mostly a diagram tool for coding agents, but the validated-JSON-IR-then-compile pattern is relevant to documenting AgentOS's pillars. The agent-facing use is adjacent. → *Consider a JSON schema for the AgentOS pillar architecture (L1-L4), validated in CI, so that generated diagrams cannot drift from the manifest.*
- **prosharness** (1/3): Validated-IR-then-render pattern and diff-two-snapshots for review could apply to ProsHarness plan/critique artifacts. Light relevance only. → *Consider whether ProsHarness plan artifacts should also be typed JSON with schema validation before they are rendered or reviewed.*
