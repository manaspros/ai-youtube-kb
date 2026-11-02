# Training Taste — Thais Castello Branco, Taste Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `sDMGWK4wZ_w` · [watch](https://youtu.be/sDMGWK4wZ_w) · **date:** 2026-09-18 · **length:** 15:06 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Thais Castello Branco · **orgs:** Taste Labs, General Intelligence Company of New York
- **topics:** evals, product-ux, vibe-coding-app-building, context-engineering · **tags:** ai-slop, design, taste, llm-as-judge, classifiers, brand-extraction, creativity, inference-time-quality, out-of-distribution-generation

> Thais Castello Branco (Taste Labs) on measuring and fighting "AI slop" in design: decompose subjective quality into checkable parts, build feature classifiers that flag slop, and turn a brand into structured context the agent both follows and is graded against.

## Summary
The speaker, founder of Taste Labs, frames AI slop (repetition, lack of fit, low intent) as the problem to solve and argues subjective domains like design need to be decomposed until parts become checkable. Objective sub-skills such as palette choice, contrast and alignment can be judged against expert-agreed rules, while aesthetics need data-driven methods because experts disagree. The team analyzed about 2 million websites from the past decade, plus synthetic AI-generated sites, and found homogenization predates AI while AI amplifies it. They trained small "probe" classifiers on extracted features (colors, typography, layout, audience) and report that combined probe signals predict slop better than an LLM-as-judge, though no figures are given. At inference time they propose a "creativity" approach that intentionally breaks category conventions on a few dimensions rather than raising temperature, and a brand API that turns a brand URL into structured components for agents to follow and to verify against. The talk closes with one demo, a slide deck in a studio's brand made with and without the extraction step, and the claim of higher fidelity is shown only as a visual comparison.

## Key ideas
- **Slop is easier to define than greatness** — Speaker says people agree on what slop looks like (repetition, soullessness, lack of fit, low intent) even when greatness is hard to define. Treat slop as the measurable target. ([3:20](https://youtu.be/sDMGWK4wZ_w?t=200))
- **Split subjective quality into objective and aesthetic parts** — Once a design problem is narrowed (palette choice, contrast, alignment), it becomes close to deterministic and expert-agreed. Aesthetics have expert disagreement, so they need data-driven methods instead of hand-written rules. ([1:11](https://youtu.be/sDMGWK4wZ_w?t=71))
- **Lack of fit is a key slop signal** — Two different clients (a pet shop and a finance firm) getting converging designs shows missing context. Systems should interpret user intent and add context rather than one-shot. ([4:27](https://youtu.be/sDMGWK4wZ_w?t=267))
- **Slop is a long-running internet trend that AI accelerates** — Speaker's crawl of about 2M sites over 10 years shows homogenization (palettes, layouts) before AI. AI makes the repetition more visible across unrelated contexts. ([6:40](https://youtu.be/sDMGWK4wZ_w?t=400))
- **Probe classifiers for slop** — Mine patterns from extracted features, train small single-characteristic classifiers, then score sites by how often several probes fire together. Speaker says this predicts slop better than asking an LLM to judge. ([7:43](https://youtu.be/sDMGWK4wZ_w?t=463))
- **Fix slop at inference time, not only in the model** — Speaker argues intent and context get resolved at the moment the user interacts with the system, so app-layer judgment and verification matter as much as model improvements. ([9:01](https://youtu.be/sDMGWK4wZ_w?t=541))
- **Creativity means intentional rule-breaking, not randomness** — Learn the expectations of a category (what a good pitch deck looks like), then diverge on a few dimensions while keeping the rest. Speaker explicitly rejects simply raising temperature. ([10:06](https://youtu.be/sDMGWK4wZ_w?t=606))
- **Turn a brand into structured context the agent can be judged against** — The brand API takes a brand URL and extracts specific components an agent can follow. The same structure lets a reviewer check whether the agent is adhering and where it fails. A pre-built brand index can supply brand systems to users who have none. ([11:16](https://youtu.be/sDMGWK4wZ_w?t=676))

## Techniques
- **Decompose subjective quality into probes** — Mine features from a corpus (colors, typography, layout, audience), train a small classifier per characteristic, then score an output by the co-occurrence of several probe hits. *When:* You need a cheap, measurable quality or slop gate on generated artifacts and want something that may beat a single LLM judge.
- **Split objective checks from aesthetic judgment** — Write deterministic or expert-agreed rules for sub-problems that can be defined narrowly (contrast, alignment, palette), and use data-driven scoring for the rest. *When:* A subjective task (design, writing) needs verification, and parts of it can be defined tightly enough to be checked exactly.
- **Rule-aware intentional divergence** — First retrieve or state the category's conventions (what a good deck or site in this category looks like), then deliberately change a few of them while keeping the others. *When:* Output keeps collapsing to a generic average and you want distinctive results that still fit the category.
- **Brand spec as both generation context and rubric** — Extract a brand from a URL into structured components. Feed them to the agent as instructions, then reuse the same components as the checklist for judging adherence. *When:* An agent produces branded output and you need to check whether it stayed on-brand.
- **Retrieve pre-built brand systems** — Keep an index of ready-made brand systems and retrieve a matching one by mood or style, instead of generating a brand from scratch at request time. *When:* End users have no brand of their own and generative defaults would drift toward generic output.

## Numbers
- Corpus of about 2 million websites crawled over the past 10 years, plus a synthetic set of AI-generated design sites for comparison ([6:40](https://youtu.be/sDMGWK4wZ_w?t=400))
- Probe-based slop prediction described as performing better than LLM-as-judge; no accuracy or margin figures given ([7:43](https://youtu.be/sDMGWK4wZ_w?t=463))
- Talk length 15:06; company emerged from stealth a few weeks before the talk ([0:08](https://youtu.be/sDMGWK4wZ_w?t=8))

## Hot takes
- AI slop is the enemy to beat, and design and writing deserve the same eval and training effort that coding and math have received.
- Judgment is becoming more valuable than ever as generation cost falls to zero.
- Inference-time context and verification matter as much as, or more than, making the model itself better.
- Asking every user to develop taste is not realistic, so the tooling has to supply it.

## Tools mentioned
Claude Design, Wayback Machine-style web crawl

## Relevance to our work
- **agentos** (1/3): AgentOS could in principle gate generated content, but the talk is design-specific and gives no reproducible method. → *Low priority: if AgentOS ever needs a quality gate on generated text or UI, benchmark a small set of cheap feature classifiers against an LLM judge on a labelled sample.*
- **prosharness** (1/3): ProsHarness runs checkpointed agent work and could check agent-produced UI output at checkpoints. → *Try a per-checkpoint rubric of cheap deterministic checks (contrast, alignment, palette rules) before any LLM judge runs on agent-written UI output.*
- **general** (1/3): The brand-spec pattern, where one structured artifact serves as both the generation context and the grading rubric, is a reusable context-engineering idea. → *Apply the same pattern to any style or convention doc an agent must follow: derive one structured checklist and feed it to both the agent prompt and the reviewer.*
