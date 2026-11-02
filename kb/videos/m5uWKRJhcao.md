# First to Jailbreak Claude Wins $20,000

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `m5uWKRJhcao` · [watch](https://youtu.be/m5uWKRJhcao) · **date:** 2025-11-02 · **length:** 4:20 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, HackerOne
- **topics:** security-guardrails, models-research · **tags:** constitutional-classifiers, jailbreaking, red-teaming, input-output-classifiers, streaming-moderation, bug-bounty, false-positives, safety-challenge

> Anthropic's public jailbreak challenge for its constitutional classifiers (8 harmful questions, HackerOne bounty), with a walkthrough of the input/output classifier pipeline and its reported costs.

## Summary
The video covers Anthropic's public challenge for its constitutional classifier safety system: participants try to get Claude to answer 8 harmful questions with a universal jailbreak. The presenter tried it, could not pass question one, and reports the progress counts shown on the challenge site at the time (43, 14 and 5 passes on questions one to three, none on four). He explains the layered defence: an input classifier that wraps the prompt in a guard prompt, and an output classifier that scores streamed tokens and halts generation past a threshold. The pipeline for building the training data comes from a constitution that defines allowed and disallowed content, Claude-generated synthetic prompts, multilingual translation, and automated red-teaming that rewrites prompts in jailbreak style. The reported costs are 23.7% compute overhead and 0.38% more false positives. The video also covers the controversy over the challenge: a dataset that is not being released, and a bounty of up to $15,000 on HackerOne for a universal jailbreak. Most of the substance is a summary of Anthropic's research paper and the challenge rules, not original measurement.

## Key ideas
- **Anthropic runs a public challenge: get Claude to answer 8 harmful questions with one universal jailbreak. Only attempts on the challenge site are allowed, and off-site attempts could get the account banned.** — The presenter tried it, could not get past question one, and says he will not share any jailbreak because disclosure is not allowed. ([0:00](https://youtu.be/m5uWKRJhcao?t=0))
- **Reported progress is low: 43 people passed question one, 14 question two, 5 question three, and nobody question four at the time of filming.** — The presenter says a bug in the UI let a known jailbreaker (Pliny) skip questions, and Anthropic says it has fixed this. The presenter's source for these counts is the challenge site. ([1:26](https://youtu.be/m5uWKRJhcao?t=86))
- **The defence starts with a written constitution that says what may and may not be discussed. Claude is used to generate acceptable and unacceptable prompts, which become a synthetic training dataset.** — The dataset is translated into many languages. An automated red-teaming tool rewrites the prompts in the style of existing jailbreaks, which broadens coverage. ([1:26](https://youtu.be/m5uWKRJhcao?t=86))
- **The input classifier wraps the user prompt in a guard prompt that tells the model to watch for obfuscation, such as a harmful request disguised as a cake recipe.** — This is a classification step before generation, separate from the model's own refusal behaviour. ([2:32](https://youtu.be/m5uWKRJhcao?t=152))
- **The output classifier scores the streamed output as it is produced, estimating whether a token sequence contains disallowed text. Generation stops when the score crosses a threshold.** — This is a streaming check, so harmful output can be cut off partway through rather than only blocked after completion. ([2:32](https://youtu.be/m5uWKRJhcao?t=152))
- **The costs reported are 23.7% extra compute and 0.38% more false positives. The presenter calls the false-positive rate acceptable.** — These are the only overhead numbers in the video, and they come from the research paper as the presenter summarises it. ([2:32](https://youtu.be/m5uWKRJhcao?t=152))
- **The challenge has a community controversy: participants are not paid, the prompt dataset is not released, and the bounty is on HackerOne.** — The presenter reports the HackerOne bounty as up to $15,000 for a universal jailbreak. He also reports that 183 experts tried it and got through 5 of the 10 questions. This is a secondhand claim. ([2:32](https://youtu.be/m5uWKRJhcao?t=152))
- **The challenge stays open until February 10th.** — The presenter does not describe prize money for the challenge itself, even though the title says $20,000. ([3:47](https://youtu.be/m5uWKRJhcao?t=227))

## Techniques
- **Constitution-driven synthetic dataset for classifiers** — Write a constitution that says what content is allowed and disallowed. Use the model to generate prompts that fall on each side of it, then translate the set into many languages. Use an automated red-teaming step to rewrite the prompts in the style of known jailbreaks so the dataset covers adversarial phrasing. *When:* Building a safety classifier when hand-labelled adversarial data is scarce and you need coverage across languages and jailbreak styles. The video describes this as the method in Anthropic's paper.
- **Input guard prompt wrapped around user input** — Wrap the user's input in a classifier prompt that tells the model what to look for, including obfuscation such as disguised harmful requests. Use the verdict to block or allow the request before the main model runs. *When:* Adding a pre-generation check on untrusted user input, where the risk includes disguised or obfuscated requests rather than only plain keywords.
- **Streaming output classifier with a threshold** — Score the output as it streams, estimating the likelihood that a sequence of tokens contains disallowed content. Stop generation when the score passes a set threshold. *When:* Catching harmful output that a clean input filter missed. The trade-off is added latency and compute on every streamed response.
- **Separate harm-check grader for challenge submissions** — After a participant's answer is produced, a second model judges whether the answer is harmful and whether it actually answers the question. A pass moves the participant to the next question. *When:* Evaluating open-ended adversarial answers where exact-match checks do not work. The video describes this as the grading step in the challenge UI.

## Numbers
- Challenge has 8 harmful questions to pass with a universal jailbreak ([0:00](https://youtu.be/m5uWKRJhcao?t=0))
- Passes at the time of filming: 43 on question one, 14 on question two, 5 on question three, none on question four ([1:26](https://youtu.be/m5uWKRJhcao?t=86))
- Reported compute overhead of the classifiers: 23.7% ([2:32](https://youtu.be/m5uWKRJhcao?t=152))
- Reported increase in false positives: 0.38%, described as acceptable ([2:32](https://youtu.be/m5uWKRJhcao?t=152))
- HackerOne bounty of up to $15,000 for a universal jailbreak ([2:32](https://youtu.be/m5uWKRJhcao?t=152))
- Reported that 183 experts tried the HackerOne bounty and got through 5 of 10 questions ([2:32](https://youtu.be/m5uWKRJhcao?t=152))
- Challenge open until February 10th ([3:47](https://youtu.be/m5uWKRJhcao?t=227))

## Hot takes
- The title says 'Wins $20,000', but the video never mentions a $20,000 prize. The only money figure given is the HackerOne bounty of up to $15,000.
- The presenter did not complete any question, so the video adds no first-hand evidence about how strong the classifiers are.
- Most of the technical content is a secondhand summary of Anthropic's paper. The pipeline and cost figures are not independently checked.
- The presenter calls the 0.38% false-positive rate acceptable, which is his framing rather than a measured trade-off for any particular product.
- The claim that 183 experts got through only 5 of 10 questions is secondhand and has no source in the video.
- Quality is capped at 3 because the content is a news explainer built on a paper and a public challenge, with thin original data.

## Tools mentioned
Claude, Constitutional classifiers (Anthropic safety system), HackerOne (bug bounty platform)

## Relevance to our work
- **agentos** (2/3): Govrix Scout (L1) already has PII and prompt-injection scanning. The video describes a concrete input-classifier plus streaming output-classifier design with measured overhead and false-positive numbers, which is a useful baseline for comparison. → *Compare Govrix's prompt-injection scan against a guard-prompt input classifier and a streaming output classifier. Record added latency and false-positive rate on a labelled set of adversarial prompts, using the video's 23.7% overhead and 0.38% false-positive figures as rough targets, not as verified numbers.*
