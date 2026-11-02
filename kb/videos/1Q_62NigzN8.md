# I Played DuckDB Doom And It's ACTUALLY Good

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `1Q_62NigzN8` · [watch](https://youtu.be/1Q_62NigzN8) · **date:** 2025-11-02 · **length:** 7:51 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools, data-engineering · **tags:** duckdb, duckdb-wasm, sql, recursive-cte, raycasting, embedded-database, browser, doom, demo

> Better Stack demo of a Doom-like raycasting game whose 3D rendering runs entirely as DuckDB SQL queries in the browser (WASM); a stunt that shows how far an embedded analytical DB can be pushed, not a practical recipe.

## Summary
The presenter walks through a browser game, built by Patrick Traynor, where DuckDB (WASM build) handles the game state and the 3D raycasting, not just data storage. The game's index.html (about 654 lines) imports DuckDB from a CDN and renders a text frame buffer built from SELECTs over five tables (map, player, enemies, bullets, settings) and two views (Render3DFrame, ColumnDistances). The map is a 16x16 grid table of x, y and tile value, with walls as '#'. The 3D view uses a recursive common table expression: a seed row, then a recursive step that advances each ray until it hits a wall or exceeds a max step count. A setInterval re-runs the main query every 150 ms. A pixel function picks the character: blank for sky, a dot for floor, and a wall glyph whose opacity falls off with distance. The presenter then plays it (WASD to move, space to shoot; '@' player, 'E' enemies, '*' bullets). He frames it as a stress test of DuckDB and says he would not play a full game this way. The transcript has no benchmarks, and the presenter says some function/alias terms interchangeably.

## Key ideas
- **DuckDB is an analytical database that runs embedded in the host process, so it can be used as a library with no separate server or container.** — Presenter contrasts it with ClickHouse and BigQuery as analytical engines, and says a Node.js app could install it as a library and it would feel like part of the same app. ([0:00](https://youtu.be/1Q_62NigzN8?t=0))
- **A full Doom-like game's rendering is done in SQL, not in JavaScript.** — The DuckDB WASM build runs in the browser; the index.html is about 654 lines and imports DuckDB from a CDN. The screen element renders a frame buffer made of rows that come from SELECTs. ([0:00](https://youtu.be/1Q_62NigzN8?t=0))
- **Game state lives in plain tables, and the frame is a view over them.** — Tables: map, player, enemies, bullets, settings. Views: Render3DFrame and ColumnDistances. Each render tick is a set of SELECTs over these, so movement and rendering are both queries. ([1:19](https://youtu.be/1Q_62NigzN8?t=79))
- **The minimap is a 16x16 grid table with x, y and tile columns.** — Wall tiles render as '#' and empty tiles as '.', with the minimap coloured via CSS. A separate minimap element renders it, distinct from the main screen element. ([2:44](https://youtu.be/1Q_62NigzN8?t=164))
- **3D raycasting is a recursive CTE: seed the ray, then step it until it hits a wall or the max step count is reached.** — The recursion is per ray and is not applied to the whole statement. The presenter describes the query as building the row set once and then recursively updating it from what changed. Player and settings values determine the candidate rows and columns, trimmed to the screen size from settings. ([4:05](https://youtu.be/1Q_62NigzN8?t=245))
- **The whole render query re-runs on a timer, about every 150 ms.** — A setInterval triggers the main SELECT each time, so every frame is a fresh full query over the state tables. The presenter notes that player movement is also computed via SQL, so these tables are queried heavily, which he says is what DuckDB is built for. ([5:28](https://youtu.be/1Q_62NigzN8?t=328))
- **The pixel function maps distance to glyph: sky is blank, floor is a dot, and walls are a rectangle whose opacity falls with distance.** — Wall distance comes from the ray result, and wall height comes from a separate function. The presenter says the frame output is rows of characters that the browser shows as text. ([5:28](https://youtu.be/1Q_62NigzN8?t=328))

## Techniques
- **Recursive CTE as a ray-march loop** — Write a seed row CTE for the first ray step, then a recursive CTE that advances each ray one step per iteration (position += direction) until a wall tile is hit or a max-steps bound is reached. Output the hit distance per ray. The video shows this with comments marking the seed and the recursive step. Use a step bound so recursion terminates. *When:* Iterative per-element computation (marching, path-stepping, simulation) that must run inside a SQL engine instead of application code.
- **Game state as tables, render as views** — Store map, player, enemies, bullets and settings as tables. Define view layers (Render3DFrame, ColumnDistances) over them. Each frame, SELECT the frame rows; the output is text rows that the browser renders into a screen element. The minimap is a separate SELECT over the map table. *When:* Prototyping an analytics-engine-backed app or a demo where you want the database to be the single source of state and the render path.
- **Timer-driven full-query refresh** — Wrap the main render SELECT in a setInterval with a 150 ms period. Each tick re-runs the full query and replaces the displayed frame. *When:* A low-frequency UI refresh where per-tick query cost is acceptable. The video does not measure cost.
- **Distance-based glyph shading** — Map ray distance to a character: nothing for sky, a dot for floor, and a wall glyph whose opacity or density falls off with distance, using a pixel function evaluated per cell. *When:* Text-mode or ASCII rendering where distance cues come from character choice.
- **Embedded DuckDB WASM from a CDN** — Import the DuckDB WASM build from a CDN in index.html, so the analytics engine runs in the browser with no backend. The video shows the import as the first line of the page's JavaScript. *When:* Running SQL-driven logic client-side with no server, or for local demos.

## Numbers
- index.html of the game is about 654 lines. ([1:19](https://youtu.be/1Q_62NigzN8?t=79))
- The minimap is a 16x16 grid. ([2:44](https://youtu.be/1Q_62NigzN8?t=164))
- The render query runs every 150 ms via setInterval. ([4:05](https://youtu.be/1Q_62NigzN8?t=245))
- The game uses 5 tables (map, player, enemies, bullets, settings) and 2 views (Render3DFrame, ColumnDistances). ([1:19](https://youtu.be/1Q_62NigzN8?t=79))
- Video length is 7:51. No performance or latency numbers are given. ([0:00](https://youtu.be/1Q_62NigzN8?t=0))

## Hot takes
- Presented as a stress test of what an embedded analytical DB can do, not as a recommendation for game engines or for running games in SQL.
- Presenter says he would not play a full-length game this way.
- Benchmark-free: nothing shows the per-frame cost or whether 150 ms refresh is limited by the query.

## Tools mentioned
DuckDB, DuckDB WASM, SQL, Node.js, ClickHouse, BigQuery, Docker Compose, Cursor (editor), CSS

## Relevance to our work
- **agentos** (1/3): AgentOS roadmap includes a Parquet + DuckDB archive and per-tenant DuckDB read tier. This video shows only embedded DuckDB usage, with no benchmarks or storage or query-performance data. → *If the DuckDB read-tier work starts, try DuckDB embedded against a Parquet export of agent telemetry to measure cold query latency; this video gives no numbers to use.*
