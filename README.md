            
# Stegno (Image-Based Encryption & Decryption Using Python)

## 📌 Project Overview
This project provides a **secure image-based encryption and decryption system** using **Python and OpenCV**. It allows users to hide secret messages inside an image using pixel manipulation and retrieve them securely using a passcode.

## 🚀 Features
- 🔐 **Passcode-based security** for message encryption & decryption.
- 🖼 **Image steganography** using pixel modification.
- 📏 **Preserves image integrity** while embedding data.
- 🎯 **Python-based implementation** using OpenCV.
- 🔍 **Can be used for forensic & cybersecurity applications.**

## 🛠 Technologies Used
- **Programming Language:** Python
- **Libraries:** OpenCV, NumPy, OS
- **Concepts Used:** Steganography, Image Processing

## 📂 Project Structure
```
📁 Image-Encryption-Project
│── encrypt.py  # Encrypts message into image
│── decrypt.py  # Decrypts message from image
│── README.md  # Project Documentation
│── sample_image.png  # Example image for testing
```

## 📖 How to Use
## 🔹 Encryption
1. Run `encrypt.py` and provide the image path.
2. Enter the **secret message** and **passcode**.
3. The script embeds the message and saves `encrypted_image.png`.

## 🔹 Decryption
1. Run `decrypt.py` and provide the **encrypted image path**.
2. Enter the **correct passcode**.
3. The script retrieves and displays the hidden message.

## 🔍 Example Usage
```bash
# Encryption
python encrypt.py
Enter the path of the image: sample_image.png
Enter the secret message: Hello, World!
Enter a passcode: 1234
Encryption successful! Image saved as encrypted_image.png

# Decryption
python decrypt.py
Enter the path of the encrypted image: encrypted_image.png
Enter passcode for decryption: 1234
Decrypted Message: Hello, World!
```


# #📌 Future Enhancements
- 🛡 **AES/RSA encryption** for stronger security.
- 🎥 **Video steganography** support.
- 🎨 **GUI-based application** for ease of use.



## 📬 Contact
For queries or collaboration, contact: [naveen373sai@gmail.com]

---

**⭐ Don't forget to star this repository if you found it useful!** ⭐

