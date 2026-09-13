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

        sources = [
            source
            for query_results in results_by_query
            for source in query_results
        ]
        self.researcher.research_sources = sources
        return sources

    async def conduct_research(self) -> str:
        """执行规划、检索和上下文汇总。"""
        sub_queries = await self.plan_research()
        sources = await self.search_sub_queries(sub_queries)

        return "\n".join(
            f"- {source['body']}"
            for source in sources
        )
