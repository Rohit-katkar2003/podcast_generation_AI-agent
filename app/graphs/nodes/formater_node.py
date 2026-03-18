
from app.graphs.state import AgentState


def formatter_node(state: AgentState):
    prompt = f"""
    You are a podcast producer for an Indian audience. Format this script for recording:
    {state['edited_script']}

    STRICT REQUIREMENTS:
    - REMOVE ALL [MUSIC: ...] and [SFX: ...] CUES. DO NOT INCLUDE ANY BACKGROUND MUSIC OR SOUND EFFECTS.
    - Assign RANDOM, REALISTIC INDIAN NAMES to each speaker type. Use culturally diverse names from across India (Hindi, Tamil, Bengali, Marathi, Punjabi, Telugu, Malayalam, etc.).
    - Add NATURAL CALL-OUTS in dialogue to make it feel conversational and warm — e.g., "Arjun Bhaiya", "Priya Didi", "Uncle ji", "Aunty", "Boss", "Sarpanch ji", "Guruji", etc. — as contextually appropriate.
    - Format with speaker labels like:
        [Rohit (HOST-MAN)]: ...
        [Priya (COHOST-WOMAN)]: ...
        [Ramesh Uncle (EXPERT-MAN)]: ...
        [Ananya Didi (GUEST-WOMAN)]: ...
        [Chintu (KID-BOY)]: ...
      → Use different names each time. Do NOT use generic labels like "[HOST]" or "[GUEST]".
    - Keep tone conversational, friendly, and energetic — like a chai-time chat with friends.
    - Maintain natural conversational flow. Do NOT add stage directions or technical notes.
    - don't add the '*' or '**' symbol in the script.
    Output ONLY the clean, production-ready script — nothing else.
    """
    response = llm.invoke(prompt)
    return {"final_script": response.content}