import random

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

male_voices = [v for k, v in CHOICES.items() if "🚹" in k]
female_voices = [v for k, v in CHOICES.items() if "🚺" in k]

speaker_voice_map = {}

def get_voice(name, gender):
    if name in speaker_voice_map:
        return speaker_voice_map[name]

    voice = random.choice(male_voices if gender == "male" else female_voices)
    speaker_voice_map[name] = voice
    return voice