"""Render killaxbt-toolkit.html → docs/killaxbt-toolkit.pdf via Playwright."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).parent.parent
SRC  = ROOT / "pdf-src" / "killaxbt-toolkit.html"
OUT  = ROOT / "docs" / "killaxbt-toolkit.pdf"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        ctx = await browser.new_context()
        page = await ctx.new_page()
        await page.goto(SRC.as_uri(), wait_until="networkidle")
        await page.wait_for_timeout(500)
        await page.emulate_media(media="print")
        OUT.parent.mkdir(parents=True, exist_ok=True)
        await page.pdf(
            path=str(OUT),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        await browser.close()
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")

asyncio.run(main())
