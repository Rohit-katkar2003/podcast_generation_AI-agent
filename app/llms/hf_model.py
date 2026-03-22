import requests 
import os 
import time  
from app.utils.env import BASE_URL 

def hf_generate_response(prompt): 
    print("i am used...")
    payload = {
    "prompt": prompt[:3900],
    "model_size": "1b",
    "max_tokens": 1024,
    "temperature": 0.2
    }

    start_time = time.time()
    res = requests.post(url=BASE_URL , 
                        json=payload) 

    response = res.json() 
    print(response)
    end_time = time.time()
    print(end_time-start_time) 
    
    if res.status_code != 200:
        print("API ERROR:", response)
        return None
    
    return response['result']