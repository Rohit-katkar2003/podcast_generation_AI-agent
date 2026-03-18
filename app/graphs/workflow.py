from langgraph.graph import StateGraph , END , START
from app.graphs.state import AgentState 
from app.graphs.nodes.editor_mode import  editor_node 
from app.graphs.nodes.formater_node import formatter_node 
from app.graphs.nodes.research import research_node 
from app.graphs.nodes.scriptwriter import scriptwriter_node 



# Initialize graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("researcher", research_node)
workflow.add_node("scriptwriter", scriptwriter_node)
workflow.add_node("editor", editor_node)
workflow.add_node("formatter", formatter_node)

# Define edges
workflow.add_edge(START, "researcher")
workflow.add_edge("researcher", "scriptwriter")
workflow.add_edge("scriptwriter", "editor")
workflow.add_edge("editor", "formatter")
workflow.add_edge("formatter", END)

# Compile
app = workflow.compile() 

# display(Image(app.get_graph().draw_mermaid_png()))