import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def perform_encryption():
    try:
        shift = int(shift_entry.get())
        message = message_entry.get("1.0", tk.END).strip()
        encrypted_message = encrypt(message, shift)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, encrypted_message)
        message_entry.delete("1.0", tk.END)
        shift_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

def perform_decryption():
    try:
        shift = int(shift_entry.get())
        message = message_entry.get("1.0", tk.END).strip()
        decrypted_message = decrypt(message, shift)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, decrypted_message)
        message_entry.delete("1.0", tk.END)
        shift_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Tool")

# Create GUI elements
message_label = tk.Label(root, text="Enter Message:")
message_entry = tk.Text(root, height=5, width=40)
shift_label = tk.Label(root, text="Enter Shift Value:")
shift_entry = tk.Entry(root)

encrypt_button = tk.Button(root, text="Encrypt", command=perform_encryption)
decrypt_button = tk.Button(root, text="Decrypt", command=perform_decryption)
result_label = tk.Label(root, text="Result:")
result_text = tk.Text(root, height=5, width=40)

# Layout GUI elements
message_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
message_entry.grid(row=0, column=1, padx=10, pady=5)
shift_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
shift_entry.grid(row=1, column=1, padx=10, pady=5)
encrypt_button.grid(row=2, column=0, padx=10, pady=5)
decrypt_button.grid(row=2, column=1, padx=10, pady=5)
result_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
result_text.grid(row=3, column=1, padx=10, pady=5)

# Start the GUI main loop
root.mainloop()
