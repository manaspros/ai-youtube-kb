# Has This Just Made Every Other Performance Optimization Obsolete?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `5n9JjFRdeh4` · [watch](https://youtu.be/5n9JjFRdeh4) · **date:** 2025-11-02 · **length:** 6:49 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** web-performance, prefetching, predictive-preloading, foresight-js, frontend, image-loading, network-throttling, mouse-trajectory

> Better Stack demos Foresight.js, a 5KB framework-agnostic library that preloads links and images from predicted mouse movement, then argues it should come only after cheaper performance fixes.

## Summary
The presenter demos Foresight.js, a roughly 5KB framework-agnostic library that predicts which element a user will interact with from mouse trajectory and preloads it before the click. In a side-by-side image gallery under throttled 4G, Foresight-driven preloading showed images instantly while hover-based preloading produced visible pop-in, though this is one informal demo rather than a measured benchmark. The walkthrough covers the hit-slop hitbox expansion, the trajectory prediction time setting (tuned from 50 ms to 300 ms in the debugger), and the register/unregister API with per-element hit-slop overrides. Limits named in the video: no support for touch or mobile devices, and no ready-made docs for TanStack Router, which has its own prefetch plans, while Next.js and React Router are covered. The presenter's verdict is to reach for it only after lazy loading, progressive image loading, chunking and smaller images have been exhausted. The title oversells the content; the library is a niche tool for mouse-driven desktop prefetching.

## Key ideas
- **Foresight.js predicts intent from mouse trajectory and preloads before the click, unlike plain preload-on-hover or preloading every link.** — Described as a 5KB, framework-agnostic library. The presenter says the ball-like debugger cursor 'latches onto' a target the user seems about to click, and that element's content is preloaded. ([0:00](https://youtu.be/5n9JjFRdeh4?t=0))
- **Hit slop enlarges an element's hover hitbox so prediction fires earlier.** — Blue boxes in the debugger show the expanded hitbox. Slow mouse movement over that enlarged area triggers preloading before the real hover. ([1:23](https://youtu.be/5n9JjFRdeh4?t=83))
- **In the demo, intent-based preloading beat hover-based preloading for large images on a throttled connection.** — Thumbnails were about 20KB. The presenter estimates full-size images at 4-8MB and throttles to slow 4G. Hover preloading showed pop-in after scrolling and clicking; Foresight displayed the image instantly. Single informal run, no measurements beyond the Network tab. ([1:23](https://youtu.be/5n9JjFRdeh4?t=83))
- **Trajectory prediction time controls how far ahead the mouse path is extrapolated.** — Set in milliseconds. At about 50 ms the prediction circle barely leads the cursor; at about 300 ms predictions are 'wilder' and reach further ahead. Tunable live in the Foresight debugger. ([4:05](https://youtu.be/5n9JjFRdeh4?t=245))
- **Integration is a per-element register with a callback, plus unregister for cleanup.** — setupForesightForItem registers an image element; the callback preloads the image and updates a metrics value. Per-element hit slop overrides the global default. Unregister is wired to the popup close handler. ([5:22](https://youtu.be/5n9JjFRdeh4?t=322))
- **The presenter's bottom line: this is a late-stage optimization, not a first step.** — Only after lazy loading, progressive image loading, chunking and image size reduction are done and the site is still too slow. No touch or mobile support, since it relies on cursor movement. TanStack Router reportedly has its own predictive prefetch in progress. ([5:22](https://youtu.be/5n9JjFRdeh4?t=322))

## Techniques
- **Intent-based preload via register/unregister** — Initialize Foresight with optional defaults (global hit slop, trajectory prediction time in ms; initialization can be skipped to use defaults). For each image or link element, call the instance's register method with the element and a callback that performs the preload and updates metrics. Set a per-element hit slop to override the global value. Call unregister on cleanup, e.g. when a lightbox or popup closes. *When:* Image galleries or lightboxes where the target asset is large and the user's next click is predictable from cursor movement, on desktop only.
- **Tune trajectory prediction live in the debugger** — Open the Foresight debugger in the browser (minimizable, controlled by its settings panel) and change the trajectory prediction time. Shorter values (about 50 ms) keep predictions close to the cursor; longer values (about 300 ms) predict further ahead and fire more speculatively. *When:* Before committing to a config, to balance wasted bandwidth against how early the preload starts.
- **Enlarge hit slop for early triggering** — Increase the hitbox around an element (globally, or per element to override) so that the intent prediction fires before the cursor reaches the element. *When:* Targets are small or sit far from the cursor's likely path, and you want preloads to finish before hover.
- **Compare preload strategies under throttled network** — Throttle the browser network to slow 4G, then test each strategy (hover preload vs. intent preload) by scrolling, waiting, and clicking. Watch the Network tab to see when the full-size request starts relative to the click, and check for visible pop-in. *When:* Validating any prefetching change against slow connections, not just on a fast local network.
- **Performance ordering** — The presenter's order of operations before predictive prefetching: lazy loading, progressive image loading, code chunking, and reducing image sizes. Add intent-based preloading only if the site is still too slow for users. *When:* Deciding whether a predictive prefetch library is worth the added dependency on a site.

## Numbers
- Foresight.js is about 5KB and framework-agnostic. ([0:00](https://youtu.be/5n9JjFRdeh4?t=0))
- Thumbnails in the demo gallery are about 20KB; the full-size images are estimated at roughly 4-8MB each. ([1:23](https://youtu.be/5n9JjFRdeh4?t=83))
- A throttled slow 4G connection was used for the comparison. The on-screen image size went from 0 to 21KB while loading the thumbnail. ([1:23](https://youtu.be/5n9JjFRdeh4?t=83))
- Trajectory prediction time was shown at about 50 ms (short) and about 300 ms (long), with visibly different prediction reach. ([4:05](https://youtu.be/5n9JjFRdeh4?t=245))

## Hot takes
- The title ('Made Every Other Performance Optimization Obsolete?') overstates the content; the presenter's own conclusion is that it is a late-stage option, not a replacement.
- The side-by-side comparison is a single informal demo with no repeated runs or timing numbers, so the 'instant' claim is anecdotal.
- No mobile or touch support, since it depends on cursor movement, so it does not help a large share of web traffic.
- The presenter notes that the blue hit-slop boxes in one screen recording looked like a debugger bug, so the visual tooling is not fully polished.

## Tools mentioned
Foresight.js, TanStack Router, Next.js, React Router, React, Vue, Svelte
