from .retrievers import StaticSearchRetriever
from .skills.researcher import ResearchConductor


class GPTResearcher:
    """研究智能体的主编排器。"""

    def __init__(self, query: str):
        self.query = query
        self.context = ""
        self.research_sources: list[dict] = []
        self.retrievers = [StaticSearchRetriever]
        self.research_conductor = ResearchConductor(self)

    async def conduct_research(self) -> str:
        """启动研究流程并保存最终上下文。"""
        self.context = await self.research_conductor.conduct_research()
        return self.context
