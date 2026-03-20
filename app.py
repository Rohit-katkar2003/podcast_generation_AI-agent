import gradio as gr
from app.utils.config import APP
from app.tool.podcast_generator import generate_podcast

def generate(topic, model_choice, bg_audio):
    if not topic.strip():
        return None, "⚠️ Please enter a topic."
    result = APP.invoke({"topic": topic.strip(), "u_model_inp": model_choice})
    if not result or "final_script" not in result:
        return None, "❌ Script generation failed."
    audio_path = generate_podcast(response=result["final_script"], bg_audio_file=bg_audio)
    return audio_path, "✅ Podcast ready!"

with gr.Blocks(title="AI Podcast Generator") as demo:
    gr.Markdown("# 🎙️ AI Podcast Generator")
    with gr.Row():
        topic = gr.Textbox(label="Topic", placeholder="e.g. Future of Quantum Computing")
        model = gr.Radio(["gemini_model", "router_model"], label="Model", value="gemini_model")
    music = gr.Audio(label="Background Music (optional)", type="filepath")
    btn = gr.Button("Generate Podcast 🚀", variant="primary")
    output_audio = gr.Audio(label="Your Podcast")
    status = gr.Textbox(label="Status")
    btn.click(generate, inputs=[topic, model, music], outputs=[output_audio, status])

demo.launch()