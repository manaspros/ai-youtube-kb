# OpenAI's NEXT BIG LEAP in AI Reasoning

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `sFn8D9DutIw` · [watch](https://youtu.be/sFn8D9DutIw) · **date:** 2024-11-02 · **length:** 4:53 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS host (unnamed) · **orgs:** OpenAI, Anthropic
- **topics:** models-research, evals · **tags:** o1, reasoning-models, chain-of-thought, reinforcement-learning, benchmarks, model-comparison, cross-model-verification

> Short AI LABS news explainer on OpenAI's o1 preview: slower, chain-of-thought reasoning, vendor benchmark claims, and three single-prompt demos (strawberry letter count, math, murder mystery) cross-checked with Claude.

## Summary
The host introduces OpenAI's o1 model (called "GPT-01" in the transcript, previously codenamed Strawberry or Q-Star) and says it is the best model yet, which is hype the video does not back up. The explanation is brief: o1 responds more slowly than GPT-4.0 because it spends time reasoning, and it combines reinforcement learning with chain-of-thought to break problems into steps and catch mistakes early. The host repeats OpenAI's benchmark claims (89th percentile on competitive programming, top 500 on the USA Math Olympiad qualifier, PhD-level accuracy in physics, biology and chemistry) without evidence. Access is described as the o1-preview release for ChatGPT Plus and trusted API users. Three demos follow: counting the r's in "strawberry" (the older model fails, o1 gets it right with visible reasoning), a simple math problem where the older model answers immediately, and a murder-mystery logic puzzle where GPT-4.0 names Alice and o1 names Dave. The host then pastes the same puzzle into Claude, which agrees with o1. The evidence is one prompt per task with no repeats or scoring, so the video shows the behavior but not its reliability.

## Key ideas
- **o1 is slower than GPT-4.0 on purpose, because it spends time reasoning before it answers.** — The host ties the latency directly to the reasoning design and says it helps on logic, math, coding and science problems. ([0:00](https://youtu.be/sFn8D9DutIw?t=0))
- **The reasoning is attributed to a mix of reinforcement learning and chain-of-thought.** — Chain-of-thought lets the model split a task into smaller steps and solve them in order, which the host says helps it catch mistakes early. The explanation is high level and no training details are given. ([0:00](https://youtu.be/sFn8D9DutIw?t=0))
- **OpenAI's benchmark claims are repeated, not tested.** — The host cites 89th percentile on competitive programming, a top-500 placement in the USA Math Olympiad qualifier, and PhD-level accuracy in physics, biology and chemistry. These come from the vendor, and the video does not reproduce them. ([1:16](https://youtu.be/sFn8D9DutIw?t=76))
- **The strawberry letter-count case shows visible reasoning on a known failure.** — Earlier models were often wrong about how many r's are in 'strawberry'. The demo shows o1 thinking before giving the correct count along with its reasoning. The host notes that the codename Strawberry was a joke about that failure. ([1:16](https://youtu.be/sFn8D9DutIw?t=76))
- **A murder-mystery logic puzzle gives different answers from the two models.** — GPT-4.0 names Alice and o1 names Dave, with an explanation. The host sends the same prompt to Claude, which agrees with o1. Agreement across two models is used as the check, with no ground truth. ([2:37](https://youtu.be/sFn8D9DutIw?t=157))

## Techniques
- **Side-by-side prompt comparison** — Send the same prompt to the old and new model and compare the answers and any shown reasoning. The video uses a letter-count question, a math problem and a logic puzzle as the probes. *When:* Quick qualitative check of whether a model upgrade changes behavior on a known hard case. It is anecdotal and needs repeated runs and a scored set to be useful as evidence.
- **Cross-model verification** — Give the same puzzle to a second model and accept the answer when the two agree. *When:* Spot-checking a reasoning model's output when no ground truth is available. Agreement is weak evidence, since both models can be wrong in the same way.

## Numbers
- Response latency is longer than GPT-4.0 by design, because the model reasons before answering. No measurement is given. ([0:00](https://youtu.be/sFn8D9DutIw?t=0))
- o1 ranks in the 89th percentile on competitive programming questions (vendor claim). ([1:16](https://youtu.be/sFn8D9DutIw?t=76))
- o1 places in the top 500 in the USA Math Olympiad qualifier (vendor claim). ([1:16](https://youtu.be/sFn8D9DutIw?t=76))
- o1 exceeds PhD-level accuracy in physics, biology and chemistry (vendor claim). ([1:16](https://youtu.be/sFn8D9DutIw?t=76))

## Hot takes
- The video says o1 is 'the best AI model to ever exist' and builds on vendor benchmark claims. Its own demos are single prompts with no repeats or scoring.
- The strawberry, math and murder-mystery demos show the behavior but do not measure reliability. The Claude cross-check agreeing with o1 is weak evidence, since both could be wrong in the same way.
- The 'brings us closer to AGI' remark is the host's opinion and is not supported by the demos.
- The transcript misnames the model as 'GPT-01' and the codename history (Strawberry, Q-Star) is the host's account, not something verified in the video.

## Tools mentioned
OpenAI o1 (o1-preview), GPT-4.0 (as spoken in the transcript), ChatGPT Plus, Claude

## Relevance to our work
- **agentos** (1/3): The reasoning-model behavior (slower, more tokens per answer) bears on the InferCraft latency and cost tradeoffs, but the video gives no data on either. → *Read OpenAI's o1 system card or launch post for the reasoning-token and latency numbers before planning any AgentOS routing around reasoning models.*
- **prosharness** (1/3): Cross-checking one model's answer with another is a light version of ProsHarness's plan -> critique (Codex) -> debate loop. → *Treat cross-model agreement as weak evidence only, and build any critique step in ProsHarness around a scored eval, not a single spot-check.*
