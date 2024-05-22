]





import tkinter as tk
from tkinter import filedialog
from PIL import Image

def encrypt_image():
    image_path = filedialog.askopenfilename(title="Select Image for Encryption")
    if image_path:
        key = int(key_entry.get())
        image = Image.open(image_path)
        width, height = image.size
        encrypted_image = Image.new(image.mode, (width, height))

        for y in range(height):
            for x in range(width):
                pixel = image.getpixel((x, y))
                encrypted_pixel = tuple((p + key) % 256 for p in pixel)
                encrypted_image.putpixel((x, y), encrypted_pixel)

        save_path = filedialog.asksaveasfilename(title="Save Encrypted Image As", defaultextension=".png",
                                                  filetypes=[("PNG files", "*.png")])
        if save_path:
            encrypted_image.save(save_path)
            result_label.config(text="Image encrypted successfully!", fg="green")
        else:
            result_label.config(text="Encryption cancelled", fg="red")

def decrypt_image():
    image_path = filedialog.askopenfilename(title="Select Image for Decryption")
    if image_path:
        key = int(key_entry.get())
        encrypted_image = Image.open(image_path)
        width, height = encrypted_image.size
        decrypted_image = Image.new(encrypted_image.mode, (width, height))

        for y in range(height):
            for x in range(width):
                pixel = encrypted_image.getpixel((x, y))
                decrypted_pixel = tuple((p - key) % 256 for p in pixel)
                decrypted_image.putpixel((x, y), decrypted_pixel)

        save_path = filedialog.asksaveasfilename(title="Save Decrypted Image As", defaultextension=".png",
                                                  filetypes=[("PNG files", "*.png")])
        if save_path:
            decrypted_image.save(save_path)
            result_label.config(text="Image decrypted successfully!", fg="green")
        else:
            result_label.config(text="Decryption cancelled", fg="red")

# Create the main window
root = tk.Tk()
root.title("Image Encryption Tool")

# Create GUI elements
encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_image)
decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_image)
key_label = tk.Label(root, text="Enter Key:")
key_entry = tk.Entry(root)
result_label = tk.Label(root, text="", fg="green")

# Layout GUI elements
encrypt_button.grid(row=0, column=0, padx=10, pady=5)
decrypt_button.grid(row=0, column=1, padx=10, pady=5)
key_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
key_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
result_label.grid(row=2, columnspan=2, padx=10, pady=5)

# Start the GUI main loop
root.mainloop()
