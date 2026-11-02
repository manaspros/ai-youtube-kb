# Claude Mythos is FINALLY here (Fable 5)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Ubazoyagym0` · [watch](https://youtu.be/Ubazoyagym0) · **date:** 2026-07-02 · **length:** 5:55 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed) · **orgs:** Anthropic, OpenAI, Stripe, Cognition, Better Stack
- **topics:** models-research, coding-agents, token-cost-efficiency, governance-compliance · **tags:** frontier-model, benchmarks, pricing, safeguards, data-retention, usage-limits, long-running-agents, vision, ui-generation, claude-max

> Anthropic's Fable 5, a safeguarded Mythos-class model: vendor benchmarks, a one-shot UI test, steep pricing, plan-limit burn, and a 30-day retention requirement. Mostly a reaction to launch claims.

## Summary
The presenter reacts to the launch of Fable 5, which he describes as a Mythos-class model with heavy safeguards. He says it leads on nearly every benchmark in Anthropic's table, citing a roughly 10% jump on SWE-Bench Pro agentic coding and a new Cognition benchmark, Frontier Code, that checks whether produced code actually gets merged. He reports the vendor-claimed Stripe test, a codebase-wide migration of a 50-million-line Ruby codebase in one day, along with claims about staying focused across millions of tokens and vision-only play. In his own tests, Fable 5 rebuilt a website from a single screenshot and built a finance dashboard from an empty folder in about 8 minutes, versus 12 for Opus 4.8 and 15 for GPT 5.5. He judges the Claude-style UI aesthetic favorably and GPT 5.5's UI as weaker, though that is opinion from one prompt. The main concerns he raises are safeguards (vendor-claimed under 5% false positives, and a cyber eval where he reads zero passes with safeguards on), pricing of $10 per million input and $50 per million output tokens, availability limited to Max, Team and Enterprise with a planned removal and then usage credits, faster usage-limit burn than Opus, and a 30-day retention requirement on all traffic. Nearly all the performance evidence is vendor charts plus one anecdotal test.

