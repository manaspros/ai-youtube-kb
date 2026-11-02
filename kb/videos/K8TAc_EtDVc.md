# You Don't Need React Portals For Modals Anymore (react-call)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `K8TAc_EtDVc` · [watch](https://youtu.be/K8TAc_EtDVc) · **date:** 2026-07-02 · **length:** 6:01 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus (Better Stack host) · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** react, react-call, modals, dialogs, promises, ui-state, hot-module-replacement, frontend

> Better Stack walkthrough of react-call, a small library that lets you await React modals and dialogs like async functions, with upsert for singleton UI and useMutationFlow for async confirms.

## Summary
The host introduces react-call, a lightweight React utility that lets you call a component like an async function and await its result, similar to window.confirm. The pitch is that this removes the usual open-state booleans, onClose/onSubmit props, context providers and portals for modals, wizards and item pickers. The library is described as having three concepts: a root-and-stack model where a callable component is mounted once and manages multiple active instances, an upsert call that updates a single existing instance instead of stacking duplicates (for toasts, loading overlays and progress indicators), and a useMutationFlow hook that keeps a modal open with a spinner until an async backend call resolves. The walkthrough of the examples is mostly narration of the library's website, with a confirm-dialog example wrapped in a createCallable higher-order component. No install commands, versions, or code are shown on screen. The host concedes that a basic promise-wrapped modal could be hand-coded, and argues the library's value is in handling the edge cases.

## Key ideas
- **react-call lets you call a React component like an async function and await its result, like window.confirm but with a custom UI.** — The caller's logic stays local and linear: no isOpen state, no onClose or onSubmit props, no context providers or portals. ([0:00](https://youtu.be/K8TAc_EtDVc?t=0))
- **The callable component is a root mounting point placed once in the tree, not a plain function.** — Place it in the app or a high-level layout file; it listens for calls, keeps multiple active instances isolated, and handles exit animations through an internal stack. ([1:09](https://youtu.be/K8TAc_EtDVc?t=69))
- **upsert is the singleton pattern: if an instance is already open, it updates that instance instead of pushing a duplicate.** — Intended for global toasts, loading overlays and progress indicators where only one should be on screen. ([2:33](https://youtu.be/K8TAc_EtDVc?t=153))
- **useMutationFlow ties a callable modal to an async mutation.** — The modal stays open with a loading spinner while the async function runs and only ends the call when the promise resolves. ([2:33](https://youtu.be/K8TAc_EtDVc?t=153))
- **The confirm-dialog example uses a createCallable higher-order component and is invoked asynchronously from a click handler.** — The host says the setup needs no context, state variables, or Redux. The website's example section includes code snippets for each use case. ([3:42](https://youtu.be/K8TAc_EtDVc?t=222))
- **The host concedes a basic promise-wrapped modal is easy to hand-code, and argues the library's value is in edge cases: stacking, singleton updates, and syncing UI with backend mutations.** — This is a self-assessment in the video, not a benchmark or measured result. ([4:42](https://youtu.be/K8TAc_EtDVc?t=282))

## Techniques
- **Awaitable modal via createCallable HOC** — Wrap the dialog component with createCallable, mount the wrapped component once at the app root, then call it with await from an event handler (for example, const ok = await confirmDelete(); if ok, proceed). The return value is the user's choice. The exact import names and signatures are not shown in the transcript; check the react-call docs. *When:* Confirmation dialogs, multi-step form wizards, and item pickers, where a caller needs a result inline instead of managing open state and callbacks.
- **Upsert for singleton UI** — Use the upsert call instead of call when only one instance should exist. If one is already open, it is updated with new props in place. *When:* Global toasts, loading overlays, and progress indicators that should update rather than stack.
- **useMutationFlow for confirm-then-mutate** — Inside the callable confirm component, use the useMutationFlow hook around the async submit so the modal shows a spinner and only closes once the promise resolves. The transcript does not show the hook's signature. *When:* A confirmation modal that triggers a backend write, such as a delete or save, where closing early would hide failures.

## Hot takes
- The walkthrough mostly reads the library's website examples. No code, install command, or version is shown on screen, so the video does not show how to get the pattern working.
- The host admits a basic promise-wrapped modal could be hand-written, so the case for the library rests on stacking, singleton upsert, and mutation-flow edge cases that are asserted, not demonstrated.
- Quality is capped at 2 for thin substance: a 6-minute feature tour with no runnable example and no sponsorship.

## Tools mentioned
react-call, React, window.confirm (referenced as the mental model, not used)
