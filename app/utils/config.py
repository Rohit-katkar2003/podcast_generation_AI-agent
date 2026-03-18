from app.llms.gemini_model import initialize_LLM 
from app.llms.router_model import gen_response 
import os 
from tavily import TavilyClient
from dotenv import load_dotenv 
load_dotenv() 

GEMINI_API_KEY     = os.environ['GEMINI_API_KEY'] 
OPENROUTER_API_KEY = os.environ['OPENROUTER_API_KEY'] 
TRAVILY_API_KEY    = os.environ['TRAVILY_API_KEY']


TRAVILY_CLIENT = TavilyClient(api_key=TRAVILY_API_KEY)  

MODEL_USE = {"router_api" : 1 , "gemini_model":2}

def generate_response(u_model_inp ,  prompt , temperature=0.2 , max_output_token = 2048  ):
    if MODEL_USE[u_model_inp] == 1: 
        return  gen_response(prompt) 
    
    elif MODEL_USE[u_model_inp] == 2: 
        return 

