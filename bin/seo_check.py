#!/usr/bin/env python3
"""
Quick SEO / sanity check for the built Jekyll site.

Usage (from the repo root, after building the site into _site/):
    python bin/seo_check.py            # checks ./_site
    python bin/seo_check.py path/to/_site

Checks every blog post page (and the home page) for:
  - <title>, meta description (warns if missing or > 160 chars)
  - canonical link, <html lang>
  - og:title / og:description / og:image, and that the og:image file exists in _site
  - JSON-LD blocks that parse as valid JSON (and are BlogPosting on posts)
  - Google verification tag holds only the ID (not a whole <meta> tag)
  - leftover "Image N." captions and <img> tags that point to missing local files
Only uses the Python standard library.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

SITE_URL = "https://nasirlukman.github.io"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.title = ""
        self._in_title = False
        self.meta = {}
        self.canonical = None
        self.jsonld = []
        self._in_jsonld = False
        self._buf = ""
        self.imgs = []
        self.text_chunks = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = a.get("property") or a.get("name")
            if key:
                self.meta.setdefault(key, a.get("content", ""))
        elif tag == "link" and (a.get("rel") or "") == "canonical":
            self.canonical = a.get("href")
        elif tag == "script" and (a.get("type") or "") == "application/ld+json":
            self._in_jsonld = True
            self._buf = ""
        elif tag == "img" and a.get("src"):
            self.imgs.append(a.get("src"))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_jsonld:
            self.jsonld.append(self._buf)
            self._in_jsonld = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_jsonld:
            self._buf += data
        else:
            self.text_chunks.append(data)


def local_path(site_dir, url):
    """Map a site URL (absolute or root-relative) to a file in _site, or None if external."""
    p = urlparse(url)
    local_hosts = ("localhost", "127.0.0.1", "0.0.0.0")
    if p.scheme and not (url.startswith(SITE_URL) or p.hostname in local_hosts):
        return None
    path = unquote(p.path)
    if not path.startswith("/"):
        return "RELATIVE"
    return os.path.join(site_dir, path.lstrip("/").replace("/", os.sep))


def check_page(site_dir, html_path, is_post):
    issues, warns = [], []
    with open(html_path, encoding="utf-8", errors="replace") as fh:
        html = fh.read()
    pp = PageParser()
    pp.feed(html)

    title = " ".join(pp.title.split())
    desc = pp.meta.get("description", "").strip()
    if not title:
        issues.append("missing <title>")
    if not desc:
        issues.append("missing meta description")
    elif len(desc) > 160:
        warns.append(f"description is {len(desc)} chars (>160)")
    if not pp.canonical:
        issues.append("missing canonical link")
    if not pp.lang:
        issues.append("missing <html lang>")
    for k in ("og:title", "og:description", "og:image"):
        if not pp.meta.get(k):
            (issues if k != "og:image" or is_post else warns).append(f"missing {k}")
    og_img = pp.meta.get("og:image")
    if og_img:
        if not og_img.startswith("http"):
            issues.append(f"og:image is not absolute: {og_img}")
        lp = local_path(site_dir, og_img)
        if lp and lp != "RELATIVE" and not os.path.exists(lp):
            issues.append(f"og:image file not found in _site: {og_img}")
    gsv = pp.meta.get("google-site-verification", "")
    if "<" in gsv or "meta" in gsv:
        issues.append("google-site-verification content contains HTML")
    if "msvalidate.01" in pp.meta and not pp.meta["msvalidate.01"].strip():
        warns.append("empty Bing msvalidate.01 tag")

    if not pp.jsonld:
        issues.append("no JSON-LD block")
    for raw in pp.jsonld:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            issues.append(f"invalid JSON-LD: {e}")
            continue
        if is_post and data.get("@type") != "BlogPosting":
            issues.append(f"JSON-LD @type is {data.get('@type')!r}, expected BlogPosting")
        if is_post:
            for k in ("headline", "datePublished", "author", "image"):
                if k not in data:
                    warns.append(f"JSON-LD missing {k}")

    text = " ".join(pp.text_chunks)
    leftovers = sorted(set(re.findall(r"\bImage \d+\.", text)))
    if leftovers and (pp.lang or "en").startswith("en"):
        warns.append(f"old caption labels found: {', '.join(leftovers[:5])}")

    for src in pp.imgs:
        lp = local_path(site_dir, src)
        if lp and lp != "RELATIVE" and not os.path.exists(lp):
            issues.append(f"<img> points to missing file: {src}")

    return title, desc, issues, warns


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    site_dir = sys.argv[1] if len(sys.argv) > 1 else "_site"
    if not os.path.isdir(site_dir):
        sys.exit(f"Can't find '{site_dir}'. Build the site first (docker compose up, or bundle exec jekyll build).")

    pages = []
    home = os.path.join(site_dir, "index.html")
    if os.path.exists(home):
        pages.append((home, False))
    blog_root = os.path.join(site_dir, "blog")
    for root, dirs, files in os.walk(blog_root):
        rel = os.path.relpath(root, blog_root).replace(os.sep, "/")
        parts = rel.split("/")
        # posts live at blog/<year>/<slug>/index.html; skip tag/category/year archives and pagination
        if len(parts) == 2 and parts[0].isdigit() and "index.html" in files:
            pages.append((os.path.join(root, "index.html"), True))

    if not any(is_post for _, is_post in pages):
        sys.exit("No post pages found under _site/blog/<year>/<slug>/. Did the build finish?")

    n_issue = n_warn = 0
    for path, is_post in sorted(pages):
        title, desc, issues, warns = check_page(site_dir, path, is_post)
        rel = os.path.relpath(path, site_dir).replace(os.sep, "/")
        status = "FAIL" if issues else ("WARN" if warns else " OK ")
        print(f"[{status}] {rel}\n        title: {title[:90]}")
        for i in issues:
            print(f"        x {i}")
        for w in warns:
            print(f"        ! {w}")
        n_issue += bool(issues)
        n_warn += bool(warns) and not issues

    print(f"\nChecked {len(pages)} pages: {len(pages) - n_issue - n_warn} OK, {n_warn} with warnings, {n_issue} with problems.")
    sys.exit(1 if n_issue else 0)


if __name__ == "__main__":
    main()
