from typing import TypedDict, Annotated
import operator

class AgentState(TypedDict, total=False): 
    topic: str
    
    research_notes: Annotated[str, operator.add]   # ✅ FIXED NAME
    raw_script: Annotated[str, operator.add] 
    edited_script: Annotated[str, operator.add] 
    final_script: Annotated[str, operator.add] 

    u_model_inp: str 
    api_key : str
