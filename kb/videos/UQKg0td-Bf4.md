# Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `UQKg0td-Bf4` · [watch](https://youtu.be/UQKg0td-Bf4) · **date:** 2026-06-18 · **length:** 13:03 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Steven Willmott · **orgs:** SafeIntelligence, Braintrust
- **topics:** testing-verification, evals, security-guardrails, mcp-and-tools · **tags:** spec-driven testing, agent specs, robustness testing, perturbation testing, agent cards, A2A, security testing, backyard RL, formal verification, product pitch

> Steven Willmott (SafeIntelligence) argues agent testing needs an explicit spec of data, rules, terminology, roles and robustness needs, kept separate from the implementation and run in a closed loop.

## Summary
Willmott, CEO of SafeIntelligence, says that a bigger or smarter model is not automatically a safer or better agent, since jailbreaks can work better on larger models and broad tool access widens the attack surface. He proposes spec-driven testing: write down what an agent must do, not just a dataset of inputs and outputs. The spec has six parts: ground-truth examples, business rules (for example a discount cap or a refund window), domain ontologies and internal terminology, domain substitutions that a generic LLM might confuse, roles and permissions, and robustness requirements such as tolerance to typos and rephrasing. He says the spec should feed two checks, security tests (the agent's stated domain is where it is most likely to be vulnerable) and robustness sweeps that vary inputs to see the range of valid answers. He points to A2A agent cards as a partial spec that still needs valid variation ranges. The main advice is to keep the spec independent of the framework, store it as versioned files in a repo, and use it to drive automated runs whose failures guide iteration, which he calls backyard RL rather than real RL. The talk is a short pitch for his company's product, but the framing is practical.

## Key ideas
- **A smarter or bigger model is not automatically a better or safer agent.** — Jailbreaks wrapped in a poem fail on small models, which cannot read them, but succeed on larger models that can. Broad agent remits add attack surface and test surface. Large models also cost more and run slower on simple tasks. ([2:24](https://youtu.be/UQKg0td-Bf4?t=144))
- **The real trade-off is between capability and the harm an agent can do.** — Harm has two parts: what instructions the agent accepts (how flexible the prompt can be) and what tools it can use in your infrastructure. An agent that can wire money is much riskier than one that answers questions. ([3:45](https://youtu.be/UQKg0td-Bf4?t=225))
- **A test dataset is not a full spec for an agent.** — A spec needs ground-truth examples, explicit rules (for example no discount above 10%, no refunds after 30 days), ontologies of what the business offers, internal terms and valid substitutions (gross profit vs gross sales), roles and permissions, and robustness requirements. Rules are hard to test for certain, so they need to be explicit. ([4:42](https://youtu.be/UQKg0td-Bf4?t=282))
- **Robustness means passing under stress, not only on the clean test set.** — Borrowed from vision testing (sunset, fog, camera shake), the questions for agents are: do typos break it, how many, and how stable are answers under rephrasing? These form task- and role-specific benchmarks. ([7:18](https://youtu.be/UQKg0td-Bf4?t=438))
- **The same spec can drive security tests and robustness sweeps.** — Knowing the agent's intended domain shows where it is most likely to be attacked, since it will engage with that domain. Varying inputs around the spec shows the range over which the agent still answers correctly. ([8:38](https://youtu.be/UQKg0td-Bf4?t=518))
- **Keep the spec independent of the implementation and version it like code.** — Teams may build on LangSmith or Vertex agents and later switch. Specs, integration tests, unit tests and penetration tests should live in a repo, outside any one framework, and be versioned. He compares the spec to OpenAPI. ([10:03](https://youtu.be/UQKg0td-Bf4?t=603))
- **Run the spec automatically in a loop to close robustness gaps.** — Run the tests, read the failures, then change the agent until the gaps close. He calls this backyard RL, because it works around the model rather than training it. ([11:31](https://youtu.be/UQKg0td-Bf4?t=691))

## Techniques
- **Six-part agent spec** — Write down ground-truth examples, business rules, ontology and domain terms, valid term substitutions, roles and permissions, and robustness requirements as explicit artifacts, separate from the agent code. *When:* Before deploying an agent that runs with little human review, or whenever a plain eval set misses rule violations.
- **Spec-driven security testing** — Pull the agent's intended tasks and domain from the spec into the security test plan, and aim attacks at the domains and tools the agent is meant to use. *When:* For agents with tool access in a specific domain, such as banking or support.
- **Input perturbation sweep** — Vary the inputs around each spec case (typos at increasing rates, rephrasings, changed conditions) and record where correct behavior breaks. *When:* For customer-facing agents where users type loosely or phrase requests in many ways.
- **Closed-loop spec iteration (backyard RL)** — Run the spec tests automatically, collect failures, change prompts or config, and repeat until the robustness gaps are filled. The model weights are not changed. *When:* When you have an automated harness and want to improve an agent without fine-tuning.
- **Specs as versioned repo files** — Keep specs in a GitHub repo in a neutral format, pull them into any test tool, and version them with the code. *When:* When the team may change frameworks or run several testing tools.
- **Agent cards plus variation envelopes** — Use an A2A agent card for the skill description, then add the valid range of inputs (for example, which people a meeting can be booked for) to define what counts as a fair variant. *When:* When exposing agents to other agents or when test variants need limits.

## Numbers
- Example business rule from the talk: no discount above 10% (an illustration, not a measured result). ([4:42](https://youtu.be/UQKg0td-Bf4?t=282))
- Example business rule from the talk: refunds refused more than 30 days after purchase (an illustration, not a measured result). ([4:42](https://youtu.be/UQKg0td-Bf4?t=282))
- The speaker's company has been operating for about three years. No benchmark or adoption numbers are given. ([0:00](https://youtu.be/UQKg0td-Bf4?t=0))

## Hot takes
- A bigger model is not automatically safer: jailbreaks can work better on larger, smarter models.
- A test dataset is not enough to specify an agent. Rules, terminology, roles and robustness must be explicit and tested.
- Keep agent specs independent of the framework so the tests survive a change of infrastructure.

## Tools mentioned
SafeIntelligence platform, A2A agent cards, LangSmith, Vertex AI agents, Braintrust, OpenAPI

## Relevance to our work
- **prosharness** (2/3): The closed-loop spec-run-fix pattern matches the plan, critique and debate loops, and a versioned spec could serve as the acceptance check for each checkpoint. → *Add a versioned spec file (rules, roles, robustness cases) that the ProsHarness critique step checks against on each loop, and see whether it reduces repeated failures across resumed runs.*
- **general** (2/3): Gives a concrete split between dataset evals and an explicit spec of rules, roles and robustness, which applies to any agent we test. → *Pick one live agent, write its rules, roles and terminology as a spec file, run typo and rephrase sweeps, and compare the gaps found with what the current eval set catches.*
- **agentos** (1/3): Its spec ideas (rules, roles, perturbation sweeps) could feed the eval layer, but the talk does not cover the proxy, memory or serving pillars. → *Read the SafeIntelligence product docs or write a short spec for one AgentOS agent to see which rules and perturbation cases it would add to the current evals.*
