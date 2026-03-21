import re

def clean_text(text):
    text = text.replace("�", "")
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("‘", "'").replace("’", "'")
    text = re.sub(r"[^\w\s.,!?'\"]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

                                
