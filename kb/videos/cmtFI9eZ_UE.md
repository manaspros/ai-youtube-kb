# Go 1.24 Just RELEASED – Weak Pointers, Generic Aliases & More! (HUGE UPDATE)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `cmtFI9eZ_UE` · [watch](https://youtu.be/cmtFI9eZ_UE) · **date:** 2025-11-02 · **length:** 5:01 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** ?
- **topics:** dev-tools, testing-verification · **tags:** go, go-1.24, release-notes, weak-pointers, garbage-collection, swiss-tables, os-root, path-traversal, testing, synctest, encoding-json, net-http, crypto

> Better Stack's five-minute roundup of Go 1.24's new features: weak pointers, cleanup functions, a go.mod tool directive, Swiss-table maps, os.Root, testing/synctest, and more.

## Summary
The video walks through the headline changes in Go 1.24, released the day it was recorded. Weak pointers can reference an object without keeping it alive, so a cache of large objects does not pin them in memory. A new add-cleanup function replaces set-finalizer for running code when an object becomes unreachable, and several cleanups can attach to one pointer. The go.mod tool directive lets executable dependencies be declared without a tools.go workaround. The map implementation moves to Swiss tables, and sync.Map is reworked on a concurrent hash-trie. os.Root confines file operations to one directory as a path-traversal defense. Testing gains context and change-directory helpers, b.Loop, and a synctest package with a fake clock. The strings and bytes packages gain iterator functions, crypto gains SHA3, HKDF, PBKDF2 and a random-text helper, net/http gets a protocols field, and build, install and test accept a JSON output flag. The speaker gives performance figures for maps but shows no benchmark run.

