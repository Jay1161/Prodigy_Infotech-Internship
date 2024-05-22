# from PIL import Image

# def encrypt(image_path, key):
#     image = Image.open(image_path)
#     width, height = image.size
#     encrypted_image = Image.new(image.mode, (width, height))
    
#     for y in range(height):
#         for x in range(width):
#             pixel = image.getpixel((x, y))
#             encrypted_pixel = tuple((p + key) % 256 for p in pixel)
#             encrypted_image.putpixel((x, y), encrypted_pixel)
    
#     encrypted_image.save("encrypted_image.png")
#     print("Image encrypted successfully!")

# def decrypt(image_path, key):
#     encrypted_image = Image.open(image_path)
#     width, height = encrypted_image.size
#     decrypted_image = Image.new(encrypted_image.mode, (width, height))
    
#     for y in range(height):
#         for x in range(width):
#             pixel = encrypted_image.getpixel((x, y))
#             decrypted_pixel = tuple((p - key) % 256 for p in pixel)
#             decrypted_image.putpixel((x, y), decrypted_pixel)
    
#     decrypted_image.save("decrypted_image.png")
#     print("Image decrypted successfully!")

# def main():
#     while True:
#         choice = input("Do you want to encrypt or decrypt an image? (e/d): ").lower()
#         if choice == 'e':
#             image_path = input("Enter the path to the image to encrypt: ")
#             key = int(input("Enter the encryption key: "))
#             encrypt(image_path, key)
#         elif choice == 'd':
#             image_path = input("Enter the path to the image to decrypt: ")
#             key = int(input("Enter the decryption key: "))
#             decrypt(image_path, key)
#         else:
#             print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
        
#         another = input("Do you want to perform another operation? (y/n): ")
#         if another.lower() != 'y':
#             break

# if __name__ == "__main__":
#     main()
