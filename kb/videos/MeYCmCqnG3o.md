# React's NEW Activity Component Explained

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `MeYCmCqnG3o` · [watch](https://youtu.be/MeYCmCqnG3o) · **date:** 2025-11-02 · **length:** 7:06 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** ?
- **topics:** dev-tools · **tags:** react, activity, unstable_Activity, conditional-rendering, state-preservation, effects, strict-mode, tabs, frontend-performance, experimental-api

> Walks through React's experimental Activity component, which hides a subtree while keeping its state and pre-rendering it, compared with conditional rendering and CSS hiding. Practical for tab UIs, with caveats.

## Summary
The video explains React's experimental Activity component, which toggles a subtree between visible and hidden modes. The demo uses a three-tab UI where each tab fetches its own data with an artificial two-second delay. With conditional rendering, switching tabs unmounts the component, refetches data and wipes form input. Hiding the tabs with CSS keeps state but mounts everything up front and cannot pause side effects. Activity combines the two: hidden children are pre-rendered at lower priority, their state is kept, and their effects are cleaned up while hidden. A second demo with two videos shows that Activity lets a hidden video pause and resume from where it left off. The speaker notes the API is only on the experimental React build under an unstable_ import name, so it is not for production yet.

## Key ideas
- **Conditional rendering unmounts a tab on every switch, so each tab refetches its data and a half-filled form is wiped when you come back.** — The demo has about, post and contact tabs, each with a two-second fake data delay. Each switch re-runs the fetch, and the contact form resets to defaults. ([0:00](https://youtu.be/MeYCmCqnG3o?t=0))
- **Hiding tabs with CSS keeps state and avoids refetching, but every tab mounts on load and nothing pauses when hidden.** — Loading all components up front means the hidden tabs' data arrives immediately, and the form survives tab switches. The speaker says that setup gives you no way to stop hidden side effects, such as video playback. ([1:10](https://youtu.be/MeYCmCqnG3o?t=70))
- **Activity with mode set to visible or hidden gives the CSS behaviour plus performance benefits, because hidden children are pre-rendered at lower priority than visible ones.** — Visible content renders first. In the demo, the post tab's data call fires before the about call once Activity is in use. Pre-rendering means switching to a hidden tab shows its content immediately. ([2:11](https://youtu.be/MeYCmCqnG3o?t=131))
- **When an Activity is hidden, its effects are destroyed and cleanup runs, but its React and DOM state is kept and reused when it becomes visible again.** — This is why form input survives. The speaker flags this as a foot gun: effects do not run while hidden, so the work in them must be designed around that. ([3:26](https://youtu.be/MeYCmCqnG3o?t=206))
- **Use effects for play and pause so that hiding an Activity runs cleanup and resuming it runs the effect again.** — In the two-video demo, conditional rendering resets playback to the start on every switch. With Activity, the hidden video pauses through cleanup and the visible one resumes from its saved position, with no reload. ([5:47](https://youtu.be/MeYCmCqnG3o?t=347))

## Techniques
- **Replace conditional rendering with Activity for tab-like UIs** — Wrap each tab's component in Activity and set mode per tab, e.g. mode is visible when the active tab matches and hidden otherwise. Keep each tab's data fetching and form state inside its own component, since Activity preserves them. Import from the experimental React build as unstable_Activity (speaker's wording: 'import unstable activity'); the exact import line is not shown on screen. *When:* Tabs or panels whose inner state or data should survive switching, and where the first-visit wait should be hidden by pre-rendering. Only in experimental builds, not production.
- **Put media playback in an effect with cleanup** — Start playback in a useEffect and pause it in the cleanup. Under Activity, hiding the panel runs the cleanup, and showing it runs the effect again. Keep the playback position in the preserved state so it resumes where it stopped. *When:* Several media players in tabs or panels where only the visible one should play and it should resume rather than restart.
- **Compare the three approaches before choosing** — (a) Conditional rendering: unmounts, state lost, refetch on every switch. (b) CSS display toggle: state kept, all children mounted up front, no cleanup on hide. (c) Activity: state kept, hidden children pre-rendered at lower priority, effects cleaned up while hidden. Pick based on whether you need preserved state, background data loading, or pause-on-hide. *When:* Deciding how to structure stateful tabs, or when a bug report says state or data reloads on tab switch.

## Numbers
- Each tab's data call has an artificial delay of two seconds, used to show the reload cost of conditional rendering. ([0:00](https://youtu.be/MeYCmCqnG3o?t=0))
- With conditional rendering the video demo's mount count stays at two under React Strict Mode and does not grow as tabs are switched. ([4:45](https://youtu.be/MeYCmCqnG3o?t=285))
- The demo has three tabs (about, post, contact) and two videos (Big Buck Bunny, Elephant's Dream). ([0:00](https://youtu.be/MeYCmCqnG3o?t=0))

## Hot takes
- The API is available only on the experimental React build under an unstable_ name, and the speaker says that signals it should not be used in production yet.
- The speaker frames Activity as a more efficient CSS toggle, but its effect cleanup and pre-rendering trade-offs are not benchmarked. The demos are console logs and visual timings only.
- The speaker closes by asking whether this is React fixing its past mistakes or a welcome addition for performance, which signals an opinion without giving one.

## Tools mentioned
React, React Activity (unstable_Activity, experimental React build), React Strict Mode, CSS (display toggling), Cursor

## Relevance to our work
- **general** (1/3): Only relevant if we build a React UI over our data, such as a KB or trace dashboard with tabs whose state should survive switching. → *If a React dashboard is built, keep tab state with conditional rendering for now; revisit Activity once it leaves experimental, and test that effect cleanup behaves as expected.*
