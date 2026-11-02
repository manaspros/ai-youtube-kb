# Best Hardware for Running Local LLMs in 2026: Mac vs NVIDIA vs Cloud

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `gQ7iJuciMg0` · [watch](https://youtu.be/gQ7iJuciMg0) · **date:** 2026-09-02 · **length:** 15:29 · **format:** review · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Channel host (Kai Explains; not named in transcript) · **orgs:** Apple, NVIDIA, PNY
- **topics:** local-ai, inference-serving, token-cost-efficiency, infra-cost-scaling · **tags:** local LLM hardware, prefill vs decode, memory bandwidth, unified memory, DGX Spark, Mac Mini M5 Pro, RTX 5090, GPU rental, buy vs rent, GPU price shortage, KV cache, speculative decoding, vLLM, DeepSeek V4 Flash, resale value

> Compares Mac Mini M5 Pro, DGX Spark, RTX 5090 and rented GPUs for local LLMs at current prices, arguing that prefill and decode need different hardware and that renting usually wins on cost.

## Summary
The host opens with Apple's claim of a 4x AI speedup and shows it applies only to time to first token, while memory bandwidth rose about 12.5% (273 to 307 GB/s). He explains that inference splits into prefill (compute-bound, sets time to first token) and decode (bandwidth-bound, sets tokens per second), and that most hardware arguments hinge on which job you are buying for. He then covers the lineup at real street prices: the M5 Pro effectively costs about $3,000 once configured for serious work, the DGX Spark is chosen for its 128GB capacity rather than speed, and the RTX 5090 is fastest but limited to 32GB. Prices have shifted sharply because of a memory shortage, so he argues comparison tables are stale. Renting an RTX 5090 at about $0.69/hour beats buying for most hobbyist duty cycles, and he frames ownership as worth it for privacy, latency and no rate limits rather than cost. Owners who run both prefill and decode on separate machines are the strongest evidence in the video, though much of it comes from Reddit anecdotes that he flags as unverified. Several figures are self-admittedly unconfirmed, including the Spark price and the M5 Pro decode speed.

## Key ideas
- **Apple's 4x AI claim is time to first token only. Memory bandwidth went from 273 to 307 GB/s, about 12.5%.** — The 4x figure is measured on an 8,000-token prompt with a 14B model at 4-bit. The bandwidth increase is what governs how fast a local model writes. ([0:00](https://youtu.be/gQ7iJuciMg0?t=0))
- **Local inference is two jobs with different bottlenecks: prefill and decode.** — Prefill reads the whole prompt in one parallel pass and is mostly compute-bound; it sets time to first token. Decode writes one token at a time, dragging all weights through memory per token, so it is bandwidth-bound and sets tokens per second. The copier analogy is used to illustrate this split. ([1:18](https://youtu.be/gQ7iJuciMg0?t=78))
- **The advertised base price is not the configuration people buy for serious local work.** — The base Mac Mini is $899 with 16GB; the M5 Pro starts at $1,699 with 24GB. Buyers commonly configure 48GB at $2,799 or 64GB at $4,100, so the realistic price is closer to $3,000. ([2:40](https://youtu.be/gQ7iJuciMg0?t=160))
- **On memory bandwidth, the M4 Pro Mac Mini and the DGX Spark were already tied at 273 GB/s a generation earlier.** — The M5 Pro moves to 307 GB/s, so decode gains about 12.5%. The Spark's advantage is capacity (128GB unified memory), not speed. ([3:48](https://youtu.be/gQ7iJuciMg0?t=228))
- **The DGX Spark is useful only when a model will not fit anywhere else, and capacity leaves little margin.** — An owner measured about 240 GB/s real bandwidth against the 273 spec. Two Sparks serving a 304B model with 167GB of weights, at 103 tok/s over four sessions, left only 5 to 7 GB of OS headroom. When memory fills, the box locks up rather than slowing down. ([5:14](https://youtu.be/gQ7iJuciMg0?t=314))
- **GPU and memory prices have moved so much that comparison tables from months ago are obsolete.** — The RTX 5090 launched at $1,999 and street price is around $4,000 this month. The host reports three GPU price hikes of 20 to 30% this year, a 128GB Strix Halo box up 60% since December, and the base Mac Mini rising from $599 to $899. ([7:51](https://youtu.be/gQ7iJuciMg0?t=471))
- **For most hobbyist usage, renting beats buying on cost per token.** — An RTX 5090 rents for about $0.69/hour on community hosts ($0.99 on secure). A $4,000 card equals roughly 5,800 rented hours, which is over five years at three hours a day. Running rented hardware 24/7 for a month costs under $500. ([8:49](https://youtu.be/gQ7iJuciMg0?t=529))
- **The real case for owning local hardware is privacy, a latency floor, no rate limits, and no model deprecation, not cost.** — Rented infrastructure has cold starts of 30 seconds to 3 minutes while weights download. Owners who make the strongest case argue ownership rather than savings. ([10:10](https://youtu.be/gQ7iJuciMg0?t=610))
- **Owners with two machines split prefill and decode across them.** — One Redditor runs prefill on two DGX Sparks under vLLM, decodes on an M3 Ultra, and passes the KV cache between them. The host reports this without testing it himself. ([11:13](https://youtu.be/gQ7iJuciMg0?t=673))

## Techniques
- **Evaluate hardware separately for prefill (TTFT) and decode (tokens/sec)** — Treat time to first token and steady-state decode speed as independent metrics. Expect decode to be capped by memory bandwidth and prefill by compute. Do not use a single headline number for both. *When:* Comparing local inference boxes, or setting latency targets for workloads with long prompts versus long answers.
- **Split prefill and decode across machines** — Run prefill on a compute-dense, capacity-rich box (e.g. DGX Spark on vLLM) and decode on a high-bandwidth box (e.g. Mac). Pass the KV cache between them. This is a Redditor's setup as reported by the host, not verified by him. *When:* You own two different machines and have workloads with long prompts or heavy prefill.
- **Budget memory headroom, not just model fit** — Count weights, KV cache at long context, and the OS. Leave several GB of margin. A 96GB M3 Ultra running 27B at 4-bit peaks around 80GB once context grows, so multiple instances will not fit. Exceeding memory locks the machine rather than slowing it. *When:* Choosing a machine or deciding how many model instances or how much context to run in parallel.
- **Measure real memory bandwidth, not spec sheet bandwidth** — Benchmark actual bandwidth. The owner found about 240 GB/s against a 273 GB/s spec. Use the measured figure to estimate decode speed. *When:* Estimating decode speed before buying, since every current decode number is an extrapolation from spec.
- **Rent-vs-buy break-even calculation** — Hours to break even = purchase price / hourly rental rate. Compare that to your actual hours per day over the hardware's useful life. For always-on use, cost of rental = hourly rate x 720 hours per month. *When:* Deciding whether to buy GPU hardware for an intermittent or constant workload.
- **Size for the model you run this week** — Choose hardware for current models and workloads. Owners who regret purchases sized for future models that did not arrive. *When:* Before buying any local inference machine.
- **Route by workload** — Rent for chat and coding. Use an always-on local box for overnight jobs against local files. Keep a hosted model for the hardest problems, which the owner trusts more. Reported by a user who cut a $300/month API bill to about $40. *When:* Mixing local and hosted inference for cost and quality.

## Numbers
- Apple 4x speedup is time to first token on an 8,000-token prompt with a 14B 4-bit model; memory bandwidth 273 -> 307 GB/s (about 12.5%). ([0:00](https://youtu.be/gQ7iJuciMg0?t=0))
- Base Mac Mini $899, 16GB up to 32GB, 170 GB/s on the base model. M5 Pro $1,699, 24GB base, 307 GB/s, three Thunderbolt 5 ports. ([2:40](https://youtu.be/gQ7iJuciMg0?t=160))
- M5 Pro configured at 48GB/1TB costs $2,799; 64GB/2TB costs $4,100. ([2:40](https://youtu.be/gQ7iJuciMg0?t=160))
- M4 Pro (last year) 273 GB/s, matching the DGX Spark's spec bandwidth. ([3:48](https://youtu.be/gQ7iJuciMg0?t=228))
- DGX Spark: 128GB coherent unified memory, 1.2 kg. Owner-measured bandwidth about 240 GB/s versus 273 spec. ([5:14](https://youtu.be/gQ7iJuciMg0?t=314))
- Two Sparks serving DeepSeek V4 Flash (304B params, 167GB weights): 103 tok/s across 4 concurrent sessions, 5 to 7 GB OS headroom. ([5:14](https://youtu.be/gQ7iJuciMg0?t=314))
- DGX Spark price: $4,699 found in one post with 4,000 views, which the host did not confirm. NVIDIA and PNY pages showed no usable price. ([6:36](https://youtu.be/gQ7iJuciMg0?t=396))
- RTX 5090: 32GB GDDR7 at about 1.79 TB/s. Owner reports about 110 tok/s on a 27B model with speculative decoding; reviewers put it in the mid-90s. ([6:36](https://youtu.be/gQ7iJuciMg0?t=396))
- RTX 5090 launch price $1,999; street price about $4,000 this month; one store listed $5,299. ([7:51](https://youtu.be/gQ7iJuciMg0?t=471))
- Three GPU price hikes this year, each 20 to 30%. A 128GB Strix Halo box is up 60% since December. Base Mac Mini rose from $599 to $899. ([7:51](https://youtu.be/gQ7iJuciMg0?t=471))
- Rental: RTX 5090 $0.69/hr (community) or $0.99/hr (secure); H100 $2.69/hr. Pricing page dated 27 July. ([8:49](https://youtu.be/gQ7iJuciMg0?t=529))
- Break-even: a $4,000 RTX 5090 is about 5,800 rented hours, over five years at three hours a day. The $2,799 Mac Mini config is about 4,000 hours. A month of 24/7 rental is under $500. ([8:49](https://youtu.be/gQ7iJuciMg0?t=529))
- Rented GPU cold start is 30 seconds to 3 minutes while the container pulls model weights. ([10:10](https://youtu.be/gQ7iJuciMg0?t=610))
- M3 Ultra 96GB: a 27B 4-bit model peaks around 80GB at long context, so multiple instances will not fit. ([11:13](https://youtu.be/gQ7iJuciMg0?t=673))
- Resale: an M3 Ultra 512GB bought for $11,000 had a trade-in quote of $2,675. ([12:23](https://youtu.be/gQ7iJuciMg0?t=743))
- Anecdote: an owner cut $300/month in frontier API subscriptions down to about $40 after 10 days on a Spark, while still using hosted models for hard problems. ([12:23](https://youtu.be/gQ7iJuciMg0?t=743))
- M5 Pro Mac Mini ships September 22; the host expects independent decode benchmarks in late September. ([13:44](https://youtu.be/gQ7iJuciMg0?t=824))

## Hot takes
- Apple's 4x is a prefill number; decode moved only about 12%, so the headline misleads for chat-style use.
- Renting a 5090 at $0.69/hr is the correct choice for most hobbyist duty cycles; owning only makes sense for always-on work.
- The usual cost argument for owning local hardware falls apart; the defensible reasons are privacy, latency floor, no rate limits and no model deprecation.
- The DGX Spark is a narrow buy: only worth it when a 100GB+ model has to fit on one small box.
- Top comment's advice, quoted by the host: pay for tokens until the RAM shortage ends.
- Owners and reviewers disagree sharply; the host finds owners far more candid and useful than the reviews.

## Tools mentioned
Mac Mini M5 / M5 Pro (Apple), Mac Mini M4 Pro (Apple, prior generation), Mac Studio, M3 Ultra (Apple), M5 Ultra (Apple), NVIDIA DGX Spark, NVIDIA RTX 5090, NVIDIA H100 (rental), Strix Halo (AMD, 128GB box), vLLM, DeepSeek V4 Flash (304B parameters), speculative decoding (on the 5090 owner's 27B setup)

## Relevance to our work
- **agentos** (2/3): InferCraft runs vLLM on a single RTX 5090 (32GB). The video's prefill/decode split, the 32GB ceiling, and the memory-headroom warning all bear on its KV-cache and scheduler design. → *Report InferCraft prefill TTFT and decode tok/s as separate metrics on the 5090, and reserve an explicit KV-cache and OS headroom so the box degrades rather than locks up near full memory.*
- **prosharness** (1/3): ProsHarness runs long loops and schedules. The rent-vs-buy break-even math and cold-start costs of rented GPUs apply if scheduled runs move to self-hosted models. → *If ProsHarness ever routes scheduled loops to self-hosted models, use the duty-cycle break-even formula (price / hourly rate versus actual hours per day) before buying hardware.*
