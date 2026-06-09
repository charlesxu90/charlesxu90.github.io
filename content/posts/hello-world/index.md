---
title: "Welcome — and how I write notes here"
subtitle: ""
date: 2024-06-09
draft: false
author: "Xiaopeng Xu"
description: "First post on the new site, and a quick reference for writing markdown notes."
tags: ["meta", "markdown"]
categories: ["General"]
lightgallery: true
toc:
  enable: true
---

Welcome to the new home of my website! I've migrated from Google Sites to a
markdown-based static site so I can keep research notes and blog posts alongside
my academic profile.

<!--more-->

## Why a markdown site?

I wanted full control over my content and the ability to write notes as plain
markdown files in a Git repository — versioned, portable, and fast.

## Writing a new note

Every note is a markdown file under `content/posts/`. To create one:

```bash
hugo new posts/my-new-note/index.md
```

Then edit the front matter at the top and write below it:

```markdown
---
title: "My new note"
date: 2024-06-09
tags: ["topic"]
categories: ["Research"]
---

Your **markdown** content goes here.
```

## Markdown features supported

This site supports the full set of features I need:

- **Code** with syntax highlighting and a copy button
- **Math** via KaTeX, e.g. inline \(E = mc^2\) and block:

$$
\mathcal{L}(\theta) = -\frac{1}{N}\sum_{i=1}^{N} \log p_\theta(y_i \mid x_i)
$$

- **Tables**, footnotes[^1], task lists, and image galleries
- **Admonitions** for callouts:

{{< admonition type=tip title="Tip" >}}
Drop images next to the note's `index.md` and reference them with a relative
path — they'll be bundled with the post.
{{< /admonition >}}

| Feature | Status |
|---------|:------:|
| Syntax highlighting | ✅ |
| Math (KaTeX) | ✅ |
| Search | ✅ |
| Dark mode | ✅ |

That's it — push to the `main` branch and the site rebuilds automatically.

[^1]: Footnotes render at the bottom of the page like this.
