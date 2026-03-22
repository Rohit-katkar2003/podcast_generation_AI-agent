from fastapi import FastAPI , APIRouter , HTTPException , status
from app.utils.config import APP 
import os
import json
import asyncio
from app.apis.models.gen_pod import gen_podcast
from fastapi.responses import JSONResponse  , StreamingResponse
from app.tool.podcast_generator import generate_podcast
router = APIRouter()

@router.get("/")
def test(): 
    return {"status":"success" , "message":"everything fine .... "} 


@router.post("/gen_podcast")
async def gen_podcast(pod:gen_podcast): 
    pod_topic = pod.topic 
    pod_u_model= pod.u_model_inp 
    background_music = pod.audio_file 
    api_key = pod.api_key 

    try : 
        if  not pod_topic and pod_topic.strip() :  

            return JSONResponse(
                content={"error": "please give the topic"},
                status_code=status.HTTP_400_BAD_REQUEST
            ) 
              
        topic = pod_topic.strip() 
        if pod_u_model in ["router_model" , "gemini_model"]:  
            return f"give the API key for {pod_u_model} then only u can use "
        
        result = APP.invoke({
            "topic": topic ,
            "u_model_inp": pod_u_model  , 
            "api_key" : None
        })  
        
        if not result or "final_script" not in result:
            raise HTTPException(
                status_code=500,
                detail="Failed to generate script"
            )
         

        print(f"😁😁 we got the result of type {type(result)}....... \n\nNow generating audio. ") 
            
        res = generate_podcast(response=result["final_script"] , bg_audio_file=background_music) 
        print("FINAL OUTPUT:", res)
        print("EXISTS:", os.path.exists(res))
        print("SIZE:", os.path.getsize(res))
        
        return {"status":"success" , "message" :res}


    except HTTPException as e:
        raise e
    
    except Exception as e: 
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error: {str(e)}"
        )
    