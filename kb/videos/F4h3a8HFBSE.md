# Claude Code Is Wasting Your Tokens on This

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `F4h3a8HFBSE` · [watch](https://youtu.be/F4h3a8HFBSE) · **date:** 2026-11-01 · **length:** 5:27 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Better Stack host (unnamed) · **orgs:** Better Stack, Anthropic, T3 Code
- **topics:** token-cost-efficiency, claude-code, observability · **tags:** background-agents, subagents, usage-limits, prompt-caching, opentelemetry, cost-attribution, supply-chain-risk, hidden-llm-calls

> Claude Code's background-agent summaries re-send full conversations every 30 seconds, costing an estimated 2-20% of usage with no off switch; the video gives measurements and workarounds.

## Summary
Better Stack (2026-11-01, 5:27) reports that Claude Code's background-agent panel runs a model call roughly every 30 seconds per working agent whose transcript has changed. Each call sends the whole conversation so far and asks for a 3-5 word status label. The speaker measured this with Claude Code's OpenTelemetry export, tagging requests by query source ("agent summary"). In a sleep-loop test, summaries were about 12% of session cost, with about 40k input tokens and about 130 output tokens per call. In a three-agent TanStack build on Opus, they were about 8% of usage, and they ran on Opus rather than a cheaper model. Anthropic's own figures are lower (about 2% across all telemetry, about 6% in the terminal), while other users reported 8-10%. Because the summaries are not written to the JSONL transcripts, usage tools like ccusage never see them. There is no setting to turn them off. The closest workaround is setting the subagent setting to zero, which removes the summaries but also disables forked subagents, which inherit the full conversation; fresh subagents still run. The speaker also mentions a community Bun preload script that blocks the summary timer, and warns that such scripts should be read and pinned rather than curled from latest. The speaker has moved to T3 Code, which handles summaries differently.

## Key ideas
- **Claude Code makes a hidden model call about every 30 seconds for each working background agent, sending the full conversation to get a 3-5 word status label.** — The calls come from the background-agent panel, not the main status line. They fire on wallclock time for any agent whose transcript changed, so long-running agents compound. ([0:00](https://youtu.be/F4h3a8HFBSE?t=0))
- **The measured cost is large and varies by workload.** — Flamerix estimated 15-20% of usage for a team. The speaker measured about 12% in a sleep-loop session and about 8% in a three-agent Opus build. Community reports fall in the 8-10% range. ([0:00](https://youtu.be/F4h3a8HFBSE?t=0))
- **Summaries are invisible to tools that read JSONL transcripts, so detection needs OTel with query-source tags.** — The speaker sent OpenTelemetry data to Better Stack and grouped requests by query source. CCUsage-style tools never see these calls because they are not logged to the JSONL files. ([1:01](https://youtu.be/F4h3a8HFBSE?t=61))
- **Each summary call re-sends the whole growing conversation, and the summaries ran on Opus.** — In the sleep test, context grew from 18 to 42 messages across five calls about 30 seconds apart, at about 40k input tokens and about 130 output tokens each. In the TanStack test, every summary call ran on Opus, not Haiku. ([1:01](https://youtu.be/F4h3a8HFBSE?t=61))
- **Anthropic's own numbers are lower than the community's, and the cost scales with wallclock time.** — A Claude Code team member said about 2% of cost across all telemetry last week and about 6% in the terminal. A GitHub issue from August measured almost a quarter of requests in one session and is still open. ([2:22](https://youtu.be/F4h3a8HFBSE?t=142))
- **Cache reads are cheap on the API but still count against subscription usage, and Anthropic does not say how much.** — Each summary sends only a small delta, so most input tokens are cache reads at about a tenth of the normal API price. The speaker's point is that subscription usage is still consumed. ([2:22](https://youtu.be/F4h3a8HFBSE?t=142))
- **There is no off switch. The closest workaround is setting the subagent setting to zero, which trades away forked subagents.** — The summaries stop and background agents keep running. Forked subagents, which inherit the whole conversation and its prompt cache, are lost. Normal subagents still start fresh with only their assigned task. ([3:47](https://youtu.be/F4h3a8HFBSE?t=227))
- **A Bun preload script can block the summary timer, but it is risky and needs to be pinned and reviewed.** — The script hooks setTimeout to block the summary timer in every Claude Code process. The install command curls the latest version, so the speaker advises reading it and pinning your own copy. ([3:47](https://youtu.be/F4h3a8HFBSE?t=227))

## Techniques
- **Measure hidden agent-side LLM calls with OTel** — Turn on Claude Code's OpenTelemetry export and send it to any OTel backend. Filter requests by query source (the speaker saw a source labeled 'agent summary') and compare input/output tokens per source. Do not rely on JSONL-based usage tools, which miss these calls. *When:* When session usage burns faster than the visible work explains, or when you want to attribute cost by purpose across a team.
- **Disable background summaries via the subagent setting** — Set the Claude Code subagent setting (the name is not clearly spelled out in the captions; check the docs or the video) to zero. The summary calls drop to zero and background agents still run. Forked subagents are disabled, so subagents start fresh with only their handed task and lose the prompt-cache benefit of inheriting the conversation. *When:* Long-running sessions with many background agents where usage matters more than forked-context inheritance. Benchmark both settings first.
- **Block the summary timer with a preload script (advanced, risky)** — A community Bun preload script hooks setTimeout to block the summary timer across Claude Code processes. Read the full script before installing it, pin a specific copy you have reviewed, and do not install it by curling the latest version. *When:* Only if you accept patching the CLI's runtime behavior and can audit the script. The speaker explicitly calls it hacky.
- **Budget background agents by wallclock time** — Summary overhead is roughly active-agent count times runtime, with a call every 30 seconds per agent whose transcript changes. Keep the number of concurrently running background agents low and stop idle or finished ones, since cost tracks time, not the amount of work done. *When:* When planning how many background agents to run in parallel on a subscription with usage limits.

## Numbers
- Claimed share of subscription usage from background-agent summaries: 5-20% ([0:00](https://youtu.be/F4h3a8HFBSE?t=0))
- Summary calls fire about every 30 seconds per working agent with changed transcript ([0:00](https://youtu.be/F4h3a8HFBSE?t=0))
- Sleep-loop test: 5 summary calls about 30s apart, about 40k input tokens and about 130 output tokens each, summaries were 12% of session cost ([1:01](https://youtu.be/F4h3a8HFBSE?t=61))
- Context in the sleep test grew from 18 to 42 messages across the summary calls ([1:01](https://youtu.be/F4h3a8HFBSE?t=61))
- Three-agent TanStack build on Opus: summaries about 8% of usage, all on Opus ([1:01](https://youtu.be/F4h3a8HFBSE?t=61))
- Anthropic figures: about 2% of cost across all telemetry last week, about 6% in terminal; other users 8-10% ([2:22](https://youtu.be/F4h3a8HFBSE?t=142))
- Flamerix estimate: 15-20% of usage for a team running many background agents ([1:01](https://youtu.be/F4h3a8HFBSE?t=61))
- API cache-read price is about one tenth of normal input price ([2:22](https://youtu.be/F4h3a8HFBSE?t=142))
- A GitHub issue from August measured almost a quarter of all requests in one session ([2:22](https://youtu.be/F4h3a8HFBSE?t=142))
- About 80% of viewers are not subscribed (joke, not a measurement) ([1:01](https://youtu.be/F4h3a8HFBSE?t=61))

## Hot takes
- The summaries are a silent usage tax with no off switch, and running them on the full conversation every 30 seconds is not great design, even if the labels have some value.
- Usage is usage: prompt-cache reads still draw down a subscription, and Anthropic does not disclose how much they count.
- Community preload scripts that curl the latest version and hook every Claude Code process are a security risk; read and pin them.
- The speaker has stopped using Claude Code in the terminal and uses T3 Code, which handles summaries differently (not verified in the video).

## Tools mentioned
Claude Code, OpenTelemetry, Better Stack, ccusage, Bun, T3 Code, TanStack, Claude Opus, Claude Haiku

## Relevance to our work
- **agentos** (2/3): AgentOS budgets and L4 OTel observability should capture side calls the agent makes on its own (here, a background summary call), not just user-driven requests. → *Verify that AgentOS budget and OTel accounting attributes every LLM call by purpose or query source, including agent-initiated background calls, so hidden overhead shows up in the cost dashboards.*
- **prosharness** (2/3): ProsHarness wraps Claude Code for long runs, loops and subagents, so the same hidden per-agent summary calls and forked-subagent trade-offs apply to its runs. → *Instrument ProsHarness runs with OTel and group by query source to measure background-agent overhead. Then benchmark forked vs. fresh subagents for long loops before choosing a default.*
