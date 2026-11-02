# Guide: product-ux

*Synthesized by Sonnet from 144 talks since 2026-05-18.*

## State of the art

Writing code is no longer the scarce step. Judging, understanding and deciding are. Most of the best talks since May say the same thing in different words: the bottleneck moved to planning, review, delegation and "what is worth building" (`W76woOYHlvY`, `wjk0ulMAkbc`, `n97BCfyFIvw`, `WkBPX-oDMnA`, `6bmM45jkMDY`, `_fHTqOs5wQA`).

What practitioners do now:

- **Design for delegation, not chat.** Pick tasks that take hours and repeat across users. Run them as background agents. Give the user a task list, a trace per value, pause-and-ask, and plan approval (`RGiXcVxSD3s`, `XNtkiQJ49Ps`).
- **Show a plan, get approval, then spend.** This shows up in coding, video editing and generic agent UX (`pPj_tjlvYjA`, `L3RuP_q8Bwc`, `7CrPrHgoEYk`, `W76woOYHlvY`).
- **Return UI from tools (MCP Apps).** A tool returns an HTML resource. The host renders it in a sandboxed iframe. Events go back through the host (`o-zkvb0iFDQ`, `sAOBXCDiDOs`, `_xIwFcnHqp4`, `c-2eEv2ou7Y`, `lbaXnx0KLA8`).
- **Generative UI sits on a three-step control ladder.** Pick a catalog component. Emit a declarative spec validated against a catalog. Or ship open HTML in a sandbox. Most production teams pick the middle (`QrMcNe2jjt8`, `maTp79FD9gI`, `hCMrEfPG2Yg`, `Krzs8GeiWTc`).
- **Agents are a user class.** Docs, APIs, catalogs, sign-up and checkout all need agent-readable forms: llms.txt, markdown twins, WebMCP, auth.md, merchant manifests (`V_5bn4q-vAI`, `ghJmWQCIHRM`, `nSkmXakJ6eo`, `waI44NP1abk`, `A-zeQiYkmXk`, `_B4Pv9ttFgY`).
- **Trust is built in the interaction.** Provenance in one click, fact versus guess labels, visible limits, human sign-off on binding actions (`tJFjeMBKbIY`, `L3RuP_q8Bwc`, `CDqzWpwkSls`, `Emo5FGGY-wM`).
- **Voice: visuals out, not always speech out.** Fast small model for the live turn, async big model behind it. Voice can also trigger actions with no spoken reply (`65X0pQ6Lmbg`, `OpY6MmZFeHo`, `u-rJwPPU3QA`).
- **Taste is packaged as skills.** Teams write anti-pattern lists, brand specs and named commands for design (`v42opQpCy60`, `7GMKdpLsxwU`, `sDMGWK4wZ_w`, `oixzVKMAXG0`).
- **Non-engineers write agents.** They do it through skills, internal-app platforms and self-serve eval tools (`gpmze-6ueGU`, `HTzgC3FoYsI`, `bMjlRrWjdT0`, `UcYoMg-8-L8`).
- **Forward-deployed engineering is the go-to-market motion** for agent products sold to non-technical buyers (`APqXGyCoGW4`, `KwhgfwOSToQ`, `wpOA-UXynoM`).

## Consensus patterns

