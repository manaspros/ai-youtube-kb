# GSAP Is Now 100% FREE

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `sDdqMEHHEZ8` · [watch](https://youtu.be/sDdqMEHHEZ8) · **date:** 2025-11-02 · **length:** 7:53 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host (not named in transcript) · **orgs:** Webflow, Better Stack
- **topics:** dev-tools · **tags:** gsap, javascript, animation, scrolltrigger, timeline, stagger, tween, scrub, free-license, frontend

> Better Stack beginner walkthrough of GSAP after Webflow made GSAP and its plugins free: tweens, stagger, timelines, paused playback and ScrollTrigger scrubbing a video. No benchmarks; the main news is the pricing change.

## Summary
The presenter announces that Webflow has made GSAP and its plugins completely free, which he presents as removing the one drawback of the library. He opens with demos of GSAP-built sites (scroll animation, a portfolio using Observer and Motion Path, SVG morphing with text on a motion path) to show its range. The core lesson covers four tween types (to, from, fromTo, set), animating arbitrary properties including custom numeric properties on plain objects, and repeat/yoyo. He then shows stagger for sequencing elements by DOM order, and gsap.timeline() with position offsets for finer control. Playback control comes next: start paused, call play(), and restart when progress completes. The last section uses ScrollTrigger with scrub to tie a video's currentTime to scroll position, which he says resembles the GTA 6 landing page effect. He says he would not ship his primitive version to production.

## Key ideas
- **GSAP and its plugins are now free; the speaker credits Webflow with making the change.** — Presented as removing the paid-plugin barrier. Stated claim only, no license terms given in the video. ([0:00](https://youtu.be/sDdqMEHHEZ8?t=0))
- **Every GSAP animation is a tween, and there are four kinds: to, from, fromTo and set.** — to animates from the current state to given values; from animates from given values to the current state; fromTo specifies both ends; set applies the values instantly. Selectors can be a class name, an ID or the element object. ([1:27](https://youtu.be/sDdqMEHHEZ8?t=87))
- **Tweens can animate essentially any numeric property, including custom properties on a plain JavaScript object.** — Demo tweens an object's count key from 1 to 10 and logs it with an onUpdate callback, so GSAP is usable as a generic number-interpolation engine. ([1:27](https://youtu.be/sDdqMEHHEZ8?t=87))
- **repeat: -1 loops forever and yoyo reverses direction instead of restarting.** — Shows looping behavior as built-in tween options rather than hand-written loops. ([2:42](https://youtu.be/sDdqMEHHEZ8?t=162))
- **stagger offsets each element's start by its order in the matched set, which is the simple way to sequence several elements.** — Same-class elements start together by default. stagger set to a time value starts each one that much later. Stagger is limited to a fixed interval per element, so custom sequencing needs a timeline. ([2:42](https://youtu.be/sDdqMEHHEZ8?t=162))
- **Timelines give explicit control over sequencing. Tweens are added with timeline.to instead of gsap.to, and each has a position parameter.** — Position can be an absolute time in seconds, an offset from the end of the timeline, or a negative offset that overlaps the previous tween. The timeline grows as tweens are added. Unlike stagger, tweens can have different durations. ([3:53](https://youtu.be/sDdqMEHHEZ8?t=233))
- **Playback is controllable: create the timeline with paused set to true, call play() from a button, and restart the animation once its progress is complete.** — Shows the timeline as a programmable object rather than a fire-and-forget animation. ([5:02](https://youtu.be/sDdqMEHHEZ8?t=302))
- **ScrollTrigger with scrub: true ties an animation's progress to scroll position, so the video's currentTime tween plays forward when scrolling down and in reverse when scrolling up.** — The effect is a video animated from currentTime 0 to its duration, not a set of rendered images. The speaker believes the GTA 6 site uses a canvas-based approach with GSAP, and says he would not ship his primitive version to production. ([6:12](https://youtu.be/sDdqMEHHEZ8?t=372))

## Techniques
- **Basic tween on a selector** — Call gsap.to with a target (class name, ID or element) and an object of properties to animate. The demo translates a circle by 40px and changes its fill to blue; the narration does not state the exact property key used for the translation. *When:* Any simple one-off DOM animation where you want the browser to animate from current state to a target.
- **from / fromTo / set variants** — Use gsap.from to animate in from specified values, gsap.fromTo to specify both start and end, and gsap.set to apply values instantly with no animation. *When:* Entrance animations (from), exact start and end control (fromTo), and initial state setup (set).
- **Animate a custom object property** — Create a plain object such as {count: 1}, tween its count property to 10, and read it in an onUpdate callback to log or render each intermediate value. *When:* Counters, number displays, or driving any non-DOM value through GSAP's easing and timing.
- **Looping with repeat and yoyo** — Set repeat to -1 for an infinite loop. Set yoyo to true to reverse direction on each repeat instead of jumping back to the start. *When:* Ambient or idle motion such as pulsing or bobbing elements.
- **Stagger for ordered starts** — Add a stagger property to a tween applied to a class and set its value in seconds. Elements start in DOM order, each delayed by the stagger value. The demo uses 0.5 seconds. *When:* A list or grid of same-type elements animating one after another with equal delays and equal durations.
- **Timeline with position parameter** — Create with gsap.timeline(), add tweens with timeline.to(...), and pass a position value after the tween's vars and a comma. Use an absolute time in seconds to start at a fixed point, a positive value for a gap after the timeline's current end, or a negative value to overlap the previous tween. *When:* Sequences with different durations, overlapping animations, or any choreography stagger cannot express.
- **Paused timeline with manual play** — Create the timeline with paused set to true, call play() from a click handler, and restart it when its progress has reached the end. *When:* Animations triggered by user action rather than page load, or re-runnable demos.
- **Scroll-scrubbed video** — Register the ScrollTrigger plugin. Get the video element by its ID, tween its currentTime from 0 to its duration, and set scrub: true in the ScrollTrigger config. The speaker wraps the video in a container div named scroll content. The narration does not show the exact ID or the plugin registration call. *When:* Scroll-linked video effects where the frames should follow scroll position in both directions. The speaker does not recommend this exact setup for production.

## Numbers
- Pricing: GSAP and its plugins are now free (no dollar figure given). ([0:00](https://youtu.be/sDdqMEHHEZ8?t=0))
- Demo tween translates an element 40px and changes its fill to blue. ([1:27](https://youtu.be/sDdqMEHHEZ8?t=87))
- Demo counter animates a custom property from 1 to 10. ([2:42](https://youtu.be/sDdqMEHHEZ8?t=162))
- Demo stagger: three boxes each translated 500px with duration 3, then a 0.5s stagger example. ([2:42](https://youtu.be/sDdqMEHHEZ8?t=162))
- Timeline demo: green tween lasts 2s; purple tween position set to 1s, so it starts while green is still running and both end together. ([3:53](https://youtu.be/sDdqMEHHEZ8?t=233))

## Hot takes
- The main news is the pricing change. The rest is a beginner-level API walkthrough with no benchmarks, comparisons or production advice.
- The speaker says he would not ship his video-scrub recreation to production. He believes the GTA 6 site uses canvas with GSAP. He states this as a belief, not as checked fact.
- The title's 100% free claim is the speaker's report of Webflow's decision. The transcript includes no license text or source.

## Tools mentioned
GSAP, GSAP ScrollTrigger plugin, GSAP ScrollSmoother plugin, GSAP SplitText plugin, GSAP Observer plugin, GSAP Motion Path plugin, Webflow (named as the company that made GSAP free, not a tool used in the demos)
