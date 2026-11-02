# Tempo Labs Tutorial: The Ultimate Vibe Coding Package

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `k6uBbUZ9MZg` · [watch](https://youtu.be/k6uBbUZ9MZg) · **date:** 2025-11-02 · **length:** 11:50 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed AI LABS narrator · **orgs:** Tempo Labs, Supabase, Stripe, Aceternity UI, AI LABS
- **topics:** vibe-coding-app-building, product-ux · **tags:** tempo-labs, supabase, stripe, nextjs, saas-scaffolding, stripe-webhooks, test-mode-payments, prd-first-prompting, mermaid, supabase-mcp, vibe-coding

> Tutorial walkthrough of Tempo Labs, an AI app builder that wires Next.js, Supabase auth/database and Stripe payments before generating a gradient-wallpaper SaaS from a PRD-first prompt. Mostly a promotional demo with few verified claims.

## Summary
The narrator builds a small SaaS app (a gradient wallpaper generator with paid plans) in Tempo Labs. Setup happens first: pick Next.js, Supabase for auth and database, and Stripe for payments, then connect each service to the Tempo project. The Supabase connection is authorized through Tempo with read and write access, and Stripe requires a business account, test mode, API keys and a webhook endpoint that Tempo supplies. Products added in the Stripe catalog appear automatically on Tempo's pricing page. The build prompt makes Tempo write a PRD and a Mermaid user-flow diagram first, then a Supabase migration, edge functions for plans and checkout, a landing page, and dashboard components in subtasks. The narrator then registers, confirms email, signs in, and completes a simulated $10 test-mode payment. The video shows a working demo but does no testing, and it ends with a donation request.

## Key ideas
- **A SaaS needs three core parts: authentication (who can get in), a database, and payments. The narrator treats payments as the one that matters most.** — Framing for why the tool wires up auth, DB and billing before any feature code. Argued in general terms, not measured. ([0:00](https://youtu.be/k6uBbUZ9MZg?t=0))
- **Tempo lets you choose framework, auth and payments in a setup menu before the first build prompt.** — Narrator picks Next.js, Supabase and Stripe. Choosing a database or payment provider opens a setup flow for that service. ([1:23](https://youtu.be/k6uBbUZ9MZg?t=83))
- **The Supabase link is a full read-write OAuth connection through Tempo. The narrator contrasts it with Supabase MCP in Cursor or Windsurf, which he says is read-only.** — Tempo asks for permissions, you pick the organization, then the project; status should show active and healthy. The read-only claim about the MCP is stated, not shown. ([2:23](https://youtu.be/k6uBbUZ9MZg?t=143))
- **Stripe needs a business account (not personal) and test mode turned on before keys or webhooks are set up.** — Test mode simulates transactions. The publishable key, secret key and webhook signing secret go into Tempo. The endpoint URL to paste into Stripe comes from Tempo. ([3:57](https://youtu.be/k6uBbUZ9MZg?t=237))
- **Stripe catalog products flow automatically into Tempo's pricing page, on the landing page and in the app.** — Adding a product in Stripe (name, billing type, amount) and refreshing Tempo shows the new plan. The count went from one plan to two in the demo. ([5:19](https://youtu.be/k6uBbUZ9MZg?t=319))
- **The build starts from a PRD and a Mermaid user-flow diagram, then creates the Supabase migration and payment edge functions before any UI.** — The narrator then runs a template prompt that first asks the model to read and understand the codebase, then builds the landing page, then the dashboard, one subtask at a time. ([6:46](https://youtu.be/k6uBbUZ9MZg?t=406))
- **The narrator's bug-fixing sample is a known failure mode: models forget that some components must render on the client side, and fixing it took a prompt.** — Only one recurring failure is named. The narrator says these issues are common and minor. ([8:01](https://youtu.be/k6uBbUZ9MZg?t=481))
- **The demo app works end-to-end in test mode: sign-up, email confirmation, sign-in, a plan list from Stripe, and a simulated $10 payment that unlocks the generator.** — The narrator says the app works, but he explicitly deferred testing ('we'll build the app first and handle testing later'). No automated tests or verification step appear. ([10:13](https://youtu.be/k6uBbUZ9MZg?t=613))

## Techniques
- **Pre-wire integrations before the first build prompt** — In Tempo's setup menu choose framework (Next.js), auth/database (Supabase) and payments (Stripe) before writing the prompt. Connect each service from its setup flow so the generated code and migrations already reference them. *When:* Starting a new SaaS-style app where auth, database and billing are needed from the first commit, and you want the agent to build against real services.
- **Supabase connection via Tempo** — Create a Supabase project in the Supabase dashboard (a first-time user is asked to create an organization). Wait until Project Status shows active and healthy. In Tempo click Connect Supabase, authorize with read-write permissions, select the organization and then the project. *When:* When the agent needs to create tables and migrations itself rather than only reading an existing schema.
- **Stripe test-mode wiring** — Use a Stripe business account and enable test mode. Copy the publishable key and secret key from the Developers > API section into Tempo. In Webhooks, create an event destination with the endpoint URL shown in Tempo, select all events, add the endpoint, reveal the signing secret, and paste it into Tempo. *When:* Adding subscription or one-time payments to a generated app before going live. Stay in test mode until the flows are verified.
- **Adding plans through the Stripe product catalog** — In Stripe open the product catalog, add a product with a name, payment type and amount. Refresh the Tempo project to confirm the new plan appears on the pricing page. *When:* When you want pricing to be managed in Stripe and rendered automatically by the generated app.
- **PRD-first build prompt with a subtask loop** — Send the app idea as a single prompt. Let the tool produce a PRD and a Mermaid user-flow diagram first. Then use its template prompt: read and understand the codebase, build the landing page from the PRD and diagram, then give the next subtask set (components, dashboard integration, download feature). Fix errors as they come up. *When:* Building a multi-page app from a short brief where you want a written spec and flow diagram before code.
- **Fix client-side rendering by prompting** — When a component fails to render (typically a browser-only component rendered on the server), ask the agent to fix it. The narrator did not show the exact fix. *When:* Next.js apps where server-rendered output breaks interactive components.

## Numbers
- Integrations (auth, database, payments) can be set up in under a minute in Tempo. ([0:00](https://youtu.be/k6uBbUZ9MZg?t=0))
- Example pricing: full ChatGPT plan at $50 versus offering only the image-generation API part for much less. Illustrative, not measured. ([0:00](https://youtu.be/k6uBbUZ9MZg?t=0))
- Stripe plans on the pricing page went from one to two after adding one product in the catalog. ([5:19](https://youtu.be/k6uBbUZ9MZg?t=319))
- Simulated test-mode payment of $10 for one plan. ([10:13](https://youtu.be/k6uBbUZ9MZg?t=613))
- Narrator says getting payments working took two or three clicks, assuming a Stripe business account already exists. ([8:01](https://youtu.be/k6uBbUZ9MZg?t=481))
- Video length 11:50. ([0:00](https://youtu.be/k6uBbUZ9MZg?t=0))

## Hot takes
- Promotional tone for a single tool. The build is presented as 'two or three clicks' and 'under a minute', but those claims skip the Stripe business-account setup, which the narrator himself says can take time.
- The app is declared working with no testing or verification step. The narrator says testing is for later.
- The claim that Supabase MCP in Cursor or Windsurf is read-only is stated, not demonstrated. It may be outdated or configuration-dependent.
- The video is a tool walkthrough with no sponsor disclosure in the transcript. The donation request in the outro is for the channel.
- Auto-caption errors were corrected: 'Superbase' is Supabase, 'Tempolabs' is Tempo Labs, 'Aseternity' is Aceternity UI. Card numbers were mentioned but not spoken in the transcript.

## Tools mentioned
Tempo Labs (Tempo), Next.js, Supabase, Supabase edge functions, Supabase MCP, Stripe, Stripe webhooks, Mermaid, Cursor, Windsurf, Aceternity UI, Expo, ChatGPT image generation model (named as '4.0')
