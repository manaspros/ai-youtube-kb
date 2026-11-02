# Harper: The Free, Private Grammarly Alternative Built in Rust

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `lU_jse27kWA` · [watch](https://youtu.be/lU_jse27kWA) · **date:** 2026-08-02 · **length:** 5:40 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Automattic, Grammarly, LanguageTool
- **topics:** dev-tools · **tags:** grammar-checker, rust, privacy, offline, language-server, lsp, neovim, vs-code, obsidian, deterministic-rules, linting, writing-tools

> Better Stack demos Harper, a free, offline, rule-based grammar checker written in Rust that runs in editors and covers comments, commits and docs. The main takeaway is predictable, private, instant checks in exchange for narrower coverage than ML tools.

## Summary
The host presents Harper as a free, Rust-based grammar checker that runs locally with no AI or ML model, using about 287 handwritten rules, so the same sentence always gets the same verdict. The video stresses that nothing leaves the machine, that the engine works with Wi-Fi off, and that the vendor claims under 10 ms per check, which the host admits is unbenchmarked. Integrations shown include a VS Code extension, Homebrew, an Obsidian plugin (about 200k downloads), language-server support for Neovim, Zed, Helix and Emacs, and a browser playground. The host's main point is that the rule ceiling is real: a broken sentence can pass clean, and false positives (for example "Cloudflare") still happen, with about 240 false-positive issues logged in the repo. Limitations include English-only support (five dialects), a self-hosted LanguageTool alternative that needs a roughly 16 GB n-gram dataset for its context checks, and one user's report of over 1 GB RAM in the language server. The host recommends Harper for code comments, commit messages, docs and notes, and keeping an ML tool like Grammarly for tone and rewrites. Ownership by Automattic (since Nov 2024, Apache 2.0 kept) is flagged as a trust concern for some developers.

## Key ideas
- **Harper has no AI; it is a deterministic rule-based engine** — Text is tokenized word by word and checked against about 287 handwritten Rust rules. The host argues the same sentence always gets the same verdict, unlike ML checkers whose verdicts change between runs. ([0:00](https://youtu.be/lU_jse27kWA?t=0))
- **Nothing leaves the machine, so checks are instant and work offline** — The host shows the checker working with Wi-Fi off and claims under 10 ms per check. The 10 ms figure is a vendor claim, and the video says no benchmarks exist yet. ([1:00](https://youtu.be/lU_jse27kWA?t=60))
- **Ownership and licensing context** — Harper has been owned by Automattic (the WordPress company) since Nov 2024. It hired the creator and kept the project Apache 2.0. The video flags this as a trust concern for some developers. ([1:00](https://youtu.be/lU_jse27kWA?t=60))
- **Its real niche is developer surfaces, especially code comments** — It integrates through a VS Code extension, Homebrew, an Obsidian plugin and language-server support for Neovim, Zed, Helix and Emacs. It checks prose inside comments and ignores surrounding code; in Obsidian it skips code fences. ([2:22](https://youtu.be/lU_jse27kWA?t=142))
- **Browser playground gives a zero-install trial** — The engine is compiled to run in the browser, so writewithharper.com runs the full checker in a tab with no install. ([2:22](https://youtu.be/lU_jse27kWA?t=142))
- **Rules set a hard ceiling on what gets caught** — A grammatically broken sentence such as 'me and Sally went to have seen the duck's cousin' passed with zero flags, and so did 'what your name?'. If no rule matches the error shape, nothing fires. ([3:39](https://youtu.be/lU_jse27kWA?t=219))
- **Tradeoffs against the alternatives** — LanguageTool, self-hosted, has about 6,000 rules, but its good context checks need a roughly 16 GB n-gram dataset and matching RAM. Without it, HN users reported missed obvious errors. Grammarly's ML covers tone and whole-sentence rewrites, which Harper does not attempt. ([2:22](https://youtu.be/lU_jse27kWA?t=142))
- **Recommended use: free private checks for comments, commits, docs and notes** — The host advises keeping a paid ML tool for tone rewrites. Harper is released every week or two, and the target surfaces are comments, commit messages, docs and notes. ([4:55](https://youtu.be/lU_jse27kWA?t=295))

## Techniques
- **Editor-integrated deterministic prose linting** — Install Harper through Homebrew or the VS Code extension, or wire its language server into Neovim, Zed, Helix or Emacs (the video says this is one line of config; the exact config is not shown). It checks prose in comments and docs, skips code, and in Obsidian skips code fences. *When:* Checking code comments, commit messages, markdown docs and notes, where ML checkers that fire on every keystroke are noisy or send text off the machine.
- **Verify the privacy claim offline** — After installing, turn off Wi-Fi and confirm checks still run. For a zero-install check, paste text into the writewithharper.com browser playground. *When:* Before relying on a 'nothing leaves the machine' claim for sensitive text.
- **Calibrate coverage with probe sentences** — Test with sentences containing known errors ('I ate an pineapple', a doubled 'the the', 'your point is mute') to confirm the rules fire. Then test a clean-looking but broken sentence ('me and Sally went to have seen the duck's cousin') to map what the rules miss. *When:* Deciding whether a rule-based checker's coverage is good enough for your writing before trusting it.
- **Split the work: rules for correctness, ML for rewrites** — Use the deterministic checker for predictable, fast correctness on every keystroke, and keep an ML tool for tone, clarity and full-sentence rewrites. *When:* Mixed workflows where stable verdicts matter for the everyday editor check, but rewriting help is still wanted.

## Numbers
- Grammarly costs over $140 per year ([0:00](https://youtu.be/lU_jse27kWA?t=0))
- Harper uses about 287 handwritten Rust rules and no AI ([0:00](https://youtu.be/lU_jse27kWA?t=0))
- Vendor-claimed check latency under 10 ms (no published benchmarks) ([1:00](https://youtu.be/lU_jse27kWA?t=60))
- Harper owned by Automattic since Nov 2024 (Apache 2.0 kept) ([1:00](https://youtu.be/lU_jse27kWA?t=60))
- Obsidian plugin about 200,000 downloads ([2:22](https://youtu.be/lU_jse27kWA?t=142))
- LanguageTool good context checks need about a 16 GB n-gram dataset ([2:22](https://youtu.be/lU_jse27kWA?t=142))
- LanguageTool has about 6,000 rules (as stated in the video) ([3:39](https://youtu.be/lU_jse27kWA?t=219))
- About 240 issues in the repo mention false positives ([3:39](https://youtu.be/lU_jse27kWA?t=219))
- One Neovim user saw the language server use over 1 GB of RAM ([3:39](https://youtu.be/lU_jse27kWA?t=219))
- Harper supports five English dialects only ([3:39](https://youtu.be/lU_jse27kWA?t=219))
- Harper is released every week or two ([4:55](https://youtu.be/lU_jse27kWA?t=295))

## Hot takes
- The 'keylogger you pay for' framing and the claim that Grammarly stores everything you type are asserted from Grammarly's documentation, not shown on screen.
- Speed and memory figures are vendor claims. The video itself says no benchmarks exist yet.
- The title's 'Free, Private' framing holds for local use, but the video's own examples show the rule-based ceiling: broken sentences pass clean.
- The host's 'I checked' claim that the 'the the' flag is a handwritten rule in the source is shown only verbally, not with a code reference on screen.
- The video's Automattic ownership point is presented as a trust concern, and the host frames it as fair without weighing the project's Apache 2.0 license track record.

## Tools mentioned
Harper, Grammarly, LanguageTool, Homebrew, VS Code, Obsidian, Neovim, Zed, Helix, Emacs, writewithharper.com, Rust

## Relevance to our work
- **agentos** (1/3): Deterministic rule verdicts versus ML verdicts that flip between runs is a relevant point for the PII and prompt-injection scan in Govrix Scout, but this is a writing tool with no agent or security content. → *Run a fixed set of PII and injection test strings through the current scanner twice and count verdict flips, then compare with a rule-only baseline.*
