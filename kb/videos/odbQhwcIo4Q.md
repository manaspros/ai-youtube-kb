# TanStack Did It Again... They Fixed Charts

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `odbQhwcIo4Q` · [watch](https://youtu.be/odbQhwcIo4Q) · **date:** 2026-09-02 · **length:** 8:14 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** TanStack, Better Stack, Recharts, Chart.js
- **topics:** dev-tools, mcp-and-tools · **tags:** charts, data-visualization, grammar-of-graphics, tanstack, react, bundle-size, svg, canvas, agent-friendly-api, theming

> Better Stack walks through TanStack Charts, a week-old framework-agnostic charting library built on a grammar-of-graphics model, and claims a much smaller bundle than Recharts and Chart.js.

## Summary
The host introduces TanStack Charts, a new charting library with a framework-agnostic core, SVG and canvas output, and type-safe keys. Charts are described as compositions of marks, scales and mappings in the style of ggplot2, so a bar chart is just a barY mark with scales rather than a built-in type. The walkthrough shows a React bar chart built from about 20 lines, adding an average line via a ruleY mark, and a line chart with dots and an area. It then covers built-in interactions (brush, zoom, keyboard selection, crosshair, tooltip strategies and pinning), animations (value changes, staggered entry, add/remove, streaming), and SVG/PNG export. Styling is split into three levels: six categorical CSS variables, a theme block for chart furniture, and per-mark properties that can be data-driven. The speaker cites a bundle-size benchmark of 36-43 KB for the full feature suite versus 45-58 KB for Chart.js and 153-168 KB for Recharts, and says the library was designed so an AI agent can write charts without reading the docs. The video is a short hands-on tour with no sponsor, and the benchmark's origin and methodology are not explained.

## Key ideas
- **Charts are compositions, not types** — TanStack Charts uses a grammar-of-graphics model (compared to ggplot2): you declare marks, scales and data mappings, and the chart type emerges. A bar chart is just a barY mark with x/y keys and scales, and unusual charts (such as a contour map) can be built from the same primitives. ([1:14](https://youtu.be/odbQhwcIo4Q?t=74))
- **Marks are the drawn primitives** — Marks are the things actually drawn (bars, lines, dots, rules, text, areas, cells, arrows, and others). The speaker says the demo site uses roughly 55 of them, covering pie, tree map, Sankey, geo shape and similar charts. ([1:14](https://youtu.be/odbQhwcIo4Q?t=74))
- **Framework-agnostic definition, thin React wrapper** — The chart definition is framework-agnostic. In React the speaker only imports the chart component and passes it the definition plus a height and a label. ([3:25](https://youtu.be/odbQhwcIo4Q?t=205))
- **Composition by appending marks** — An average line is added by appending a ruleY mark to the marks array. A line chart with dots and an area underneath is likewise just several marks combined. ([3:25](https://youtu.be/odbQhwcIo4Q?t=205))
- **Interactions and tooltips are built in** — Brush, zoom, keyed and keyboard selection, crosshair, and tooltips are included. Tooltip strategies such as nearest-X or group-X are configurable, tooltips can be pinned on click, and custom tooltip UIs can be rendered in React. ([4:42](https://youtu.be/odbQhwcIo4Q?t=282))
- **Animation and export are included** — Value changes interpolate, entrances can be staggered, added and removed items animate, and streaming data shifts existing elements instead of redrawing. Charts export to SVG and PNG. ([5:47](https://youtu.be/odbQhwcIo4Q?t=347))
- **Three styling levels** — Level one is six categorical CSS custom properties that can be overridden on any container. Level two is a theme block in the chart definition for furniture such as text, grid lines and background. Level three is per-mark properties (fill, stroke, opacity, dashes, corner radius, fonts), which can be fixed or data-driven, for example coloring bars by a target threshold. ([5:47](https://youtu.be/odbQhwcIo4Q?t=347))
- **API designed so an agent can write charts** — The stated design goals are polished charts from short declarations, and AI being able to compose, inspect and modify charts without learning an app-specific series model. The speaker says an agent wrote most of the demos with few corrections. ([6:55](https://youtu.be/odbQhwcIo4Q?t=415))

## Techniques
- **Declare a chart as marks plus scales** — Call the define-chart function (named 'define chart' in the captions; exact identifier not shown). Inside it, list marks; for a bar chart use one barY mark with the data array and x and y keys. Set the x scale to band (for categories, with padding) and the y scale to linear with nice set to true so the axis rounds to a sensible value. Add an axis label and a number format such as percentage. Render in React by passing the definition, a height and a label to the chart component. *When:* Any categorical or numeric chart where you want the data shape to stay unchanged and key typos to be caught by types.
- **Add reference lines and overlays as marks** — Append a ruleY mark to the marks array with the average value to draw a horizontal average line. Combine a line mark, a dot mark and an area mark for a composite chart. *When:* Adding averages, thresholds or secondary series without writing custom SVG.
- **Data-driven mark styling** — Pass a function or data-derived value to a mark's fill, stroke or opacity instead of a constant (the speaker colors bars by whether they exceed a target and builds gradients from data). *When:* Highlighting outliers or threshold breaches, or encoding a value in color.
- **Three-level theming** — Override the six categorical CSS custom properties on a container to recolor series. Set text, grid, background and similar furniture in the chart definition's theme block. Set per-mark fill, stroke, dash, corner radius and font where needed. *When:* Matching a brand or supporting dark mode without touching each mark.

## Numbers
- Bundle size of TanStack Charts full-feature suite (crosshair, brush, zoom, selection, etc.): 36-43 KB, per the speaker's benchmark ([6:55](https://youtu.be/odbQhwcIo4Q?t=415))
- Chart.js bundle size in the same benchmark: 45-58 KB ([6:55](https://youtu.be/odbQhwcIo4Q?t=415))
- Recharts bundle size in the same benchmark: 153-168 KB ([6:55](https://youtu.be/odbQhwcIo4Q?t=415))
- Roughly 55 mark types in the speaker's demo site ([1:14](https://youtu.be/odbQhwcIo4Q?t=74))
- The bar-chart demo's chart definition is about 20 lines of code ([1:14](https://youtu.be/odbQhwcIo4Q?t=74))
- Library was about one week old at the time of recording ([1:14](https://youtu.be/odbQhwcIo4Q?t=74))
- Six categorical colour CSS custom properties ([5:47](https://youtu.be/odbQhwcIo4Q?t=347))

## Hot takes
- The title ('They Fixed Charts') and the 'my new favorite charting library' verdict are hype for a library about a week old; the speaker admits he has not explored most features.
- The bundle-size comparison is the speaker's cited benchmark for the full feature suite, but the video does not say who ran it or with what methodology.
- The claim that an AI agent can write charts without reading the docs is an interesting design principle, but it is supported only by the speaker's own experience with a few demos.
- A grammar-of-graphics approach is powerful for composition, but the speaker shows no performance or large-dataset numbers.

## Tools mentioned
TanStack Charts, React, ggplot2 (referenced as the inspiration for the grammar of graphics), Recharts (comparison), Chart.js (comparison), TanStack (library family)
