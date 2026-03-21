
from app.graphs.state import AgentState 
from app.utils.helper import generate_response 

def scriptwriter_node(state: AgentState): 

    # print("STATE IN SCRIPTWRITER:", state)

    prompt = f"""
    You are a professional podcast scriptwriter.
    Using these research notes:
    {state['research_notes']}

    Write a full podcast script including:
    - Host introduction
    - 2-3 engaging segments with natural dialogue
    - Guest quotes (if applicable)
    - Transitions
    - Call-to-action and outro

    Format with speaker labels like:
    [HOST]: ...
    [GUEST]: ...

    Keep tone conversational and energetic.
    """
    response =  generate_response(u_model_inp=state['u_model_inp'] , prompt=prompt)  
    return {"raw_script": response}