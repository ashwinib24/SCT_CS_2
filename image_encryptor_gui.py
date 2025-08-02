from tkinter import Tk, filedialog, Label, Button, Entry, StringVar
from PIL import Image
import os

def encrypt_image(path, key):
    img = Image.open(path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    save_path = os.path.splitext(path)[0] + "_encrypted.png"
    img.save(save_path)
    return save_path

def decrypt_image(path, key):
    img = Image.open(path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    save_path = os.path.splitext(path)[0] + "_decrypted.png"
    img.save(save_path)
    return save_path

def browse_file():
    file_path.set(filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")]))
    result.set("")

def encrypt_action():
    try:
        key_val = int(key.get())
        output = encrypt_image(file_path.get(), key_val)
        result.set(f"Image encrypted → {output}")
    except Exception as e:
        result.set(f"Error: {e}")

def decrypt_action():
    try:
        key_val = int(key.get())
        output = decrypt_image(file_path.get(), key_val)
        result.set(f"Image decrypted → {output}")
    except Exception as e:
        result.set(f"Error: {e}")

# GUI setup
root = Tk()
root.title("🖼 Image Encryptor Tool")
root.geometry("500x300")

file_path = StringVar()
key = StringVar()
result = StringVar()

Label(root, text="Select Image File:").pack()
Button(root, text="Browse", command=browse_file).pack()

Label(root, textvariable=file_path, wraplength=400).pack()

Label(root, text="Enter Key (number):").pack()
Entry(root, textvariable=key).pack()

Button(root, text="Encrypt Image", command=encrypt_action, bg="lightblue").pack(pady=5)
Button(root, text="Decrypt Image", command=decrypt_action, bg="lightgreen").pack(pady=5)

Label(root, textvariable=result, wraplength=400, fg="blue").pack(pady=10)

root.mainloop()
