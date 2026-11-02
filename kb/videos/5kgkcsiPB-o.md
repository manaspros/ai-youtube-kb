# Your VPN Is Probably FAKE! (85% Exposed in Investigation)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `5kgkcsiPB-o` · [watch](https://youtu.be/5kgkcsiPB-o) · **date:** 2026-01-02 · **length:** 4:43 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, IPinfo, NordVPN, Proton VPN, Netflix
- **topics:** security-guardrails, infra-cost-scaling · **tags:** vpn, ip-geolocation, virtual-locations, network-measurement, latency, privacy, transparency

> Better Stack summarizes an IPinfo investigation finding that most VPN providers list server countries that are virtual, with traffic exiting elsewhere; the speaker says the core problem is transparency, not encryption.

## Summary
The video summarizes an IPinfo report that tested the advertised country locations of 20 popular VPN providers. IPinfo ran latency measurements from its ProbeNet network of over 1,200 probes, pinging each VPN exit IP from several cities and comparing round-trip times. Of about 150,000 exit IPs across 137 countries, only three providers had exits exactly where they claimed. The main mechanism is virtual locations: a provider maps a block of IPs to a server in one country (for example France) while registries or geofeeds declare those IPs to be in another (for example Somalia), and IP databases copy the declaration without verifying it. Services that geofence by IP, such as Netflix, then serve content for the declared country. The speaker says 12% of virtual locations are more than 8,000 km from their stated position, which matters for privacy and latency. He argues that encryption and tunneling can still be sound when the exit is in another country, so the real problem is that providers do not disclose which servers are virtual or where traffic actually exits. This is a consumer explainer with no sponsor segment, and it rests on a single third-party report.

## Key ideas
- **Most VPN country lists are inaccurate: IPinfo found only 3 of 20 providers had exit IPs exactly where they claimed.** — The report covered about 150,000 exit IPs in 137 countries. The speaker frames this as 85% of providers misreporting, and cites 51% of Proton VPN's 110 listed countries as not matching their claimed location. ([0:00](https://youtu.be/5kgkcsiPB-o?t=0))
- **Virtual locations are the mechanism: the server sits in one country while the IP is registered to another.** — A provider maps a block of IPs to a server in France but the registry or geofeed declares them as Somalia. IP databases copy that data without checking it, so the app shows Somalia while traffic exits in France under French jurisdiction. ([2:39](https://youtu.be/5kgkcsiPB-o?t=159))
- **IPinfo measured location by latency triangulation from many probes rather than trusting the provider or the registry.** — ProbeNet has over 1,200 probes that ping the exit IP. A probe near the claimed country that sees sub-millisecond RTT, while distant probes see higher RTT, is strong evidence the exit is elsewhere. Several probes per location are used to reduce noise. ([1:18](https://youtu.be/5kgkcsiPB-o?t=78))
- **IP-based geofencing turns a location mismatch into a content and compliance mismatch.** — Services such as Netflix pick content by the IP's declared country, so a virtual Somalia exit gets Somali content even though the packets leave from France. ([3:39](https://youtu.be/5kgkcsiPB-o?t=219))
- **Virtual locations also carry latency and privacy costs, and 12% are more than 8,000 km from their stated place.** — The speaker says the distance gap affects latency, and that the legal jurisdiction of the real exit is what matters for privacy. ([3:39](https://youtu.be/5kgkcsiPB-o?t=219))
- **The speaker's conclusion is that encryption can still be sound, and the failure is one of transparency.** — A correctly implemented tunnel can be secure even if the exit is in another country. The fix he proposes is for providers to label virtual servers and disclose the true exit location. ([3:39](https://youtu.be/5kgkcsiPB-o?t=219))

## Techniques
- **Latency-based location verification** — Ping the target IP from probes placed in several known cities, then compare RTTs. A sub-millisecond RTT from a probe near the claimed country supports that location. A high RTT from distant probes is evidence it is elsewhere. Take several samples per location to cut noise. *When:* When you need to check where an IP really is instead of trusting a database, registry or geofeed entry.
- **Do not trust declared IP geolocation** — Treat registry, geofeed and IP-database country fields as claims. Verify them with measurements before using them for geofencing, compliance or routing decisions. *When:* When routing, access control or content decisions depend on an IP's country.

## Numbers
- 85% of VPN providers misreport locations (3 of 20 matched). ([0:00](https://youtu.be/5kgkcsiPB-o?t=0))
- 51% of Proton VPN's 110 countries are not where claimed. ([1:18](https://youtu.be/5kgkcsiPB-o?t=78))
- ProbeNet has over 1,200 probe servers worldwide. ([1:18](https://youtu.be/5kgkcsiPB-o?t=78))
- About 150,000 exit IPs tested across 137 countries from 20 providers. ([2:39](https://youtu.be/5kgkcsiPB-o?t=159))
- 12% of virtual locations are more than 8,000 km from their stated location. ([3:39](https://youtu.be/5kgkcsiPB-o?t=219))

## Hot takes
- Title says VPNs are FAKE and 85% exposed. The body says virtual locations are a transparency problem, and encryption and tunneling can still be sound, so the headline overstates it. Quality capped at 2 under the sales-pitch rule: thin for engineering use, and no sponsor segment.

## Tools mentioned
IPinfo ProbeNet, OpenVPN
