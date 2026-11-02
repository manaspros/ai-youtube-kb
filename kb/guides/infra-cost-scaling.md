# Guide: infra-cost-scaling

*Synthesized by Sonnet from 97 talks since 2026-05-18.*

## State of the art

Cost is now a first-class constraint. The 2026 survey calls it something teams watch like an SLA (`RGe6EjucbzI`). Leaders talk less about token maxing and more about value per token (`GJX19pNhmSw`, `dSg0pu8d6qg`, `8g1N_a3h9H0`).

What practitioners do now, newest first:

- **Measure before cutting.** Split API keys by team and use case. About 30-40% of customers start with one shared key (`Ti-BmGU1_mQ`). Track spend per key and cut off a key that trends up (`Bck7ABCZRZI`). Attribute cost per agent run, not only per request (`GJX19pNhmSw`).
- **Route by task, not by habit.** Frontier models plan. Cheaper or open-weight models implement. Plain code handles deterministic steps (`-I5W5QVAT8E`, `QHBjufYK8TA`, `48YUYDjwfYY`, `vGCJ7diEtrw`, `TN3mj92oZ8I`). Compare models on cost per task at equal quality, not price per token (`48YUYDjwfYY`).
- **Treat the KV cache as the main cost lever.** Agent prompts are long and mostly repeated. Cache hit rates often pass 90% (`YXowceUKYJI`). The stack is prefix caching, cache-aware routing, tiered KV offload and sometimes prefill/decode split (`Hvb2LfMH58c`, `cQQbJqvZkpo`, `TRe1u7dHYiA`, `_naLJOqVOEI`, `_cRgl3maiT8`).
- **Optimise the task, not the request.** Meta says to use cost per successful task, including retries (`7c9FSUVcXR0`). FriendliAI says the same for latency (`Hvb2LfMH58c`).
- **Gateways hold governance.** One gateway fronts MCP servers or LLM providers for auth, credentials and policy (`CD6R4Wf3jnY`, `zrZ1amZBSPw`). Newer work adds a run-level control plane beside it (`GJX19pNhmSw`).
- **Make reliability a platform job.** The model proposes. A deterministic layer validates and enforces (`APh1Vx0oLmQ`, `cf2IhzqeQH4`). Durable execution covers long runs (`cI7zfqusmFU`, `svCnShDvgQg`).
- **Own inference only once a use case is proven or budgeted.** Rent first, own later (`Bck7ABCZRZI`, `4n08JHb90hI`).

## Consensus patterns

