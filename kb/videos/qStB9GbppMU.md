# 1 Trillion Phone Calls/yr, 10% Error rate: The Crisis in Voice AI — Sumanyu Sharma, Hamming AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `qStB9GbppMU` · [watch](https://youtu.be/qStB9GbppMU) · **date:** 2026-09-18 · **length:** 16:04 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sumanyu Sharma · **orgs:** Hamming AI, Citizen
- **topics:** voice-multimodal, evals, observability, security-guardrails · **tags:** voice-agents, reliability, error-analysis, cross-conversation-analysis, ab-testing, red-teaming, prompt-injection, monitoring, triage

> Hamming AI's CEO argues voice agent errors (about 10% in practice) are the top deployment blocker, and offers a loop to find, prioritise, test and red-team failures across many calls.

## Summary
The speaker, founder of Hamming AI, opens with a comparison between crime alerts and voice agent incidents. He argues voice agents are scaling fast, reliability is still the main blocker, and errors reach users with high confidence. He cites about 10% real-world error across roughly 10,000 monitored agents, and says a 1% error rate would still mean billions of incidents a year. Because one prompt or architecture change hits millions of calls at once, he wants incidents made visible. His loop is: find problems, rank them by frequency and severity, fix, test for regressions, then monitor. Teams should start by listening to calls manually, then move to rubrics and LLM judges, then cross-conversation analysis to find patterns no single-call check would catch. For testing, he recommends varying the wording, accents and intents of a real failing call, and using A/B tests in production for things simulation cannot show. He ends with adversarial risk: his red-team product reports it can break about one in five agents, and he recommends 24/7 red-teaming. The talk is partly a sales pitch, but the framework is concrete.

## Key ideas
- **Voice agent reliability is the main blocker to scale, and the errors are confident and sound natural.** — Agents now act on calendars, CRMs and booking systems, but wrong information is delivered in a confident voice. Examples include a booking that was never made and a skipped eligibility check. ([2:21](https://youtu.be/qStB9GbppMU?t=141))
- **Voice agent incidents have a large blast radius because the system is centralised.** — Crime is local and decentralised. One prompt or architecture change can affect millions of calls, so incidents need to be made visible quickly. ([6:19](https://youtu.be/qStB9GbppMU?t=379))
- **Use a repeating loop: find, rank, fix, verify, monitor.** — The loop is identify, prioritise by frequency and severity, understand the fix, execute, check for regressions, then keep monitoring in production. He says the fix step is the easy part. ([7:18](https://youtu.be/qStB9GbppMU?t=438))
- **Per-call rubrics and LLM judges check known problems but miss emerging ones.** — Teams start by listening to calls, then move to spreadsheets of rubrics and LLM-as-judge evals. Cross-conversation analysis is what finds new patterns, and he splits problems into known versus emerging, and low coverage versus high. ([7:18](https://youtu.be/qStB9GbppMU?t=438))
- **Systematic plus high-impact issues are P0; one-off low-impact issues still matter at scale.** — Triage uses frequency and severity. Even low-impact systematic issues such as repetition are worth fixing at scale. ([8:42](https://youtu.be/qStB9GbppMU?t=522))
- **Test a fix with varied scenarios, and use A/B tests for what simulation cannot show.** — Replaying a failed call 5 to 50 times gives a pass rate for that one case. Varying wording, accents, style and intents gives better coverage. For outbound agents, the first five seconds matter most, so A/B testing in production is the only reliable check there. ([10:13](https://youtu.be/qStB9GbppMU?t=613))
- **Adversarial users are a real risk, and red-teaming should run continuously.** — The speaker says a red-team product has broken about one in five agents across finance, healthcare and consumer use cases, including bypassing verification and extracting data. He recommends pre-deployment testing, layered monitoring, and 24/7 red-teaming when the cost of a bad call is high. ([11:41](https://youtu.be/qStB9GbppMU?t=701))

## Techniques
- **Frequency and severity triage matrix** — Place each agent failure on a frequency axis and an impact axis. Systematic and high-impact issues are P0. Track known problems separately from emerging patterns. *When:* When choosing what to fix next from a large set of failing calls.
- **Scenario-variation regression testing** — Start from a real failing call, keep the same intent, then vary wording, accent, style and added intents. Run many times and measure the pass rate instead of replaying one transcript. *When:* Before deploying a change to a voice agent, to check it is a net improvement.
- **Production A/B testing for voice fixes** — Run the old and new versions on live traffic and compare outcomes. Use it for hypotheses that synthetic tests miss, such as opening lines in the first seconds of outbound calls. *When:* When voice quality or early-call wording is likely to matter and simulation cannot capture it.
- **Cross-conversation pattern analysis** — Analyse many sessions together to find recurring behaviour, instead of checking one call against a rubric. Combine this with per-call scoring and manual listening. *When:* To discover failure patterns that rubrics and LLM judges miss.
- **Continuous adversarial red-teaming** — Run automated attacks against the agent, including social engineering to extract personal or health data, on a schedule that runs all the time. *When:* When a bad interaction is costly, such as access to tools, personal data or payments.

## Numbers
- At least one trillion phone calls a year, with most expected to be handled by conversational voice agents over the next five years (speaker's estimate). ([3:52](https://youtu.be/qStB9GbppMU?t=232))
- Monitored agents (about 10,000) show a real-world error rate of about 10%. He says a 1% error rate would still mean about 10 billion incidents a year. ([4:50](https://youtu.be/qStB9GbppMU?t=290))
- The vendor's red-team product, released in April, reportedly breaks about one in five voice agents across finance, healthcare and consumer use cases (vendor claim, untested). ([12:53](https://youtu.be/qStB9GbppMU?t=773))
- Replaying one real failing call 5, 10, 20 or 50 times gives a pass probability for that one case. He calls this the naive approach. ([10:13](https://youtu.be/qStB9GbppMU?t=613))

## Hot takes
- Voice agents scare him more than crime, because one bad prompt change can reach millions of people at once.
- The main threat from voice agents is adversarial users who sound like real customers, not honest mistakes.
- Manual call listening is the right starting point but cannot scale, so teams must move to cross-conversation analysis.

## Relevance to our work
- **agentos** (1/3): L1 Govrix already has PII and prompt-injection scanning, and this talk's red-team numbers suggest those checks need testing against adversarial voice or text attacks. → *Add a recurring adversarial test suite (prompt injection and PII extraction via multi-turn chat) against the Govrix scan layer, and track the bypass rate over time.*
- **prosharness** (1/3): The talk's example of an agent claiming a booking it never made maps to a harness that trusts claimed outcomes. → *Add a check in the ProsHarness loop that compares an agent's claimed outcomes against tool-call evidence before accepting a checkpoint.*
- **general** (1/3): The frequency and severity triage and the scenario-variation test loop apply to any agent eval loop. → *Use frequency-times-severity ranking and multi-variant replay (not single-trace replay) when designing the next agent eval loop.*