1. **Make work verifiable, then let agents loop.** Easy-to-check pieces go to the agent. Judgment stays with the human. Use proxies such as golden examples where there is no ground truth (`XNtkiQJ49Ps`, `8KkibGU_DDY`).
2. **Plan up front is cheaper than review.** About five minutes of planning saves about thirty minutes of review. Ask clarifying questions until none are left (`W76woOYHlvY`, `9fubhllmsBU`, `7CrPrHgoEYk`).
3. **Give humans a compressed review surface.** Use evidence bundles, explainer docs with a quiz, diagrams of flows, review kits with screenshots (`n97BCfyFIvw`, `WkBPX-oDMnA`, `6qkzlT962es`, `YIVkERhy8xo`).
4. **Design the human-in-the-loop step against rubber-stamping.** Call model output a "lead", demand independent evidence, split compound yes/no questions, capture the human edit as the label (`CDqzWpwkSls`, `RGiXcVxSD3s`, `Zd5b40Jbp_k`, `Emo5FGGY-wM`).
5. **Show the agent's work.** Live task list, tool calls, plan, stop button, undo, scoped permissions, a visible signal when the agent acts (`7CrPrHgoEYk`, `L3RuP_q8Bwc`, `ghJmWQCIHRM`).
6. **Return summaries, not raw dumps, to agents.** Make errors say the next step. Fewer, workflow-shaped tools beat one tool per endpoint (`_B4Pv9ttFgY`, `jJQoVkd5yLg`).
7. **In an MCP app, the model must see what the user sees.** Return structured data next to the UI. Split search tools from a render tool. Send UI interactions back to the model (`lbaXnx0KLA8`, `sAOBXCDiDOs`). Hide UI-only tools from the model (`LMbeDEQO6QM`, `_xIwFcnHqp4`).
8. **Isolate untrusted generated UI.** Use a double iframe, declared domains and postMessage-only RPC (`c-2eEv2ou7Y`, `RmS5s6Wbin4`).
9. **Deterministic guardrails beat prompt guardrails.** Use allowlists, capped writes, secret brokers, post-generation vetoes, drift checks around generated UI (`iQ5xldZ9StU`, `ij-AU9dpJjc`, `NW-jwOVr32w`, `XNtkiQJ49Ps`).
10. **Evals come from production and users, not imagination.** Use trace classifiers, question banks, golden sets from real use, calibrated judges (`jHMiYtjoJfA`, `DrTdD-ttjCY`, `bMjlRrWjdT0`, `Emo5FGGY-wM`, `McknwOzbmyg`).
11. **Roll out with an autonomy ladder.** Shadow mode, then advisory, then narrow autonomy with kill switches (`AGkzpxMdPn8`, `Yphdry8ttAQ`, `B0fjR3yaZFU`, `DrTdD-ttjCY`).
12. **Hybrid pricing with credits and runtime guards.** Base fee plus usage. Caps, alerts at set percentages, a pre-consumption check (`CrqPcIZOOXA`, `cf2IhzqeQH4`, `T3wRyXg_yVg`).
13. **Domain experts sit inside the loop.** They act as oracle, evaluator or architect, or write skills from narrated real cases (`kfSDc2eVLo4`, `Yphdry8ttAQ`, `gpmze-6ueGU`).
14. **Go to the customer's site.** Watch the real workflow. Ship fixes under a day. Treat a bare FDE motion without shared primitives as a dev shop (`1OMHGsUZiqA`, `KwhgfwOSToQ`, `wpOA-UXynoM`).

## Disagreements & open questions

- **Why understand agent code?** Litt says understanding is for taking part in the next loop, not only for verification (`WkBPX-oDMnA`). Osmani frames the human as owner of the verdict and accountable (`n97BCfyFIvw`). Others want to push review into automation, such as approval-as-code (`AGkzpxMdPn8`). Open: how much understanding is enough once PRs reach tens of thousands of lines.
- **How free should generated UI be?** Open HTML is flexible and needs a sandbox (`hCMrEfPG2Yg`, `c-2eEv2ou7Y`). Catalog or declarative specs are consistent but limited (`QrMcNe2jjt8`, `maTp79FD9gI`). One speaker argues thin HTML wins for video output (`Cz4v1WHVyZc`). Another argues one-version-for-all software is ending in favour of per-user divergence (`bRnoEpoK5m4`).
- **Do agent-readiness files matter?** One team found llms.txt mostly ignored by agents (`waI44NP1abk`). Another reports gains from hand-written llms.txt, markdown twins and docs inside node_modules (`V_5bn4q-vAI`).
- **Is chat dead?** Delegation talks say chat is not enough (`RGiXcVxSD3s`, `XNtkiQJ49Ps`). The voice and durable-session talks keep chat as the front door and fix its plumbing (`YNJvm7t3yq8`, `65X0pQ6Lmbg`).
- **Taste.** Some say taste is the moat (`wjk0ulMAkbc`). Another says broad taste is imitable and only your own point of view lasts (`1KOdiGgMtpY`). A third says rented models and harnesses converge on a median (`0JZy5AuuQzc`). Open: how to measure taste. Probe classifiers for "slop" are one try (`sDMGWK4wZ_w`).
- **Agent safety in consumer products** is unsettled. Sycophancy in relationship advice and persona fidelity both lack agreed evals (`yoONZwV2smc`, `IJXjTLPzvAU`, `YnNF55QV0zs`).
- **Many-agent supervision.** Human attention is the limit. Proposals include attention queues, spatial maps and review kits (`YIVkERhy8xo`, `XWcXwnysmpY`). Nobody has shown which works at scale.

