# Hotwire Spark for Ruby on Rails — Hot Reloading… FINALLY!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `b7SWkjgcuMU` · [watch](https://youtu.be/b7SWkjgcuMU) · **date:** 2025-11-02 · **length:** 4:05 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** ?
- **topics:** dev-tools · **tags:** rails, hotwire, hot-reload, turbo, stimulus, import-maps, developer-experience

> One development-only gem, Hotwire Spark, gives Rails hot reloading for HTML, CSS and Stimulus edits. Under JS bundling, HTML and Stimulus changes fall back to a full page visit.

## Summary
The presenter walks through Hotwire Spark, a Rails gem that adds hot reloading to the browser during development. Before installing it, edits to HTML, CSS and Stimulus controllers only show up after a manual refresh. Installation is a single gem line in the development group, followed by bundle install and a server restart. The demo shows HTML, CSS and Stimulus changes applying without a refresh, with scroll position and page state kept. The explanation then splits behavior by asset pipeline: with import maps, HTML morphs the body and Stimulus controllers are swapped and reconnected, while with JavaScript bundling HTML and Stimulus changes trigger a Turbo visit. The video is a short, accurate tutorial with no sponsorship, and it mentions Hotwire Live Reload and Vite Ruby's full reload as alternatives.

## Key ideas
- **Rails has had no official hot reloading; Hotwire Spark fills that gap.** — Without it, HTML, CSS and Stimulus edits all require a manual browser refresh, which the presenter calls friction. Spark is positioned as a near-free win for development. ([0:00](https://youtu.be/b7SWkjgcuMU?t=0))
- **Installing Spark is one gem in the development group.** — Add the gem to the Gemfile's development group, run bundle, and restart the server. The terminal then prints a Hotwire Spark subscription confirmation line. ([0:56](https://youtu.be/b7SWkjgcuMU?t=56))
- **Edits apply without losing page state.** — On the demo page, HTML, CSS and Stimulus changes updated in place. Scroll position and other page state were kept, which the presenter cites as the main friction reduction. ([1:59](https://youtu.be/b7SWkjgcuMU?t=119))
- **Spark supports HTML, CSS and Stimulus changes.** — The demo covers a title change, a CSS color change to a delete button, and a Stimulus controller string change that appeared on the button without a refresh. ([1:59](https://youtu.be/b7SWkjgcuMU?t=119))
- **Import maps give surgical updates; the mechanism differs per change type.** — With import maps, an HTML change morphs the page body and disconnects and reconnects Stimulus controllers. A CSS change reloads only the changed stylesheet. A Stimulus change re-fetches the controller, replaces it in the Stimulus module, and reconnects the controllers. ([3:03](https://youtu.be/b7SWkjgcuMU?t=183))
- **JavaScript bundling falls back to full visits for HTML and Stimulus.** — Under JS bundling, an HTML change or a Stimulus change reloads the page with a Turbo visit. Only CSS changes use the stylesheet reload path, so the behavior is less seamless there. ([3:03](https://youtu.be/b7SWkjgcuMU?t=183))
- **Small reload savings add up over a session, per the presenter.** — The presenter argues that repeated fine-tuning of CSS and markup is where refresh friction accumulates. Alternatives named in passing are Hotwire Live Reload and Vite Ruby's full reload. ([3:03](https://youtu.be/b7SWkjgcuMU?t=183))

## Techniques
- **Install Hotwire Spark in a Rails app** — Add the Hotwire Spark gem to the development group in the Gemfile, run bundle install, restart the dev server, and confirm the terminal prints the Spark channel subscription confirmation line. The video does not show the exact gem line or version. *When:* Any Rails app where you are fine-tuning HTML, CSS or Stimulus during development and want to avoid manual refreshes.
- **Expect import-maps update semantics** — HTML edits morph the page body and reconnect Stimulus controllers. CSS edits reload only the changed stylesheet. Stimulus edits re-fetch the changed controller, swap it into the Stimulus module, and reconnect controllers, so the page keeps its state. *When:* Projects using Rails import maps, where you want to keep scroll and page state while adjusting markup, styles or controller behavior.
- **Plan around full visits under JS bundling** — Under JavaScript bundling, HTML and Stimulus changes trigger a Turbo visit, which is a full page reload. CSS changes still reload only the stylesheet. Expect the stylesheet path to be the only seamless one. *When:* Projects using JavaScript bundling, where the seamless behavior is partial and a full reload on markup or controller edits is acceptable.

## Numbers
- Install takes about five seconds, per the presenter's estimate. ([0:56](https://youtu.be/b7SWkjgcuMU?t=56))
- Video length is 4:05, with a single demo app and no benchmarks or timing measurements. ([0:00](https://youtu.be/b7SWkjgcuMU?t=0))

## Hot takes
- Presenter calls hot reloading 'a must have' and 'a free win', framing it as a clear developer-experience gain.
- Title says 'FINALLY!', but the content is a short, low-hype feature demo; the 'free win' framing is not backed by measurements.
- The demo is one toy app with three edits, so the claims about reduced friction are anecdotal.
- Under JS bundling the seamless behavior covers CSS only, which the presenter notes but does not weigh heavily.

## Tools mentioned
Hotwire Spark, Ruby on Rails, Bundler (bundle command), Gemfile, Turbo (Turbo visit), Stimulus, Import Maps, Hotwire Live Reload (mentioned as an alternative), Vite Ruby (full reload, mentioned as an alternative), Vim (aside about keybinds)
