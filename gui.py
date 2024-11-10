import tkinter as tk
import json
from action import handle_command  # Assuming handle_command processes the commands
from user_settings.settings import save_user_name, load_user_name
from speech.voice_output import set_voice
from voice_input import listen_to_command

# Suggested commands list
suggested_commands = ["Tell me a joke", "Set a reminder", "What's the weather?", "Quote of the day", "Inspire me"]

# Function to update suggestions based on user input
def update_suggestions(event):
    input_text = command_entry.get().lower()
    suggestions_listbox.delete(0, tk.END)  # Clear previous suggestions
    for command in suggested_commands:
        if input_text in command.lower():
            suggestions_listbox.insert(tk.END, command)

# Function to handle selecting a suggestion from the list
def select_suggestion(event):
    try:
        selected_command = suggestions_listbox.get(suggestions_listbox.curselection())
        command_entry.delete(0, tk.END)  # Clear the entry box
        command_entry.insert(0, selected_command)  # Insert the selected suggestion
        suggestions_listbox.delete(0, tk.END)  # Clear the suggestions list after selection
        handle_command(selected_command)  # Optionally, process the selected command
    except tk.TclError:
        pass  # Ignore errors when no selection is made

# Function to handle command entry submission
def submit_command():
    command = command_entry.get()
    if command:  # Ensure command is not empty
        response = handle_command(command, mood=mood_var.get(), language=language_var.get())  # Pass the selected mood and language
        response_label.config(text=response)  # Display the response in the GUI
        command_entry.delete(0, tk.END)
        suggestions_listbox.delete(0, tk.END)  # Clear suggestions after submission

# Function to set user name from input field
def set_user_name():
    global user_name
    user_name = name_entry.get()
    greeting_label.config(text=f"Hello, {user_name}! How can I assist you today?")
    save_user_name(user_name)

# Function to update voice gender dynamically
def update_voice_gender(gender):
    set_voice(gender)

# Function to update voice speed dynamically
def update_voice_speed(speed):
    from speech.voice_output import engine
    engine.setProperty('rate', int(speed))

# Function to listen for voice command and handle it
def handle_voice_command():
    command = listen_to_command()
    if command:
        response = handle_command(command, mood=mood_var.get(), language=language_var.get())  # Pass the selected mood and language
        response_label.config(text=response)

# Function to search command history
def search_history():
    search_term = search_entry.get().lower()
    history_listbox.delete(0, tk.END)  # Clear previous results

    try:
        with open("command_log.json", "r") as log_file:
            for line in log_file:
                log_entry = json.loads(line)
                if search_term in log_entry["command"].lower():
                    history_listbox.insert(tk.END, f"{log_entry['timestamp']}: {log_entry['command']} -> {log_entry['response']}")
    except FileNotFoundError:
        history_listbox.insert(tk.END, "No history found.")

# Load user name if it exists
user_name = load_user_name()

# GUI Setup
root = tk.Tk()
root.title("MyAssist - Virtual Assistant")

# Name Input
name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

name_button = tk.Button(root, text="Set Name", command=set_user_name)
name_button.pack()

# Greeting Label
greeting_text = f"Hello {user_name}, how can I assist you?" if user_name else "Hello! How can I assist you today?"
greeting_label = tk.Label(root, text=greeting_text)
greeting_label.pack()

# Command Entry
command_entry = tk.Entry(root)
command_entry.pack()
command_entry.bind("<KeyRelease>", update_suggestions)  # Update suggestions on key release

# Suggestions Listbox
suggestions_listbox = tk.Listbox(root, height=5)
suggestions_listbox.pack()
suggestions_listbox.bind("<<ListboxSelect>>", select_suggestion)  # Select suggestion on click

# Command Submission Button
submit_button = tk.Button(root, text="Submit", command=submit_command)
submit_button.pack()

# Voice Command Button
listen_button = tk.Button(root, text="Listen", command=handle_voice_command)
listen_button.pack()

# Mood Selection
mood_label = tk.Label(root, text="Select Mood:")
mood_label.pack()

mood_var = tk.StringVar(value="friendly")
mood_dropdown = tk.OptionMenu(root, mood_var, "friendly", "formal", "humorous")
mood_dropdown.pack()

# Language Selection
language_label = tk.Label(root, text="Select Language:")
language_label.pack()

language_var = tk.StringVar(value="en")
language_dropdown = tk.OptionMenu(root, language_var, "en", "es", "fr", "de")  # Add more languages as needed
language_dropdown.pack()

# Search Command History
search_label = tk.Label(root, text="Search Command History:")
search_label.pack()

search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_history)
search_button.pack()

# History Listbox
history_listbox = tk.Listbox(root, height=10)
history_listbox.pack()

# Voice Gender Selection
gender_label = tk.Label(root, text="Select Voice Gender:")
gender_label.pack()

gender_var = tk.StringVar(value="female")
gender_dropdown = tk.OptionMenu(root, gender_var, "female", "male", command=update_voice_gender)
gender_dropdown.pack()

# Voice Speed Slider
speed_label = tk.Label(root, text="Set Voice Speed:")
speed_label.pack()

speed_slider = tk.Scale(root, from_=100, to=200, orient="horizontal", command=update_voice_speed)
speed_slider.set(150)  # Default speed
speed_slider.pack()

# Response Display Label
response_label = tk.Label(root, text="", wraplength=300)  # Shows assistant's response
response_label.pack()

# Run the GUI
root.mainloop()