## How thinking changed over time

- **2026-05-18.** Framing is "agents beyond code" and "plan and review". Staff run a business with coding agents (`zepu8Kk6FBQ`). Verifiable work is the trust lever (`XNtkiQJ49Ps`). Alignment between people is the new bottleneck (`ClWD8OEYgp8`). MCP UI is introduced as the answer to text-only tool output (`o-zkvb0iFDQ`).
- **2026-06-18.** Focus moves to the plumbing. MCP Apps get concrete: VS Code demo, double-iframe security, WebMCP for browser agents (`_xIwFcnHqp4`, `c-2eEv2ou7Y`, `ghJmWQCIHRM`, `LMbeDEQO6QM`). Agent-facing interface design appears as its own craft (`_B4Pv9ttFgY`). Enterprise governance is named as the drag on value (`AGkzpxMdPn8`).
- **2026-07-18.** Human judgment is the theme. Discernment over approval, understanding debt, owning the verdict (`CDqzWpwkSls`, `WkBPX-oDMnA`, `n97BCfyFIvw`). "What to build" gets its own genre (`6bmM45jkMDY`, `d_Ftrl3vfV0`). Model-side advice shifts to smaller prompts and tool access (`9fubhllmsBU`).
- **2026-08-18.** Production patterns arrive. Typed rendering contracts and BFFs (`maTp79FD9gI`). Shipping measures: PR previews, trace stores (`ON5LIT0M4do`). Trust plumbing for finance memos (`tJFjeMBKbIY`). Memory is called a product problem, not a RAG problem (`5ZGyKWjQDr0`). FDE becomes a named discipline across three talks (`KwhgfwOSToQ`, `wpOA-UXynoM`, `1OMHGsUZiqA`).
- **2026-09-18.** Large batch on agentic commerce, voice, generative UI and design taste (`G7cgLjZtmMU`, `A-zeQiYkmXk`, `OpY6MmZFeHo`, `Krzs8GeiWTc`, `7GMKdpLsxwU`). Measurement turns practical: act/confirm/stop thresholds, outcome-tied token accounting, hazard-first safety cases (`Zd5b40Jbp_k`, `8KkibGU_DDY`, `McknwOzbmyg`).
- **2026-10.** Agents as a customer class: sign-up, identity, pricing runtime (`nSkmXakJ6eo`, `mBNVKkyfnE0`, `cf2IhzqeQH4`). Sloppy one-shot output gets named and fought with conventions and polish skills (`6qkzlT962es`, `oixzVKMAXG0`). Reliability is perceived as a cliff, not a slope (`Emo5FGGY-wM`). Lead-agent subagent teams appear in product UIs (`buHC7bQE1X4`).

## Numbers worth remembering

