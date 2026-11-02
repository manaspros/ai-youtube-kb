# The AI bugpocalypse is here. Now what? - Jack Cable, Corridor

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `7JgIS42mz7U` · [watch](https://youtu.be/7JgIS42mz7U) · **date:** 2026-07-18 · **length:** 19:44 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Jack Cable · **orgs:** Corridor, CISA, Stanford, HackerOne, Anthropic, Google, MITRE, ETH Zurich, UC Berkeley, Stack Overflow, Microsoft, Amazon
- **topics:** security-guardrails, pr-code-review, governance-compliance, models-research · **tags:** vulnerabilities, memory-safety, rust, ai-generated-code, open-source-security, secure-by-design, business-logic-bugs, policy, export-controls, open-weight-models

> Jack Cable (Corridor, ex-CISA) argues frontier models now find and exploit vulnerabilities at scale, but the bug classes are old and preventable, so rewrite toward memory safety and add guardrails before the PR for AI-written code.

## Summary
Jack Cable, co-founder and CEO of Corridor and a former CISA senior technical advisor, frames the moment as a bugpocalypse: frontier models are getting better at finding and exploiting vulnerabilities, especially in open source libraries, while AI coding agents spread fast. He argues most bugs models find belong to old, well-documented classes that defenders already know how to prevent. He points to memory-safe languages as the clearest lever, citing CVE-based estimates and Google's Android data, and recommends rewriting critical libraries rather than patching bugs one at a time. He says AI-written code still introduces vulnerabilities at a high rate, and the newer ones are contextual business-logic and authorization bugs that models lack the company context to avoid. He predicts AI will review most shipped code within 6 to 12 months because human review is the bottleneck, so security teams should add guardrails and visibility around coding agents before the pull request instead of blocking them. The talk closes with policy recommendations to Congress: prevent new vulnerabilities, harden open source, and build American open-weight models. Most of the content is the speaker's opinion and policy advocacy, and the Corridor pitch is brief.

## Key ideas
- **Frontier models are now good at finding and exploiting vulnerabilities, and the open source libraries under most software are the main exposure** — The speaker calls this a bugpocalypse. Attack surface also grows as AI becomes the default code writer, so both sides of the equation are moving. ([0:00](https://youtu.be/7JgIS42mz7U?t=0))
- **Agents have moved from autocomplete to background agents that run for hours and open large changes** — The speaker describes teams starting agents from Slack and running many at once. He expects adversaries to automate the whole attack chain, not just discovery. ([2:15](https://youtu.be/7JgIS42mz7U?t=135))
- **Most bugs models find are old, well-known classes, so they can be designed out** — He cites the MITRE classes that appear in CISA's known-exploited catalog, such as buffer overflows, and says the same classes show up in what models find now. The bug is new, but the class is not. ([6:49](https://youtu.be/7JgIS42mz7U?t=409))
- **Memory-safe languages remove a large share of bugs, and a rewrite of critical libraries pays off over years** — He cites roughly 60 to 70 percent of vulnerabilities in memory-unsafe products as preventable with memory-safe languages. Google's Android share of memory-safety bugs fell as new code moved to memory-safe languages. He prefers this to whack-a-mole patching. ([8:06](https://youtu.be/7JgIS42mz7U?t=486))
- **AI-written code still has a high vulnerability rate, and the bugs are increasingly contextual** — A benchmark he cites (BaxBench, ETH Zurich and UC Berkeley) finds the best models introduce vulnerabilities 20 to 40 percent of the time. Newer bugs are authorization and business-logic issues that depend on company context the model does not have. ([11:18](https://youtu.be/7JgIS42mz7U?t=678))
- **Code review is the bottleneck, so he expects AI to review most shipped code soon** — He predicts that within 6 to 12 months most shipped code will be reviewed by AI rather than humans. Under that model, security needs assurance tooling that lets teams merge with less human oversight. ([13:08](https://youtu.be/7JgIS42mz7U?t=788))
- **Security should set guardrails on coding agents before the pull request, not block their use** — The speaker's company, Corridor, focuses on preventing vulnerabilities before the PR and giving visibility into how coding tools are used. He says the question from security teams has shifted from whether to allow agents to how to allow them with guardrails. ([14:16](https://youtu.be/7JgIS42mz7U?t=856))
- **Dual-use model access is a policy tension, and open-weight models shrink the gap for adversaries** — He refers to export controls on the Mythos and Fable models and a letter urging their lift. He notes distillation lets open-weight models catch up faster, and argues defenders need access to the same capabilities. ([15:21](https://youtu.be/7JgIS42mz7U?t=921))
- **Recommendations: prevent new vulnerabilities, harden open source, and back American open-weight models** — These were his three points to Congress. He argues open-weight models matter because fine-tuning requires them, and that the work should be systemic (rewrites) rather than one-off patches. ([17:10](https://youtu.be/7JgIS42mz7U?t=1030))

## Techniques
- **Rewrite critical components in a memory-safe language** — Move new code, and then critical open source libraries, to Rust or another memory-safe language, so whole bug classes cannot be introduced rather than patching each instance. *When:* When a library is a recurring source of memory-safety CVEs and will be used for years.
- **Pre-PR guardrails and visibility for agent-written code** — Check code for vulnerabilities before the pull request is opened, and log how coding agents are used so security has assurance without blocking developers. *When:* When teams run background coding agents and code review is becoming the bottleneck.
- **Give the reviewer business and threat context** — Business-logic and authorization bugs need knowledge of the company's own rules and threat model, so the review should carry that context rather than rely on generic checks. *When:* When reviewing changes that touch permissions, data access or core business rules.
- **Use defenders' frontier models to harden systems** — Run the same capable models that attackers use to find and fix vulnerabilities in your own code and in open source dependencies. *When:* When attackers already have strong models and you need to shrink the window before exploitation.

## Numbers
- About 84 percent of developers were using AI coding tools, and 30 to 40 percent of companies encouraged use (Stack Overflow survey, last year's data) ([2:15](https://youtu.be/7JgIS42mz7U?t=135))
- Roughly 60 to 70 percent of vulnerabilities in memory-unsafe products could be prevented by memory-safe languages (CVE data, as cited) ([8:06](https://youtu.be/7JgIS42mz7U?t=486))
- Android memory-safety vulnerabilities fell from about 75 percent in 2019 to about 30 percent in 2022, after new code moved to memory-safe languages (Google chart) ([8:55](https://youtu.be/7JgIS42mz7U?t=535))
- Best models introduce vulnerabilities 20 to 40 percent of the time when writing code (BaxBench) ([11:18](https://youtu.be/7JgIS42mz7U?t=678))
- Speaker predicts the majority of shipped code will be reviewed by AI rather than humans within 6 to 12 months ([13:08](https://youtu.be/7JgIS42mz7U?t=788))
- An Opus 4.6 introduced smart-contract vulnerability reportedly led to a couple million dollars being stolen (speaker's account, unverified) ([10:07](https://youtu.be/7JgIS42mz7U?t=607))

## Hot takes
- Security cannot be the blocker; acceleration will always win, so guardrails are the answer, not gatekeeping
- Patching one-off vulnerabilities is whack-a-mole; one-time rewrites to memory-safe languages are the better investment
- Within 6 to 12 months the majority of shipped code will be reviewed by AI, not humans
- Export controls on dual-use models should be lifted because defenders gain more than adversaries
- The US needs frontier open-weight models for fine-tuning and competitiveness

## Tools mentioned
Claude Code, Cursor, Rust, Slack, BaxBench

## Relevance to our work
- **agentos** (1/3): AgentOS has exec-gate guardrails in Crucible and a PII/prompt-injection scan in Govrix, but the talk is about code vulnerabilities in agent-written software, not agent runtime security. The business-logic bug point is the only overlap. → *Read the BaxBench methodology and consider a small Crucible or exec-gate eval that checks agent-written patches for authorization bugs.*
- **prosharness** (1/3): ProsHarness runs plan, critique and debate stages. A security-focused critique stage could catch the contextual bugs the talk describes, but the talk does not give a method for it. → *Consider adding a security critique stage, with the repo's threat model as context, before ProsHarness opens a PR on agent-written code.*
- **general** (1/3): Concrete data on AI-written code vulnerability rates and the memory-safety argument, from a practitioner with government and security experience. Mostly opinion and policy. → *Read the BaxBench paper for the vulnerability-rate methodology before quoting the 20 to 40 percent figure.*
