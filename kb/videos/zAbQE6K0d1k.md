# The NPM Package Everyone Is Adding To Their Site (Web Haptics)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `zAbQE6K0d1k` · [watch](https://youtu.be/zAbQE6K0d1k) · **date:** 2026-04-02 · **length:** 4:50 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Polymarket, Apple
- **topics:** dev-tools, product-ux · **tags:** haptics, npm, react, svelte, web-api, navigator-vibrate, ios, safari, ui-feedback, frontend

> Walkthrough of web-haptics, an npm package that adds vibration feedback to websites through a React hook, custom patterns, and a hidden-switch trick that makes it work on iOS.

## Summary
The host presents web-haptics, a small npm package that gives websites haptic feedback on Android and iOS with a single trigger function. He shows the React hook, which returns trigger, cancel and an isSupported flag, and a debug option that plays a simulated vibration sound for testing on a laptop. Patterns can be built-in presets such as buzz, error or heavy, or custom arrays of timed vibrations with delay, duration and intensity, which can be authored in the package's web editor. Android works through the standard navigator.vibrate API, but iOS has no support for it, so the library falls back to clicking a hidden switch input, which iOS renders as a haptic tick. The host calls this a neat workaround that depends on iOS behaviour Apple could patch. The video is a short tutorial with no benchmarks, and its adoption claims (trending on Twitter, used by Polymarket) are unverified.

## Key ideas
- **One npm package gives websites haptic feedback, and the same trigger function works across React, Svelte and vanilla JS helpers.** — The React hook returns trigger, cancel and isSupported, so a button click can fire a vibration in a single call. The video says it is trending and that Polymarket has adopted it, but both are unverified claims. ([0:00](https://youtu.be/zAbQE6K0d1k?t=0))
- **Debug mode lets you test haptics on a desktop with no device.** — Setting debug to true in the hook plays an audible noise that simulates the vibration on each trigger. It is the only local check the host shows before testing on a phone. ([1:08](https://youtu.be/zAbQE6K0d1k?t=68))
- **Patterns come in two forms: presets and custom arrays of timed vibrations.** — Presets include buzz, error and heavy. A custom pattern is an array of steps, each with a delay in ms from the previous vibration, a duration in ms and an intensity where 1 is strongest. The host's example has four steps. ([2:27](https://youtu.be/zAbQE6K0d1k?t=147))
- **Designing a pattern by ear is slower than designing it in the editor on the package website.** — The web editor lets you click to add a vibration, drag horizontally to set duration and vertically to set intensity, and play the result. The host suggests testing on a phone, since a laptop cannot show the feel. ([2:27](https://youtu.be/zAbQE6K0d1k?t=147))
- **iOS has no navigator.vibrate support, so the library falls back to a hidden switch.** — On Android it calls navigator.vibrate. On iOS it clicks an invisible checkbox-style switch several times to mimic the pattern, because iOS gives a haptic tick on switch toggles. The hook has a showSwitch option to reveal the switch while debugging. ([3:27](https://youtu.be/zAbQE6K0d1k?t=207))
- **The iOS path depends on undocumented behaviour that Apple could remove.** — The host says he hopes Apple does not patch the trick, or that it adds real support for the vibrate function. Treat this as a fragile workaround, not a supported API. ([3:27](https://youtu.be/zAbQE6K0d1k?t=207))

## Techniques
- **Basic React trigger** — Import the useWebHaptics hook (captioned as 'use web haptics'). Destructure trigger, cancel and isSupported from it. Call trigger() in a button onClick handler. Use cancel() to stop a running pattern. Check isSupported before relying on the feedback. Set debug: true in the hook options while developing on desktop. *When:* Adding tactile confirmation to buttons, success or error states, or other UI actions on mobile web pages, especially where you need to test on a laptop first.
- **Preset patterns** — Import one of the package's default patterns (buzz, error, heavy and others listed on the package site) and pass it to trigger(). The exact import name is not shown in the transcript. *When:* Standard feedback such as success or error, where a custom pattern is unnecessary.
- **Custom vibration array** — Pass trigger() an array of step objects. Each step has delay (ms since the previous vibration), duration (ms) and intensity (0 to 1, where 1 is strongest). Build the array in the package website editor: click to add a step, drag horizontally for duration and vertically for intensity, press play to preview, then copy the array into code. *When:* A distinctive feel for a key interaction, such as a confirm or a warning, where a preset is not strong enough.
- **Hidden-switch fallback for iOS** — When navigator.vibrate is unavailable (iOS), the library clicks an invisible switch input several times in the pattern's timing, and iOS renders each toggle as a haptic tick. For debugging, set showSwitch: true in the hook options to make the switch visible and check the toggle timing. You do not write this part yourself; the package handles it. *When:* You need haptic feedback on iOS Safari and accept that the behaviour depends on an iOS quirk that could change. Do not rely on it for anything critical.
- **Feature detection before rendering haptic UI** — Read the isSupported flag from the hook. If it is false, skip the feedback or fall back to a visual cue. Expect that on iOS the switch fallback may still produce feedback even when navigator.vibrate is missing. *When:* Shipping haptics to a mixed audience of Android, iOS and desktop users, where the UI should work with no haptics.

## Numbers
- The example custom pattern contains four vibration steps, each with a delay, a duration and an intensity. ([2:27](https://youtu.be/zAbQE6K0d1k?t=147))
- Pattern timing is in milliseconds: delay is measured from the previous vibration, and duration is how long each vibration lasts. ([2:27](https://youtu.be/zAbQE6K0d1k?t=147))
- Intensity runs from 0 to 1, where 1 is the strongest vibration. ([2:27](https://youtu.be/zAbQE6K0d1k?t=147))
- The speaker says the package is trending on Twitter and that Polymarket has implemented it. Both are unverified and anecdotal, with no usage figures. ([0:00](https://youtu.be/zAbQE6K0d1k?t=0))
- The video is 4:50 long and contains no benchmarks or measured latency. ([0:00](https://youtu.be/zAbQE6K0d1k?t=0))

## Hot takes
- The iOS switch trick is a clever workaround, but it relies on undocumented behaviour that Apple could patch. The host says so himself and hopes Apple adds real vibrate support.
- The 'everyone is adding it' framing rests on a Twitter trend and one named adopter (Polymarket), with no evidence beyond that.
- Haptics are a small UI polish feature. The video does not discuss when they help or hurt, or accessibility and user-preference concerns.

## Tools mentioned
web-haptics (npm package, the video spells it 'webhaptics'), React hook (useWebHaptics, captioned as 'use web haptics'), Svelte helper, Vanilla JavaScript API, navigator.vibrate (Web Vibration API), web-haptics package website editor

## Relevance to our work
- **prosharness** (1/3): ProsHarness has phone-driven approvals. If the approval surface is a mobile web page, a haptic cue on a new approval request could help. → *If the phone approval page is a web UI, prototype a trigger on new approval requests with isSupported checked first. Low priority.*
- **general** (1/3): Shows a general pattern for mobile web feedback: feature-detect, add a desktop debug mode, and degrade gracefully when a platform API is missing. → *Skim only if building a mobile-facing web UI. No agent-infra action.*
