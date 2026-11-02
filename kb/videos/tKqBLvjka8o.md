# The ONLY package manager you'll ever need for macOS

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `tKqBLvjka8o` · [watch](https://youtu.be/tKqBLvjka8o) · **date:** 2026-01-02 · **length:** 4:29 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Determinate
- **topics:** dev-tools · **tags:** nix, nix-darwin, macos, package-manager, homebrew, nix-homebrew, flakes, declarative-config, dotfiles, neovim, zellij, mackup, mise

> A short walkthrough of using Nix with nix-darwin and nix-homebrew to manage packages, Mac App Store apps and macOS defaults declaratively, as a possible replacement for Homebrew.

## Summary
The speaker tries Nix as one package manager for a Mac, replacing Homebrew and his config and language-version tools. He explains that Nix is a functional package manager with a steep learning curve, and that nix-darwin is the macOS framework built on it for managing packages and services. The setup covers installing Nix (he used the standard installer, and mentions the Determinate installer if you want easy uninstall), creating a config directory, and downloading the nix-darwin flake. He explains flake files as declarative manifests with inputs and outputs, and says the configuration name should match the hostname. He applies the config with darwin-rebuild switch, and shows that changing a package in the config (vim to neovim, plus zellij) takes effect on rebuild. For Mac-only GUI apps he adds nix-homebrew to the config so Mac App Store apps can be installed by app ID, and sets macOS system defaults in the Nix file. He ends with the goal of reproducing his whole Mac from Nix files, and says the video is a first impression rather than a full guide.

## Key ideas
- **Nix as one declarative package manager to replace Homebrew and separate config/version tools** — The speaker wants one tool for CLI packages, system configs and Mac App Store apps, and says Nix has a very steep learning curve. ([0:00](https://youtu.be/tKqBLvjka8o?t=0))
- **nix-darwin brings Nix to macOS** — It is a Nix framework for managing packages and services on Darwin, the Unix base of macOS. Nix itself dates to 2003 (per the speaker). ([0:58](https://youtu.be/tKqBLvjka8o?t=58))
- **Flakes are the entry point to the config** — A flake is a declarative project manifest with inputs (external dependencies) and outputs. Flakes are described as stable but still experimental, so a flag is needed to enable them. The configuration name in the flake should match the machine's hostname. ([1:51](https://youtu.be/tKqBLvjka8o?t=111))
- **Packages are declared in the config and applied by rebuilding** — Running darwin-rebuild switch installs what the flake declares. Changing vim to neovim and adding zellij shows the config is the source of truth. For one-off tools, the nix shell command works, but the speaker advises putting packages in the config. ([1:51](https://youtu.be/tKqBLvjka8o?t=111))
- **nix-homebrew covers Mac-only GUI apps** — Adding nix-homebrew to the darwin config, plus its URL, lets Nix install Mac App Store apps by app ID. The speaker says the app must have been purchased before. ([3:11](https://youtu.be/tKqBLvjka8o?t=191))
- **macOS system defaults can live in the Nix config** — Setting the user and changing system defaults in the Nix file applies them on rebuild, so Mac settings are reproducible too. ([3:11](https://youtu.be/tKqBLvjka8o?t=191))
- **The goal is a fully reproducible Mac, with the caveat that it is still a first impression** — The speaker plans to replace Brew and MacUp with Nix and rebuild his Mac from Nix files, using his public dotfiles repo to follow along. The video is an early experiment, not a complete guide. ([4:25](https://youtu.be/tKqBLvjka8o?t=265))

## Techniques
- **Install nix-darwin from a flake** — 1) Install Nix for macOS (the speaker used the standard installer; the Determinate Nix installer is the option if you want to uninstall cleanly later). 2) Create a Nix config directory. 3) Download the nix-darwin flake file into it. 4) Set the configuration name in the flake to your hostname. 5) Enable flakes, which need an experimental-features flag. The exact flag and install command are not clearly captured in the auto-captions, so check the nix-darwin README. 6) If darwin-rebuild is not found, the speaker says to comment out a line or run the install command again. 7) Run darwin-rebuild switch to build and activate the config. *When:* Setting up a fresh Mac with a declarative, reproducible configuration instead of Homebrew.
- **Declarative packages with rebuild** — Add package names (e.g. neovim, zellij) to the nix-darwin config's package list, then run darwin-rebuild switch. The speaker notes that vim then comes from Nix, and that a tool can be tried temporarily with the nix shell command before adding it to the config. *When:* Replacing Homebrew formulae or per-language version managers with pinned, rebuildable packages.
- **Mac App Store and cask apps via nix-homebrew** — Add the nix-homebrew module to the darwin config, plus its input URL, then declare each app by its App Store app ID. The app must already be purchased on the account. Rebuild to install. *When:* You need Mac-only GUI apps or App Store apps managed in the same config as CLI packages.
- **macOS system defaults in Nix** — Set the primary user and the system defaults options in the nix-darwin config, then rebuild. The speaker says the defaults update on rebuild. Options are in the nix-darwin documentation. *When:* Making Mac preferences reproducible across machines.

## Numbers
- Nix was created in 2003 by a Dutch computer scientist during PhD research (speaker's claim, not verified here). ([0:00](https://youtu.be/tKqBLvjka8o?t=0))
- Video runs 4:29, which is too short to cover the full nix-darwin setup. ([0:00](https://youtu.be/tKqBLvjka8o?t=0))

## Hot takes
- Nix has a very steep learning curve, but the speaker thinks it is worth it for one tool that covers packages, system config and App Store apps.
- The speaker plans to replace Homebrew and his other Mac config tools with Nix.
- The video is a first impression with thin reproducible detail. The exact install command and config lines are not shown in the captions.

## Tools mentioned
Nix, nix-darwin, darwin-rebuild, nix-homebrew, Homebrew, Determinate Nix installer, Nix shell, Neovim, Zellij, Mackup (spoken as 'MacUp'), mise (spoken as 'Mez'), Vim, NixOS, Mac App Store
