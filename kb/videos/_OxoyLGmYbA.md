# UV - Every Python Developer NEEDS This

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `_OxoyLGmYbA` · [watch](https://youtu.be/_OxoyLGmYbA) · **date:** 2025-11-02 · **length:** 7:21 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed) · **orgs:** Astral, Better Stack, Cursor
- **topics:** dev-tools · **tags:** python, uv, package-management, lockfile, virtualenv, pyproject-toml, uvx, ruff, inline-script-metadata, python-version-management

> A Better Stack walkthrough of uv, Astral's Rust-based Python package and project manager, covering projects, lockfiles, inline script dependencies, uvx tools and Python version management.

## Summary
The video is a short tutorial presenting uv as a single replacement for pip, pip-tools, pipx, Poetry, pyenv, twine and virtualenv. It starts with project setup (uv init, pyproject.toml, .python-version, main.py) and shows uv run creating a .venv and a uv.lock file. It then covers adding, upgrading, viewing and removing dependencies, plus a pip-compatible interface for legacy projects. The middle section explains running standalone scripts with uv run, including --with and inline script metadata added via uv add --script. It closes with uvx and uv tool install for running and installing CLI tools such as Ruff, and with uv python install, list and pin for managing interpreters. The presenter claims uv wins nearly every benchmark but shows no measurements beyond one install taking about five milliseconds. Nothing is sponsored, and the content is a practical command tour rather than deep analysis.

## Key ideas
- **uv replaces most of the Python packaging stack (pip, pip-tools, pipx, Poetry, pyenv, twine, virtualenv) with one tool.** — Presented as a drop-in replacement for pip and pip-tools workflows, usable as only a resolver, only a venv creator, or only a package manager. ([0:00](https://youtu.be/_OxoyLGmYbA?t=0))
- **uv init scaffolds a project and uv run manages the environment and lockfile automatically.** — uv init creates pyproject.toml, .python-version and main.py. uv run main.py creates .venv and uv.lock, so no manual venv activation is needed. ([0:00](https://youtu.be/_OxoyLGmYbA?t=0))
- **Dependency changes go through uv add, uv remove and uv lock --upgrade, and the lockfile pins exact versions.** — uv add updates pyproject.toml. Upgrading one package keeps the rest of uv.lock fixed, and omitting the package name upgrades everything. A global cache deduplicates packages, which the presenter compares to what pnpm did for npm. ([1:15](https://youtu.be/_OxoyLGmYbA?t=75))
- **uv tree shows the dependency graph, and uv keeps a pip-compatible interface for legacy projects.** — uv tree lists direct and transitive dependencies for debugging. uv pip install, check and freeze cover manual workflows, and the presenter notes a requirements.txt migration command exists. ([2:32](https://youtu.be/_OxoyLGmYbA?t=152))
- **Standalone scripts can declare their own dependencies, so they no longer need a shared project environment.** — uv run script.py runs dependency-free scripts by default. For scripts with dependencies, uv run --with <pkg> works ad hoc, or uv add --script adds inline metadata to the file's header so uv run handles it. ([3:41](https://youtu.be/_OxoyLGmYbA?t=221))
- **uvx (alias for uv tool run) runs Python CLI tools in throwaway environments, and uv tool install puts them on PATH.** — uvx ruff check runs Ruff without installing it into the project. uv tool install ruff installs it globally, and uv tool update-shell adds it to PATH. The presenter says this is how many MCP servers are commonly set up. ([4:42](https://youtu.be/_OxoyLGmYbA?t=282))
- **uv installs and pins Python interpreters, and downloads the version a project requires when it is missing.** — uv python install 3.11 fetches a version, uv python list shows installed and downloadable versions, and uv python pin records a project version. The presenter says a project requiring 3.13 on a fresh machine triggers an automatic download. ([5:47](https://youtu.be/_OxoyLGmYbA?t=347))

## Techniques
- **Project bootstrap with lockfile** — Run `uv init <name>`, then `uv run main.py`. This creates .venv and uv.lock. Add packages with `uv add <pkg>`, remove with `uv remove <pkg>`, and inspect with `uv tree`. *When:* Starting any new Python project to avoid manual venv and requirements management.
- **Targeted lockfile upgrades** — `uv lock --upgrade-package <pkg>` upgrades one package and leaves the rest of uv.lock unchanged. `uv lock --upgrade` upgrades everything. *When:* When you want a controlled dependency bump without churn in the lockfile.
- **Ad hoc script dependencies** — `uv run --with rich script.py` installs the named package into a short-lived environment for that run only. *When:* Running a one-off script that needs a library without changing any project.
- **Inline script metadata** — `uv add --script script.py rich` writes the Python version and dependency list into a header block in the file. Then `uv run script.py` resolves them with no --with flags. *When:* Writing shareable single-file Python scripts that carry their own dependencies.
- **Ephemeral CLI tool runs** — `uvx ruff check` (alias for `uv tool run ruff check`) runs the tool without installing it. For a persistent install, run `uv tool install ruff`, then `uv tool update-shell`. *When:* Running linters, formatters or MCP server packages that are published as Python packages.
- **Interpreter pinning** — `uv python install 3.11` downloads an interpreter, `uv python list` shows what is available, and `uv python pin <version>` writes the project's .python-version. Other distributions such as PyPy are also supported by the install command. *When:* Keeping every machine and CI run on the same Python version without installing it separately.
- **Legacy pip compatibility** — Use `uv pip install`, `uv pip check` and `uv pip freeze` inside existing projects. The presenter also mentions a command to migrate requirements.txt but does not name it in the video. *When:* Migrating a project incrementally from pip without rewriting its workflow at once.

## Numbers
- A dependency install (uv add) completed in about 5 milliseconds, attributed to the global cache. ([1:15](https://youtu.be/_OxoyLGmYbA?t=75))
- uv is described as winning nearly every benchmark, but no benchmark figures are shown. ([0:00](https://youtu.be/_OxoyLGmYbA?t=0))
- Example Python versions used in the demos are 3.11 (explicit install) and 3.13 (auto-download for a project pin). ([5:47](https://youtu.be/_OxoyLGmYbA?t=347))

## Hot takes
- "You won't need pip again." The video offers no evidence that uv covers every pip use case, and it does not discuss limitations.
- The claim that uv wins nearly every benchmark is unsupported in the video, and the only speed evidence is a single 5 ms install.
- The mention of MCP servers being set up via uvx is an aside with no detail.

## Tools mentioned
uv (Astral), Ruff (spoken as "rough" in the captions; described as made by Astral), pip, pip-tools, pipx, Poetry, pyenv, twine, virtualenv, pnpm (analogy), npm (analogy), Cursor, Flask, rich (rich.progress), black (mentioned), PyPy, Python 3.11, Python 3.13, pyproject.toml, uv.lock, .python-version, .venv

## Relevance to our work
- **agentos** (1/3): AgentOS is a Python-based multi-service project, and uv's lockfile-based environments could make its service environments reproducible. → *Check whether the AgentOS Python services use a lockfile-based tool such as uv, and if not, trial uv lock on one service to see whether the resolved set reproduces across machines.*
