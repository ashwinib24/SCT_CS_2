# 🖼️ SkillCraft Task 2 – Image Encryption Tool

## 🔐 Description

A simple image encryption and decryption tool using pixel manipulation techniques. The tool supports encryption by altering pixel RGB values using a numeric key and can also reverse the process to restore the original image.

## 📂 Files Included

- `image_encryptor.py`: The main Python script for encryption/decryption
- `input.jpg`: Example image to test the program
- `requirements.txt`: Contains required library (`Pillow`)

## ⚙️ Features

- Encrypts an image by modifying pixel values with a user-defined key
- Decrypts the encrypted image using the same key
- CLI-based interaction with image path and key input
- Supports `.jpg`, `.png`, and other common image formats

Requirements
Install dependencies with:

bash
Copy
Edit
pip install -r requirements.txt

Only required library:

Pillow

## ▶️ How to Run

```bash
python image_encryptor.py

Follow the prompts to:

Enter input image path (e.g., input.jpg)

Enter output image path (e.g., encrypted.jpg)

Enter numeric key