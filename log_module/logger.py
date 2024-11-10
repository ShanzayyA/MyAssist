import datetime

def log_speech(text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("speech_log.txt", "a") as log_file:
            log_file.write(f"[{timestamp}] {text}\n")
    except IOError as e:
        print(f"Error logging speech: {e}")  # Log the error to the console or handle it as needed
