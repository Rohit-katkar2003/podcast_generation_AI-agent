import numpy as np
import soundfile as sf

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