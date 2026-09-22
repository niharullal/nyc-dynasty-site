# NYC Dynasty League Site

Static site for the NYC Dynasty fantasy football league (Sleeper league `1312585067658223616`).

- **Week tabs** — one tab per week, showing the commissioner's newsletter pages.
- **Standings tab** — live standings and current-week scoreboard, fetched client-side from the public Sleeper API (no key needed).

Open `index.html` in a browser. No build step, no server required.

## Adding a new week's newsletter

1. Create `newsletters/week-XX/` and copy the newsletter images in, numbered in
   reading order: `01-week-X-preview.jpeg`, `02-<matchup>.jpeg`, ...
2. Add an entry to the **top** of the `WEEKS` array in `weeks.js` (newest first;
   the first entry is the default tab). Copy an existing entry as a template.
3. If the week previously had a light preview entry (`preview: true`), replace
   that entry with the real `pages` entry.
4. Bump the version number in the `<script src="weeks.js?v=N">` tag in
   `index.html` so cached browsers pick up the new manifest immediately.

## Light preview weeks (no newsletter yet)

A week can be listed before its newsletter exists by giving it `preview: true`
and a `matchups` array instead of `pages` — see the Week 3 entry in `weeks.js`.
Matchup pairings come from the Sleeper API:
`https://api.sleeper.app/v1/league/1312585067658223616/matchups/<week>`
(pair rosters sharing a `matchup_id`; map `roster_id` → owner via the
`/rosters` and `/users` endpoints).
