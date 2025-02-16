import cv2
import os

def encrypt_image(image_path, secret_message, passcode):
    try:
        img = cv2.imread(image_path)
        if img is None:
            print("Error: Unable to read the image. Check the file path.")
            return
        
        height, width, _ = img.shape
        max_chars = height * width * 3 - len(passcode) - 2  # Leave space for passcode
        if len(secret_message) > max_chars:
            print("Error: Message too long to fit in the image.")
            return

        d = {chr(i): i for i in range(256)}

        # Store the passcode length in (0,0,0)
        img[0, 0, 0] = len(passcode)

        # Store the passcode in the first few pixels
        for i, char in enumerate(passcode):
            img[0, i + 1, 0] = d[char]

        # Store the secret message
        n, m, z = 1, 0, 0  # Start storing from (1,0,0)
        for char in secret_message:
            img[n, m, z] = d[char]
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m >= width:
                    m = 0
                    n += 1

        encrypted_path = "encrypted_image.png"
        cv2.imwrite(encrypted_path, img)
        print(f"Encryption successful! Image saved as {encrypted_path}")
    except Exception as e:
        print("An error occurred:", e)

# User Input
image_path = input("Enter the path of the image: ")
secret_message = input("Enter the secret message: ")
passcode = input("Enter a passcode: ")

encrypt_image(image_path, secret_message, passcode)
