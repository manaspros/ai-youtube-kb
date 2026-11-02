# Building uReview, Uber’s Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `EL123UNokkI` · [watch](https://youtu.be/EL123UNokkI) · **date:** 2026-09-18 · **length:** 15:07 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Will Bond, Ameya Ketkar · **orgs:** Uber
- **topics:** pr-code-review, evals, multi-agent, observability · **tags:** uber, ureview, code-review, feedback-loop, addressal-rate, agent-trajectory, team-customization, ai-linters, custom-agents, ownership-routing, inner-loop, outer-loop, agentic-sdlc, fabricator, github

> Uber's engineers explain uReview, their multi-agent code review system: how they built feedback-driven evals, team-owned customizations, and a cost/quality loop, plus why they think humans move up to an expanded outer loop.

## Summary
Will Bond and Ameya Ketkar of Uber describe uReview, an in-house automated code review system built because review had become the bottleneck: time to first review rose from about 3 hours in 2024 to 9 hours in 2026. The system routes review requests through a service to several generators tuned for cost and performance, then post-processes the output by rating, categorizing, filtering and deduplicating comments before posting. Their observability grew from surface metrics (cost, surveys) to classifying developer replies and tracking whether developers actually addressed each comment. Agent trajectory logs (tool calls and reasoning) let them tune runtime and cut wasted turns, and they found the model is confidently wrong without team-specific guidance. Team customizations come in layers (single-file and multi-file reviewers, AI linters with few-shot prompts, and custom team agents with knowledge bases and skills), co-located with code ownership and routed deterministically. Writing a review skill was easy, but running skills at scale with consistent quality and low cost took many iterations. Against a naive baseline they report about 60% lower cost and about 70% higher quality and accuracy, and they argue that inner-loop agents need higher accuracy than human-facing review, so humans move up to architecture and product judgment rather than leaving the loop.

