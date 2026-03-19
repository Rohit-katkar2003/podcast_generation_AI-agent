## adding music to podcast
import librosa
import soundfile as sf
import numpy as np

def add_background_music_mp3(
    voice_file,
    music_file,
    output_file="final_with_music.wav",
    music_volume=0.1
):
    # 🎙 Load voice (WAV)
    voice, sr_voice = sf.read(voice_file)

    # 🎵 Load MP3 music
    music, sr_music = librosa.load(music_file, sr=None)

    # ⚠️ Resample if needed
    if sr_music != sr_voice:
        music = librosa.resample(music, orig_sr=sr_music, target_sr=sr_voice)

    # 🔁 Loop music
    if len(music) < len(voice):
        repeat = len(voice) // len(music) + 1
        music = np.tile(music, repeat)

    # ✂ Trim
    music = music[:len(voice)]

    # 🔉 Volume control
    music = music * music_volume

    # 🎙 Mix
    mixed = voice + music

    # ⚠️ Clip
    mixed = np.clip(mixed, -1.0, 1.0)

    # 💾 Save
    sf.write(output_file, mixed, sr_voice)

    return output_file 

final_with_music = add_background_music_mp3(
    voice_file="final_podcast.wav",
    music_file="bg_music.mp3"
)

print("Done:", final_with_music)