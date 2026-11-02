# TanStack Has A New Package (And Its Awesome)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `EdKTZ7WsaiY` · [watch](https://youtu.be/EdKTZ7WsaiY) · **date:** 2026-03-02 · **length:** 8:22 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host · **orgs:** TanStack, Better Stack
- **topics:** dev-tools · **tags:** tanstack, hotkeys, keyboard-shortcuts, react, cross-platform, type-safety, devtools, alpha, javascript

> A feature tour of TanStack Hotkeys, an alpha, type-safe, framework-agnostic keyboard-shortcut package for React and vanilla JS, covering cross-platform bindings, scoping, sequences, recording UI and DevTools.

## Summary
The host introduces TanStack Hotkeys, a new alpha package that handles keyboard-shortcut edge cases such as keyboard layouts, operating systems, conflicting hotkeys and scopes. The demo runs in a React app using the React package, with a vanilla JS package also available and other framework packages promised. The core hook registers a hotkey with a callback that gets the raw event and context, and the hotkey string is type-checked so invalid combinations raise a type error. Using a modifier key instead of Meta gives a cross-platform binding (Command on macOS, Control elsewhere), and an object form is offered as an alternative. Options control enabled state, keydown versus keyup, require-reset to stop auto-repeat, ignoring inputs, and scoping the hotkey to an element or ref instead of the whole document. Sequence hooks support multi-key chords with a per-key timeout, shown with GG and a joke sequence. Helper hooks report whether a key is held and which keys are currently held, and a recorder hook supports shortcut-customization UIs. Formatting helpers render shortcuts as platform icons or text labels, and the TanStack DevTools panel lists registered hotkeys, sequences, trigger counts, scope and options, with a manual trigger.

## Key ideas
- **Keyboard shortcuts are harder than they look: the package claims to handle layouts, OS differences, conflicting hotkeys and scopes, which the host says AI-written code often misses.** — Presented as a reason to use a library rather than hand-rolling; the host did not demonstrate the edge-case handling itself. The package is alpha and the host admits there may be bugs. ([0:00](https://youtu.be/EdKTZ7WsaiY?t=0))
- **Hotkey strings are type-checked, so an invalid key combination is a compile-time type error.** — The host shows that the valid combinations are autocompleted and that a mistyped combination is flagged. Using Meta+S as a Save example shows it maps to Command+S on macOS. ([1:11](https://youtu.be/EdKTZ7WsaiY?t=71))
- **Use the modifier key instead of Meta for cross-platform shortcuts.** — Meta is Command on macOS and does not exist on Windows, so a Meta+K binding silently breaks elsewhere. The modifier key resolves to Command on macOS and Control on other platforms. An object form (non-modifier key plus modifier flags) is equivalent. ([2:11](https://youtu.be/EdKTZ7WsaiY?t=131))
- **Hook options control repeat, input handling and scope.** — Options are enabled, event type (keydown or keyup), require reset (the hotkey must be released before it fires again), ignore inputs (suppresses it inside form fields), and target (document by default, or an element or React ref for a scoped hotkey). ([3:28](https://youtu.be/EdKTZ7WsaiY?t=208))
- **Multi-key sequences with a timeout between keys cover Vim-style navigation.** — The sequence hook takes a key sequence, a callback and options; the timeout is the maximum gap between keys. The demo binds GG to jump to the top of a list. ([4:32](https://youtu.be/EdKTZ7WsaiY?t=272))
- **Helper hooks expose key state and a recorder for user-customizable shortcuts.** — A key-hold hook returns a boolean for one key, and a held-keys hook returns the array of currently held keys. The recorder hook returns recording state, the recorded hotkey, and start and cancel functions, plus a callback to persist the chosen hotkey. It converts a recorded Command key into the modifier key so the saved binding stays cross-platform. ([5:39](https://youtu.be/EdKTZ7WsaiY?t=339))
- **Formatting helpers and DevTools cover display and debugging.** — formatForDisplay renders icons for the user's platform, formatWithLabels renders text labels. The DevTools panel shows registered hotkeys and sequences with trigger counts, keydown or keyup, scope, options, a manual trigger, and currently held keys. ([6:52](https://youtu.be/EdKTZ7WsaiY?t=412))

## Techniques
- **Cross-platform hotkey binding** — Write the hotkey with the modifier key rather than Meta (string form, e.g. modifier+K), or use the object form: the non-modifier key plus modifier set to true. The library resolves it to Command on macOS and Control elsewhere. Exact string spelling was not shown in the transcript. *When:* Any app that ships on more than one OS and binds a shortcut that uses the primary modifier.
- **Scoped hotkey via target** — Pass an element or React ref as the target option instead of the default document. The hotkey only fires while focus is inside that element. *When:* A shortcut should only work in one panel or widget, e.g. a command palette trigger that should not fire globally.
- **Avoid key-repeat re-triggering** — Set require reset to true so the hotkey must be released before it can fire again. *When:* Toggle-style actions (open a palette, toggle a panel) where holding the key should trigger once.
- **Allow shortcuts inside inputs** — Set ignore inputs to false. The default true suppresses hotkeys while the user is typing in a field. *When:* Global shortcuts that must still work when a text input has focus, such as save or open-palette.
- **Multi-key sequences** — Use the sequence hook with the key sequence string, a callback and a timeout (maximum gap between keys). Example from the demo: GG to jump to the top of a list. *When:* Vim-style navigation or chord shortcuts.
- **User-customizable shortcuts** — Use the recorder hook: call start to begin listening, read the recorded hotkey and recording state, and save the chosen hotkey in the recorder's success callback (the demo writes it to a palette-hotkey setting, which the host suggests persisting in the database). *When:* Settings screens where users rebind shortcuts.
- **Display shortcuts per platform** — Pass the hotkey to formatForDisplay for platform icons or formatWithLabels for text labels (e.g. Command vs Control). *When:* Showing shortcut hints in menus or tooltips that should match the user's OS.
- **Debug registrations with DevTools** — Open the TanStack DevTools panel to inspect registered hotkeys and sequences, trigger counts, scope, options, and held keys. Use the manual trigger to test a binding and press a key to read its exact value. *When:* Finding why a shortcut does not fire, or confirming the exact key name for a binding.

## Numbers
- Package is in alpha; no version number, benchmark or adoption figure is stated. ([0:00](https://youtu.be/EdKTZ7WsaiY?t=0))
- Sequence timeout is the per-key gap allowed between keys; no default value is stated. ([4:32](https://youtu.be/EdKTZ7WsaiY?t=272))

## Hot takes
- Title and intro lean on hype ('Awesome', 'think again' about AI, 'trust me, just use this package'); the edge-case claims are asserted, not demonstrated.
- Package is alpha and the presenter says it may have bugs, yet the pitch is 'use this or tell your AI agent'.
- Feature tour with no install commands, package names beyond the React and vanilla ones, or code shown beyond the demo, so it is not reproducible from the video alone.
- The video's own point that the modifier key beats hardcoding Meta is a useful, concrete cross-platform gotcha.

## Tools mentioned
TanStack Hotkeys (React package, alpha; vanilla JS package also available; other framework packages announced as coming), TanStack DevTools (hotkeys panel), React
