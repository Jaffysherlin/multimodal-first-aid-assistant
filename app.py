
---

### 4️⃣ `app.py` (Streamlit UI)
```python
import streamlit as st
from PIL import Image
from image_model import predict_injury
from speech_to_text import recognize_speech
from symptom_nlp import extract_symptoms
from guidance_generator import generate_guidance
from tts_output import text_to_speech
import os

st.set_page_config(page_title="Multimodal First Aid Assistant", layout="wide")

st.title("🩹 Multimodal AI-Based First Aid Assistant")
st.write("Upload an image of the injury and describe symptoms via voice or text.")

# Upload Image
uploaded_file = st.file_uploader("Upload Injury Image", type=["jpg","jpeg","png"])
injury_type = None
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Injury Image", use_column_width=True)
    injury_type = predict_injury(image)
    st.success(f"Detected Injury Type: {injury_type}")

# Record or type symptoms
st.subheader("Record Symptoms or Type Them")
mode = st.radio("Input Mode", ["Text", "Voice"])
symptom_text = ""
if mode == "Text":
    symptom_text = st.text_area("Enter Symptoms Here")
elif mode == "Voice":
    if st.button("Record Symptoms"):
        st.info("Recording... speak now")
        symptom_text = recognize_speech()
        st.success(f"Transcribed Symptoms: {symptom_text}")

# Analyze and Generate Guidance
if st.button("Analyze and Get Guidance"):
    if not uploaded_file and symptom_text.strip() == "":
        st.error("Please provide either an image or symptoms.")
    else:
        symptoms = extract_symptoms(symptom_text)
        guidance = generate_guidance(injury_type, symptoms)
        st.subheader("📝 First Aid Guidance")
        st.write(guidance)

        audio_file = text_to_speech(guidance)
        st.audio(audio_file, format="audio/mp3")
