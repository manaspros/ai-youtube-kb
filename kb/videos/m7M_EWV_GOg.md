# Janus Pro-7B: DeepSeek's New Model

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `m7M_EWV_GOg` · [watch](https://youtu.be/m7M_EWV_GOg) · **date:** 2025-11-02 · **length:** 6:31 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed AI LABS narrator · **orgs:** DeepSeek, OpenAI, Hugging Face, Meta, Nvidia
- **topics:** voice-multimodal, models-research · **tags:** janus-pro, deepseek, multimodal, vision-language, image-generation, ocr, latex, hugging-face-spaces, open-weights

> A short hands-on demo of DeepSeek's Janus Pro 7B multimodal model on a Hugging Face Space, covering formula-to-LaTeX, image and code understanding, and text-to-image, with the speaker's training and limitation claims.

## Summary
The narrator tests Janus Pro 7B through a Hugging Face Space in two modes: multimodal understanding and text-to-image. It converts a handwritten-style math formula to LaTeX correctly, identifies the Python logo, and explains a Python prime-check screenshot section by section. Text-to-image output is detailed but has inaccurate faces. The second half summarizes the developers' claims: optimized training, expanded data, a larger model, and benchmark leadership on instruction following for image generation, which the narrator notes measures prompt adherence rather than image quality. The narrator also reports a stated training cost of about $120,000 and a 384x384 input-resolution cap that hurts OCR and fine detail. Evidence is four anecdotal prompts on one model with no quantitative evaluation of the narrator's own, so treat it as a quick capability probe, not a benchmark.

## Key ideas
- **Janus Pro is a multimodal model with two modes on a Hugging Face Space: image understanding and text-to-image generation. The narrator tests the 7B variant.** — The narrator frames it as competing with DALL-E and other image models. The variant size is stated as 1.3B at the start and 1.5B later, so the size is inconsistent in the transcript. ([0:00](https://youtu.be/m7M_EWV_GOg?t=0))
- **Formula-to-LaTeX conversion worked, and the narrator verified it by rendering the output in an online LaTeX viewer.** — This is a practical OCR-style use case. The narrator says the output was accurate and fast, and that the Space had a GPU queue delay. ([1:19](https://youtu.be/m7M_EWV_GOg?t=79))
- **Image understanding handled a logo and a code screenshot. The model identified the Python logo and explained a prime-checking snippet section by section.** — It gave a per-section description and an overall summary that the code checks primality. The narrator judged both answers correct. ([2:23](https://youtu.be/m7M_EWV_GOg?t=143))
- **Text-to-image output was detailed for a complex scene prompt, but faces were drawn inaccurately.** — The narrator attributes the face problem to the low input and output resolution. This is a single-prompt observation, not a systematic test. ([3:31](https://youtu.be/m7M_EWV_GOg?t=211))
- **Developer claims credit optimized training, expanded data, and scale. The narrator says the benchmark leadership on image-generation instruction following measures prompt adherence, not image quality.** — Janus Pro is said to lead on average multimodal performance and on instruction following for image generation. The narrator's caveat is that these benchmarks do not measure how good the images look. ([4:30](https://youtu.be/m7M_EWV_GOg?t=270))
- **The stated limits are a 384x384 maximum input resolution, which weakens OCR on fine detail, and low resolution that degrades faces in generation.** — The narrator suggests scaling resolution could fix this later, but gives no evidence for it. ([4:30](https://youtu.be/m7M_EWV_GOg?t=270))
- **Claimed training cost was about $120,000, which the narrator says is much lower than what DALL-E 3-class models cost. No source is given for the comparison.** — The claimed cost comes with a claimed training setup: the smaller variant on 16 A100 nodes for 7 days, and the 7B on 32 nodes for 14 days. ([4:30](https://youtu.be/m7M_EWV_GOg?t=270))

## Techniques
- **Quick multimodal capability probe** — Test a vision-language model on a fixed set of four prompts: formula to LaTeX (then render the output to verify), logo identification, explanation of a code screenshot, and a complex text-to-image scene prompt. Judge each output by eye, and compare face and fine-detail rendering across tasks. *When:* When you want a fast, cheap read on whether a new open multimodal model is worth a closer evaluation. It is not a substitute for a benchmark with a fixed rubric.
- **Round-trip check for OCR-to-markup output** — Convert the model output (here LaTeX) and render it in an independent viewer, then compare with the source. Rendering the output is a more reliable check than reading the markup. *When:* When a multimodal model turns images of structured content (formulas, tables, diagrams) into code or markup that a downstream tool will consume.

## Numbers
- Input resolution cap of 384x384 pixels, limiting OCR fine detail ([4:30](https://youtu.be/m7M_EWV_GOg?t=270))
- Smaller variant trained in 7 days on 16 Nvidia A100 nodes (stated as 1.5B) ([4:30](https://youtu.be/m7M_EWV_GOg?t=270))
- 7B variant trained in 14 days on 32 nodes ([4:30](https://youtu.be/m7M_EWV_GOg?t=270))
- Total training cost around $120,000 (developer figure as relayed) ([4:30](https://youtu.be/m7M_EWV_GOg?t=270))
- Video length 6:31; four demo prompts on one model ([0:00](https://youtu.be/m7M_EWV_GOg?t=0))

## Hot takes
- Speaker calls the model impressive given how cheap DeepSeek models are to run, despite the face artifacts.
- Speaker says benchmark leadership on image-generation instruction following tells you about prompt adherence, not overall image quality.
- Speaker says the training cost is significantly lower than DALL-E 3-class training, with no source for that comparison.
- Speaker frames the release as a US-China AI race question, then argues for open research citing Yann LeCun. This framing is outside the technical content.

## Tools mentioned
Janus Pro 7B (DeepSeek, multimodal), Janus Pro 1.3B / 1.5B (mentioned, sizes inconsistent in transcript), Hugging Face Spaces, DALL-E 3 (comparison only), Python (screenshot content), Online LaTeX viewer (unnamed)

## Relevance to our work
- **agentos** (1/3): AgentOS routes OpenAI-compatible traffic and has no vision path, so this model is only marginally relevant. The 384x384 input cap matters if images are ever routed through the proxy.
