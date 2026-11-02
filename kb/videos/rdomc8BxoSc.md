# Why Bun is 7x FASTER Than NPM (Speed Secret Revealed)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `rdomc8BxoSc` · [watch](https://youtu.be/rdomc8BxoSc) · **date:** 2025-12-02 · **length:** 4:42 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Bun
- **topics:** dev-tools · **tags:** bun, npm, package-managers, zig, performance, lockfile, tarball, system-calls, cpu-cache

> Walks through Bun's blog post on why its package installs are fast: fewer system calls via Zig, cache-friendly lockfile layout, and tarball extraction without buffer regrowth.

## Summary
The video explains why Bun installs packages much faster than npm, pnpm and yarn, citing a claimed 7x speedup on installs. It follows the install pipeline step by step: writing files to disk, parsing manifest and lock files, and extracting tarballs. Bun is written in Zig, so it reaches the OS with direct system calls instead of going through Node.js, libuv and the JavaScript event loop, which cuts mode switches and syscall count. The lockfile uses a structure-of-arrays layout instead of JSON objects, which the narrator argues suits CPU cache lines and avoids scattered memory access. For tarballs, Bun downloads the whole compressed file into memory, reads the uncompressed size from the last four bytes, and preallocates the output, avoiding repeated buffer growth and copies; this is only sensible for small packages. The narrator also says Bun uses a faster decompression library and multi-core parallelism for heavy steps, but does not cover them. The whole video is a summary of Bun's blog post and shows no benchmarks of its own.

## Key ideas
- **Package installs are dominated by many small system calls, and each user-to-kernel mode switch stalls the program.** — Installs can make hundreds of thousands of syscalls. Node-based managers (npm, pnpm, yarn) add overhead through libuv and the JS event loop even for simple file reads. Bun, written in Zig, calls the OS directly and makes far fewer syscalls. ([0:58](https://youtu.be/rdomc8BxoSc?t=58))
- **Bun's lockfile uses a structure-of-arrays layout instead of JSON objects, so reads are cache-friendly.** — JSON parsers allocate objects at scattered memory addresses, and a CPU cache line is 64 bytes even when only 8 are needed. A flat array lets the CPU load related data in one fetch. The narrator says the same idea applies to registry manifests in a machine-readable format. ([2:03](https://youtu.be/rdomc8BxoSc?t=123))
- **Streaming tarball decompression causes repeated buffer grow-and-copy, so Bun downloads the whole compressed tarball first.** — With an unknown output size, the buffer is reallocated and copied as it grows; the narrator's example is about 960 KB copied unnecessarily for a 1 MB package. Bun holds the compressed file in memory, reads the uncompressed size from the last four bytes, and preallocates. This is a poor fit for large packages such as TypeScript. ([3:15](https://youtu.be/rdomc8BxoSc?t=195))
- **Bun uses a faster decompression library than the standard library most package managers use.** — The narrator names this as a separate factor in the tarball step but does not name the library or give numbers. ([3:15](https://youtu.be/rdomc8BxoSc?t=195))
- **Heavy install steps are spread across all CPU cores.** — The narrator mentions multi-core parallelism for the heavy parts of installation, plus async DNS resolution, but explicitly skips both. He points to Bun's blog post for details. ([4:17](https://youtu.be/rdomc8BxoSc?t=257))

## Techniques
- **Cut syscall overhead with native code** — Implement the hot file I/O path in a language that compiles to native code and calls the OS directly, avoiding runtime layers such as an async I/O library plus an event loop. Fewer syscalls and user/kernel switches are the goal. *When:* When a CLI does many small file operations (installers, build tools, unpackers) and runtime overhead per call dominates.
- **Cache-friendly structure-of-arrays for parsed metadata** — Store parsed lockfile or manifest data as flat, contiguous arrays (one array per field) in a machine-readable form, not as many small heap-allocated objects. Scans then touch contiguous memory and reuse each 64-byte cache line. *When:* When large metadata files are parsed on every run and the parsed structure is traversed hot.
- **Preallocate decompression output from the archive trailer** — Download the whole compressed payload into memory, read the uncompressed size from the last four bytes, allocate the output buffer once, then decompress into it. This removes repeated grow-and-copy cycles. *When:* For many small archives (under about 1 MB in the narrator's example) where holding the compressed bytes in memory is cheap. Avoid it for large archives, where memory use grows.
- **Parallelize heavy install steps across cores** — Split the CPU-heavy parts of the install pipeline across all cores instead of running them on one core. The narrator gives no implementation details. *When:* When a multi-step pipeline has independent CPU-bound stages, such as extracting many packages.

## Numbers
- Bun is claimed to be about 7x faster than npm for package installs (headline; no benchmark shown in the video). ([0:00](https://youtu.be/rdomc8BxoSc?t=0))
- A typical user-to-kernel mode switch takes a fraction of a millisecond, and installs can make hundreds of thousands of system calls. ([0:58](https://youtu.be/rdomc8BxoSc?t=58))
- A CPU cache line is 64 bytes, and it is loaded even when only 8 bytes are needed. ([2:03](https://youtu.be/rdomc8BxoSc?t=123))
- Growing a tarball buffer during streaming decompression copies about 960 KB unnecessarily for a 1 MB package (the narrator's example). ([3:15](https://youtu.be/rdomc8BxoSc?t=195))
- Bun reads the uncompressed size from the last 4 bytes of the downloaded tarball to preallocate output memory. ([3:15](https://youtu.be/rdomc8BxoSc?t=195))

## Hot takes
- The 7x npm speedup is stated in the intro but not measured in the video; the claim rests on Bun's blog post.
- The video frames the speed as three secrets, but the narrator covers only syscalls, lockfile layout and tarball handling in depth; parallelism and async DNS are mentioned and skipped.
- Buffering whole compressed tarballs in memory is a trade-off the narrator admits is poor for large packages such as TypeScript.
- The title's 'Speed Secret Revealed' framing oversells what is a summary of a blog post, but the technical points are accurate at the level of detail given.

## Tools mentioned
Bun, npm, pnpm, yarn, Node.js, libuv, Zig, TypeScript (as the example of a large package)
