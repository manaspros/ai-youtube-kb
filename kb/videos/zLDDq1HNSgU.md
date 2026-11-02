# 5 Deadly ENV Mistakes Everybody Makes

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `zLDDq1HNSgU` · [watch](https://youtu.be/zLDDq1HNSgU) · **date:** 2025-11-02 · **length:** 4:35 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Bernard · **orgs:** Better Stack
- **topics:** dev-tools, security-guardrails · **tags:** env-vars, secrets, gitignore, .env.example, secret-leakage, git-history, nextjs, vite, react, NODE_ENV, README, rotate-keys

> Five common .env mistakes (committing secrets, undocumented projects, rewriting git history, one env file for all environments, and leaking secrets through frontend bundles) and the fix for each.

## Summary
Bernard from Better Stack lists five environment-variable mistakes. The first is committing a .env file to a repository; he suggests a .env.example with variable names only, a .gitignore entry for the real file, or documenting the required variables in the README. The second is undocumented projects, which cost him hours of code reading when he returned to one. The third is assuming git rm removes a secret: anything pushed stays in history, so any exposed key should be revoked or rotated and treated as compromised. The fourth is using one env file with commented-out blocks for local, staging and production, which is easy to get wrong; he recommends separate files per environment, selected by NODE_ENV. The fifth is exposing secrets to the browser: frontend frameworks inline variables into the client bundle unless they are explicitly prefixed (NEXT_PUBLIC_, VITE_, REACT_APP_), and secrets should never get those prefixes. He closes with a rule of thumb: publishing the key should not cost you a job or thousands of dollars. The video is short, beginner-level and generic, with no product pitch beyond a subscribe joke.

## Key ideas
- **Committing a real .env file exposes secrets; GitHub search for .env or API keys returns large numbers of such files.** — Check in a .env.example that lists variable names only, add the real .env to .gitignore, or skip env files entirely and document the variables in the README. Speaker's claim of hundreds of thousands of exposed files is unsourced. ([0:00](https://youtu.be/zLDDq1HNSgU?t=0))
- **Undocumented projects are costly to resume; a README and an example env file save hours of reverse-engineering the code.** — He had to read code for hours to find which API key and secret a project needed because there was no example env file or documentation. ([1:12](https://youtu.be/zLDDq1HNSgU?t=72))
- **Deleting a committed secret in a later commit does not remove it from the repository history.** — Anything pushed stays in the commit history, so after a leak the advice is to revoke or rotate every affected API key, password and secret and treat them as compromised. ([1:12](https://youtu.be/zLDDq1HNSgU?t=72))
- **One env file with commented-out blocks for local, staging and production is error-prone.** — Switching blocks by hand risks running tests or changes against the wrong environment, even deleting data thought to be local. Use separate files per environment and pick one conditionally based on NODE_ENV. ([2:19](https://youtu.be/zLDDq1HNSgU?t=139))
- **Frontend bundlers ship env variables to the browser, so unprefixed secrets in React, Next.js or Vite apps can be read in dev tools.** — Only variables with the framework's public prefix are exposed: NEXT_PUBLIC_ for Next.js, VITE_ for Vite, REACT_APP_ for React. Never put secrets, passwords or private API keys under those prefixes. ([2:19](https://youtu.be/zLDDq1HNSgU?t=139))
- **Some keys are meant to be public, such as read-only publishable keys (his example is Supabase), so the test is the consequence of exposure.** — Golden rule: ask whether publishing the key would cost you a job or thousands of dollars. If not, it is mostly fine. When unsure, ask other developers. ([3:31](https://youtu.be/zLDDq1HNSgU?t=211))

## Techniques
- **Commit a .env.example with variable names only** — Copy the real .env to .env.example, strip every value (or use placeholders), commit the example, and add .env to .gitignore so the real file is never pushed. *When:* Any repo that reads secrets or config from env vars, so new contributors can see what is required.
- **Document required env vars in the README** — List each required variable, what it is for, and the setup steps in the README. Speaker presents this as an alternative to committing an example file. *When:* Projects that will be revisited later or shared with other developers.
- **Respond to a leaked secret by rotating it** — Assume any key that reached a repository is compromised. Revoke or rotate it at the provider and change passwords or secrets. Deleting the file in a new commit is not enough because history keeps it. *When:* Immediately after discovering a secret was pushed, even if the repo is private or the commit was quickly removed.
- **Separate env files per environment, selected by NODE_ENV** — Keep one env file each for local/development, staging and production. Load the matching file based on the NODE_ENV value instead of commenting lines in and out in one file. *When:* Any project that runs against more than one environment with the same variable names.
- **Use framework prefixes only for values safe to expose** — Expose a value to the browser only with the framework's prefix: NEXT_PUBLIC_ (Next.js), VITE_ (Vite), REACT_APP_ (React). Keep secrets and private keys unprefixed and read them only on the server. *When:* Any frontend bundle built with Next.js, Vite or React, whenever a variable is added.

## Numbers
- Video length is 4:35 and covers five mistakes. ([0:00](https://youtu.be/zLDDq1HNSgU?t=0))
- Speaker says GitHub searches for .env or API keys turn up hundreds of thousands of files (anecdotal, unsourced). ([0:00](https://youtu.be/zLDDq1HNSgU?t=0))
- Speaker spent hours reading code to recover an undocumented project's required keys (anecdote). ([1:12](https://youtu.be/zLDDq1HNSgU?t=72))

## Hot takes
- Anything pushed to a repository is permanent in its history, so deleting a secret later is not a fix; rotate it.
- Beginner-level tip list with a clickbait title; the substance is correct but generic. Scored 2 because there is no depth beyond basic hygiene.
- Some keys are safe to expose (publishable, read-only ones), and the test he gives is the consequence of exposure, not the key type.

## Tools mentioned
GitHub, Git (.gitignore, commit history), Next.js, Vite, React, Node.js (NODE_ENV), Supabase (publishable API key example)

## Relevance to our work
- **prosharness** (2/3): ProsHarness has zero-token credential handling. The video's rules on keeping secrets out of committed files and out of client bundles apply directly to its design. → *Audit ProsHarness for secrets in committed env files or history, and make sure secrets never get a public framework prefix such as VITE_ or NEXT_PUBLIC_ in any UI it generates.*
- **agentos** (1/3): AgentOS runs many provider and infra keys (proxy, Postgres, Redis, Neo4j); the same .env hygiene applies to the repo. → *Add a committed .env.example for AgentOS services and a pre-commit or CI check that blocks real .env files and key patterns.*
- **general** (1/3): Generic dev-hygiene reminder for any project that uses env vars. → *Keep a short env-var checklist (example file, gitignore, per-environment files, public-prefix check) in each new repo template.*
