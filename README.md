# gpt-4o-mini-tts Text to Speech Demo

![image](https://github.com/user-attachments/assets/86177d5c-3cb2-49cd-9da7-a4262ab85200)

This repository contains two Python scripts demonstrating the use of OpenAI's GPT-4o-mini-TTS (Text-to-Speech) model running on Azure OpenAI:

## Files

### `tts_gradio.py`
A Gradio-based web application that provides an interactive interface for generating speech audio. Users can specify detailed voice instructions, input text, and select from various voice styles. The app generates audio files using Azure OpenAI's GPT-4o-mini TTS model.

### `tts_aoai_announce.py`
An asynchronous Python script demonstrating how to stream audio responses directly from Azure OpenAI's GPT-4o-mini TTS model. It includes detailed voice instructions and plays the generated audio locally using the `LocalAudioPlayer`.

## Requirements
- Python 3.x
- Azure OpenAI API key and endpoint configured via environment variables (`AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_API_VERSION`, `AZURE_OPENAI_API_ENDPOINT`)
- Dependencies listed in scripts (`gradio`, `openai[voice_helpers]`, `python-dotenv`, etc.)

```bash
pip install gradio openai[voice_helpers] python-dotenv
```
