import os
import soundfile as sf
import tempfile

from app.utils.parser import parse_script
from app.utils.text_cleaner import clean_text
from app.utils.voice_manager import get_voice
from app.utils.audio_util import merge_wavs
from app.llms.kokoro_TTS import generate_response
from app.utils.bg_music_pod import add_background_music_auto

import uuid

OUTPUT_DIR = os.path.abspath("outputs") 
TEMP_DIR = os.path.abspath("TEMP") 
os.makedirs(TEMP_DIR , exist_ok=True)  
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_podcast(response, bg_audio_file):

    parsed = parse_script(response)

    temp_files = []

    for i, (name, gender, text) in enumerate(parsed):
        print("we currently on:", i)

        voice = get_voice(name, gender)
        text = clean_text(text)

        audio_data, _ = generate_response(text, voice=voice)

        if audio_data is None:
            continue

        sr, audio = audio_data

        filename = os.path.join(TEMP_DIR , f"temp_{uuid.uuid4().hex}_{i}.wav")
        sf.write(filename, audio, sr)

        temp_files.append(filename)

    # ✅ FINAL OUTPUT (persistent file)
    final_output = os.path.join(OUTPUT_DIR, f"podcast_{uuid.uuid4().hex}.wav")

    merge_wavs(temp_files, final_output)

    # Cleanup temp files manually
    for f in temp_files:
        if os.path.exists(f):
            os.remove(f)

    # 🎵 Background music
    if not bg_audio_file:
        print("without audio file ..... ")
        return final_output
    else:
        final_out_file = os.path.join(OUTPUT_DIR, f"podcast_bg_{uuid.uuid4().hex}.wav")

        add_background_music_auto(
            voice_file=final_output,
            music_file=bg_audio_file,
            output_file=final_out_file
        )

        if os.path.exists(final_out_file):
            os.remove(final_output)

        return final_out_file