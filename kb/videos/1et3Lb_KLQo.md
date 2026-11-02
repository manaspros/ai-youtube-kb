# I Don't Fear AI Slop. I Fear Untold Stories - Zack Proser, WorkOS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `1et3Lb_KLQo` · [watch](https://youtu.be/1et3Lb_KLQo) · **date:** 2026-11-02 · **length:** 18:34 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Zack Proser · **orgs:** WorkOS, Cloudflare
- **topics:** product-ux, enterprise-adoption · **tags:** internal-tooling, content-factory, human-in-the-loop, asymmetric-leverage, craft, llm-writing, blog-automation, slack-bot, accountability

> WorkOS's Zack Proser argues you should encode your taste into an AI "factory" and hand it to others. Examples: an internal blog-drafting bot and a bedtime-story app. A named human still signs off.

## Summary
Zack Proser, an engineer on WorkOS's applied AI team, argues that people should build "factories" that encode their expertise and taste into an AI tool, then give that tool to others who don't normally produce that kind of work. His main example is BlogBot, an internal system on Cloudflare that a colleague triggers from Slack with a transcript or event notes and gets back an 85-90% draft that needs a human read-through and sign-off. He describes the human role as taste, shaping, and final accountability rather than typing every sentence. He also shows a personal factory: a bedtime-story app built in about four hours for his two toddlers, which turns their photographed day into a narrated story. The talk is mostly opinion and anecdote, with few metrics and no implementation details beyond the high-level architecture. It is useful as a framing for internal tooling and human-in-the-loop publishing rather than as a technical how-to.

