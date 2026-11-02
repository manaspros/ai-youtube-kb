# Gemini 3 Flash Is Incredible… Until It Isn’t

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `YoBiCEXUqmU` · [watch](https://youtu.be/YoBiCEXUqmU) · **date:** 2026-01-02 · **length:** 4:56 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Google, Artificial Analysis, Anthropic, OpenAI
- **topics:** models-research, token-cost-efficiency, evals · **tags:** gemini-3-flash, model-review, hallucination, pricing, speed-vs-intelligence, one-shot-test, multimodal

> Better Stack's quick review of Gemini 3 Flash: fast and cheap with strong benchmark scores, but a high hallucination score rules it out for accuracy-sensitive work, and the presenter would not use it for coding.

## Summary
The presenter tests Gemini 3 Flash with a one-shot browser game prompt (a Minecraft-style clone, transcribed as "3GS", likely Three.js). Flash produces a playable but rough result in about 32 seconds, while Opus 4.5 takes around 5 minutes on the same prompt. Artificial Analysis ranks Flash above Opus 4.5 on its Intelligence Index and puts it one point behind on coding. The presenter still would not recommend it for coding, citing his experience that Google models follow instructions and understand codebases less reliably than Claude models. The main caveat is the hallucination benchmark, where Flash scores 91 and is one of the worst models tested, despite leading on accuracy. Pricing is $0.50 per million input tokens and $3 per million output tokens, with a 1M-token context window. The video closes by noting the multimodal inputs (images, video, audio, PDF) and a Google demo of real-time video analysis.

## Key ideas
- **Flash is fast and cheap, and Artificial Analysis ranks it above Opus 4.5 on its Intelligence Index.** — The presenter frames Flash as a model that keeps most of the intelligence while staying fast and cheap, based on the Artificial Analysis index. ([0:00](https://youtu.be/YoBiCEXUqmU?t=0))
- **One-shot game generation shows speed, with rough output.** — Flash generates a basic Minecraft-style clone in about 32.4 seconds, versus around 5 minutes for Opus 4.5. The result is playable, but it has clipping, fast movement, and other issues. The presenter argues that cheap follow-up fixes could still beat Opus on cost. ([0:00](https://youtu.be/YoBiCEXUqmU?t=0))
- **Coding is the weak spot for Google models in the presenter's experience.** — Flash is one point behind Opus 4.5 on the Artificial Analysis coding index, and Google's own numbers show it beating Gemini 3 Pro on SWE-bench Verified. The presenter still would not use it for coding, citing weaker codebase understanding and instruction-following than Claude models. He suggests it may suit occasional repetitive tasks. ([1:15](https://youtu.be/YoBiCEXUqmU?t=75))
- **Accuracy and hallucination are separate measures, and Flash splits them.** — Flash is top on the Artificial Analysis knowledge index and on accuracy, meaning it gets the most answers right. But it scores 91 on the hallucination benchmark, which measures wrong answers given instead of refusals or admitting uncertainty. The presenter's summary is that it knows a lot but does not know what it does not know. ([2:55](https://youtu.be/YoBiCEXUqmU?t=175))
- **Pricing is low but not the cheapest on the speed-versus-intelligence chart.** — Flash costs $0.50 per million input tokens and $3 per million output tokens, with a 1M-token context. That is about 4x cheaper than Gemini 3 Pro, or 6x above 200k tokens. Its price places it just outside the ideal quadrant of the Artificial Analysis cost-versus-intelligence chart. ([2:55](https://youtu.be/YoBiCEXUqmU?t=175))
- **Multimodal input is the main upside for the price.** — Flash accepts images, video, audio, and PDFs. Google's demo analyzes video and hand-tracking input at once to give real-time guidance in a slingshot game. ([4:09](https://youtu.be/YoBiCEXUqmU?t=249))

## Techniques
- **One-shot build as a speed and cost probe** — Give the model one large generation prompt (here, a Minecraft-style voxel clone in Three.js), time the run, then play the output to judge quality. Compare time and cost against a stronger model on the same prompt. *When:* Quick first pass when comparing models on speed and rough capability. The presenter treats it as directional only, not a reliable quality measure.
- **Cheap model plus correction prompts** — Accept that a fast, cheap model may produce flawed output, then send follow-up prompts to fix the specific problems instead of paying for a stronger model's single pass. *When:* Cost-sensitive work where errors are visible and cheap to check, such as repetitive edits. The presenter says it might still come out cheaper than Opus even with a few fixes.
- **Check hallucination separately before using a model for factual answers** — Look at the hallucination or refusal benchmark next to accuracy and the aggregate index. A model can lead on accuracy and still fail badly on not making things up. *When:* Before routing any use case where a fabricated answer would be costly, such as factual lookup, compliance, or support.

## Numbers
- Opus 4.5 takes around 5 minutes to build the Minecraft-style clone; Gemini 3 Flash finishes in 32.4 seconds. ([0:00-1:15](https://youtu.be/YoBiCEXUqmU?t=0))
- Flash ranks above Opus 4.5 on the Artificial Analysis Intelligence Index. ([0:00](https://youtu.be/YoBiCEXUqmU?t=0))
- Flash is one point behind Opus 4.5 on the Artificial Analysis coding index. ([2:05](https://youtu.be/YoBiCEXUqmU?t=125))
- Flash scores 91 on the Artificial Analysis hallucination benchmark, one of the worst models tested (the presenter's reading; the unit is not stated). ([2:55](https://youtu.be/YoBiCEXUqmU?t=175))
- Price is $0.50 per million input tokens and $3 per million output tokens, with a 1M-token context window. ([2:55](https://youtu.be/YoBiCEXUqmU?t=175))
- Flash is about 4x cheaper than Gemini 3 Pro, or 6x cheaper above 200k tokens. ([2:55](https://youtu.be/YoBiCEXUqmU?t=175))

## Hot takes
- A model can lead the accuracy and index rankings and still be one of the worst on hallucination; the presenter says it 'doesn't know what it doesn't know'.
- Not recommended for coding; Claude models are preferred on codebase understanding and instruction-following, based on the presenter's experience.
- Even if a cheap model needs several follow-up fixes, it may still beat Opus 4.5 on cost.
- The verdict rests on one game-generation prompt and on benchmarks from Artificial Analysis and Google, not on the presenter's own evals.

## Tools mentioned
Gemini 3 Flash, Gemini 3 Pro, Gemini 2.5 Flash, Claude Opus 4.5, Artificial Analysis (Intelligence Index, coding index, knowledge and hallucination benchmark, cost-vs-intelligence chart), SWE-bench Verified, Three.js (transcribed as '3GS')

## Relevance to our work
- **agentos** (2/3): AgentOS has strategy routing and cost control, and this review gives a concrete reason to route by hallucination rate as well as price and speed. → *Add a hallucination or refusal check to the model-routing criteria in Govrix Scout, and run a small factual-QA set on Gemini 3 Flash before sending any factual traffic to it.*
- **prosharness** (1/3): ProsHarness drives Claude Code, and the talk's coding verdict favors Claude models over Flash for codebase work. → *Keep Opus-class models for coding steps. Consider a cheap Flash-tier model only for repetitive subtasks, after a check of its error rate on those tasks.*
