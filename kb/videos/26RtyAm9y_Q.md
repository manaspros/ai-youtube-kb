# The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans — Corey Gallon, Rexmore

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `26RtyAm9y_Q` · [watch](https://youtu.be/26RtyAm9y_Q) · **date:** 2026-08-18 · **length:** 21:38 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Corey Gallon · **orgs:** Rexmore, Arise AI, Anthropic, OpenAI, Cloudflare, Google
- **topics:** voice-multimodal, mcp-and-tools, agent-architecture, security-guardrails · **tags:** browser-automation, chrome-devtools-protocol, captcha, cli-vs-mcp, trusted-input, sense-act-verify, human-like-input, explore-then-codify

> Corey Gallon on driving websites with agents via a shell CLI over the Chrome DevTools Protocol, climbing from synthetic clicks to trusted input to human-like motion, and beating Cloudflare Turnstile, MT Capture, Lemin and reCAPTCHA v2.

## Summary
The speaker argues that an agent driving Chrome over the Chrome DevTools Protocol looks like a human to the page, since its input goes through the same browser path as a real mouse and keyboard. He recommends a shell CLI over an MCP server because, on his cited study, both reach about 83% task success while the CLI is cheaper, faster and reusable as a program. His method is a sense-act-verify loop that checks each action through a different channel, and an escalation ladder: synthetic JavaScript click, then trusted CDP input, then human-like motion and vision, climbing only as far as the page forces. He shows that untrusted JavaScript clicks are silently ignored on a shopping site while trusted CDP clicks go through. For Cloudflare Turnstile he finds the iframe's screen position and fires a trusted click at computed coordinates. For reCAPTCHA v2 he splits the work into a deterministic solver loop and an operator call where the model only classifies the grid tiles, which keeps rounds fast before they expire. He closes by saying the durable pattern is to explore by hand, then write the working path down as code or a skill. Speed and cost figures are his own citations and were not verified here.

## Key ideas
- **Premise: a CDP-driven browser's clicks and keystrokes take the same path inside Chrome as a human's, so pages cannot tell them apart by default.** — The speaker's framing is that the agent is a 'meat bag with a mouse' from the page's point of view. The rest of the talk covers how to pull that off. ([1:17](https://youtu.be/26RtyAm9y_Q?t=77))
- **Use a shell CLI, not an MCP server, for browser agents. Capability is about equal; the CLI wins on reuse, speed and cost.** — He cites an Arise AI study where both reach about 83% success. A CLI sequence can be written once and replayed with no model in the loop, while MCP calls the model every turn. ([2:19](https://youtu.be/26RtyAm9y_Q?t=139))
- **Think of CDP as a set of sensors and actuators. You need only a small subset of its 57 domains.** — Sensors: DOM, accessibility tree, screenshots, and network or console logs. Actuators: clicks, keystrokes and navigation. He groups the domains into eight buckets for memory. ([4:37](https://youtu.be/26RtyAm9y_Q?t=277))
- **Run a sense-act-verify loop, and verify through a different channel than the one you used to act.** — After a click, do not ask the click whether it worked. Check the network or the screen. If the loop will not close, that is the page pushing back. ([4:37](https://youtu.be/26RtyAm9y_Q?t=277))
- **Climb an escalation ladder and stop at the lowest rung that works: synthetic JS click, then trusted CDP input, then human-like motion and vision.** — Rung one is free and instant and is the default. Rung two is needed when the page ignores untrusted events. Rung three adds a real mouse path with dwell and jitter, or vision, and is needed for the hardest bot checks. ([6:05](https://youtu.be/26RtyAm9y_Q?t=365))
- **Pages can drop untrusted events silently. Chrome stamps each event as trusted or untrusted, and a shop page ignored the JS click with no error.** — Switching to CDP's input domain produced trusted events that the page accepted, and items went into the cart. The failure was silent, so you need to watch the page's behaviour to notice it. ([11:21](https://youtu.be/26RtyAm9y_Q?t=681))
- **Split the work into a deterministic solver and a model 'operator'. The model only handles the step that needs eyes.** — For reCAPTCHA v2, code does the trusted clicks, the iframe piercing, screenshots and rearming on expiry. The model is called once per round to name the tiles. Speed matters because each challenge round has a clock. ([17:42](https://youtu.be/26RtyAm9y_Q?t=1062))
- **Explore by hand, then write down the path that worked as code or an agent skill, so it runs again without rediscovery.** — The loop is run manually and the rungs are climbed until it works. Then the sequence is captured as a replayable program or skill. He says this is what makes the approach durable. ([7:25](https://youtu.be/26RtyAm9y_Q?t=445))

## Techniques
- **CLI over MCP for repeatable browser tasks** — Expose the browser driver as shell tools, record a working sequence once, then loop it over many inputs without a model in each step. He uses this for batches such as sending 20 or 200 personalised emails. *When:* Use it for high-volume or repeated UI tasks where replay speed and token cost matter more than per-step model judgement.
- **Cross-channel verification after each action** — After a click or keystroke, check the network traffic, the DOM or a screenshot. Do not trust the action's own return value. *When:* Use it in any UI automation loop, so each step is confirmed before the next one.
- **Lowest-rung escalation** — Try a synthetic JavaScript click first. Move to CDP Input trusted clicks only when the page ignores untrusted events. Use human-like motion and vision only when trusted input still fails. *When:* Use it on any site with bot defences, so you pay the cost of stealth only where the page forces it.
- **Coordinate-based trusted click through closed shadow roots and cross-origin iframes** — Ask the browser for the iframe's on-screen position, add the widget's offset from it, then fire a trusted click at that screen point. This avoids the blocked element tree. *When:* Use it when the target control sits inside a closed shadow root in a cross-origin iframe and cannot be selected.
- **Solver plus operator split** — Keep the mechanical loop in deterministic code and send only the perception step to the model, which returns an answer that code then submits. The loop waits for the next round. *When:* Use it for time-limited challenges or any flow where a model round trip per action would miss the deadline.
- **Explore, then codify** — Run the sense-act-verify loop by hand, climb rungs until the task works, then save the verified sequence as code or as an agent skill. *When:* Use it when you are teaching an agent a new web flow that you expect to run more than once.

## Numbers
- CLI and MCP reach about the same task success rate, roughly 83% each, in an Arise AI study the speaker cites. ([2:19](https://youtu.be/26RtyAm9y_Q?t=139))
- On the same task in that study, MCP took 71 round trips and about 8 minutes; the CLI took 7 turns and under 1 minute. ([2:19](https://youtu.be/26RtyAm9y_Q?t=139))
- The speaker says Anthropic reported that a CLI can be up to 75 times cheaper in token cost than MCP. ([3:45](https://youtu.be/26RtyAm9y_Q?t=225))
- CDP has 57 domains with hundreds of methods and events, which the speaker groups into eight buckets. ([4:37](https://youtu.be/26RtyAm9y_Q?t=277))

## Hot takes
- For repeated tasks a shell CLI beats MCP on reuse, speed and cost, and the capability difference is negligible.
- The web UI can act as a permissionless API when the official API needs an app registration and admin approval the employee cannot get.
- Synthetic JavaScript clicks are silently dropped on bot-hostile pages, and trusted CDP input is what gets through.

## Tools mentioned
Chrome DevTools Protocol (CDP), Chrome Agent (speaker's Python CLI), Cloudflare Turnstile, MT Capture, Lemin (auto-captioned as 'lemon'), reCAPTCHA v2, Outlook web client

## Relevance to our work
- **agentos** (1/3): The CLI-over-MCP argument bears on how AgentOS should expose tools to agents. The speaker's cost and speed figures are unverified, so this is a prompt to test, not evidence. → *Measure a CLI-wrapped tool against its MCP version on one repeated AgentOS task, counting turns, wall time and tokens, before choosing how Crucible-style tools are exposed.*
- **prosharness** (1/3): The talk's explore-then-codify advice (save a verified path as code or a skill) matches ProsHarness's skill ranking and checkpoint/resume. The talk does not cover Claude Code CLI runs. → *When a long ProsHarness run succeeds, save its verified step sequence as a replayable skill candidate for the skill ranker to score.*
