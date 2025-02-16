import cv2

def decrypt_image(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            print("Error: Unable to read the image. Check the file path.")
            return
        
        height, width, _ = img.shape
        c = {i: chr(i) for i in range(256)}

        # Retrieve the passcode length
        passcode_length = img[0, 0, 0]

        # Retrieve the stored passcode
        stored_passcode = ""
        for i in range(passcode_length):
            stored_passcode += c[img[0, i + 1, 0]]

        # Ask for passcode
        user_passcode = input("Enter passcode for decryption: ")
        if user_passcode != stored_passcode:
            print("Authentication failed! Incorrect passcode.")
            return

        # Retrieve the message
        message = ""
        n, m, z = 1, 0, 0  # Start extracting from (1,0,0)
        while True:
            char_value = img[n, m, z]
            if char_value == 0:  # Stop at NULL character
                break
            message += c[char_value]
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m >= width:
                    m = 0
                    n += 1
        
        print("Decrypted Message:", message)
    except Exception as e:
        print("An error occurred:", e)

# User Input
image_path = input("Enter the path of the encrypted image: ")
decrypt_image(image_path)
