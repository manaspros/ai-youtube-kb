# WebAssembly vs AWS Lambda vs Cloudflare Workers: Which Actually Performs Best?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `5vCGMrYadBI` · [watch](https://youtu.be/5vCGMrYadBI) · **date:** 2025-11-02 · **length:** 7:26 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack, Fermyon, Cloudflare, AWS
- **topics:** infra-cost-scaling, sandboxing-execution, dev-tools · **tags:** webassembly, wasm, serverless, cold-start, cloudflare-workers, aws-lambda, fermyon-spin, benchmark, v8-isolates, sandbox, opentelemetry

> Better Stack runs one TypeScript app on Fermyon Spin (WebAssembly), Cloudflare Workers and AWS Lambda, comparing latency, recursion limits, sandbox behavior and resource use. Workers win on JS speed, Wasm has the smallest footprint, and the test is small and single-region.

## Summary
The host compiles one simple TypeScript app to WebAssembly with Fermyon Spin and deploys it to Fermyon Cloud, then deploys the same app to Cloudflare Workers and part of it to AWS Lambda (Node.js). He measures hosted latency with a Better Stack monitor pinging each URL every minute from North America, which shows Lambda cold-start spikes above 1 second, Fermyon spikes around 200 ms, and Workers mostly under 50 ms. Local timings show Spin and Wrangler warming up over three calls. For CPU stress he uses recursive and iterative Fibonacci, where recursion crashes Lambda and Spin at 40 and Workers at 50, while iterative runs favor Workers at 100 to 1000 iterations. A security probe that fetches a remote script and runs it with new Function leaks an env secret on Lambda, is blocked by Workers' string-codegen restriction, and is blocked by Spin's default no-outbound-calls rule. Resource checks show Spin at about 0.1% CPU and 91 MB locally, a three-process Workers local stack using much more, and a 12 MB Wasm binary versus an 88 MB Node binary. He concludes that JS/TS backends that do not need Node features suit Workers, while Python, Go or Rust services may benefit from Wasm.

