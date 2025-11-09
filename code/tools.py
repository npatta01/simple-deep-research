import utils
import constants
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


@tool
def web_search_tool(query: str, max_results: int = 3) -> str:
    """Search the web for information about a specific query.
    
    Args:
        query: The search query (be specific for better results)
        max_results: Number of results to return (1-5)
        
    Returns:
        Formatted search results with sources
    """
    print(f"🔍 Searching: {query}")

    results = utils.web_search(query, max_results=max_results)

    return results


@tool
def think_tool(reasoning: str) -> str:
    """Document your thinking process.

    Use this to analyze findings, plan next steps, and show your reasoning.

    Args:
        reasoning: Your detailed thought process
    """
    print(f"💭 Thinking: {reasoning[:100]}...")
    return f"Reasoning recorded: {reasoning}"


@tool
def summarize_findings_tool(findings: str) -> str:
    """Summarize and organize research findings.
    
    Args:
        findings: The raw findings to summarize
    """
    print(f"📝 Summarizing {len(findings)} chars of findings")
    
    model = ChatOpenAI(
        model="gpt-4o",
        base_url=constants.OPENAI_BASE_URL,
        max_tokens=16000,
    )

    system_prompt = f"""You are a research summarization assistant. Today is {utils.get_today_str()}.

Create a comprehensive research summary with:
1. Key information organized clearly
2. Inline citations [1], [2], etc.
3. Sources list at the end

Format:
**Summary**
[Findings with citations]

**Sources**
[1] Source 1
[2] Source 2
"""
    
    response = model.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Summarize:\n\n{findings}")
    ])
    
    return response.content