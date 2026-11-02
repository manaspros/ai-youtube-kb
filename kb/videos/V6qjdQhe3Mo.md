# This Single Line of Code Saves 440GB a WEEK

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `V6qjdQhe3Mo` · [watch](https://youtu.be/V6qjdQhe3Mo) · **date:** 2025-11-02 · **length:** 4:01 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, npm, E18E (Ecosystem Performance Initiative)
- **topics:** dev-tools · **tags:** npm, javascript, dependencies, micro-packages, supply-chain, left-pad, polyfill-io, bandwidth, eslint

> A one-line PR that inlined a micro-package cut about 440 GB/week of npm bandwidth, and the video uses it to argue about micro-libraries, supply-chain risk and copy-paste versus dependencies.

## Summary
The video starts from a pull request to the to-regex-range npm package that replaced the is-number dependency with an inline copy of its code. The speaker says the change cut npm download bandwidth by about 440 GB a week, because the code itself is under 1 KB while an installed package is about 10 KB with its README, license and package.json. The PR thread turned heated, and the merged change also removed the dependency from chokidar, which the speaker says saved a further 2.5 TB a week. The speaker then looks at the maintainer behind is-number, who has over 1,500 npm packages. The pro side of the micro-library debate is that JavaScript has no standard library and micro-packages come with thorough tests and fixes, while the con side is left-pad (2016) and the polyfill.io compromise. The recommended middle ground is to copy the small function into your codebase or use a native check such as typeof, which the speaker says covers about 90% of cases. The video closes by pointing to the E18E ecosystem initiative and its eslint-plugin-depend tool for finding redundant dependencies.

## Key ideas
- **One inlined micro-dependency saved a large amount of npm bandwidth** — A PR to to-regex-range replaced the is-number dependency with an inline copy. The speaker attributes roughly 440 GB/week of npm bandwidth saving to it, given about 70 million weekly downloads. ([0:00](https://youtu.be/V6qjdQhe3Mo?t=0))
- **Installed size is much larger than the code itself** — The function code is under 1 KB, but downloading the package brings about 10 KB because of the README, license and package.json. Across millions of installs this adds up. ([0:00](https://youtu.be/V6qjdQhe3Mo?t=0))
- **Removing the dependency had knock-on effects** — The speaker says chokidar also dropped the dependency as a result, which the speaker estimates saved a further 2.5 TB/week. ([0:00](https://youtu.be/V6qjdQhe3Mo?t=0))
- **Micro-library defenders have a real argument** — JavaScript has no standard library, so micro-packages save development time. They often ship with extensive tests; the speaker cites 111 tests for is-number, which is at major version 7. ([1:11](https://youtu.be/V6qjdQhe3Mo?t=71))
- **Micro-packages carry real fragility and security risk** — The left-pad incident (2016) broke thousands of builds when one tiny package was removed. Each package is another thing to audit, monitor and possibly compromise, illustrated by the polyfill.io domain being acquired and used to redirect mobile users to phishing sites. ([2:31](https://youtu.be/V6qjdQhe3Mo?t=151))
- **Copy the function in, or use a native check** — Pasting the small function into your codebase keeps you in control and lets you modify it. Often a native check like typeof === 'number' is enough, and you can assess whether edge cases matter for your app. The speaker adds that AI IDEs can now write such helpers on demand. ([2:31](https://youtu.be/V6qjdQhe3Mo?t=151))
- **Ecosystem-level cleanup efforts exist** — The E18E (Ecosystem Performance Initiative) works on removing redundant dependencies and modernising necessary ones. It publishes a blog and tools such as eslint-plugin-depend to find and replace unnecessary packages. ([3:57](https://youtu.be/V6qjdQhe3Mo?t=237))

## Techniques
- **Inline a tiny dependency** — Copy the function's source into your own module, keep its license/attribution, and delete the package from package.json. Cuts install size and removes one supply-chain surface. *When:* The dependency is a one-liner or a few lines of logic, and you do not need its edge-case handling.
- **Replace with a native check** — Use built-in language checks in place of the package. The speaker's example is typeof x === 'number' in place of is-number, then decide whether the remaining edge cases matter. *When:* The package only covers common cases your app actually hits, so the edge cases do not apply.
- **Find redundant dependencies with eslint-plugin-depend** — Run the ESLint plugin the speaker names (eslint-plugin-depend) over the project to flag unnecessary or replaceable packages. The video does not show the config. *When:* You want a systematic audit of a Node project's dependency list rather than a manual review.

## Numbers
- About 440 GB/week of npm download bandwidth saved by the inlining PR ([0:00](https://youtu.be/V6qjdQhe3Mo?t=0))
- Code is under 1 KB; installed package is about 10 KB ([0:00](https://youtu.be/V6qjdQhe3Mo?t=0))
- About 70 million npm downloads per week for the affected package ([0:00](https://youtu.be/V6qjdQhe3Mo?t=0))
- Knock-on saving of about 2.5 TB/week, attributed to chokidar also dropping the dependency (speaker's figure) ([0:00](https://youtu.be/V6qjdQhe3Mo?t=0))
- is-number has 111 tests and is at version 7 ([1:11](https://youtu.be/V6qjdQhe3Mo?t=71))
- Maintainer has over 1,500 npm packages attributed to them ([1:11](https://youtu.be/V6qjdQhe3Mo?t=71))
- typeof-style native check said to cover about 90% of cases (speaker's estimate) ([2:31](https://youtu.be/V6qjdQhe3Mo?t=151))

## Hot takes
- Copy-pasting small functions into your code is presented as a better default than adding a micro-package, with AI IDEs making that easier.
- The title's 440 GB/week figure is a bandwidth estimate for one PR; the rest is a light commentary on a public argument. Hype title with thin practitioner substance, so quality is capped at 2.
- The speaker points out that the PR code was the maintainer's own, just moved inline, and frames the dispute as a question of code attribution.
- Caveat: the copy-paste advice trades a versioned, audited dependency for unmanaged copied code, which the video mentions only briefly.

## Tools mentioned
npm, to-regex-range, is-number (v7 per the video), chokidar, isOdd, isEven, ansi-colors, left-pad, polyfill.io, eslint-plugin-depend, E18E (Ecosystem Performance Initiative)

## Relevance to our work
- **agentos** (1/3): AgentOS is a multi-package stack, so dependency footprint and supply-chain exposure matter; the video's micro-package argument is only tangentially related to AgentOS's core work. → *Audit the AgentOS dependency trees (npm and Python) for one-line or trivially replaceable packages, and check whether they are pinned in lockfiles.*
