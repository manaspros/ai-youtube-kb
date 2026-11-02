# Jev CEO: I made ChatGPT, now I'm building what's next

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `cJ0EOzey--o` · [watch](https://youtu.be/cJ0EOzey--o) · **date:** 2026-08-18 · **length:** 18:05 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Diego Almeida · **orgs:** OpenAI, TypeSafe
- **topics:** training-finetuning-rl, models-research, product-ux · **tags:** RLHF, RLVR, post-training, assistance-vs-automation, reward-model, calibration, hallucination, Claude Code, scaling laws, SaaS

> Former OpenAI post-training lead Diego Almeida argues RLHF models are built for assistance, not automation, and pitches a new post-training objective (calibrated decision making) at his stealth startup TypeSafe.

## Summary
The speaker, who says he co-authored InstructGPT (RLHF), GPT-4 and ChatGPT at OpenAI, frames the field as a split between "AI is going insanely well" and "AI is going insanely poorly." His explanation is that RLHF optimizes for human preference, so models are strong on tasks where a human is in the loop and weak on tasks meant to run unattended. He says over-promising is a built-in result of this optimization, and that the reward-model asymmetry makes wrong answers look right. He argues Claude Code is still an RLHF model and is part of the same "assistance era" as ChatGPT. He also says SaaS has barely changed since 2019 and that AI so far automates writing software without making software more expressive. He describes his company's approach as a third post-training target, calibrated decision making, next to RLHF (human preference) and RLVR (correctness). The talk is mostly position and framing, with no benchmarks, and the company is still in stealth.

## Key ideas
- **RLHF models are strong at human-in-the-loop tasks but weak at automation tasks, because the training goal is to please the human in the loop.** — The speaker says tasks like coding assistance have the human as the goal, while unattended back-office tasks need the model to just do the job correctly. He calls this the divide between assistance and automation. Lesson one of the talk. ([5:02](https://youtu.be/cJ0EOzey--o?t=302))
- **Over-promising is built into RLHF by design.** — The speaker says an RLHF model will always show a gap between what humans rate highly and what the results actually are, because human preference is the objective. He ties this to a cited study whose numbers he says are probably out of date. ([6:22](https://youtu.be/cJ0EOzey--o?t=382))
- **Optimizing for human preference makes wrong answers look right, because of an asymmetry in the reward model.** — Models get rewarded for seeming confident and punished for visible uncertainty. The speaker calls this lesson two: today's AI was designed for assistance through preference optimization. ([7:30](https://youtu.be/cJ0EOzey--o?t=450))
- **Claude Code is still an RLHF model and sits in the same assistance era as ChatGPT.** — The speaker says a coding agent trained with RLVR would look very different. He describes a trade-off where models get better at agentic work but stop following what the user wants, and says neither side of that trade-off adds automation. ([8:37](https://youtu.be/cJ0EOzey--o?t=517))
- **Software has not become smarter in the LLM era; AI has only made it cheaper to write.** — He says SaaS products have barely changed since 2019 and that AI has mostly added a chat assistant on the side. He argues the goal should be more expressive software, not only just-in-time software. ([9:54](https://youtu.be/cJ0EOzey--o?t=594))
- **Pre-training is not the problem; the way the model is unlocked is.** — In Q&A he says pre-training compresses internet knowledge into a useful core. He says hallucination comes from optimizing for human preference, in particular the reward asymmetry that pushes models to drop modes and sound confident. ([13:54](https://youtu.be/cJ0EOzey--o?t=834))
- **Each post-training branch has its own objective, and the speaker proposes a third one.** — RLHF optimizes human preference, RLVR optimizes pure correctness (he mentions log error rates), and his company optimizes calibrated decision making on top of pre-trained intelligence. He says the API shape differs in each case, and that new branches look alien until they become obvious in hindsight. ([15:19](https://youtu.be/cJ0EOzey--o?t=919))

## Techniques
- **Assistance vs automation diagnostic** — For each task, ask whether its goal is to please a human in the loop or to finish the work correctly without anyone watching. Tasks of the first kind suit RLHF-style models. Tasks of the second kind need a different optimization target. *When:* When deciding if a model or agent is fit for a task that will run unattended, or when judging why a model that looks strong performs poorly in a background workflow.
- **Cost-shifting to the user as a deployment pattern** — The speaker describes businesses sending users to endless docs in customer service rather than letting the AI make costly decisions. Costs fall on the user, not the business. *When:* Described as the state of the industry today, which the speaker criticizes; useful as a reference point when designing an agent that makes consequential decisions.
- **Name the optimization target before choosing a post-training method** — State what the model is optimized for (human preference, verifiable correctness, or calibrated decisions) and check whether that target matches the job, since the target shapes behavior such as confidence and over-promising. *When:* When evaluating or choosing a model or fine-tune for agent work, especially if its behavior seems to rely on pleasing the user.

## Numbers
- Roughly 100% of LLMs are trained with RLHF, based on the speaker's own reading of usage. ([5:02](https://youtu.be/cJ0EOzey--o?t=302))
- A cited study shows a gap between human preference and results in RLHF models. The speaker gives no figures and says the numbers have probably changed. ([6:22](https://youtu.be/cJ0EOzey--o?t=382))
- A skeptic-side claim, reported without verification, says the time LLMs can operate autonomously is growing exponentially. ([2:35](https://youtu.be/cJ0EOzey--o?t=155))
- The talk is 18:05 long and runs about 3 minutes over time. ([0:00](https://youtu.be/cJ0EOzey--o?t=0))

## Hot takes
- Over-promising is a feature of RLHF by design, not a bug.
- Pre-training is phenomenal; the real problem is how the knowledge is unlocked.
- Hallucination is intrinsic to optimizing for human preference.
- Claude Code is still RLHF-trained and still part of the assistance era.
- SaaS has not really changed since 2019; AI has mostly added a chatbot on the side.
- The original scaling laws were incorrect (teased, not explained).
- Data matters more than compute, and doing the right task matters more than data.

## Tools mentioned
Claude Code

## Relevance to our work
- **agentos** (1/3): The assistance-vs-automation split and the point that preference-trained models sound confident when wrong apply to how AgentOS would evaluate unattended agents. The talk gives no method. → *When writing AgentOS evals, score human-in-the-loop tasks and unattended tasks separately, and add a check that penalizes confident wrong answers.*
- **prosharness** (1/3): The speaker says a Claude Code run can get better at agentic work while drifting from what the user wants. This is the failure ProsHarness's checkpoint and critique loop would need to catch. → *Check whether ProsHarness's plan-critique loop verifies that a long run still matches the user's stated intent, not only that steps completed.*
- **general** (1/3): Gives a vocabulary for explaining why models over-promise (RLHF vs RLVR objectives), useful background for model choice on automation work. No measured results. → *Read the RLHF-vs-RLVR framing from this talk before the next models-research note on agent reliability; no concrete method to adopt yet.*
