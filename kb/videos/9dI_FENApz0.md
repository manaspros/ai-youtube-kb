# Everything New in Nuxt 4 — Should You Switch?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `9dI_FENApz0` · [watch](https://youtu.be/9dI_FENApz0) · **date:** 2025-11-02 · **length:** 5:21 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** Bernard · **orgs:** Better Stack, Nuxt, Vercel
- **topics:** dev-tools · **tags:** nuxt, nuxt-4, nuxt-3, vue, typescript, tsconfig, migration, hmr, data-fetching, frontend

> Better Stack's 5-minute walkthrough of Nuxt 4: the new app/ directory layout, shared data-fetch keys, a references-based tsconfig, the upgrade steps, and one module incompatibility.

## Summary
The speaker (Bernard) argues Nuxt 4 is worth upgrading to and walks through what changed. The CLI onboarding is leaner, and modules are now opt-in during setup rather than through a long question list. The biggest change is that application code moves into an app/ directory, with server/ and shared/ staying in the root; the speaker says this also speeds up development because the dev server only watches the app/ folders. Data fetching gets consistency rules: useFetch and useAsyncData calls that share an explicit key share one data reference, so conflicting options such as deep trigger a warning. TypeScript moves to a single tsconfig that uses references, with paths for app, server, shared and node contexts. The migration is an upgrade command, updating tsconfig references, and optionally moving files into app/. The speaker closes by noting that some modules are still incompatible, with Nuxt Apollo disabled as an example. The video is a feature overview with a short migration section and no benchmarks.

## Key ideas
- **Nuxt 4 CLI onboarding is leaner: it asks whether to install modules instead of a long list of questions.** — The speaker likes Nuxt modules and installs them all in the demo project. ([0:00](https://youtu.be/9dI_FENApz0?t=0))
- **Application code moves into an app/ directory (app.vue, assets, components, composables and so on); server/ and shared/ stay in the root.** — This mirrors the Next.js layout. It is also performance-driven: during development Nuxt only watches the app/ folders, which the speaker says means faster HMR and less CPU use. The new layout is optional, and Nuxt 4 still supports the old one. ([1:07](https://youtu.be/9dI_FENApz0?t=67))
- **Data fetching is about consistency: calls that share an explicit key share the same data reference.** — The smarter data fetching itself shipped in Nuxt 3, so Nuxt 3 users likely already have it. In Nuxt 4, calls with the same key and conflicting options (the speaker's example uses deep) produce a warning, because Nuxt cannot tell which version to trust. ([1:59](https://youtu.be/9dI_FENApz0?t=119))
- **A single tsconfig with references replaces the separate server tsconfig, covering app, server and shared code.** — The speaker says this should give better autocompletion and fewer confusing errors across contexts, which are listed as app, server, shared and node paths. ([1:59](https://youtu.be/9dI_FENApz0?t=119))
- **Upgrading a Nuxt 3 project is mostly mechanical, and import errors after the upgrade are expected.** — After upgrading, the fix is updating tsconfig to the references form. If the generated types are missing, running the post-install script creates them. The app/ move is optional on top of that. ([3:10](https://youtu.be/9dI_FENApz0?t=190))
- **Not everything is compatible yet. The Nuxt Apollo module was disabled for this project.** — This is the speaker's only reported caveat, and the video does not say when or whether it will be fixed. ([4:15](https://youtu.be/9dI_FENApz0?t=255))

## Techniques
- **Upgrade a Nuxt 3 app to Nuxt 4** — Run `npx nuxt upgrade --dedupe` (the auto-caption reads 'ddup'; the flag is the dedupe option). Then update tsconfig.json to the references-based config from the Nuxt docs; the referenced files live in the generated .nuxt folder. If those types are missing, run the post-install script to generate them. The import errors that follow the upgrade are expected. *When:* Migrating an existing Nuxt 3 project. Check module compatibility first, since some modules (the speaker cites Nuxt Apollo) may be disabled.
- **Move app code into app/** — Create an app/ folder and move app.vue, assets, components, composables and the other directories listed in the Nuxt 4 docs into it. server/ and shared/ stay in the root. *When:* Optional, as a second step after the upgrade. Worth doing for faster HMR and less watcher CPU, or for a cleaner layout as the app grows.
- **Give shared fetch calls explicit keys with matching options** — Use an explicit key with useFetch or useAsyncData. Calls that share a key share one data reference, so every call with the same key must use the same options such as deep. Otherwise Nuxt 4 logs a warning. *When:* Several components fetch the same data, or any call uses an explicit key.

## Hot takes
- The speaker says 'you should' switch to Nuxt 4 because 'it's really good', which is an opinion based on one migrated project.
- The app/ move is said to be performance-driven (faster HMR, less CPU), but no measurements are shown.
- On why the layout matches Next.js, the speaker says 'maybe it's just a coincidence' after mentioning that Nuxt joined Vercel.
- Auto-captions render 'Nuxt' as 'Noxt' throughout.

## Tools mentioned
Nuxt 4, Nuxt 3, Nuxt CLI (npx nuxt upgrade), TypeScript, tsconfig references, Next.js (referenced as the layout the change resembles), Nuxt Apollo module (disabled, incompatible), Nuxt modules
