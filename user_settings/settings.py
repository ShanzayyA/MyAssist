def save_user_name(name):
    try:
        with open("user_name.txt", "w") as f:
            f.write(name)
    except Exception as e:
        print(f"Error saving user name: {e}")  # Log any errors during saving

def load_user_name():
    try:
        with open("user_name.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("User name file not found. Returning None.")  # Log that the file was not found
        return None
    except Exception as e:
        print(f"Error loading user name: {e}")  # Log any other errors that occur
        return None
