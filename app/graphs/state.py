from typing import TypedDict , Annotated 
from langgraph.graph import StateGraph  

class AgentState(TypedDict): 
    topic : str 
    research_nodes : str 
    raw_script : str 
    edited_script : str 
    final_script : str 
    audio_files : list[str] 

