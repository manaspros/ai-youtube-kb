# This Tool Codes for FREE – Here’s How to Install It!

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `xsJAA3vhy0E` · [watch](https://youtu.be/xsJAA3vhy0E) · **date:** 2025-11-02 · **length:** 9:34 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** DeepSeek, OpenRouter, Anthropic, Google, Perplexity AI, Hugging Face, StackBlitz (Bolt.new, not named in transcript; omit if unverified)
- **topics:** vibe-coding-app-building, coding-agents, dev-tools · **tags:** bolt-diy, bolt-new, deepseek-v3, openrouter, shadcn-ui, self-hosted, pnpm, model-provider-config, whiteboard-demo

> Install-and-try walkthrough of Bolt DIY, a self-hosted, free alternative to Bolt.new, driven by DeepSeek V3 through OpenRouter. The demo works for a whiteboard app, but shapes stay broken, and the title overstates what is free.

## Summary
The creator introduces Bolt DIY, the renamed open-source fork of Bolt.new, and runs it with DeepSeek V3 through OpenRouter. He first generates a ShadCN UI landing page, which looks good and supports light and dark mode. He then walks through cloning the repo, running pnpm install and pnpm run dev, and listing the new features (repo import, file and chat import, prompt library, auto-install and preview, error autofix, starter templates, Perplexity integration). Model and API key setup is covered next, including the mistake of selecting the DeepSeek provider directly instead of OpenRouter, which caused an API error. The whiteboard test shows pen, color and thickness working, text and shapes broken at first, an eraser added after a follow-up prompt, and rectangle and circle still not working at the end. The creator's verdict is that Bolt DIY is a solid self-hosted option, with the rough results possibly due to the model choice. The video is light on measurement and does not compare models or costs.

## Key ideas
- **Bolt DIY is a self-hosted, open-source take on Bolt.new that runs locally after a clone and pnpm setup.** — The creator frames it as the free alternative to Bolt.new, previously named bolt fork and then renamed to Bolt DIY. He stresses it suits people who want to self-host. ([0:00](https://youtu.be/xsJAA3vhy0E?t=0))
- **Model access goes through an API key, and OpenRouter is the easiest route to many models, including DeepSeek V3.** — Keys can go in the UI or an env file. OpenRouter lists many providers and models under one key. The creator notes some providers offer free keys or free models, and paid models require credits. The 'free' in the title applies to the tool, not to the model calls. ([4:18](https://youtu.be/xsJAA3vhy0E?t=258))
- **The first failure was a provider mismatch, not a model problem.** — The creator picked DeepSeek as the provider with an OpenRouter key, which produced an API error. Switching the provider to OpenRouter and then choosing the DeepSeek V3 model fixed it. Direct DeepSeek keys need the DeepSeek provider configuration instead. ([5:42](https://youtu.be/xsJAA3vhy0E?t=342))
- **The app reports a set of 2025-era features: repo and chat import, auto-install, and error autofix.** — New items include a Get Clone button, file upload import, chat import, a prompt library, auto-detection of package.json with dependency install and preview, a selection tool, terminal and preview error detection with autofix, starter templates, and Perplexity integration. ([2:53](https://youtu.be/xsJAA3vhy0E?t=173))
- **Iterative follow-up prompts fix some bugs but not all, and the whiteboard test ends with two broken features.** — After the first build, pen, color and thickness work, but text and shapes do not. A follow-up prompt adds an eraser, which works though its icon does not change. Rectangle and circle still fail at the end. The creator attributes this partly to the model and suggests trying other models. ([8:34](https://youtu.be/xsJAA3vhy0E?t=514))
- **The creator recommends the DeepSeek chat model over the coder model for this use.** — He says DeepSeek suggests using deepseek-chat rather than deepseek-coder, and he switches to chat before generating the whiteboard. ([4:18](https://youtu.be/xsJAA3vhy0E?t=258))

## Techniques
- **Clone, install and run Bolt DIY locally** — 1) git clone the repo from its GitHub page (or git pull inside an existing clone to update). 2) Ensure pnpm is installed for your OS. 3) Run pnpm install inside the folder. 4) Run pnpm run dev and open the localhost address it prints in the browser. *When:* Self-hosting Bolt DIY on a dev machine as a free alternative to Bolt.new. Requires pnpm and git.
- **Configure OpenRouter as the provider with DeepSeek V3** — On OpenRouter, open the model page, go to the API section, create a key (optional credit limit), then paste it into Bolt DIY or the env file. In Bolt DIY, set the provider dropdown to OpenRouter and choose the DeepSeek V3 model from the list. If the model is not listed, search for it on OpenRouter. Do not pick the direct DeepSeek provider unless you have a DeepSeek key. *When:* Trying one key across many models, or when the direct DeepSeek provider gives API errors.
- **Set a model from the dropdown and check its voice and image support** — Choose the model from the dropdown (the creator also lists Anthropic, Google and Hugging Face options). Speech recognition works only with supported models such as Claude and GPT. Image attachments can give extra context. *When:* Choosing the model for a build, or when using speech or image inputs.
- **Iterate with one bug per follow-up prompt** — Paste the initial spec, check the preview, then send a focused follow-up prompt for each broken feature (for example 'fix text and shape, add an eraser'). The tool reruns npm install and restarts the preview on its own. Verify each feature manually in the preview. *When:* Building a small app where the first generation is partly broken. Test each feature before moving on.

## Numbers
- Creator says DeepSeek V3 is better than Claude models and costs one-fourth the price. This is an unverified claim with no benchmark or pricing data shown. ([1:34](https://youtu.be/xsJAA3vhy0E?t=94))

## Hot takes
- The 'Codes for FREE' title overstates it: the tool is free, but model calls depend on provider keys, and the creator says paid models need credits.
- The claim that DeepSeek V3 beats Claude and costs a quarter as much is asserted, not shown. The whiteboard test shows the opposite of a clean win, with shapes still broken.
- The video is mostly install steps and one demo. It gives no comparison, cost data or repeatable evaluation, so practitioner depth is thin.
- The creator blames the model for the broken shapes without testing a second model, so the cause is unproven.

## Tools mentioned
Bolt DIY (bolt.diy), Bolt.new, DeepSeek V3, DeepSeek chat, deepseek-coder, OpenRouter, ShadCN UI, Claude 3.5 Sonnet, Perplexity AI, Hugging Face, pnpm, git, npm (run automatically by Bolt DIY)

## Relevance to our work
- **agentos** (1/3): Shows a self-hosted client that routes many providers through one OpenRouter key, the same multi-provider idea AgentOS targets. The talk does not show any proxy, budgeting or base_url setup. → *Low priority. If you want a third-party UI to drive an OpenAI-compatible endpoint, test it against the AgentOS proxy. Check whether Bolt DIY supports a custom base URL first, since the talk does not show that.*
