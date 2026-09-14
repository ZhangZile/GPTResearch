from .base import BaseScraper


class StaticScraper(BaseScraper):
    """用于学习抓取调用链的本地模拟抓取器。"""

    def scrape(self, url: str) -> dict[str, object]:
        """返回与 URL 对应的模拟正文。"""
        return {
            "url": url,
            "raw_content": f"模拟正文：这是从 {url} 抓取到的页面主体内容。",
            "title": "模拟研究页面",
            "image_urls": [],
        }
