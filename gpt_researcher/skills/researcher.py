import asyncio

from ..actions import get_search_results, plan_research_outline


class ResearchConductor:
    """协调研究流程。"""

    def __init__(self, researcher):
        self.researcher = researcher

    async def plan_research(self) -> list[str]:
        """为当前研究任务生成子问题。"""
        return await plan_research_outline(self.researcher.query)

    async def search_sub_queries(self, sub_queries: list[str]) -> list[dict]:
        """并发执行所有子问题的检索。"""
        retriever_cls = self.researcher.retrievers[0]
        tasks = [
            get_search_results(query, retriever_cls)
            for query in sub_queries
        ]
        results_by_query = await asyncio.gather(*tasks)

        search_results = [
            source
            for query_results in results_by_query
            for source in query_results
        ]
        self.researcher.search_results = search_results
        return search_results

    async def browse_search_results(self, search_results: list[dict]) -> list[dict]:
        """把搜索结果中的 URL 交给 BrowserManager 抓取正文。"""
        urls = [
            source["href"]
            for source in search_results
            if source.get("href")
        ]
        return await self.researcher.scraper_manager.browse_urls(urls)

    async def conduct_research(self) -> str:
        """执行规划、检索、抓取和上下文汇总。"""
        sub_queries = await self.plan_research()
        search_results = await self.search_sub_queries(sub_queries)
        research_sources = await self.browse_search_results(search_results)

        return "\n\n".join(
            source["raw_content"]
            for source in research_sources
        )
