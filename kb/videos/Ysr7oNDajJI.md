# Insane Claude Design Skills You Need To Actually Build Beautiful Sites

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `Ysr7oNDajJI` · [watch](https://youtu.be/Ysr7oNDajJI) · **date:** 2026-09-02 · **length:** 12:55 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS presenter (unnamed) · **orgs:** AI LABS, Make
- **topics:** skills-self-improvement, product-ux, claude-code · **tags:** claude-design, agent-skills, frontend-design, web-design, animation, landing-pages, design-review, design-tokens, ux-laws, sponsor

> AI LABS walks through design-focused agent skill packs (Emil Kowalski, Conard Lee, Elia Design, Meng To, Jakub Krehel, Tastemaker, perception laws) for Claude Design and says they steer models away from generic layouts. Mostly an overview; little measured evidence.

## Summary
The presenter argues that models default to a recognizable design pattern and that installable skills can steer them away from it. They tour a set of design skill packs from different creators, mainly to be added in Claude's settings and invoked with a slash command inside Claude Design. Emil Kowalski's nine-skill set is the one they use most, with a design-engineering skill for starting a design and an Animate skill for refining motion on an existing site. Conard Lee's pack adds a web design engineer skill that scores an existing design, and Elia Design's single-file skill targets landing pages around one call to action. Jakub Krehel's split-by-area skills include a review skill that can compare against GitHub history to flag regressions. Tastemaker extracts design details from reference images with scripts instead of text summaries. The video gives no benchmarks or before/after measurements, relies on subjective "looks better" judgments, includes a sponsored Make segment, and says the skills should also work in Claude Code and Codex without demonstrating it.

## Key ideas
- **Models follow a recognizable default design pattern, so a skill is used to steer them off it and make a site stand out.** — The presenter's premise is that even strong models produce similar-looking sites, and that the pattern is easy to spot. ([0:00](https://youtu.be/Ysr7oNDajJI?t=0))
- **Skills added in the Claude settings are available inside Claude Design, and the presenter says the same skills work in Claude Code, Codex, or other agents.** — Stated as a claim; the video does not demonstrate the non-Claude-Design case. ([0:00](https://youtu.be/Ysr7oNDajJI?t=0))
- **Emil Kowalski's set is nine skills. The design-engineering skill is used to start a design, and the Animate skill refines motion on an already-built site.** — The first build was minimal and monotone with out-of-sync animations; Animate improved scroll-synced motion and added small interaction animations such as form-submit feedback and hover effects. ([1:09](https://youtu.be/Ysr7oNDajJI?t=69))
- **Conard Lee's web design engineer skill works through requirements, looks for reference designs, and can score an existing design so you can iterate toward a target score.** — References cover judging design, common failure modes, and style recipes for sites such as Apple and Linear. ([3:48](https://youtu.be/Ysr7oNDajJI?t=228))
- **Elia Design's single-file landing-page skill builds a visual system (colors, type, spacing) and structures the whole page around one action the visitor should take.** — It also addresses search discoverability, which the presenter says models often overlook. ([5:16](https://youtu.be/Ysr7oNDajJI?t=316))
- **Meng To's awards-quality skill encodes the principles and specific effects of award-winning sites, steering output toward scroll-based storytelling.** — A companion skill turns a screen recording or walkthrough into a prompt using local tools. ([7:26](https://youtu.be/Ysr7oNDajJI?t=446))
- **Jakub Krehel's pack splits design concerns into separate skills. The review skill is more useful when connected to GitHub, since it can flag what regressed after a change.** — A better-layout skill caught a date that needed more room and reported how many extra pixels it needed. ([8:54](https://youtu.be/Ysr7oNDajJI?t=534))
- **Tastemaker avoids lossy text summaries of reference images by extracting exact design details with scripts into a structured format that agents reuse across the project.** — It also tries variations in different directions to avoid generic defaults. ([10:22](https://youtu.be/Ysr7oNDajJI?t=622))
- **The perception-law skills are grounded in named UX/psychology laws, with one skill per law. The presenter installed a screen critique skill and a perception-laws skill.** — The screen critique flags issues such as what stands out first, type, and spacing. The presenter says you do not need to install a whole pack, only the skills that fit your workflow. ([10:22](https://youtu.be/Ysr7oNDajJI?t=622))

## Techniques
- **Install and invoke a design skill in Claude Design** — Add the skill from Claude's settings, then type / and the skill name in Claude Design with a prompt describing the site. The skill asks clarifying questions before building. *When:* Starting a new site where you want a designed result rather than a default one.
- **Layer skills by stage** — Use a starting-design skill first (e.g. Emil's design-engineering skill), then a motion-refinement skill (Animate) on the built site. *When:* When the first build looks minimal or its animations are out of sync.
- **Score-and-iterate loop** — Run a scoring or review skill on the existing design, fix the flagged items, and re-run until the score matches the target. *When:* Refining a design with objective-ish checkpoints instead of eyeballing it.
- **Regression-aware review via GitHub** — Connect the review skill to the GitHub repo so it compares the design before and after your changes and flags what regressed and which change caused it. *When:* Iterating on a site with frequent edits where a previous fix may silently break.
- **Script-based reference extraction** — Instead of having the model summarize a reference image in text, run scripts to pull exact design details (colors, spacing, type) into a structured file the agent reads later. *When:* You need a style to carry consistently across many screens without losing details in summarization.
- **Landing-page as one-action structure** — Organize the whole page around a single desired visitor action and derive colors, type, and spacing from that structure. *When:* Building a conversion-focused landing page rather than a general home page.
- **Install only the skills that fit your workflow** — Pick individual skills from a pack (e.g. screen critique and perception laws) rather than installing the whole collection. *When:* You want targeted review without bloating the agent's context with unused skills.

## Numbers
- Emil Kowalski's set contains nine skills; two (design engineering and Animate) are the ones the presenter uses most. ([1:09](https://youtu.be/Ysr7oNDajJI?t=69))
- Conard Lee's set contains five skills; the web design engineer skill is the main one. ([3:48](https://youtu.be/Ysr7oNDajJI?t=228))
- Jakub Krehel's review skill and better-layout skill were used; the layout skill reported a specific extra pixel requirement for a date element, but the value is not stated in the transcript. ([8:54](https://youtu.be/Ysr7oNDajJI?t=534))
- Sponsored Make segment runs roughly 6:21 to 7:26. ([6:21](https://youtu.be/Ysr7oNDajJI?t=381))

## Hot takes
- Skills steer models away from a recognizable default design pattern, and the same skills should give the same results in Claude Code and Codex as in Claude Design (claimed, not demonstrated).
- Most of the evidence is subjective ('looks more intentional', 'feels more refined'); no benchmarks, A/B comparisons, or token costs are shown.
- Sponsored segment (Make / Maya) caps the quality score; the upsell to a paid AI Labs Pro community for the presenter's own skills is also an extra pitch.

## Tools mentioned
Claude Design, Claude Code, Codex, GitHub, Emil Kowalski design skills (design-engineering skill, Animate, Apple Design, animation vocabulary), Conard Lee garden skills (web design engineer skill), Elia Design landing-page skill, Meng To skills (video-to-prompt, awards-quality sites), Jakub Krehel skills (review, better layout), Tastemaker, screen critique skill, perception laws skill, Make / Maya (sponsor)

## Relevance to our work
- **prosharness** (1/3): ProsHarness has a skill-ranking component, and this video is a catalogue of third-party skill packs with no measured quality or token data. → *If we evaluate third-party skill packs for ProsHarness, measure them with skillrank-style token/success evals rather than adopting them on visual impressions.*
