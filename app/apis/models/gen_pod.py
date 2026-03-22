from pydantic import BaseModel


class gen_podcast(BaseModel): 
    topic : str 
    u_model_inp : str = "hf_model"
    audio_file : str = "assets/bg_music/bg_music.mp3"   
    api_key : str = None