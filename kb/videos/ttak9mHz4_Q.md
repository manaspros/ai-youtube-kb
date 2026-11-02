# DeepSeek Vision Is Actually Impressive.... And Incredibly Cheap

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ttak9mHz4_Q` · [watch](https://youtu.be/ttak9mHz4_Q) · **date:** 2026-10-02 · **length:** 5:45 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Presenter (Better Stack, unnamed in transcript) · **orgs:** DeepSeek, Anthropic, Better Stack
- **topics:** models-research, token-cost-efficiency · **tags:** deepseek, vision, multimodal, ocr, image-input, files-api, cost, claude-comparison, hallucination

> Hands-on test of DeepSeek's experimental vision model on about 14 real-world photos, compared with Claude: strong on large text, weak on small or blurred text, with some hallucinated text, at a very low per-image price.

## Summary
The presenter tests DeepSeek's newly released vision model (named deepseek-v4-flash-vision-exp, where "exp" means experimental) on about 14 photos of food labels, a fruit, a leaf, a street lamp, a bench and a car, comparing its output with Claude. The model reads large, clear bold text well but misreads small print, misses a small "no palm oil" badge, and invents text on one pack. It misidentifies an apple as a peach and a plane tree leaf as an American sycamore, while Claude gets both right, including the Gala apple variety and the London plane. It does correctly identify the Victorian street lamp and the Tesla Model 3. The presenter stresses the price: about 14 photos cost under 1p, so he considers it viable for cheap in-app use despite the rough edges. The video also covers the three ways to send images and how the API resizes them. The evidence is one creator's informal test with a small sample, not a benchmark.

## Key ideas
- **DeepSeek's vision model is very cheap per image (quoted as about 0.00008 cents per photo), so it is pitched for running at scale behind your own apps.** — The presenter says 14 photos cost him less than 1p in total, and calls the price the main reason it is still viable despite rough edges. ([0:00](https://youtu.be/ttak9mHz4_Q?t=0))
- **Three ways to send an image, with size limits: base64 inline, external URL, or the Files API.** — Base64 counts against a 48 MB request body limit, so it only suits small images. An external URL can be up to 32 MB and must download within 60 seconds. The Files API allows larger images and is the option he uses for his demos. ([1:13](https://youtu.be/ttak9mHz4_Q?t=73))
- **The API resizes images before the model sees them, which can destroy small text.** — Small images are scaled up to roughly 394x384 and large ones scaled down to roughly 800x800, preserving aspect ratio. The presenter warns that fine detail and small text can be lost before the model reads it. ([1:13](https://youtu.be/ttak9mHz4_Q?t=73))
- **The model reads large, clear text well but struggles with small, blurred or angled text.** — On the peanut butter and tea packs it read the bold headline text correctly but misread a per-serving figure (15 g became 30 g) and missed a small 'no palm oil' badge and 'plant-based compostable tea bags' that Claude caught. ([2:15](https://youtu.be/ttak9mHz4_Q?t=135))
- **It can invent text that is not on the image.** — On a Jammy Dodgers pack it added 'The Rise of Gru', which is not on the label. The presenter links this to training-data bias: it fills gaps with plausible text when it cannot read something. ([3:34](https://youtu.be/ttak9mHz4_Q?t=214))
- **Object identification is inconsistent on everyday items.** — It called a Gala apple a yellow peach and said a London plane leaf was an American sycamore, while Claude got both right, including the apple variety and the tree species from location context. It did correctly identify the Victorian street lamp, the park bench and the Tesla Model 3. ([3:34](https://youtu.be/ttak9mHz4_Q?t=214))
- **Pick the vision model per task and verify its output against a stronger model before trusting it.** — The presenter's takeaway is that the model is rough but cheap enough to be viable, which implies checking results on the failure modes he found: small text, blur, and species or brand identification. ([4:40](https://youtu.be/ttak9mHz4_Q?t=280))

## Techniques
- **Pick the image input method by size** — Send small images as base64 in the request body (limit 48 MB total body). Pass larger images as an external URL (max 32 MB, must download within 60 s), or upload them with the Files API and reference the uploaded file, which the presenter uses for his demos. *When:* Choosing how to feed photos to a vision model whose request body or download limits you must respect.
- **Pre-crop or upscale small-text images before sending** — The API scales small images up to about 394x384 and large ones down to about 800x800 while keeping aspect ratio. Crop to the text region, or the image may lose small print before the model reads it. *When:* Reading labels, fine print, or any text smaller than the scaled-down resolution.
- **Cross-check a cheap vision model against a stronger one on a small sample** — Run the same set of photos through the cheap model and a stronger model (Claude here), then compare field by field. Look for misread numbers, missed small badges, and invented text. *When:* Before trusting a cheap vision model in a product, especially for OCR-style extraction or species/brand identification.

## Numbers
- Quoted price as low as about 0.00008 cents per photo. ([0:00](https://youtu.be/ttak9mHz4_Q?t=0))
- About 14 photos cost less than 1p in total. ([0:00](https://youtu.be/ttak9mHz4_Q?t=0))
- Base64 image input counts against a 48 MB request body limit. ([1:13](https://youtu.be/ttak9mHz4_Q?t=73))
- External image URL input: max 32 MB, download must complete within 60 seconds. ([1:13](https://youtu.be/ttak9mHz4_Q?t=73))
- Small images are scaled up to roughly 394x384 px; large images are scaled down to roughly 800x800 px (aspect ratio preserved). ([1:13](https://youtu.be/ttak9mHz4_Q?t=73))
- Peanut butter pack: per-serving figure read as 30 g where the label says 15 g. ([2:15](https://youtu.be/ttak9mHz4_Q?t=135))

## Hot takes
- The title's 'Actually Impressive' and 'Incredibly Cheap' overstate a test of about 14 informal photos; the presenter's own results show misreads, missed badges and invented text.
- The cost argument is the strongest claim, but the presenter does not measure accuracy against a set of ground truth labels, so the 'viable for your services' verdict is an impression, not a measured result.
- Claude outperforms DeepSeek on every blurred or small-text case shown, which undercuts the 'impressive' framing unless the workload is only large, clear text.
- Quality capped at 2: the title leans on hype and the evidence is a single small anecdotal test.

## Tools mentioned
DeepSeek V4 Flash Vision (deepseek-v4-flash-vision-exp, experimental), DeepSeek Files API, Claude (vision comparison)

## Relevance to our work
- **agentos** (1/3): AgentOS routes LLM traffic through one proxy; a vision-capable cheap model could sit behind the same proxy, but this is a single anecdotal test with no benchmark. → *If AgentOS ever proxies image requests, add a per-model cost and OCR-accuracy check to the router before enabling a cheap vision model.*
- **general** (1/3): Cheap multimodal models in Haiku-style pipelines are a cost-versus-accuracy trade-off worth checking against a stronger model on a small labelled sample. → *Run a small labelled OCR or image-extraction sample through a cheap vision model and Claude before choosing a model for a pipeline.*