1. **Cache the stable prefix.** Keep the system prompt and tool definitions byte-identical across turns. Put variable text at the end (`65X0pQ6Lmbg`, `ESbWpPT_9-o`, `uiP88SpCi1Q`, `8g1N_a3h9H0`). Cached tokens are about 10x cheaper (`YXowceUKYJI`). Caching also changes compaction math: summaries must shrink context by a large factor to pay off after the cache is lost (`WP3hjUXd918`).
2. **Route to a model sized for the task.** Use a difficulty classifier or task-class rules. Escalate on failure (`vGCJ7diEtrw`, `uiP88SpCi1Q`, `FvxY8oPoI8o`, `TN3mj92oZ8I`). Learn the rules by running best-of-k across models and recording winners per task class (`TN3mj92oZ8I`). Validate routing on your own evals (`FvxY8oPoI8o`).
3. **Send less context.** Input is about 90% of coding cost. A local code index with hybrid search and slim results cut input by a reported 94% (`dRmWYHuIJxM`). Offload big tool results, cap loops, and use a sliding window (`uiP88SpCi1Q`). Check invalid pages before the model reads them. In one example about 70% of tokens were wasted (`XsvUhpnHepE`).
4. **Cap spend in the request path.** Check entitlement and balance before the call. Place a hold, then settle later (`cf2IhzqeQH4`). Add alerts at 50, 70 and 90% of allowance and rate limits to stop loops (`CrqPcIZOOXA`). Give payment agents capped sessions with expiry (`qTZirYu9pr0`, `xKzU_3riL6s`).
5. **Steer first, halt last.** Compact, trim tool output and detect loops before you kill a run (`GJX19pNhmSw`). Bound retries with a budget that tightens as load rises (`sOB3HSiG8vo`, `7c9FSUVcXR0`).
6. **Fallback beats blind retry for LLM APIs.** Retry on a second provider. Pull a failing provider for a few minutes. Set timeouts and P99 per route, not gateway-wide (`zrZ1amZBSPw`). Hedge requests near P90 of the budget (`zrZ1amZBSPw`).
7. **Route on cache locality and load together.** Score replicas on queue depth, KV use and prefix hit. Keep one session on one pod (`YXowceUKYJI`, `cQQbJqvZkpo`, `sOB3HSiG8vo`).
8. **Split prefill and decode with care.** They have opposite profiles (`woIYJYd_etI`, `y2W4FNAuPEA`). Disaggregation is a trade-off. It needs a fast fabric and fits long context and big models (`YXowceUKYJI`). CoreWeave treats it as optional (`cQQbJqvZkpo`).
9. **Plan capacity from the KV budget and the knee.** KV bytes per token set how many users fit (`y2W4FNAuPEA`, `4n08JHb90hI`). Ramp load and report the knee, where throughput flattens and latency jumps (`4n08JHb90hI`, `g4SsanB0gMc`). Use P90 and full distributions, not means (`YXowceUKYJI`).
10. **Right-size with evals.** Prototype on a frontier model. Record a golden set. Pick the smallest model that passes (`fWXJM-J0ZB8`, `Ti-BmGU1_mQ`). Run a ceiling test first so you know the noise floor (`8g1N_a3h9H0`).
11. **Make long runs durable.** Keep the context as an append-only log and snapshot the machine (`svCnShDvgQg`). Or journal each side effect so a crash replays to the failure point (`cI7zfqusmFU`). Hold no compute while idle (`svCnShDvgQg`, `fz6-NS7qpZc`).
12. **Assume hardware fails.** Let crashing jobs restart. Checkpoint every 20-30 minutes (`byn9PURoBNY`). Cordon, replace and requeue on a GPU error (`bRGyYaE0lxI`).
13. **Profile the data path before blaming the model.** One pipeline went from 15% to about 90% GPU use by fixing data loading (`tNAV259UhCM`).
14. **Guard the egress, not only the prompt.** Put a proxy outside the agent. Inject real credentials at the proxy (`MkRYPFIMCSA`). A gateway can also swap credentials per user or team (`CD6R4Wf3jnY`).

## Disagreements & open questions

- **Does routing really save money?** Gains are reported as 25% (`vGCJ7diEtrw`), 40% (`QHBjufYK8TA`) and about 3x on one demo (`FvxY8oPoI8o`). Most are vendor numbers. Panelists also warn that routing by task type is fragile for agents and that small models can cost more out of distribution (`QHBjufYK8TA`).
- **Compaction or full history?** Towards AI found full history beat every compaction preset on recall, cost and latency (`WP3hjUXd918`). Other talks still advise sliding windows and summaries (`uiP88SpCi1Q`).
- **Cheap open models or premium?** Cline argues open-weight models plus a strong harness can win on cost (`CoEIs6Xm8m8`). Notion keeps optionality and tiers traffic (`-I5W5QVAT8E`). Prices may rise if lab subsidies end (`XV2oYi7kojc`).
- **Is a request-level gateway enough?** Microsoft says no, since loops and sub-agents hide at run level (`GJX19pNhmSw`). Twilio shows a request gateway still needs fallbacks, timeouts and shedding (`zrZ1amZBSPw`).
- **Centralised queue or per-worker batching?** Superlinked saw about 2x throughput from a central pull queue (`g4SsanB0gMc`). Its own later talk found per-worker batching gave lower latency (`Ndp5VaqFrl0`). Workload shape probably decides.
- **Is PD disaggregation worth it?** Red Hat shows large tail gains (`YXowceUKYJI`). CoreWeave says it is not cheap enough for every workload (`cQQbJqvZkpo`).
- **Own or rent inference?** Rent before product-market fit, own after (`Bck7ABCZRZI`). The 5090-class local path is a prediction, not a result (`XV2oYi7kojc`).
- **Open question:** how to price and budget agents when one run can fan out. Several talks show the problem and few show data (`cf2IhzqeQH4`, `GJX19pNhmSw`).
- **Caveat on evidence.** Many numbers are vendor claims with no method (`Hvb2LfMH58c`, `7BcQdtRA3Tc`, `GJX19pNhmSw`).

