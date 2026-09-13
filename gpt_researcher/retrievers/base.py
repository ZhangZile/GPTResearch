from abc import ABC, abstractmethod
from typing import Any


class BaseRetriever(ABC):
    """定义检索器统一接口。"""

    requires_scraping: bool = True

    def __init__(self, query: str, query_domains: list[str] | None = None):
        self.query = query
        self.query_domains = query_domains or []

    @abstractmethod
    def search(self, max_results: int = 5) -> list[dict[str, Any]]:
        """返回结构化搜索结果。"""
        raise NotImplementedError
