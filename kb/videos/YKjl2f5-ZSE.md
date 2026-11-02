# This Keyboard Tool is BETTER Than Karabiner (Here's Why)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `YKjl2f5-ZSE` · [watch](https://youtu.be/YKjl2f5-ZSE) · **date:** 2026-02-02 · **length:** 4:40 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** kanata, keyboard-remapping, home-row-mods, karabiner-elements, macos, rust, s-expression-config, sketchybar, qmk, tap-hold

> Kanata, an open-source Rust keyboard remapper, adds tap-hold, layers and home-row mods at the software level. The speaker prefers it to Karabiner Elements for home-row mods, despite its Lisp-style config and some gaps.

## Summary
Better Stack presents Kanata, an open-source software-level keyboard remapper written in Rust, as a QMK-like tool that works with any keyboard, including laptop keyboards. The speaker explains its S-expression configuration, which is unusual because function names sit inside the parentheses and nesting is common. A basic remap defines source keys with def src and output keys inside a def layer, and unlisted keys pass through unchanged. Further features include tap-hold with a timeout, def var variables referenced with a dollar sign for home-row mods, extra named layers such as an editor layer, and a TCP server that lets other apps such as SketchyBar react to layer changes. The speaker's main argument is that Kanata's tap-hold handling works out of the box, while Karabiner Elements' tap-hold often registered holds as taps for him. The downsides he names are one config file per keyboard, which means running a command when switching keyboards, no way to remap the play/pause key to F8 that he found, and some friction with an MX Master mouse. He says he worked around these by vibe coding solutions, and he asks viewers to share the video because Kanata's community is small.

## Key ideas
- **Kanata is a software-level remapper, similar to QMK but working on any keyboard, including a laptop's built-in one.** — Written in Rust, so the speaker says it is fast with no noticeable typing delay. He presents it as an alternative to Karabiner Elements. ([0:00](https://youtu.be/YKjl2f5-ZSE?t=0))
- **The config syntax is an unusual Lisp-style S-expression format, and it takes time to get used to.** — Function names sit inside the parentheses next to their arguments, so nesting reads oddly. The speaker says he now cannot imagine using a keyboard any other way. ([0:55](https://youtu.be/YKjl2f5-ZSE?t=55))
- **Unlisted keys behave normally, so a remap only needs entries for the keys it changes.** — Whitespace and tabs are insignificant, so the file can be spaced out for readability. Example: def src with a, and a def layer named base with x. ([1:53](https://youtu.be/YKjl2f5-ZSE?t=113))
- **Tap-hold and home-row mods are the main reason he prefers Kanata.** — He says Karabiner's tap-hold, used for home-row mods, took a lot of research and configuration and still often registered holds as taps. Kanata handled it correctly out of the box. ([2:54](https://youtu.be/YKjl2f5-ZSE?t=174))
- **A TCP server lets external apps react to Kanata events such as layer changes.** — He connects SketchyBar so the current layer appears at the top of the desktop. Kanata's features also include named layers, such as an editor layer for video editing, and a layer-switch key. ([2:54](https://youtu.be/YKjl2f5-ZSE?t=174))
- **Kanata's limitations are per-keyboard configs and missing remaps.** — Different keymaps need different config files, so switching keyboards means running a command. He could not remap play/pause to F8 in Kanata, which he could do in Karabiner, and the MX Master mouse needed tweaks. He suggests the community is small. ([4:09](https://youtu.be/YKjl2f5-ZSE?t=249))

## Techniques
- **Basic key remap with def src and def layer** — Declare the source keys with a def src form, then declare an output layer with def layer and a name (e.g. base) listing the output keys in the same order, for example mapping a to x. Keys not listed in the file pass through unchanged. The speaker says whitespace is insignificant, so the lists can be aligned for readability. *When:* Any simple remap, or as the starting point before adding taps, holds and layers.
- **Tap-hold for one key** — Configure a tap-hold action with a tap-hold timeout, then add the output for a tap and the output for a hold. In the example, tapping a registers x and holding a registers left shift. *When:* Dual-role keys, such as a key that types a letter on tap and acts as a modifier on hold.
- **Home-row mods via def var** — Define the repeated home-row mappings once with def var, then reference them with a dollar sign inside the layer definitions. The speaker maps the home keys to the four common modifiers. *When:* Home-row mods, where the same modifier mappings would otherwise be repeated across many keys.
- **Extra named layers with a layer-switch key** — Add another def layer with its own name, for example editor, that gets a separate set of key maps. Bind a layer-switch key to move into that layer. *When:* Context-specific keymaps, such as a separate layer for video editing.
- **External integration through the TCP server** — Enable Kanata's TCP server so other applications can listen to events. The speaker's example is SketchyBar, which displays the active layer at the top of the desktop when the layer changes. *When:* Showing the current layer or other remapper state in a status bar or other tool.

## Hot takes
- Kanata handles home-row mods (tap-hold) better out of the box than Karabiner Elements, which he says often registered holds as taps for him. This is one user's experience, not a benchmark.
- The S-expression config is the weirdest syntax he has seen, but he says it is easy to get used to and AI can help write it.
- Kanata's community is too small, and he hopes the video helps grow it.

## Tools mentioned
Kanata, Karabiner Elements, Karabiner for Mac, QMK, SketchyBar, MX Master (mouse), Rust
