# Bolt.new Tutorial Website – Replaces Cursor, Claude & v0 – The Only AI Tool You Need!

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `6-sTKmPl4wA` · [watch](https://youtu.be/6-sTKmPl4wA) · **date:** 2024-11-02 · **length:** 7:33 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** ?
- **topics:** vibe-coding-app-building, coding-agents · **tags:** bolt.new, website generation, chat-driven iteration, error copy-back, vague vs specific prompts, credits and pricing, react, v0 comparison, cursor comparison

> A 7-minute walkthrough of Bolt.new, a browser tool that generates a React website from a text prompt, then iterates on it through chat; the transcript shows real friction (vague prompts, missing images, out-of-credits).

## Summary
The speaker presents Bolt.new as a browser-based AI builder that combines the ideas of V0 and Cursor, with a chat-style prompt box, a visible code editor, a built-in terminal and a live preview. They build a bakery website from one prompt; the tool writes React code, starts the dev server itself and shows the preview. Follow-up requests in chat fix broken buttons, add About and Contact sections, and add a confetti effect on a button. A vague request ("a cool effect on the button") missed, and a specific one (confetti) worked. Missing images needed several rounds of prompting, and a build error was fixed by pasting it back into the tool until free credits ran out. The speaker then fixed the error by hand and ends by recommending the $9 Pro tier. The video is a single-user demo with no benchmarks, no failure-rate data and no comparison beyond the speaker's opinion.

## Key ideas
- **Bolt.new is pitched as V0 and Cursor combined: a chat prompt produces a full-stack app in the browser.** — The speaker says the tool is like V0 and Cursor together 'on steroids', and that a non-engineer can get a deployable app from English alone. The only app shown is a React bakery site. ([0:00](https://youtu.be/6-sTKmPl4wA?t=0))
- **The tool shows its work: code is written in a visible editor, and it starts the React dev server and a preview itself.** — It has its own terminal and runs the install and start commands automatically. The speaker compares the terminal to Replit's. ([0:00](https://youtu.be/6-sTKmPl4wA?t=0))
- **Iteration happens by chat, and the tool locates the files to change itself.** — A follow-up asking to fix non-working buttons made it edit the relevant files. It also added About and Contact sections that matched the existing styling. ([1:46](https://youtu.be/6-sTKmPl4wA?t=106))
- **Vague requests miss; specific ones land.** — 'Add a cool little effect on the button' did not match what the speaker wanted. A request naming a confetti effect worked, and the tool gave the command to restart the dev server after the speaker stopped it while viewing the code tab. ([3:29](https://youtu.be/6-sTKmPl4wA?t=209))
- **Errors are fed back to the tool as text, but the loop depends on credits.** — The speaker copied a build error into the chat. The tool stopped working when free credits ran out, and the speaker fixed the error by hand. ([5:52](https://youtu.be/6-sTKmPl4wA?t=352))

## Techniques
- **One-prompt scaffold, then chat-driven iteration** — Describe the whole site in one prompt (business type plus extra details). Let the tool generate and run the app, then request changes one at a time in the same chat, checking the live preview after each change. *When:* Early prototyping of a static or simple React marketing site, where the goal is a visual first draft and not a maintained codebase.
- **Name the exact effect or fix instead of describing a mood** — Replace open-ended wording ('add a cool effect') with a named effect ('add a confetti effect on click'). Ask for one change per message so a failure is easy to isolate. *When:* Whenever a generated change misses; the speaker's confetti retry worked after the vague request did not.
- **Copy build errors back into the chat** — When the dev server or build fails, copy the error text from the terminal into the chat and ask for a fix. Re-run the dev server if the tool's stop or restart steps are needed. *When:* The speaker used this for a build error. It only works while the tool still has credits, and the speaker had to fix the error manually once they ran out.
- **Check generated assets and sections by eye** — After each generation, open the preview and check images, navigation and sections. Re-prompt for missing images; the speaker needed several rounds to get all of them to load. *When:* Generated sites often reference images that do not exist. Check every one before accepting the output.

## Numbers
- Pro plan price stated as $9 (monthly), described by the speaker as enough for most people. ([5:52](https://youtu.be/6-sTKmPl4wA?t=352))
- Free credits ran out during the demo, which ended the AI-assisted fix loop. ([5:52](https://youtu.be/6-sTKmPl4wA?t=352))
- The demo is one site built in one session of about 7.5 minutes; no benchmarks, timings or success rates are reported. ([0:00](https://youtu.be/6-sTKmPl4wA?t=0))

## Hot takes
- Speaker claims anyone can become a software engineer by knowing English and that an app built this way could earn millions; the video does not support either claim.
- Title says 'the only AI tool you need' and 'replaces Cursor, Claude and V0'; the video does not compare Bolt.new against those tools.
- Speaker says the AI 'could have fixed it itself' if credits had lasted, which the transcript does not show.

## Tools mentioned
Bolt.new, React, V0, Cursor, Replit (comparison only), Claude (UI resemblance only)
