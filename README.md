# cmdlinestudios.github.io

The website for **Command Line Studios, LLC**, an independent iOS app studio. Live at
**https://cmdlinestudios.com**, served by GitHub Pages from this repository (`CNAME`).

It's a plain static site: HTML, one stylesheet and one small script. There's no build step,
no framework and no package manager. Edit a file, commit, push, and the site updates.

> Design: **"Mono Prism v2"** (glass and depth, bento layout, terminal accents, orange `#FF6B2C`).
> Redesigned November 2026. Only the design changed; the content and URLs are the same as before.

---

## 1. Folder layout

```
cmdlinestudios-site/
├── index.html                  Homepage
├── categories/
│   ├── fitness.html            Fitness: reps_ beta teaser
│   ├── productivity.html       Productivity: "coming soon"
│   ├── education.html          Education: Launchpad showcase
│   └── games.html              Games: "coming soon"
├── privacy/
│   └── index.html              Data Privacy: one page, a section per app
├── assets/
│   ├── css/site.css            The whole design system (colors, layout, every component)
│   ├── js/site.js              Gallery reel, iPhone/iPad switch, screenshot viewer, app shelf
│   ├── badges/                 Official "Download on the App Store" badge (don't edit it)
│   ├── screenshots/            App Store marketing screenshots (<app>-iphone-N / <app>-ipad-N)
│   ├── launchpad/              Launchpad icon
│   └── reps/                   reps_ icon + 1200×630 teaser image
├── _project/                   NOT published (see below): build notes, mockups, helper scripts
├── CNAME                       cmdlinestudios.com (don't change)
├── .gitignore
└── README.md                   This file
```

**Keep these URLs.** App Store Connect and TestFlight link to `privacy/index.html`, and people
may have bookmarked the category pages. Add new pages and files as you need, but don't rename or
move these ones.

**`_project/`** holds working files: `BUILD-NOTES.md`, the design mockups and helper scripts.
GitHub Pages skips folders that start with `_`, so nothing in it goes on the live site. It is still
in the repo, which is public, so anyone browsing the repo can see it.

All links are **relative** (`../assets/...`, `fitness.html`), so the site also works when you open
the files locally. To preview it with working links, run this in the site folder:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

---

## 2. The app lifecycle: three stages

Every app moves through the same three stages, and each stage has its own change to the site. **An
app only shows on its category page once it's in TestFlight, and gets the full showcase only once
it's live on the App Store.**

| Stage | When | What to change on the site |
|---|---|---|
| **1 · Privacy first** | Before you submit the build to TestFlight | Add the app's section to `privacy/index.html` (Apple needs a working privacy-policy URL to approve TestFlight). **Don't change the category page yet.** |
| **2 · Beta teaser** | TestFlight approves the build | Add a **beta teaser card** to the category page (§4.2). No price, App Store badge or gallery. |
| **3 · Full release** | The app is live on the App Store | **Replace the teaser with a showcase** (§4.3): 3D screenshot stack, details card, App Store badge and gallery. With 2+ released apps in a category, add the **app shelf** (§4.4). |

Where things stand (November 2026):

| App | Category | Stage |
|---|---|---|
| Launchpad: Planetary Simulator | Education | 3 · released ($1.99) |
| reps_: Your Digital Logbook | Fitness | 2 · beta teaser |
| *(next)* Mobile physics equation sheet | Education | not started |
| *(next)* Cardio app | Fitness | not started |

**Order within a category = build order.** The first app built is the default/eye-catcher
(Launchpad in Education, reps_ in Fitness).

---

## 3. Ground rules

1. **Content is the source of truth.** Design changes must never change the wording on the site.
2. **Never edit an existing privacy statement or its "Last updated" date** unless the app's data
   practices have actually changed. If they have, change the text and update the date.
3. **No purple, ever.** Orange `#FF6B2C` is the only accent color, with `#141414` text on orange.
4. **No status labels on the homepage category tiles** (no "1 app available", "In development",
   etc.). Visitors explore the category pages to find out.
5. The **logo `>_ Command Line Studios` is the link home** on every page. There's no "Home" menu item.
6. **Contact** is a `mailto:support@cmdlinestudios.com` link (the orange button in the nav).
7. **Screenshots are App Store marketing images** that already include the device frame and caption.
   Don't add frames around them.

---

## 4. How to update the site

