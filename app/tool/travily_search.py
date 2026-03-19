from tavily import TavilyClient 
from app.utils.env import TRAVILY_API_KEY

TRAVILY_CLIENT = TavilyClient(api_key=TRAVILY_API_KEY)  


def initialize_web_search_tool(topic , max_result=5):
    
    search_result = TRAVILY_CLIENT.search(
        query=topic , 
        max_results=max_result , 
        include_answer=False , 
        include_raw_content=False,  # Keep it fast
        include_images=False
        )

    return search_result 