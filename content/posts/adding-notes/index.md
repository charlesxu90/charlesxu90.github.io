---
title: "How I add notes to this site"
subtitle: ""
date: 2026-06-11
draft: false
author: "Xiaopeng Xu"
description: "A how-to for adding new notes to this Hugo site — file layout, front matter, indexing, images, and publishing."
tags: ["meta", "workflow"]
categories: ["General"]
lightgallery: true
toc:
  enable: true
---

A quick reference (mostly to my future self) for adding a new note here, and how
the **Notes** section indexes them automatically.

<!--more-->

## How notes are indexed

The **Notes** menu points at `/posts/`. I never edit a list of links by hand —
Hugo builds the index for me:

- The list page comes from `content/posts/_index.md`.
- Every folder under `content/posts/` with an `index.md` becomes one note.
- Notes are sorted by the front-matter **`date`**, newest first.
- `tags` and `categories` generate their own index pages (`/tags/…`, `/categories/…`).
- Push to `main` → GitHub Actions rebuilds and deploys.

## Steps to add a new note

1. **Create a page bundle** — a folder named after the URL slug, with an `index.md` inside:

   ```bash
   hugo new posts/tracking-research-trends/index.md
   ```

   This creates `content/posts/tracking-research-trends/index.md`, which will be
   served at `/posts/tracking-research-trends/`.

2. **Fill in the front matter** at the top of the file:

   ```markdown
   ---
   title: "Tracking trends in scientific research"
   date: 2026-06-11
   draft: false
   author: "Xiaopeng Xu"
   description: "One-line summary shown in search and previews."
   tags: ["research-trends", "reading"]
   categories: ["Research"]
   toc:
     enable: true
   ---
   ```

3. **Write the body** in markdown below the front matter.

4. **Add a summary cut** where the preview card should stop:

   ```markdown
   A short hook that shows on the Notes list and homepage.

   <!--more-->

   The full note continues here…
   ```

5. **Host images on Aliyun OSS, not in the repo.** Upload with PicGo (it copies a
   URL to the clipboard), then reference that URL — keeping binaries out of git
   keeps the repo small. Append OSS image-processing params to serve a light,
   resized version, and use a quoted title for the caption:

   ```markdown
   ![Trend overview](https://<bucket>.oss-cn-beijing.aliyuncs.com/img/<name>.png?x-oss-process=image/resize,w_1600/format,webp "Publications per year in my field.")
   ```

6. **Preview locally**, then publish by pushing to `main`:

   ```bash
   hugo server -D          # -D also shows drafts
   git add content/posts/tracking-research-trends
   git commit -m "post: tracking trends in scientific research"
   git push origin main
   ```

## Front-matter cheatsheet

| Field | Purpose |
|---|---|
| `title` | Shown as the heading and in the Notes list |
| `date` | Controls sort order (newest first) |
| `draft` | `true` hides it from the production build |
| `description` | Used in search results and link previews |
| `tags` / `categories` | Build `/tags/…` and `/categories/…` index pages |
| `featuredImagePreview` | Thumbnail shown on the homepage post card (optional; an OSS URL) |
| `toc.enable` | Toggles the table of contents |

{{< admonition type=note title="Post thumbnails" >}}
The homepage cards only show a thumbnail when a post sets `featuredImagePreview`
— there's no automatic image pick, so each note opts in deliberately. Point it at
an OSS URL (a small card variant is enough), e.g.
`...png?x-oss-process=image/resize,w_800/format,webp`.
{{< /admonition >}}

{{< admonition type=tip title="Drafts and dates" >}}
Set `draft: true` while writing — it stays out of the live site until you flip it
to `false`. Future-dated posts are also hidden until their date arrives.
{{< /admonition >}}

## Pre-publish checklist

- [ ] Folder is `content/posts/<slug>/index.md`
- [ ] `draft: false` and a correct `date`
- [ ] `description` set (for search and previews)
- [ ] `tags` / `categories` chosen
- [ ] Images co-located and rendering
- [ ] Previewed locally, then pushed to `main`

That's the whole workflow — next up, notes like *tracking trends in scientific
research* are just a new folder away.
