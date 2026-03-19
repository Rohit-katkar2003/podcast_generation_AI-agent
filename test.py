# from app.utils.config import LLM 
from app.utils.config import APP 


response = APP.invoke({
    "topic": "podcast between Rohit and Priya how to take call of IT job",
    "u_model_inp": "router_model"
})

print(response) 
print(response.keys())  

with open("script.txt" , "w") as f: 
    f.write(response["final_script"]) 

