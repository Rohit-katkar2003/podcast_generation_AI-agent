from fastapi import FastAPI , APIRouter , HTTPException , status
from app.utils.config import APP 
from app.apis.models.gen_pod import gen_podcast
from fastapi.responses import JSONResponse 
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
    
    try : 
        if pod_topic is not None :  
            topic = pod_topic.strip()
            result = APP.invoke({
            "topic": topic ,
            "u_model_inp": pod_u_model 
        })  
        else: 
            return JSONResponse(content="please give the topic" ,  status_code=status.HTTP_204_NO_CONTENT) 

        if result: 
            print(f"😁😁 we got the result of type {type(result)}....... \n\n {result['final_script']}") 
             
            res = generate_podcast(response=result["final_script"]) 

            return {"status":"success" , "message" : f"the podcast at  🤥 {res}"}


    except Exception as e: 
        raise f"Got error : {e}"