# # from app.utils.config import LLM 
# from app.utils.config import APP 


# response = APP.invoke({
#     "topic": "podcast between Rohit and Priya how to take call of IT job",
#     "u_model_inp": "router_model"
# })

# print(response) 
# print(response.keys())  

# with open("script.txt" , "w") as f: 
#     f.write(response["final_script"]) 

############################# TTS test ###################################### 
from kokoro import KModel, KPipeline
import gradio as gr
import torch
import os 
import re
import soundfile as sf
import random
import warnings 
warnings.filterwarnings("ignore")
print("everything loaded success fully ")
# ---------------------------
# SETUP
# ---------------------------
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

## Voices 
CHOICES = {
    '🇺🇸 🚺 Heart ❤️':    'af_heart',
    '🇺🇸 🚺 Bella 🔥':    'af_bella',
    '🇺🇸 🚺 Nicole 🎧':   'af_nicole',
    '🇺🇸 🚺 Aoede':        'af_aoede',
    '🇺🇸 🚺 Kore':         'af_kore',
    '🇺🇸 🚺 Sarah':        'af_sarah',
    '🇺🇸 🚺 Nova':         'af_nova',
    '🇺🇸 🚺 Sky':          'af_sky',
    '🇺🇸 🚺 Alloy':        'af_alloy',
    '🇺🇸 🚺 Jessica':      'af_jessica',
    '🇺🇸 🚺 River':        'af_river',
    '🇺🇸 🚹 Michael':      'am_michael',
    '🇺🇸 🚹 Fenrir':       'am_fenrir',
    '🇺🇸 🚹 Puck':         'am_puck',
    '🇺🇸 🚹 Echo':         'am_echo',
    '🇺🇸 🚹 Eric':         'am_eric',
    '🇺🇸 🚹 Liam':         'am_liam',
    '🇺🇸 🚹 Onyx':         'am_onyx',
    '🇺🇸 🚹 Santa':        'am_santa',
    '🇺🇸 🚹 Adam':         'am_adam',
    '🇬🇧 🚺 Emma':         'bf_emma',
    '🇬🇧 🚺 Isabella':     'bf_isabella',
    '🇬🇧 🚺 Alice':        'bf_alice',
    '🇬🇧 🚺 Lily':         'bf_lily',
    '🇬🇧 🚹 George':       'bm_george',
    '🇬🇧 🚹 Fable':        'bm_fable',
    '🇬🇧 🚹 Lewis':        'bm_lewis',
    '🇬🇧 🚹 Daniel':       'bm_daniel',
}


## load all voice to memory 
for v in CHOICES.values(): 
    pipelines[v[0]].load_voice(v) 


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
                raise gr.Error(str(e))
        return (24000, audio.numpy()), ps
    return None , "" 

def tokenize_first(text, voice='af_heart'):
    pipeline = pipelines[voice[0]]
    for _, ps, _ in pipeline(text, voice):
        return ps
    return '' 

print("Generating ................. !")
# generate_response("hello my self rohit")
male_voices = [v for k, v in CHOICES.items() if "🚹" in k]
female_voices = [v for k, v in CHOICES.items() if "🚺" in k]
print("Male Voice : " , male_voices)
print("female Voice : " , female_voices)

def parse_script(script):
    pattern = r"\[(.*?)\]:\s*(.*?)(?=\n\[|$)"
    matches = re.findall(pattern, script, re.DOTALL)
    
    parsed = []
    for speaker_info, text in matches:
        name = speaker_info.split("(")[0].strip()
        gender = "female" if "WOMAN" in speaker_info else "male"
        parsed.append((name, gender, text.strip()))
    
    return parsed



speaker_voice_map = {}

def get_voice(name, gender):
    if name in speaker_voice_map:
        return speaker_voice_map[name]
    
    if gender == "male":
        voice = random.choice(male_voices)
    else:
        voice = random.choice(female_voices)
    
    speaker_voice_map[name] = voice
    return voice

import re

def clean_text(text):
    # 1. Fix encoding issues (remove �)
    text = text.replace("�", "")

    # 2. Remove markdown asterisks (*bold*, *italic*)
    text = re.sub(r"\*(.*?)\*", r"\1", text)

    # 3. Replace fancy quotes with normal ones
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("‘", "'").replace("’", "'")

    # 4. Remove extra symbols but keep punctuation
    text = re.sub(r"[^\w\s.,!?'\"]+", " ", text)

    # 5. Fix multiple spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

def generate_chunks(parsed_data, output_dir="chunks"):
    os.makedirs(output_dir, exist_ok=True)
    audio_files = []

    for i, (name, gender, text) in enumerate(parsed_data):
        voice = get_voice(name, gender)

        text = clean_text(text) 
        
        audio_data, _ = generate_response(text, voice=voice)

        if audio_data is None:
            continue

        sr, audio = audio_data
        filename = f"{output_dir}/{i}_{name}.wav"
        
        sf.write(filename, audio, sr)
        audio_files.append(filename)

    return audio_files 

import numpy as np

def merge_wavs(wav_files, output="final_podcast.wav"):
    final_audio = []
    sr = None

    for file in wav_files:
        audio, samplerate = sf.read(file)

        if sr is None:
            sr = samplerate

        final_audio.append(audio)

    merged_audio = np.concatenate(final_audio)
    sf.write(output, merged_audio, sr)

    return output 


with open("script.txt" , "r") as f: 
    script = f.read()

parsed = parse_script(script)

chunk_files = generate_chunks(parsed)

final_file = merge_wavs(chunk_files)

print("Final podcast saved:", final_file)