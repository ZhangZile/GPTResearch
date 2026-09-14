from abc import ABC, abstractmethod
from typing import Any


class BaseScraper(ABC):
    """定义网页抓取器的统一接口。"""

    @abstractmethod
    def scrape(self, url: str) -> dict[str, Any]:
        """抓取单个 URL，并返回结构化正文数据。"""
        raise NotImplementedError
