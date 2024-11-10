import time
import threading
import random
import json
from speech.voice_output import speak_text, set_voice
from user_settings.settings import save_user_name, load_user_name
from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Mood-based response sets
mood_responses = {
    "friendly": {
        "default": "I'm here to help with anything else you need.",
        "joke": "Here's a funny one: {}",
        "quote": "You'll love this: {}"
    },
    "formal": {
        "default": "I am available to assist you with any inquiries.",
        "joke": "I have a joke for you: {}",
        "quote": "Please consider this quote: {}"
    },
    "humorous": {
        "default": "What else can I help you with? I'm all ears!",
        "joke": "Knock knock! Who's there? {}",
        "quote": "This will crack you up: {}"
    }
}

def log_command_response(command, response):
    """Log the command and response in a JSON file."""
    with open("command_log.json", "a") as log_file:
        log_entry = {"command": command, "response": response, "timestamp": time.time()}
        log_file.write(json.dumps(log_entry) + "\n")

# Function to translate text
def translate_text(text, dest_language):
    """Translate the input text to the specified destination language."""
    try:
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Return original text if translation fails

# Function to set reminders
def set_reminder(text):
    """Set a reminder based on the user's command."""
    words = text.split()
    try:
        # Extract time duration in minutes from user input
        minutes = int([word for word in words if word.isdigit()][0])
        reminder_text = " ".join(words[words.index("to") + 1:])
        speak_text(f"Reminder set for {minutes} minutes.")

        # Define function to wait and then alert user
        def remind():
            time.sleep(minutes * 60)
            speak_text(f"Reminder: {reminder_text}")

        # Start a thread so it runs in the background
        threading.Thread(target=remind).start()
        return f"Reminder set for {minutes} minutes to {reminder_text}."
    except (IndexError, ValueError):
        return "I couldn't set the reminder. Please specify the time in minutes."

# Function to get a joke
def get_joke():
    """Return a random joke."""
    jokes = [
        "Why did the computer cross the road? To get to the other side of the screen!",
        "I told my computer I needed a break, and now it won't stop sending me coffee memes.",
        "How many programmers does it take to change a light bulb? None. It's a hardware problem!"
    ]
    return random.choice(jokes)

# Function to get an inspirational quote
def get_quote():
    """Return a random inspirational quote."""
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "The journey of a thousand miles begins with one step. - Lao Tzu"
    ]
    return random.choice(quotes)

def handle_command(text, mood="friendly", language="en"):
    """Process the user's command and return an appropriate response."""
    text = translate_text(text, language)
    response = ""

    if "remind me" in text:
        response = set_reminder(text)
    elif "tell me a joke" in text:
        joke = get_joke()
        response = mood_responses[mood]["joke"].format(joke)
        speak_text(joke)
    elif "inspire me" in text or "quote of the day" in text:
        quote = get_quote()
        response = mood_responses[mood]["quote"].format(quote)
        speak_text(quote)
    else:
        response = mood_responses[mood]["default"]

    # Log the command and response
    log_command_response(text, response)
    return response
