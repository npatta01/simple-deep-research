import datetime
import requests 

import constants
import utils
import prompts
from langchain_core.messages import HumanMessage, SystemMessage


from langchain_openai import ChatOpenAI
import schema



def get_today_str() -> str:
    """Get current date in a human-readable format."""
    return datetime.datetime.now().strftime("%a %b %-d, %Y")




def tavily_search_helper(query: str, max_results: int = 3, **kw):
    """Call Tavily API."""
    r = requests.post(
        constants.TAVILY_BASE_URL,
        json={"query": query, "max_results": max_results, **kw},
        timeout=180
    )
    r.raise_for_status()
    return r.json()

def web_search(query: str, max_results: int = 3) -> str:
    """Search the web for information about a specific query.
    
    Args:
        query: The search query (be specific for better results)
        max_results: Number of results to return (1-5)
        
    Returns:
        Formatted search results with sources
    """
    print(f"🔍 Searching: {query}")
    
    result = tavily_search_helper(
        query,
        max_results=max_results,
        include_raw_content=True,
        topic="general"
    )
    
    unique_results = {}
    for res in result.get('results', []):
        url = res.get('url')
        if not url or url in unique_results:
            continue

        raw_content = res.get('raw_content')
        fallback_content = res.get('content') or ""
        content = summarize_webpage_content(raw_content or fallback_content)

        unique_results[url] = {
            'title': res.get('title', 'Untitled Source'),
            'content': content
        }
    
    if not unique_results:
        return "No results found."
    
    output = f"Search results for: '{query}'\n\n"
    for i, (url, data) in enumerate(unique_results.items(), 1):
        output += f"\n--- SOURCE {i}: {data['title']} ---\n"
        output += f"URL: {url}\n\n{data['content']}\n\n" + "-"*80 + "\n"
    
    return output


def summarize_webpage_content(webpage_content:str) -> str:
    """Summarize webpage content."""
    if not webpage_content:
        return "No content available from this source."

    if not isinstance(webpage_content, str):
        webpage_content = str(webpage_content)


    try:
        summarization_model = ChatOpenAI(
            model="gpt-4o-mini",
            base_url=constants.OPENAI_BASE_URL,
        ).with_structured_output(schema.SummaryOutput)


        system_prompt = prompts.summarize_webpage.format(date=utils.get_today_str(), webpage_content=webpage_content)


        summary = summarization_model.invoke([
            HumanMessage(content=system_prompt)
        ])

        return (
            f"<summary>\n{summary.summary}\n</summary>\n\n"
            f"<key_excerpts>\n{summary.key_excerpts}\n</key_excerpts>"
        )
    except Exception as e:
        print(f"Summarization failed: {e}")
        trimmed = webpage_content if len(webpage_content) <= 1000 else webpage_content[:1000] + "..."
        return trimmed
    


