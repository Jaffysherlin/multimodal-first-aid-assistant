from gtts import gTTS
import tempfile

def text_to_speech(text):
    tts = gTTS(text)
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp_file.name)
    return tmp_file.name
