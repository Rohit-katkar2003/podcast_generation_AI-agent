from app.apis.routes import  router 
from fastapi import FastAPI 
import uvicorn 

app = FastAPI() 

app.include_router(router=router , 
                   prefix="/api/v1") 




if __name__ == "__main__": 
    uvicorn.run(app=app  , port=1111)

