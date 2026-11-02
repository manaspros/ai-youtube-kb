# I Can Control My PC From Anywhere in the World (JetKVM)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `jNFv1Lr2Db4` · [watch](https://youtu.be/jNFv1Lr2Db4) · **date:** 2026-11-01 · **length:** 10:07 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, JetKVM, Gigabyte, Nvidia
- **topics:** dev-tools · **tags:** jetkvm, kvm-over-ip, remote-power-on, atx, homelab, hardware, webrtc, self-hosting, remote-desktop

> Better Stack walkthrough of wiring a JetKVM (open-source KVM-over-IP) plus its ATX power-button extension board into a workstation so it can be powered on and used remotely from a browser or phone.

## Summary
Andrus from Better Stack shows how he added a JetKVM and its ATX extension board to his workstation so he can power it on remotely. He covers wiring the ATX board's ribbon cable to the motherboard's F-Panel header, keeping the case's original power button via DuPont jumpers, and the four cables into the JetKVM (Ethernet, HDMI from the GPU, USB-C to the host, ATX extension). The JetKVM is powered from a wall charger through the ATX board, not from the host's USB ports, because host USB is off when the machine is off. He then demos powering on, booting into BIOS and Windows, shutting down, and doing the same from the free JetKVM cloud app on a phone. The video is explicitly not sponsored. It is a hands-on hardware tutorial with no benchmarks beyond vendor-stated specs, and the one troubleshooting tip is that a VPN browser extension blocking WebRTC stalls the video stream.

## Key ideas
- **A KVM-over-IP device sees the host's screen over HDMI and acts as a keyboard and mouse over USB, so it can be used remotely from a browser, including before the OS loads.** — JetKVM captures HDMI up to 1080p60 and presents itself to the host as a USB keyboard and mouse. The speaker says the vendor claims 30 to 60 ms latency. Because it works at the hardware level, BIOS access is possible. ([0:03](https://youtu.be/jNFv1Lr2Db4?t=3))
- **A JetKVM alone cannot press the power button. The ATX extension board supplies that, and it also reads the power LEDs so the UI shows on or off state.** — The ATX board connects to the motherboard's power-button pins and reads the power LEDs. This is the only part that lets the workstation be turned on remotely. ([2:25](https://youtu.be/jNFv1Lr2Db4?t=145))
- **Wire the ATX board in parallel with the case's original power button so the physical button still works.** — The ATX board's two-row header takes the ribbon cable on one row, and the case's original power-button wires go on the other row through DuPont jumpers. Both the JetKVM and the case button can then trigger power. ([3:37](https://youtu.be/jNFv1Lr2Db4?t=217))
- **Power the JetKVM from a wall charger through the ATX board's USB-C port, not from the host computer.** — Host USB ports have no power while the machine is off, so the JetKVM must have its own external supply or it cannot turn the machine on. ([6:00](https://youtu.be/jNFv1Lr2Db4?t=360))
- **Board layouts differ, so check the motherboard manual's front-panel diagram pin by pin before connecting anything.** — The speaker's Gigabyte Z890 board did not match the JetKVM's standard front-panel layout, so he matched each wire against the board manual. ([3:37](https://youtu.be/jNFv1Lr2Db4?t=217))
- **Remote access works from the free JetKVM cloud app as well as the local IP address, which gives a phone-controlled power button.** — After enabling cloud access and signing in at app.jetkvm.com, the same interface can be used from a phone or laptop to press the power button and control the machine. ([7:28](https://youtu.be/jNFv1Lr2Db4?t=448))
- **A VPN browser extension that blocks WebRTC can keep the JetKVM video stuck on connecting.** — JetKVM streams video over WebRTC. Disabling the VPN extension let the stream connect within seconds. ([8:38](https://youtu.be/jNFv1Lr2Db4?t=518))

## Techniques
- **Parallel power-button wiring with an ATX extension board** — Disconnect the case's power and reset leads from the motherboard F-Panel header. Connect the ATX board's ribbon cable to the F-Panel. Use DuPont jumpers to put the case's original power-button wires on the second row of the ATX board's header so both the physical button and the remote button work. Connect the ATX board's extension cable to the JetKVM's extension port, and power the JetKVM from a wall charger through the ATX board's USB-C port. *When:* Remote power-on of a desktop from a KVM device, while keeping the local power button working. Always shut down, switch off the PSU and unplug before opening the case.
- **Four-cable JetKVM hookup** — Ethernet to the router, HDMI from the GPU output, USB-C from the JetKVM to a host USB port (acts as keyboard and mouse), and the ATX extension cable from the ATX board. Then power the JetKVM from its own USB-C supply. *When:* Setting up any JetKVM with a host that must be powered on or off remotely.
- **Pick a KVM connection for remote access** — Open the JetKVM's local IP address (shown on its small screen) in a browser for LAN access. For remote access, enable cloud access in the JetKVM settings, sign in at app.jetkvm.com, and connect to the device. *When:* Accessing the machine from outside the home network, or from a phone.
- **Browser troubleshooting for JetKVM video** — If the video is stuck on connecting, disable browser extensions, especially VPN extensions that block WebRTC. *When:* The JetKVM web UI shows connecting indefinitely.

## Numbers
- JetKVM captures HDMI at up to 1080p and 60 fps, using a Rockchip SoC with a hardware video encoder (vendor-stated). ([0:03](https://youtu.be/jNFv1Lr2Db4?t=3))
- Vendor-claimed glass-to-glass latency of 30 to 60 ms (vendor claim, not measured by the speaker). ([1:13](https://youtu.be/jNFv1Lr2Db4?t=73))
- Workstation spec: 64 GB DDR5 RAM and an RTX 5090 GPU (the opening says RTX 1590, which is probably a caption error for the RTX 5090 mentioned later). ([0:03](https://youtu.be/jNFv1Lr2Db4?t=3))

## Hot takes
- Not sponsored, per the speaker. The main value is a hands-on tutorial for remote power-on, not a benchmark.
- The speaker stresses that the JetKVM needs its own external power to turn the machine on remotely, because host USB is unpowered while the machine is off.
- Thin on methodology: no latency measurement, only the vendor's 30 to 60 ms claim. Quality is a practitioner walkthrough.

## Tools mentioned
JetKVM (open-source KVM-over-IP device, ATX extension board, cloud service at app.jetkvm.com), Chrome, Windows 11, Ubuntu, Gigabyte Z890 motherboard, Nvidia RTX 5090 (GPU, HDMI source), Nvidia RTX 1590 (mentioned as the workstation GPU in the opening), WebRTC

## Relevance to our work
- **prosharness** (1/3): ProsHarness runs long Claude Code runs and uses phone-driven approvals. A remotely powered workstation with cloud phone access is loosely adjacent to that setup, but the video does not touch agent or harness design. → *Optional: if ProsHarness ever runs on a home workstation, a KVM-over-IP box is a remote-recovery option for when the machine has powered off.*
