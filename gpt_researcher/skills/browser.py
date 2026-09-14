from ..actions.web_scraping import scrape_urls
from ..scraper import StaticScraper


class BrowserManager:
    """负责管理 URL 抓取与正文收集。"""

    def __init__(self, researcher):
        self.researcher = researcher

    async def browse_urls(self, urls: list[str]) -> list[dict]:
        """抓取 URL，并把正文结果写回研究实例。"""
        scraped_content = await scrape_urls(urls, StaticScraper)
        self.researcher.research_sources = scraped_content
        return scraped_content