## Key ideas
- **Code review became the bottleneck for AI-accelerated teams** — PR volume and size grew over 24 months, and time to first review rose from about 3h (2024) to 9h (2026) across thousands of engineers in six monorepos. ([0:12](https://youtu.be/EL123UNokkI?t=12))
- **Measure what developers do with comments, not only what they say** — Early observability (cost, NPS survey, Google Forms, Slack) was too shallow. They classified developer reply sentiment and then tracked the addressal rate, meaning whether a developer acted on a bot comment. This made the quality-to-cost ratio visible and fixable. ([4:45](https://youtu.be/EL123UNokkI?t=285))
- **Agent trajectory logs show why the agent did what it did** — Logging tool calls and the reasoning trace let them tune runtime and performance so the agent gave good results at low cost. ([5:52](https://youtu.be/EL123UNokkI?t=352))
- **The model is confidently wrong and needs team guidance and guardrails** — The model always sounds certain. Each team has its own style guide and anti-patterns, which must be encoded. Guardrails also tell the agent what not to spend turns on, since wasted turns reduce review quality. ([5:52](https://youtu.be/EL123UNokkI?t=352))
- **Layer the review stack: general reviewers, deep multi-file review, AI linters, custom agents** — Single-file logic-bug reviewers and multi-file deep reviewers per monorepo form the base. AI linters are few-shot prompts that pull deterministic context and check mechanical issues. Custom agents let a team link a knowledge base, past PRs and a skill. ([7:00](https://youtu.be/EL123UNokkI?t=420))
- **Co-locate customizations with code ownership and route deterministically** — Team rules live next to the code, reusing the existing ownership model. Deterministic routing decides which team gets which reviewer, model and generator, so rules roll out consistently to hundreds of teams. ([8:20](https://youtu.be/EL123UNokkI?t=500))
- **Writing the skill is easy; running it at scale is hard** — Teams simply asked Claude to write a review skill from their past PR reviews. The hard part was consistent quality and low cost at scale, which took many iterations from both the platform team and each team. ([9:39](https://youtu.be/EL123UNokkI?t=579))
- **The inner loop needs higher accuracy than human-facing review** — A low-quality comment makes an agent fix something, get reviewed again and fix backwards (the transcript's word is 'cavitation', likely a caption error). Agents will also fix 100 nits, which frustrates humans. ([12:05](https://youtu.be/EL123UNokkI?t=725))
- **The outer loop expands rather than disappears** — Humans move up a layer, focusing on architecture, domain expertise and product thinking instead of implementation details like performance and API compatibility. ([13:22](https://youtu.be/EL123UNokkI?t=802))

## Techniques
- **Reply-sentiment and addressal-rate tracking** — Classify developer replies to bot comments into positive or negative and categories. Measure whether the developer changed the code in response to each comment. Use these as the quality signal to tune prompts and reviewers. *When:* Any AI reviewer or agent that posts comments that humans respond to, where you need a quality signal beyond manual surveys.
- **Trajectory-based runtime tuning with turn guardrails** — Record each agent run's tool calls and reasoning. Find turns spent on work the agent should not do. Add explicit instructions about what to skip, and tune the runtime against cost and quality. *When:* Long agent runs with a time or turn budget, where quality drops because the agent wanders.
- **Tiered review generators with post-processing** — Run several generators (single-file, multi-file, linters, custom agents) tuned for different cost and performance. Then rate, categorize, filter and deduplicate the combined comments so only high-confidence, actionable ones reach the developer. *When:* When several review sources would otherwise produce duplicate or noisy output at high volume.
- **Few-shot AI linters with deterministic context** — Give a few-shot prompt plus deterministically gathered file context, so the model checks systematic or mechanical rules per file. *When:* Team-specific mechanical rules that are too narrow for a general reviewer but too fuzzy for a static linter.
- **Ownership-coupled rule distribution** — Store each team's review customizations next to its code, reuse the existing ownership system to route them, and let teams update rules with feedback visible to them. *When:* Many teams need their own review rules and a central team cannot maintain them all.

## Numbers
- Time to first review went from about 3 hours (2024) to about 9 hours (2026) ([0:12](https://youtu.be/EL123UNokkI?t=12))
- Scale: thousands of engineers, hundreds of teams, 12 sites, six language-specific monorepos ([0:12](https://youtu.be/EL123UNokkI?t=12))
- uReview produces about 25,000 comments per week ([9:39](https://youtu.be/EL123UNokkI?t=579))
- About 10% of comments receive some developer feedback ([9:39](https://youtu.be/EL123UNokkI?t=579))
- About 4% of PRs receive negative feedback ([9:39](https://youtu.be/EL123UNokkI?t=579))
- Overall addressal rate is about 67% ([9:39](https://youtu.be/EL123UNokkI?t=579))
- About three quarters of high-severity issues are addressed by developers ([9:39](https://youtu.be/EL123UNokkI?t=579))
- Versus a naive implementation, cost is down about 60% ([10:43](https://youtu.be/EL123UNokkI?t=643))
- Versus a naive implementation, quality and accuracy are up about 70% (the baseline for the percentage is not stated) ([10:43](https://youtu.be/EL123UNokkI?t=643))

## Hot takes
- The model doesn't know it's wrong. It always sounds 100% sure, so teams' style guides must be baked in.
- Writing a review skill is easy (ask Claude to write one from past PRs). Running skills at scale with consistent quality and low cost is the hard part.
- The inner loop needs higher accuracy than human-facing review, because agents will fix 100 nits and go back and forth on low-quality comments.
- The outer loop is expanding, not being killed. Humans move up to architecture and product thinking.

## Tools mentioned
GitHub, Fabricator, Claude

## Relevance to our work
- **agentos** (2/3): The addressal-rate and reply-sentiment signals are a concrete candidate for the open 'success signal' question in SkillForge, and the trajectory logs show how to find wasted agent turns. → *Prototype a SkillForge success signal from the rate at which an agent's output is acted on downstream (e.g. edited or accepted), and check it against manual labels on a sample.*
- **general** (2/3): Strong practitioner evidence for feedback-driven evals and layered customization of agent behaviour, both recurring interests. → *Read the uReview post-processing approach (rate, categorize, filter, deduplicate) before designing a multi-source agent output stage.*
- **prosharness** (1/3): Per-run trajectory logging and turn guardrails map loosely to ProsHarness checkpoint and resume, but the talk gives no concrete harness design. → *Log tool calls per turn in one long ProsHarness run and count turns that did not move the task before adding any new guardrail prompt.*
