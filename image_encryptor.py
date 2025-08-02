from PIL import Image

def encrypt_image(input_path, output_path, key=50):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Simple encryption by adding key and wrapping around 256
            r_enc = (r + key) % 256
            g_enc = (g + key) % 256
            b_enc = (b + key) % 256
            pixels[x, y] = (r_enc, g_enc, b_enc)

    img.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path, key=50):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Reverse encryption by subtracting key
            r_dec = (r - key) % 256
            g_dec = (g - key) % 256
            b_dec = (b - key) % 256
            pixels[x, y] = (r_dec, g_dec, b_dec)

    img.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    print("Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice: ")

    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    key = int(input("Enter key (number): "))

    if choice == '1':
        encrypt_image(input_path, output_path, key)
    elif choice == '2':
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

