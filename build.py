#!/usr/bin/env python3
"""Build the standalone single-file app and the Cloudflare Pages site."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"

html = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "styles.css").read_text(encoding="utf-8")
js = (ROOT / "app.js").read_text(encoding="utf-8")

html = html.replace(
    '<link rel="stylesheet" href="styles.css">',
    f"<style>\n{css}\n</style>",
)
html = html.replace(
    '<script src="app.js"></script>',
    f"<script>\n{js}\n</script>",
)

(ROOT / "monitor-check.html").write_text(html, encoding="utf-8")

SITE.mkdir(exist_ok=True)
(SITE / "index.html").write_text(html, encoding="utf-8")
(SITE / "404.html").write_text(html, encoding="utf-8")

(SITE / "_headers").write_text(
    """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: no-referrer
  Cross-Origin-Resource-Policy: same-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=(), magnetometer=(), gyroscope=(), accelerometer=(), interest-cohort=()
  Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'

/
  Cache-Control: public, max-age=0, must-revalidate

/*.html
  Cache-Control: public, max-age=0, must-revalidate
""",
    encoding="utf-8",
)

(SITE / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")

# Ship the licence with the site so the README's LICENSE link also resolves on Pages.
LICENSE = ROOT / "LICENSE"
if LICENSE.exists():
    (SITE / "LICENSE").write_text(LICENSE.read_text(encoding="utf-8"), encoding="utf-8")

print(f"Built monitor-check.html ({len(html):,} bytes) and site/")
