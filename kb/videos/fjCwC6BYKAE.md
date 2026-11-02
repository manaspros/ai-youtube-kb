# Claude Killer? My Review on Kimi K2 Thinking After Days of Testing

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `fjCwC6BYKAE` · [watch](https://youtu.be/fjCwC6BYKAE) · **date:** 2025-12-02 · **length:** 6:22 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** AI LABS host (unnamed) · **orgs:** Moonshot AI, Anthropic, OpenAI, Make
- **topics:** models-research, coding-agents, token-cost-efficiency · **tags:** kimi-k2-thinking, open-weight-models, model-comparison, context-window, cost, ui-generation, firebase-auth, sponsored

> Hands-on review of Moonshot's Kimi K2 Thinking via a coding agent: cheap and context-efficient, but slower and weaker than Claude on UI, game and feature-addition tasks.

## Summary
The host tested Kimi K2 Thinking for four days, mostly through a VS Code coding agent (transcribed as "Klein") and partly through the web interface. Each task used one prompt, and the same prompt was run on Claude for comparison. On a component-heavy fashion-site UI prototype, both models produced comparable results, with Claude ahead because it added a modal that Kimi skipped. Kimi used about 52.5k tokens of context and cost about 20 cents, versus Claude's 137k tokens (68% of its window) and a higher cost, though Kimi took longer. On a 3D pinball game, Kimi's build ended in a blank state with no way to restart, and repeated prompt fixes did not change the outcome, while Claude's version was playable. When adding Firebase authentication to an existing dashboard, both models produced working login and signup flows, but Kimi's login page ignored the site's theme and no verification email was sent. The verdict is that Kimi is slower, less consistent on design and complex tasks, and not yet at the level of GPT-5 or Sonnet 4.5, but its cost makes its performance impressive. The video contains a sponsored segment for Make.com.

## Key ideas
- **Kimi K2 Thinking is marketed as the best open-source thinking model and priced well below Sonnet 4.5 and GPT-5.** — The host frames the release as a challenge to closed models on price and claimed benchmark parity, then sets out to check the hype with hands-on tests. ([0:00](https://youtu.be/fjCwC6BYKAE?t=0))
- **On a one-prompt UI prototype, Kimi and Claude came out comparable, with Claude ahead because it added a modal that Kimi left out despite it being in the instructions.** — Kimi's site was interactive and let the user change product colours, but had some broken parts. Claude produced the same site faster. ([0:00](https://youtu.be/fjCwC6BYKAE?t=0))
- **Kimi was far more context- and cost-efficient on the UI task even though it was slower.** — Kimi used about 52.5k tokens of context and cost about 20 cents for the whole task. Claude used 137k tokens (68% of its window) and cost more. ([1:19](https://youtu.be/fjCwC6BYKAE?t=79))
- **On a 3D pinball game, Kimi's build failed in a way that could not be recovered from, and re-prompting did not fix it.** — The game ended with a blank screen after a new game started, with no way back to the home page. Iterating on the logic prompt did not move it past the same stage. Claude's version was partly broken but playable and included sound effects. ([3:34](https://youtu.be/fjCwC6BYKAE?t=214))
- **Adding Firebase authentication to an existing dashboard worked on both models, but Kimi's login page did not follow the site's theme.** — Kimi's signup gave access to the existing dashboard and sign-out worked, but no verification email arrived. Claude's login page integrated more cleanly and matched the theme. ([5:02](https://youtu.be/fjCwC6BYKAE?t=302))
- **The verdict is that Kimi is slower, weaker on design consistency and complex tasks, and not yet at GPT-5 or Sonnet 4.5 level, though its cost-effectiveness is impressive.** — The host calls the hype overstated but credits the price-to-performance ratio and says Moonshot could become a serious competitor. ([5:02](https://youtu.be/fjCwC6BYKAE?t=302))

## Techniques
- **Same-prompt A/B against a reference model** — Give the identical prompt to the candidate model and to the incumbent (here Claude), then compare output quality, wall-clock time, context tokens used and cost per task. *When:* When evaluating a new cheap model against a known best model in the same coding agent, to separate quality gaps from cost and speed gaps.
- **Feature addition to an existing codebase** — Build a small app first (here, a project-management dashboard), then ask the model to add a cross-cutting feature such as Firebase authentication. Check that existing features still work, that the new feature works, and whether the new UI matches the existing theme. *When:* To test integration with existing code and design consistency, not only greenfield generation.
- **Iterate the prompt on a stuck build** — When the generated game got stuck, the host gave corrective instructions for the logic over several rounds and checked whether behaviour changed. *When:* As a recovery test: a model that cannot progress on repeated corrective prompts is weak for multi-step debugging, even if its first output looked plausible.

## Numbers
- Kimi K2 Thinking UI task used about 52.5k context tokens and cost about 20 cents in total. ([1:19](https://youtu.be/fjCwC6BYKAE?t=79))
- Claude used 137k context tokens on the same UI prompt, 68% of its context window, and cost more than Kimi. ([1:19](https://youtu.be/fjCwC6BYKAE?t=79))
- The host tested the model for four days, with one prompt per task and no repeated runs reported. ([0:00](https://youtu.be/fjCwC6BYKAE?t=0))
- Kimi K2 Thinking was described as priced significantly lower than Sonnet 4.5 and GPT-5, with no figures given. ([0:00](https://youtu.be/fjCwC6BYKAE?t=0))

## Hot takes
- Kimi K2 Thinking did not live up to the hype: slower than expected, inconsistent design, and weak on complex tasks compared with Sonnet 4.5 and GPT-5.
- Its cost-effectiveness makes its performance genuinely impressive, and Moonshot could become a serious competitor.
- Each comparison used a single prompt and a single run per model, so the results are anecdotal.
- A sponsored Make.com segment at 2:29 caps quality at 2.

## Tools mentioned
Kimi K2 Thinking (Moonshot AI), Claude (Sonnet 4.5 named as the comparison point), GPT-5, Klein (transcribed name, likely the Cline VS Code coding agent; used as the editor agent), Firebase Authentication, Make (sponsor)

## Relevance to our work
- **agentos** (1/3): The only quantitative data point is per-task context tokens and cost for an open model versus Claude. That is relevant to cost tracking for models routed through the proxy, but it is a single-run anecdote. → *When benchmarking models behind the proxy, log context tokens and cost per task alongside quality, as the video does, instead of relying on list price.*
