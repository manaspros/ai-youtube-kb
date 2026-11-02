# Zero Cold Starts: Serverless AI Agents on Akamai Functions — Thorsten Hans

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Zf_e45GiNCE` · [watch](https://youtu.be/Zf_e45GiNCE) · **date:** 2026-10-11 · **length:** 22:37 · **format:** demo · **quality:** 3/5 · **depth:** intro
- **speakers:** Thorsten Hans · **orgs:** Akamai, CNCF, Bytecode Alliance, Vercel, Linode, Ollama
- **topics:** mcp-and-tools, sandboxing-execution, infra-cost-scaling · **tags:** webassembly, wasm, spin, wasmcp, akamai-functions, edge-computing, serverless, cold-start, mcp-server, wasi, vercel-ai-sdk, agents-at-edge

> Thorsten Hans (Akamai) demos building MCP servers and a Vercel AI SDK agent as WebAssembly apps on Spin, deployed to Akamai Functions for near-zero cold starts and global distribution.

## Summary
The speaker argues that MCP servers and agents need low latency worldwide, and that containers or VMs suffer cold starts of seconds to minutes plus costly over-provisioning. He proposes WebAssembly on the server, using Spin (a CNCF project with a CLI, runtime and SDKs) on Akamai Functions, which he presents as a globally distributed runtime with no cold start per request. He builds a Rust/TypeScript MCP server with the wasmcp CLI, which composes components such as auth off the shelf so the developer writes only tools, resources and prompts. He then deploys it with a single spin aka deploy command, reporting global distribution in about 60 seconds and a generated subdomain, and connects an MCP client to it. Next he builds a TypeScript agent with the Vercel AI SDK that calls an Ollama-hosted model on a Linode GPU instance, explaining that the JavaScript runtime is pre-initialized into a Wasm snapshot to avoid cold-start cost. He reports roughly 820 ms for a full agent loop through the LLM, but the talk has no benchmark methodology and the earlier 33 ms figure came from a failed request. The talk is a product-led walkthrough, so vendor claims such as sub-millisecond cold starts are unverified here.

## Key ideas
- **Region-bound architectures and cold starts hurt agents and MCP servers** — Global users see uneven latency from a single region. Containers or VMs can take seconds to minutes to cold start during sudden scale-ups. Over-provisioning avoids this but wastes cloud spend and energy. ([0:12](https://youtu.be/Zf_e45GiNCE?t=12))
- **WebAssembly as the server-side unit, run on Spin and Akamai Functions** — Wasm binaries are small, portable and fast to start, and the speaker compares them to containers versus VMs. Spin (a CNCF, vendor-neutral project) provides the CLI, WasmTime-based runtime and language SDKs. Akamai Functions is the runtime he runs them on. ([2:36](https://youtu.be/Zf_e45GiNCE?t=156))
- **Compose MCP servers from off-the-shelf Wasm components, so developers write only business logic** — The wasmcp CLI scaffolds a server (Rust, TypeScript or Python), and developers write tools, resources and prompts. Non-functional parts such as OAuth2/OIDC auth come as ready-made components that get composed into the final server. He skipped auth in the demo. ([6:45](https://youtu.be/Zf_e45GiNCE?t=405))
- **One code path for local and production storage** — The Spin key-value store uses SQLite locally and a managed, multi-tenant global store on the platform. The app code does not change, and no credentials need to be handled. ([12:01](https://youtu.be/Zf_e45GiNCE?t=721))
- **Single-command global deploy with per-region health checks** — spin aka deploy pushes the Wasm and manifest as OCI layers. Each region confirms it received and can run the workload, instantiates it, and runs a health check. The platform then issues a public subdomain, which he says takes about 60 seconds. ([13:14](https://youtu.be/Zf_e45GiNCE?t=794))
- **Pre-initialized JavaScript runtime snapshot to keep JS cold starts low** — At build time the runtime loads the interpreter, the user code and its dependencies, then snapshots memory into the Wasm binary. The trade-off is shipping the JS runtime, StarlingMonkey, which he says is about 10 MB. ([18:41](https://youtu.be/Zf_e45GiNCE?t=1121))
- **Latency in the talk is measured end-to-end through the LLM, not per function** — After fixing a user error, the speaker measured an agent loop through a self-hosted model at about 820 to 866 ms. He calls this a more realistic figure than the earlier 33 ms reading, which came from a failed request. ([19:59](https://youtu.be/Zf_e45GiNCE?t=1199))

## Techniques
- **Compose MCP servers from Wasm components** — Scaffold with wasmcp, implement only tools, resources and prompts, build the tool component with make, then compose it with off-the-shelf components (for example auth) into one MCP server that runs under spin up or on the edge. *When:* When you want a standards-based MCP server without writing the HTTP/MCP protocol layer or auth yourself.
- **Snapshot a pre-initialized interpreter into the Wasm artifact** — At compile time, load the JS interpreter and the user code and dependencies, evaluate the global scope, and snapshot memory into the .wasm file. Startup then skips module loading and dependency init. *When:* When per-request cold starts matter more than the extra runtime size in the artifact.
- **Edge-deployed agent using a Wasm framework with a remote model** — Write the agent in TypeScript with the Vercel AI SDK inside a Spin app. Register tools, set a step limit, give the agent a role and instruction, and call a model served on a GPU host (Ollama on Linode in the demo). *When:* When the agent logic is light and you want it close to users while the model stays in one region.
- **Local-to-cloud parity via Spin abstractions** — Use the Spin SDK for HTTP, key-value storage and similar services. Spin maps them to SQLite locally and a managed store on the platform, so no code changes are needed for deployment. *When:* When you want to develop locally and deploy to a different runtime without changing application code.

## Numbers
- Akamai Functions cold start averages under 0.5 ms per request (vendor claim, not benchmarked in the talk) ([3:52](https://youtu.be/Zf_e45GiNCE?t=232))
- Containers or VMs can cold start in seconds up to several minutes under sudden scale-up ([1:24](https://youtu.be/Zf_e45GiNCE?t=84))
- Global deployment takes roughly 60 seconds from spin aka deploy to a live MCP URL ([13:14](https://youtu.be/Zf_e45GiNCE?t=794))
- StarlingMonkey JS runtime is about 10 MB ([18:41](https://youtu.be/Zf_e45GiNCE?t=1121))
- Full agent loop through self-hosted LLM takes about 820 to 866 ms ([19:59](https://youtu.be/Zf_e45GiNCE?t=1199))
- A 33 to 34 ms upstream service time was shown, but that run was a failed request, so it is not a valid latency figure ([18:41](https://youtu.be/Zf_e45GiNCE?t=1121))

## Hot takes
- Over-provisioning containers to hide cold starts is unsustainable for both cloud spend and environmental footprint.
- Proprietary SDKs and deployable units make migrating agent workloads between hyperscalers complex and costly.
- Wasm is to server-side apps what containers are to VMs: smaller, faster to start and more portable.
- Developers should be able to deploy an MCP server or agent with one command and no Terraform or infrastructure setup.

## Tools mentioned
Spin, WasmTime, WASI, wasmcp, Akamai Functions, StarlingMonkey, Vercel AI SDK, Ollama, MCP Inspector, SQLite, OCI registries

## Relevance to our work
- **agentos** (1/3): Wasm/WASI with sandboxed capabilities (permissions granted explicitly) is an alternative isolation model for Crucible's opt-in code execution, though the talk shows no security or isolation benchmarks. → *Read the Spin/WASI capability model and prototype one Crucible exec path as a Wasm component to compare cold start and isolation against the current celld backend.*
