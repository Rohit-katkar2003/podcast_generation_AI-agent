import requests
import json
import os 
from app.utils.env import OPENROUTER_API_KEY

# First API call with reasoning
def gen_response(prompt):  
    print("✅ Router model used .... !") 

    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "nvidia/nemotron-3-super-120b-a12b:free",
        "messages": [
            {
            "role": "user",
            "content": prompt
            }
        ],
        "reasoning": {"enabled": False}
    })
    )

    # Extract the assistant message with reasoning_details
    response = response.json() 
    print(response)
    response = response['choices'][0]['message']

    return response['content']