## Key ideas
- **The core claim: if you care about someone or a team, build them a 'factory' that encodes your strongly held opinions about an artifact, then hand it over so they can produce that artifact themselves.** — Framed as a 'factory of loving grace.' The speaker's own taste is packed into an automated pipeline, which is then given to colleagues or family. ([0:08](https://youtu.be/1et3Lb_KLQo?t=8))
- **Fear of untold stories matters more than AI slop. Many people hold back their work because they think they are not writers.** — The speaker says he is less worried about slop than about the stories people never share, because of fear and self-concept, and argues the slop problem has known fixes. ([2:51](https://youtu.be/1et3Lb_KLQo?t=171))
- **Asymmetric leverage: a very simple front door (a Slack message) sits on a complex distributed system with data connectors, custom tools, human approval steps for confirming facts, and an image-generation endpoint.** — A colleague posts an event transcript and asks for a recap post. The system pulls context from Granola recordings, images, and Slack, then returns a draft that is 85-90% done. The colleague can tune it in plain language without involving the speaker. ([3:55](https://youtu.be/1et3Lb_KLQo?t=235))
- **The output is a near-final draft, not a one-shot publish. A human must read all of it and take responsibility before it goes out.** — This is the accountability model: the tool reduces assembly work, and the named author is the one who stands behind the claims, links, specs, and performance data. ([6:25](https://youtu.be/1et3Lb_KLQo?t=385))
- **Craft runs through the whole production line. Machines can do the volume, but a person with a long-standing quality bar still inspects and signs off on each unit.** — The speaker uses a manufacturing video (a company mass-producing and inspecting parts) that his WorkOS founder used to describe the approach as craft at speed. ([7:44](https://youtu.be/1et3Lb_KLQo?t=464))
- **Blacksmith framing for the human role: the spark (taste and judgment), the bellows (continuous shaping of the work), and the quench (the publish decision that puts a name on it).** — The speaker says a reader cannot tell the difference between a hand-written post and one that took 14 LLM iterations over 2.5-3 hours plus manual edits, so the accountability is what matters. ([10:23](https://youtu.be/1et3Lb_KLQo?t=623))
- **Evaluation rubric for AI-assisted artifacts: is it true, is it useful, is it beautiful, and does it help anyone else.** — The speaker applies this to anything produced for humans to review, and proposes it as the shared standard for quality. ([12:47](https://youtu.be/1et3Lb_KLQo?t=767))
- **The same pattern works for a tiny audience of two. A bedtime-story app built in four hours turns the day's photos into a story with narration, and kids can request new stories by voice.** — The speaker calls it the fastest successful playtest he has run. The main success signal was repeated requests for 'again'; the average was about three replays per story. Story generation takes about 1.5 minutes. ([14:11](https://youtu.be/1et3Lb_KLQo?t=851))

## Techniques
- **Codify your taste as a fixed pipeline, then expose it behind a simple interface** — Write down the criteria you use to judge the artifact (the speaker's 'what makes a good artifact' list) and encode them as automated steps. Put a front door in a tool people already use daily, such as a Slack message that takes an input like a transcript and returns a draft. *When:* You repeatedly produce the same kind of artifact (recap posts, specs, reports) and others on the team need it but lack your context or skill.
- **Connector-backed context assembly before drafting** — Before generation, pull the context a human would otherwise collect by hand: meeting recordings, event photos, and Slack threads. Add an explicit human approval step for confirming facts, plus a dedicated endpoint for images so the output matches the design team's style. *When:* The source material is scattered across tools and a first draft that already has the context saves most of the assembly work.
- **Draft, iterate in plain language, then human sign-off** — Accept the machine draft at about 85-90% completion. Let the author make changes in plain language, without the factory owner in the loop. Require a named person to read the whole thing, fix the rest by hand, and publish under their own name. *When:* The output is public or will be relied on, and a person is accountable for its claims.
- **Four-question review rubric for AI-assisted output** — For each artifact, check: is it true, is it useful, is it beautiful, and does it help anyone else. Apply it to the final text rather than to how it was produced. *When:* Reviewing drafts from a generation pipeline, or deciding whether AI-assisted work is acceptable to publish.
- **Playtest a factory with a small audience and measure repeat use** — Build the factory for one or two users, watch what they do with it, and treat repeated use (the speaker's kids asking 'again') as the success signal. Feed their requested changes back into the factory. *When:* You want a fast, real-user feedback loop before any broader rollout.

## Numbers
- Original blog post written and published in 23 minutes, before LLMs, from blank page to published markdown. ([1:33](https://youtu.be/1et3Lb_KLQo?t=93))
- BlogBot drafts are about 85-90% complete. The colleague still needs to read, edit, and publish. ([5:18](https://youtu.be/1et3Lb_KLQo?t=318))
- Speaker estimates his LLM-assisted process is about 6x faster, with many more iterations. ([10:23](https://youtu.be/1et3Lb_KLQo?t=623))
- Typical LLM-assisted post took about 14 iterations over 2.5-3 hours plus manual edits. ([11:31](https://youtu.be/1et3Lb_KLQo?t=691))
- Bedtime-story app built to working in about 4 hours using Opus (captioned 'Opus 5-5 extra high'). ([14:11](https://youtu.be/1et3Lb_KLQo?t=851))
- Story generation takes about 1.5 minutes from request to full story. ([15:22](https://youtu.be/1et3Lb_KLQo?t=922))
- Average replay requests ('again') were about 3 per story. ([16:30](https://youtu.be/1et3Lb_KLQo?t=990))

## Hot takes
- AI slop is a smaller risk than untold stories held back by fear and self-concept.
- Accountability belongs to the named person who publishes, not to the tool; readers cannot tell the difference between heavy LLM iteration and hand writing.
- Craft survives automation if a person with a long-standing quality bar inspects every unit.
- Build the factory for the smallest audience that matters, even two people.
- Speaker's own claim that an iterated LLM draft has effectively no difference for the end user is an opinion and is not measured.

## Tools mentioned
BlogBot (internal WorkOS blog-drafting system; name as stated in talk), Cloudflare (hosting for BlogBot), Slack (entry point for colleagues), Granola (meeting recordings as a data source), Claude Opus (captioned as 'Opus 5-5 extra high'; the version string is uncertain from auto-captions)

## Relevance to our work
- **agentos** (1/3): The asymmetric-leverage pattern (simple front door over a multi-connector system with approval gates) is a product framing that touches the opt-in agent platform idea, but the talk gives no architecture or evals to reuse. → *Low priority: note the 'simple front door plus human approval step' framing as product copy or onboarding for AgentOS, with no build change.*
- **prosharness** (1/3): Human sign-off at the end of an automated draft loop parallels ProsHarness's phone-driven approvals, though the talk does not describe an approval mechanism. → *When designing ProsHarness approvals, consider the draft-iterate-then-named-sign-off pattern, where the human takes ownership of the final artifact.*
