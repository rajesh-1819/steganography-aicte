This project implements image-based steganography using OpenCV in Python. It allows users to hide secret messages inside an image and later retrieve them with a passcode.

Features:

1.Encrypt messages inside an image (Steganography)

2.Decrypt messages from the encrypted image

3.Uses lossless PNG format to prevent data loss

4.Requires a passcode for decryption

Prerequisites:

Ensure you have the following installed:

Python 3.x

OpenCV (cv2)

OS module (built-in in Python)

Install OpenCV if not already installed:

pip install opencv-python

File Structure:

├── encrypt.py      # Encryption Script
├── decrypt.py      # Decryption Script
├── photo.jpg/png        # Sample Input Image
├── encryptedImage.png  # Output Encrypted Image
├── README.md       # Documentation

Usage:

Encryption (Hiding a message in an image):

Place your image (preferably .png) in the project directory.

Run encrypt.py:

  python encrypt.py

Enter a secret message and a passcode.

The encrypted image will be saved as encryptedImage.jpg/png.

Decryption (Retrieving the message from an image): 

Run decrypt.py:

  python decrypt.py

Enter the correct passcode to reveal the hidden message.

Deployment on GitHub:

To upload this project to GitHub:

Initialize a Git repository:

git init

Add files:

git add .

Commit changes:

git commit -m "Initial commit: Steganography project"

Create a new repository on GitHub and copy the provided remote URL.

Link your local repo to GitHub:

git remote add origin <your-repo-url>

Push your code:

  git push -u origin main

Notes:

Use PNG images for best results (JPG compression may alter pixel values).

Ensure the message fits within the image size.

This project is open-source and can be used for learning and development purposes.
