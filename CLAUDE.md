# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Personal academic website of Xiaopeng Xu — a **Hugo** static site using the **LoveIt** theme
(a git submodule at `themes/LoveIt`). Content is plain Markdown. Deployed to GitHub Pages
(custom domain **xu-xp.com**) automatically on push to `main`.

- Hugo **extended** is required. The local binary lives at `~/bin/hugo` (v0.163.0) and is **not** on `$PATH` — invoke it as `~/bin/hugo`.
- Content language is mostly Chinese (`hasCJKLanguage = true`, `enableEmoji = true`).

## Commands

```bash
# Local preview (includes drafts) at http://localhost:1313
~/bin/hugo server -D

# Production build — ALWAYS use this to verify before pushing.
# HUGO_ENVIRONMENT=production matters: the CDN/simpleicons data (e.g. Google
# Scholar icon, fingerprinting) is only wired up in the production environment.
HUGO_ENVIRONMENT=production HUGO_ENV=production ~/bin/hugo --gc --minify

# One-click: verify build -> commit -> push -> watch the Pages deploy via `gh`.
# Pass explicit paths to avoid sweeping unrelated work-in-progress (git add -A by default).
scripts/publish.sh -m "post: my note" content/posts/my-note
scripts/publish.sh -m "msg"           # commit ALL changes

# If the theme submodule is missing after a fresh clone:
git submodule update --init --recursive
```

There is no test suite, linter, or package manager — the "build" is the Hugo build above.

## Deployment model

- `.github/workflows/hugo.yml` builds and deploys on every push to `main` (Pages source = "GitHub Actions").
- `/public/` and `/resources/_gen/` are **git-ignored** and built by CI from a clean checkout. Never commit them; a stale local `public/` does not affect the live site.
- The deploy step (`actions/deploy-pages`) makes an authenticated API call. Intermittent `401 "Requires authentication"` failures are usually a transient GitHub incident, **not** a config problem — the build always succeeds; just re-run/re-push. `publish.sh` reports the run conclusion.

## How content works

Each post is a **page bundle**: a folder under `content/posts/<slug>/` containing `index.md`.
The folder name is the URL slug (`/posts/<slug>/`). The Notes section (`/posts/`) and homepage
auto-index every bundle — you never hand-edit a list of links. Section pages are About, Research,
Publications, Awards (`content/<section>/index.md`); the Notes menu points at `/posts/`.

Front matter shape used across posts (see any `content/posts/*/index.md`):

```yaml
---
title: "..."
date: YYYY-MM-DD        # controls sort order (newest first); future dates may publish since buildFuture is on
draft: false
description: "..."
tags: [...]
categories: ["Technology" | "Research" | "Projects" | "Reading" | "Life" | "General"]
featuredImagePreview: "<OSS url>"   # optional homepage card thumbnail
toc:
  enable: true
---
```

## Critical conventions

**Images go to Aliyun OSS via PicGo — never commit image binaries.** The repo must stay lean.
- Helper scripts already use this; reach for them first: `scripts/migrate_images.py` (Feishu temp URLs + staged TODO placeholders → OSS, in place), `scripts/format_batch.py` (raw notes: base64 + Feishu images → OSS, lift `Date:`, add front matter, demote headings), `scripts/compress-image.sh` (downscale/compress a local image for the few self-hosted assets — logo, favicon, `static/images/`; default 1600px, q80).
- OSS supports on-the-fly processing — append `?x-oss-process=image/resize,w_1600/format,webp` to serve a light variant (used for `featuredImagePreview` card thumbnails).

### PicGo upload skill (how to upload headlessly)

The PicGo desktop app must be running; it exposes a local HTTP server at `http://127.0.0.1:36677/upload`.
POST a JSON body of **absolute** file paths and it uploads them (in order) to Aliyun OSS and returns the public URLs:

```python
import json, urllib.request

def picgo_upload(path):  # path must be absolute
    req = urllib.request.Request(
        "http://127.0.0.1:36677/upload",
        data=json.dumps({"list": [path]}).encode(),
        headers={"Content-Type": "application/json"},
    )
    r = json.load(urllib.request.urlopen(req, timeout=120))
    if r.get("success") and r.get("result"):
        return r["result"][0]            # e.g. https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/<ts>.png
    raise RuntimeError(r.get("message", "picgo upload failed"))
```

Checks and patterns:
- **Confirm the server is up first:** `curl -s -m 3 -X POST http://127.0.0.1:36677/upload -H 'Content-Type: application/json' -d '{"list":[]}'` returns JSON. If it's unreachable, PicGo isn't running — ask the user to start it; do **not** fall back to committing the image.
- **base64 image** in markdown (`![alt](data:image/png;base64,...)`): decode to a temp file → `picgo_upload` → replace the markdown with `![alt](<oss-url>)`.
- **Public URL image** (e.g. a Feishu `internal-api-drive-stream.feishu.cn/...` temp link, still live): download to a temp file (verify `Content-Type` is `image/*`) → `picgo_upload` → replace the URL. These Feishu links expire, so migrate promptly.
- **Large batches** (hundreds of images take ~10–20 min): run the migration as a background task that logs progress and writes a result JSON, then poll it — see `scripts/migrate_images.py` / `scripts/format_batch.py` for the exact pattern. Handle per-image failures (leave the original on failure and report the count) rather than aborting the whole run.
- After migrating, verify **no** `data:image`, `internal-api-drive-stream`, or `TODO image` strings remain in `content/posts/`.

**Raw exported notes need formatting.** Notes pasted from Feishu/Notion arrive as a `.md` (sometimes not named `index.md`) with no front matter, a leading `# Title` or section heading, an inline `Date:` line, and embedded base64 or Feishu-URL images. Formatting means: rename to `index.md`; lift `Date:`; add front matter (title from the first heading or folder); migrate all images to OSS; and **demote body headings one level** so they nest under the post's `<h1>` title.

**Heading demotion must be fence-aware.** Bash/config code blocks contain `#`-prefixed comments and list items can contain `* # ...` headings. Demote only ATX/list-nested headings *outside* fenced code blocks, or you corrupt code comments. After formatting, verify each note renders exactly one `<h1>` (the title) and has no `##`-style demotion leaking into code.

**Always scan new content for secrets before pushing.** Config/tutorial notes have leaked real tokens (e.g. an Asana PAT). GitHub push protection will block the push; redact to a placeholder and amend before re-pushing — and the real secret must be rotated.

## Theme customization

Do **not** edit the `themes/LoveIt` submodule. Override via Hugo's layered filesystem at the project root:
- `assets/css/_custom.scss` — imported last by the theme's `style.scss`; site-specific CSS that overrides theme rules (header alignment, content width at breakpoints, left-aligned special-page titles, uncropped card thumbnails, in-content social icons). Each block is commented with what theme rule it overrides and why.
- `layouts/` — overrides/additions: `home.html`, `_partials/social-links.html`, and `_shortcodes/` (`about-intro`, `recent-news`, `social-links`).

Shortcode gotcha: a `{{% percent %}}` shortcode re-parses its own HTML through goldmark and can mangle wrapping tags; for shortcodes that emit a wrapping block (e.g. `recent-news`), use the `{{< angle >}}` form and render inner markdown explicitly.
