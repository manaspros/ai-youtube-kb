# Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `hOWU0KPUp1k` · [watch](https://youtu.be/hOWU0KPUp1k) · **date:** 2026-09-18 · **length:** 17:00 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Brendan Rappazzo · **orgs:** Morgan Stanley, NVIDIA
- **topics:** evals, governance-compliance, multi-agent, context-engineering · **tags:** adversarial-agents, red-teaming, legal-codification, moral-reasoning, contracts, chatbot-system-prompts, hill-climbing, persona-simulation, open-source, ai-governance

> Brendan Rappazzo presents Loophole, an open-source game where two adversarial agents hunt contradictions in a legal code codified from the user's morals, then extends it to chatbot prompts, contracts, and simulated Senate votes.

## Summary
The speaker built Loophole, a terminal game where the user writes moral principles in natural language and one agent drafts a formal legal code from them. Two adversarial agents then search for loopholes (immoral but legal) and overreach (moral but illegal) using synthetic case-law examples. A judging agent either auto-patches the code with a git-style diff or escalates real contradictions or under-specification to the user. The motivation is that enumerating nuanced morals case by case is cognitively prohibitive, and he argues recent LLMs are now capable enough for this kind of high-level moral reasoning. He describes three extension branches: generating codified system prompts for customer-facing chatbots (compared to GEPA), stress-testing contracts and terms of service before signing, and simulating legislators and voters. In the legislative branch, Claude builds moral systems for current senators from public voting records, and hill-climbing a Medicare bill's wording moved the simulated vote from about 50-50 to passing with 52 votes. A later experiment built 500 persona-based moral systems per state from an NVIDIA US persona dataset. No formal evaluation or benchmark is shown, the results are demo-level, and the speaker says he is biased toward his project.

## Key ideas
- **Adversarial pair as a stress test for a rule set** — One agent hunts for immoral-but-legal outcomes (loopholes) and another for moral-but-illegal outcomes (overreach), both generating synthetic cases against the drafted code. ([0:12](https://youtu.be/hOWU0KPUp1k?t=12))
- **Judge decides between auto-patch and human escalation** — A judging agent first tries to patch the legal code automatically when the draft was just an imperfect translation. It escalates to the user only when the problem is under-specification or a genuine contradiction in the morals. ([4:22](https://youtu.be/hOWU0KPUp1k?t=262))
- **Case-by-case moral judgement does not scale, so codify it** — Enumerating preferences one case at a time is cognitively prohibitive. The speaker frames a legal system as a codification of moral beliefs and treats the nuance problem as a hard translation task, with case law as the usual remedy. ([1:38](https://youtu.be/hOWU0KPUp1k?t=98))
- **Codified system prompts for chatbots** — Write what the bot should and should not discuss in plain language, have the system draft a formal system prompt, then use adversarial agents to try to make it break either rule. The speaker sees this as analogous to GEPA, aimed at codified prompts. ([7:59](https://youtu.be/hOWU0KPUp1k?t=479))
- **Pre-signing contract checks** — Run your codified preferences against a company's new terms of service, or against a counterparty's codified terms, to surface contradictions before agreeing. He says this gives better information even when there is no room to negotiate. ([9:14](https://youtu.be/hOWU0KPUp1k?t=554))
- **Hill-climbing bill language against simulated voters** — Each senator's codified system is checked against a bill. The system then rewrites the language to avoid violating core tenets and ranks the changes by how many votes each one adds, so the user can choose trade-offs. ([13:07](https://youtu.be/hOWU0KPUp1k?t=787))

## Techniques
- **Adversarial loophole and overreach search** — Prompt two adversarial agents with opposite goals, one to find immoral-but-legal cases and one to find moral-but-illegal cases, and have them generate synthetic case-law examples against a formal rule set. *When:* Stress-testing any written policy, spec, or rule set for contradictions and gaps before relying on it.
- **Judge with auto-patch first, human escalation second** — A judging agent checks each finding. It applies a git-style patch when the fix is a translation error and asks the user only for real contradictions or under-specification. *When:* Long-running spec-maintenance loops where most fixes are mechanical but a few need a human decision.
- **Formalize natural-language values into numbered legal text first** — Ask the model to turn short moral statements into structured articles and sections written in precise language, then test that artifact instead of the raw prose. *When:* Making fuzzy preferences or guidelines testable and diffable.
- **Persona-conditioned rule generation for simulation** — Give each synthetic persona (for example, 500 per state from a persona dataset) its own generated moral and legal system, then run a proposal against every persona and measure agreement. *When:* Simulating how a population would react to a proposal or document before it is released.
- **Hill-climbing text against an adversarial judge** — Repeatedly edit the wording of a proposal and re-run it against every stakeholder system, keeping edits that reduce violations and ranking the edits by their effect on the vote count. *When:* Optimizing a document toward a target such as approval or agreement when the verifier is an LLM.

## Numbers
- Simulated Medicare bill vote moved from about 50-50 to passing with 52 votes after hill-climbing the bill language against per-senator moral systems. ([13:07](https://youtu.be/hOWU0KPUp1k?t=787))
- Persona experiment used 500 personas per US state, each with its own generated moral system and legal contract, drawn from an NVIDIA US persona dataset. ([14:36](https://youtu.be/hOWU0KPUp1k?t=876))

## Hot takes
- Current LLMs are now smart enough to do high-level moral reasoning and turn a person's values into a usable legal code.
- Most political disagreement is about core values people actually share, and the real differences only show up in nuanced cases that a stress test can surface.
- A stress-tested contract with a counterparty's terms can surface disagreements before signing, which gives people better information even when they cannot negotiate.

## Tools mentioned
Claude, GitHub

## Relevance to our work
- **agentos** (1/3): The adversarial loophole search is a red-team style probe that could be applied to guardrail rules, but the talk offers no measured results for guardrails. → *Optional: build a small attacker agent that tries to slip requests past the AgentOS exec-gate and PII rules, and log which rules it breaks.*
- **prosharness** (1/3): The attacker and judge loop resembles ProsHarness's plan, critique, and debate steps, and it adds an explicit auto-fix versus escalate decision. → *Compare the debate step with an adversarial-attacker role and a judge that auto-patches the plan and only asks for approval on real conflicts.*
- **general** (1/3): The auto-patch-or-escalate judge pattern is a reusable design for agent loops that run unattended but still need human decisions at true conflicts. → *Read the Loophole GitHub repo to check how the judge decides between auto-patching and escalation before reusing the pattern.*
