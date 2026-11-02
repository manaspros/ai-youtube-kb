# Bun.Image Makes Your Entire Image Pipeline Obsolete

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Tnmyb_pdM10` · [watch](https://youtu.be/Tnmyb_pdM10) · **date:** 2026-06-02 · **length:** 4:34 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Host (unnamed Better Stack presenter) · **orgs:** Bun, Vercel, Better Stack, Waku
- **topics:** dev-tools, infra-cost-scaling · **tags:** bun, bun-image, image-processing, sharp, libvips, webp, thumbhash, placeholders, static-site, nodejs, runtime-comparison

> Short walkthrough of Bun.Image, the built-in image API in Bun 1.3.14, with resize, WebP conversion and ThumbHash placeholders, and a claim that it is faster than Sharp.

## Summary
The host presents Bun.Image, an image processing API shipped in Bun 1.3.14 that resizes, crops and converts images with no native dependencies and runs off the main thread. He argues it is faster than Sharp (metadata reads about 70x faster, resizing about 30% faster), and that Sharp needs a platform-specific libvips binary, which causes Docker and CI install failures. The demo runs on his static Waku blog: one script resizes a profile photo to 800px wide, converts it to WebP at reduced quality, and cuts its size by about 99%. He then shows resize filters, rotate/flip and brightness/saturation, and a placeholder function that produces ThumbHash blurry images (28-byte hashes) embedded as base64 for instant loading. He notes progressive JPEG as an alternative for a similar effect, and mentions S3-compatible input and output and format fallbacks without demoing them. His verdict: a no-brainer if you already run Bun, but on Node, Sharp is battle-tested and not worth switching runtimes for. He closes by speculating that Bun is building a full-stack platform (SQLite, S3, Postgres, now images) and may add auth next.

## Key ideas
- **Bun 1.3.14 ships image processing built into the runtime, so no native libvips binary or platform-specific install is needed.** — Resize, crop and format conversion with zero native dependencies. Work runs off the main thread, so a server is not blocked during processing. Motivation given is that Sharp's libvips binary breaks Docker and CI builds. ([0:00](https://youtu.be/Tnmyb_pdM10?t=0))
- **Bun.Image is claimed to beat Sharp on common operations.** — Metadata reads about 70x faster and resizing about 30% faster, per the speaker's benchmarks. He cites Sharp at over 55M weekly npm downloads and as the library Next.js uses for image optimization. No benchmark setup is shown. ([0:50](https://youtu.be/Tnmyb_pdM10?t=50))
- **The demo is a one-script image optimization pass on a real blog with large images.** — Load the image, resize to 800px width with height derived from aspect ratio, set WebP output with reduced quality, then write the output (a promise, so await it). He reports a 99% size reduction on the profile photo. ([0:50](https://youtu.be/Tnmyb_pdM10?t=50))
- **A ThumbHash placeholder gives a blurry preview with no extra network request.** — The placeholder function encodes each image as a 28-byte hash. The result is stored as base64 so it can sit inline, for example as a CSS background while the full image loads, avoiding a separate fetch for the placeholder. ([2:03](https://youtu.be/Tnmyb_pdM10?t=123))
- **Progressive JPEG is an alternative when you want a similar progressive-loading effect.** — Setting progressive to true on JPEG output gives a comparable loading experience to the placeholder approach, per the speaker. ([3:18](https://youtu.be/Tnmyb_pdM10?t=198))
- **Verdict: adopt Bun.Image on Bun, keep Sharp on Node.** — On Bun it is a no-brainer. On Node, Sharp is battle-tested and switching runtimes just for image processing is not justified. ([3:18](https://youtu.be/Tnmyb_pdM10?t=198))
- **Bun is building up batteries-included platform features, and images are the latest.** — Built-in SQLite, S3 and Postgres come before images. The speaker speculates Bun could be aiming to be a Rails/Laravel-style full-stack platform and that auth is the likely next addition. He flags this as speculation. ([3:18](https://youtu.be/Tnmyb_pdM10?t=198))

## Techniques
- **Resize, convert and compress with Bun.Image** — Load the image through the Bun image API, resize with a target width (height derived from aspect ratio), choose a WebP output format at a reduced quality, then await the write to a file. The speaker says the surrounding script can be trimmed down to these few lines. Exact API casing and option names are not shown on screen and should be checked against the Bun docs. *When:* Build-time or request-time image optimization on a Bun project, where you want to drop native image dependencies such as Sharp and libvips.
- **Optional image operations** — Chain further operations on the same image: a resampling filter to change the resize kernel, rotate or flip, and brightness or saturation adjustments. Only mentioned, not demoed in detail. *When:* Further size reduction or simple transforms in the same pipeline.
- **ThumbHash blur placeholders** — Loop over every image in a directory matching image extensions, resize without cropping or upscaling, run the placeholder function to produce a 28-byte ThumbHash, store the result as base64 in a JSON object or file, then inline it as a CSS background or an image src while the real image loads. *When:* Slow connections or image-heavy static sites where layout and perceived load time matter and an extra placeholder request is undesirable.
- **Progressive JPEG for a loading effect** — Set the progressive option to true when encoding JPEG output. *When:* You need a JPEG and want progressive rendering rather than a separate placeholder.

## Numbers
- Bun.Image ships in Bun 1.3.14. ([0:00](https://youtu.be/Tnmyb_pdM10?t=0))
- Sharp has more than 55 million npm downloads a week. ([0:50](https://youtu.be/Tnmyb_pdM10?t=50))
- Metadata reads are about 70x faster than Sharp, and resizing about 30% faster, per the speaker's benchmarks. ([0:50](https://youtu.be/Tnmyb_pdM10?t=50))
- Profile picture optimization cuts file size by about 99%, using an 800px-wide WebP at reduced quality. ([0:50](https://youtu.be/Tnmyb_pdM10?t=50))
- ThumbHash placeholders encode any image as a 28-byte hash. ([2:03](https://youtu.be/Tnmyb_pdM10?t=123))

## Hot takes
- Bun is probably building a Rails/Laravel-style full-stack platform and auth is likely next (speculation, flagged as such).
- Bun.Image beats Sharp on speed. Only the speaker's own benchmark numbers are given, with no method shown.
- On Node, keep Sharp. Switching runtimes just for image processing is not worth it.

## Tools mentioned
Bun 1.3.14 (Bun.Image / image API), Sharp, libvips, WebP, ThumbHash, Waku, Next.js, Bun SQLite, Bun S3, Bun Postgres, Vercel Zero (referenced, not discussed)
