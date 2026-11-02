# 10 Crazy Ways To Use Nano Banana Pro

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `OWdlgdQSR60` · [watch](https://youtu.be/OWdlgdQSR60) · **date:** 2026-01-02 · **length:** 5:31 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Google, Make
- **topics:** voice-multimodal, models-research · **tags:** nano-banana-pro, image-generation, prompting, image-editing, infographics, storyboard, reference-images, grounding, synthid, sponsored

> A 5-minute AI LABS walkthrough of ten prompting and editing tips for Google's Nano Banana Pro image model, with a Make.com sponsor segment and a brief SynthID note.

## Summary
The host presents ten tips for Nano Banana Pro, Google's image model, described as a roundup of Google's own published guidance with the host's personal tests added. The tips cover iterative editing instead of regenerating, specific prompts with context words like "movie poster", infographic prompts that name a style and quote exact text, up to 14 reference images for keeping characters consistent, grounding generations with Google Search, editing (remove or add objects, restore, colorize), 3D-to-2D conversion, 4K output with explicit resolution and texture wording, step-by-step math solving, one-shot storyboards from a narrative, and using rough sketches or wireframes as inputs. The host also notes that higher plans drop the visible Gemini watermark in favour of an invisible SynthID mark, which the host says can also flag images from other models through style analysis; no evidence is shown for that second claim. The video ends with a sponsored segment for Make.com. Demos are single anecdotal runs with no failure rates, and the host reports several misses, including a font that did not change on a text edit, a duplicated text block and an unnatural face.

## Key ideas
- **Iterate on a generated image by asking the model to change one feature, rather than regenerating from scratch.** — The host says that if you like an image but dislike one feature, you should ask the model to change that feature instead of starting over. ([0:00](https://youtu.be/OWdlgdQSR60?t=0))
- **Be specific and add context words to set the style.** — Define every aspect of the desired output (for example, what kind of man). Adding a phrase like 'movie poster' produced a cyberpunk-style result, since clear context improves the output. ([0:00](https://youtu.be/OWdlgdQSR60?t=0))
- **Infographics work when you name the style and quote the exact text.** — The model can render legible, stylized text. Ask it to compress dense text or a PDF into a visual aid, specify the infographic style, and put any text that should appear in quotes. ([0:00](https://youtu.be/OWdlgdQSR60?t=0))
- **Up to 14 reference images enable entity locking across generations.** — Reference images keep characters or products consistent. The host also specifies exact expressions and actions per character. A caveat: a reference image given only for style was still used as a character. ([0:59](https://youtu.be/OWdlgdQSR60?t=59))
- **Ground generations with Google Search by asking the model to search first.** — Asking the model to search for the subject before generating is said to raise visual accuracy a lot. This is demonstrated with a single example. ([0:59](https://youtu.be/OWdlgdQSR60?t=59))
- **The model edits existing images: adds or removes objects, restores damaged photos, colorizes.** — In the host's test, shadows and highlights were applied correctly on a colorized old photo and the original grain was kept. A difficult panel was also colorized. ([0:59](https://youtu.be/OWdlgdQSR60?t=59))
- **Thinking before generation enables 3D-to-2D conversion, step-by-step math and storyboards from narrative.** — The host attributes this to a thinking step that interprets semantics. Examples: a floor plan from a 3D render, a worked equation written on paper, and a full storyboard from a short story-style description. ([2:09](https://youtu.be/OWdlgdQSR60?t=129))
- **Specify resolution and texture in the prompt to get 4K detail.** — The model supports up to 4K. The host says most users never request high resolution, and that the downloaded image was 4K with sharp leaf and water texture, even though the app did not show it clearly. ([2:09](https://youtu.be/OWdlgdQSR60?t=129))
- **Rough drafts and wireframes can serve as inputs, not only as references.** — A wireframe was turned into a UI mock, and a rough perfume-ad sketch with a style direction became a full visual. Caveat: text edits updated the words but kept the original font, and the text above and below was duplicated. ([3:10](https://youtu.be/OWdlgdQSR60?t=190))
- **Higher plans replace the visible watermark with an invisible SynthID mark, which the host says can be used for detection.** — The host says the mark lets you check whether an image is AI-generated and that style analysis can also flag images from other models. This is the host's claim and is not demonstrated. ([3:10](https://youtu.be/OWdlgdQSR60?t=190))

## Techniques
- **Iterative single-feature edits** — Keep the generated image and prompt only the change you want, e.g. 'change the X to Y', instead of regenerating the whole scene. *When:* When most of an image is right and one element is wrong.
- **Context word for style** — Add a genre or medium term (the host uses 'movie poster') to the prompt alongside full specification of subject details. *When:* When you want a specific aesthetic and the output is too generic.
- **Infographic prompt pattern** — State the infographic style, quote every piece of text that must appear, and ask the model to compress the source text or PDF into the visual. *When:* Turning dense documents or notes into a visual aid with legible labels.
- **Entity locking with reference images** — Upload up to 14 reference images of the characters or products. For each character, specify the exact expression and action in the prompt. *When:* Keeping the same characters across a storyboard or a set of images.
- **Search grounding before generation** — Ask the model to search Google for the subject first, then generate, so the image reflects real-world detail. *When:* Generating real objects, places or products whose accuracy matters.
- **Narrative storyboard prompt** — Describe the scene as a short story in one prompt and ask for a storyboard. Optionally attach one style reference image and separate character images. Note the caveat that style-only references may be used as characters. *When:* Quickly prototyping a sequence of frames with a consistent mood.
- **Sketch or wireframe as input** — Upload a rough sketch or UI wireframe with a style direction and ask for the finished image or interface. *When:* Turning a layout or draft into a polished visual, such as a UI mock or ad concept.
- **Resolution and texture in the prompt** — Include the target resolution (up to 4K) and surface or texture details, such as leaf texture or water reflections, in the prompt. *When:* When you need sharp output and the default resolution is not enough.

## Numbers
- Up to 14 reference images for entity locking ([0:59](https://youtu.be/OWdlgdQSR60?t=59))
- Model supports up to 4K output; the host downloaded a 4K image ([2:09](https://youtu.be/OWdlgdQSR60?t=129))
- Ten tips in total, summarised from a Google publication (per the host) ([0:00](https://youtu.be/OWdlgdQSR60?t=0))
- Make.com sponsor claims over 3,000 pre-built apps (sponsor claim, not verified) ([4:22](https://youtu.be/OWdlgdQSR60?t=262))

## Hot takes
- The host says the model can detect images from other models through style analysis. This is an unverified claim with no demo.
- Sponsored segment (Make.com) at 4:22 with promotional claims, which caps quality.
- Much of the content restates Google's published tips, and the host's additions are single anecdotal runs with no failure rates.
- Title hype ('10 Crazy Ways') is ahead of the substance; the host reports several misses (font not changed, duplicated text, unnatural face).

## Tools mentioned
Nano Banana Pro (Google image model), Gemini (watermark, plans), Google Search (grounding), SynthID (invisible watermark), Make.com (sponsor)
