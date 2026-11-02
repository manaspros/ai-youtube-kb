# jQuery 4 FINALLY released... (What!?)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `HNp8naNxS0w` · [watch](https://youtu.be/HNp8naNxS0w) · **date:** 2026-02-02 · **length:** 4:31 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, jQuery, WordPress
- **topics:** dev-tools · **tags:** jquery, javascript, browser-compatibility, legacy-code, release-notes, es-modules, web-frontend

> Better Stack walkthrough of jQuery 4, the first major release since 2016: dropped browsers, ES module source, removed utilities, focus-order fix, and a 19.5 KB slim build.

## Summary
Better Stack covers the release of jQuery 4, billed as the first major version since 2016 after roughly two years in beta. The speaker says jQuery is still widely used (he cites about 88% of websites, mostly via WordPress, with no source given) and that this release is where the project collects the breaking changes it had deferred. Browser support is cut to modern versions: IE10 and below, Edge Legacy, older iOS, Firefox and Android browsers are dropped, while IE11 support continues until jQuery 5. The source moves from AMD to ES modules so it works with modern bundlers without workarounds. Many utilities that JavaScript now provides natively are removed, including isArray, parseJSON, trim, now, isNumeric and isFunction. The focus and blur event ordering override is removed because supported browsers now agree, except IE. A slim build strips the extra modules down to about 19.5 KB. The speaker closes by saying he would not pick jQuery over React today, but that legacy apps depend on it.

## Key ideas
- **jQuery 4 is the first major version since 2016, after about two years in beta, and collects breaking changes the project had deferred.** — Speaker frames it as a cleanup release: trimmed legacy code, removed deprecated and undocumented APIs, and a batch of bug fixes. ([0:00](https://youtu.be/HNp8naNxS0w?t=0))
- **Browser support is cut to modern engines.** — Dropped: IE10 and below, Edge Legacy, iOS versions older than the last three, Firefox versions older than the last two, and the Android browser. IE11 support stays until jQuery 5. ([0:00](https://youtu.be/HNp8naNxS0w?t=0))
- **The source is migrated from AMD to ES modules.** — Speaker says it should now work with bundlers such as Webpack and the build tool he calls V (likely Vite, given auto-caption errors) without special configuration. ([1:17](https://youtu.be/HNp8naNxS0w?t=77))
- **Utilities that JavaScript now provides natively are removed.** — Removed names he lists include isArray, parseJSON, trim, now, isNumeric and isFunction, plus many more. ([1:17](https://youtu.be/HNp8naNxS0w?t=77))
- **The focus and blur event-order override is removed.** — jQuery used to impose its own order because browsers disagreed. With old browsers dropped, all supported browsers except IE share the same order, so jQuery no longer overrides native behavior. ([1:17](https://youtu.be/HNp8naNxS0w?t=77))
- **A slim build removes optional modules for a much smaller bundle.** — Speaker says the slim build is about 19.5 KB. The full build keeps the extra functions for users who still need them. ([2:21](https://youtu.be/HNp8naNxS0w?t=141))
- **Some remaining jQuery patterns have modern replacements.** — Deferreds and callbacks can move to promises (except where IE11 must work), and some jQuery animations are easy to express in CSS now. ([2:21](https://youtu.be/HNp8naNxS0w?t=141))
- **Long-standing bugs are being fixed, some from years ago.** — The oldest fix he found is from 2014 (JSON-P auto-promotion). Another from 2015 is the CSS setter that appended px to unitless numbers. ([2:21](https://youtu.be/HNp8naNxS0w?t=141))

## Techniques
- **Gate an upgrade on your browser matrix** — Before moving to jQuery 4, check that your real traffic is inside the supported set: no IE10 or older, no Edge Legacy, only the last three iOS and last two Firefox versions. IE11 still works until jQuery 5, so a jQuery 4 upgrade does not yet cut IE11 users. *When:* Upgrading a legacy app that still ships to older browsers, or planning for the jQuery 5 IE11 cutoff.
- **Consume jQuery as an ES module in the bundler** — Because the source is now ES modules, import jQuery through the bundler's normal module path and drop any AMD shim or config workaround that existed for jQuery 3. *When:* Bundling jQuery in a Webpack or Vite project. Speaker says no tricks are needed; the exact import syntax is not shown.
- **Prefer the slim build when you do not need the removed extras** — Use the slim build variant, which the speaker says drops the optional modules and is about 19.5 KB. Keep the full build if your code still calls functions that live in the extra modules. *When:* New or cleaned-up pages that only need DOM and event basics, where payload size matters.
- **Replace utility calls with platform code** — Audit calls to the removed helpers (isArray, parseJSON, trim, now, isNumeric, isFunction and others). The speaker says all of these are now possible in plain JavaScript; he does not show the replacements. *When:* Before the upgrade, so the build fails or warns on removed APIs and you can swap them one by one.
- **Move deferred chains to promises and simple animations to CSS** — Convert $.Deferred chains and callback-style async code to native promises, and turn simple jQuery animate effects into CSS transitions or keyframes. Keep deferreds where IE11 support is still required. *When:* Modernizing jQuery-heavy code without a full rewrite, or after the IE11 constraint is gone.

## Numbers
- About 88% of all websites still use jQuery, per the speaker, mostly via WordPress. No source is given. ([0:00](https://youtu.be/HNp8naNxS0w?t=0))
- Slim build is about 19.5 KB. ([2:21](https://youtu.be/HNp8naNxS0w?t=141))
- jQuery was first introduced about 20 years before this release. ([0:00](https://youtu.be/HNp8naNxS0w?t=0))
- This is the first major version since 2016, after about two years in beta. ([0:00](https://youtu.be/HNp8naNxS0w?t=0))
- Oldest bug fix mentioned dates from 2014 (JSON-P auto-promotion); another from 2015 (CSS px append). ([2:21](https://youtu.be/HNp8naNxS0w?t=141))

## Hot takes
- Speaker says the 88% usage figure but gives no source, so treat it as anecdotal.
- Title's 'FINALLY released... (What!?)' framing is overstated: this is a changelog recap of a long-expected major version, not a surprise drop.
- Speaker says he would not choose jQuery over React today, yet recommends the slim build for cleanup; he treats jQuery as legacy maintenance, not a new-project default.
- Most of the video restates release-note headlines. Little data or migration detail beyond the list of dropped APIs and browsers.

## Tools mentioned
jQuery 4, jQuery 5 (announced future release, no details given), jQuery slim build, Webpack, V (auto-caption error, likely Vite), React, WordPress, Internet Explorer 10 and 11, Edge Legacy, Firefox, Android browser
