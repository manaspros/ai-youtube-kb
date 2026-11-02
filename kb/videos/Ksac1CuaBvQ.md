# Google Just Released the ULTIMATE AI SDK (And It's Good)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Ksac1CuaBvQ` · [watch](https://youtu.be/Ksac1CuaBvQ) · **date:** 2025-11-02 · **length:** 5:32 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Google, OpenAI, Replicate, Vertex AI
- **topics:** voice-multimodal, dev-tools · **tags:** gemini, google-gen-ai-sdk, javascript, express, multer, video-analysis, image-generation, video-generation, grounding, openai-compatibility

> A short Better Stack walkthrough of Google's new Gen AI JavaScript SDK for Gemini: one client for text, image and video analysis and generation, plus the speaker's complaints about API design, model access and cost.

## Summary
The speaker builds a small Express app that uploads a video with Multer and sends it to Gemini through Google's Gen AI JavaScript SDK for analysis, and reports that the result comes back quickly and in detail. The app is then adapted to image generation, which means swapping the generate-content call for a generate-images call and returning base64 image bytes to the browser. Video generation is described as asynchronous: the job runs on Google's servers for minutes, so the client has to poll until it finishes and then download the file. The speaker lists further SDK features (function calling, file references in prompts, URL context, live audio, and grounding with Google Search, which he calls the standout). His criticisms are that the newest image model is only reachable through Vertex AI rather than the SDK or a third-party host like Replicate, that the API shape differs from OpenAI's so text-chat apps that switch models are simpler with the OpenAI SDK pointed at Gemini, and that Google's non-text models are cheaper, though no prices are given. The video is short, has poor audio, and offers little beyond a demo and opinions, so it is best treated as a quick orientation to the SDK.

## Key ideas
- **One Google Gen AI JavaScript SDK covers text, image, audio and video work with Gemini, so there is no need to juggle separate APIs for each modality.** — The speaker frames the SDK as a single entry point for multimodal processing across several models. He says it is a departure from how the older Google SDK was organised. ([0:00](https://youtu.be/Ksac1CuaBvQ?t=0))
- **Video analysis with Gemini is fast and detailed on a short clip, and the code change is small.** — He uploads a short family video and gets a detailed description back quickly. He says the video is not sped up. The SDK is flexible enough that the same app can be turned into image or video generation by changing a few lines. ([1:17](https://youtu.be/Ksac1CuaBvQ?t=77))
- **The whole integration lives in one Express endpoint, with a client constructed from an options object.** — The app is Express with Multer for uploads. The client is created with an object containing the API key, which he keeps in a .env file. The options object is there so Vertex AI settings can be added later. The call uses the models namespace's generate-content method with a prompt, a file path for the video asset and an optional system prompt. ([2:41](https://youtu.be/Ksac1CuaBvQ?t=161))
- **Image generation reuses the same client with a different method, and the result must be converted for the browser.** — The speaker switches the method to generate-images, picks a model, supplies a prompt, pulls the image bytes out of the result and base64-encodes them so the browser can render them. ([2:41](https://youtu.be/Ksac1CuaBvQ?t=161))
- **Video generation is asynchronous, so the client must poll for completion and then download the file.** — Generation runs on Google's servers and can take minutes. The code keeps checking until the job is done, then saves the file locally. He says the official docs cover this pattern well. ([2:41](https://youtu.be/Ksac1CuaBvQ?t=161))
- **Grounding with Google Search is the feature he rates most highly.** — He also lists function calling, uploading files and referencing them in prompts, passing URLs for the model to read, and real-time audio conversations as things the SDK can do. He only skims them. ([3:20](https://youtu.be/Ksac1CuaBvQ?t=200))
- **Newest image models are gated behind Vertex AI and not exposed through the SDK, which he finds frustrating.** — He says a Replicate account already gives access to the latest image model, and that a Veo 3 API could appear on Replicate before it reaches the Google SDK. He calls this illogical. ([4:04](https://youtu.be/Ksac1CuaBvQ?t=244))
- **The Gemini SDK's API shape differs from OpenAI's, which makes model-switching text apps easier through the OpenAI SDK.** — For text chat across providers he would point the OpenAI SDK at a Gemini key. He argues the native SDK is the better choice only for non-text modalities, where Google's models are cheaper, though he gives no prices. ([4:04](https://youtu.be/Ksac1CuaBvQ?t=244))

## Techniques
- **Single client, method per modality** — Create one Google Gen AI client with an options object holding the API key (keep the key in a .env file; the object leaves room for Vertex AI options). Use the generate-content method on the models namespace for analysis: pass the model, a prompt, the asset (a video file path in the demo) and an optional system prompt, then read the text from the result. For images, call the generate-images method with a model and a prompt, extract the image bytes and base64-encode them for the browser. *When:* When one app needs text, vision/video understanding and image generation from Gemini and you want a single SDK instead of separate APIs.
- **Poll-then-download for video generation** — Start the generation job, which runs on Google's servers and can take minutes. Poll the operation until it reports done, then download the output file to local storage. The speaker points to the official Gemini docs for the exact calls. *When:* When generating video with Veo or a similar long-running model, where a synchronous request would time out.
- **Express plus Multer upload endpoint** — Accept a video with Multer in an Express POST handler, then pass the saved file path to the SDK call. The demo app is built this way. *When:* For a quick browser-to-model prototype that analyses user-uploaded media.
- **OpenAI SDK pointed at Gemini for text** — Use the OpenAI client with a Gemini API key for text chat. This keeps one client shape when switching between providers. The speaker's advice is to switch to the Google SDK only for image, video and audio work. *When:* When an app swaps between many chat models and mostly handles text.

## Numbers
- Gemini returned a detailed analysis of a short clip quickly, shown in real time without speeding up the footage. No timing figure is given. ([1:17](https://youtu.be/Ksac1CuaBvQ?t=77))
- The speaker says Google's non-text models (image, video, audio) are much cheaper than alternatives, but gives no prices or ratios. ([4:04](https://youtu.be/Ksac1CuaBvQ?t=244))
- Video generation takes a few minutes on Google's servers; no exact duration is given. ([2:41](https://youtu.be/Ksac1CuaBvQ?t=161))

## Hot takes
- The SDK is good, but Google withholding the newest image model from the SDK (it is only on Vertex AI) makes no sense when Replicate already offers it.
- The Gemini SDK's API differs from OpenAI's for no clear benefit, so text-only, model-switching apps are easier to build with the OpenAI SDK pointed at Gemini.
- Google's image and video models are the reason to use the native SDK, because they are cheaper than the alternatives.
- Title hype ("ULTIMATE") exceeds the content: a single short demo with opinions, no code shown, no benchmarks, poor audio. Quality capped at 2.

## Tools mentioned
Google Gen AI SDK for JavaScript (Gemini API), Gemini, Veo 3 (said as VO3; the transcript caption is unclear), Express, Multer, Vertex AI, OpenAI SDK, Replicate, Google Search grounding

## Relevance to our work
- **agentos** (1/3): AgentOS puts an OpenAI-compatible proxy in front of agents. The speaker's point that the native Gemini API differs from OpenAI's and only pays off for non-text modalities is a data point for keeping the OpenAI-compatible surface and handling media routes separately. → *When adding multimodal routes to the Govrix proxy, decide whether image and video generation get their own endpoints instead of being forced through the chat-completions shape. Check the Gemini generate-images and video polling flow as a reference.*
