import requests
import time
import hashlib
from pathlib import Path
import logging

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; FantasyBot/1.0; +https://github.com/yourusername)"
}

CACHE_DIR = Path(__file__).parent.parent / "data" / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

def cache_path(url: str) -> Path:
    """Generate a cache file path based on the md5 hash of the URL."""
    url_hash = hashlib.md5(url.encode()).hexdigest()
    return CACHE_DIR / f"{url_hash}.html"

def fetch_url(url: str, use_cache=True, delay=1.5) -> str:
    """
    Fetch content from a URL with caching and polite delay.
    Returns the raw HTML text.
    """
    path = cache_path(url)

    if use_cache and path.exists():
        logging.info(f"[CACHE] Loading from cache: {url}")
        return path.read_text(encoding="utf-8")

    logging.info(f"[HTTP] Fetching URL: {url}")
    time.sleep(delay)  # polite delay to avoid hammering server
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    html = response.text
    path.write_text(html, encoding="utf-8")
    return html
