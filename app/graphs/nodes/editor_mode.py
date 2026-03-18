from app.graphs.state import AgentState

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
    response = llm.invoke(prompt)
    return {"edited_script": response.content}