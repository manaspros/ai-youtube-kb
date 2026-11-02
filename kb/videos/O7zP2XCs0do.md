# Meta Just Dropped a NEW Python Type Checker!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `O7zP2XCs0do` · [watch](https://youtu.be/O7zP2XCs0do) · **date:** 2025-12-02 · **length:** 7:33 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Meta, Instagram
- **topics:** dev-tools · **tags:** python, type-checking, language-server, ide, mypy, pyre, pydantic, django, numpy, jupyter, beta

> Overview of Pyrefly, Meta's open-source Python type checker and language server, covering its speed claims, IDE features, mypy/Pyre migration path, and beta maturity.

## Summary
The video introduces Pyrefly, a fast static type checker and language server for Python built by Meta, where the CLI and the editor share one engine. The speaker frames its design around Meta's large monorepos: per-keystroke type checking, instant go-to-definition, inference for untyped legacy code, and automatic import updates on file rename. Meta's own benchmark of 1.8M lines per second and a 95% speedup over early alpha builds are cited without independent verification. The tool is pitched as a drop-in replacement for mypy or Pyre, with a config migration that reads the old settings and gradual adoption through baselines, inline ignores, and partial includes. The speaker says Pyrefly is still beta, though the IDE extension is production-ready, with 350+ bugs fixed and spec conformance up from 39% to 70% since alpha. The closing advice is to use it on medium or large codebases or with Pydantic, Django, or data-heavy libraries, to hold off if you depend on niche typing features or specialized library stubs, and to trial it on a small project first. The video has no hands-on demo, so the claims are unmeasured.

## Key ideas
- **Pyrefly is an open-source static type checker plus full language server for Python, and the CLI and editor share one engine so they report the same results.** — Positioned as an editor-first tool that also runs from the command line, built by Meta after its existing checker Pyre could not keep up with the scale and speed needed. ([0:00](https://youtu.be/O7zP2XCs0do?t=0))
- **The design goals come from Meta's monorepo scale: type checking on every keystroke, instant go-to-definition in huge multi-folder repos, inference for untyped legacy code, and one engine for CLI and IDE.** — The speaker frames the tool as a way to speed up development rather than slow it down, with millions of lines and many microservices as the motivating environment. ([1:18](https://youtu.be/O7zP2XCs0do?t=78))
- **Editor features are the main pitch: fast autocomplete, go-to-definition, automatic import updates when a file is renamed, built-in library stubs, and Jupyter support.** — The speaker calls the automatic import update on rename a standout feature. Editors named include VS Code, PyCharm, Neovim, Vim, and Cursor. ([1:18](https://youtu.be/O7zP2XCs0do?t=78))
- **Performance is the headline claim: 1.8M lines per second on Meta's benchmark and 95% faster type checking on large projects versus early alpha builds.** — Both figures come from Meta's own reporting and are not independently verified in the video. ([2:35](https://youtu.be/O7zP2XCs0do?t=155))
- **Static analysis features include inference on unannotated code, flow-sensitive narrowing (for example after an isinstance check), and library support for Pydantic v2, the Django ORM, and NumPy stubs.** — The speaker claims nearly 90% type completeness for the library stubs. This is presented as one of Pyrefly's main strengths. ([3:47](https://youtu.be/O7zP2XCs0do?t=227))
- **Fast navigation depends on deterministic import resolution: import root detection, automatic site-packages discovery, prioritized stub packages, and a fixed search order.** — This is the stated reason go-to-definition stays predictable in messy or mixed-environment projects. ([3:47](https://youtu.be/O7zP2XCs0do?t=227))
- **Migration from mypy or Pyre is meant to be low-effort: the tool scans the project, reads the old config, and generates a Pyrefly config that maps diagnostics, suppressed error codes, and include/exclude rules.** — Adoption can be gradual through baselines, inline ignores, and partial project includes. ([4:56](https://youtu.be/O7zP2XCs0do?t=296))
- **The maturity picture is mixed: Pyrefly is beta overall, the IDE extension is production-ready, 350+ bugs were fixed since alpha, and spec conformance rose from 39% to 70%.** — The stated roadmap includes full typing spec implementation, more Django and Pydantic support, more stubs, lower memory use, faster incremental checks, and a stable v1. ([4:56](https://youtu.be/O7zP2XCs0do?t=296))
- **The verdict is to adopt Pyrefly for medium or large codebases and for Pydantic, Django, or data-heavy code, but to wait if you depend on niche typing features or need full coverage of specialized libraries.** — The speaker's recommendation is to try it on a tiny project first, since it is easy to install and uninstall. ([6:18](https://youtu.be/O7zP2XCs0do?t=378))

## Techniques
- **Migrate an existing mypy or Pyre setup to Pyrefly** — Run the Pyrefly setup command at the project root (the captions garble the exact command, so check the official docs). It scans the project, finds the existing config, and writes a Pyrefly config that carries over diagnostic settings, suppressed error codes, and include/exclude patterns. *When:* Adopting Pyrefly in an existing Python codebase that already has a type checker configured.
- **Adopt a type checker gradually in a large legacy repo** — Use baselines to accept current errors, inline ignore comments for specific lines, and partial project includes to check only some directories at first. Widen the include scope over time. *When:* A large codebase cannot be made fully type-clean at once.
- **Share one checker config between editor and CLI** — Use the same Pyrefly config for IDE diagnostics and command-line checks so the editor and CI report the same results. The speaker's claim is that the CLI and IDE share a single engine. *When:* You want local editor feedback to match what CI enforces.
- **Trial a new type checker on a small project before committing** — Install Pyrefly, run it on a small project or a single package, compare its diagnostics and speed against the current checker, then decide whether to adopt it. *When:* Evaluating a beta tool whose coverage of your libraries is uncertain.

## Numbers
- Meta's benchmark: Pyrefly checks 1.8 million lines of Python per second (Meta's own figure, unverified). ([2:35](https://youtu.be/O7zP2XCs0do?t=155))
- 95% faster type checking on large projects compared with early alpha builds (Meta's figure). ([2:35](https://youtu.be/O7zP2XCs0do?t=155))
- Nearly 90% type completeness for library support, including Pydantic v2, Django ORM, and NumPy stubs (speaker's claim). ([3:47](https://youtu.be/O7zP2XCs0do?t=227))
- Over 350 bugs fixed since alpha. ([4:56](https://youtu.be/O7zP2XCs0do?t=296))
- Spec conformance rose from 39% to 70% since alpha. ([4:56](https://youtu.be/O7zP2XCs0do?t=296))

## Hot takes
- The 1.8M lines/sec headline is Meta's own benchmark, and the video does not test it on any real project.
- The title's 'Just Dropped' framing is news-driven, but the substance is a moderate recap of Meta's claims with no hands-on comparison.
- The most actionable advice is the speaker's suggestion to trial it on a small project first, since the tool is beta and easy to remove.

## Tools mentioned
Pyrefly (Meta, beta; version not stated), mypy, Pyre, Pyright (likely; the captions read 'Pyrite'), Pydantic v2, Django ORM, NumPy stubs, Jupyter, VS Code, PyCharm, Neovim, Vim, Cursor

## Relevance to our work
- **agentos** (1/3): AgentOS has Python services (MemoryMesh, InferCraft glue, evals), so a faster type checker could matter there, but the tool is beta and the video has no benchmarks. → *Trial Pyrefly on one AgentOS Python package in a branch and compare its diagnostics and runtime with the current checker. Keep the existing checker as the CI gate while Pyrefly is beta.*
