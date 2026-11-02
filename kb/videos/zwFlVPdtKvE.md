# JavaScript Dates SUCK — Here's What's Replacing Them

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `zwFlVPdtKvE` · [watch](https://youtu.be/zwFlVPdtKvE) · **date:** 2025-11-02 · **length:** 13:10 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** ?
- **topics:** dev-tools · **tags:** javascript, temporal-api, dates, time-zones, daylight-saving-time, ecmascript-proposal, polyfill

> A walkthrough of the Temporal date/time API (polyfilled today) covering the seven types, strict parsing, overflow and DST disambiguation, immutable durations, rounding and comparison, as a replacement for JavaScript Date.

## Summary
The presenter walks through the Temporal proposal for JavaScript dates, which he says is starting to appear in experimental browser releases and is currently used through a polyfill package. He covers Temporal.Now and the seven types: Instant (UTC epoch time with nanosecond precision), ZonedDateTime (time zone and calendar aware), and the Plain types (PlainDateTime, PlainDate, PlainTime, PlainYearMonth, PlainMonthDay), which carry no zone. Construction goes through from(), which accepts a string or an object and requires enough information, such as a zone or offset, with a missing hour defaulting to midnight. Strictness is controlled explicitly: overflow defaults to constrain but can be set to reject, and DST ambiguity is resolved with compatible, earlier, later or reject, where compatible matches the legacy Date behaviour. Durations are created from ISO strings or objects, support add/subtract on immutable values, until/since, total in a chosen unit, negated and absolute, and rounding with smallest unit, increment and rounding mode. The talk closes by suggesting that Temporal could remove the need for Moment, Luxon or hand-written date helpers.

## Key ideas
- **Temporal is the proposed replacement for the JavaScript Date object, fixing mutability, month-zero indexing, time zone handling and parsing.** — The presenter says it is starting to ship in experimental browser releases, and until then he uses a polyfill package (name not shown). Availability is his expectation, not a confirmed timeline. ([0:00](https://youtu.be/zwFlVPdtKvE?t=0))
- **Temporal.Now exposes seven types, and Instant is the UTC/epoch type with nanosecond precision and an ISO string output.** — Temporal.Now.instant() gives epoch nanoseconds and milliseconds; logging it gives an ISO UTC string, which he says suits front-end/back-end exchange without time zone handling. ([0:00](https://youtu.be/zwFlVPdtKvE?t=0))
- **Construction is strict: types need enough information to say which moment is meant.** — Instant.from needs a Z or an explicit offset; ZonedDateTime needs a time zone. Missing components like hour default (to midnight) in some types, but a missing zone throws. ([1:18](https://youtu.be/zwFlVPdtKvE?t=78))
- **ZonedDateTime is the most complete type, and the other types expose derived calendar fields.** — It combines instant, time zone and calendar (he names Gregorian, Islamic, Hebrew and Chinese). Built-in getters cover month code, day of week, week of year, days in month/year and leap-year checks, which previously needed Moment or Luxon. ([2:41](https://youtu.be/zwFlVPdtKvE?t=161))
- **Overflow handling is explicit: the default constrains out-of-range fields, and reject throws.** — A month of 13 is constrained to 12 by default. Passing an options object with overflow set to reject raises a range error instead. ([3:52](https://youtu.be/zwFlVPdtKvE?t=232))
- **DST ambiguity has four explicit options, and compatible reproduces legacy Date behaviour.** — Using 1:30 a.m. on 5 Nov 2023 in America/New_York, which occurs twice, earlier gives the -04:00 instance, later gives -05:00, and compatible follows Date (earlier on fall-back, next valid time on spring-forward). reject throws for ambiguous or non-existent times. ([5:09](https://youtu.be/zwFlVPdtKvE?t=309))
- **Plain types drop the time zone and are the right choice for wall-clock values like birthdays or business dates.** — PlainDateTime, PlainDate, PlainTime, PlainYearMonth and PlainMonthDay all share the from() pattern and serialize without an offset. ([6:28](https://youtu.be/zwFlVPdtKvE?t=388))
- **Durations are ISO-8601 based, and date math returns new values instead of mutating.** — Duration.from accepts an object or a string like PT1H30M and toString returns the ISO form. Add and subtract on a PlainDate return new values, while the original is unchanged, unlike Date.setMonth, which mutates in place. ([8:38](https://youtu.be/zwFlVPdtKvE?t=518))
- **until/since build durations between values, and total, negated and absolute handle units and sign.** — Jan 1 until Jan 31 gives a 30-day duration; total with a unit such as second returns the count in that unit; negated flips the sign and absolute strips it. ([9:54](https://youtu.be/zwFlVPdtKvE?t=594))
- **Rounding and comparison are built in.** — round takes smallestUnit, roundingMode (ceil, floor, expand, truncate, half-ceil, half-floor and more) and roundingIncrement. compare returns -1, 0 or 1, and equals is available on instances. ([11:10](https://youtu.be/zwFlVPdtKvE?t=670))

## Techniques
- **Get current time in a chosen type** — Call Temporal.Now.<type>() instead of new Date(): Temporal.Now.instant() for UTC epoch with nanoseconds, or Temporal.Now.zonedDateTime... for zone-aware values. Log the value to get the ISO string. *When:* Replacing new Date() for timestamps that cross the front-end/back-end boundary, where nanosecond precision or explicit UTC is needed.
- **Build values with from() and explicit zone/offset** — Temporal.Instant.from('...Z') or with an explicit offset such as -01:00; Temporal.ZonedDateTime.from with an object including timeZone. Both string and object forms work. Omitting the zone or offset throws. Epoch construction is done from epoch with nanoseconds or milliseconds. *When:* Parsing external timestamps where a missing zone would silently produce wrong values.
- **Pick the right Plain type for the data** — Use PlainDate for dates without times, PlainTime for times without dates, PlainYearMonth and PlainMonthDay for partial dates, PlainDateTime for wall-clock date+time, and ZonedDateTime only when a real instant in a zone matters. *When:* Modelling business dates, schedules or user-facing wall-clock values that must not shift with time zones.
- **Reject out-of-range fields** — Pass a second options argument: { overflow: 'reject' } on from(). Default is 'constrain', which clamps (month 13 becomes 12). *When:* Validating user or API input where clamping would hide bad data.
- **Resolve DST ambiguity explicitly** — Pass { disambiguation: 'compatible' | 'earlier' | 'later' | 'reject' } when building a ZonedDateTime. Use 'reject' to surface ambiguous or non-existent local times as errors. *When:* Scheduling recurring events or cron-like jobs in a time zone that has DST transitions.
- **Date arithmetic with durations** — Build durations with Temporal.Duration.from({ days: 1, months: 1 }) or from('P1M1D'). Use x.add(duration) and x.subtract(duration), and assign the returned value because the original is immutable. Use a.until(b) or b.since(a) for differences, and dur.total({ unit: 'second' }) for totals. *When:* Replacing manual date math, Date.setMonth-style mutation, or Moment/Luxon add/diff calls.
- **Round and compare temporal values** — value.round({ smallestUnit: 'minute', roundingMode: 'ceil' }); add roundingIncrement: 5 with roundingMode: 'floor' for 5-minute buckets. Use Temporal.PlainTime.compare(a, b) returning -1/0/1, or a.equals(b). *When:* Bucketing timestamps into fixed intervals (for example for metrics or logs) and sorting or de-duplicating values.

## Numbers
- Temporal.Now has seven types, and Instant gives nanosecond precision. ([0:00](https://youtu.be/zwFlVPdtKvE?t=0))
- Calendar systems mentioned: Gregorian, Islamic, Hebrew, Chinese. ([2:41](https://youtu.be/zwFlVPdtKvE?t=161))
- Overflow example: month 13 is constrained to 12 by default. ([3:52](https://youtu.be/zwFlVPdtKvE?t=232))
- DST example: 1:30 a.m. on 5 Nov 2023 in America/New_York occurs twice; offsets shown are -04:00 (earlier) and -05:00 (later). ([5:09](https://youtu.be/zwFlVPdtKvE?t=309))
- Duration example: Jan 1 until Jan 31 is 30 days; total in seconds gives the seconds in 30 days (2,592,000, derived from 30 x 86,400). ([9:54](https://youtu.be/zwFlVPdtKvE?t=594))
- Rounding example: 3:30:45 plus milliseconds rounds up to 3:31 with ceil, and to 3:30 with a 5-minute floor. ([11:10](https://youtu.be/zwFlVPdtKvE?t=670))

## Hot takes
- The title frames JavaScript dates as broken and Temporal as a fix ready soon; the speaker's shipping timeline is his expectation, not a confirmed release date.
- He suggests Temporal could make Moment, Luxon and hand-written date helpers unnecessary, a strong claim that the talk does not test against real codebases.

## Tools mentioned
Temporal API (TC39 proposal), JavaScript Date object, Moment.js, Luxon, a Temporal polyfill package (name not shown)

## Relevance to our work
- **prosharness** (1/3): ProsHarness has loops and schedules; recurring runs across DST transitions need deterministic handling of repeated or missing local hours, which the disambiguation options cover. → *If ProsHarness schedules recurring runs in local time zones, decide how repeated and skipped DST hours behave and write a test for a fall-back and a spring-forward date.*
