# Get 400K+ Al Apps on this site...

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `jEYHsyiTwso` · [watch](https://youtu.be/jEYHsyiTwso) · **date:** 2025-11-02 · **length:** 5:49 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Hugging Face
- **topics:** models-research, local-ai · **tags:** hugging-face, spaces, open-weight-models, image-generation, image-to-3d, demo-hosting, flux

> A five-minute tour of Hugging Face Spaces: a public directory of 400K+ community AI apps and hosted open models, shown through logo placement, image-to-3D, image extension and comic generation demos.

## Summary
The host presents Hugging Face Spaces as a public directory of over 400,000 AI apps, plus a place where developers release and host models such as o3 mini (named as a ChatGPT model), Flux and Janus Pro 7B for free community use. He points to categories, a Spaces-of-the-week feature and a few playable games. He then runs four demos: a logo-on-mug compositor, the Trellis image-to-3D app with GLB export, an image extender set to 16:9, and the AI Comic Factory, where speech bubbles failed to render on one run and were not fixed. He recommends hosting your own project as a Space so people can try it, and says he uses Hugging Face mainly for image generation because the Flux rate limits are generous. The video is a casual directory tour with no benchmarks, code or setup steps.

## Key ideas
- **Hugging Face Spaces is a public directory of over 400,000 AI apps, browsable by category.** — Categories include image generation, translation, speech synthesis, 3D modeling, chatbots and sentiment analysis. There is also a weekly Spaces-of-the-week feature and some AI-powered games (Neural Jam, an AI detective puzzle game). ([0:00](https://youtu.be/jEYHsyiTwso?t=0))
- **Hugging Face also hosts community-released models you can run without local hardware.** — He lists Janus Pro 7B, Qwen 2.5 Max, Flux Dev and Midjourney as available, and says most are open source and hosted free by the community. He also mentions an o3 mini release, which he attributes to ChatGPT. ([1:26](https://youtu.be/jEYHsyiTwso?t=86))
- **A Space can be a single-purpose compositor: upload an input image, describe the target, and specify placement.** — In the logo demo he uploads a logo, describes it as a circular maze, and asks for it to be placed on the side of a cup. The tool returns the original logo and a generated result. ([1:26](https://youtu.be/jEYHsyiTwso?t=86))
- **Image-to-3D apps export standard formats for downstream tools.** — The Trellis app turns one uploaded image into a 3D asset. The speaker exports it as GLB, which he describes as a format used in 3D apps such as Blender. He judges the car model accurate and says it could matter for the 3D industry. ([2:55](https://youtu.be/jEYHsyiTwso?t=175))
- **Image extension is controlled by an aspect-ratio setting.** — He uploads a photo, prompts a man standing on a red carpet, sets the aspect ratio to 16:9 and generates. He reports it was fast and looked good, with no quality numbers given. ([2:55](https://youtu.be/jEYHsyiTwso?t=175))
- **The AI Comic Factory shows that generated outputs can miss parts of the spec.** — He picks a style and grid layout, enters a Jurassic Park-style story, and sets jungle and island as styles. The speech bubbles did not appear on that run, and he did not show a fix. He also notes that a more detailed story option was not visible. ([4:25](https://youtu.be/jEYHsyiTwso?t=265))
- **Publishing your own project as a Space gives you a public demo and a community audience.** — He says creators can build their own Spaces using the provided intro guide and setup instructions, and that this also contributes to the community. He says he sees Flux reused across many Spaces, including one by its developers. ([4:25](https://youtu.be/jEYHsyiTwso?t=265))

## Techniques
- **Discover demo apps via the Spaces directory** — Open the Hugging Face Spaces directory, browse by category (image generation, 3D, speech, translation, chatbots), or check the weekly Spaces-of-the-week list. Open a candidate and try it in the browser. *When:* You want to evaluate a model or app quickly without installing anything.
- **Try an open model through its hosted demo before running it locally** — Open the model's Hugging Face page (he uses Flux as the example), find the Spaces that use it, and generate directly in the browser. He reports generous rate limits for image generation. *When:* You lack local GPU capacity or want to compare outputs before committing to a self-hosted setup.
- **Publish a project as a Space to share a demo** — Create a Space and follow Hugging Face's introductory guide. The video shows no config steps, commands or file layout. *When:* You want a public, shareable demo of a project and feedback from the community.

## Numbers
- Hugging Face Spaces hosts over 400,000 AI apps. ([0:00](https://youtu.be/jEYHsyiTwso?t=0))
- Image extender demo uses a 16:9 aspect ratio. No generation time or quality metric is given beyond 'pretty fast'. ([2:55](https://youtu.be/jEYHsyiTwso?t=175))
- Video length is 5:49. Contains no benchmarks, latencies, prices or token counts. ([0:00](https://youtu.be/jEYHsyiTwso?t=0))

## Hot takes
- The 400,000-app figure sets up a casual directory tour, not a technical evaluation. The title frames it as a must-see site, but the substance is four unbenchmarked demos.
- He calls Flux 'the best model' for image generation with no comparison shown.
- The comic demo produced output that missed part of the spec (speech bubbles), and the speaker did not explain it. Free hosted demos may differ from the full product.
- Some model names in the transcript are misspelled (Quen, ChatGPT's o3 mini), so treat the names as approximate.

## Tools mentioned
Hugging Face Spaces, Flux (Flux Dev), Trellis, Janus Pro 7B, Qwen 2.5 Max, Midjourney, o3 mini (attributed to ChatGPT), AI Comic Factory, Neural Jam, Blender (mentioned as the target for GLB export), GLB (3D file format)

## Relevance to our work
- **agentos** (1/3): Hugging Face is a source of open-weight models that could be candidates for the InferCraft serving stack. The video does not discuss serving, KV cache or throughput. → *Skim Hugging Face model pages for open-weight candidates (Janus Pro, Flux, Qwen) when choosing models to benchmark on the RTX 5090, but treat this as low priority.*
- **general** (1/3): A low-effort way to find hosted open models and demo apps to compare against our own work. → *Bookmark the Hugging Face Spaces directory as a quick check for new open-weight models.*
