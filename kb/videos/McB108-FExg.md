# WebAssembly 3.0: It's Not Just for Browsers Anymore

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `McB108-FExg` · [watch](https://youtu.be/McB108-FExg) · **date:** 2026-08-02 · **length:** 6:23 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Figma, Google, Adobe, Cloudflare, Fastly, Stack Overflow, npm
- **topics:** sandboxing-execution, infra-cost-scaling, dev-tools · **tags:** webassembly, wasm-3-0, component-model, wasi, edge-computing, cold-start, sandboxing, browser, javascript, explainer

> Kai Explains argues WebAssembly 3.0 (component model plus WASI) makes Wasm a cross-language, server and edge runtime, while JavaScript keeps the DOM and is not being replaced.

## Summary
The host argues that WebAssembly does not replace JavaScript. Its real change is ending the browser's one-language rule, so Wasm now serves server, edge and plug-in use cases beyond the browser. He credits the Wasm 3.0 component model with letting modules written in different languages call each other through a typed contract without glue code, and credits WASI with giving components file, socket, clock and environment access. He presents server-side use as the fastest-growing area, with sub-millisecond cold starts and kilobyte-sized binaries compared with containers, and secure-by-default sandboxing. He is candid about weak spots: immature debugging and source maps, a small library ecosystem, and no direct DOM access, which makes DOM-heavy UIs a poor fit. His advice is to keep front-end work in JavaScript and learn what compiles to Wasm. The evidence is mostly anecdotal or vendor-sourced (Figma, Cloudflare, Fastly), with no benchmarks shown.

## Key ideas
- **Wasm breaks the browser's one-language monopoly rather than replacing JavaScript** — The speaker says the replaced thing was the rule that a browser runs only JavaScript. Wasm lets C++, Rust, Go and C# run in the browser near native speed, and JS keeps its ecosystem (3.2M npm packages, 63%+ of pro devs per the 2025 Stack Overflow survey, as cited). ([0:00](https://youtu.be/McB108-FExg?t=0))
- **The component model is the Wasm 3.0 change that makes modules interoperable** — Before this, a Wasm module was a black box with no standard way to call another module. The component model gives a universal type system so a Rust module can import and call a Go module directly, with no serialization or shared runtime. The speaker compares it to USB-C. ([1:25](https://youtu.be/McB108-FExg?t=85))
- **WASI supplies the OS access that makes Wasm components useful** — WASI, shipped alongside the component model, exposes files, sockets, clocks and environment variables. The speaker's line: Wasm without WASI is a calculator, and Wasm with WASI is a platform. ([1:25](https://youtu.be/McB108-FExg?t=85))
- **Server and edge use is the fastest-growing Wasm segment, driven by cold start and size** — Cited deployments: a spin framework company with 1M Wasm apps deployed, Cloudflare Workers across 300 cities, and Fastly's compute platform. The speaker claims sub-millisecond cold start versus hundreds of milliseconds for a Docker container, and kilobyte binaries with no OS image or runtime. ([2:50](https://youtu.be/McB108-FExg?t=170))
- **Sandboxing is the default property of the format, not an add-on** — Each module runs in its own memory space with no access to anything not explicitly handed to it. The speaker presents this as the reason the format is attractive for untrusted code and plug-ins. ([2:50](https://youtu.be/McB108-FExg?t=170))
- **Tooling and the DOM are the main limits** — Debugging is far from JS with Chrome DevTools, source maps are fragile, and stack traces can be cryptic. The library ecosystem is a fraction of npm. Wasm cannot touch the DOM directly, so each UI update crosses a bridge back into JS, which adds overhead for apps with frequent small DOM updates. ([2:50](https://youtu.be/McB108-FExg?t=170))
- **Verdict: JS keeps the DOM and Wasm takes the rest; do not rewrite the front end** — For content sites, dashboards, or any app where the DOM is the product, the speaker says JavaScript wins today and probably in 2030. His advice is to learn what compiles to Wasm (some Rust, Go, C#, C) and watch the component model. ([4:18](https://youtu.be/McB108-FExg?t=258))

## Techniques
- **Polyglot components via the component model** — Compile separate modules from different languages to Wasm components and let one import another through the component model's typed contract, with no hand-written glue or serialization. The speaker did not show code or the interface syntax. *When:* When you want to combine libraries from different languages, or build a plug-in system where plug-ins can be written in any language that compiles to Wasm.
- **Wasm instead of containers for short-lived edge or per-request execution** — Package the workload as a Wasm module with WASI for the system access it needs, and grant only the capabilities it should have. The speaker's argument: sub-millisecond cold starts, kilobyte binaries, and sandboxing by default. *When:* Latency-sensitive, bursty or untrusted workloads where container cold start (hundreds of ms) is the bottleneck. Measure cold start yourself first; the speaker showed no benchmark.
- **Split UI from logic across the JS/Wasm boundary** — Keep DOM rendering and frequent small DOM updates in JavaScript, and move compute or system-facing logic into Wasm. The speaker's point is that every Wasm-to-DOM call crosses a bridge with a cost, so chatty UI code in Wasm is a bad fit. *When:* Apps that combine a heavy compute core, such as a CAD, design or image engine, with a standard web UI. This is the pattern he credits for Figma's canvas.

## Numbers
- npm has 3.2 million packages ([0:00](https://youtu.be/McB108-FExg?t=0))
- Over 63% of professional developers use JavaScript daily (2025 Stack Overflow Survey, as cited) ([0:00](https://youtu.be/McB108-FExg?t=0))
- Figma's canvas, compiled from C++ to Wasm, loads more than 3x faster (vendor claim) ([0:00](https://youtu.be/McB108-FExg?t=0))
- Wasm apps deployed by the spin framework company: 1 million ([2:50](https://youtu.be/McB108-FExg?t=170))
- Cloudflare Workers runs Wasm at the edge in 300 cities ([2:50](https://youtu.be/McB108-FExg?t=170))
- Cold start under 1 ms for Wasm vs hundreds of ms for a Docker container ([2:50](https://youtu.be/McB108-FExg?t=170))
- Wasm binaries are measured in kilobytes, not megabytes ([2:50](https://youtu.be/McB108-FExg?t=170))

## Hot takes
- JavaScript is not being replaced; the browser's one-language monopoly is what broke, and Wasm turns that into a marketplace.
- Wasm 3.0's component model makes WebAssembly a universal binary format, not just a browser target.
- Do not rewrite your front end in Wasm; for DOM-heavy apps JavaScript wins today and probably in 2030.
- The fastest-growing Wasm use is on the server, not in the browser.
- Wasm's cold-start advantage over containers is a category difference, not a percentage improvement (the speaker's claim, unbenchmarked).

## Tools mentioned
WebAssembly 3.0, Wasm component model, WASI, Spin framework, Cloudflare Workers, Fastly Compute, Docker, Chrome DevTools, npm, React, Figma, Photoshop, Google Earth, Rust, Go, C++, C, C#

## Relevance to our work
- **agentos** (1/3): Wasm's per-module sandbox and fast cold start are a possible alternative isolation backend for Crucible's opt-in code execution. The talk gives no benchmark or security analysis. → *Spike a Wasm (WASI) execution backend for Crucible's exec path and benchmark cold start and per-call overhead against the current celld/container path before choosing it.*
