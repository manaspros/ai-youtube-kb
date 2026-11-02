# I Turned My Wi-Fi Into a Surveillance System

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `9Tihk9_jUyo` · [watch](https://youtu.be/9Tihk9_jUyo) · **date:** 2026-10-12 · **length:** 10:05 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andris · **orgs:** Better Stack, Carnegie Mellon University, Google
- **topics:** models-research, voice-multimodal, security-guardrails · **tags:** wifi-sensing, csi, esp32-s3, pose-estimation, cross-modal-distillation, teacher-student, mediapipe, privacy, ruview, 802.11bf, generalization

> Walkthrough of Wi-Fi sensing (RuView): the speaker critiques its headline accuracy, rebuilds a cheap ESP32-S3 setup, and trains a Wi-Fi-only pose model from camera labels.

## Summary
The speaker explains Wi-Fi sensing via channel state information (CSI): body movement changes how a router's signal reflects around a room, so the per-packet measurements carry motion information. He describes the teacher-student method from a 2020 CMU work, where a camera-based pose model labels data and a Wi-Fi model learns to reproduce those labels. He critiques the open-source RuView project's claims, noting its 82% figure came from test examples drawn from the training recordings and accuracy fell to 11% on an unseen room, and that the viral skeleton demo was partly simulated. He then builds his own setup with three ~$10 ESP32-S3 boards running modified RuView firmware (per-board LED colors, and boards listening to each other for nine sensing lines instead of three). He collects about nine minutes of labeled data with a webcam running MediaPipe in the browser, so only text labels leave the browser. In a separate live session he reports 79.5% accuracy across his movement classes, with presence detection at 96%, and waving performing poorly at 13%. He closes by discussing privacy risks (sensing through walls, burglary and occupancy inference) and possible benefits (alarms, fall detection), while noting that the test was a single person in one room trained in one afternoon.

## Key ideas
- **Wi-Fi sensing reads channel state information (CSI) per packet across many frequency bands; body movement changes how the signal reflects, so the numbers shift when you move.** — The router computes CSI for every packet to decode data and normally discards it. Held onto, it encodes motion, but the raw values look random without a learned mapping. ([0:46](https://youtu.be/9Tihk9_jUyo?t=46))
- **Training uses a camera as teacher: a pose model labels video frames and a Wi-Fi-only model learns to predict those labels, after which the camera can be removed.** — The idea comes from a 2020 CMU work, and RuView's pose model is built on the same approach. ([1:55](https://youtu.be/9Tihk9_jUyo?t=115))
- **RuView's headline numbers are misleading: the 82% MMFI accuracy was measured on examples drawn from the training recordings, and accuracy fell to 11% on an unseen room.** — The speaker also says the viral real-time skeleton demo was partly simulated, with the skeleton coming from the webcam and a simulated Wi-Fi component. ([3:23](https://youtu.be/9Tihk9_jUyo?t=203))
- **Cheap hardware can be made more informative by making the nodes listen to each other, not just the router.** — Three ESP32-S3 boards (about $10 each) with modified RuView firmware give nine sensing lines rather than three. Per-board LED colors help tell the boards apart during placement. ([3:23](https://youtu.be/9Tihk9_jUyo?t=203))
- **Labeling can keep raw video on the client: MediaPipe runs in the browser, and only the label (e.g. squatting) is passed on.** — This is a privacy-preserving data-collection pattern. The speaker collected about nine minutes of data over three rounds of each movement. ([4:50](https://youtu.be/9Tihk9_jUyo?t=290))
- **On a fresh live session, the model scored 79.5% across its movement classes, with an empty room always correct.** — Per-class: jumping 97%, sitting 93%, spinning 92%, standing 84%, squats 79%, walking 70%, waving 13% (usually predicted as jumping). Arms appear too small to change the signal enough. ([6:05](https://youtu.be/9Tihk9_jUyo?t=365))
- **Presence detection is the easiest task and the most privacy-relevant one, since Wi-Fi passes through walls.** — Presence was 96% accurate in the speaker's room. The speaker suggests this could reveal when someone leaves home or sleeps, while the same sensing could serve home alarms or fall detection for elderly people living alone. ([7:04](https://youtu.be/9Tihk9_jUyo?t=424))
- **The speaker's own test has clear limits: one person, one room, one afternoon of training, and moving a board means retraining.** — He also notes that the 802.11bf Wi-Fi sensing standard was published last year, so routers may eventually sense out of the box. ([8:06](https://youtu.be/9Tihk9_jUyo?t=486))

## Techniques
- **Camera-supervised CSI training (teacher-student)** — Run a pose model on synchronized webcam frames (MediaPipe in the browser), log only the predicted labels alongside Wi-Fi CSI, and train a small model on CSI to predict the labels. Collect each movement across multiple rounds (the speaker used three, about nine minutes total). Drop the camera at inference time. *When:* When you need a sensor that is cheap and private at inference time but has no labels. Use it when a camera is available for data collection only.
- **Held-out environment evaluation for sensing models** — Do not score on examples from the training recordings. Hold out a separate session, and ideally a separate room or node placement, and report accuracy on it. The speaker's jump from 82% to 11% on an unseen room shows why. *When:* Before trusting any published accuracy for a sensing or CV model, and before claiming a demo generalizes.
- **Node-to-node links to multiply sensing lines** — Firmware on each board is changed so boards listen to each other as well as the router. With three boards this gives nine links instead of three, so the links cross the room from different angles. *When:* When a small number of sensing nodes gives too little spatial coverage.
- **Edge-only label export for privacy** — Run perception locally (in the browser or on device) and send only symbolic labels off the device, never raw frames. *When:* When collecting or sending sensitive sensor data (video, presence) to a backend.
- **Visual node identification during setup** — Give each board a distinct LED color in firmware so physical placement can be matched with what the signal view shows. *When:* During hardware placement and debugging of multi-node sensing setups.

## Numbers
- RuView's pose model claims a little over 82% accuracy on the MMFI dataset (40 people, four rooms), but the test examples came from the training recordings. ([1:55](https://youtu.be/9Tihk9_jUyo?t=115))
- Accuracy on an unseen room dropped to 11%, according to the speaker's account of the author's test. ([3:23](https://youtu.be/9Tihk9_jUyo?t=203))
- Three ESP32-S3 boards at about $10 each, so about $30 total hardware. Sensing lines went from 3 to 9 with board-to-board listening. ([3:23](https://youtu.be/9Tihk9_jUyo?t=203))
- About nine minutes of labeled training data, collected over three rounds of each movement. ([4:50](https://youtu.be/9Tihk9_jUyo?t=290))
- Live test: 79.5% correct overall across the classes, with 100% on an empty room. Jumping 97%, sitting 93%, spinning 92%, standing 84%, squats 79%, walking 70%, waving 13%. ([6:05](https://youtu.be/9Tihk9_jUyo?t=365))
- Presence detection (is anyone in the room) was right 96% of the time in the speaker's room. ([7:04](https://youtu.be/9Tihk9_jUyo?t=424))

## Hot takes
- The viral RuView demo's skeleton is said to come partly from the webcam and partly from a simulated Wi-Fi component, and the 82% headline number is in-distribution only.
- The speaker calls Wi-Fi sensing a privacy risk for burglary and occupancy inference, but the threat is speculative and this test was a single person in one room.
- The title's 'surveillance' framing overstates a single-room, single-person experiment. The summary numbers also have inconsistencies: the speaker says 'eight movements' but lists seven movement classes plus an empty room, and quotes 'about 80%' in the intro versus 79.5% later.

## Tools mentioned
RuView (open-source Wi-Fi sensing firmware and pose model; includes a fall detection feature), ESP32-S3 boards (about $10 each, three used), MediaPipe (Google, pose detection running in the browser), MacBook (ran the RuView pose model), MMFI public dataset (40 people, four rooms, camera plus Wi-Fi), 802.11bf (Wi-Fi sensing standard, mentioned as published last year)

## Relevance to our work
- **agentos** (1/3): Only tangential. The edge-label-only pattern (raw sensor data never leaves the client) is a privacy-by-design reference for PII handling. The speaker's generalization critique echoes the RAGAS and held-out-eval concerns, but it is about a sensing model, not an agent system. → *Optional reading: keep the raw-data-stays-local, send-only-labels pattern in mind when designing PII handling for camera or sensor inputs. Nothing to build now.*