## How thinking changed over time

- **2026-05-18:** Gateways are about MCP access, credentials and observability (`CD6R4Wf3jnY`). Pricing talks say the first price is a hypothesis and push credits (`CrqPcIZOOXA`). Small-model serving gets its own layer (`qdh_x-uRs9g`).
- **2026-06-18:** Infra is the time sink. Serverless GPU tools remove the Docker loop (`zDGHt0LB-dA`). DeepMind names token cost and quota as the top scaling problem (`7gujZrJ9L5I`). Decode is memory-bound, and the harness changes performance (`ESbWpPT_9-o`).
- **2026-07-18:** Reliability becomes an infra problem. Isolation gets a ladder from containers to microVMs (`OqM67QG_Ikk`). Input context is named as most of the coding bill (`dRmWYHuIJxM`).
- **2026-08-18:** Cost becomes a spend and governance story. Survey, Notion and Cline all talk budgets, tiers and open weights (`RGe6EjucbzI`, `-I5W5QVAT8E`, `CoEIs6Xm8m8`). Runaway spend stories spread (`Bck7ABCZRZI`).
- **2026-09-18/20:** Focus moves to the serving fleet. KV-aware routing, control/data plane split and cost per task appear (`YXowceUKYJI`, `sOB3HSiG8vo`, `7c9FSUVcXR0`). Run-level FinOps appears (`GJX19pNhmSw`).
- **2026-10:** Practical playbooks arrive. Measure by key, right-size, buy capacity (`Ti-BmGU1_mQ`). Gate cheaper prompts on paired shadow tests (`8g1N_a3h9H0`). Own-your-inference workshops show the math (`4n08JHb90hI`).

## Numbers worth remembering

