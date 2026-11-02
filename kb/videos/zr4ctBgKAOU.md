# OpenTUI: React for Your Terminal, Powered by Bun and Zig

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `zr4ctBgKAOU` · [watch](https://youtu.be/zr4ctBgKAOU) · **date:** 2026-06-02 · **length:** 7:27 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anomaly, Better Stack
- **topics:** dev-tools, coding-agents · **tags:** terminal-ui, tui, react, bun, zig, opentui, ink, opencode

> Walkthrough of OpenTUI, a Zig-core terminal UI library with React and Solid bindings running on Bun, compared against Ink. The speaker builds a small React TUI and argues JSX is the best way to compose terminal UIs.

## Summary
The video introduces OpenTUI, a terminal UI library whose rendering core is written in Zig and which exposes bindings for React, Solid and a framework-free "core" API, all running on the Bun runtime. The speaker says it was built by Anomaly, the team behind the OpenCode coding agent, to replace the Go/Bubble Tea UI they had used, and that it was built on an existing Zig terminal library by another developer. The walkthrough scaffolds a project with a Bun template wizard, explains the custom React reconciler that maps JSX onto terminal boxes and text, and covers screen modes (full screen versus a split footer), Yoga flexbox layout, responsive inputs, box styling, and a timeline hook for row-by-row animation. It then notes Bun APIs such as SQLite, Postgres and fetch are available in the app, and reports the compiled binary is 71 MB but uses under 50 MB of memory at runtime. The closing section argues the three bindings differ mainly in how updates are applied while the drawing is identical, and the speaker prefers OpenTUI over Ink for developer experience despite a heavier footprint than native TUI frameworks. The content is a practitioner-style tool intro with no sponsor segment, but it is shallow on internals and benchmarks.

## Key ideas
- **OpenTUI is a Zig-core terminal rendering library with bindings for React, Solid and a framework-free core.** — All bindings render through the same Zig core, so the drawing is identical. The bindings differ mainly in how component updates are applied. ([0:00](https://youtu.be/zr4ctBgKAOU?t=0))
- **The motivation was Ink's limits when streaming lots of text.** — The speaker says Ink-based apps use over 50 MB for a simple app and have a hard-coded 30 FPS cap, which makes a streaming coding-agent UI feel sluggish. Anomaly had used Go with Bubble Tea for OpenCode and wanted a TypeScript option. ([0:00](https://youtu.be/zr4ctBgKAOU?t=0))
- **Bun's FFI is the performance mechanism that connects TypeScript to the Zig core.** — The TypeScript side calls the native Zig renderer through Bun FFI with little overhead. Layout uses Yoga flexbox, and built-in components include inputs and selects. ([1:12](https://youtu.be/zr4ctBgKAOU?t=72))
- **A React reconciler maps JSX to terminal boxes and text instead of DOM nodes.** — There is no index.html. The entry point creates a CLI renderer and a root that mounts the App component, and JSX box and text elements are laid out with flexbox props. ([2:31](https://youtu.be/zr4ctBgKAOU?t=151))
- **Terminal rendering has quirks that web React does not.** — Inputs can disappear unless given an explicit width. Only fonts the terminal supports render. Animations move row by row, so they look jerky. ([3:47](https://youtu.be/zr4ctBgKAOU?t=227))
- **Built-in timeline hook enables simple terminal animation.** — The speaker animates opacity from 0 to 1 and a top offset from 8 to 0 with a timeline hook, feeding the values into box props. The result is a small fade-in when the view changes on submit. ([3:47](https://youtu.be/zr4ctBgKAOU?t=227))
- **Bun runtime APIs are available inside the app, and the compiled binary is large but light at runtime.** — Bun SQLite, Bun Postgres and fetch can be used directly. The compiled app is 71 MB because it bundles Bun and the React reconciler, yet uses under 50 MB of memory when running. ([5:07](https://youtu.be/zr4ctBgKAOU?t=307))
- **The speaker's conclusion is that framework choice is a developer-experience preference, not a performance one.** — React reruns components and diffs a virtual tree, Solid updates fine-grained, and core mutates objects directly. Because the Zig core does the heavy work, the speaker prefers JSX and picks OpenTUI over Ink every time, while acknowledging it is still heavier than Ratatui or Bubble Tea. ([6:20](https://youtu.be/zr4ctBgKAOU?t=380))

## Techniques
- **Scaffold a React TUI project with the Bun template wizard** — Run the Bun create-TUI wizard as the transcript shows it ("BunCreateTui", likely `bun create tui`), name the project, and pick the React template. The generated index file calls createCliRenderer from OpenTUI and then createRoot to render the App component. Solid and core templates are the other options. *When:* Starting any new terminal app that should be written in React-style JSX.
- **Choose a screen mode** — Default is full screen. Switch to split footer mode with a footer height to pin the render to a reserved region at the bottom of the terminal. *When:* A CLI that needs a persistent input or status area while output scrolls above it, as a coding agent does.
- **Bind input state with useState and onInput** — Hold the value in useState, update it in the input's onInput prop, and render it in a text element. Give the input an explicit width or its text can fail to show. *When:* Any form-like terminal UI, such as a name prompt.
- **Style and lay out with Box props and Yoga flexbox** — Use box props for border and background color and flexbox props for alignment. Place boxes side by side with flex to combine an input panel and an output panel. *When:* Dressing up a terminal screen or building responsive multi-pane layouts that resize with the terminal width.
- **Animate with the useTimeline hook** — Set a duration and targets for opacity and offset, here going from opacity 0 with offset 8 to opacity 1 with offset 0. Feed the animated state values into the box props, which changes the view on a state change such as submit. *When:* Short transition effects on state changes. Expect row-by-row stepping rather than smooth motion.
- **Use other OpenTUI hooks and components** — The speaker names a keyboard hook (useKeyboard), mouse support, virtualized lists, and built-in input and select components. System data comes from the Node OS module, and the app can also use Bun SQLite or Bun Postgres and fetch. *When:* Interactive TUIs that need keyboard navigation, long scrollable lists, or local data without a separate server.
- **Live reload during development** — Save the file and the change appears in the running app without HMR. The transcript does not show the command used to run the dev loop. *When:* Iterating on layout and text during development.

## Numbers
- A simple Ink-based app uses more than 50 MB of memory, and Ink has a hard-coded 30 FPS cap. ([0:00](https://youtu.be/zr4ctBgKAOU?t=0))
- The compiled OpenTUI demo app is 71 MB, including the Bun runtime and React reconciliation, and uses under 50 MB of memory when running. ([5:07](https://youtu.be/zr4ctBgKAOU?t=307))
- OpenTUI is described as powering the OpenCode UI, which the speaker says is used by millions of people. ([0:00](https://youtu.be/zr4ctBgKAOU?t=0))

## Hot takes
- The speaker says JSX is the best and most intuitive way to compose any UI, and would pick OpenTUI over Ink every single time.
- The speaker says frameworks are just a personal preference for OpenTUI, because the Zig core does the heavy lifting.
- The speaker says LLMs know React like the back of their hand, so building OpenTUI apps with them is simple. This is unverified in the video.
- The speaker says the Bun FFI is the clever part that makes OpenTUI performant. No benchmark is shown to support this.

## Tools mentioned
OpenTUI, Zig, React, Solid, Bun, Bun FFI, Yoga, Ink, Bubble Tea, Ratatui (spoken as 'Ratatouille'), Three.js (spoken as '3.js', WebGPU rendering), OpenCode, Go, Node OS module, Bun SQLite, Bun Postgres, Bun create-TUI wizard

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI and could eventually need a terminal dashboard for checkpoints or approvals. The video is an intro with no benchmarks. → *If ProsHarness needs a richer terminal status view, evaluate OpenTUI against Ink with a small spike that streams Claude Code output and measures memory and frame behaviour.*
