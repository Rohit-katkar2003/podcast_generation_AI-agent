from app.llms.gemini_model import initialize_LLM 
from app.llms.router_model import gen_response 
from app.llms.hf_model import hf_generate_response

def generate_response(u_model_inp, prompt, api_key=None, temperature=0.2, max_output_token=2048):

    if u_model_inp == "router_model":
        if not api_key:
            raise ValueError("OpenRouter API key required")
        return gen_response(prompt, api_key)

    elif u_model_inp == "gemini_model":
        if not api_key:
            raise ValueError("Gemini API key required")
        return initialize_LLM(prompt, temperature=temperature, max_output_token=max_output_token)

    elif u_model_inp == "hf_model":
        return hf_generate_response(prompt)

    else:
        raise ValueError("Invalid model selected")