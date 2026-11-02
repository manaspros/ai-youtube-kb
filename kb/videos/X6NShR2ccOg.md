# Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `X6NShR2ccOg` · [watch](https://youtu.be/X6NShR2ccOg) · **date:** 2026-05-18 · **length:** 18:35 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Alessandro Cappelli · **orgs:** Adaptive ML, AT&T, Manulife, CCS
- **topics:** training-finetuning-rl, evals, enterprise-adoption, inference-serving · **tags:** reinforcement-learning, RLOps, production-gap, small-models, LLM-as-judge, reward-models, synthetic-data, rejection-sampling, mock-environments, enterprise

> Adaptive ML's CCO argues RL, not prompting or SFT, is the systematic way to take enterprise LLMs and agents from MVP to production, using environments, rewards, and LLM judges. Mostly a product pitch for their platform.

## Summary
Alessandro Cappelli, co-founder and chief customer officer of Adaptive ML, argues that getting from an MVP to production is the real marathon, and that most MVPs built on prompting or instruction fine-tuning cannot be improved systematically. He claims reinforcement learning is much more effective than SFT or prompting at steering model behavior, so a smaller specialized model can match a larger one. He says that makes serving cheaper and faster and gives the enterprise ownership of its data. For agents, he describes training inside an environment with mocked tools and an LLM-played user, using business KPIs or LLM judges as rewards. Rejection sampling on rewarded trajectories then bootstraps a synthetic dataset. Humans mainly write rubrics and scenarios, first to calibrate judges and later to train reward models once production feedback accumulates. The talk ends by pitching their Adaptive Engine, which hides RL recipes such as PPO and GSPO behind pre-built pipelines. The talk gives few hard numbers and no independent benchmarks, so treat it mainly as a framing of the RL-for-production argument.