## Key ideas
- **Weak pointers reference an object without keeping it alive; once the GC reclaims it, the weak pointer's value returns nil. Intended for caches of large objects.** — Demonstrated with a 1000 KB blob: a regular pointer blocks reclamation, a weak pointer created with weak.Make lets the GC free it, and Value() then returns nil. ([0:00](https://youtu.be/cmtFI9eZ_UE?t=0))
- **Add-cleanup replaces set-finalizer for running a function when an object becomes unreachable. Multiple cleanups can attach to one pointer, and each can take arguments.** — Passing the resource to clean up as an argument is the suggested pattern. The speaker says set-finalizer use is now discouraged. ([1:01](https://youtu.be/cmtFI9eZ_UE?t=61))
- **The go.mod tool directive declares executable dependencies, removing the need for empty tools.go import files. The speaker calls it possibly his favorite change.** — One command adds a tool and writes the directive into go.mod. ([1:01](https://youtu.be/cmtFI9eZ_UE?t=61))
- **Maps move to Swiss tables, and sync.Map is reimplemented on a concurrent hash-trie that was first offered in the unique package in Go 1.23.** — Claimed gains: about 30% faster access and assignment for large maps, about 10% faster iteration overall, and about 60% faster iteration for low-load maps. The speaker says the new sync.Map beats the old one on nearly all benchmarks. ([1:01](https://youtu.be/cmtFI9eZ_UE?t=61))
- **os.Root (opened with the open-root function) restricts all methods on the returned root to one directory, which the speaker presents as a path-traversal defense.** — The security benefit is stated but not demonstrated in the video. ([1:01](https://youtu.be/cmtFI9eZ_UE?t=61))
- **Testing gets context and cleanup improvements, b.Loop, and synthetic time. The testing/synctest package with synctest.Run swaps the time package to a fake clock so a function that sleeps for a minute tests instantly.** — The t context is canceled just before cleanup functions run, which replaces manually canceling a context. A change-directory method is restored after the test or benchmark ends. ([2:20](https://youtu.be/cmtFI9eZ_UE?t=140))
- **strings and bytes gain iterator functions for lines, splitting (keeping or dropping the separator), whitespace fields, and predicate-based field splitting.** — Auto-captions render the Seq suffix as 'seek' (e.g. Lines, SplitSeq, SplitAfterSeq, FieldsSeq, FieldsFuncSeq). ([2:20](https://youtu.be/cmtFI9eZ_UE?t=140))
- **Crypto gets SHA3, HKDF, PBKDF2, and a cryptographically random string helper using base32. net/http gets a protocols field to choose HTTP/1, HTTP/2 over TLS, or unencrypted HTTP/2 on servers and clients. go build, install and test accept a JSON output flag.** — The speaker presents these as quality-of-life changes with no code shown. ([3:34](https://youtu.be/cmtFI9eZ_UE?t=214))

## Techniques
- **Weak-reference cache for large objects** — Store a weak pointer (created with weak.Make) instead of a strong pointer in the cache. Read it back with Value(); a nil result means the GC has reclaimed the object, so treat it as a cache miss. *When:* A cache of large objects where the cache itself must not keep those objects alive.
- **Cleanup on unreachable objects** — Attach a function with add-cleanup to the object, passing the resource to release as an argument. Several cleanups can be attached to one pointer. Do not use set-finalizer for new code. *When:* Releasing an external resource tied to a Go object when the GC finds it unreachable.
- **Executable dependencies via go.mod tool directive** — Add a tool with the single command the speaker shows; go.mod gets a tool directive. No empty tools.go file is needed. *When:* Pinning CLI tools such as code generators or linters as module dependencies.
- **Directory-confined file access with os.Root** — Call the open-root function on a directory. Perform file operations through the returned root so they cannot leave that directory. *When:* Opening paths that come from untrusted input, to block path traversal.
- **Context-aware and self-restoring tests** — Use the context method on testing T or B instead of creating and canceling a context by hand. Use the change-directory methods to change the working directory for one test, since the original is restored afterward. Use b.Loop instead of for range b.N. *When:* Writing tests or benchmarks that need a cancellable context or a different working directory, or that want cleaner benchmark loops.
- **Instant time-dependent tests with synctest** — Wrap the test body in synctest.Run. Inside it, time package calls use a fake clock, so code that sleeps or waits can be tested without real delays. *When:* Testing timeouts, retries, backoff, or any code that sleeps for long periods.
- **Iterator string splitting** — Use the iterator variants (Lines, SplitSeq, SplitAfterSeq, FieldsSeq, FieldsFuncSeq) in strings and bytes. The Seq suffix is spoken as 'seek' in the video. *When:* Walking over lines or split parts without allocating a full slice.

## Numbers
- Swiss-table maps: about 30% faster access and assignment for large maps ([1:01](https://youtu.be/cmtFI9eZ_UE?t=61))
- Map iteration about 10% faster across the board; about 60% faster for low-load maps ([1:01](https://youtu.be/cmtFI9eZ_UE?t=61))
- Weak-pointer demo uses a 1000 KB blob ([0:00](https://youtu.be/cmtFI9eZ_UE?t=0))
- synctest example: a function that waits about a minute runs instantly under the fake clock ([2:20](https://youtu.be/cmtFI9eZ_UE?t=140))

## Hot takes
- Title says 'HUGE UPDATE' but this is a five-minute feature list with one code example and no runnable demos or outputs. Quality is capped at 3 for that reason.
- Performance figures (Swiss tables, sync.Map, iteration) are stated without showing a benchmark. Treat them as the speaker's claims until checked against the release notes or benchmarks.
- The os.Root path-traversal benefit is asserted, not demonstrated.
- Speaker calls the go.mod tool directive possibly his favorite change; this is opinion, not evidence.

## Tools mentioned
Go 1.24, weak package (weak.Make, Value), add cleanup (replaces set-finalizer), go.mod tool directive, os.Root (open-root function), testing/synctest (synctest.Run), testing.B.Loop, crypto/sha3, HKDF, PBKDF2, net/http protocols field, encoding/json zero-value tag (transcribed 'emit zero', described as omit-zero behavior), go build / install / test -json flag
