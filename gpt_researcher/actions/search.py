import asyncio
from typing import Any

from ..retrievers import BaseRetriever


async def get_search_results(
    query: str,
    retriever_cls: type[BaseRetriever],
    max_results: int = 3,
) -> list[dict[str, Any]]:
    """使用指定检索器执行搜索。"""
    retriever = retriever_cls(query)

    # 检索器当前使用同步接口，这里放到线程中执行，避免阻塞事件循环。
    return await asyncio.to_thread(retriever.search, max_results=max_results)
