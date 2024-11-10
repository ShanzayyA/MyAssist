### MyAssist - Virtual Assistant

MyAssist is a Python-based virtual assistant designed to streamline personal task management through intuitive voice commands, intelligent reminders, and customizable mood-based interactions. By leveraging advanced speech recognition and text-to-speech technologies, MyAssist offers a unique and user-friendly experience.

### Key Features 

- **Voice Commands**: Control the assistant and manage tasks using natural language.
- **Reminders**: Set notifications for specific times to help you stay on track.
- **Entertainment**: Enjoy jokes and inspirational quotes for a quick break.
- **Mood-Based Responses**: Choose from different response styles (friendly, formal, humorous) for a more personalized interaction.
- **Multilingual Support**: Communicate with MyAssist in multiple languages through Google Translate.
- **Command History**: Easily search through past commands and responses.


### Development Approach and Enhancements
MyAssist was designed with a focus on creating an interactive, multilingual, and user-friendly virtual assistant. The project drew initial insights from various virtual assistant frameworks, including Faizan Alam’s AI Assistant, but has been extensively developed and enhanced with unique features and a custom architecture, making it an independently created project.

- **Google Text-to-Speech (gTTS)** integration for enhanced voice output quality.
- **Google Translate (Googletrans)** support, enabling seamless multilingual interactions.
- **Mood-based responses** to personalize the assistant’s tone and adapt to user preferences.
- Improved **notification system for reminders** and **command logging** for efficient task tracking and history searchability.

These enhancements transform MyAssist into a versatile and practical tool that goes beyond traditional virtual assistant capabilities.


## Installation

### Prerequisites

Make sure you have Python 3.9 or later installed on your system.

### Steps to Install

```bash
# Clone the repository
git clone https://github.com/yourusername/MyAssist.git
cd MyAssist

# Create a virtual environment (optional but recommended)
python3 -m venv myassist_env
source myassist_env/bin/activate  # On Windows use `myassist_env\\Scripts\\activate`

# Install the required packages
pip install -r requirements.txt

# Ensure you have the required dependencies installed
brew install tcl-tk

# To run the virtual assistant, execute the following command:
python gui.py

```
### Acknowledgments
This project uses the following libraries:

- **SpeechRecognition**: For recognizing speech input.
- **gTTS(Google Text-to-Speech)**: To convert text responses to speech.
- **Pyttsx3**: A text-to-speech conversion library.
- **Googletrans**: For translating text to different languages