## Key ideas
- **Cold starts drive the tail latency. Lambda had spikes above 1 s, Fermyon Cloud's largest spike was about 200 ms, and Workers mostly stayed under 50 ms but had spikes above 300 ms and cold starts above 100 ms.** — Measured with a Better Stack uptime monitor pinging each app URL every minute from North America only. The speaker attributes the Lambda spikes to cold starts and credits Cloudflare's larger edge network for Workers' speed. ([1:20](https://youtu.be/5vCGMrYadBI?t=80))
- **Recursive Fibonacci separates the runtimes by stack and memory limits. Lambda and Spin handle 10 and 15 but crash at 40. Workers handle 30 and 40 but error at 50.** — The speaker credits Workers' V8 engine for optimizing this recursion and notes that the Spin JS app runs on QuickJS, not V8. Recursion is exponential in time and memory, so this measures limits more than throughput. ([2:46](https://youtu.be/5vCGMrYadBI?t=166))
- **The iterative version reverses the picture on throughput. Lambda handles 30, 50, 200 and 300. Wasm is faster than Lambda at 100 and 200, and Workers beat Spin at 100, 200, 500 and 1000, finishing 1000 in under 0.01 ms.** — Same app and same Fibonacci harness across all three targets, so this is the closest thing to a like-for-like CPU comparison in the video. ([3:45](https://youtu.be/5vCGMrYadBI?t=225))
- **Sandbox behavior differs sharply for fetched code. A probe that fetches a script from a query parameter, builds it with new Function and runs it exposes the env secret on Lambda. Workers refuse code generation from strings. Spin blocks all external calls unless the URL is listed in its manifest.** — Default-deny outbound networking is the Wasm sandbox's main property here. Workers still ran a console.log before failing, so the code got partway in before the codegen restriction stopped it. ([3:45](https://youtu.be/5vCGMrYadBI?t=225))
- **Resource accounting is not comparable across platforms. Hosted Lambda reports about 82% memory and 10 to 45% CPU. Fermyon Cloud exposes only request-over-time metrics, and its OpenTelemetry traces reach Jaeger while Prometheus gets just two metrics.** — Locally, Spin used about 0.1% CPU and 91 MB and stayed under 2% under load. Workers locally run three processes (Node, esbuild, workerd), and their combined CPU and memory is much higher than Spin's. ([4:45](https://youtu.be/5vCGMrYadBI?t=285))
- **Wasm artifacts are small. A Spin Hello World binary is about 12 MB, compared with about 88 MB for a Node.js Hello World compiled to a binary executable.** — Size is one of the main arguments for Wasm in the video, alongside the sandbox and resource results. ([6:12](https://youtu.be/5vCGMrYadBI?t=372))
- **The verdict is language-dependent. A JS or TS backend that does not need Node.js features is a no-brainer for Workers. Python, Go or Rust services may benefit from compiling to Wasm.** — This verdict rests on one JS-heavy workload, so the recommendation for non-JS languages is an inference rather than something the video measured. ([6:12](https://youtu.be/5vCGMrYadBI?t=372))

## Techniques
- **Per-minute uptime probe for latency distribution** — Point an uptime monitor (the video uses Better Stack) at each app URL with a GET every minute, from one region, then read the latency chart and separate steady-state calls from spikes. Pin the region so the platforms are compared on the same footing. *When:* Comparing hosted endpoints across platforms without writing a load generator, and attributing tail spikes to cold starts.
- **Local warm-up timing with repeated curl** — Run `spin watch` to build and serve the Spin app locally, then `time curl` the port three times and compare the first call with later ones (32, 14, 11 ms in the video). Do the same with Wrangler for the Workers app (19, 11, 11 ms). *When:* Checking the cold versus warm local path before testing hosted latency.
- **Recursion vs iteration as a stress test** — Run recursive Fibonacci with increasing n to find where each runtime's stack or memory breaks (40 on Lambda and Spin, 50 on Workers), then switch to iterative Fibonacci and push n up to 1000 to compare throughput. *When:* Finding per-runtime limits (call stack, memory) and separately measuring CPU throughput on the same harness.
- **Eval-injection sandbox probe** — Give the app an endpoint that takes a URL query parameter, fetches the text, parses it, builds a function with `new Function` and runs it. Serve a script that reads an env var secret and check whether it comes back. Record the result per platform: Lambda leaked the secret, Workers threw 'code generation from strings is not allowed', and Spin blocked outbound calls unless the target is declared in the manifest (spin.toml). *When:* Testing whether a sandbox boundary holds for remote or agent-generated code.
- **Host-level resource sampling per process** — Get the server's process ID (the video uses `spin` PID), run a load script, and sample per-process CPU and memory. For Workers local, add up Node, esbuild and workerd, since the stack is multi-process. *When:* Comparing the local footprint of runtimes when hosted metrics are missing or incomplete.
- **OpenTelemetry trace export from a Spin app** — Install the Spin OpenTelemetry plugin. Traces showed up in Jaeger, but Prometheus showed only two metrics and no CPU, memory or disk, so host-level metrics need another source. *When:* Checking what observability a hosted Wasm platform actually gives you before depending on it.

## Numbers
- Lambda latency: most calls under 100 ms, with spikes above 1 second (possibly cold starts) ([1:20](https://youtu.be/5vCGMrYadBI?t=80))
- Fermyon Cloud: largest latency spike about 200 ms, with cold starts below 200 ms ([1:20](https://youtu.be/5vCGMrYadBI?t=80))
- Cloudflare Workers hosted: calls regularly under 50 ms (e.g. 26, 27 ms), spikes above 300 ms, cold starts above 100 ms ([1:20](https://youtu.be/5vCGMrYadBI?t=80))
- Spin local, three sequential calls: 32 ms, 14 ms, 11 ms ([1:20](https://youtu.be/5vCGMrYadBI?t=80))
- Wrangler local, three sequential calls: 19 ms, 11 ms, 11 ms ([2:46](https://youtu.be/5vCGMrYadBI?t=166))
- Recursive Fibonacci limits: Lambda and Spin OK at 10 and 15, crash at 40; Workers OK at 30 and 40, error at 50 ([2:46](https://youtu.be/5vCGMrYadBI?t=166))
- Iterative Fibonacci: Lambda handles 30, 50, 200, 300; Workers faster than Spin at 100, 200, 500, 1000, and 1000 finishes under 0.01 ms ([3:45](https://youtu.be/5vCGMrYadBI?t=225))
- Lambda hosted resource usage: memory about 82%, CPU between 10% and 45% ([4:45](https://youtu.be/5vCGMrYadBI?t=285))
- Spin locally: about 0.1% CPU and 91 MB memory; CPU stays under 2% under load ([4:45](https://youtu.be/5vCGMrYadBI?t=285))
- Wasm binary about 12 MB vs about 88 MB for a Node.js Hello World compiled to a binary ([6:12](https://youtu.be/5vCGMrYadBI?t=372))
- Local Node process memory over 100 MB during Workers test; esbuild CPU above 2% ([6:12](https://youtu.be/5vCGMrYadBI?t=372))

## Hot takes
- The intro says Wasm is faster, lighter and more secure than containers and cites a Docker founder quote. The video never tests containers, so that comparison is unsupported here.
- Methodology is thin: one app, one North America region, three warm calls per platform, and a single Fibonacci workload. The latency ranking is anecdotal.
- The speaker's explanations (Workers' V8 optimizing recursion, Cloudflare's bigger edge network) are speculation the video does not isolate.
- The Lambda runtime and memory configuration behind the recursion crash at 40 are not stated, so the crash threshold is not reproducible from the video.
- The Wasm-for-Python/Go/Rust advice is inferred from a JS-only test. The video does not measure those languages.
- The security test is one payload. It shows the sandbox boundary for that payload, not a general security ranking.

## Tools mentioned
Fermyon Spin (captioned 'Thermian Spin'), Fermyon Cloud (captioned 'Thermian Cloud'), Cloudflare Workers, Wrangler, workerd, esbuild, Node.js, V8 / V8 isolates, QuickJS, AWS Lambda, Better Stack uptime monitors, OpenTelemetry, Jaeger, Prometheus, TypeScript, WebAssembly / WASI, curl, Docker (mentioned in intro only)

## Relevance to our work
- **agentos** (2/3): Crucible is AgentOS's opt-in sandboxed code execution (celld, Cloudflare backend). The video's fetch-then-new-Function probe is a concrete sandbox-escape check, and it contrasts V8 isolate codegen blocking with Wasm's default-deny network. → *Add the video's probe (fetch remote JS, run via new Function, try to read an env secret, try an outbound call) as a regression test for Crucible's celld and Cloudflare backends, and record the result per backend.*
