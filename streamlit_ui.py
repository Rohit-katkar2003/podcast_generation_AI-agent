import streamlit as st
import os
import tempfile

st.set_page_config(page_title="AI Podcast Generator", page_icon="🎙️", layout="wide")

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Page background */
.stApp {
    background: #080b12;
}

/* Hide default streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 2rem 3rem !important; max-width: 100% !important; }

/* ── Hero header ── */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 2rem;
    margin-bottom: 2rem;
}
.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: 3.5rem;
    font-weight: 800;
    letter-spacing: -1px;
    background: linear-gradient(135deg, #e2e8f0 0%, #a78bfa 50%, #38bdf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 0 0.5rem;
    line-height: 1.1;
}
.hero p {
    color: #64748b;
    font-size: 1.2rem;
    font-weight: 300;
    margin: 0;
    letter-spacing: 0.5px;
}

/* ── Cards ── */
.panel {
    background: #0f1420;
    border: 1px solid rgba(148,130,255,0.15);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

/* ── Section labels ── */
.label {
    font-family: 'Syne', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 0.6rem;
    display: block;
}

/* ── Inputs ── */
.stTextArea textarea {
    background: #151929 !important;
    border: 1px solid rgba(148,130,255,0.2) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1.05rem !important;
    resize: none !important;
}
.stTextArea textarea:focus {
    border-color: #7c6ff7 !important;
    box-shadow: 0 0 0 3px rgba(124,111,247,0.2) !important;
}

/* ── Radio pills ── */
.stRadio > div { gap: 10px !important; flex-direction: row !important; }
.stRadio label {
    background: #151929 !important;
    border: 1px solid rgba(148,130,255,0.2) !important;
    border-radius: 50px !important;
    padding: 6px 20px !important;
    color: #64748b !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    cursor: pointer;
    transition: all 0.2s !important;
}
.stRadio label:has(input:checked) {
    background: #7c6ff7 !important;
    border-color: #7c6ff7 !important;
    color: #fff !important;
}

/* ── File uploader ── */
.stFileUploader > div {
    background: #151929 !important;
    border: 2px dashed rgba(148,130,255,0.25) !important;
    border-radius: 12px !important;
}

/* ── Generate button ── */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #7c6ff7, #a78bfa) !important;
    border: none !important;
    border-radius: 50px !important;
    color: #fff !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    padding: 0.65rem 2rem !important;
    letter-spacing: 0.5px;
    box-shadow: 0 4px 20px rgba(124,111,247,0.35) !important;
    transition: all 0.2s !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(124,111,247,0.5) !important;
}

/* ── Clear button ── */
.stButton > button[kind="secondary"] {
    background: #151929 !important;
    border: 1px solid rgba(148,130,255,0.2) !important;
    border-radius: 50px !important;
    color: #64748b !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
}
.stButton > button[kind="secondary"]:hover {
    border-color: #ef4444 !important;
    color: #ef4444 !important;
}

/* ── Status ── */
.stTextInput input, .stTextInput textarea {
    background: #151929 !important;
    border-color: rgba(148,130,255,0.2) !important;
    color: #e2e8f0 !important;
}

/* ── Example cards ── */
.example-grid {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 0.5rem;
}
.example-card {
    background: #151929;
    border: 1px solid rgba(148,130,255,0.2);
    border-radius: 12px;
    padding: 10px 14px;
    cursor: pointer;
    flex: 1;
    min-width: 200px;
    transition: all 0.2s;
}
.example-card:hover {
    border-color: #7c6ff7;
    background: rgba(124,111,247,0.08);
}
.example-card .ex-num {
    font-size: 0.81rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #7c6ff7;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.example-card .ex-topic {
    font-size: 0.99rem;
    color: #cbd5e1;
    font-weight: 400;
    line-height: 1.3;
}

/* ── Output panel ── */
.output-panel {
    background: #0f1420;
    border: 1px solid rgba(148,130,255,0.15);
    border-radius: 16px;
    padding: 1.5rem;
    min-height: 300px;
}
.output-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 1rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid rgba(148,130,255,0.12);
}

/* ── Success / error alert ── */
.stSuccess, .stError {
    border-radius: 10px !important;
}

