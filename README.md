# nasirlukman.github.io

Personal site and blog of Muhamad Nasir Lukman, built with Jekyll (simplified from the al-folio theme).

## Preview locally

Requires Docker Desktop.

```
docker compose up
```

Open http://localhost:8080. The first start installs gems and takes a few minutes; later starts are fast.
Edits to posts and pages reload automatically. After editing `_config.yml`, stop (Ctrl+C) and run it again.

## Publish

Push to `master`. GitHub Actions (`.github/workflows/deploy.yml`) builds the site and publishes it to the `gh-pages` branch.

## Where things are

| What | Where |
| --- | --- |
| Home page (bio) | `_pages/about.md` |
| Blog list + category buttons | `_pages/blog.md` |
| CV page (hidden until `published: true`) | `_pages/cv.md` |
| Posts | `_posts/YYYY-MM-DD-slug.md` |
| Images | `assets/img/` (post images), `assets/img/og/` (social previews) |
| Site settings, categories, SEO | `_config.yml` |
| Page templates | `_layouts/`, `_includes/` |
| Styles | `_sass/` |

## Writing a post

Front matter:

```yaml
---
layout: post
title: "Post title"
date: 2026-12-01 10:00:00
description: "One sentence, under ~160 characters (used by Google and link previews)."
tags: [hyperspectral, mineral-mapping]
categories: ["Geoscience"]          # Geoscience, Environment, OSINT, Other (one or more)
og_image: /assets/img/og/my_image.jpg  # optional link-preview image (JPEG, ~1200 px wide)
---
```

Images (WebP plus 480/800/1400 px versions for phones):

```liquid
{% include figure.liquid path="assets/img/my_image.webp" class="img-fluid rounded" alt="What the image shows" %}
```

Add `animated=true` for animated WebP. Math with `$$ ... $$` loads MathJax automatically.
For an interactive map, add `map: true` to the front matter and use a ```` ```geojson ```` code block.

## Checks

`python bin/seo_check.py` checks the built `_site/` for titles, descriptions, link-preview images,
structured data and broken image links.
