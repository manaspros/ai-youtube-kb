# Why is Everyone OBSESSED With The New Kimi K2.5 AI Model

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `KvOYDevFGiw` · [watch](https://youtu.be/KvOYDevFGiw) · **date:** 2026-02-02 · **length:** 13:47 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Moonshot AI, Better Stack, Apple, Anthropic, GitHub
- **topics:** models-research, multi-agent, vibe-coding-app-building, coding-agents · **tags:** kimi-k2.5, moonshot-ai, agent-swarm, parallel-agent-rl, video-to-code, open-weights, kimi-cli, ffmpeg, front-end-generation, deep-research-output-check

> Hands-on review of Moonshot's open-weight Kimi K2.5: video-to-website cloning, a single-image campaign site, and the Agent Swarm feature, with the speaker's verdict that the front-end output is strong but the research output had stale data.

## Summary
Andrus from Better Stack tests Kimi K2.5, Moonshot AI's open-weight model, using its Kimi CLI and API. He first tries cloning an Apple iPad Air product page from a screen recording, which the model handles by compressing the file with FFmpeg and extracting keyframes; the resulting site takes about 5.5 minutes and looks polished, though one carousel's dots don't work. A second test turns a single image of a cartoon character into a satirical campaign site with hidden extras, which takes about 6 minutes and is praised as slick. The third test is the Agent Swarm feature (up to 100 sub-agents and 1,500 tool calls, per Moonshot), run in Kimi's chat UI because the model may skip the swarm unless the prompt asks for it; it takes about 10.5 minutes to produce a PDF. The swarm's report was based on data from January 2025 despite a request for current information, and the speaker says he wasted time and tokens on it. He rates the model as good for visually striking front-end work and fun to use, but not state of the art, and says he does not trust vendor benchmark charts. He also claims Claude Code can reproduce the swarm pattern, citing another video.

## Key ideas
- **Agent Swarm is K2.5's headline feature: a trainable orchestrator splits a task into parallel subtasks, with up to 100 sub-agents and 1,500 tool calls run concurrently; Moonshot claims a 4.5x speedup.** — Training uses Parallel Agent Reinforcement Learning (PARL). The orchestrator is meant to stop the swarm from collapsing into serial execution, and sub-agents get rewards at separate critical steps. The 4.5x figure and the scale numbers are vendor claims that the speaker does not verify. ([1:17](https://youtu.be/KvOYDevFGiw?t=77))
- **The speaker distrusts vendor benchmark charts and skips them, testing only vision/coding and the swarm instead.** — He says the benchmark graphics are inconsistent and the numbers no longer seem trustworthy, so the review is qualitative. ([2:23](https://youtu.be/KvOYDevFGiw?t=143))
- **Video-to-code works on a raw screen recording: the model downsizes an oversized file with FFmpeg on its own and pulls keyframes as visual references.** — The test folder contains only the recording and a prompt asking for a promo site. Shell commands ask for permission first, and the speaker allows them for the session. The Apple-style site (3D floating iPad, mouse-reactive, carousel, animations) is convincing, though one carousel's dots do not respond. ([3:25](https://youtu.be/KvOYDevFGiw?t=205))
- **Creative output from a single reference image plus a short prompt is strong, with the reasoning visible while it works.** — A cartoon character image plus a 'campaign website with policies' prompt yields a multi-section satirical site, hidden easter egg included. Some sections are placeholders such as 'coming soon' and the merch shop, and the site is static HTML. ([5:37](https://youtu.be/KvOYDevFGiw?t=337))
- **Swarm mode must be requested explicitly in the prompt, or the model may decide on its own that it does not need the swarm and refund tokens.** — In one earlier test the model did this, so the speaker now says to name the swarm in the prompt. The chat UI shows per-agent IDs, live task status, the pages each agent visits, and the code it writes. ([9:16](https://youtu.be/KvOYDevFGiw?t=556))
- **Swarm research output was stale: the report used data from January 2025 even though the prompt asked for the currently most used models.** — The report's headline statistics (81% of devs use AI, 46% distrust AI output, 45% of AI-generated code has vulnerabilities, a GitHub Copilot 42% market share) appear in the video without any sourcing, and the speaker never checks them. The model admitted the error after it was pointed out. The output also could not be read directly in the PDF, so the speaker had to copy-paste the text. ([10:35](https://youtu.be/KvOYDevFGiw?t=635))
- **Verdict: K2.5 is a good model for beautiful front-end work and fun to use, but not groundbreaking, and it is weaker than Claude Code models for research accuracy.** — The speaker would pick K2.5 over a Claude Code model for a visually striking website. He says Claude Code can do the same swarm feature and points to another Better Stack video on that topic (not verified here). ([11:48](https://youtu.be/KvOYDevFGiw?t=708))

## Techniques
- **Reference-video to front-end clone** — Create an empty folder that contains only the screen recording of the target site, then prompt the agent to build a promo site from it. Allow shell commands for the session. The agent compresses large files with ffmpeg and extracts keyframes as visual references. The run took about 5.5 minutes for a short recording. *When:* Recreating a reference site's look and animations quickly, as a front-end starting point to refine by hand.
- **Single-image creative brief** — Put one reference image in a folder and give a short prompt describing the product and sections. Expect the model to expand the prompt into a multi-section page and add extras (easter eggs, placeholders) that you should review. *When:* Quick concept sites or visual prototypes from a single asset, where aesthetics matter more than accuracy.
- **Force subagent fan-out by naming it in the prompt** — Say explicitly that the task should use the swarm or subagents. Otherwise the model may decide a single agent is enough and skip the parallel path, wasting the time and tokens the parallel run would have used. *When:* Parallel research or breadth-first gathering tasks where you want the multi-agent path actually used.
- **Check the as-of date of generated research** — Look for an explicit 'based on information as of' line in the output and compare it to the current date. Put the required date range in the prompt, and reject or re-run any report whose source window is older than requested. *When:* Any research or market-data report produced by an agent, especially one that consolidates many sources.

## Numbers
- Agent Swarm: up to 100 sub-agents and 1,500 tool calls run concurrently (Moonshot claim) ([1:17](https://youtu.be/KvOYDevFGiw?t=77))
- Moonshot-claimed 4.5x faster performance from the swarm (not verified by the speaker) ([1:17](https://youtu.be/KvOYDevFGiw?t=77))
- Video-to-website generation (iPad Air page clone) took about 5.5 minutes ([3:25](https://youtu.be/KvOYDevFGiw?t=205))
- Single-image campaign website generation took about 6 minutes ([5:37](https://youtu.be/KvOYDevFGiw?t=337))
- Swarm research task took about 10.5 minutes to finish and deliver a PDF ([9:16](https://youtu.be/KvOYDevFGiw?t=556))
- Generated report stats (unsourced, presented in the video): 81% of devs use or plan to use AI; 59% run three AI tools in parallel; 46% actively distrust AI output; GitHub Copilot 42% market share; Llama 4 Scout 10M-token context; 45% of AI-generated code has vulnerabilities ([10:35](https://youtu.be/KvOYDevFGiw?t=635))
- Report's data window was January 2025 when January 2026 was requested ([11:48](https://youtu.be/KvOYDevFGiw?t=708))

## Hot takes
- The title's 'everyone is obsessed' framing is not borne out by the hands-on tests, which show real strengths but also stale research output.
- Vendor benchmark charts are not trustworthy and should not drive model choice; the speaker chose not to rely on them.
- For visually striking front-end work, K2.5 is preferred over Claude Code models, but not for accuracy-sensitive research.
- Claude Code can reproduce the swarm feature (speaker's claim, deferred to another video, not shown here).

## Tools mentioned
Kimi K2.5, Kimi CLI, FFmpeg, Claude Code, Kimi K2, Llama 4 Scout, GitHub Copilot

## Relevance to our work
- **agentos** (1/3): Kimi K2.5 is an open-weight model with a parallel-subagent design, so it may matter as a model candidate for the InferCraft/serving work. The talk gives no serving, hardware or latency data. → *Add Kimi K2.5 as an open-weight candidate in the model matrix and benchmark it on the RTX 5090 before adopting it. Do not rely on the vendor's 4.5x claim.*
- **prosharness** (1/3): Covers an orchestrator-plus-subagents pattern and the failure mode where the model silently skips parallel work unless told to use it, which matters for a harness wrapping Claude Code. → *In ProsHarness prompts for fan-out steps, state explicitly that subagents must be used, and add a check that they actually ran. Also check report outputs for an as-of date that matches the requested window.*
