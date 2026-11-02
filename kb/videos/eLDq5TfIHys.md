# Claude Just Introduced a New Way To Fix Your UI

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `eLDq5TfIHys` · [watch](https://youtu.be/eLDq5TfIHys) · **date:** 2025-12-02 · **length:** 10:50 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** AI LABS host (unnamed) · **orgs:** Anthropic, Scrimba (sponsor), Google Fonts
- **topics:** skills-self-improvement, claude-code, context-engineering, vibe-coding-app-building · **tags:** front-end-design, skills, system-prompt, distributional-convergence, typography, ai-slop, artifacts, context-window, sub-agents, mcp, google-fonts

> AI LABS tests Anthropic's front-end design skill guidance in Claude Code: typography and theme prompts, a 400k-token mega-prompt, and skills that often fail to auto-load.

## Summary
The host walks through Anthropic's article on improving front-end design with skills. The core claim is that models drift toward the highest-probability, safest UI ("distributional convergence"), and that steering them with targeted design instructions helps. Skills are pitched as a way to load UI guidance only when needed, keeping the context window clean compared with a bloated system prompt. Anthropic's examples go dimension by dimension (typography, then themes and aesthetics) and are then combined into one very large general-purpose prompt, which the host says is about 400k tokens. The host reproduces each step in Claude Code: he turns a prompt into a skill, places it in the project's skill folder, and finds that Claude Code often does not invoke the skill unless he names it explicitly. His results are mixed. Fonts improve visibly, the glow and dashboard colors look like "AI slop" or unusable, and the artifacts-builder skill gives only small gains on an Apple Notes clone. The video is a single-person, qualitative test with no benchmarks, and a sponsor segment appears at 2:29.

## Key ideas
- **Distributional convergence: models pick the most probable, safest output, which produces the generic 'AI look' in UI.** — The host's reading of Anthropic's article. Models predict next tokens from training-data probability, so the most common landing page or dashboard wins. Steerability means creativity can be injected with the right instructions. ([0:00](https://youtu.be/eLDq5TfIHys?t=0))
- **Skills load specialized UI guidance on demand instead of bloating a system prompt.** — A system prompt full of UI rules would clutter unrelated work. He summarizes Anthropic's split: skills for specialized expertise, sub-agents for specialized tasks in a separate instance with its own tools, MCP for external data access (skills cannot make network requests). Keeping context clean matters because too many tokens degrade performance. ([1:11](https://youtu.be/eLDq5TfIHys?t=71))
- **Write design prompts the way a front-end engineer thinks: map taste to concrete implementation.** — Instead of 'this gradient looks bad', specify the replacement (solid colors or geometric patterns). Anthropic advises targeted, directional language rather than exact hex codes, since the model is more creative when the instruction is about code modification. ([3:28](https://youtu.be/eLDq5TfIHys?t=208))
- **Anthropic's examples work per dimension and then get merged into one large prompt (about 400k tokens, per the host).** — Typography comes first, then themes and aesthetics (an RPG-themed UI example). The combined general-purpose prompt tells the model it converges to generic output, scolds it for 'AI slop', and asks for unexpected choices. Results were mixed: the landing page and blog looked good, but the admin dashboard became overly colorful. ([6:17](https://youtu.be/eLDq5TfIHys?t=377))
- **In the host's Claude Code tests, skills were not invoked automatically; naming the skill in the prompt was needed.** — A skill named 'typography' and then 'frontend aesthetic' was ignored in a plain landing-page prompt until he explicitly asked for the front-end skill. He says the same setup worked in the Claude desktop app, so he treats this as a Claude Code issue. Single-user observation. ([7:37](https://youtu.be/eLDq5TfIHys?t=457))
- **Negative instructions do not pick a font; the model converges on the same fonts again.** — The mega-prompt said which fonts to avoid but not which to use, and two different landing pages came out with the same typefaces. The host concludes that you must choose fonts yourself, for example from Google Fonts. The fonts made the biggest visible difference in his tests. ([9:04](https://youtu.be/eLDq5TfIHys?t=544))
- **The artifacts-builder skill adds componentization and file-system access, but gains over the baseline were small.** — The host disputes Anthropic's claim that artifacts are only single-file vanilla JS, since the baseline already uses React. The skill produced slightly better icons and hover states on the Apple Notes clone, with no major difference otherwise. ([9:04](https://youtu.be/eLDq5TfIHys?t=544))
- **Repeatable design judgments should be turned into skills, and Anthropic released a front-end cookbook and a Claude Code plugin.** — The conclusion treats skills as constant domain guidance. The host says he will test the new front-end design plugin in a future video. ([10:08](https://youtu.be/eLDq5TfIHys?t=608))

## Techniques
- **Turn a design prompt into a project skill** — Ask Claude to make a skill from your design prompt, download the generated skill, place it in the project's skill folder, then start Claude Code. The host did this for a typography prompt and then for a 'frontend aesthetic' prompt. *When:* When you want a reusable design-direction prompt that does not bloat the system prompt for unrelated work.
- **Force-invoke the skill by name** — In the Claude Code prompt, explicitly say to use the front-end skill (for example 'use the frontend aesthetic skill to build the landing page'). Without this, the host's skill did not run. *When:* Until the auto-invocation issue is resolved, whenever a skill must affect the output.
- **Describe design as implementation, not taste** — Translate each design preference into a concrete replacement: 'replace the gradient with solid colors or geometric patterns' rather than 'this gradient looks bad'. Use directional language and avoid exact hex codes. *When:* When writing UI prompts or skill bodies that should steer style without over-constraining the model.
- **Name the fonts explicitly** — Pick the typefaces yourself (the host used Google Fonts) and put them in the prompt. A list of fonts to avoid did not stop convergence to the same typefaces. *When:* Whenever typography must differ between generated pages.
- **Stage the design prompt per dimension, then combine** — Write one prompt per dimension (typography first, then themes/aesthetics), test each on a known page (for example an admin dashboard), and only then merge them into a single general prompt. *When:* When building a reusable front-end design skill and needing to verify each dimension's effect.
- **Artifacts builder skill for componentized output** — Use the artifacts-builder skill to break an app into components and use the file system, rather than a single file. *When:* For multi-component artifact-style apps. The host saw small gains only, so measure against the baseline first.

## Numbers
- Combined general-purpose front-end prompt stated as about 400k tokens (Anthropic's figure, relayed by the host). ([6:17](https://youtu.be/eLDq5TfIHys?t=377))
- Sponsor segment (Scrimba) runs about one minute, from 2:29 to 3:28. ([2:29](https://youtu.be/eLDq5TfIHys?t=149))
- No quantitative benchmarks. Tests are single-run qualitative comparisons: one landing page, one admin dashboard, one blog layout, and one Apple Notes clone. ([4:56](https://youtu.be/eLDq5TfIHys?t=296))

## Hot takes
- Quality capped at 2 because of the sponsored Scrimba segment at 2:29, as the rubric requires. Substance is otherwise moderate.
- The skill-not-invoked finding is one user's observation in Claude Code. The host himself asks whether he is doing something wrong [4:56].
- The 400k-token mega-prompt over-colored the admin dashboard, which the host calls 'unusable' [6:17].
- The host disputes Anthropic's claim that artifacts are single-file vanilla JS, saying the baseline already uses React [9:04].
- Anthropic's advice to avoid fonts gave the same typefaces twice, so the host concludes you should pick fonts yourself [9:04].
- The glow effect in the landing page looks like 'AI slop' even though the fonts and background patterns work well [7:37].

## Tools mentioned
Claude Code, Claude skills, Claude desktop app, Google Fonts, React, shadcn-style UI (as generated by Claude), Zen Browser, Arc Browser, Anthropic front-end design cookbook, Claude Code front-end design plugin

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and manages skills, and the video reports Claude Code silently not invoking a project skill unless it is named explicitly. This is a real failure mode for a harness that depends on skills. → *Add a check in ProsHarness runs that confirms the intended skill actually fired (for example by inspecting the transcript for skill use) instead of trusting that the skill was loaded.*
- **agentos** (1/3): Skills-as-on-demand-context versus sub-agents versus MCP is a clean taxonomy, but the content is front-end-specific and AgentOS is not a UI product. → *Read Anthropic's front-end skills article (referenced in the video) only if we build a skill-loading layer for agent context; otherwise skip.*
