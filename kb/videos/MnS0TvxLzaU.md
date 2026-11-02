# I Tested a File Transfer Tool With No Network At All (decimen)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `MnS0TvxLzaU` · [watch](https://youtu.be/MnS0TvxLzaU) · **date:** 2026-09-02 · **length:** 9:49 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andrus · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** optical-file-transfer, qr-codes, fountain-coding, air-gap, file-transfer, camera-decoding, tuning, deciman

> Better Stack tests Deciman, a fountain-coded QR file transfer tool that needs no network; its defaults work phone-to-phone but fail laptop-to-phone until bytes per frame and fps are retuned.

## Summary
Better Stack tries Deciman, an open tool by Evan Crawley that sends a file from one device to another by flashing a stream of QR codes on one screen while the other device's camera decodes them, with no network involved. The speaker explains the core design: fountain coding, where each frame is a blend of pieces of the file so missed frames do not matter and the receiver only needs enough frames. The defaults send 2953 bytes per frame at 60 fps, a theoretical ceiling of about 177 KB/s, and the README claims about 128 KB/s measured phone-to-phone at close range. In a laptop-to-phone test at arm's length the speaker saw only about 3 KB/s with 1-2% of frames decoded, which he attributes to the 60 fps sender outpacing a 30 fps camera, LCD ghosting, and too little camera resolution per QR module. Repeating the test phone-to-phone reproduced the README numbers. For the laptop case he suggests dropping to 1465 bytes per frame and 24 fps, and says throughput rises a lot, though he gives no post-tuning figure. The video's takeaway is that optical transfer needs per-setup tuning rather than one default.

