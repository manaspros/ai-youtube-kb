# The Loop Is the Product — Roland Gavrilescu, Introspection

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `7taOQBfjDyE` · [watch](https://youtu.be/7taOQBfjDyE) · **date:** 2026-09-27 · **length:** 18:44 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Roland Gavrilescu · **orgs:** Introspection, xAI
- **topics:** skills-self-improvement, evals, agent-architecture, product-ux · **tags:** self-improving agents, agent loops, agent recipes, system distillation, LLM judges, calibration, pattern discovery, A/B testing, bandits, value per watt, harness versioning, Py.Recipes, Harbor

> Introspection's Roland Gavrilescu argues self-improving agent loops should distill a team's taste into versioned recipes of evals, judges and skills, validated in production and measured as value per watt.

## Summary
The speaker, a co-founder of Introspection (formerly at xAI), presents a framing he calls "the loop is the product" for always-on, long-running agents. He traces the idea to an early OpenClaw (originally CloudBot) example where an agent looped over Reddit, dealer and inventory data to negotiate a car price, with a verifiable end state. He says each loop's artifacts should feed a second loop, which he calls system distillation, and that these artifacts (harness, profiles, evals, tools, models, environment) should be packaged as portable, versioned "agent recipes" in a Git repo, which he says are an early release called Py.Recipes built on a harness and Harbor for evals. A worked example, a talent-sourcing agent, shows the method: cluster traces to find recurring behaviors, have agents draft judges from those patterns, and have a human only confirm the judgment rather than write the evals. Recipe changes are then tested offline and promoted only after production A/B or bandit tests show users agree with the taste encoded. The talk closes by proposing "value per watt" (value delivered versus economic cost) as the metric to optimize. Most claims are conceptual and the talk ends with a product pitch, with no benchmarks or cost figures given.

## Key ideas
- **The loop is the product** — The speaker argues the valuable part of an agent is the loop of acting, getting a verifiable signal, and feeding results back. Signal quality sets the loop's success rate, and the verifier decides whether a success is real. Automating yourself as the higher-level judge is the goal. ([0:08](https://youtu.be/7taOQBfjDyE?t=8))
- **Second loop distills the first loop's artifacts** — Each loop produces information about harnesses, profiles, evals, models, tools and the environment. A second loop should read what went well or wrong in the first and change the system, similar to how RL data recipes were iterated to fix hallucinations and reward hacking. ([4:28](https://youtu.be/7taOQBfjDyE?t=268))
- **Agent recipe as a versioned, provider-agnostic artifact** — The speaker proposes a recipe, kept in a Git repo, that bundles evals, prompts, skills, harness profiles and per-model tools. Failure patterns become judges and evals, and repeated behavior becomes skills and prompts. The recipe is meant to be owned by the team and not tied to one provider. ([5:27](https://youtu.be/7taOQBfjDyE?t=327))
- **Recipes encode the maker's taste** — The speaker says a recipe should record how and why a system was built, so another team could adopt the taste along with the code. Agents should calibrate toward the owner's taste, with the owner as the top judge. ([7:49](https://youtu.be/7taOQBfjDyE?t=469))
- **Value per watt is the metric** — Teams first reach a frontier by iterating in production, then need to make it economically viable. The speaker says the metric is the value delivered per unit of cost, and that a lower price for the same value is what would make users switch from a tool such as Claude Code. ([9:02](https://youtu.be/7taOQBfjDyE?t=542))
- **Humans calibrate judges instead of writing evals** — In the talent-sourcing example, clustering traces surfaces a behavior the team did not intend, such as reaching out to big-tech employees instead of hidden gems. An agent can draft the judge and eval from that pattern, and a human only confirms whether the judgment is right. ([12:53](https://youtu.be/7taOQBfjDyE?t=773))
- **Promote recipes only after production validation** — Recipe changes are proposed as diffs, tested on an offline eval set, then checked in production with A/B or multi-armed bandit tests. A version is promoted only when end users agree with the encoded taste. ([15:19](https://youtu.be/7taOQBfjDyE?t=919))

## Techniques
- **Trace pattern clustering to find signals** — Pull agent traces, group them by common behaviors or user frustrations, and turn each cluster into a candidate signal for the next change. *When:* When you have many production traces and need to find unexpected agent behavior worth codifying.
- **Agent-drafted judges with human calibration** — From a trajectory pattern, have an agent write the judge and eval. The human reviews only whether the judgment is right, then the judge runs across traces. *When:* When you want consistent LLM-judge criteria without a human writing every eval, and the criterion is a judgment call (for example, which candidates to target).
- **Recipe diffs as reviewable candidates** — Treat each change to the harness, prompts, skills, evals or tool profiles as a diff in a Git-versioned recipe. Check it on offline evals, then on live traffic. *When:* When you need reproducible agent configurations and a history of why each change was made.
- **Production A/B or bandit promotion** — Split live users between recipe versions, using a multi-armed bandit to shift traffic, and promote a version only when users prefer it. *When:* When offline evals do not show whether end users agree with the change.
- **Per-model harness profiles** — Keep separate harness profiles per model and store them in the same recipe so tools and prompts can be matched to each model. *When:* When one agent must run on several model providers.

## Hot takes
- The model is a commodity; the harness is a commodity; the loop and its recipe are the real product.
- Code was the first domain where this worked, and everything beyond customer support, legal and research will follow the same value-per-watt logic.
- Teams should not write evals by hand; agents should draft them and humans should only calibrate the judgments.
- A team's taste can be packaged as a portable recipe that another team can adopt.

## Tools mentioned
Py.Recipes, Harbor, OpenClaw (originally CloudBot), Claude Code, Codex, Cursor, Cognition

## Relevance to our work
- **agentos** (2/3): SkillForge's open questions are the success signal and skill-worthiness scoring. The talk's pattern clustering over traces, with an agent-drafted judge that a human calibrates, is a candidate answer to the success-signal question. → *Read the talk's trace-clustering and judge-calibration steps against SkillForge's open success-signal question; prototype a clustered-trace judge that a human approves before a skill is governed.*
- **prosharness** (1/3): The recipe idea of versioning harness profiles and eval suites per model in one repo could tidy ProsHarness configuration. The talk gives no checkpoint or resume ideas. → *Consider storing ProsHarness harness profiles and eval settings per model as one git-versioned recipe so each change has a recorded reason.*
- **general** (1/3): The A/B and bandit promotion step for agent changes is a general eval method that could apply to any agent we run in production. → *Note the production A/B promotion pattern (offline eval, then a bandit split on live traffic, then promote) for any future agent change that needs user validation.*
