# Command Line Studios site redesign: build notes

Working record of the November 2026 redesign. For **how to update the site**, read `../README.md`.
This file covers **what was decided and why**, plus how the build was checked.

Last updated: 2026-11-21. Status: **built and verified. The owner unpacks the zip, replaces the
site folder's contents and pushes.**

---

## 1. Project and workflow

- Site: **Command Line Studios, LLC** (independent iOS app studio), https://cmdlinestudios.com.
  A static site in a public GitHub repo, served by GitHub Pages (`CNAME`).
- Brand: premium apps. **No ads (ever), no subscriptions (ever), no data collection for revenue
  (ever), no bloat.** Pay once, own it forever.
- Workflow (the owner's rule):
  1. The owner zips the **entire site folder** and hands it over.
  2. Claude unpacks it into its own working folder, rebuilds it and returns a new zip.
  3. The owner unpacks it, replaces the site folder's contents, and **commits and pushes
     themselves**. Claude never touches the repo.
- The owner confirms understanding and permission before each major step and likes a running
  decision table.

## 2. Ground rules

1. **Content stays as is. This was a design overhaul only.**
2. **Privacy statements and their "Last updated" dates never change** unless the app's practices
   change. Verified against the original files with `scripts/check_privacy.py`.
3. **No purple** anywhere.
4. Approved **added** text (decorative labels the owner OK'd):
   - Homepage:
     - `01 // ads` … `04 // focus` tile labels
     - the headline "No data collection for revenue. Ever."
     - the `+ what you need / - feature you'll never use / - another upsell screen / - tracking sdk` box
     - `$ price --once`, `$ ads --none` and `$ data --local` tags
     - "Explore the apps" and "Our promise" buttons
     - `01 // fitness` … `04 // games` labels
     - lower-case mono section labels (`// our philosophy`, `// get in touch`, …)
     - the period in "wallet."
   - `cd ~/home` back link, replacing "← back to home".
   - Education:
     - floating tags "10 solar system bodies", "Mercury → Pluto" and "Hand-verified physics"
     - "Launchpad" heading above the gallery
   - Coming-soon pages: `$ ls ~/games` / `$ ls ~/productivity`, and "// keep exploring" with links.
   - Fitness: the `beta_` tag and "// keep exploring".
   - Privacy: `// privacy` label.
5. **No status labels** on homepage category tiles.
6. The **logo links home** on every page, and there's no "Home" menu item. Contact is a
   `mailto:support@cmdlinestudios.com` button.

## 3. What was built

| Page | Path | State |
|---|---|---|
| Home | `index.html` | Hero + terminal card, promise bento, philosophy, category bento, pricing promise |
| Fitness | `categories/fitness.html` | **reps_ beta teaser** (stage 2). OG and Twitter meta tags kept exactly. |
| Productivity | `categories/productivity.html` | Coming soon (ring + check graphic) |
| Education | `categories/education.html` | **Launchpad showcase** (stage 3): 3D stack, details, badge, gallery reel, lightbox. No shelf (only 1 app). Shelf template left in a comment. |
| Games | `categories/games.html` | Coming soon (block grid graphic) |
| Data Privacy | `privacy/index.html` | One glass section per app, jump links with icons, dashed "More apps" card |

### Folder structure: kept, with three additions
The original structure is unchanged: every page, asset, `CNAME`, `.gitignore` and URL is where it
was. Additions:

- `assets/css/site.css`: the shared stylesheet. The old pages each had their own inline `<style>`.
- `assets/js/site.js`: shelf, gallery reel loop, iPhone/iPad switch and lightbox. It replaces the
  old inline script on `education.html`.
- `assets/launchpad/launchpad-icon.svg`: the Launchpad icon, flattened from the owner's Icon
  Composer bundle with `scripts/compose_icon.py`. The old site had no Launchpad icon.
- `_project/` (this folder): notes, mockups and scripts. GitHub Pages doesn't publish it.
- `README.md` was rewritten. It used to contain only the title line, which is kept as line 1.

**The `.git` folder was not included in the returned zip** (decision Q19). The owner keeps their own
`.git` when replacing the folder's contents.

Links changed from root-absolute (`/categories/...`) to **relative** (`categories/...`,
`../assets/...`). They work the same on the live site and also when the files are opened locally.

## 4. Design system: "Mono Prism v2", orange

- Look: glass and depth, bento layout, giant tight headlines, terminal and mono accents.
- Fonts (Google Fonts): **Plus Jakarta Sans** 400–800 and **JetBrains Mono** 400/500.
  These replace Space Grotesk and Inter.
- Accent **#FF6B2C**, with **#141414** text on orange. This replaces the old cyan `#00D4FF` and
  amber `#FFB347`.
- Color mode: **follows the device** (`prefers-color-scheme`). **There's no manual toggle**
  (decision Q21).

| Token | Light | Dark |
|---|---|---|
| bg | #F4F4F2 | #0B0B0D |
| fg | #0E0E10 | #F5F5F4 |
| muted | #55555C | #A1A1A6 |
| glass | rgba(255,255,255,0.58) | rgba(255,255,255,0.05) |
| stroke | rgba(14,14,16,0.08) | rgba(255,255,255,0.11) |
| hair | rgba(14,14,16,0.05) | rgba(255,255,255,0.07) |

- Glass: `backdrop-filter: blur(30px) saturate(140%)`, a 1px stroke and a 24–36px radius.
- Motion is subtle, and all of it switches off under `prefers-reduced-motion`. The gallery then
  becomes a normal sideways-scrolling row.
- Breakpoints: 1020px (smaller 3D stack), 860px (one column) and 600px (phone: 16px gutters,
  smaller stack and reel).

## 5. Changes made during the build (vs. the mockups)

1. **Restored original text the homepage mockup had dropped** (ground rule 1):
   - the terminal box lines: "No ads // ever", "No subscriptions // ever",
     "No bloat // just what you need" and "Pay once // own it forever"
   - the "iOS / One-time purchase / No ads. Ever." pills, now beside the hero
   - the four philosophy card headings ("Zero ads.", "Pay once, own it.", "Your data stays yours.",
     "Focused by design.") with their full original sentences, as bold lead-ins inside the promise
     tiles. The mockup had shortened two of them.
   - "Get in touch", now `// get in touch` in the footer
   - "View apps", which appears on hover next to each category arrow, as before
2. **Fixed** the clipped period in "No subscriptions." The heading now wraps naturally and isn't
   clipped. Checked at 1440, 1024, 768, 390 and 360px.
3. **Raised the iPad shot** in the Education 3D stack so it shows above the two iPhones. In the
   mockup position it was almost hidden.
4. "Now available on the App Store" and "$1.99 · one-time purchase" keep the **original wording and
   case**. The mockup used lower case and `//`.
5. Kept the **screenshot lightbox** from the old Education page. Clicking any gallery shot enlarges
   it, with arrow keys and Escape.
6. Real App Store link: `https://apps.apple.com/us/app/id6819044247`.

## 6. App lifecycle (also in README §2)

| Stage | When | Site change |
|---|---|---|
| 1 · Privacy first | Before submitting to TestFlight | Add the app's section to the privacy page (Apple needs a valid policy URL). Nothing on category pages. |
| 2 · Beta teaser | TestFlight approved | Add a compact beta teaser card to the category page. |
| 3 · Full release | Live on the App Store | Replace the teaser with the full showcase. Add the shelf when there are 2+ released apps. |

- **reps_**: stage 2 (teaser on Fitness, privacy section live).
- **Launchpad**: stage 3.
- Next apps: a mobile physics equation sheet (Education) and a cardio app (Fitness).

## 7. Verification done on 2026-11-21

- `scripts/check_content.py <original> <new>`: **every visible text string and every alt/meta value
  from the original six pages is present** in the new pages. The only intended drops are the
  emojis, the "Home" nav item and "← back to home".
- `scripts/check_privacy.py privacy/index.html`: **all privacy statements and both dates match**.
  A block-by-block comparison against the original page also found no differences.
- Every internal link, image and `#anchor` resolves. The only miss is the placeholder inside the
  commented-out shelf template, which is expected.
- No sideways scrolling and no clipped text on any page at 1440, 1024, 768, 390 and 360px.
- Checked visually in light and dark mode. The iPhone/iPad switch, lightbox (click, arrows, Escape)
  and reel loop all work, with no console errors.

## 8. Decision log

| # | Question | Answer |
|---|---|---|
| Q1 | Visual direction | Glass and depth |
| Q2 | Color mode | Both, follow device |
| Q3 | Motion | Subtle |
| Q4 | Workflow | Zip in, zip out; the owner pushes |
| Q5 | Scope | New look + new layouts, working with the current pages and content |
| Q6 | Branding | Fresh identity |
| Q7 | App showcase | Category pages hold their apps; no page per app |
| Q8 | Seeing the site | Live URLs for design; zip for the build |
| Q9 | Palette | Mono Prism, orange #FF6B2C (original shade, over tangerine and burnt), no purple |
| Q10 | Type | Clean geometric sans (Plus Jakarta Sans) |
| Q11 | Assets | Screenshots, App Store links, badge, icons |
| Q12 | Inspiration | None, surprise me |
| Q13 | Privacy page | New theme, same content |
| Q14 | Apps per category | 2–3 expected |
| Q15 | Multi-app layout | Shelf + showcase (shelf only with 2+ released apps) |
| Q16 | Beta apps | Three-stage lifecycle (privacy → teaser → full release) |
| Q17 | Assets per app | Varies; layout adapts |
| Q18 | Logo link | The logo links home; no separate Home item |
| Q19 | `.git` in the returned zip | Left out; the owner keeps their own `.git` |
| Q20 | Notes, mockups and scripts | `_project/` inside the site (not published, but in the public repo) |
| Q21 | Light/dark toggle | None; follow the device only |

## 9. Where things are

- Design canvas (private): https://claude.ai/artifact/Dgv8PkG3omAsssMsMkkRyj
- `mockups/*.dc.html`: the approved mockups, for design reference only. Their image URLs
  (`/_blob/...`) only work on the canvas.
- `scripts/compose_icon.py`: flattens an Icon Composer `.icon` bundle into one SVG.
- `scripts/check_privacy.py`: verifies the privacy text. Update its list when a policy changes on
  purpose.
- `scripts/check_content.py`: compares the text of two copies of the site, old and new.
