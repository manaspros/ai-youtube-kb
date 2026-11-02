# Clone Any Website INSTANTLY! New V0 Updates You Need to See.

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `gNgxnECvLWM` · [watch](https://youtu.be/gNgxnECvLWM) · **date:** 2025-11-02 · **length:** 6:26 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** ?
- **topics:** vibe-coding-app-building, testing-verification · **tags:** v0, website-cloning, url-to-code, console-logging, version-control, element-selection, ui-generation, prompt-iteration

> Walkthrough of v0's new URL-to-clone, built-in console logs, version rollback and click-to-edit features, shown on one Notion homepage clone; thin substance behind a hype title.

## Summary
The host demos four recent v0 features: cloning a site by pasting its URL, built-in console logging, version rollback, and selecting a UI element to target an edit. The clone demo uses the Notion homepage. The first generation threw an error that was fixed by prompting v0 again, and the result matched the page layout closely but used placeholders for images. The console-log demo shows a generated button click being logged and the output being pasted back into chat for fixes. The version demo recolors the site and then reverts to an earlier version, and the element-select demo adds a confetti effect that first rendered behind a popup until the prompt was made more explicit. The video closes by suggesting generated templates could be sold, with no analysis of that claim. The content is a single-site feature tour with no metrics, comparisons or failure-rate data.

## Key ideas
- **v0 can now generate a site from a pasted URL: it takes a screenshot of the page, then generates front-end code that is more structured than the single-page output the host saw before.** — Demo uses the Notion homepage. The host adds clarifying instructions with the URL. Generation first threw an error, which was fixed by prompting v0 again. ([0:00](https://youtu.be/gNgxnECvLWM?t=0))
- **The clone is structurally close to the original, but images are replaced with placeholders.** — The host judges the overall layout as nearly identical after the fix, and says the missing images are the main visible gap. This is one site, not a benchmark. ([1:47](https://youtu.be/gNgxnECvLWM?t=107))
- **Built-in console logging lets generated apps emit logs without manual instrumentation, and those logs can be passed back to v0 to fix issues.** — The host asks for a popup on the Get Notion Free button plus logs. The console then shows the button click and any errors, which the host feeds back to v0. ([1:47](https://youtu.be/gNgxnECvLWM?t=107))
- **Version control lets you revert to an earlier generation and mark it as the main version so later edits build on it.** — The host recolors the whole site blue and red, then rolls back. The rollback is set as the base for future changes through a revert-to-this-version action. ([3:31](https://youtu.be/gNgxnECvLWM?t=211))
- **A select mode lets you click a specific element and describe a change scoped to that section, instead of describing it in a global prompt.** — The host selects a button and asks for confetti when it is pressed and the popup appears. The confetti renders behind the popup, so the host re-prompts to place it on top. ([3:31](https://youtu.be/gNgxnECvLWM?t=211))
- **Prompt wording mattered for a layering fix: the first request did not fix the z-order, and an explicit explanation in the main chat did.** — The host says the issue may have been their own prompting, and the fix is not guaranteed to be first-try. This is the host's own assessment, offered honestly rather than as a general finding. ([4:57](https://youtu.be/gNgxnECvLWM?t=297))

## Techniques
- **Clone a page from its URL** — Paste the page URL into v0 and add instructions about what to keep or change. v0 captures a screenshot and generates the front-end structure. Expect placeholder images and possibly an initial runtime error, then iterate with follow-up prompts. *When:* Fast layout prototyping from an existing design. Not for pixel-accurate or asset-complete clones.
- **Log-driven debugging loop** — Turn on v0's built-in console logging instead of adding console.log calls by hand. Ask the generated code to log key events such as button clicks. Copy the logs and errors from the console and paste them back to v0 as the next prompt. *When:* Debugging generated UI behaviour where you need the runtime event trace, not only the visual result.
- **Roll back and rebase on a known-good version** — Use the version history to revert to an earlier generation. Mark it as the main version, so later changes build on it and not on the rejected one. *When:* Trying a risky design change, such as a colour scheme, that you may want to undo.
- **Scoped edits by element selection** — Open the preview in full screen, click the select control, hover the target element and click it, then describe only that change. If the result is wrong, restate the placement precisely (for example, 'on top of the popup, not behind it') and explain it in the main chat. *When:* Changing one component in a generated page without re-prompting the whole layout.

## Numbers
- Video length is 6:26. No benchmarks, costs, latencies or adoption figures are given. ([0:00](https://youtu.be/gNgxnECvLWM?t=0))

## Hot takes
- The 'Clone Any Website INSTANTLY' title overclaims: the only evidence is a single Notion homepage clone that needed a fix and still used placeholder images.
- Substance is a feature tour with one demo and no comparisons, error rates or limits, so quality is capped at 2.
- The closing suggestion to start selling generated templates is unexamined and off-topic for the feature demo.

## Tools mentioned
v0

## Relevance to our work
- **prosharness** (1/3): Shows a generate, run, read-console, and feed-the-logs-back-to-the-generator loop, a loose parallel to a harness that checks agent output before continuing. → *When building ProsHarness verification, consider feeding runtime logs or errors from the generated app back into the coding agent as the next prompt, and compare that with our current checkpoint-based loop.*
