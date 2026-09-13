async def plan_research_outline(query: str) -> list[str]:
    """根据用户问题生成最小研究计划。"""

    # 当前先使用固定规则模拟 Planner，后续再替换为官方的 LLM 规划逻辑
    return [
        f"{query} 的核心概念是什么？",
        f"{query} 的关键组成部分有哪些？",
        f"{query} 在实际应用中如何工作？",
    ]