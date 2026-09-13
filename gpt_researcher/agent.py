from .skills.researcher import ResearchConductor


class GPTResearcher:
    """研究智能体的主编排器"""

    def __init__(self, query: str):
        self.query = query
        self.context = ""
        self.research_conductor = ResearchConductor(self)

    async def conduct_research(self) -> str:
        self.context = await self.research_conductor.conduct_research()
        return self.context