# The BEST way to make NPM packages

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Hf6u1RA7dTg` · [watch](https://youtu.be/Hf6u1RA7dTg) · **date:** 2025-11-02 · **length:** 5:49 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Bernard · **orgs:** Better Stack, npm, GitHub
- **topics:** dev-tools · **tags:** npm, nodejs, npm-packages, scoped-packages, npm-link, npm-publish, fisher-yates, git, github, tutorial

> Beginner tutorial on building a small npm package (a Fisher-Yates array shuffle), testing it with npm link, publishing it, and linking it to a GitHub repo.

## Summary
Bernard walks through creating an npm package from scratch in about six minutes. He starts by installing Node and Git, creating a GitHub repository, and running npm init, using a scoped name (@username/shuffle) to avoid name collisions. He then writes index.js with a shuffle function implementing Fisher-Yates (loop backward, swap with a random earlier element) and exports it. Local testing uses npm link from the package folder and npm link <package name> in a separate project, then requiring the module in app.js. Publishing requires an npm account whose username matches the scope, npm login, and npm publish --access public. The video ends by pushing the code to the GitHub repo so the npm page links to source. It is a basic, linear tutorial with no tests, versioning or CI covered.

## Key ideas
- **Prerequisites are Node (to run and test the project locally) and Git (to push code); create the GitHub repo first.** — The repo is created on github.com before running npm init, and its URL goes into package.json. ([0:00](https://youtu.be/Hf6u1RA7dTg?t=0))
- **Package names must be unique on npm, so use a scoped name tied to your username.** — A plain name like shuffle is likely taken; @username/shuffle avoids the clash, and the npm username must match the scope for publishing. ([1:17](https://youtu.be/Hf6u1RA7dTg?t=77))
- **npm init fills in package.json, with entry point index.js as the default.** — Version starts at 1.0.0 (semver), description shows on the npm registry page, and the git repository URL and author are recorded; license is left as ISC. ([1:17](https://youtu.be/Hf6u1RA7dTg?t=77))
- **The package is one exported function: a Fisher-Yates shuffle.** — The function loops backward through the array, picks a random index, swaps it with the current element, and returns the array. ([2:31](https://youtu.be/Hf6u1RA7dTg?t=151))
- **npm link lets you test the package in another local project without publishing it.** — It creates a global symlink to the package folder; the consumer project then links the scoped package name and requires it. ([2:31](https://youtu.be/Hf6u1RA7dTg?t=151))
- **Publishing needs npm login and npm publish --access public for a scoped package.** — Login opens a browser flow; after publishing, the package page on npmjs.com shows the install command. ([3:47](https://youtu.be/Hf6u1RA7dTg?t=227))
- **Linking the package to its GitHub repo is done by pushing the code, since the npm page shows the repo link even when it is empty.** — The speaker copies the commands from GitHub's new-repo page, then runs git add, commit with a first message, and push. ([5:04](https://youtu.be/Hf6u1RA7dTg?t=304))

## Techniques
- **Scoped npm package setup** — Create the GitHub repo first. Run npm init and enter a scoped name like @<npm-username>/shuffle, version 1.0.0, a description, the git repo URL, author, and license (ISC default). Keep entry point index.js. The npm username must match the scope. *When:* Starting any new npm package whose plain name is likely taken.
- **Write the entry point and export it** — Create index.js with a shuffle(array) function implementing Fisher-Yates: loop backward, pick a random index, swap the current element with it, return the array. Export the function as a module. *When:* Implementing a single-function utility package.
- **Local testing with npm link** — In the package folder run npm link. In a separate test project run npm link @<username>/shuffle, create app.js that requires the package and logs shuffle(array), then run node app.js. *When:* Trying out a package locally before publishing it to the registry.
- **Publish a scoped package publicly** — Create an npm account whose username matches the scope. In the package folder run npm login (browser flow), then npm publish --access public. Verify on npmjs.com/package/<name> and install it in a fresh project with npm install @<username>/shuffle. *When:* Publishing a scoped package so anyone can install it.
- **Link the npm package to source** — Create the GitHub repo empty, then in the project run git add, git commit -m with a first message, and git push using the commands GitHub shows for an existing repo. The npm page then links to the repo. *When:* Publishing a package whose source should be visible on npm.

## Hot takes
- The title promises 'the BEST way' but the video is a basic beginner walkthrough with no tests, CI, versioning workflow or publish automation.
- Quality capped at 2: thin substance for a generic title, though the steps are accurate and clearly shown.

## Tools mentioned
Node.js, npm, npm link, npm login, npm publish, npm init, Git, GitHub, npmjs.com, VS Code

## Relevance to our work
- **general** (1/3): Useful only as a refresher for publishing small npm utilities.
