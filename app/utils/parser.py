import re 

def parse_script(script):
    pattern = r"\[(.*?)\]:\s*(.*?)(?=\n\[|$)"
    matches = re.findall(pattern, script, re.DOTALL)
    
    parsed = []
    for speaker_info, text in matches:
        name = speaker_info.split("(")[0].strip()
        gender = "female" if "WOMAN" in speaker_info else "male"
        parsed.append((name, gender, text.strip()))
    
    return parsed