## Key ideas
- **Fable 5 is presented as a Mythos-class model with added safeguards, and the presenter says it leads on nearly every benchmark in Anthropic's table.** — Cited examples: about a 10% jump on SWE-Bench Pro agentic coding, a claimed lead over GPT 5.5, and a lead on Frontier Code, a Cognition benchmark that checks whether code gets merged. Computer use and Terminal Bench gains are described as marginal. All of this is from charts, not the presenter's own runs. ([0:00](https://youtu.be/Ubazoyagym0?t=0))
- **Long-running work is the claimed differentiator. A vendor-reported Stripe test migrated a 50M-line Ruby codebase in one day.** — The presenter says the model stays focused across millions of tokens and improves its outputs by consulting its own notes. He presents these as vendor and customer claims. ([0:00](https://youtu.be/Ubazoyagym0?t=0))
- **Vision is a second claimed strength: a vision-only harness beats Pokemon FireRed, and a full website screenshot can be turned into a near-copy in one shot with no web search.** — The presenter cloned the Linear site from a screenshot and said it nailed most sections, with SVG animations as the weak spot. He calls it a starting point to iterate from. ([1:22](https://youtu.be/Ubazoyagym0?t=82))
- **A single-prompt comparison of a finance dashboard (front end plus back end, empty folder) is the presenter's main head-to-head.** — Fable 5 was fastest at about 8 minutes, versus 12 for Opus 4.8 and 15 for GPT 5.5. He rates the Claude-style UI highly and says GPT 5.5 is far behind on UI. This is one prompt and one run, and he says he did not prompt for a design style. ([2:33](https://youtu.be/Ubazoyagym0?t=153))
- **Safeguards are aggressive. Refusals are expected, and the system may route a request to Opus 4.8 first to check whether it is safe.** — Vendor claim: under 5% of messages are false positives. In a cyber eval the presenter reads zero passes with safeguards on, versus about 88% for Opus as he recalls it. Cyber-adjacent work is restricted except in a special enterprise program. ([3:48](https://youtu.be/Ubazoyagym0?t=228))
- **Pricing is $10 per million input tokens and $50 per million output tokens. Availability and limits are the real cost issue.** — Access starts on Max, Team and Enterprise plans, with a removal date of June 23 and usage credits after that. The model is said to burn usage limits about twice as fast as Opus, and the presenter says the plan return date is undetermined. ([3:48](https://youtu.be/Ubazoyagym0?t=228))
- **A 30-day retention requirement applies to all traffic on first-party and third-party tools. Anthropic says the data is not used for training and is kept only for security.** — This affects any gateway or proxy that sends Fable 5 traffic, since retention and logging rules become a compliance requirement. ([5:04](https://youtu.be/Ubazoyagym0?t=304))

## Techniques
- **Same-prompt side-by-side model comparison** — Give an identical single prompt (for example, build a finance dashboard with front end and back end from an empty folder) to each candidate model, record wall-clock completion time, and judge the result by eye. Do not add a design style, so the model's default aesthetic is visible. *When:* Quick qualitative comparison of coding or UI-generation models when no eval harness exists. It is anecdotal, with one run per model.
- **Screenshot-to-site cloning** — Pass a full-page screenshot of a target website to the model with no web search or extra tools, ask for the page as code, then iterate on the parts that differ. *When:* Fast first draft of a UI from a visual reference, where a rough match is enough to start iterating on details.

## Numbers
- Pricing: $10 per 1M input tokens, $50 per 1M output tokens ([3:48](https://youtu.be/Ubazoyagym0?t=228))
- Agentic coding on SWE-Bench Pro: about a 10% jump over the prior model, presenter says about 20% ahead of GPT 5.5 (basis unclear from the charts) ([0:00](https://youtu.be/Ubazoyagym0?t=0))
- Stripe reported codebase-wide migration of a 50-million-line Ruby codebase in a single day (vendor/customer claim) ([0:00](https://youtu.be/Ubazoyagym0?t=0))
- Finance dashboard one-shot completion time: Fable 5 about 8 min, Opus 4.8 about 12 min, GPT 5.5 about 15 min (single run each) ([2:33](https://youtu.be/Ubazoyagym0?t=153))
- Safeguard false positives: under 5% of messages (vendor claim) ([3:48](https://youtu.be/Ubazoyagym0?t=228))
- Cyber evals with safeguards: zero passes (presenter's reading); Opus about 88% pass rate as he recalls ([3:48](https://youtu.be/Ubazoyagym0?t=228))
- Fable 5 uses usage limits about 2x as fast as Opus ([5:04](https://youtu.be/Ubazoyagym0?t=304))
- Required retention: 30 days of traffic on first- and third-party tools ([5:04](https://youtu.be/Ubazoyagym0?t=304))

## Hot takes
- The title says it is finally here, but no evidence beyond the vendor table and a few demos is shown. The presenter reads the charts and does not run any benchmark himself.
- He calls the plan removal a rug pull and says the model is too expensive to be a primary model unless you are a billionaire. This is his opinion on Anthropic's business motives.
- Date inconsistency: the metadata says 2026-07-02, but the presenter says the June 23 removal is a couple of weeks away. Treat the timeline as unverified until checked against Anthropic's announcement.
- Calls the Claude UI aesthetic better than GPT 5.5's and says he is disappointed with GPT's UI. One prompt, one run, and his own admission that he did not steer the design.
- Auto-caption artifact: the plan name appears as 'Promax' in the transcript and is read here as Max.

## Tools mentioned
Fable 5 (Anthropic model, Mythos class), Claude Mythos, Opus 4.8, GPT 5.5 (OpenAI), SWE-Bench Pro, Frontier Code (Cognition benchmark), Terminal Bench, Devin (referenced as Cognition product), Claude Max, Team and Enterprise plans

## Relevance to our work
- **agentos** (1/3): Premium-tier model with per-token pricing, plan-gated access and a retention requirement is relevant to AgentOS L1 budgets and strategy routing, but the evidence is vendor claims. → *Add Fable 5 price and retention flags to the L1 routing and budget config as a test case, and keep refusal rate as a metric alongside cost.*
- **prosharness** (1/3): Claims about long-running coherence (notes and millions of tokens) and usage-limit burn bear on checkpoint/resume and loop budgets, but the evidence here is an unverified vendor claim. → *When a model claims multi-hour runs, test ProsHarness checkpoint/resume with it and record usage-limit burn per phase.*
- **general** (1/3): Model-release news with a single one-shot comparison and vendor benchmarks. Useful context, not a decision input. → *Read the Anthropic release notes and run a repeatable eval on the same task before deciding on the model.*