## Key ideas
- **The hard part is not the MVP but the path from MVP to production and beyond, which is a continuous improvement loop.** — The speaker calls the MVP the 'first mile' and says the 'myth of the last mile' is wrong. He claims 95% of GenAI pilots fail to reach production. He argues the secret is to shorten the model life cycle by folding in feedback from many sources. ([1:06](https://youtu.be/X6NShR2ccOg?t=66))
- **Prompting and instruction fine-tuning cannot improve a system in a measurable, systematic way.** — With prompting, fixing one defect can create another, and there is no scientific way to monitor the change. With SFT, the only lever is rebuilding the dataset, which is expensive and must be repeated after launch. The speaker says RL is disproportionately more effective at steering behavior than either. ([2:04](https://youtu.be/X6NShR2ccOg?t=124))
- **RL-trained small models are pitched as the economic path to scale, with ownership as a side benefit.** — The claim is that RL can match SFT performance with a much smaller model. Smaller models are cheaper and faster to serve, and the enterprise owns the trained model and its data, so it is not exposed to upstream model updates. The speaker says this applies to any use case, and agents only make the case stronger. ([4:30](https://youtu.be/X6NShR2ccOg?t=270))
- **Agent training can start without real agent data, because a reward-scored environment yields its own synthetic dataset.** — No web dataset shows agents using tools. If you have an environment and a reward, the good trajectories become a by-product. Rejection sampling on those trajectories bootstraps the first SFT dataset. Existing customer-agent transcripts can seed a realistic mock user. ([9:42](https://youtu.be/X6NShR2ccOg?t=582))
- **The reward is where the human sits in the loop, and the reward can be a business metric, a verifiable check, or an LLM judge.** — Example rewards include whether code runs, the containment rate of a support bot, tone, and business-rule compliance. Humans write rubrics, judge prompts, and scenarios. The speaker says this takes minutes to hours, not weeks of repeated annotation campaigns. ([11:07](https://youtu.be/X6NShR2ccOg?t=667))
- **Human feedback is used in stages: prompted judges first, then reward models trained once production data exists.** — With 10 to 20 feedbacks, the feedback calibrates the LLM judges. The speaker starts with a large prompted open model as judge. With thousands of production feedbacks, a reward model is trained to scale that signal into RL. Implicit feedback would need a use-case-specific reward model. Candidate training setups are compared on the same eval. ([15:03](https://youtu.be/X6NShR2ccOg?t=903))
- **RL is hard to run, so the platform wraps the algorithm behind recipes.** — The speaker says PPO needs orchestration of four LLMs at once. The user defines rubrics and the platform supplies recipes such as GSPO. The talk frames the platform as observe, train, and serve in one place, with defect finding before and after production. ([13:45](https://youtu.be/X6NShR2ccOg?t=825))

## Techniques
- **Mock environment with mock tools and an LLM-played user** — Mock the tools the agent calls, and if needed a user simulated by an LLM. Seed the user with real customer-agent transcripts so the simulated user is realistic and difficult. Then run RL against it. *When:* When an agent exists but its training environment does not, or when real agent trajectories are not available.
- **Rejection-sampling bootstrap from reward-scored trajectories** — Run the agent in the environment, keep only trajectories the reward marks as good, and use them as the SFT dataset to bootstrap the first training run. *When:* When there is no agent training data but there is an environment with a computable reward.
- **Business KPI as the RL reward** — Use a measurable outcome such as containment rate, the share of calls resolved end to end by the model, as the reward to maximize directly. *When:* When the business has a clear automatic success metric for the agent.
- **LLM judge with human-written rubric, graduated to a reward model** — Humans write the judge rubric and scenarios. Start with a large prompted model as judge, calibrated on a handful of human labels. When production feedback is plentiful, train a reward model on it and use that as the RL signal. *When:* When subjective quality such as tone or policy compliance matters and human labels are scarce early on and plentiful later.
- **Prefer a smaller RL-trained model for high-volume or latency-bound features** — Train a small open model on the enterprise's own data with RL, instead of calling a frontier model, then serve it at the required latency. *When:* When per-call cost at scale or a speech latency budget makes frontier model calls impractical.

## Numbers
- Speaker claims 95% of GenAI pilots fail to reach production (his cited figure, not sourced in the talk) ([1:06](https://youtu.be/X6NShR2ccOg?t=66))
- Summarizing every customer-agent transcript at AT&T costs millions of dollars at scale ([5:31](https://youtu.be/X6NShR2ccOg?t=331))
- Speech-to-speech latency: half a second already feels weird; a third of a second is ideal and needs a small model ([5:31](https://youtu.be/X6NShR2ccOg?t=331))
- RL can reach the same performance as SFT with a much smaller model (shown in a plot the speaker does not quantify in the transcript) ([4:30](https://youtu.be/X6NShR2ccOg?t=270))
- PPO requires orchestrating four LLMs at the same time ([13:45](https://youtu.be/X6NShR2ccOg?t=825))
- Judge calibration starts from roughly 10 to 20 human feedbacks ([15:03](https://youtu.be/X6NShR2ccOg?t=903))
- Reward-model training becomes possible once there are thousands of production feedbacks ([17:18](https://youtu.be/X6NShR2ccOg?t=1038))

## Hot takes
- RL is the one algorithm that industrializes bringing models into production; prompting and SFT cannot be improved systematically.
- 95% of GenAI pilots fail to reach production, and the hard part is the MVP-to-production path, not the MVP.
- Human-in-the-loop annotation campaigns are usually expensive or useless; humans should only write rubrics and scenarios.
- Agents make small-model RL more important, because agent token costs scale faster than single-call use cases.

## Tools mentioned
Adaptive Engine, PPO, GSPO, Gemma, Mistral, Qwen

## Relevance to our work
- **agentos** (1/3): AgentOS has no training pillar. The environment-plus-reward and rejection-sampling idea is adjacent to EvolveCraft and SkillForge, which mine agent telemetry into skills. → *Read the rejection-sampling idea (reward-verified trajectories as a dataset) as one candidate input for SkillForge's skill-worthiness scoring when that design is written up.*
- **general** (1/3): Its calibrate-judge-then-reward-model staging matches the recurring interest in LLM-judge evals for agents and data-quality tasks. → *When building an LLM-judge eval for agent or entity-resolution outputs, calibrate the judge on 10 to 20 hand labels first and record the rubric as the human input.*
