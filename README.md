# charlesxu90.github.io

Personal academic website of **Xiaopeng Xu**, built with [Hugo](https://gohugo.io/)
and the [LoveIt](https://github.com/dillonzq/LoveIt) theme. Notes and blog posts
are written as plain markdown files.

## Structure

```
content/
├── _index.md              # home page (profile comes from hugo.toml)
├── about/index.md         # bio, research, education, experience
├── publications/index.md  # selected publications
└── posts/                 # ← write markdown notes/blogs here
    └── hello-world/index.md
static/images/avatar.png   # profile photo (replace with your own)
hugo.toml                  # site configuration
themes/LoveIt/             # theme (git submodule)
.github/workflows/hugo.yml # auto-build + deploy on push to main
```

## Local preview

Hugo **extended** is required (the local binary used to build this lives at `~/bin/hugo`).

```bash
# clone with the theme submodule
git clone --recurse-submodules <repo-url>
cd charlesxu90.github.io

# live preview at http://localhost:1313 (includes drafts)
hugo server -D
```

If you cloned without `--recurse-submodules`:

```bash
git submodule update --init --recursive
```

## Writing a new note / blog post

```bash
hugo new posts/my-note/index.md
```

Edit the front matter, write markdown below it, then commit & push:

```bash
git add content/posts/my-note
git commit -m "post: my note"
git push           # GitHub Actions rebuilds and deploys automatically
```

Set `draft: false` when it's ready to publish.

## Publishing (one-time setup)

This repo deploys via **GitHub Actions** (`.github/workflows/hugo.yml`):

1. On GitHub → **Settings → Pages → Build and deployment → Source** = **GitHub Actions**.
2. Push to `main`. The site builds and deploys to
   <https://charlesxu90.github.io/>.

### Using your custom domain (xu-xp.com)

When you're ready to move `xu-xp.com` off Google Sites:

1. In `hugo.toml`, set `baseURL = "https://www.xu-xp.com/"`.
2. Create a file `static/CNAME` containing one line: `www.xu-xp.com`.
3. On GitHub → **Settings → Pages → Custom domain**, enter `www.xu-xp.com`
   and configure your DNS (CNAME → `charlesxu90.github.io`).

## Content

All pages are populated from the previous Google Site (xu-xp.com):

- `content/about/index.md` — bio, education, experience, service
- `content/research/index.md` — research interests
- `content/publications/index.md` — 16 articles, 1 patent, 2 theses (with links/PDFs)
- `content/awards/index.md` — awards & honours
- `static/images/avatar.png` — headshot (cropped from the public KAUST profile)

Social links (GitHub, Google Scholar, ResearchGate, LinkedIn, ORCID, email) are
configured in `hugo.toml` under `[params.social]`.

## Optional follow-ups

- [ ] Swap in a higher-resolution / preferred headshot if you have one.
- [ ] Move the `xu-xp.com` domain over (see custom-domain steps above).
