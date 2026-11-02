# This Tiny Linux Setting Fixed My Next.js Builds (Swap)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `HU5CV64vLg4` · [watch](https://youtu.be/HU5CV64vLg4) · **date:** 2026-01-02 · **length:** 10:44 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, DigitalOcean, Payload CMS
- **topics:** dev-tools, infra-cost-scaling · **tags:** swap, linux, nextjs, out-of-memory, small-vps, digitalocean, node-build, payload-cms, node-heap

> Tutorial on fixing out-of-memory Next.js builds on a 1 GB DigitalOcean droplet by adding swap files and capping the Node heap, instead of upscaling the server.

## Summary
The host says Next.js builds on a 1 GB RAM droplet freeze or get killed because build bursts (workers, TypeScript, bundling, image processing) exceed physical memory. He argues a swap file gives the kernel room to page out cold memory so the build finishes, and that this is cheaper than upgrading the server. He demonstrates on a fresh Payload CMS project with SQLite: pnpm install is OOM-killed, a 1 GB swap file lets it finish, and an unswapped build runs for a long time at about 90% CPU before he kills it. The build also fails at the default Node heap of 8000 MB, so he lowers --max-old-space-size to 2 GB and adds a second 1 GB swap file, after which the build completes in about 8 minutes with steadier CPU and disk I/O. He is clear that swap is for short bursts only: if production stays in swap or swap stays high at idle, the fix is more RAM or lower memory use. The video does not cover making swap persist across reboots or tuning swappiness.

## Key ideas
- **Small-server Next.js build crashes are a memory-burst problem, not a CPU problem; swap avoids an upgrade.** — Builds spawn workers, load TypeScript, bundle client and server code and process images in a short burst that can exceed 1 GB. Without swap the machine either freezes or the kernel kills processes. Swap lets rarely used pages move to disk so the build finishes, slowly. ([0:00](https://youtu.be/HU5CV64vLg4?t=0))
- **Swap suits short memory spikes, not sustained load.** — Good fits are build steps, package installs, data imports, migrations and admin scripts where stability matters more than speed. A production app that constantly dips into swap gets sluggish and slower response times. Persistent swap use at idle, or latency that shows up in normal operation, means the real fix is more RAM or less memory use. ([1:59](https://youtu.be/HU5CV64vLg4?t=119))
- **Reproduction: a pnpm install on a 1 GB droplet is OOM-killed.** — He creates a Payload CMS app with SQLite on a 1 GB RAM, 25 GB disk Ubuntu droplet. pnpm install fails with 'Killed' when npm runs out of memory. Disk was only 18 percent used, so disk space was not the constraint. ([4:15](https://youtu.be/HU5CV64vLg4?t=255))
- **Swap file setup is a short fixed sequence and the install succeeds afterwards.** — Check for existing swap, create a 1 GB file, lock permissions to 600, mark it as swap, and activate it. Then pnpm install completes; swap usage shows about 42 MB afterwards. ([5:32](https://youtu.be/HU5CV64vLg4?t=332))
- **The build still needs its Node heap capped to fit the available swap.** — Payload's build script sets --max-old-space-size to 8000 (MB), far above what the box can supply. He lowers it to 2 GB in package.json and reasons that the heap limit should be at or below total swap. A 1 GB swap file alone was not enough. ([8:03](https://youtu.be/HU5CV64vLg4?t=483))
- **Stacking multiple swap files adds capacity, and the build then completes.** — Adding a second 1 GB swap file gives 2 GB total swap. With the lowered heap cap the build finishes in about 8 minutes, with steadier CPU and lower disk I/O than the unswapped run. ([9:21](https://youtu.be/HU5CV64vLg4?t=561))

## Techniques
- **Diagnose swap and disk before creating a swap file** — Run `sudo swapon --show` (empty output means no active swap), `free -h` for total and swap memory, and `df -h` to confirm free disk space. *When:* Before adding swap to any small VPS, to see whether swap already exists and whether disk can hold the file.
- **Create and activate a swap file** — `sudo fallocate -l 1G swapfile`; verify with `ls -lh swapfile`; `sudo chmod 600 swapfile`; `sudo mkswap swapfile`; `sudo swapon swapfile`; verify with `sudo swapon --show` and `free -h`. He does not show /etc/fstab, so the file is not persisted across reboots in this video. *When:* On a 1 GB RAM box where a build or install gets OOM-killed, as a burst buffer rather than a permanent memory fix.
- **Stack extra swap files to reach a larger total** — Repeat the same steps with a different name, e.g. `swapfile2`, so total swap is the sum of the files (two 1 GB files = 2 GB). *When:* When one swap file is not enough for the build, and resizing the existing file is not wanted.
- **Lower the Node heap cap to match swap** — In package.json, change the build script's `--max-old-space-size` from 8000 to 2048 (MB) for Payload. He uses the rule of thumb that the heap limit should be at or below total swap. *When:* When a Node build with a large default heap OOMs on a small box even with swap enabled. This rule is his heuristic and was not benchmarked.
- **Set a swap budget against steady-state use** — After the build, confirm swap usage is back near zero, or at least not elevated during idle hours or normal traffic. If it stays high, add RAM or reduce memory use rather than relying on swap. *When:* On any server where swap was added for builds, to check it is not hiding a production capacity problem.

## Numbers
- Test server: 1 GB RAM, 25 GB disk Ubuntu droplet. ([3:10](https://youtu.be/HU5CV64vLg4?t=190))
- Disk usage was 18 percent before adding swap. ([4:15](https://youtu.be/HU5CV64vLg4?t=255))
- A 1 GB swap file is created, and swap usage reads about 42 MB after pnpm install succeeds. ([5:32](https://youtu.be/HU5CV64vLg4?t=332))
- Unswapped build: CPU at about 90 percent; the speaker says it ran about 40 minutes before he shut it off. The CPU graph he shows spans roughly 1:14pm to 1:40pm, about 26 minutes, so the two figures do not match. ([6:45](https://youtu.be/HU5CV64vLg4?t=405))
- Payload build default --max-old-space-size is 8000 (MB); lowered to 2048 (2 GB). ([8:03](https://youtu.be/HU5CV64vLg4?t=483))
- Two 1 GB swap files give 2 GB total; the build completes in about 8 minutes. ([9:21](https://youtu.be/HU5CV64vLg4?t=561))

## Hot takes
- Swap is presented as a cheap alternative to upscaling, but the speaker concedes it only covers short bursts and that sustained swap use is a capacity problem.
- The rule that the Node heap cap should be at or below total swap is the speaker's heuristic. He picked 2 GB without showing a sweep of values.
- The build-duration claim (about 40 minutes) conflicts with the CPU graph timestamps he shows (about 26 minutes).
- Gaps: no /etc/fstab persistence across reboots, no swappiness or zram discussion, and no monitoring of swap over time. Viewers running this in production need to handle these themselves.
- No sponsorship segment seen. Substance is a short, reproducible sysadmin tutorial.

## Tools mentioned
Next.js, Node.js, pnpm, npm, create-payload-app (pnpx create payload app@latest), Payload CMS, SQLite, DigitalOcean droplet, Ubuntu, fallocate, mkswap, swapon, chmod, free, df

## Relevance to our work
- **agentos** (1/3): Self-hosted single-box stack (vLLM, Postgres, Redis, Neo4j on one RTX 5090 host). The video's point that swap covers bursts and not steady memory pressure applies to host-RAM headroom, but the video is about Node builds on small VPSes. → *On the single-box AgentOS host, check swap usage during model loads and heavy builds, and treat sustained swap as a memory-capacity alarm in the observability stack.*
