import pyttsx3
from log_module.logger import log_speech

# Initialize the TTS engine
engine = pyttsx3.init()

# Set default properties for the TTS engine
engine.setProperty('rate', 150)  # Default speed
engine.setProperty('volume', 0.9)  # Default volume

# Function to set a specific voice gender
def set_voice(gender="female"):
    voices = engine.getProperty('voices')
    for voice in voices:
        if gender == "female" and "female" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
        elif gender == "male" and "male" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

# Speak function to convert text to audio and log it
def speak_text(text):
    print(f"MyAssist says: {text}")  # Optional: Print the text to console for debugging
    log_speech(text)  # Log the text
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speech synthesis: {e}")  # Log any errors during speech synthesis
