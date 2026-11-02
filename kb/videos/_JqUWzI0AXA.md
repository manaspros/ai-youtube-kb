# Build Your Own Shadcn/ui

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `_JqUWzI0AXA` · [watch](https://youtu.be/_JqUWzI0AXA) · **date:** 2025-11-02 · **length:** 7:19 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack, Supabase
- **topics:** dev-tools, vibe-coding-app-building · **tags:** shadcn, shadcn-cli, component-registry, code-distribution, registry-json, nextjs, react, v0, tweakcn, theming, react-aria

> Better Stack walkthrough of publishing your own components and blocks as a shadcn registry: registry.json, npx shadcn build, hosted JSON installed by URL, plus v0 and theme hooks.

## Summary
The video shows how to turn your own React components into a distributable shadcn/ui registry, so they can be installed with the shadcn CLI like built-in components. The speaker frames shadcn as a code distribution system rather than just a component library, and separates small "primitives" (UI pieces) from "blocks" (compositions that use them). The walkthrough is in a Next.js project: organize files under registry/<style>/ui and blocks, describe each shared item in a registry.json at the project root, and run npx shadcn build to generate one JSON file per item under public/r/. Hosting that JSON makes it installable with npx shadcn add <url> in any other project, and the CLI also installs npm dependencies such as React Aria Components. Blocks reference primitives through registryDependencies, which can mix shadcn component names with URLs to your own registry items. The video closes with two extensions: opening a registry item in v0 through a v0.dev link, and shipping custom CSS and variables so a theme installs with components (TweakCN is cited as an example). It is a short happy-path tutorial with no versioning, update flow, or private-registry auth covered.

## Key ideas
- **shadcn is positioned as a code distribution system, not only a component collection** — The speaker says shadcn now covers sharing and theming code (components, hooks, collections) and cites hooks, a Supabase UI collection and v0 output as examples of the same pattern. ([0:00](https://youtu.be/_JqUWzI0AXA?t=0))
- **Split shared code into primitives and blocks** — Primitives are small reusable pieces (card, avatar, toggle button, profile info) and a block is a composed unit built from them (a YouTube subscribe card). The analogy is Lego pieces versus a finished Lego set. ([0:00](https://youtu.be/_JqUWzI0AXA?t=0))
- **A registry.json entry describes each shared item** — Each item has a unique name, a type (registry:ui for primitives, registry:block for compositions), title, description, a files array (path and target type) and a dependencies array for npm packages. The type tells the CLI where the file lands in the consuming project. ([2:21](https://youtu.be/_JqUWzI0AXA?t=141))
- **The build step turns registry items into hostable JSON, and the URL is the distribution unit** — npx shadcn build writes one JSON file per item into public/r/ by default, and each JSON embeds the component source. The speaker says the JSON can be hosted anywhere, even GitHub. Installation is npx shadcn add with that URL. ([3:28](https://youtu.be/_JqUWzI0AXA?t=208))
- **Blocks depend on primitives through registryDependencies, which can point at your own registry** — A block lists dependencies by shadcn component name or by full URL to your own hosted item JSON. Rebuilding and adding the block URL installs the primitives it needs as well. ([4:53](https://youtu.be/_JqUWzI0AXA?t=293))
- **Registry items can open in v0 and carry themes** — A v0.dev link with the hosted registry JSON URL opens the component in a v0 chat for AI iteration; v0 cannot reach localhost, so the URL must be public. The registry can also ship custom CSS and variables, so a theme can be distributed alone, the pattern TweakCN uses. ([6:10](https://youtu.be/_JqUWzI0AXA?t=370))

## Techniques
- **Registry folder layout** — Create a registry/ folder at the project root, then a folder named for the style (the speaker used default; shadcn itself ships New York alongside default). Put primitives under registry/<style>/ui/ and compositions under registry/<style>/blocks/. The speaker says this structure is currently required and expects the next shadcn update to relax it. *When:* Before declaring any shared item, when you want a predictable layout the CLI build can read.
- **registry.json item entries** — At the project root, write registry.json with name, homepage and an items array. Each item has a unique name, type (registry:ui or registry:block), title, description, files: [{path, type}], and dependencies (npm packages). Example from the video: the toggle button item uses React Aria Components as a dependency, so the CLI installs it in consuming projects. *When:* For each component or block you want to distribute.
- **Build to hostable JSON** — Run npx shadcn build. Default output is public/r/<name>.json for each item. Change the output directory if the project is not Next.js or uses a different layout. Verify by visiting localhost:3000/r/<name>.json in dev. *When:* After every change to registry.json or the registry source files, and before publishing.
- **Install into another project** — Host the generated JSON (in the speaker's case, the Next.js public folder, served on deploy). Copy its full URL, then run npx shadcn add <url> in the consuming project. The CLI resolves the link, installs npm dependencies and writes the component files. *When:* Consuming a shared component from any project.
- **Compose a block from registry dependencies** — Give the block item type registry:block and add a registryDependencies array. List shadcn components by name (for example avatar, button) and your own items by their full hosted JSON URL. Rebuild, then run npx shadcn add with the block's URL. *When:* A composed UI reuses your own primitives and you want one install command to pull in the whole set.
- **Open a registry item in v0** — Build a v0.dev link and append the hosted registry JSON URL at the end, then place the link on a page (the speaker used an 'open in v0' button on his site). The hosted URL must be public because v0 cannot fetch localhost. *When:* You want users or collaborators to iterate on a shared component with AI inside v0.
- **Distribute a theme through the registry** — Add custom CSS and CSS variables to the registry item definition so they install with the component, or publish a theme-only item. The speaker cites TweakCN as a site that customizes a theme and then installs it with the CLI. *When:* You want shared styling or a whole theme to travel with components.

## Numbers
- Demo registry contents: 4 primitives (card, avatar, toggle button, profile info) plus 1 composed block (YouTube subscribe card). No benchmarks, costs or adoption stats are given. ([0:00](https://youtu.be/_JqUWzI0AXA?t=0))
- Build output: one JSON file per registry item in public/r/<name>.json by default, served at /r/<name>.json. ([3:28](https://youtu.be/_JqUWzI0AXA?t=208))

## Hot takes
- The speaker expects the registry folder-structure requirement to loosen in the next shadcn update (1:02).
- Shadcn is becoming a general code distribution platform for hooks, collections, Supabase UI and v0 output, not only components (0:00).
- Cursor can see the first registry item and write the remaining ones, so the pattern is easy to automate with AI (3:28).
- The hosted JSON is the real unit of distribution, and it can live anywhere, including GitHub (3:28).

## Tools mentioned
shadcn/ui CLI (npx shadcn build, npx shadcn add), Next.js, React Aria Components, v0 (v0.dev), TweakCN, Cursor (mentioned as writing the remaining primitives from the first one), Supabase UI (transcript says 'Superbase UI'; mentioned as a shadcn-style collection), GitHub (mentioned as a possible host for the JSON)

## Relevance to our work
- **agentos** (1/3): SkillForge aims to turn agent telemetry into governed, reusable skills, and this shows a build step that emits per-item JSON manifests with file lists and dependency edges that other projects install by URL. → *Use shadcn's registry.json item schema (name, type, files, dependencies, registryDependencies) as a template for a per-skill manifest in SkillForge, with dependent skills declared as URLs.*