## Key ideas
- **Optical file transfer sends a file with no network stack: one device flashes QR frames on screen and another decodes them with its camera.** — The speaker positions this for air-gapped machines and devices with no Bluetooth or Wi-Fi, where a screen and a camera are the only reliable channel. The tool under test is Deciman by Evan Crawley. ([0:00](https://youtu.be/MnS0TvxLzaU?t=0))
- **Fountain coding removes the need for any specific frame to arrive.** — Each frame is a mathematical blend of pieces of the original file, and the sender keeps broadcasting. The receiver does not need frame 47 specifically, only enough frames in total, so dropped frames are harmless. ([1:05](https://youtu.be/MnS0TvxLzaU?t=65))
- **Throughput has a hard ceiling set by bytes per frame times fps, and the defaults are tuned for one scenario.** — 2953 bytes at 60 fps gives a theoretical ceiling near 177 KB/s; fountain overhead brings the README's claimed phone-to-phone peak to about 128 KB/s. 2953 bytes is QR version 40, a 177x177 module grid, which is why it is used as the chunk size. ([2:16](https://youtu.be/MnS0TvxLzaU?t=136))
- **Three variables trade off against each other: sender fps, code density per frame, and the receiver camera's resolving power.** — Denser frames mean fewer frames for the same file, but they need more camera resolution, steadier hands, and sharper focus to read each module. Defaults that work at close range fail at arm's length. ([3:18](https://youtu.be/MnS0TvxLzaU?t=198))
- **Laptop-to-phone failed at about 3 KB/s because of frame-rate mismatch, LCD ghosting and low resolution.** — A 60 fps sender against a camera that delivers 30 fps means each capture straddles two QR codes and decodes to nothing. LCD gray-to-gray transitions leave ghosting, and an arm's-length laptop rarely fills enough of the phone frame for the roughly 3-4 pixels per module needed. ([3:18](https://youtu.be/MnS0TvxLzaU?t=198))
- **iOS silently delivers 30 fps even when the app requests 60, and the project's own code and comments already note this.** — The speaker says main.ts handles the discrepancy and that a comment in the same file predicted the laptop-at-distance failure, so reading the code before testing would have saved the first attempt. ([4:40](https://youtu.be/MnS0TvxLzaU?t=280))
- **The receiver's separate capture-fps and decode-fps readouts diagnose the failure.** — Healthy capture with collapsing decode means the frames are too dense for the range. The speaker uses this split to decide whether to change density or fps. ([6:50](https://youtu.be/MnS0TvxLzaU?t=410))
- **For laptop-to-phone, retune the sender to coarser codes and a sub-camera frame rate.** — Speaker's suggested settings are 1465 bytes per frame (a coarser QR version with larger modules) and 24 fps, deliberately below the camera's 30 fps so frames are sampled cleanly one at a time. He reports much higher throughput but gives no measured number after the change. ([6:50](https://youtu.be/MnS0TvxLzaU?t=410))

## Techniques
- **Fountain-coded one-way transfer over a screen and camera** — Encode the file as an endless stream of blended (fountain-coded) frames rather than numbered chunks. The sender loops and the receiver stops once it has collected enough frames, whichever ones landed. Nothing needs retransmission or acknowledgement. *When:* One-way transfer with no network, air-gapped machines, or devices with no radio, where frames are lossy and the sender cannot wait for acks.
- **Tune bytes per frame and fps to the capture setup** — Start from defaults (2953 B/frame, 60 fps) for close phone-to-phone. For laptop-to-phone at arm's length, drop to 1465 B/frame (coarser QR version, larger modules) and 24 fps. Keep the sender fps below the camera's effective rate (here 30) so each capture lands on one code. *When:* Any setup where the sender is a laptop or monitor, the distance is more than a few centimetres, or the receiving camera delivers less than the requested fps.
- **Diagnose with capture fps versus decode fps** — Watch the receiver's two readouts. Capture fps high and decode fps low means the code density is too high for the camera's resolving power at that distance, so lower bytes per frame. If capture itself is low, lower the sender fps or check the camera's real rate. *When:* Debugging a low-throughput optical transfer before changing settings at random.
- **Check the camera's real frame rate and resolution budget before tuning** — Assume the camera may deliver less than requested (the speaker's iOS case gave 30 fps for a 60 fps request). Plan for roughly 3-4 camera pixels per QR module, so a version-40 code needs about 600+ px across in sharp focus. *When:* Sizing a QR-based transfer for a given sender and receiver pair, before running a long transfer.

## Numbers
- Default sender: 2953 bytes per frame at 60 fps, giving a theoretical ceiling of about 177 KB/s. ([2:16](https://youtu.be/MnS0TvxLzaU?t=136))
- README claims about 128 KB/s peak measured phone-to-phone at close range. ([2:16](https://youtu.be/MnS0TvxLzaU?t=136))
- Laptop-to-phone at arm's length with defaults: about 3 KB/s, with roughly 1-2% of transmitted frames decoded. ([3:18](https://youtu.be/MnS0TvxLzaU?t=198))
- Sender pushes 60 fps while the phone camera captures 30 fps. ([3:18](https://youtu.be/MnS0TvxLzaU?t=198))
- Reliable decoding needs about 3-4 camera pixels per QR module, meaning 600+ px across in sharp focus for a version-40 code. ([5:55](https://youtu.be/MnS0TvxLzaU?t=355))
- Recommended laptop-to-phone settings: 1465 bytes per frame and 24 fps. The speaker says throughput rises a lot but gives no measured figure. ([6:50](https://youtu.be/MnS0TvxLzaU?t=410))

## Hot takes
- Optical file transfer is not one-size-fits-all; each tool needs manual tuning for the sender, distance and camera in use.
- Defaults tuned for close phone-to-phone are expected to fail on a laptop monitor at arm's length, and the project's own code comments predicted this.
- A camera asked for 60 fps may silently deliver 30 fps, so the requested frame rate is not the real one.
- Practical use cases are air-gapped transfers and devices with no Bluetooth or Wi-Fi, where a screen and a camera are the only reliable channel.

## Tools mentioned
Deciman (optical file transfer tool by Evan Crawley; the title spells it 'decimen'), QR codes (version 40 = 177x177 modules, 2953 bytes per frame), fountain coding (concept), main.ts (Deciman source file, sender/receiver logic), iOS camera capture
