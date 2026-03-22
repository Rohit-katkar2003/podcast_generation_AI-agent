
from app.graphs.state import AgentState
from app.utils.helper import generate_response

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
    response = generate_response(u_model_inp=state['u_model_inp'] ,api_key=state.get('api_key') ,  prompt=prompt , temperature=0.3) 

    # print(response)
    return {"final_script": response}