from app.graphs.state import AgentState
from app.utils.helper import generate_response


def editor_node(state: AgentState):
    prompt = f"""
    You are a senior podcast editor.
    Improve this script for pacing, clarity, and engagement:
    {state['raw_script']}

    - Trim fluff
    - Add humor or emotional hooks
    - Ensure smooth transitions
    - Fix awkward phrasing

    Output the improved version only.
    """
    response = generate_response(u_model_inp=state['u_model_inp'] ,api_key=state.get('api_key') ,  prompt=prompt , temperature=0.2)
    return {"edited_script": response}