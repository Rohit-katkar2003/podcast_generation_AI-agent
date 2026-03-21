import requests 
import os 
import time  

BASE_URL = "https://rohit-katkar2003-llama-q8.hf.space/generate" 


def hf_generate_response(prompt): 
    print("i am used...")
    payload = {
    "prompt": prompt,
    "model_size": "1b",
    "max_tokens": 4096,
    "temperature": 0.2
    }

    start_time = time.time()
    res = requests.post(url=BASE_URL , 
                        json=payload) 

    response = res.json() 
    print(response)
    end_time = time.time()
    print(end_time-start_time) 
    
    return response['result']