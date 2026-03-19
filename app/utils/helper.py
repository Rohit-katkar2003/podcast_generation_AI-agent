from app.llms.gemini_model import initialize_LLM 
from app.llms.router_model import gen_response 


def generate_response(u_model_inp ,  prompt , temperature=0.2 , max_output_token = 2048  ):
    if u_model_inp == "router_model": 
        return gen_response(prompt) 
    
    elif u_model_inp == "gemini_model": 
        return initialize_LLM(prompt , temperature=temperature , max_output_token=max_output_token) 
    