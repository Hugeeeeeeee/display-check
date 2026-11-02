# Display Check · Monitor Self-Test

[中文 → README.md](README.md) | **English**

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Offline](https://img.shields.io/badge/100%25-offline-blue)](#privacy--security)
[![Star on GitHub](https://img.shields.io/badge/Star%20on%20GitHub-display--check-f5a623)](https://github.com/Hugeeeeeeee/display-check)

New monitor in the box, a used panel you want to inspect, or a return claim that needs evidence — open one web page, run ten full-screen tests, and walk away with a report you can print, copy or export.

- **Fully local**: no backend, no analytics, no external fonts or CDNs. The browser makes zero outbound requests (`connect-src 'none'`).
- **Ten full-screen tests**: dead pixels, gradients, grayscale levels, uniformity, backlight bleed, sharpness, motion clarity, refresh rate, viewing angles, gamma.
- **One report**: verdict, per-test results, your notes and screen information — print or save as PDF, copy a plain-text summary, export/import progress as JSON.
- **Bilingual interface**: Simplified Chinese and English, picked from your browser language, switchable with `L` at any time.
- **Progress stays on your machine**: close the tab, come back later, continue where you stopped.

> ⭐ **[Leave a star on GitHub](https://github.com/Hugeeeeeeee/display-check)** — this project is anonymous, free, has no ads and takes no money. A star is the only reward it can get: it helps other people who just unboxed a display and have no idea how to check it. [One click is enough](https://github.com/Hugeeeeeeee/display-check). Thank you.

Live demo: <https://displaycheck.pages.dev> ｜ Repository: <https://github.com/Hugeeeeeeee/display-check>

## Open it

Three ways, none of them need an install or a network connection:

| Option | Best for |
| --- | --- |
| Double-click `monitor-check.html` | The single-file build — send it to someone, keep it on a USB stick, run it on another computer |
| Open `index.html` in a browser | Development version, loads `styles.css` and `app.js` from the same folder |
| <https://displaycheck.pages.dev> | Use it online; the served bytes are identical to the single-file build |

Use a recent Chrome, Edge or Safari. Tests try to go full screen automatically, but browsers only allow full screen from a real user gesture: clicking a card on the home screen or pressing `F` works, while opening a shared `#test-name` link directly will not auto-fullscreen — press `F`.

## The ten tests

They run in the order shown on the home cards; press `1`–`9` or `0` on the home screen to jump straight to one.

| # | Test | What you look for |
| --- | --- | --- |
| 1 | Dead pixels & solids | Nine full-screen solid colours (white / black / red / green / blue / cyan / magenta / yellow / grey) — bright dots on black, dark dots on white |
| 2 | Gradients & banding | Whether ramps are smooth or break into steps; six channels (grey / shadows / highlights / R / G / B) and a **Dither** switch that rules out fake bands created by browser interpolation |
| 3 | Grayscale detail | Whether black levels 0–10 and white levels 245–255 actually separate |
| 4 | Brightness uniformity | Seven full-screen fields to spot corner tint and dark corners; `G` overlays a grid to help locate them |
| 5 | Backlight bleed | Pure black with the lights off — glow at the edges, washed-out blacks |
| 6 | Sharpness & pixel mapping | Whether the 1:1 checkerboard moirés, whether hairlines stay continuous, whether small text blurs or gains coloured fringes |
| 7 | Motion clarity | Fast-moving bars — check the trailing edge for smearing, white or black overshoot; speed adjustable from 80 to 1600 px/s |
| 8 | Refresh rate & frame pacing | Frames measured with `requestAnimationFrame`, compared against the panel's rated hz, plus dropped-frame counting while the bar glides |
| 9 | Viewing angles | Four colour blocks and a centre dot — hue and brightness should not wash out when seen off-axis |
| 10 | Gamma calibration | Checkerbox against flat grey; when both halves match, the slider reading gives you an estimated γ (desktop panels usually sit near 2.2) |

## Controls inside a test

Every test puts its controls in the HUD at the bottom, and `Space` triggers the primary action of the test you are in:

| Test | Controls | `Space` does |
| --- | --- | --- |
| Dead pixels & solids | Nine colour swatches, click to jump to one | Next colour |
| Gradients & banding | Channel dropdown + Dither switch | Next channel |
| Grayscale detail | — (static pattern, just look) | — |
| Brightness uniformity | Seven field swatches + grid switch (`G`) | Next field |
| Backlight bleed | — (pure black; turn the lights off) | — |
| Sharpness & pixel mapping | Black / white background toggle | Flip background |
| Motion clarity | Speed slider 80–1600 px/s + pause / resume | Pause / resume |
| Refresh rate & frame pacing | Pause / resume (measured hz and drops shown at the top) | Pause / resume |
| Viewing angles | — (read the colours head-on, then look from the side) | — |
| Gamma calibration | Grey slider 120–240 + one-click reset | Reset to 186 |

In any test, press `M` (or the pencil icon at the bottom) to add a **note** — “glow in the bottom-right corner”, “bright spot centre-left”. Notes appear on the home cards and in the report, and they travel with the copied summary and the exported JSON. They are stored in your browser only.

## Keyboard

| Key | Action |
| --- | --- |
| `←` `→` | Previous / next test |
| `Space` | Primary action of the current test (next colour, next channel, pause, …); when a HUD control has focus the key goes to the control instead |
| `P` / `X` | Mark pass / fail |
| `M` | Add or edit a note for the current test |
| `G` | Show the grid in the uniformity test |
| `F` | Enter / leave full screen |
| `R` | Open / close the report |
| `T` / `?` / `F1` | Open the judgement cheat sheet and shortcut panel |
| `L` | Switch interface language |
| `1`–`9` `0` | On the home screen, open test 1–9 and test 10 |
| `Esc` | Leave full screen; when not full screen, back to home / close report / close panel |

Combinations with `Ctrl` / `Cmd` / `Alt` never trigger these shortcuts. Notes are typed in the browser's own prompt, so there is no in-page text field that could swallow your keystrokes.

Touch: **swipe left or right** during a test to change tests, **double-tap** to mark it pass.

## How a run goes

1. Press **Run all tests** on the home screen — it starts at the first unmarked test and turns on continuous mode.
2. After each test press `P` (pass) or `X` (fail); continuous mode moves on for you.
3. Marking the tenth test generates the **report**: verdict, per-test results, notes and screen information (resolution, measured refresh rate, pixel ratio, gamut and HDR capability).
4. From the report you can
   - **print / save as PDF** — the print stylesheet is laid out for A4 and the footer carries the project URL;
   - **copy the text summary** — plain text, ready to paste into a chat or a warranty ticket;
   - **back up / restore progress** — export and import JSON to continue on another device;
   - **re-test** — clear this round and start over.
5. Opening a single card does not auto-advance, so you can re-check one test in peace. `R`, or the report icon in the top-right, opens the report at any time.

## Judgement cheat sheet

Press `T` (or `?`) in the app for the same guidance inline; here it is in text form:

- **Dead pixels**: a permanently lit white dot, coloured dot or unlit black dot on a solid field is a dead / stuck subpixel.
- **Gradients**: obvious vertical banding in a ramp points at poor bit depth or gamma handling — trust it only if the bands survive **Dither** being switched on.
- **Grayscale**: being able to separate black levels down to 2–3, and seeing steps at the white end (245–255), is fine.
- **Uniformity**: corners and centre should match; a slight difference is normal, visible tint or dark corners are not.
- **Bleed**: mild corner bleed on IPS is normal; a large glow or a milky black is return-worthy.
- **Sharpness**: a 1:1 checkerboard must not moiré; text must not blur or show coloured fringes.
- **Motion**: the trailing edge of moving bars must not show long smear, white or black overshoot.
- **Refresh**: measured hz should be close to the rated value, and the bar should glide evenly without jumps.
- **Viewing angles**: colours must not wash out or shift noticeably when seen from the side.
- **Gamma**: if both halves match around 186, γ is close to 2.2.

## Test conditions

1. Use the panel's native resolution and 100% system scaling (on high-DPI screens the OS recommendation is fine, but scaling breaks the 1:1 pixel test).
2. Turn off night mode, eye-comfort mode, HDR and vendor “colour enhancement” / sharpening before you start.
3. Run the dead-pixel, bleed and grayscale tests in a dark room, and let the panel warm up for 20–30 minutes.
4. Do the motion and refresh tests in their own full-screen window — background tabs get throttled and the numbers will lie.

## Language

- The interface has two languages: Simplified Chinese (`zh-CN`) and English (`en`), 252 strings each, key for key, with no placeholder gaps.
- Your last manual choice wins (stored in `localStorage` under `displaycheck.lang.v1`); with no choice yet, `zh*` browser languages get Chinese and everything else gets English.
- Switch via the 「中 / EN」 segmented control in the top-right of the home screen, the language button inside a test and in the report, or the `L` key (it cycles when more than two languages are registered). The open test, the report, the cheat sheet and the summary all update immediately — no need to go back to the home screen.
- The copied text summary, the exported JSON, the print footer, `<title>`, `meta description` and the Open Graph / Twitter card strings all follow the current language. The test patterns themselves (colour fields, checkerboards, the Chinese and Latin text samples) deliberately do not — those samples *are* the sharpness test.
- **Adding a third language**: copy the `ZH` dictionary in `app.js`, rename it to your language code, and register one line in `STRINGS`. The segmented control, the `L` cycle and the missing-key fallback all adapt automatically; add one line in `detectLang()` to map browser languages onto it. A missing key falls back to Chinese and renders as `???`, and the key name is logged to the Console — so a quick way to accept a new language is to click through every screen and check nothing shows `???`.

## Repository layout

```
index.html                 development page (loads the two files below)
styles.css                 all styling, including the print sheet
app.js                     all logic plus the Chinese and English dictionaries
build.py                   packaging: single-file build and the site/ folder
monitor-check.html         artefact: single-file offline build (CSS and JS inlined)
site/                      artefact: ready-to-deploy static site
  index.html 404.html      the same app (404.html is identical, so any path opens the tool)
  _headers                 security headers and cache policy
  robots.txt  LICENSE
.qoder/rules/              this project's own development and delivery rules
```

## Build

```bash
python3 build.py
```

Standard library only — nothing to install. It produces:

- `monitor-check.html` — the single-file offline build with `styles.css` and `app.js` inlined;
- `site/` — the deploy folder, where `index.html` and `404.html` equal the single-file build.

After changing `index.html`, `styles.css`, `app.js`, or the `_headers` template inside `build.py`, you **must** run `python3 build.py` again, otherwise the deployed artefacts drift from the source. The three HTML files should be byte-identical; check with `md5 -r monitor-check.html site/index.html site/404.html`.

On macOS you can syntax-check `app.js` without Node (JXA has no `require`):

```bash
osascript -l JavaScript -e "ObjC.import('Foundation'); var s=$.NSString.stringWithContentsOfFileEncodingError('app.js',$.NSUTF8StringEncoding,null).js; new Function(s); 'syntax ok'"
```

## Deploying to Cloudflare Pages

The live site at <https://displaycheck.pages.dev> is a Pages **Direct Upload** of the committed `site/` folder; no build runs in the cloud. Two ways to refresh it:

1. **Direct Upload**: run `python3 build.py` locally, then drag `site/` onto the Pages upload area, or use wrangler:

   ```bash
   npx wrangler pages deploy site --project-name displaycheck
   ```

2. **Connect to Git**: choose *Connect to Git* in Cloudflare Pages and pick this repository, with **Framework preset: None**, **Build command empty**, **Output directory `site`**, production branch **`main`**. Because `site/` is committed, no build is needed; every later `git push` redeploys in a few minutes.

pages.dev project names are **globally unique**: `display-check`, `monitor-check` and `screen-check` were already taken by someone else, so this project uses `displaycheck`. If you deploy under another name, update the links at the top of this file, in the deploy section, and in [README.md](README.md).

`site/_headers` already ships the security headers and the no-cache rules for HTML, so nothing extra is needed on the platform.

## Privacy & security

The page makes no requests, enforced twice — in the code and in the response headers:

- No backend, no analytics, no ads, no external fonts or CDNs. `Content-Security-Policy: connect-src 'none'` blocks outbound connections at the header level, and `base-uri 'none'` plus `form-action 'none'` close off navigation and form submission targets.
- Screen specs, marks and notes are never collected or uploaded. They live in three `localStorage` keys on your machine (progress `displaycheck.progress.v1`, language `displaycheck.lang.v1`, and the dismissed-star-hint flag `displaycheck.starHinted.v1`); clearing browser data deletes them completely.
- Sharing happens through local artefacts only: copied text summary, printed PDF, exported JSON — you decide what leaves your machine.
- Response headers disable camera, microphone, geolocation, payment, USB and every sensor permission, send `Referrer-Policy: no-referrer`, and forbid framing via `frame-ancestors 'none'` plus `X-Frame-Options: DENY`.
- Notes and any imported content are HTML-escaped before touching the DOM, and restoring a backup JSON accepts only known test ids, coerces values to strings and truncates them to 300 characters — pasting a hostile JSON cannot execute anything and cannot corrupt the interface.
- The only external link is the GitHub repository URL, and it appears solely in plain `<a target="_blank" rel="noopener noreferrer">` tags.
- The badges at the top load only when the README is viewed on GitHub; the app and the deployed site request nothing externally.
- Published anonymously (see `LICENSE`), with commits using GitHub's noreply email.

## FAQ

- **It opened in English?** Your browser language is not `zh*`, so English was auto-selected. Click 「中」 in the top right or press `L`; the choice is remembered.
- **No full screen when a test opens?** Browsers only grant full screen on a genuine user gesture. Press `F`. Some browsers are strict about what counts after navigating back — click once more.
- **Measured hz looks low or jumpy?** `requestAnimationFrame` reports the rate the browser actually presents, which tab throttling, power saving and variable refresh rate all affect. Measure in full screen, in the foreground, with nothing heavy running elsewhere.
- **I see banding in a gradient — is the panel broken?** Switch Dither on and look again. Bands that survive dithering are worth worrying about; bands that disappear came from browser interpolation or bit-depth handling.
- **Do results follow me to another computer?** No. Use **Back up progress** on the report to export JSON, then **Restore progress** on the other device.
- **Did my notes disappear?** Notes and marks share the same `localStorage` store, so clearing browser data — or using a private window — wipes them. Print or export JSON if the result matters.

## Feedback & contributing

- Something broken, or an idea for another test (per-region uniformity sampling, more colour-temperature fields): open an [Issue](https://github.com/Hugeeeeeeee/display-check/issues) with your browser version, resolution and scaling.
- Keep the rules when changing code: no new dependencies or network calls; all copy goes into the `ZH` / `EN` dictionaries rather than being hardcoded in render logic; run `python3 build.py` afterwards and confirm the three HTML artefacts still match.
- Before opening a PR, describe the motivation, and include both the Chinese and English wording for any UI change.

## Star

To be explicit about what this project wants: **a star**.

- Repository: <https://github.com/Hugeeeeeeee/display-check> (try it online: <https://displaycheck.pages.dev>)
- If it helped, [leave a star](https://github.com/Hugeeeeeeee/display-check) — and pass it to whoever is unboxing a display this week.

The in-app reminder is deliberately restrained: the banner appears once, and only after you have completed all ten tests and opened the report for the first time. Dismissing or seeing it is recorded in `localStorage` (`displaycheck.starHinted.v1`) so it never nags again. The report footer and the copied summary each carry one line with the project URL. It is a plain link — no analytics script, no extra request.

The repository address is defined in exactly **one place** — the `REPO` constant at the top of `app.js` (after changing it you must run `python3 build.py`, or `monitor-check.html` and `site/` will keep the old address):

```js
const REPO = 'Hugeeeeeeee/display-check';   // no https:// prefix
```

It drives the GitHub entry on the home screen, the one-time banner at the top of the report, the report footer, the copied summary and the URL inside the exported JSON. While the placeholder `YOUR_GITHUB_USERNAME` is untouched, all of these hide themselves rather than linking to a page that does not exist.

## License

MIT — use, modify and redistribute freely. See [LICENSE](LICENSE) (also served at <https://displaycheck.pages.dev/LICENSE>).

---

If this caught a dead pixel or saved you from a bad return, [a star](https://github.com/Hugeeeeeeee/display-check) is the best way to say so. 中文读者请看 [README.md](README.md)。
