import os
import soundfile as sf
import tempfile

from app.utils.parser import parse_script
from app.utils.text_cleaner import clean_text
from app.utils.voice_manager import get_voice
from app.utils.audio_util import merge_wavs
from app.llms.kokoro_TTS import generate_response


def generate_podcast(script_path):
    with open(script_path, "r") as f:
        script = f.read()

    parsed = parse_script(script)

    with tempfile.TemporaryDirectory() as temp_dir:
        audio_files = []


        for i, (name, gender, text) in enumerate(parsed):
            print("we currently on : " , i) 
            print("lenght : " , len(parsed))
            voice = get_voice(name, gender)
            text = clean_text(text)

            audio_data, _ = generate_response(text, voice=voice)

            if audio_data is None:
                continue

            sr, audio = audio_data

            filename = os.path.join(temp_dir, f"{i}_{name}.wav")
            sf.write(filename, audio, sr)

            audio_files.append(filename)

        final_output = "final_podcast.wav"
        merge_wavs(audio_files, final_output)

    return final_output