# # from app.utils.config import LLM 
# from app.utils.config import APP 


# response = APP.invoke({
#     "topic": "podcast between Rohit and Priya how to take call of IT job",
#     "u_model_inp": "router_model"
# })

# print(response) 
# print(response.keys())  

# with open("script.txt" , "w") as f: 
#     f.write(response["final_script"]) 

############################# TTS test ###################################### 
from app.tool.podcast_generator import generate_podcast

if __name__ == "__main__":
    final_file = generate_podcast("script.txt")
    print("Final podcast saved:", final_file) 
    