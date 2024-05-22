import tkinter as tk
from tkinter import filedialog
from PIL import Image
import random

def manipulate_pixel(value, key, operation):
    if operation == "encrypt":
        return (value + key) % 256
    else:  # decrypt
        return (value - key) % 256

def encrypt_decrypt_image(operation):
    image_path = filedialog.askopenfilename(title=f"Select Image for {operation.capitalize()}")
    if image_path:
        try:
            key = int(key_entry.get())
        except ValueError:
            result_label.config(text="Key must be an integer.", fg="red")
            return
        
        image = Image.open(image_path)
        width, height = image.size
        pixels = list(image.getdata())
        
        # Create a random number generator with the given key
        random.seed(key)
        
        if operation == "encrypt":
            # Manipulate pixel values and shuffle them
            if image.mode == "RGB":
                manipulated_pixels = [(manipulate_pixel(r, key, operation),
                                       manipulate_pixel(g, key, operation),
                                       manipulate_pixel(b, key, operation)) for r, g, b in pixels]
            elif image.mode == "RGBA":
                manipulated_pixels = [(manipulate_pixel(r, key, operation),
                                       manipulate_pixel(g, key, operation),
                                       manipulate_pixel(b, key, operation),
                                       a) for r, g, b, a in pixels]
            else:
                manipulated_pixels = [manipulate_pixel(p, key, operation) for p in pixels]
            random.shuffle(manipulated_pixels)
        else:  # decrypt
            # Unshuffle pixels
            shuffled_indices = list(range(len(pixels)))
            random.shuffle(shuffled_indices)
            unshuffled_pixels = [None] * len(pixels)
            for i, shuffled_index in enumerate(shuffled_indices):
                unshuffled_pixels[shuffled_index] = pixels[i]
            
            # Manipulate pixel values back
            if image.mode == "RGB":
                manipulated_pixels = [(manipulate_pixel(r, key, operation),
                                       manipulate_pixel(g, key, operation),
                                       manipulate_pixel(b, key, operation)) for r, g, b in unshuffled_pixels]
            elif image.mode == "RGBA":
                manipulated_pixels = [(manipulate_pixel(r, key, operation),
                                       manipulate_pixel(g, key, operation),
                                       manipulate_pixel(b, key, operation),
                                       a) for r, g, b, a in unshuffled_pixels]
            else:
                manipulated_pixels = [manipulate_pixel(p, key, operation) for p in unshuffled_pixels]

        # Create a new image with manipulated pixels
        new_image = Image.new(image.mode, image.size)
        new_image.putdata(manipulated_pixels)
        
        save_path = filedialog.asksaveasfilename(title=f"Save {operation.capitalize()}ed Image As", defaultextension=".png",
                                                  filetypes=[("PNG files", "*.png")])
        if save_path:
            new_image.save(save_path)
            result_label.config(text=f"Image {operation}ed successfully!", fg="green")
        else:
            result_label.config(text=f"{operation.capitalize()}ion cancelled", fg="red")

def encrypt_image():
    encrypt_decrypt_image("encrypt")

def decrypt_image():
    encrypt_decrypt_image("decrypt")

# Create the main window
root = tk.Tk()
root.title("Image Encryption Tool")

# Create GUI elements
key_label = tk.Label(root, text="Enter Key:")
key_entry = tk.Entry(root)
encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_image)
decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_image)
result_label = tk.Label(root, text="", fg="green")

# Layout GUI elements
key_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
key_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
encrypt_button.grid(row=1, column=0, padx=10, pady=5)
decrypt_button.grid(row=1, column=1, padx=10, pady=5)
result_label.grid(row=2, columnspan=2, padx=10, pady=5)

# Start the GUI main loop
root.mainloop()
