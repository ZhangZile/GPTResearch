from ..actions import plan_research_outline


class ResearchConductor:
    """协调研究流程。"""
    def __init__(self, researcher):
        self.researcher = researcher

    async def plan_research(self) -> list[str]:
        """为当前研究任务生成子问题。"""
        return await plan_research_outline(self.researcher.query)

    async def conduct_research(self) -> str:
        """执行最小研究流程。"""
        sub_queries = await self.plan_research()
        return "\n".join(sub_queries)