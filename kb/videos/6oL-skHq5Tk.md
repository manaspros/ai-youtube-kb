# ViewTransition: The BEST Way to Animate React Components

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `6oL-skHq5Tk` · [watch](https://youtu.be/6oL-skHq5Tk) · **date:** 2025-11-02 · **length:** 4:19 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, React (Meta), Bun, Next.js, React Router
- **topics:** dev-tools · **tags:** react, view-transitions, animation, frontend, react-canary, suspense, bun, startTransition, css-animation

> Short Better Stack tutorial on React's canary <ViewTransition> component: wrap elements, trigger updates with startTransition, customize the default fade, and use it with Suspense. Advises keeping router-level view transitions for existing apps for now.

## Summary
The presenter walks through the React <ViewTransition> component, announced at React Conf 2025, which wraps the browser's View Transitions API so animations are driven by React transitions. It is only available in React canary, so the API may change. In a small Bun + React blog, they wrap the post list in the component, import startTransition, and update the click handler so the list animates in and out with the default fade. They then swap in a CSS animation from animate.css through the component's props and callbacks, and use the name prop so matching elements morph between page states. The component also works inside Suspense boundaries, including the fallback, and degrades gracefully in browsers without view transitions. Their closing advice is to use it for new components or apps, but not to switch existing React Router or Next.js view-transition setups straight away. The video is short and demo-driven, with no benchmarks and little detail on the props and callbacks.

## Key ideas
- **React's <ViewTransition> component is a React-side wrapper over the browser View Transitions API, announced at React Conf 2025, and it is canary-only for now** — The speaker says it was added to React earlier in the year, that a blog post came out in March, and that it is only available in React canary, so the API may change. They also note that canary types are not yet published, which causes type errors that they ignore in the demo. ([0:00](https://youtu.be/6oL-skHq5Tk?t=0))
- **Updates must run inside startTransition for any animation to happen** — Wrapping the list in <ViewTransition> alone changes nothing. The click handler must call startTransition so that React marks the update as a transition. The speaker imports startTransition directly instead of useTransition because they do not need isPending. ([1:13](https://youtu.be/6oL-skHq5Tk?t=73))
- **Under the hood, React finds ViewTransition components at commit time and calls document.startViewTransition** — After a render, React looks for ViewTransition components during the commit phase and calls document.startViewTransition with the related transition types. This ties React's transition scheduling to the browser's API. ([2:14](https://youtu.be/6oL-skHq5Tk?t=134))
- **The default fade can be replaced by CSS animations applied to view-transition pseudo-elements** — The speaker copies keyframes from animate.css into the project and attaches them to the view-transition pseudo-elements. The component's default prop is meant to take the animation name, but it did not work under Bun in their setup, so they used another route. The video does not show that route. ([2:14](https://youtu.be/6oL-skHq5Tk?t=134))
- **Page-to-page navigation needs ViewTransition on both the source and destination pages, plus startTransition in the navigation logic** — To animate navigating to a blog post, they add ViewTransition to the index page and to the target page, and wrap the page-changing logic in startTransition. That produces a fade on post click. ([2:14](https://youtu.be/6oL-skHq5Tk?t=134))
- **The name prop makes matching elements morph between states; otherwise React assigns unique names automatically** — Giving the same name to elements in the before and after states turns the transition into a smooth shared-element animation. Without a custom name, React generates a unique name for each element, so nothing is shared. ([2:14](https://youtu.be/6oL-skHq5Tk?t=134))
- **ViewTransition works with Suspense, including the fallback, and degrades to a plain update in unsupported browsers** — The component can wrap Suspense content and can sit inside the fallback prop. The speaker says it is progressively enhanced, so apps still work in browsers without the View Transitions API. ([3:34](https://youtu.be/6oL-skHq5Tk?t=214))
- **Advice is to use the built-in component for new code, not to migrate existing router-level view transitions yet** — The speaker says that apps already using view transitions through React Router or Next.js should not switch straight away. The built-in component is recommended for new components or new apps. They describe the feature as getting closer to production-ready but not yet there. ([3:34](https://youtu.be/6oL-skHq5Tk?t=214))

## Techniques
- **Enable React canary for ViewTransition** — Install the canary builds of react and react-dom (the speaker says to make sure the project uses canary versions). Exact version strings are not shown. Expect type errors because canary types are not published yet. *When:* Trying <ViewTransition> before it ships in a stable React release.
- **Wrap a list in ViewTransition and trigger with startTransition** — Wrap the component that renders the list in <ViewTransition>, importing it from react. Change the button onClick to call startTransition(() => <state update>) and import startTransition directly from react when isPending is not needed. Use useTransition if isPending is needed. *When:* Animating UI that changes in place, such as showing or hiding a list of items.
- **Replace the default fade with a CSS keyframe animation** — Copy keyframes (the speaker uses animate.css) into the project, then target the ::view-transition-old and ::view-transition-new pseudo-elements with those animations. The default prop takes the animation name, but the speaker reports it did not work under Bun in their setup, so they used a different approach. *When:* The default fade is not the desired motion, and a custom CSS animation is wanted.
- **Animate page-to-page navigation** — Add <ViewTransition> to both the index page and the target page. Wrap the page-changing state update in startTransition in the navigation logic. *When:* Moving between views in a single-page app without a router that handles transitions.
- **Shared-element morph with the name prop** — Give the same name value to the matching element in the old and new states. Without a name, React assigns each element a unique name, so no morph happens. *When:* A thumbnail, card, or header should visibly move or resize into its detail view.
- **Animate Suspense boundaries** — Wrap Suspense content in <ViewTransition>, or place it inside the Suspense fallback prop, to animate the reveal of loaded content. *When:* Loading states should transition into content rather than swap instantly.

## Numbers
- The ViewTransition component exposes five props and four callbacks for customization (the speaker does not name most of them) ([2:14](https://youtu.be/6oL-skHq5Tk?t=134))
- The component was added to React early in 2025, with a blog post in March, and is available only in canary ([0:00](https://youtu.be/6oL-skHq5Tk?t=0))
- Video length is 4:19 ([0:00](https://youtu.be/6oL-skHq5Tk?t=0))

## Hot takes
- Feature is canary-only and the API may change, so it is not ready for production code.
- Recommends the built-in component only for new code, and suggests keeping React Router or Next.js view transitions for existing apps.
- Describes the feature as progressively enhanced, but gives no detail on fallback behavior.

## Tools mentioned
React (canary), react-dom (canary), Bun, animate.css, Next.js, React Router, Browser View Transitions API (document.startViewTransition)
