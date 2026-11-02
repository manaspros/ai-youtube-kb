# I Found the BEST UI Library

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `aQB0B3a1fh8` · [watch](https://youtu.be/aQB0B3a1fh8) · **date:** 2025-11-02 · **length:** 5:43 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** 21st.dev, shadcn, Aceternity, Origin UI, Magic UI, Lovable, Bolt.new
- **topics:** vibe-coding-app-building, dev-tools · **tags:** shadcn, react, tailwind-css, ui-components, component-registry, copy-prompt, v0, nextjs, landing-pages

> A 5-minute tour of 21st.dev, a catalog of shadcn-style React component collections, showing how to install a component with the shadcn CLI or paste a copy-prompt into an AI editor to adapt it.

## Summary
The video presents 21st.dev as an aggregator of shadcn-style React component libraries such as Aceternity, Origin UI and Magic UI, covering landing-page effects, core UI components and marketing blocks. Components are sourced from the shadcn registry, so the speaker shows two ways to get one: run the install command with the shadcn CLI, or copy the code manually. He installs a commit-grid component into a Next.js project, where it lands in components/ui, and describes the result as code the team owns and can edit. The copy-prompt button is the second workflow: it produces a prompt tailored to an AI editor (v0, Lovable, Bolt.new or a generic one) that tells the model to place the component in components/ui and extend the Tailwind config. He pastes that prompt into v0, gets a preview, then asks for small changes (red highlight, different text) to show iterative AI editing. The video is a product showcase with no caveats on licensing, maintenance or accessibility, and the speaker notes that one of his own shadcn spin-offs was added to the site.

## Key ideas
- **21st.dev acts as a catalog over many shadcn-style community component libraries (Aceternity, Origin UI, Magic UI and others), so you browse one site instead of many.** — The speaker calls it a collection of collections. Covers landing-page effects (3D scenes, background lights, tube-light sidebars, cursor splash effects), core components and marketing blocks (heroes, footers, pricing cards, comparisons). ([0:00](https://youtu.be/aQB0B3a1fh8?t=0))
- **Components come from the shadcn registry, so each one can be installed with the shadcn CLI or copied by hand, and the source is visible for learning how an effect is built.** — The speaker opens a component's code to show how the effect is done, then either copies the install command or copies the code manually. ([1:11](https://youtu.be/aQB0B3a1fh8?t=71))
- **The catalog doubles as a reference for how modern sites are built: find a component similar to what you want, then read its source.** — Speaker suggests searching for the effect on a site you admire. Also mentions that a spin-off of his own shadcn-style library was added to the site. ([2:09](https://youtu.be/aQB0B3a1fh8?t=129))
- **After install the component is local source in components/ui, so it is owned by the project and can be edited directly.** — Speaker installs a commit-grid component into a Next.js project, adds it to a landing page, and then changes its highlight colour and corner radius by hand. He says 'we own this code now'. ([3:16](https://youtu.be/aQB0B3a1fh8?t=196))
- **The copy-prompt button writes a prompt tailored to a specific AI editor (v0, Lovable, Bolt.new or a generic one) that carries the component code plus the Tailwind config it needs.** — The prompt instructs the model to copy the component into components/ui and extend the existing Tailwind config with the included styles. Pasting it into v0 produced a working preview. ([4:13](https://youtu.be/aQB0B3a1fh8?t=253))
- **The speaker's recommended workflow is find a base component, paste it in, then refine it with AI prompts.** — He asks v0 to change the highlight to red and the text to 'yay' and reports the result as a satisfactory preview. He does not discuss failure cases or how many iterations it took. ([5:06](https://youtu.be/aQB0B3a1fh8?t=306))

## Techniques
- **Install a registry component with the shadcn CLI** — On the 21st.dev component page, copy the shadcn install command shown there. Run it in the root of the project (a Next.js app in the demo). The component files are created under components/ui/. Use the component in a page like any local component. Open the component's source on the site first if you want to learn how the effect works. *When:* You want a polished UI effect or block quickly and are happy to own and edit the code rather than depend on a package version.
- **Install by copying the code manually** — Open the component on 21st.dev and copy its source code instead of the CLI command. Paste it into your own components folder. *When:* You do not want the shadcn CLI in the project, or you want to read and learn from the code before adding it.
- **Use the copy-prompt button for an AI editor** — On a component page, click copy prompt and pick the variant for your AI tool (v0, Lovable, Bolt.new or generic). Paste it into the tool. The prompt tells the model to put the component in components/ui and to extend the Tailwind config with the styles the component needs. Check the generated files and the preview. *When:* You build in an AI app builder and want it to integrate the component correctly, including Tailwind config changes, without doing those edits yourself.
- **Iterate on the pasted component with small prompts** — After the component is in the project or in the AI builder, ask for small, specific changes in plain language, such as changing a colour or a text string. Verify the preview after each change. *When:* You need the component to match your brand or copy, and manual edits to the component source are slower than prompting.

## Numbers
- The speaker describes shadcn-style spin-off libraries as hundreds of variants. ([0:00](https://youtu.be/aQB0B3a1fh8?t=0))
- Video length is 5:43. No benchmarks, costs, download counts or latency figures are given, apart from the 'most downloaded' sort order on the site. ([0:00](https://youtu.be/aQB0B3a1fh8?t=0))

## Hot takes
- Calls 21st.dev 'a collection of the collections' and 'a modern way to build UI': find a base component, paste it in, and modify it with AI. This is opinion, not measured.
- The video is a promotional tour of one site with no caveats on licensing, maintenance, accessibility or dependency risk. Copying components into the codebase is presented only as an advantage.
- Conflict of interest not declared: the speaker says a shadcn spin-off he built was added to the site and that the site features his components. He presents the site as a community-driven resource without saying so up front.
- Quality is capped at 2 because the content is a thin product walkthrough with no sponsorship disclosure, no comparison with alternatives and no tested outcomes.

## Tools mentioned
21st.dev, shadcn/ui and the shadcn CLI, shadcn registry, Aceternity UI, Origin UI, Magic UI, Next.js, Tailwind CSS, v0, Lovable, Bolt.new
