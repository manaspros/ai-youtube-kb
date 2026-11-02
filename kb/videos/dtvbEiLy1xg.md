# Lynx: TikTok’s Blazing Fast Framework – The Next React Native Killer?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `dtvbEiLy1xg` · [watch](https://youtu.be/dtvbEiLy1xg) · **date:** 2025-11-02 · **length:** 7:58 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andres · **orgs:** ByteDance, TikTok, Better Stack
- **topics:** dev-tools · **tags:** lynx, react-native, mobile, cross-platform-ui, main-thread-scripting, dual-threaded-rendering, instant-first-frame, ios, css

> Hands-on review of ByteDance's open-source Lynx, a web-tech (HTML/CSS/JS) mobile UI framework with a dual-threaded design; the verdict is promising but not yet a React Native replacement.

## Summary
The speaker reviews Lynx, an open-source cross-platform mobile UI framework from ByteDance (the TikTok company) that lets developers write apps with HTML, CSS and JavaScript. He contrasts its architecture with React Native's JavaScript-bridge model: Lynx runs a background thread for most app code and a main-thread runtime (main thread scripting) for gestures and animations, with strict rules on what runs there. He also covers instant first frame rendering, which shows content right after the splash screen by letting the main thread render with data already available. A short iOS setup walkthrough follows, using the Lynx Explorer app in the simulator with hot reload. He notes that Lynx runs inside a native Lynx View container rather than as a standalone framework like Expo, so production use means embedding it in native code. His verdict is that Lynx is not yet a React Native killer because it lacks higher-level components and APIs, but embedding a Lynx view for feeds or carousels is a reasonable starting point. The video is an honest, unsponsored walkthrough with no benchmarks of its own; the performance figures come from ByteDance's claims.

## Key ideas
- **Lynx is ByteDance's in-house open-source cross-platform mobile UI framework, written with web technologies (HTML, CSS, JavaScript) but aimed at native performance.** — ByteDance says parts of TikTok already run on it (TikTok Shop section, live-streaming special events). The speaker presents this as more than an experiment. ([0:00](https://youtu.be/dtvbEiLy1xg?t=0))
- **React Native sends almost everything, including gestures, taps and scrolling, through the JavaScript bridge, which adds thread hops.** — The speaker estimates the hops add delays of a few milliseconds, enough to make fast gestures feel sluggish on low-end devices. ([1:09](https://youtu.be/dtvbEiLy1xg?t=69))
- **Lynx uses a dual runtime: a background thread for most app code, plus a main-thread runtime (main thread scripting, MTS) for gestures and animations.** — Small privileged scripts run directly on the main thread and update DOM/style there, avoiding the background round trip. The scroll example moves to zero-delay updates once the function body is marked to run on the main thread. ([1:09](https://youtu.be/dtvbEiLy1xg?t=69))
- **Main-thread code is restricted: it is isolated from background functions, can only exchange small serializable data, and is meant for micro-transactions like gestures, animations and quick style updates.** — Lynx provides run-on-main-thread and run-on-background APIs to cross over, but the speaker says these should be used cautiously because heavy work on the main thread blocks everything. ([2:06](https://youtu.be/dtvbEiLy1xg?t=126))
- **Instant first frame rendering (IFR) shows meaningful content right after the splash screen instead of a blank screen.** — The background thread prepares data while the main thread renders the first frame with whatever data is already available. ByteDance reports 2 to 4 times faster launch than its web and React Native surfaces; this is a vendor claim the speaker does not verify. ([3:16](https://youtu.be/dtvbEiLy1xg?t=196))
- **Lynx is not a standalone framework like Expo or React Native: it renders inside a native Lynx View container, and the Lynx Explorer app is only for development and testing.** — In production you embed the Lynx View in native app code, following the official guide. ([5:35](https://youtu.be/dtvbEiLy1xg?t=335))
- **Verdict: Lynx is not yet a React Native killer. It is early in open source and missing many higher-level components and APIs for a Lynx-only app.** — The speaker suggests embedding a Lynx view for high-interaction surfaces such as feeds or carousels as the practical starting point, and expects it could be a serious contender in about a year. ([6:57](https://youtu.be/dtvbEiLy1xg?t=417))

## Techniques
- **Keep gesture and animation handlers on the main thread** — Mark the handler with a main thread directive placed before the function body, so DOM/style updates run on the main thread instead of round-tripping to the background thread. Keep the function small, pass only serializable data, do not call background functions from it, and use the run-on-background API to hand heavy work back. *When:* Scroll, drag or animation handlers that lag because each event waits for the background thread (the speaker's scroll example).
- **Split work for instant first frame** — Prepare data on the background thread and render the first frame on the main thread with data already available, so the first screen shows content right after the splash screen. *When:* Launch screens and feeds where a blank or white first frame is a visible problem.
- **Embed Lynx View in a native app** — Integrate the Lynx View into the app's native code using the official Lynx guide. Do not treat Lynx as a full standalone app framework. *When:* Performance-critical, high-interaction parts of an existing native app, such as feeds or carousels. The speaker does not recommend a full Lynx-only app yet.
- **Hands-on iOS trial of Lynx** — 1) Install the project with bun (the speaker's package manager). 2) Download the prebuilt Lynx Explorer binary, extract the archive, and drag Lynx Explorer into the iOS simulator. 3) In the Lynx project, run the installer, then run dev. 4) Copy the URL shown with the QR code in the terminal and paste it into Lynx Explorer. Hot reload then applies on save, including CSS animations. The speaker did not show exact command names beyond bun and dev. Android steps are in the official docs. *When:* Evaluating Lynx without building a native container first. Use the official tutorials on the Lynx site (for example a two-column waterfall gallery or a product carousel) to see main-thread animations in practice.

## Numbers
- Lynx launch time is 2 to 4 times faster than ByteDance's web and React Native surfaces (ByteDance-reported, not verified in the video). ([4:14](https://youtu.be/dtvbEiLy1xg?t=254))
- React Native thread hops add delays of a few milliseconds per gesture (the speaker's estimate). ([2:06](https://youtu.be/dtvbEiLy1xg?t=126))
- Lynx is already used in parts of the TikTok app (TikTok Shop section) and for live-streaming special events, according to ByteDance. ([1:09](https://youtu.be/dtvbEiLy1xg?t=69))

## Hot takes
- Lynx is not yet a React Native killer, but embedding a Lynx view for feeds or carousels is a sensible starting point.
- The main-thread-script model, where you choose per function what runs where, is the real architectural difference from React Native's bridge model.
- The launch-speed numbers are ByteDance's own claims, and the video does not benchmark them.

## Tools mentioned
Lynx, Lynx Explorer, Lynx View, React Native, Expo, bun, iOS Simulator