- Cached tokens are about 10x cheaper than uncached. Agent cache hits often exceed 90% (`YXowceUKYJI`).
- Agent inputs are 80-90% shared across requests (`cQQbJqvZkpo`).
- Input is about 90% of AI coding cost. Cutting input 94% saves about 61% of total (speaker arithmetic) (`dRmWYHuIJxM`).
- Caching cuts token cost by about 90% or more. Compaction must shrink context by about 50x to pay off after cache loss (`WP3hjUXd918`).
- Five devs on about 8 agents spent about $150k/month on Opus. A cheaper model on one node cut it under $10k (self-reported) (`Ti-BmGU1_mQ`).
- Opus 4.8 at about $1.50 vs GLM 5.2 at $0.27 on one task (vendor demo) (`Hvb2LfMH58c`).
- Reported TokenOps results: spend down about 78%, completion 67% to 96% (vendor) (`GJX19pNhmSw`).
- Self-agreement ceiling about 93%. A cheaper candidate disagreed about 18% (`8g1N_a3h9H0`, synthetic example).
- Agent calls per task: 1 for chat, 10-20 for copilots, about 50 for research agents (`7c9FSUVcXR0`).
- Small-request fleets with top-down routers sit at 20-30% GPU use. A central queue about doubled throughput (`g4SsanB0gMc`).
- Reasoning and router model latency ranged 2 to 60 seconds. Hedge near P90 (`zrZ1amZBSPw`).
- Short-message P99: TCP above 1 ms vs Homa under 100 microseconds (`eZ8WWZzoaR0`).
- GPU use 15% to about 90% after fixing the data path (`tNAV259UhCM`).
- Decode memory budget: 4B model in BF16 is about 8 GB. KV room was about 37,000 tokens on one card (`4n08JHb90hI`).
- 5-10% of users can use about 80% of compute (`CrqPcIZOOXA`).
- S3 P99 for a 256-512 KB object is about 200 ms (`jQDXzEVHMSE`).
- Weight sync: a full checkpoint is about 500 GB. The talk targets a sparse patch of about 500 MB using bit-exact diffs (`maRzp4kImJ4`).
- A 78% rate of at least one critical security mistake across 50 ML setups. Basic controls cost under about 8% overhead (`XjI-AR4pt7Y`).
- A last-seen write grew about 60x with agent traffic and caused a 15-minute latency spike (`lMCxVorb9wM`).
- Voice budget: about 200 ms human turn, trouble past about 800 ms to 1 s (`hMlLw1LeIK8`, `65X0pQ6Lmbg`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Scope: 86 videos in this category. Most are Better Stack tutorials and Kai Explains analysis. No AI LABS video appears in these notes. Almost every claim here comes from one video. Many numbers are vendor or host figures, and several videos are sponsored or vendor-led (Manifest, Context Mode, Claw Patrol, Hookdeck). The checked notes show no sponsor segment, but Manifest's framing is promotional.

Short version: creators treat cost as spend control. They pin providers, measure per request, price by effective cost, and test a claim on one real task before trusting it.

### Practical playbook

1. **Pin providers instead of trusting price-sorted routing.** Add a provider object to the request with a verified `order` list, `require_parameters` set to true, and an explicit `max_tokens`. Check the key names in the vendor docs first; the video names them but does not show the JSON. Leave tool-call requests on the default routing (`ZsnFX5mEJ4s`, 11:50).
2. **Log the endpoint that served each request.** Before you blame the model for a bad or cut-off answer, open the provider log for that request. Compare the endpoint's context and output caps with the model's limits (`ZsnFX5mEJ4s`, 6:22).
3. **Track cached and fresh input tokens separately, per provider.** Compute the cache-hit ratio for each model and provider. Rank providers by effective cost at your real ratio, not list price. The host's example is one provider's price change, so treat the size of the effect as anecdotal (`dXieY9PwvJg`, 4:40; `ZsnFX5mEJ4s`, 9:02).
4. **Split price from volume before you trust a cost trend.** Re-price a fixed traffic snapshot under the old and new price sheets. This shows how much of a change is price and how much is usage (`dXieY9PwvJg`, 2:09 and 5:54).
5. **Pin exact model identifiers and check the vendor changelog on a fixed day.** One vendor retired a model with about four days' notice and silently rerouted traffic. It reversed within a day (`u00vNoI2iQc`, 0:00).
6. **Run a side-by-side test before you adopt a proxy or optimizer.** Use the same model, prompts and clean setup, once direct and once through the proxy. Check request counts to confirm equal work, check answers by hand, and repeat runs. The test in the video was one run per task (`Afm-GNrJbEQ`, 0:00 and 2:37).
7. **Test a new agent harness on a trivial task before a big job.** Run a file read, then tests, then a one-line edit. If tool calls fail, switch the harness before you change the model (`uefMWJ1GBWg`, 6:54).
8. **Size local hardware as weights plus context.** Weights in GB ≈ parameters in billions × bits per parameter ÷ 8. Count every expert in an MoE model. Add headroom for agent context, and measure real memory at the target context length (`ni5P3gT8OXo`, 1:18; `uefMWJ1GBWg`, 4:09).
9. **Count concurrency, not users.** Concurrent requests ≈ users × requests per user per second × seconds per answer. The video's example is 100 users, one request per 600 s, 30 s each, which is about 5 at once. Size for the busiest moment (`ni5P3gT8OXo`; `fXWFSTSvnVM`, 5:03).
10. **Benchmark prefill and decode separately, at several concurrency levels.** Run 1, 8 and 32 concurrent requests and report tokens/s for each. Enable prefix caching when requests share a prompt. Halve the inter-node link to test network sensitivity. Prompt processing is the more network-sensitive number (`SeQ8qou_i-E`, 7:28, 8:48 and 11:28).
11. **Give a small server swap, then cap the build's heap to fit.** Run `sudo fallocate -l 1G swapfile`, `sudo chmod 600 swapfile`, `sudo mkswap swapfile`, `sudo swapon swapfile`, then check with `free -h`. Set `--max-old-space-size` at or below total swap. The video does not persist swap across reboots, so add that yourself (`HU5CV64vLg4`, 5:32 and 8:03).
12. **Shrink Docker images in this order.** Use an alpine base (or distroless if you can). Copy dependency manifests and install before you copy source. Add a `.dockerignore` for `node_modules` and `.env`. Clean up in the same `RUN` that creates the files. Use a multi-stage build (`t779DVjCKCs`, 1:17 to 4:54).
13. **Log one canonical line per request, and sample the noisy ones.** Keep all errors and warnings. Sample high-volume successes. Redact secrets in the collector. Set retention per log type (`I2mWnh66Bkg`, 5:12, 6:09 and 8:45). The speaker's benchmark: Logrus cut throughput about 20%, Go's slog about 3%.
14. **Put processing in the OpenTelemetry Collector, not in the app.** Start with OTLP in, a batch processor, OTLP out, and one pipeline per signal (`4ACQhkJBKyA`, 2:40 and 7:23).
15. **Answer webhooks fast and queue the work.** Vendors time out after about 3 to 5 seconds. Acknowledge, enqueue, then process. Keep a per-vendor latency baseline and alert on drift (`ElaEGr2t9XQ`, 28:05 and 33:02). Host and vendor claims, not measured here.
16. **Test each fallback before you need it, and check who runs it.** An untested fallback fails on the day you need it. Also check whether two "different" providers share one data-center operator, and pick the fallback by who owns the hardware. This is opinion from one commentary video (`e0NvEaJT7cY`, 6:29 and 7:53).

### Tools creators recommend (tool — what for — `video_id`)

- OpenRouter provider routing (`order`, `require_parameters`, `quantizations`) — pin trusted endpoints and set precision floors — `ZsnFX5mEJ4s`
- Manifest — self-hosted drop-in LLM router with deterministic scoring, failover and per-agent cost view (vendor-framed) — `BXme4u4uoyA`
- llama-swap — one OpenAI- or Anthropic-compatible proxy for several local backends, with TTL unload — `GtTzO5ZOQr4`
- FreeLLM API — pooled free-tier keys behind one endpoint with failover; the speaker would not run production on it — `sHOwbyMbun0`
- Claw Patrol (Deno) — gateway credential injection, CEL approve and deny verdicts, request dashboard — `ZiFoTw6doGI`
- Context Mode gateway — hosted Claude Code proxy that folds tool output and adds a command firewall; prompts pass through vendor servers — `Afm-GNrJbEQ`
- Hookdeck Event Gateway and Outpost (open source, Apache 2.0) — webhook buffering, replay and per-vendor latency monitoring — `ElaEGr2t9XQ`
- OpenTelemetry Collector — receivers, processors and exporters that control telemetry volume — `4ACQhkJBKyA`
- Cloudflare Containers — run a heavy binary such as ffmpeg behind a Worker, with idle sleep — `c6TEXxpUEUw`
- Cloudflare Sandbox SDK — isolated exec for AI-generated code — `0bkeZOXNJBg`
- Cloudflare Dynamic Workers — V8-isolate child Workers, JavaScript only, no filesystem; speed claims are not measured in the video — `7Re3HReM5SQ`
- CellD (Deno team) — self-hostable durable objects, one Rust binary plus a storage bucket — `W_g7WKMwNeo`
- JuiceFS — POSIX volume on S3-style storage with a local SSD cache — `ZoBEQWxosGg`
- Postgres extensions (pgvector, PostGIS, pg_cron, UNLOGGED tables) — replace small-app services; not a scale claim — `MZfhhl6ej-k`
- ClickHouse and DuckDB — columnar stores for aggregates; keep Postgres for point lookups — `mR06J55fLvo`
- llama.cpp and vLLM — pick by VRAM headroom; check that vLLM's CUDA graphs built — `sR8sJ2mybQU`
- Headscale — self-hosted Tailscale control plane; setup is involved and the UI is buggy — `8t8FZaBamqA`
- PocketBase — one Go binary with SQLite; needs a persistent disk — `WZoC1HA1vec`
- Bun.Image — built-in image API in Bun 1.3.14, a claimed Sharp replacement on Bun only — `Tnmyb_pdM10`

### Where creators agree or clash with the conference talks

Agree:
- Route by task and use the cheapest model that can do it. Manifest and Kai's hybrid route both say so (`BXme4u4uoyA`, `fXWFSTSvnVM`). This matches "route by task" in State of the art and consensus 2. Both sources warn that the savings are single-demo numbers, as in Disagreements.
- Cache the stable prefix. The DeepSeek and OpenRouter videos show cache-hit economics decide the bill (`dXieY9PwvJg`, `ZsnFX5mEJ4s`). This matches consensus 1. The creators add that cache pricing varies by provider, so the cheapest list price can cost more.
- Rent before you own. Kai's pilot advice and hardware comparisons agree (`fXWFSTSvnVM`, `sR8sJ2mybQU`). This matches the own-or-rent point in State of the art.
- Fallbacks matter. Manifest and FreeLLM both fail over (`BXme4u4uoyA`, `sHOwbyMbun0`). This matches consensus 6, but neither video measures failover latency.

Clash or gap:
- Scaling out. Creators show that tensor-splitting over PCIe can get slower as cards are added (`eckOsa0kBkY`), and that four consumer RTX 3090s gave no gain over two (`sR8sJ2mybQU`). Conference talks on KV-aware routing assume many replicas.
- Prefill and decode on two boxes. One creator mentions a Redditor's split (`gQ7iJuciMg0`). It is unverified and not tested. The conference guide treats disaggregation as a trade-off that needs a fast fabric.
- Isolation claims. Dynamic Workers' 100x and million-per-second claims are unmeasured (`7Re3HReM5SQ`). Conference talks on isolation describe a ladder from containers to microVMs. The creator's claims are not evidence for either side.
- Sizing method. One creator names the method Little's law (`ni5P3gT8OXo`), and another uses the same 100-user arithmetic (`fXWFSTSvnVM`). The conference guide sizes by KV budget and the knee. The two methods agree on the idea. Creators give a simpler form.

### Watch first

- `ZsnFX5mEJ4s` — pin providers, check endpoint caps and rank by effective cost. The best creator evidence on routing. Kai Explains, one video.
- `dXieY9PwvJg` — price times volume, and why cache-hit ratio can outweigh list price. Single host analysis of a news story.
- `Afm-GNrJbEQ` — the side-by-side method for judging a proxy, plus the privacy trade-off. One run per task.
- `ElaEGr2t9XQ` — per-vendor latency baselines and queue-first webhooks. Vendor-led podcast, but the operational points are concrete.
- `ni5P3gT8OXo` — napkin math: weights, headroom and concurrency in under eight minutes.

## Watch first

- `zrZ1amZBSPw` — best practical account of running an LLM gateway: fallback, per-route P99, shedding, fail-open choices.
- `GJX19pNhmSw` — run-level cost control: attribution, steer before halt, out-of-band plane.
- `sOB3HSiG8vo` — why a feedback-loop balancer oscillated and how a control/data plane split fixed it.
- `YXowceUKYJI` — KV-aware routing and PD disaggregation with tail-latency data and honest trade-offs.
- `Ti-BmGU1_mQ` — step-by-step tokenomics: measure, right-size, buy capacity.
- `8g1N_a3h9H0` — a clean method to cut tokens safely: ceiling test, paired shadow stats.
- `4n08JHb90hI` — memory-budget math and finding the concurrency knee on one GPU.
- `cI7zfqusmFU` — durable agent runs: journaled steps, approval as a durable promise, keyed sessions.

## Implications for our projects

**AgentOS Govrix Scout (L1 proxy).**
- Add run-level budgets next to request-level ones. Tag each run, keep a ledger, and use the steer-then-halt ladder (`GJX19pNhmSw`).
- Check balance before the call. Place a hold, then settle (`cf2IhzqeQH4`). This fits the Redis multi-instance counters on the roadmap.
- Add per-provider fallback, per-route P99 and timeouts, and bounded queues with shedding (`zrZ1amZBSPw`). Add a retry budget that tightens with load (`sOB3HSiG8vo`).
- Keep strategy routing rule-based and eval-gated. Log best-of-k results to learn rules (`TN3mj92oZ8I`, `FvxY8oPoI8o`).
- Inject credentials in the proxy so agents never hold secrets (`MkRYPFIMCSA`).

**AgentOS InferCraft (vLLM + Ray on one RTX 5090).**
- Write the KV budget formula into docs and benchmarks (`y2W4FNAuPEA`, `4n08JHb90hI`).
- Report the concurrency knee, P90 and cache-hit tokens separately (`4n08JHb90hI`, `YXowceUKYJI`).
- Test speculative decoding by acceptance rate per workload, not by default (`XTpyNrEgJQ4`, `woIYJYd_etI`).
- Keep the prompt prefix stable in the proxy so cache strategies (LMCache, offload) can pay off (`ESbWpPT_9-o`, `cQQbJqvZkpo`).
- Make the 4-class scheduler workload-aware, as Krea's training-over-inference preemption is (`byn9PURoBNY`, `7c9FSUVcXR0`).
- Quantisation changes need your own eval set before adoption (`4n08JHb90hI`).

**MemoryMesh and Crucible.**
- Index once and query at runtime, and reuse near-identical indexes (`UM6sFg_jdlE`). Test multiscale chunking for hybrid retrieval (`r9OwPx_HoV0`).
- For Crucible, snapshot-and-resume and warm templates fit the cost goal (`fz6-NS7qpZc`, `OqM67QG_Ikk`). Use a short idle timeout.

- Hunt latency stage by stage, and use a thin front hop (`1UmZHb_E_SM`, `g4SsanB0gMc`).
- Use napkin math before benchmarks, and put hot and cold data in tiers (`jQDXzEVHMSE`).
- Precompute read copies at insert time and route reads by consistency class. Use a hidden replica for heavy reports (`lyL5QhgIOxc`).
- Per-segment query budgets with warnings before kills suit trace readers (`uKUA1a0Kdfc`).
- Check high-frequency writes from agent traffic. Coalesce them (`lMCxVorb9wM`).
- Use tiered anomaly detection with per-segment baselines for p95 drift (`u1yaOeEX4e8`).


**ProsHarness.**
- Add a spend ledger per run and a max-iteration cap (`uiP88SpCi1Q`, `GJX19pNhmSw`).
- Checkpoint design maps to a context log plus state snapshot (`svCnShDvgQg`) and journaled steps (`cI7zfqusmFU`).
- Route plan, critique and implement across models by task class, and judge cost per task (`48YUYDjwfYY`, `Ti-BmGU1_mQ`).
- Keep long sessions alive in a remote sandbox (`48YUYDjwfYY`).

**Haiku-style cheap pipelines (entity resolution and similar).**
- Prototype big, deploy small. Build the golden set first (`fWXJM-J0ZB8`, `8g1N_a3h9H0`).
- Put state and rules in code and let the small model only speak or classify (`fnLBmfsI_Fg`).
- Use cheap classifiers and small models in front of the agent (`qdh_x-uRs9g`, `Ti-BmGU1_mQ`).
