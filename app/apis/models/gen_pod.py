from pydantic import BaseModel


class gen_podcast(BaseModel): 
    topic : str 
    u_model_inp : str = "router_model"
