from app.graphs.state import AgentState 
from app.tool.travily_search import initialize_web_search_tool
from app.utils.config import gen_response




def research_node(state:AgentState): 
    topic = state['topic'] 

    search_results = initialize_web_search_tool(topic=topic , max_result=5) 

    # Step 2: Extract clean text from results
    sources_text = "\n\n".join([
        f"Title: {res['title']}\nURL: {res['url']}\nSummary: {res['content']}"
        for res in search_results['results']
    ])

    # Step 3: Ask LLM to synthesize into research notes
    prompt = f"""
    You are a professional podcast researcher.
    Based on the following real-time web search results about "{topic}", 
    synthesize detailed research notes including:
    - Key facts and stats
    - Interesting angles or lesser-known insights
    - Controversies or debates
    - Memorable quotes or references
    - Audience hooks or surprising takeaways

    SEARCH RESULTS:
    {sources_text}

    Output in clear, structured plain text. Do NOT mention sources or URLs.
    """

    response = gen_response(prompt) 
    return {"research_notes": response.content}
