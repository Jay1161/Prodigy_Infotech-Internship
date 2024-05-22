# import tkinter as tk
# from tkinter import ttk
# import re
# import math

# def check_password_strength(password):
#     length = len(password)
#     uppercase = any(char.isupper() for char in password)
#     lowercase = any(char.islower() for char in password)
#     digit = any(char.isdigit() for char in password)
#     special_char = re.match(r'^.*[\W_].*$', password) is not None
    
#     strength = 0
#     suggestions = []
    
#     if length >= 8:
#         strength += 1
#     else:
#         suggestions.append("Password should be at least 8 characters long.")
#     if uppercase:
#         strength += 1
#     else:
#         suggestions.append("Password should contain at least one uppercase letter.")
#     if lowercase:
#         strength += 1
#     else:
#         suggestions.append("Password should contain at least one lowercase letter.")
#     if digit:
#         strength += 1
#     else:
#         suggestions.append("Password should contain at least one digit.")
#     if special_char:
#         strength += 1
#     else:
#         suggestions.append("Password should contain at least one special character.")
    
#     crack_time = calculate_crack_time(strength, length)
    
#     return strength, suggestions, crack_time

# def calculate_crack_time(strength, length):
#     # Crack time estimation constants
#     possible_chars = 94  # 26 (lowercase letters) + 26 (uppercase letters) + 10 (digits) + 32 (common special characters)
#     hashes_per_second = 1000000000  # 1 billion hashes per second (typical attacker's speed)
#     seconds_per_year = 31536000  # 60 seconds * 60 minutes * 24 hours * 365 days
    
#     entropy = length * math.log2(possible_chars)
#     crack_time_seconds = (2 ** entropy) / hashes_per_second
#     crack_time_years = crack_time_seconds / seconds_per_year
    
#     return crack_time_years

# def assess_password():
#     password = password_entry.get()
#     strength, suggestions, crack_time = check_password_strength(password)
    
#     if strength == 0:
#         strength_label.config(text="Very Weak", fg="red")
#     elif strength == 1:
#         strength_label.config(text="Weak", fg="orange")
#     elif strength == 2:
#         strength_label.config(text="Moderate", fg="yellow")
#     elif strength == 3:
#         strength_label.config(text="Strong", fg="green")
#     else:
#         strength_label.config(text="Very Strong", fg="dark green")
    
#     suggestions_label.config(text="\n".join(suggestions))
#     crack_time_label.config(text=f"Estimated time to crack: {crack_time:.2f} years")

# # Create the main window
# root = tk.Tk()
# root.title("Password Strength Checker")

# # Create GUI elements
# password_label = tk.Label(root, text="Enter Password:")
# password_entry = tk.Entry(root, show="")
# assess_button = tk.Button(root, text="Assess Password", command=assess_password)
# strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
# suggestions_label = tk.Label(root, text="", justify="left", wraplength=200)
# crack_time_label = tk.Label(root, text="", font=("Arial", 10))
# progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')


# # Layout GUI elements
# password_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
# password_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
# assess_button.grid(row=1, columnspan=2, padx=10, pady=5)
# strength_label.grid(row=2, columnspan=2, padx=10, pady=5)
# suggestions_label.grid(row=3, columnspan=2, padx=10, pady=5)
# crack_time_label.grid(row=4, columnspan=2, padx=10, pady=5)

# # Start the GUI main loop
# root.mainloop()


import tkinter as tk
from tkinter import ttk
import re
import math

def check_password_strength(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = re.match(r'^.*[\W_].*$', password) is not None
    
    strength = 0
    suggestions = []
    
    if length >= 8:
        strength += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")
    if uppercase:
        strength += 1
    if lowercase:
        strength += 1
    if digit:
        strength += 1
    if special_char:
        strength += 1
    
    crack_time = calculate_crack_time(strength, length)
    
    return strength, suggestions, crack_time

def calculate_crack_time(strength, length):
    # Crack time estimation constants
    possible_chars = 94  # 26 (lowercase letters) + 26 (uppercase letters) + 10 (digits) + 32 (common special characters)
    hashes_per_second = 1000000000  # 1 billion hashes per second (typical attacker's speed)
    seconds_per_year = 31536000  # 60 seconds * 60 minutes * 24 hours * 365 days
    
    entropy = length * math.log2(possible_chars)
    crack_time_seconds = (2 ** entropy) / hashes_per_second
    crack_time_years = crack_time_seconds / seconds_per_year
    
    return crack_time_years

def assess_password():
    password = password_entry.get()
    strength, suggestions, crack_time = check_password_strength(password)
    
    progress = strength / 5 * 100
    progress_bar['value'] = progress
    
    if strength == 0:
        strength_label.config(text="Very Weak", fg="red")
    elif strength == 1:
        strength_label.config(text="Weak", fg="orange")
    elif strength == 2:
        strength_label.config(text="Moderate", fg="yellow")
    elif strength == 3:
        strength_label.config(text="Strong", fg="green")
    else:
        strength_label.config(text="Very Strong", fg="dark green")
    
    suggestions_label.config(text="\n".join(suggestions))
    crack_time_label.config(text=f"Estimated time to crack: {crack_time:.2f} years")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create GUI elements
password_label = tk.Label(root, text="Enter Password:")
password_entry = tk.Entry(root, show="*")
assess_button = tk.Button(root, text="Assess Password", command=assess_password)
strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
suggestions_label = tk.Label(root, text="", justify="left", wraplength=200)
crack_time_label = tk.Label(root, text="", font=("Arial", 10))
progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')

# Layout GUI elements
password_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
password_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
assess_button.grid(row=1, columnspan=2, padx=10, pady=5)
strength_label.grid(row=2, columnspan=2, padx=10, pady=5)
suggestions_label.grid(row=3, columnspan=2, padx=10, pady=5)
crack_time_label.grid(row=4, columnspan=2, padx=10, pady=5)
progress_bar.grid(row=5, columnspan=2, padx=10, pady=5)

# Start the GUI main loop
root.mainloop()