Every page uses the same nav, footer and stylesheet. When you change the nav or footer, change it
on **all six pages** (it's copied in each one).

### 4.1 Stage 1: add a privacy section

In `privacy/index.html`:

1. Add a **jump link** inside `<nav class="jumps">`:
   ```html
   <a class="jump glass" href="#APP-ID"><img src="../assets/APP-ID/APP-ID-icon.png" alt="">App Name: Subtitle</a>
   ```
2. Copy an existing `<article class="policy glass" id="...">` block, put it **above** the dashed
   "More apps, more policies" card, and change the `id`, icon, name, `Last updated: Month YYYY` and
   paragraphs. The first paragraph is styled slightly bolder automatically.
3. Put the app's icon in `assets/APP-ID/` (a 384×384 PNG or an SVG).

`APP-ID` is a short lowercase id (`launchpad`, `reps`). Use the same id everywhere: the privacy
anchor, the asset folder, the category page anchor and screenshot file names.

### 4.2 Stage 2: add a beta teaser (TestFlight)

Use `categories/fitness.html` as the template. Copy the block between
`<!-- ============ BETA TEASER ... -->` and `<!-- ============ /BETA TEASER ... -->` into the
category page:

- If the category page currently says **"coming soon"**, replace the whole
  `<!-- COMING SOON -->` block with the teaser.
- If the category already has **released** apps, put the teaser **below** their showcases.

Change the `id`, the teaser image (1200×630 PNG works well), icon, name and description. Keep the
`beta_` tag and the `// in beta testing · coming soon to the App Store` line.

If the page should show a nice preview when it's shared, update the `og:` and `twitter:` meta tags
in `<head>`, as `fitness.html` does.

### 4.3 Stage 3: replace the teaser with a showcase (App Store)

Use `categories/education.html` as the template. A showcase is the two blocks marked
`<!-- ============ SHOWCASE: ... -->`, both with the same `data-app="APP-ID"`:

1. **Main block** (inside `<main>`): 3D stack + details card + gallery header.
   - **3D stack**: `s-back` = an iPad screenshot (sits at the back-left, mostly visible),
     `s-left` and `s-right` = two iPhone screenshots fanned to its right. No iPad shots? Delete the
     `s-back` line and the two iPhones center themselves automatically.
   - **Fact labels**: the `float-tag` chips inside `<div class="stage-tags">` are optional short
     facts (keep them to 3, a few words each). On wide screens they float in the stage's corners,
     always on top of the screenshots; set each one's corner with its inline `left/right/top/bottom`.
     Below 1020px they automatically become a centered row of pills under the stack.
   - **Details card**: "Now available on the App Store" tag, name, price
     (`<b>$X.XX</b> <span>· one-time purchase</span>`), description, ✓ points (`<li>` items; the
     check mark is added automatically), App Store badge link
     (`https://apps.apple.com/us/app/idXXXXXXXXXX`), and the privacy link
     `../privacy/index.html#APP-ID`.
   - **Gallery header**: `data-gallery="reel-APP-ID"`. No iPad shots? Delete the iPhone/iPad switch
     (`<div class="seg-group ...">`).
2. **Reel block** (after `</main>`, so it runs edge to edge): `<div class="reel" id="reel-APP-ID">`
   with one `<div class="track iphone">` and, if you have them, one `<div class="track ipad" hidden>`.
   Each screenshot is a `<button class="frame">` with an `<img>`. Write good `alt` text, for example
   "Launchpad on iPhone: Two worlds. One launch".
   - **Fewer than 4 screenshots?** Leave out the gallery header and reel block. The 3D stack is enough.
   - Don't duplicate screenshots for the loop. `site.js` does that itself.
3. Name screenshots `assets/screenshots/APP-ID-iphone-N.webp` and `APP-ID-ipad-N.webp`.
4. Make sure the lightbox `<div class="lightbox" ...>` and
   `<script src="../assets/js/site.js"></script>` are at the bottom of the page (copy them from
   `education.html`).
5. Delete the app's beta teaser.

### 4.4 Two or more released apps in one category: the app shelf

When a category has **2+ apps on the App Store**:

1. Uncomment the **APP SHELF** template near the top of `education.html` (or copy it into the
   category page). Add one `shelf-tile` per released app, **in build order**, each with
   `data-app="APP-ID"`. The first one has `aria-selected="true"`.
2. Add a showcase (§4.3) for each app. `site.js` shows one app at a time and switches when a tile
   is clicked. Links like `categories/education.html#APP-ID` open that app directly.
3. With only **one** released app, leave the shelf out.

### 4.5 A category's first app

A category with no apps shows the **"Coming soon"** panel (`games.html`, `productivity.html`).
When its first app reaches stage 2, replace that panel with the teaser (§4.2). The category tile on
the homepage doesn't change.

### 4.6 Changing the look

Everything visual lives in `assets/css/site.css`:

- **Colors**: the tokens at the top (`:root` for light mode, `@media (prefers-color-scheme: dark)`
  for dark mode). The site **follows the visitor's device setting**. There's no manual toggle.
- **Fonts**: Plus Jakarta Sans (text) and JetBrains Mono (labels), loaded from Google Fonts in each
  page's `<head>`.
- **Motion**: subtle, and turned off automatically for visitors who set "Reduce Motion" on their
  device (`prefers-reduced-motion` at the bottom of the file).
- **Phones**: layouts drop to one column under 860px wide. Check changes at phone width.

---

## 5. Checklist before you push

- [ ] Privacy text and dates are unchanged (unless you meant to change them).
- [ ] New app ids match everywhere: privacy anchor, asset folder, `data-app`, `reel-` id.
- [ ] Links work when the site is served locally (`python3 -m http.server`).
- [ ] The page looks right on a phone and in both light and dark mode.
- [ ] Helper scripts in `_project/scripts/` pass (see `_project/BUILD-NOTES.md`).
