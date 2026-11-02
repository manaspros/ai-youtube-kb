# Add Social Logins to Next.js in 5 Minutes (Supabase UI)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `jg6XAc-hhc8` · [watch](https://youtu.be/jg6XAc-hhc8) · **date:** 2025-11-02 · **length:** 4:32 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Supabase, shadcn, GitHub, Vercel
- **topics:** dev-tools, vibe-coding-app-building · **tags:** nextjs, supabase, shadcn-ui, oauth, github-login, social-auth, component-registry, env-vars

> Better Stack walkthrough of adding GitHub social login to a Next.js app using Supabase UI, shadcn's CLI, and a registry-installed component; mostly UI clicking through Supabase and GitHub settings.

## Summary
The video shows how to add a social login button to a Next.js app with the shadcn CLI and a Supabase UI registry component. The presenter initializes shadcn, adds a button component as a demo, then installs the social login component by running the add command against a registry URL that returns JSON describing the component. The component reports missing environment variables, so the presenter creates a Supabase project and copies the public URL and publishable/anon key into an env file. Login fails with "unsupported provider" until GitHub is enabled in Supabase's auth providers. The presenter then creates a GitHub OAuth app (homepage http://localhost:3000, callback URL copied from Supabase's GitHub provider page, device flow left off), generates a client secret, and saves it in Supabase. After that, GitHub login works and the new user appears in the Supabase users table. Other providers such as Google are mentioned but not shown. The video is a short, practical click-through with little code, and the "5 minutes" framing is the main hook.

## Key ideas
- **shadcn's CLI can install components from a registry URL, and Supabase UI components are distributed this way** — The presenter first runs the shadcn init and add commands, then uses the same add command with a registry URL. That URL returns a JSON object describing the component, which he calls a registry. He notes that you can build your own registry for custom components. ([0:08](https://youtu.be/jg6XAc-hhc8?t=8))
- **The social login component is installed with one add command and needs Supabase env vars before it works** — After the install, the terminal lists the variables to set (the public Supabase URL and the publishable/anon key). The presenter has the user create a Supabase project, copy the values from the connect dialog's app frameworks tab, and put them in a local env file. ([0:53](https://youtu.be/jg6XAc-hhc8?t=53))
- **Social login fails with 'unsupported provider' until the provider is enabled in Supabase** — Clicking continue before GitHub is configured returns an error saying the provider is not enabled. The fix is in Supabase's Authentication > Sign in / Providers settings, where GitHub must be turned on. ([2:04](https://youtu.be/jg6XAc-hhc8?t=124))
- **A GitHub OAuth app supplies the client ID and secret that Supabase needs** — The presenter creates the OAuth app in GitHub developer settings with homepage http://localhost:3000 and a callback URL copied from Supabase's GitHub provider page. He leaves device flow unchecked, registers the app, generates a client secret, and pastes both values into Supabase. ([3:15](https://youtu.be/jg6XAc-hhc8?t=195))
- **Verification is checking the Supabase users table for a new user with provider GitHub** — After a successful GitHub sign-in, the presenter checks the Supabase table, where the new user appears with GitHub as the provider. Other providers such as Google need their own setup, which he says is similar but not shown. ([3:15](https://youtu.be/jg6XAc-hhc8?t=195))

## Techniques
- **Install a Supabase UI auth component via shadcn registry** — 1) Create or open a Next.js app. 2) Run `npx shadcn@latest init` (the transcript auto-caption reads it as 'shadcn at latest'). 3) Add a base component to check the setup, e.g. `npx shadcn@latest add button`. 4) Run the same add command with the Supabase UI registry URL shown in the video, which returns the component JSON. The social login component then appears in the app, and the CLI lists required env vars. *When:* Adding a prebuilt auth UI to a Next.js + shadcn project without writing the OAuth button and handler code yourself.
- **Wire GitHub OAuth into Supabase Auth** — 1) In GitHub developer settings, create a new OAuth app with homepage URL http://localhost:3000. 2) Copy the callback URL from Supabase's GitHub provider page into the OAuth app. 3) Leave device flow unchecked and register the app. 4) Copy the client ID and generate a client secret. 5) In Supabase, open Authentication > Sign in / Providers, enable GitHub, and paste the client ID and secret. 6) Save, then retry the login from the app. *When:* Enabling GitHub sign-in on a Supabase-backed local Next.js app for development. The callback and homepage URLs here are localhost only.
- **Env vars from the Supabase connect dialog** — Open the project's Connect button, go to the app frameworks tab, and copy the Next.js env block. Put it in the project's env file. The presenter notes that the anon key name should be changed to the publishable key name (the video says `NEXT_PUBLIC_SUPABASE_ANON_KEY` is replaced with the publishable/anon key variable; the exact names are shown on screen and were not clearly spoken). *When:* Connecting a Next.js app to a new Supabase project. The exact variable names were not fully spoken, so check the on-screen values.

## Numbers
- Video length is 4:32, and the presenter frames the whole setup as taking 5 minutes ([0:00](https://youtu.be/jg6XAc-hhc8?t=0))
- The social login component's install step is one add command, after which the component shows on the page ([0:53](https://youtu.be/jg6XAc-hhc8?t=53))

## Hot takes
- The 'in just a single command' framing understates the setup. Most of the time goes to creating a Supabase project, a GitHub OAuth app, and a client secret, all manual dashboard steps.
- Thin for a tutorial: no code is written, the registry URL is shown on screen but not spoken, and the env var names are not clearly stated. Other providers are mentioned but not shown.
- The presenter's comments are stream-of-consciousness and include asides; the useful content is short.

## Tools mentioned
Next.js, shadcn/ui (shadcn CLI, `npx shadcn@latest`), Supabase, Supabase UI, GitHub OAuth, VS Code, Vercel (mentioned only as the look to imitate)

## Relevance to our work
- **general** (1/3): Shows the 'install from registry plus print required env vars' flow for a CLI-driven setup, which is a reasonable pattern for onboarding steps. → *Note it as an example of how a CLI can list the env vars a component needs at install time, if a onboarding flow is ever designed.*
