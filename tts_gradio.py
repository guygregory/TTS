import gradio as gr
from openai import AzureOpenAI
from dotenv import load_dotenv
import os
import tempfile
import time

# Load environment variables
load_dotenv()

# Set up Azure OpenAI client
client = AzureOpenAI(
    api_key = os.environ["AZURE_OPENAI_API_KEY"],  
    api_version = os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint = os.environ["AZURE_OPENAI_API_ENDPOINT"]
    )

VOICE_LIST = [
    "alloy", "ash", "ballad", "coral", "echo",
    "fable", "onyx", "nova", "sage", "shimmer"
]

def tts_play(instructions, input_text, voice):
    # Call AzureOpenAI text-to-speech and save to temp wav file
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice=voice,
        input=input_text,
        instructions=instructions,
        response_format="wav",
    )
    # Write response to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(response.content)
        temp_filename = temp_audio.name
    time.sleep(0.5)  # Wait for file flush
    return temp_filename

with gr.Blocks() as demo:
    gr.Markdown("# 🎤 Azure OpenAI gpt-4o-mini-tts Text to Speech Demo")
    gr.Markdown("### Fill out delivery **Instructions** (left), the **Input** text (right), and pick a **Voice**. Then click **Play**!")
    with gr.Row():
        instructions_box = gr.Textbox(
            label="Instructions",
            value="Voice: Confident, resonant, and vibrant—commanding attention and generating excitement.\n\nTone: Energetic, optimistic, and authoritative, creating anticipation and highlighting the significance of announcements.\n\nDelivery: Clear and dynamic, with strategic pauses to emphasise key moments and build suspense before major reveals.\n\nEmotion: Enthusiastic, celebratory, and inclusive, making attendees feel they are part of a ground-breaking moment.\n\nPunctuation: Crisp, impactful phrases, using exclamation points and well-timed pauses to heighten engagement and dramatic effect.\n\nPronunciation: Precise articulation of technical terms with enthusiastic emphasis to underline their importance.\n\nPersonality Affect: Professional yet approachable, blending credibility with genuine excitement to energise and unify the audience.",
            lines=10,
            interactive=True
        )
        input_box = gr.Textbox(
            label="Input",
            value="We’re excited to launch the new gpt-4o-mini-tts model on Azure OpenAI. Developers can now “instruct” the model not just on what to say but how to say it—enabling more customised experiences for use cases ranging from customer service to creative storytelling.\n\nWe're also thrilled to share that the new gpt-4o-transcribe and gpt-4o-mini-transcribe models are now available to deploy in Azure OpenAI. These new speech to text models have improved word error rates and better language recognition and accuracy, compared to the original Whisper models.\n\nDeploy them in Azure AI Foundry, and try them today!",
            lines=10,
            interactive=True
        )
    voice_picker = gr.Dropdown(VOICE_LIST, value="ballad", label="Voice Picker")
    output_audio = gr.Audio(label="Audio Output", type="filepath")
    play_button = gr.Button("Generate Audio")
    play_button.click(
        fn=tts_play, 
        inputs=[instructions_box, input_box, voice_picker], 
        outputs=[output_audio]
    )

if __name__ == "__main__":
    demo.launch()