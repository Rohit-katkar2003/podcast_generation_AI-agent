from langchain_google_genai import ChatGoogleGenerativeAI
import os 
# Initialize Gemini 2.0 Flash-Lite 
from dotenv import load_dotenv 
load_dotenv()

from app.utils.env import GEMINI_API_KEY

print(GEMINI_API_KEY)
def initialize_LLM(model_name = "gemini-2.0-flash-lite" , temperature=0.2 , max_output_token = 2048 ): 
    llm = ChatGoogleGenerativeAI(
        model=model_name,  # Confirm exact name via Google AI Studio
        temperature=temperature,
        max_output_tokens=max_output_token, 
        google_api_key =GEMINI_API_KEY
    )
    return llm['content'] 
