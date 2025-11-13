# Multimodal AI-Based First Aid Assistant

**GitHub Username:** Jaffysherlin

## Description
An AI-powered web app that accepts both **injury images** and **voice descriptions** to provide **personalized, AI-generated first-aid advice** with both **text and voice output**.

## Features
- Upload an injury image for AI analysis
- Record or type symptoms
- Multimodal fusion: image + text analysis
- AI-generated first aid instructions using GPT-2
- Text-to-speech output for guidance
- Interactive Streamlit frontend

## Tech Stack
Python, Streamlit, TensorFlow, HuggingFace Transformers (BERT, GPT-2), Whisper, gTTS

## Run Locally
```bash
git clone https://github.com/Jaffysherlin/multimodal-first-aid-assistant.git
cd multimodal-first-aid-assistant
pip install -r requirements.txt
streamlit run app.py
