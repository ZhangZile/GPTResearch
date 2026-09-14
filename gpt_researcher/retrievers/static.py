from urllib.parse import quote

from .base import BaseRetriever


class StaticSearchRetriever(BaseRetriever):
    """用于学习检索调用链的本地模拟检索器。"""

    requires_scraping = True

    def search(self, max_results: int = 5) -> list[dict[str, str]]:
        """返回与当前查询对应的模拟搜索结果。"""
        encoded_query = quote(self.query, safe="")
        results = [
            {
                "href": f"https://example.com/research/{encoded_query}/{index}",
                "body": f"模拟搜索结果 {index}：围绕“{self.query}”返回的摘要。",
            }
            for index in range(1, 4)
        ]
        return results[:max_results]
