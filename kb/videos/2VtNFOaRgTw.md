# Leap Year Bugs: From Satellites to Spreadsheets

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `2VtNFOaRgTw` · [watch](https://youtu.be/2VtNFOaRgTw) · **date:** 2025-11-02 · **length:** 4:47 · **format:** other · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, OneWeb, Starlink, Microsoft, Lotus, IBM, The Register
- **topics:** dev-tools, testing-verification · **tags:** leap-year, date-handling, edge-cases, time-zones, legacy-compatibility, excel, python, javascript, gps-utc, zune

> Better Stack walkthrough of leap-year bugs in satellites, Excel, Python, JavaScript and Zune, with the Gregorian leap-year rule and the Lotus 1-2-3 1900 bug that Excel kept for compatibility.

## Summary
The video is a short explainer on leap-year bugs. It opens with the OneWeb outage that began just after midnight on December 31, 2024 and lasted 48 hours; a spokesperson attributed it to day 366 handling in a manual GPS-to-UTC offset calculation, though the speaker does not know the exact calculation. The speaker splits leap-year bugs into two categories: ones that throw errors (Python's date arithmetic raising on February 29) and silent ones that produce wrong data (JavaScript's Date rolling over to March 1). It then states the full Gregorian leap-year rule (divisible by 4, except centuries, unless divisible by 400) and notes that 1900 is not a leap year while 2000 is. The main historical story is Lotus 1-2-3 treating 1900 as a leap year, which Excel copied for compatibility and which Microsoft documents and keeps. The video ends with the Zune freeze on December 31, 2008, which fixed itself after 24 hours, and a reminder that the next leap year is 2028. Substance is light: mostly anecdotes and one rule, with no production data or deep technical analysis.

## Key ideas
- **OneWeb's outage (48 hours from just after midnight on Dec 31, 2024) was attributed by a spokesperson to a leap-year problem with day 366 in the manual GPS-to-UTC offset calculation.** — The speaker says he does not know the exact calculation. He notes a leap-year bug can surface months after the leap day, not only on it. ([0:00](https://youtu.be/2VtNFOaRgTw?t=0))
- **Leap-year bugs fall into two categories: errors (the program throws) and silent wrong data (off-by-one, date rollover).** — The speaker treats the silent category as more dangerous because nothing signals the failure. ([0:56](https://youtu.be/2VtNFOaRgTw?t=56))
- **Python raises when asked for February 29 in a non-leap year; JavaScript's Date silently rolls over to March 1.** — Both examples compute a date one year ahead, which fails only once the source date is Feb 29. Python is the error case; JavaScript is the silent case. ([0:56](https://youtu.be/2VtNFOaRgTw?t=56))
- **The leap-year rule is not every four years: years divisible by 4 are leap years, except centuries, which must be divisible by 400.** — The speaker uses 1900 (not a leap year) and 2000 (a leap year) as the examples that break naive logic. ([2:04](https://youtu.be/2VtNFOaRgTw?t=124))
- **Lotus 1-2-3 wrongly treated 1900 as a leap year, and Excel copied the bug for compatibility.** — Microsoft documents the bug on its own page and keeps it. The speaker argues that backward compatibility means it cannot be fixed, so it is effectively standardised. ([2:04](https://youtu.be/2VtNFOaRgTw?t=124))
- **The Zune froze on December 31, 2008 because the internal clock driver could not handle the leap year.** — Microsoft said it fixed itself after about 24 hours. The speaker reports a user workaround: drain the battery and recharge it after the UTC rollover on January 1, 2009, which saved about 12 hours. ([3:21](https://youtu.be/2VtNFOaRgTw?t=201))

## Techniques
- **Gregorian leap-year check** — Leap year if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0. Do not use year % 4 alone. The speaker presents this as the correct rule, with 1900 as non-leap and 2000 as leap. *When:* Any code that computes leap years itself, for example date math, scheduling, or offset calculations. Prefer the standard library where it exists.
- **Edge-case test years for date logic** — The speaker's examples imply testing with 1900 (century non-leap), 2000 (century leap), and 2024-02-29 (a real leap day) as inputs. He also suggests testing 'add one year' on Feb 29, which exposes the Python error and JavaScript rollover. *When:* Before shipping any date arithmetic, especially year offsets, retention windows, or schedules that can land on Feb 29.
- **Check for silent date rollover** — The speaker's JavaScript example shows a date that rolls forward to 1 March instead of failing. The implied check is to compare the result's month and day against the intended values after date arithmetic, rather than trusting that no exception means correct output. *When:* When date arithmetic can produce an invalid calendar date and the library normalises it silently.

## Numbers
- OneWeb outage lasted 48 hours, starting just after midnight on Dec 31, 2024. ([0:00](https://youtu.be/2VtNFOaRgTw?t=0))
- Lotus 1-2-3 bug is about 41 years old. ([2:04](https://youtu.be/2VtNFOaRgTw?t=124))
- Zune freeze on Dec 31, 2008; auto-fixed after about 24 hours; the battery workaround saved about 12 hours. ([3:21](https://youtu.be/2VtNFOaRgTw?t=201))
- Next leap year is 2028 (speaker suggests setting a reminder for Feb 28, 2028). ([3:21](https://youtu.be/2VtNFOaRgTw?t=201))

## Hot takes
- Excel's 1900 leap-year bug is effectively a standard because backward compatibility stops it being fixed.
- Naive leap-year logic (every four years) is the common mistake, and the century rule is less intuitive than people expect.
- The speaker finds the OneWeb admission surprisingly candid.

## Tools mentioned
Python, JavaScript (Date object), Excel, Lotus 1-2-3, Zune, Claude (used to generate the buggy GPS-to-UTC example code), The Register (cited source)

## Relevance to our work
- **agentos** (1/3): Budget windows and time buckets in the planned TimescaleDB and budget layers rely on calendar date arithmetic, which can break on Feb 29 or century years. → *Add tests for budget reset and time-bucket boundaries on 2028-02-29 and 2100-02-28/03-01 (2100 is not a leap year).*
- **prosharness** (1/3): Loops and schedules that run on calendar dates can silently shift on Feb 29 or century boundaries. → *Add a schedule test that rolls a yearly or annual trigger from Feb 29, checking it does not silently land on 1 March.*
