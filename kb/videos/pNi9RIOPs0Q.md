# GPT-5 Just Killed Claude – Smarter & Cheaper

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `pNi9RIOPs0Q` · [watch](https://youtu.be/pNi9RIOPs0Q) · **date:** 2025-11-02 · **length:** 7:27 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** OpenAI, Anthropic, Better Stack
- **topics:** models-research, coding-agents, token-cost-efficiency · **tags:** gpt-5, gpt-5-mini, gpt-5-nano, codex, claude-opus, pricing, swe-bench, launch-day, next-js, trpc, hallucination

> Hands-on first look at OpenAI's GPT-5 launch (Nov 2025): a few informal coding tests against Claude Opus, plus the pricing and benchmark claims relayed from OpenAI's livestream.

## Summary
The host reacts to OpenAI's GPT-5 launch day, which included GPT-5, Pro, Mini, Nano and Chat variants. He covers the claimed 400k context window, OpenAI's demo repo of one-shot UIs, and per-token prices against Claude Opus. He runs three informal tests in Codex: a physics polygon-ball sim (impressive), a personal-finance dashboard added to an existing Next.js + tRPC + database boilerplate (UI "okay", but the backend wiring worked), and a single-file Flappy Bird clone (playable but the pipes were misaligned). He then reads the benchmark claims from the livestream (SWE-bench, MMMU, AIME, hallucination rate) and gives a verdict that the price makes switching worthwhile. The evidence is one run per task with no repeats, and the benchmark numbers are OpenAI's own figures as relayed by the host.

## Key ideas
- **OpenAI launched five GPT-5 variants on one day (GPT-5, GPT-5 Pro, Mini, Nano, Chat), with a stated 400,000-token context window and positioning as the best model for coding and agentic tasks.** — Host says the context window doubled and reads OpenAI's claims of better reasoning, code quality and one-shotting. Pro is described only as coming soon, so the host did not test it. ([0:00](https://youtu.be/pNi9RIOPs0Q?t=0))
- **The host gives the UI demos from OpenAI's repo a positive read but calls them cherry-picked, then runs his own tests.** — The demos (an OpenAI FM-style page, a ball game, a whiteboard built in one shot) look more polished than earlier models' output, according to the host. He treats them as marketing examples and not evidence of general quality. ([1:04](https://youtu.be/pNi9RIOPs0Q?t=64))
- **The pitch is price. The host compares GPT-5 at $1.25 per million input and $10 per million output tokens with Opus at $15 and $75, which he says makes it roughly 7.5x cheaper while beating Opus on some benchmarks.** — Price comparison uses figures read from the launch and the host's own Opus numbers. He reports that per-token price is the main reason for switching, and does not measure cost per completed task. ([1:04](https://youtu.be/pNi9RIOPs0Q?t=64))
- **On a real Next.js + tRPC + database boilerplate, the model built a finance dashboard in about five minutes. The UI was only okay and it struggled to replace the boilerplate theme, but adding funds updated the state, so the backend and database were wired in.** — The host checked the code and says the model used the tRPC backend. He describes open-source models in the same test as failing to produce usable front-end code or to connect to the backend. ([2:31](https://youtu.be/pNi9RIOPs0Q?t=151))
- **OpenAI claims GPT-5 is better at agentic work in Codex, Cursor, Windsurf and Copilot: it outputs plans, gives progress updates and recaps between tool calls, and is more proactive without pausing for approval.** — These are the vendor's claims, relayed by the host. In his Codex run he saw it initialise git on its own, pause for a couple of minutes, then return a long summary, and fail on an apply-patch command that was not found. ([3:26](https://youtu.be/pNi9RIOPs0Q?t=206))
- **On a single-file Flappy Bird prompt, the game worked, but the pipes were misaligned and the host could not get past one point. He calls the result better than what he had seen from other models but not complete.** — One run of a single-HTML-file prompt, no repeats. Used to show the gap between a working game loop and correct game logic. ([4:34](https://youtu.be/pNi9RIOPs0Q?t=274))
- **The cheaper tiers are positioned for well-defined tasks. Mini is $0.25 input and $2 output per million tokens, and Nano is $0.05 input and $0.40 output. Pro is announced but not yet available.** — The host reads these from the blog post. Routing the simple work to Mini or Nano and keeping the flagship for complex tasks is implied but not tested. ([4:34](https://youtu.be/pNi9RIOPs0Q?t=274))
- **The host reads OpenAI's benchmark claims: GPT-5 (thinking) at 74.9% on SWE-bench against Opus 4.1 at 74.5%, MMMU 84.2% against 78% for Opus 4.1, and AIME at 100% with Python and 94.6% without.** — All numbers are from the vendor's launch materials, read aloud. The host did not rerun them, and he questions one chart's scale, so treat them as unverified claims. ([5:59](https://youtu.be/pNi9RIOPs0Q?t=359))
- **The host highlights a hallucination claim: O3 is said to have produced nearly one wrong fact in four on one benchmark, and GPT-5 is said to have a much lower error rate.** — No exact GPT-5 error rate is given in the video. The claim is that GPT-5 is much better, and the host did not check it. ([5:59](https://youtu.be/pNi9RIOPs0Q?t=359))

## Techniques
- **Same prompt across models, judged by running the output** — Give each model the same prompt in the same coding environment. Judge by running the result and exercising the features, for example checking that adding money updates the dashboard state, and checking the code really calls the backend. Do not judge by screenshots alone. *When:* Comparing coding models on your own codebase before switching a default.
- **Compare models inside the agent harness, not in chat** — The host ran GPT-5 in Codex (a CLI coding agent) for fairness, since Claude Code is the competitor. Look at how the agent behaves across the whole run: git setup, tool-call loop, pauses, recaps, and failed tool calls such as apply-patch. *When:* Evaluating an agent, not a raw model. Tool-use behaviour can matter more than benchmark scores.
- **Tier models by task definition** — Send well-specified, bounded tasks to small models (Mini or Nano class, from the launch pricing), and reserve the flagship for ambiguous or multi-file work. The host only describes this positioning and does not test it. *When:* Designing model routing or cost policy for an agent pipeline. Verify quality on your own tasks before routing.
- **Check the backend, not just the UI** — After an agent builds a full-stack feature, confirm it reads and writes through the existing API layer (here tRPC plus the database) by changing data in the running app and watching it persist. *When:* Accepting agent-written full-stack changes.

## Numbers
- GPT-5 context window 400,000 tokens (stated as doubled). ([0:00](https://youtu.be/pNi9RIOPs0Q?t=0))
- GPT-5 pricing $1.25 per 1M input tokens, $10 per 1M output tokens; Opus $15 input, $75 output (host's figures; he says about 7.5x cheaper). ([1:04](https://youtu.be/pNi9RIOPs0Q?t=64))
- Personal-finance dashboard task built in about 5 minutes in Codex. ([2:31](https://youtu.be/pNi9RIOPs0Q?t=151))
- GPT-5 Mini $0.25 input / $2 output per 1M tokens; Nano $0.05 input / $0.40 output per 1M tokens. ([4:34](https://youtu.be/pNi9RIOPs0Q?t=274))
- SWE-bench: GPT-5 (thinking) 74.9% vs Opus 4.1 74.5% (vendor figures; host says the price gap is about 8x). ([4:34](https://youtu.be/pNi9RIOPs0Q?t=274))
- MMMU: GPT-5 84.2% vs Opus 4.1 78%. ([5:59](https://youtu.be/pNi9RIOPs0Q?t=359))
- AIME: GPT-5 100% with Python, 94.6% without; Opus 4.1 quoted at 78%. ([5:59](https://youtu.be/pNi9RIOPs0Q?t=359))
- Hallucination: O3 said to have hallucinated nearly 1 in 4 facts on one benchmark; GPT-5 said to be much lower (no exact figure). ([5:59](https://youtu.be/pNi9RIOPs0Q?t=359))

## Hot takes
- Title says GPT-5 'Just Killed Claude', but the video's own tests are single informal runs, so the verdict rests on price more than on measured quality.
- The host's Flappy Bird and dashboard results are mixed. He calls the UI 'okay' and 'not mind-blowing' while still recommending a switch for price.
- The benchmark numbers come from OpenAI's livestream and are read aloud without being checked. The host also questions the scale of one chart.
- The 'open-source models failed' claim is asserted without showing the runs.
- Quality is capped at 2 because the title is hype and the substance is thin: one run per task, vendor numbers relayed, and no repeats or cost-per-task measurement.

## Tools mentioned
GPT-5, GPT-5 Pro, GPT-5 Mini, GPT-5 Nano, GPT-5 Chat, Codex, Claude Opus 4.1, Claude Opus, OpenAI O3, Cursor, Windsurf, GitHub Copilot, OpenRouter, Next.js, tRPC, Polygon Ball test prompt

## Relevance to our work
- **agentos** (1/3): Tiered pricing for small versus flagship models is relevant to L1 strategy routing and budgets, but this video gives only launch prices and single-run anecdotes, with no routing data. → *When adding cost-based routing, add per-model price entries for the GPT-5 Mini and Nano tiers and benchmark them on your own well-defined tasks before routing traffic to them.*
- **prosharness** (1/3): ProsHarness uses Codex in its plan critique step, and this video runs Codex as a coding agent. The comparison is anecdotal, but it shows where agent behaviour (pauses, failed tool calls, recaps) can be checked. → *Use the same fixed prompt across two models in the Codex harness on a real ProsHarness task and log tool-call failures and pauses, not just final output.*
