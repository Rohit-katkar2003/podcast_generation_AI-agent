import soundfile as sf
import numpy as np
import librosa 
import os  

def add_background_music_wav(
    voice_file,
    music_file,
    output_file="final_with_music.wav",
    music_volume=0.1
):
    voice, sr_voice = sf.read(voice_file)

    music, sr_music = sf.read(music_file)

    if voice.ndim != music.ndim:
        if music.ndim == 1:
            music = np.expand_dims(music, axis=1)
        if voice.ndim == 1:
            voice = np.expand_dims(voice, axis=1)

    if sr_music != sr_voice:
        raise ValueError("Sample rates must match for WAV")

    if len(music) < len(voice):
        repeat = len(voice) // len(music) + 1
        music = np.tile(music, (repeat, 1)) if music.ndim > 1 else np.tile(music, repeat)

    music = music[:len(voice)]

    music = music * music_volume

    mixed = voice + music

    mixed = np.clip(mixed, -1.0, 1.0)

    sf.write(output_file, mixed, sr_voice)

    return output_file 


def add_background_music_mp3(
    voice_file,
    music_file,
    output_file="final_with_music.wav",
    music_volume=0.1
):
    voice, sr_voice = sf.read(voice_file)

    music, sr_music = librosa.load(music_file, sr=None)

    if sr_music != sr_voice:
        music = librosa.resample(music, orig_sr=sr_music, target_sr=sr_voice)

    if voice.ndim > 1 and music.ndim == 1:
        music = np.tile(music[:, None], (1, voice.shape[1]))

    if len(music) < len(voice):
        repeat = len(voice) // len(music) + 1
        music = np.tile(music, (repeat, 1)) if music.ndim > 1 else np.tile(music, repeat)

    music = music[:len(voice)]

    music = music * music_volume

    mixed = voice + music

    mixed = np.clip(mixed, -1.0, 1.0)

    sf.write(output_file, mixed, sr_voice)

    return output_file



def add_background_music_auto(voice_file, music_file, output_file="final_with_music.wav"):
    ext = os.path.splitext(music_file)[1].lower()

    if ext == ".wav":
        return add_background_music_wav(voice_file, music_file, output_file)
    elif ext == ".mp3":
        return add_background_music_mp3(voice_file, music_file, output_file)
    else:
        raise ValueError("Unsupported format. Use .wav or .mp3") 
    
    