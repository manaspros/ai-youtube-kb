# AI Hackers Are Faster Than Your Pen Test — Eli Cohen, Snyk

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `f3o0-9Dlw3E` · [watch](https://youtu.be/f3o0-9Dlw3E) · **date:** 2026-10-08 · **length:** 19:29 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Eli Cohen · **orgs:** Snyk, Helios
- **topics:** security-guardrails, multi-agent, pr-code-review · **tags:** ai-pentesting, offensive-security, appsec, dast, sast, exploit-validation, agent-red-teaming, bola, mcp-security, snyk-evo, vendor-pitch

> Snyk's Eli Cohen argues LLM-generated code and LLM attackers make twice-yearly pentests obsolete, and pitches a continuous, per-PR AI pentest pipeline (Snyk Evo) with an exploit-validation judge.

## Summary
Eli Cohen (Snyk Field CTO, former Helios co-founder) argues that AI coding agents are producing far more code, much of it insecure, while attackers use the same frontier models to find and chain vulnerabilities faster. He positions traditional tools as insufficient: static scanners miss runtime and authorization issues, DAST sends payload lists without business context, and human pentests are expensive and run only once or twice a year. He proposes continuous offensive security: an LLM-driven pentest that runs on every PR or code delta, combines findings from existing scanners as context, and proves exploitability before flagging. The described architecture is a chain of agents: an orchestrator, a recon agent that builds an architecture model, specialized vulnerability-testing agents, an exploit-validation "judge", a remediation agent, and a reporting agent. He closes with four questions to ask any vendor. The talk is a product pitch for Snyk Evo; its headline statistics are unsourced and the design details are high-level, not reproducible.

## Key ideas
- **AI coding agents raise code volume and insecurity at the same time, so the vulnerability backlog grows faster than teams can remediate.** — Speaker cites 218% more lines of code per developer, over 85% of developers using coding agents, and 62% of LLM output being insecure or broken. He presents these as Snyk data without a source or methodology. ([1:19](https://youtu.be/f3o0-9Dlw3E?t=79))
- **Attackers use the same frontier models to chain low-severity findings into critical ones, and they are strongest on application-context bugs.** — Cites an unattributed incident of an operating model finding 600+ vulnerabilities across 600 firewalls in 55+ countries. The argument is that LLM-generated code creates the most bugs in exactly the context-dependent areas attackers target. ([2:45](https://youtu.be/f3o0-9Dlw3E?t=165))
- **Each testing method covers a different class of bug: SAST for code patterns, DAST for runtime and authorization issues, pentesting for business logic.** — SAST handles SQL injection and XSS in code. DAST catches runtime and config issues such as BOLA (user A reads user B's data), which static analysis cannot see. Pentesting is the only method that reasons about business logic, but it is costly and usually run two or three times a year. ([5:34](https://youtu.be/f3o0-9Dlw3E?t=334))
- **Annual or semi-annual pentests leave most of the year untested, and their PDF reports are slow to act on.** — Speaker's framing: roughly 350 days a year with no pentest. Developers must work out which findings are real before they can fix anything, followed by a retest cycle. ([8:06](https://youtu.be/f3o0-9Dlw3E?t=486))
- **Proposed approach: run an LLM pentest on every PR or code delta, and have it prove exploitability instead of just flagging suspicions.** — Goal is to reduce false positives and cover red-teaming themes: multi-step attacks, prompt injection, data exfiltration, and goal hijacking, combined with dynamic authorization testing. Speaker claims some agents can complete an attack in about 4 minutes. ([11:05](https://youtu.be/f3o0-9Dlw3E?t=665))
- **Architecture is an agent chain: orchestrator, recon, vulnerability testers, exploit-validation judge, remediation, reporting.** — The recon agent collects endpoints, APIs and fingerprints and formalizes an architecture for the testers. The judge decides whether each candidate finding is actually exploitable. Remediation and reporting turn results into developer-actionable output. ([12:24](https://youtu.be/f3o0-9Dlw3E?t=744))
- **Feeding findings from existing scanners into the LLM as context improves where it looks and what it finds.** — Static and dynamic scanner outputs are passed to the pentest agent to guide it. Speaker says results are better when models know where to look, and says no single engine is enough: DAST suits XSS, pentesting suits business logic. ([15:07](https://youtu.be/f3o0-9Dlw3E?t=907))
- **Four questions for evaluating any continuous AI pentest vendor.** — (1) Does it run continuously or as a periodic point solution? (2) Does it reason about application context? (3) Can it take richer context, which the speaker says lowers cost? (4) Does it prove exploitability or only flag suspected bugs? ([16:33](https://youtu.be/f3o0-9Dlw3E?t=993))

## Techniques
- **Layered agent pipeline for continuous pentesting** — Chain agents: orchestrator (holds a dynamic plan and dispatches sub-agents), recon (enumerate endpoints, APIs and fingerprints, output a formal architecture), specialized vuln testers (known vulnerability classes plus open-ended hunting), exploit-validation judge (accept only findings it can show are exploitable), remediation (developer-actionable fix guidance), reporting. Speaker gives no prompts, tools or code. *When:* When you want autonomous security testing of agent-written code beyond scanner output, and false-positive load is the bottleneck.
- **Scanner output as LLM context** — Run SAST and DAST first, then pass their findings and the architecture model into the LLM pentest agent so it focuses on likely weak spots. Use DAST for payload-driven classes like XSS and the LLM for business-logic and authorization flaws. *When:* When you already run scanners and want the LLM to spend its budget on the most promising areas instead of searching the whole app.
- **Exploit proof gate before flagging** — Do not report a candidate vulnerability until a validator confirms it is exploitable, for example by reproducing the attack. Treat unvalidated findings as suspicions, not bugs. *When:* When developer trust in security alerts is low because of false positives.
- **Per-PR security trigger** — Run the pentest on every PR or code delta, not on a schedule, so each change is tested while its context is fresh. *When:* When code is merged continuously, including agent-generated code, and periodic audits leave long gaps.

## Numbers
- 218% more lines of code per developer than before (speaker's Snyk data) ([1:19](https://youtu.be/f3o0-9Dlw3E?t=79))
- More than 85% of developers use coding agents ([1:19](https://youtu.be/f3o0-9Dlw3E?t=79))
- 62% of LLM-generated output is insecure or broken (speaker's figure, unsourced) ([1:19](https://youtu.be/f3o0-9Dlw3E?t=79))
- One AI-driven operating model reportedly found 600+ vulnerabilities across 600 firewalls in 55+ countries (unattributed) ([2:45](https://youtu.be/f3o0-9Dlw3E?t=165))
- Average time for a successful AI attack reported as 24 (transcript garbled as "24 minutes 34 minutes"); fastest reported at 4 minutes ([4:12](https://youtu.be/f3o0-9Dlw3E?t=252))
- 43% of MCP servers have vulnerabilities (unsourced) ([4:12](https://youtu.be/f3o0-9Dlw3E?t=252))
- Pentests are typically run 2 to 3 times a year, leaving about 350 days untested ([6:48](https://youtu.be/f3o0-9Dlw3E?t=408))
- Some LLM attackers can finish an attack in about 4 minutes, roughly five times the length of the talk so far ([16:33](https://youtu.be/f3o0-9Dlw3E?t=993))

## Hot takes
- Vendor pitch: the talk launches Snyk Evo and says the same structure applies to any vendor. Speaker is not neutral.
- Headline statistics (218%, 85%, 62%, 43%, 600 firewalls, 24/34 minute attack times) come with no source or methodology. Treat them as anecdotes.
- Exploitability is claimed, not demonstrated. No benchmark, false-positive rate or case study is given.
- The most reusable part is the four-question vendor checklist and the principle that a finding should be proven before it is flagged. The agent-chain design is described only at a high level.
- Quality is capped at 2 because the content is a sales pitch with thin technical substance.

## Tools mentioned
Snyk Evo (Snyk's continuous AI offensive security / AI pentesting offering, named in the talk), Snyk (company), Helios (runtime security company, acquired by Snyk), Claude Code (called "cloud code" in captions), Codex (OpenAI coding agent), SAST (static application security testing), DAST (dynamic application security testing; captioned as "dust"), MCP (Model Context Protocol), Mythos (model named in passing; exact referent unclear)

## Relevance to our work
- **agentos** (2/3): Crucible has exec-gate guardrails and L1 has prompt-injection scanning. The talk's idea of an exploit-validation judge that confirms a finding before flagging it maps onto validating guardrail and sandbox findings. Agent red-teaming (multi-step prompt injection, exfiltration) is also relevant to AgentOS's security pillars. → *Prototype an exploit-validation step for AgentOS security findings: a candidate guardrail or sandbox bypass is recorded as a bug only after a scripted reproduction passes. Use this as a test-suite gate for Crucible's exec-gate.*
- **prosharness** (1/3): The orchestrator, specialist agents, validator, and reporter chain is a multi-agent pattern similar to plan, critique, debate in ProsHarness, with a separate judge that checks the output of the specialists. → *Compare the orchestrator-to-judge hand-off with ProsHarness's plan, critique, debate loop and consider a separate verifier role that only accepts claims with evidence.*