- 5 minutes of planning saves about 30 minutes of review (`W76woOYHlvY`). Humans stop watching agents past about 5 minutes, same talk.
- Reviewers with over 90% calibration accepted about half of planted false AI flags. A guideline change raised rejections 21% (`CDqzWpwkSls`).
- Customers treat 80% reliability as needing ongoing monitoring and about 92% as trustworthy enough to hand a workflow to (`Emo5FGGY-wM`, speaker's claim).
- Act/confirm/stop: cost per turn fell from 2.1 (always act) to about 1.9 (guessed 65% threshold) to about 1.27 (optimized) at fixed 79% accuracy (`Zd5b40Jbp_k`).
- Raw performance trace of about 50,000 lines of JSON overflowed agent context (`_B4Pv9ttFgY`). Slim mode is about three tools.
- Python UI representation is about 70% smaller than JSON when streaming (`Krzs8GeiWTc`).
- Same query phrased four ways gave four layouts in generative UI (`QrMcNe2jjt8`).
- Page generation about 1.1 s on a fast host versus 4.6 s elsewhere, over 15 prompts (`jebp4V0vh30`).
- Voice latency: about 100 ms feels instant, about 1000 ms loses the thread, about 200 ms or less for voice-to-voice (`65X0pQ6Lmbg`).
- Agent run: 93 subagents, 12 hours, about 2 billion tokens, under $1,000 (`buHC7bQE1X4`, speaker's figures).
- 5-10% of users can use about 80% of compute. Alerts at 50/70/90% of allowance (`CrqPcIZOOXA`).
- About 5% of enterprise demo calls end in a contract. Pilot windows shrank from six months to two weeks (`7A65O-0lvKE`).
- About 10% of Linear bugs land via a single-shot agent PR (`wjk0ulMAkbc`).
- 37% of about 60 internal apps had no engineer commits (`HTzgC3FoYsI`).
- 58% cost cut and a third of the time with an accessibility skill, a one-off run (`ZccJsdOE54M`).
- Pure LLM UI generation starts near 30% design fidelity (`NW-jwOVr32w`).
- About 40% of agents used llms.txt only when docs pointed to it (`waI44NP1abk`).
- Memory profile of about 4,000 tokens, re-synthesised every few days (ChatGPT) or daily (Claude) (`5ZGyKWjQDr0`).
- 17 of 21 agent-hackathon ideas were dropped (`6bmM45jkMDY`).
- A two-week build took about 12 months to reach production at a large enterprise (`AGkzpxMdPn8`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Most of this comes from AI LABS tutorials and reviews. Better Stack adds reviews and podcasts. Kai Explains adds one opinion essay. Most creator claims rest on one video or one founder's anecdote. Sponsored segments and paid-community pitches are flagged where they matter.

### Practical playbook

1. **Write actors and constraints before any PRD.** List each actor as a person with a goal. Note where actors hit the same URL and see different views. Write limits on what the agent may not do or spend. Leave the stack out. (`X4vAlWtsJD4`, about 2:32. Single creator. The prompt text was on screen only.)
2. **Turn the PRD into architecture.md, then a persisted task list.** architecture.md holds pages, modals and per-actor flows. The agent builds its task list from that file. Build a clickable mock-data prototype before any backend, and use an MCP for the database instead of pasted SQL. (`X4vAlWtsJD4`, about 3:49. The backend step, about 8:01, was sponsored.)
3. **Shadow the repetitive job for about an hour.** Write every step in the order it happens. Ask why each step exists. Treat "we've always done it" as a workaround to check, since an unwritten check can be the real policy. (`AD-EmZ3v6-g`, about 1:24. Single creator.)
4. **Triage each step with three filters.** A fixed rule that must always hold becomes ordinary code. Messy input that needs judgment goes to a model. An expensive failure keeps a human, even where a model could do the step. Record the verdict per step. (`AD-EmZ3v6-g`, about 8:31. Moza's eight-step example ended with four automated, three reviewed and one human.)
5. **Eval on labelled real cases.** Run the full set, count correct outcomes, read every miss, fix the cause and rerun. Do not trust a few runs, because outputs vary. (`AD-EmZ3v6-g`, about 9:55.)
6. **Keep the old steps visible and budget for trust.** Moza, quoted in the video, says collapsing an 11-step process into one step made people stop trusting it. Show intermediate results inside each step. (`AD-EmZ3v6-g`, about 7:04. One anecdote from a bank project.)
7. **Keep the design in the repo as a file.** Pencil saves the canvas as a `.pen` JSON file that Git can track. It connects to Claude Code over MCP. Sync was not automatic, so the creator wrote a file watcher. The watcher runs the Claude CLI with a fixed sync prompt on each save, with a cooldown. The script sits in a paid community. (`sdxJEd7nqiQ`, about 1:13 and 2:37.)
8. **Pre-approve permissions before any unattended run.** Add read, write and MCP tool permissions to the project's `.claude/settings.json`. Otherwise a headless run waits forever on a permission prompt. The creator names the file but shows no keys. (`sdxJEd7nqiQ`, about 4:04.)
9. **Split multi-page work across subagents.** Keep the PRD and UI guide in the repo. Ask for one agent per page. Each agent reads the shared docs and the design. (`sdxJEd7nqiQ`, about 5:21. Five pages in one run, with no measurement.)
10. **Run a scored UX audit before calling a UI done.** Build a skill with Skill Creator. It checks a nine-point checklist and ranks issues as critical, major or minor. It gives a letter grade. Fix the critical items, then rerun. The demo moved one site from C to B. The WCAG claim is not measured. (`sdxJEd7nqiQ`, about 8:58.)
11. **Put base rules in a CLAUDE.md at the parent folder.** Claude Code reads CLAUDE.md from the project and from its parent folders. The creator puts four rules there. Ask when a request is ambiguous. Use the simplest working solution. Touch only the requested scope and report other issues. State the check first and loop until it passes. (`jyLKRN36-Dc`, about 7:07. Single creator.)
12. **Log candidate skill lessons, then review them.** A task-observer skill writes lessons to a log outside the project. A person reviews each one before it changes the skill. One bad run should not become a permanent rule. (`jyLKRN36-Dc`, about 0:46 and 2:14.)
13. **Cut onboarding friction and design the cancel flow.** Ask only for what account creation needs. Prefill known fields. Preselect the popular plan. On cancel, ask for the reason, offer a matched alternative, and make pause the main button. (`jyLKRN36-Dc`, about 3:41 and 5:58. No conversion or churn numbers are shown.)
14. **Validate demand before building.** Name 10 real people with the problem. Get at least 3 to say they would pay. (`jyLKRN36-Dc`, about 12:17. Based on one founder's playbook.)
15. **Prompt in small chunks.** Use one feature per prompt, under about three sentences, with only the context the task needs. Switch model if one fails the task. (`zNOunnM1jTs`, about 3:50 and 9:03. Founder anecdotes, not measured.)

### Tools creators recommend

- Pencil.dev — design canvas stored as JSON in Git, read by Claude Code over MCP — `sdxJEd7nqiQ`
- Skill Creator — builds project skills such as the UX audit — `sdxJEd7nqiQ`
- Supabase MCP — creates schema and migrations from PRD and spec files — `X4vAlWtsJD4`
- Anthropic frontend-design skill — better UI before implementation — `X4vAlWtsJD4`
- Context7 MCP — pulls current framework docs before a port or fix — `i_31WoayEIo`
- GSAP and Lenis — scroll animation and smooth scroll layered together — `sdxJEd7nqiQ`
- OpenCLI — site commands on a logged-in Chrome session, for personal use only — `jyLKRN36-Dc`
- Variate skill — generates variants of one page section — `jyLKRN36-Dc`
- Warp Oz — cloud agent for a self-contained backend task (sponsored segment) — `X4vAlWtsJD4`

### Where creators agree or clash with the conference talks

- **Agree: plan before building.** Actor and PRD files (`X4vAlWtsJD4`) and process audits (`AD-EmZ3v6-g`) back the conference rule that planning is cheaper than review.
- **Agree: triage by error cost.** Keeping humans on expensive failures matches the conference advice on human sign-off for binding actions.
- **Agree: review skill lessons before promotion.** The log-then-review pattern (`jyLKRN36-Dc`) matches the conference advice to capture skills from corrections and gate them.
- **Agree: taste is packaged as skills.** Design skills that name common AI defaults and force one direction (`Ot582-E61ac`, `Ysr7oNDajJI`) match the conference view.
- **Agree on agent docs, weakly.** The Tailwind commentary's host says, without verifying it, that he has heard major providers do not use llms.txt (`YIRugFtqBsM`). The conference section above reports mixed results too. Single opinion piece.
- **Clash: speed versus governance.** Creators show solo builds and fast prototypes (`zNOunnM1jTs`, `X4vAlWtsJD4`). The conference talks stress enterprise governance and how much review is enough. Creators skip that side.
- **Clash: parallel subagents.** One-agent-per-page is shown as a time saver (`sdxJEd7nqiQ`). The conference section above says nobody has shown which many-agent supervision works at scale. The creator evidence is one run.
- **Gap: growth and pricing.** Paywalls, onboarding and cancel flows (`jyLKRN36-Dc`) have no counterpart in the conference talks. Treat them as untested.
- **Agree on trust.** Overselling, and treating lived experience as non-evidence, cost trust, according to one essay (`xu-i-Zeu46s`). That matches the conference point that trust is built in the interaction. Opinion, not a technical talk.

### Watch first

- `X4vAlWtsJD4` — actors, constraints, PRD and architecture.md in order. Sponsored tail; prompts not shown.
- `AD-EmZ3v6-g` — three-filter triage and labelled-case eval loop. Sponsored segment; most stats unsourced.
- `sdxJEd7nqiQ` — file-watch sync, pre-approved permissions, per-page subagents and the audit loop in one build. The key code is paywalled.
- `jyLKRN36-Dc` — layered CLAUDE.md and the reviewed-lesson log. Promotional tone; no measured gains.
- `zNOunnM1jTs` — the same habits told as founder anecdotes. Read it for the pattern, not the numbers.

## Watch first

- `W76woOYHlvY` — plan-versus-review rule by task type, with the five-minutes-saves-thirty rule.
- `CDqzWpwkSls` — the cleanest evidence that HITL fails through interaction design, plus label hygiene.
- `WkBPX-oDMnA` — explainer docs, quiz gate, micro-worlds for staying in the loop.
- `_B4Pv9ttFgY` — how to build interfaces for agents: summaries, errors, tokens per successful outcome.
- `lbaXnx0KLA8` — the most practical MCP Apps rules (data parity, explore/render split).
- `QrMcNe2jjt8` — generative UI in production: orchestrator, catalog as contract, placement.
- `RGiXcVxSD3s` — delegation-first product design with traces, pause-and-tag, skill capture.
- `Zd5b40Jbp_k` — a quantified method for when an agent should act, ask or stop.

## Implications for our projects

**AgentOS**

- **Gateway as the control point for approval and spend.** Put act/confirm/stop gating in Govrix Scout. Pick thresholds by minimizing a user-cost function, not by gut (`Zd5b40Jbp_k`). Add a synchronous pre-call budget check with hold-and-settle for concurrency (`cf2IhzqeQH4`). Add 50/70/90% alerts and rate limits against runaway loops (`CrqPcIZOOXA`).
- **Deterministic guardrails over prompts.** Declare tool allowlists, write caps and domain allowlists in the manifest. Keep secrets in a broker the agent never touches (`iQ5xldZ9StU`, `XNtkiQJ49Ps`). Put a rule-based veto after generation (`ij-AU9dpJjc`).
- **Crucible and generated UI.** If sandboxed output ever renders as UI, use the double-iframe, declared-domain and postMessage-only pattern (`c-2eEv2ou7Y`, `RmS5s6Wbin4`). Run the harness apart from generated code (`XKup1pj-34M`).
- **MemoryMesh.** Consumer memory moved to a running profile plus search tools over past chats, re-synthesised in the background (`5ZGyKWjQDr0`). Test a profile tier above the pgvector tiers. Precompute meaning offline and recompute a thin slice at serve time (`Btk8wDUVs74`). Show provenance and let the user edit it (`5ZGyKWjQDr0`, `tJFjeMBKbIY`).
- **SkillForge success signal.** Use the human diff between agent draft and final output as an implicit label (`B0fjR3yaZFU`, `CDqzWpwkSls`). Capture skills from repeated user corrections (`RGiXcVxSD3s`, `EEt3ZSG4a1s`). Tie token spend to completed outcomes to score skill value (`8KkibGU_DDY`). Skills that encode taste, with ask-first and never-do sections, are what non-engineers actually wrote (`gpmze-6ueGU`).
- **Evals and benchmarks.** Seed evals from real questions and traces (`DrTdD-ttjCY`, `jHMiYtjoJfA`). Calibrate judges against expert labels and report sensitivity (`McknwOzbmyg`). Refresh weekly (`Emo5FGGY-wM`). This fits the "benchmarks and correctness, not demos" thesis.
- **InferCraft latency.** The voice talks give concrete budgets and tricks: stable prompt prefix for caching, eager short inference, fast model plus async thinker (`65X0pQ6Lmbg`). Priority classes map onto foreground over background calls on a shared model (`owH1f0N-keY`).


- **Registry entries should be agent-readable.** Use a per-domain catalog file, a queryable directory, a skill.md-style sign-up, and tool descriptions tuned from agent traces (`waI44NP1abk`, `nSkmXakJ6eo`, `mBNVKkyfnE0`, `Lrw0jqBNaw0`). Measure agent paths, not checklists (`waI44NP1abk`).
- **Tool quality.** Fewer workflow-shaped tools, error codes with next steps, snapshot tools (`jJQoVkd5yLg`, `_B4Pv9ttFgY`). Track tokens per successful outcome inside one journey (`_B4Pv9ttFgY`).
- **Admin control plane.** Enterprise buyers want an admin API, audit trail, group-gated features and zero data retention verified in practice (`7A65O-0lvKE`). Attribution by team, user, agent and model is a stated buyer need (`cf2IhzqeQH4`).

**ProsHarness**

- **Phone approvals and plan gates.** Show the plan, wait for approval, offer always-allow for repeat flows (`L3RuP_q8Bwc`, `pPj_tjlvYjA`). Keep an attention queue with jump-to-next for agents blocked on a question (`YIVkERhy8xo`).
- **Checkpoints for long runs.** Treat day-long runs as work streams with checkpoints and escalation, and cap delegation depth (`n97BCfyFIvw`). Use heartbeat re-invocation for always-on loops (`EEt3ZSG4a1s`).
- **Plan then critique.** Let the model interview you until it has no questions and run a blind-spot pass before a task (`W76woOYHlvY`, `9fubhllmsBU`). A verifier agent beside the worker fits the Codex-critique step (`8KkibGU_DDY`).
- **Review kit.** Return evidence bundles, not only diffs: tests, logs, screenshots (`n97BCfyFIvw`, `YIVkERhy8xo`). A comprehension quiz before sharing code is a cheap gate (`WkBPX-oDMnA`).
- **Subagent teams.** One subagent per hypothesis, with a lead that asks clarifying questions first (`buHC7bQE1X4`).

**Recurring interests**

- **Entity resolution and data quality.** Per-field source precedence, with owner validation, is a ready pattern for conflicting sources (`BOWYujhIQuo`). Surface contradictions to a human and show both values (`tJFjeMBKbIY`). Use human edits as labels with split detection and decision questions (`CDqzWpwkSls`).
- **Cheap-model (Haiku) pipelines.** Small model for the live turn and layout choices, big model async (`65X0pQ6Lmbg`, `jebp4V0vh30`). Use a cheaper model for many revision rounds (`7GMKdpLsxwU`). Cache the expensive teacher outputs and reuse them across experiments (`phchDt63qAA`).
- **Context engineering.** Newer models want smaller prompts and tools to build their own context (`9fubhllmsBU`). Layer prompts in a single assembly function, with immutable rules first (`ij-AU9dpJjc`).
