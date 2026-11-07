#!/usr/bin/env python3
"""Print current Sainsbury's prices for the products in tools/products.json.

Usage: python3 tools/price_check.py [filter]

Prices come from Trolley.co.uk product pages, which track supermarket online
prices. Trolley says these may not match in store. Needs network access to
www.trolley.co.uk. Add or edit products by pasting their Trolley path into
tools/products.json.
"""
import html
import json
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

PRODUCTS = Path(__file__).resolve().parent / "products.json"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"


def page_lines(path):
    req = urllib.request.Request("https://www.trolley.co.uk" + path, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        s = r.read().decode("utf8", "ignore")
    s = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
    s = html.unescape(re.sub(r"<[^>]+>", "\n", s))
    return [l.strip() for l in s.split("\n") if l.strip()]


def sainsburys_price(lines):
    """Return (price, extras) for Sainsbury's from the Where To Buy block."""
    if "Where To Buy" not in lines:
        return None, "page layout not recognised"
    a = lines.index("Where To Buy")
    block = []
    for l in lines[a + 1:]:
        if l.startswith("The prices shown") or l == "Today's Price":
            break
        block.append(l)
    if block and block[0].startswith("Currently out of stock"):
        return None, "out of stock everywhere"
    for i, l in enumerate(block):
        if l == "Sainsbury's" and i + 1 < len(block) and block[i + 1].startswith("£"):
            extras = []
            for x in block[i + 2:]:
                if x == "VISIT":
                    break
                extras.append(x)
            return block[i + 1], " | ".join(extras)
    return None, "not sold at Sainsbury's"


def main():
    filt = sys.argv[1].lower() if len(sys.argv) > 1 else ""
    products = json.loads(PRODUCTS.read_text())
    print(f"Sainsbury's online prices via Trolley.co.uk, checked {date.today().isoformat()}\n")
    for name, path in products.items():
        if filt and filt not in name.lower():
            continue
        try:
            price, extra = sainsburys_price(page_lines(path))
        except Exception as e:  # network or parsing failure
            price, extra = None, f"error: {e}"
        print(f"{name:34} {price or '-':>8}  {extra}")
        time.sleep(0.3)
    return 0


if __name__ == "__main__":
    sys.exit(main())