/* ── Audio player ── */
.stAudio audio {
    width: 100% !important;
    border-radius: 10px !important;
}

/* ── Spinner ── */
.stSpinner > div { border-top-color: #7c6ff7 !important; }

/* ── Divider ── */
hr { border-color: rgba(148,130,255,0.1) !important; }
</style>
""", unsafe_allow_html=True)


@st.cache_resource(show_spinner="🧠 Loading AI models... please wait")
def load_models():
    from app.utils.config import APP
    from app.tool.podcast_generator import generate_podcast
    return APP, generate_podcast


EXAMPLES = [
    {
        "num": "01",
        "topic": "What is Transformers in NLP",
        "audio": os.path.abspath("outputs/podcast_bg_72543443ab3f496fa28bebcdb1dd1a54.wav"),
    },
    {
        "num": "02",
        "topic": "How to read AI/ML research papers",
        "audio": os.path.abspath("outputs/podcast_bg_b9091426fcc94eab9fa6a8ca1a9fd1c9.wav"),
    },
    {
        "num": "03",
        "topic": "What is ML and its types",
        "audio": os.path.abspath("outputs/podcast_cb6e9894df334be289ad17a2ad3f92c9.wav"),
    },
]

DEFAULT_AUDIO = "assets/bg_music/bg_music.mp3"


def run_ui():
    APP, generate_podcast = load_models()

    # ── Session state ──
    if "status_msg" not in st.session_state:
        st.session_state.status_msg = None
    if "audio_bytes" not in st.session_state:
        st.session_state.audio_bytes = None
    if "topic_val" not in st.session_state:
        st.session_state.topic_val = ""

    # ── Hero ──
    st.markdown("""
    <div class="hero">
      <h1>🎙 AI Podcast Generator</h1>
      <p>Transform any topic into a fully voiced, AI-generated podcast</p>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1, 1], gap="large")

    # ══════════════ LEFT PANEL ══════════════
    with left:

        # Topic input
        st.markdown('<span class="label">📌 Podcast Topic</span>', unsafe_allow_html=True)
        topic = st.text_area(
            "topic_input",
            value=st.session_state.topic_val,
            placeholder="e.g. How does attention mechanism work in transformers?",
            height=110,
            label_visibility="collapsed",
            key="topic_textarea"
        )

        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

        # Model selector
        st.markdown('<span class="label">🤖 Model</span>', unsafe_allow_html=True)
        model_options = ["hf_model","router_model", "gemini_model"]
        model_choice = st.radio(
            "model_radio",
            options=model_options,
            index=0,
            horizontal=True,
            label_visibility="collapsed"
        )

        api_key = None

        if model_choice == "router_model":
            api_key = st.text_input(
                "🔑 Enter OpenRouter API Key",
                type="password",
                placeholder="sk-xxxx..."
            )

        elif model_choice == "gemini_model":
            api_key = st.text_input(
                "🔑 Enter Gemini API Key",
                type="password",
                placeholder="AIza..."
            )

        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

        # Upload music
        st.markdown('<span class="label">🎵 Background Music <span style="color:#475569;font-weight:300;text-transform:none;letter-spacing:0;font-size:0.75rem">(optional)</span></span>', unsafe_allow_html=True)
        audio_file = st.file_uploader(
            "bg_music",
            type=["mp3", "wav"],
            label_visibility="collapsed"
        )

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

        # Buttons
        col_gen, col_clr = st.columns([3, 2])
        with col_gen:
            generate_btn = st.button("🚀 Generate Podcast", type="primary", use_container_width=True)
        with col_clr:
            clear_btn = st.button("✕ Clear", type="secondary", use_container_width=True)

        # ── Examples section ──
        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
        st.markdown('<span class="label">⚡ Try an example</span>', unsafe_allow_html=True)
        st.markdown('<p style="color:#475569;font-size:0.78rem;margin:0 0 8px">Click to instantly load a pre-generated podcast</p>', unsafe_allow_html=True)

        for ex in EXAMPLES:
            col_info, col_btn = st.columns([4, 1])
            with col_info:
                st.markdown(f"""
                <div style="background:#151929;border:1px solid rgba(148,130,255,0.18);
                            border-radius:10px;padding:10px 14px;margin-bottom:6px">
                  <div style="font-size:0.62rem;font-weight:700;letter-spacing:1.5px;
                              color:#7c6ff7;text-transform:uppercase;margin-bottom:3px">
                    Example {ex['num']}
                  </div>
                  <div style="font-size:0.83rem;color:#cbd5e1;line-height:1.3">
                    {ex['topic']}
                  </div>
                </div>
                """, unsafe_allow_html=True)
            with col_btn:
                st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
                if st.button("▶ Play", key=f"ex_{ex['num']}"):
                    if os.path.exists(ex["audio"]):
                        with open(ex["audio"], "rb") as f:
                            st.session_state.audio_bytes = f.read()
                        st.session_state.status_msg = ("success", f"✅ Example: {ex['topic']}")
                        st.session_state.topic_val = ex["topic"]
                        st.rerun()
                    else:
                        st.warning(f"Example audio not found at: {ex['audio']}")

    # ══════════════ RIGHT PANEL ══════════════
    with right:
        st.markdown('<span class="label">📢 Status</span>', unsafe_allow_html=True)
        status_placeholder = st.empty()

        if st.session_state.status_msg:
            kind, msg = st.session_state.status_msg
            if kind == "success":
                status_placeholder.success(msg)
            else:
                status_placeholder.error(msg)

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        st.markdown('<span class="label">🎧 Generated Podcast</span>', unsafe_allow_html=True)
        audio_placeholder = st.empty()

        if st.session_state.audio_bytes:
            audio_placeholder.audio(st.session_state.audio_bytes, format="audio/wav", autoplay=True)
        else:
            st.markdown("""
            <div style="background:#0a0d16;border:1px dashed rgba(148,130,255,0.15);
                        border-radius:12px;padding:3rem 2rem;text-align:center;margin-top:4px">
              <div style="font-size:2rem;margin-bottom:0.5rem">🎙</div>
              <div style="color:#334155;font-size:0.85rem">
                Your podcast will appear here
              </div>
            </div>
            """, unsafe_allow_html=True)

    # ══════════════ ACTIONS ══════════════
    if clear_btn:
        st.session_state.status_msg = None
        st.session_state.audio_bytes = None
        st.session_state.topic_val = ""
        st.rerun()

    if generate_btn:
        topic_val = topic.strip()
        if not topic_val:
            st.session_state.status_msg = ("error", "❌ Please enter a topic")
            st.rerun()
        else:
            with st.spinner("🎙️ Generating your podcast... this takes 5–6 minutes"):
                try:
                    if audio_file is None:
                        bg_audio = DEFAULT_AUDIO if os.path.exists(DEFAULT_AUDIO) else None
                    else:
                        temp_path = tempfile.mktemp(suffix=".mp3")
                        with open(temp_path, "wb") as f:
                            f.write(audio_file.read())
                        bg_audio = temp_path

                    result = APP.invoke({
                        "topic": topic_val,
                        "u_model_inp": model_choice , 
                        "api_key" : api_key
                    })

                    if not result or "final_script" not in result:
                        st.session_state.status_msg = ("error", "❌ Script generation failed")
                        st.rerun()

                    audio_path = generate_podcast(
                        response=result["final_script"],
                        bg_audio_file=bg_audio
                    )
                    audio_path = os.path.abspath(audio_path)

                    if not audio_path or not os.path.exists(audio_path):
                        st.session_state.status_msg = ("error", "❌ Audio file was not created")
                        st.rerun()

                    print(f"[UI] Audio ready: {audio_path} | size: {os.path.getsize(audio_path)} bytes")

                    with open(audio_path, "rb") as f:
                        st.session_state.audio_bytes = f.read()
                    st.session_state.status_msg = ("success", "✅ Podcast Generated!")
                    st.rerun()

                except Exception as e:
                    import traceback
                    full_error = traceback.format_exc()
                    print(f"[ERROR] Full traceback:\n{full_error}")
                    st.session_state.status_msg = ("error", f"❌ Error: {str(e)}")
                    st.rerun()


run_ui()