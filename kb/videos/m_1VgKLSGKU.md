# React Scan - My New Favorite Debugging Tool

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `m_1VgKLSGKU` · [watch](https://youtu.be/m_1VgKLSGKU) · **date:** 2025-11-02 · **length:** 10:14 · **format:** tutorial · **quality:** 2/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Million, Better Stack
- **topics:** dev-tools · **tags:** react, performance, re-renders, memoization, useMemo, useCallback, React.memo, state colocation, debugging, frontend

> Better Stack walkthrough of React Scan, a free Million tool that highlights unnecessary React re-renders and shows why, then fixes them with useMemo, useCallback, React.memo and state colocation. Not AI-related.

## Summary
The video introduces React Scan, a free debugging tool from Million that highlights components re-rendering on the page and can show the cause via an inspect-element view. The presenter adds it to a demo app with a script tag and walks through a set of deliberately bad re-render patterns. The first fix is useMemo for an expensive computed value, which helps only partly because the parent recreates the theme object on every render. Wrapping the child in React.memo, then useCallback for a handler prop and useMemo for a static array, removes the remaining re-renders. The presenter's main advice is to optimize only where there is a measured slowdown and to first restructure state, moving the counter into its own component so only that subtree re-renders. He also mentions state managers such as Redux or Zustand and a React Compiler that he presents as future work. The content is general React performance advice rather than AI engineering.

## Key ideas
- **React Scan is a free tool from Million that highlights re-rendering components on the page and can show the cause of each re-render.** — It can be added by a script tag copied from the project's GitHub README, via npm or its CLI, or as a browser extension. The presenter uses the script-tag method and turns on its demo view to see highlighted boxes. An optional sound plays per re-render. ([0:00](https://youtu.be/m_1VgKLSGKU?t=0))
- **The inspect-element view names the prop that changed, which points to the real cause.** — In the demo the UserProfile component re-renders because its theme prop is always treated as changing. The tool also flags that the component is slow, with about six seconds of render time shown. ([1:08](https://youtu.be/m_1VgKLSGKU?t=68))
- **useMemo fixes an expensive computation but not the re-render itself.** — Wrapping the costly computed value in useMemo with theme as the dependency stops recalculation, but the component still re-renders because the parent gives it a new theme object. ([2:25](https://youtu.be/m_1VgKLSGKU?t=145))
- **Parent re-renders recreate objects, so identity-based prop checks fail even when the content is the same.** — The presenter says React re-renders components because state changes, not props. A state change in App recreates the theme object, so the presenter memoizes it with useMemo. ([3:30](https://youtu.be/m_1VgKLSGKU?t=210))
- **React.memo stops a child re-render when its props are unchanged.** — Wrapping UserProfile in memo tells React to skip the re-render unless its props change, so the expensive path no longer runs on each counter increment. ([4:29](https://youtu.be/m_1VgKLSGKU?t=269))
- **useCallback keeps a handler prop's identity stable across parent renders.** — The handleBigIncrement function is recreated on each App render, which breaks memo on the child. Wrapping it in useCallback, and using the functional form of the state setter so it has no dependencies, fixes this. ([5:42](https://youtu.be/m_1VgKLSGKU?t=342))
- **Static arrays passed as props also need memoizing, and the presenter uses an empty dependency array for a fixed list.** — The usernames list is a module-level array, but the component still sees a new array on each App render. useMemo with [] keeps one reference. ([6:56](https://youtu.be/m_1VgKLSGKU?t=416))
- **Before adding memoization, move state down into the component that uses it.** — Moving count into a CounterSection component means only that subtree re-renders on increment. The presenter avoids memoizing the small child at all. He says optimizing re-renders usually wastes time when the gains are small. ([7:53](https://youtu.be/m_1VgKLSGKU?t=473))
- **Use a state manager or the React Compiler when state scoping is not enough.** — The presenter suggests Redux or Zustand to limit re-renders to the components that read the changed state. He says the React Compiler will auto-memoize code in the future, so manual hooks may rarely be needed. ([9:03](https://youtu.be/m_1VgKLSGKU?t=543))

## Techniques
- **Find re-renders with React Scan** — Add React Scan to index.html by copying its script tag from the project's GitHub README, or install it through npm, its CLI, or the browser extension. Turn on the demo view or interact with the page to see re-rendering components highlighted. Use the inspect-element tool on a component to see which prop changed. *When:* When a React page lags, drops FPS, or re-renders more than expected. Use it to find the real hotspot before optimizing.
- **Memoize an expensive derived value with useMemo** — Wrap the costly computation in useMemo(() => compute(...), [dependencies]), where the dependency array lists only the inputs that affect the result, such as theme. *When:* When a computed value is costly and depends on a small set of inputs that change rarely.
- **Stabilize object and array props passed from a parent** — Wrap object or array literals passed as props in useMemo. Use the relevant values as dependencies, or [] for a constant list. *When:* When the child is memoized, or when the child's cost depends on the prop's identity rather than its content.
- **Skip child re-renders with React.memo** — Wrap the child component in memo(Component). Re-renders then happen only when its props change by reference. *When:* When a child is expensive and gets the same props while the parent re-renders for unrelated state.
- **Stabilize handler props with useCallback and functional state updates** — Wrap the handler in useCallback. Use setCount(c => c + 1) instead of reading count, so the dependency array can be empty. *When:* When a memoized child receives a function prop that is recreated on each parent render.
- **Move state down before memoizing** — Put state into the smallest component that needs it, such as a CounterSection that owns count and renders the counter UI. Siblings and unrelated subtrees then stop re-rendering without any memo hooks. *When:* First step when re-renders come from state high in the tree. Prefer it over memo hooks.
- **Use a state manager for shared state** — Move the shared state into Redux or Zustand so only components that subscribe to the changed slice re-render. The presenter does not show a setup. *When:* When state is shared across distant components and colocation is no longer enough.

## Numbers
- The demo's expensive UserProfile component shows about 6 seconds of render time before the fix. ([1:08](https://youtu.be/m_1VgKLSGKU?t=68))
- The presenter describes the demo's FPS as dropping massively when the button is held down, with no figure given. ([1:08](https://youtu.be/m_1VgKLSGKU?t=68))
- The video claims React Scan makes finding and fixing these issues 'a hundred times easier'. No measurement is shown. ([0:08](https://youtu.be/m_1VgKLSGKU?t=8))

## Hot takes
- Off-topic for an AI engineering KB. The content is general React performance advice and a promotion of one vendor's free tool.
- The 'hundred times easier' claim is unsupported hype. The video shows no measurements beyond one demo component's render time.
- Good practical advice in the video: do not memoize everything, and move state down before adding memo hooks.

## Tools mentioned
React Scan, React, React.memo, useMemo, useCallback, Redux, Zustand, React Compiler, Million
