import speech_recognition as sr

def listen_to_command():
    recognizer = sr.Recognizer()
    
    # Ensure the microphone is accessible
    with sr.Microphone() as source:
        print("Listening for a command...")
        # Optional: adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        try:
            audio = recognizer.listen(source, timeout=5)  # Timeout after 5 seconds
        except Exception as e:
            print(f"Error while listening: {e}")
            return None

    try:
        # Convert the audio to text
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
