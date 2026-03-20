from kokoro import KModel, KPipeline
import torch

import warnings 
warnings.filterwarnings("ignore")
print("everything loaded success fully ")

CUDA_AVAILABLE = torch.cuda.is_available()

models = {
    False : KModel().to("cpu").eval()
}

if CUDA_AVAILABLE: 
    models[True] = KModel().to("cuda").eval() 

pipelines = {
    lang_code: KPipeline(lang_code=lang_code, model=False)
    for lang_code in 'ab'
}


pipelines["a"].g2p.lexicon.golds['kokoro'] = 'kˈQkəɹQ' 
pipelines["b"].g2p.lexicon.golds['kokoro'] = 'kˈQkəɹQ' 


def generate_response(text , voice="af_heart" , speed = 1.0 , use_gpu=False): 
    text = text.strip() 

    if not text: 
        return None , '' 
    
    pipeline = pipelines[voice[0]] 
    pack = pipeline.load_voice(voice) 


    for _, ps, _ in pipeline(text, voice, speed): 
        ref_s = pack[len(ps)-1] 
        try: 
            if use_gpu: 
                audio = models[True](ps , ref_s , speed) 
            else: 
                audio = models[False](ps , ref_s , speed) 
        except Exception as e: 
            if use_gpu:
                audio = models[False](ps, ref_s, speed)
            else:
                raise f"Got error : {e}"
        return (24000, audio.numpy()), ps
    return None , "" 

