import speech_recognition as sr
import whisper

# Using Whisper small model (offline)
model = whisper.load_model("small")

def recognize_speech(audio_file=None):
    if audio_file:
        result = model.transcribe(audio_file)
        return result['text']
    else:
        # Record from microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = ""
        return text
