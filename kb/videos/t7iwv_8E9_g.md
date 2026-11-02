# Future of AI security with Michal Pechoucek

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `t7iwv_8E9_g` · [watch](https://youtu.be/t7iwv_8E9_g) · **date:** 2024-11-02 · **length:** 17:30 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Michal Pechoucek · **orgs:** Gen Digital, Norton, Avast, MITRE, FTC, Microsoft
- **topics:** security-guardrails, coding-agents · **tags:** ai-security, prompt-injection, data-poisoning, ai-generated-code, scams, social-engineering, fraud-detection, threat-model

> Gen Digital's technology head argues the real AI threats are weaponized attacks, insecure AI-written code, attacks on AI systems, and mostly human-targeted scams, and pitches a free scam-detection app.

## Summary
Michal Pechoucek, who runs technology at Gen Digital (the consumer cybersecurity firm that includes Norton and formerly Avast), gives a short, opinion-led talk on AI security. He opens with a techno-optimist framing and an analogy: self-driving trucks were predicted to replace drivers but have not, while software spending is a much larger market that AI coding tools target. He lists four AI threats: attackers using generative AI, insecure code written with AI assistants, attacks on AI systems themselves (poisoning, prompt injection), and AI-enabled misuse aimed at people. Most of the talk is about the last one, using Gen's telemetry (85% of threats are human-directed scams, not malware) and FTC fraud figures. He argues that detecting scams in text, video and voice is getting easier with generative AI, while long-running conversational scams are the hardest to catch. The talk closes with a product plug for Norton Genie, a free phone app that explains whether content is scammy.

## Key ideas
- **Analogy against job-loss predictions: self-driving trucks were predicted to remove truck drivers but are still not deployed at scale because of engineering, regulation and cost. The speaker says automating software writing will arrive earlier.** — Speaker compares about 40 million truck drivers and a cargo market of roughly $250B against a software development market he puts near $1T. Developer count is guessed at 20-40 million. His advice: worry about a person using AI better than you, not about AI replacing you. ([1:14](https://youtu.be/t7iwv_8E9_g?t=74))
- **Four AI threat categories: weaponization by attackers, exploitation of vulnerabilities in AI-written code, attacks on AI systems, and cognitive attacks on people.** — He frames these as the list technologists should track. Alignment and bias get a brief mention before the list. ([3:57](https://youtu.be/t7iwv_8E9_g?t=237))
- **Attackers already use generative AI to find vulnerabilities, obfuscate attacks and A/B test malware, so defenders must invest in AI at least as heavily.** — His argument is that defenders cannot win by adding more people against AI-driven attacks. He says defenders must keep investing in AI research for defense. ([5:22](https://youtu.be/t7iwv_8E9_g?t=322))
- **AI-written code is a bigger shift for software security than past platform changes, because volume and unexplained behavior create new vulnerabilities.** — He cites a lab claim that copilots produce 40% fewer errors and vulnerabilities than people, then argues this is not reassuring because the volume of generated code could grow about 10x. Systems that connect feeds and services and hallucinate create an unexplained attack surface. ([7:33](https://youtu.be/t7iwv_8E9_g?t=453))
- **Attacks on AI systems themselves: poisoned training or fine-tuning data, manipulated and injected prompts, and poisoned parameters. He points to a MITRE taxonomy of known AI attacks (transcribed as 'Mitra', and called Atlas).** — He says AI systems are not yet resilient enough and are becoming backbone infrastructure, so they need better protection. ([9:01](https://youtu.be/t7iwv_8E9_g?t=541))
- **Most threats are now human-directed cognitive attacks: scams, fraud and social engineering account for 85% of threats in Gen telemetry, and malware 15%.** — Telemetry comes from more than 500M connected devices, per the speaker. Social media and messaging apps are the most common scam sources. Scam detection has moved from URLs to text, then to video and voice. ([11:35](https://youtu.be/t7iwv_8E9_g?t=695))
- **Conversational, multi-month scams (for example pig-butchering) are the hardest to detect because the defender must read a whole long conversation, which he calls computationally hard.** — He says the scam operations are heavily automated, which makes detection difficult. Gen uses generative-AI models trained to flag scammy text. Detecting scam video and voice is in progress. ([14:11](https://youtu.be/t7iwv_8E9_g?t=851))

## Techniques
- **Generative-AI scam text classifier** — Train a generative-AI model to flag scammy text, as Gen does for scam detection. The speaker describes this only at a high level and gives no architecture or metrics. *When:* Use for screening user-facing messages where URL or file scanning misses scams (social media, messaging apps).
- **On-device conversational scam check** — Ask a phone app to explain whether on-screen content is a scam through a conversation. The app reads what is visible on the phone and gives a verdict with an explanation. Gen calls this Norton Genie. *When:* Use as a consumer-facing defense where content is ambiguous to the user. The speaker does not describe how it works internally.

## Numbers
- About 40 million truck drivers worldwide; freight cargo market about $250B (as spoken, 'a quarter of a billion'). ([1:14](https://youtu.be/t7iwv_8E9_g?t=74))
- Software development spending estimated at about $1T per year, roughly 4x the cargo market. Copilot priced at about $1 per day. ([2:39](https://youtu.be/t7iwv_8E9_g?t=159))
- Lab tests reportedly show copilots about 40% safer than people at avoiding code vulnerabilities and errors. The speaker says this is not reassuring. ([7:33](https://youtu.be/t7iwv_8E9_g?t=453))
- Gen sees more than 500M connected devices in its telemetry. 85% of threats are human-directed cognitive attacks (scams, fraud, social engineering) and 15% are malware. ([11:35](https://youtu.be/t7iwv_8E9_g?t=695))
- US FTC data: about 2.6-2.7M fraud reports in 2023, about $10B reported loss, average damage about $500. Reporting falls with age while damage rises. ([11:35](https://youtu.be/t7iwv_8E9_g?t=695))
- Social media is the leading scam source: about $2.7B of reported loss, with messaging apps (WhatsApp and similar) about $2.8B, as spoken. ([13:06](https://youtu.be/t7iwv_8E9_g?t=786))

## Hot takes
- Product placement: the closing segment promotes Norton Genie (a Gen Digital product) and the speaker says it is a product placement; the app is said to be free with no plan to charge.
- The 40% copilot safety figure is repeated without a source or study details.
- The scam loss figures are self-reported US FTC numbers, and the speaker does not reconcile the reported losses (about $10B total) with the per-channel figures he gives.
- Strong claim that AI-written code will be a bigger security shift than Windows 95, the internet, cloud and SaaS, with no evidence beyond the speaker's opinion.
- Speaker's view that AI will hit developers before drivers, based on a market-size comparison, is speculation.
- Quality is capped at 2 because the closing segment is a product pitch and the talk has thin technical substance.

## Tools mentioned
Norton Genie (Gen Digital, free scam-detection app for iPhone and Android), MITRE ATLAS (taxonomy of known attacks on AI systems, transcribed as 'Mitra' / 'Atlas'), Windows 95 (cited as a historical vulnerability event), Copilot-style AI coding assistants (unnamed 'copilots')

## Relevance to our work
- **agentos** (2/3): L1 Govrix Scout already does PII and prompt-injection scanning. The talk's threat list (data poisoning, prompt injection, AI-written code vulnerabilities) is a useful threat model for the proxy and the sandbox/exec-gate layers, though it is high-level. → *Write a threat-model page for AgentOS covering the four threat classes from the talk, and map each to a gate: prompt-injection scan, training/knowledge-bucket ingestion checks, and exec-gate review for agent-written code.*
- **prosharness** (1/3): ProsHarness runs Claude Code in long loops. The talk's point that AI-written code adds unexplained vulnerabilities at high volume applies to unattended runs. → *Consider a security review step (or a separate review agent) for code produced in unattended ProsHarness runs before it is merged.*
- **general** (1/3): Useful framing on AI-enabled scams and social engineering, but not a technique to adopt directly. → *Read the MITRE ATLAS taxonomy the speaker cites for a list of known attacks on AI systems.*
