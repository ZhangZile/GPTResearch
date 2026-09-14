import asyncio
from typing import Any

from ..scraper import BaseScraper


async def scrape_urls(
    urls: list[str],
    scraper_cls: type[BaseScraper],
) -> list[dict[str, Any]]:
    """并发抓取一组 URL，并过滤无正文结果。"""
    unique_urls = list(dict.fromkeys(urls))
    scraper = scraper_cls()

    tasks = [
        asyncio.to_thread(scraper.scrape, url)
        for url in unique_urls
    ]
    results = await asyncio.gather(*tasks)

    return [
        result
        for result in results
        if isinstance(result, dict) and result.get("raw_content")
    ]
