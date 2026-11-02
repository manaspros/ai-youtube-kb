# Cloudflare Just Saved 100TB of Memory

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `RTmTebnxwKc` · [watch](https://youtu.be/RTmTebnxwKc) · **date:** 2026-10-02 · **length:** 9:17 · **format:** review · **quality:** 4/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Cloudflare, Better Stack
- **topics:** infra-cost-scaling, dev-tools · **tags:** rust, dns, memory-layout, caching, allocator, data-structures, cloudflare, performance

> Cloudflare cut DNS cache memory per entry by 56% with five Rust data-layout changes (Vec to Box, flattened lists, deduped owner names, boxed enum variants, raw wire-format bytes), freeing about 100TB fleet-wide.

## Summary
This Better Stack video walks through Cloudflare's write-up of how it shrank the per-entry memory of the DNS cache behind 1.1.1.1, which is written in Rust and holds over 250 billion entries. At that scale, each wasted byte per entry costs roughly 250GB. The changes were: replacing growable Vec and String fields with fixed-size Box types for data that is never mutated after insert; merging three parallel record lists into one list with two 16-bit offsets; dropping the owner name when it matches the query name; boxing the rare large enum variants so common A and 4A records stay small; and finally storing record data as one contiguous buffer in DNS wire format. The combined effect reported is per-entry size down from 953 to 420 bytes, allocated memory per entry down from 1.1KB to 461 bytes, insert throughput up 43%, lookups 19% faster, and p99 resident memory down 43% on production traffic. The narrator presents the fleet-wide figure of roughly 100TB freed. The video closes by asking whether this kind of optimization should happen up front or only once cost justifies it, without answering.

## Key ideas
- **At massive scale, per-entry overhead dominates cost** — Cloudflare's DNS cache holds over 250 billion entries, so one wasted byte per entry is roughly 250GB of RAM across the fleet. This framing motivates the whole exercise. ([0:00](https://youtu.be/RTmTebnxwKc?t=0))
- **Vec and String carry unused capacity for write-once data** — Cache entries were written once and only read afterwards, so the capacity field and reserved spare slots were pure waste. Switching the 8 Vec and String fields to fixed-size boxes saved 8 bytes of capacity per field plus the unused heap, about 64 bytes per entry and over 15TB across the fleet. ([1:14](https://youtu.be/RTmTebnxwKc?t=74))
- **Parallel lists that are always used together can be flattened** — The answer, authority and additional record lists were always written, read and ordered together. They became one list of records with two u16 offsets marking where answers and authority end. This replaced two 16-byte headers with two 2-byte numbers, saving about 28 bytes per entry. ([2:42](https://youtu.be/RTmTebnxwKc?t=162))
- **Remove fields that duplicate a key already stored** — Each record's owner name usually equals the query name, which was already the cache key. The owner is now an optional box that is None when it matches the query, and is stored only in cases like CNAME chains where it differs. This saves a heap allocation per record. ([3:47](https://youtu.be/RTmTebnxwKc?t=227))
- **Enum size is set by the largest variant, so common small variants pay for rare large ones** — The record-data enum was 144 bytes because of the NAPTR variant, while A records need only 4 bytes. Since A and 4A records are most of the traffic (about 56% and 25% in Cloudflare's benchmark mix), the common variants were kept inline and the large ones boxed. That saves about 120 bytes per A or 4A record. ([3:47](https://youtu.be/RTmTebnxwKc?t=227))
- **Boxing trades padding for allocator rounding and worse locality** — The allocator (transcribed as gemmalloc) rounds requests up to fixed bins, so a 40-byte record takes 48 bytes. Boxed data also lands far from the entry, costing an extra cache line on read. These costs motivated the final change. ([6:15](https://youtu.be/RTmTebnxwKc?t=375))
- **Store record data as one contiguous buffer of wire-format bytes** — Each record became a 2-byte length prefix followed by its DNS wire-format bytes, all in one boxed u8 array per entry. This removes per-record allocations and rounding, restores locality, and avoids re-serializing on cache hits. Only records containing domain names (CNAME, NS, MX, SOA) still need parsing, because DNS name compression requires rewriting them. ([7:33](https://youtu.be/RTmTebnxwKc?t=453))
- **Reported net results** — Per-entry footprint went from 953 to 420 bytes, and allocated memory per entry from 1.1KB to 461 bytes. Insert throughput rose from 625k to 893k entries per second, and lookup time fell from 828 to 670 ns. Production p99 resident memory dropped from 9.3GB to 5.3GB, which Cloudflare projects to roughly 100TB fleet-wide and which the narrator says equals about 130 gen-13 servers' RAM. The freed space is planned for a larger cache. ([7:33](https://youtu.be/RTmTebnxwKc?t=453))

## Techniques
- **Swap growable Vec/String for Box<[T]> / Box<str> on write-once data** — In Rust, change struct fields from Vec<T> and String to Box<[T]> and Box<str> once the value is built and never grows. This drops the 8-byte capacity field and the reserved slack. Measure the struct size and the heap bytes allocated per entry before and after. *When:* Cache entries or any long-lived records that are built once and then only read.
- **Flatten parallel same-length-lifecycle lists into one list plus small offsets** — If several Vecs are always written, read and ordered together, store one Vec of the combined items and a few u16 boundary offsets. Verify that the count per group cannot exceed the offset type's range before choosing the width. *When:* Structured records split into sections (answer/authority/additional style) that always travel as a unit.
- **Store a field only when it differs from a value already stored** — Make the field Option<Box<T>>. Set it to None when it equals the key or parent value, and populate it only for exceptions such as alias chains. *When:* A per-record field usually repeats data the container already holds, such as a name equal to the lookup key.
- **Box rare large enum variants, keep common small ones inline** — Check the size of each enum variant and the real traffic mix. Box the variants that are large and rare, so the enum is sized by the common case. Watch for allocator rounding and pointer-chasing costs that boxing adds. *When:* A single enum covers many record or message kinds with very uneven size and frequency.
- **Keep cached payloads in the wire or serialized format** — Store each item as a length-prefixed byte run in one contiguous buffer, copy it straight to the output on hit, and parse only the fields that must be rewritten (for DNS, names needing compression). This removes per-item allocation, restores locality and skips re-serialization. *When:* A cache is read far more often than written and the output format is already known.
- **Audit per-entry footprint and allocated bytes separately** — Track both the in-struct size and the heap bytes actually allocated per entry, including allocator rounding. Compare insert throughput and lookup latency alongside, since layout changes can help both memory and speed. *When:* Optimizing a memory-heavy cache or data structure, to confirm that a change helps and to catch hidden costs.

## Numbers
- DNS cache holds over 250 billion entries; one wasted byte per entry costs about 250GB of RAM ([0:00](https://youtu.be/RTmTebnxwKc?t=0))
- Vec/String to Box change: 8 bytes of capacity saved per field, 64 bytes per entry, over 15TB fleet-wide ([1:14](https://youtu.be/RTmTebnxwKc?t=74))
- Record list flattening: about 28 bytes saved per entry (two 16-byte headers replaced by two 2-byte offsets) ([2:42](https://youtu.be/RTmTebnxwKc?t=162))
- Enum size 144 bytes (NAPTR variant 136 bytes) versus 4 bytes needed for an A record; about 120 bytes saved per A or 4A record ([3:47](https://youtu.be/RTmTebnxwKc?t=227))
- Benchmark traffic mix: 56% A records, 25% AAAA (4A) records ([4:54](https://youtu.be/RTmTebnxwKc?t=294))
- Example allocator rounding: a 40-byte MX record is allocated as 48 bytes ([6:15](https://youtu.be/RTmTebnxwKc?t=375))
- Per-entry footprint 953 bytes down to 420 bytes (56% smaller) ([7:33](https://youtu.be/RTmTebnxwKc?t=453))
- Allocated memory per entry 1.1KB down to 461 bytes (58% cut) ([7:33](https://youtu.be/RTmTebnxwKc?t=453))
- Insert throughput 625,000 to 893,000 entries per second (+43%) ([7:33](https://youtu.be/RTmTebnxwKc?t=453))
- Lookup latency 828 ns down to 670 ns (19% faster) ([7:33](https://youtu.be/RTmTebnxwKc?t=453))
- Production p99 resident memory 9.3GB down to 5.3GB (43% cut); fleet-wide roughly 100TB freed, about 130 gen-13 servers' worth of RAM ([7:33](https://youtu.be/RTmTebnxwKc?t=453))

## Hot takes
- This is a walkthrough of a Cloudflare engineering blog post, not original measurement. The numbers are Cloudflare's, and the 100TB fleet-wide figure is an extrapolation the narrator repeats without independent checking.
- The narrator says the 2018 design was built when RAM was cheaper and asks whether such optimization should happen up front or only once cost justifies it. The video raises the question but does not answer it.
- Auto-captions render several terms oddly (for example 'veck' for Vec, 'gemmalloc' for the allocator name); the names here follow the transcript and may be wrong.
- Quality is capped at 4 because the content is a secondary summary, though the data is hard-won and specific.

## Tools mentioned
Rust, Cloudflare 1.1.1.1 (public DNS resolver), Big Pineapple (Cloudflare's DNS resolver software, Rust), gemmalloc (allocator, as transcribed; may be an auto-caption error), DNS wire format

## Relevance to our work
- **agentos** (1/3): AgentOS's Rust L1 proxy keeps in-memory state, and the layout techniques (write-once Box fields, wire-format storage, per-entry footprint audits) could apply there, but the video is about a DNS cache and does not touch the AgentOS pillars directly. → *Audit the Rust proxy's hot in-memory structures: record struct size and heap bytes per entry, and switch write-once Vec/String fields to Box<[T]>/Box<str>, before adding any new caching layer.*
