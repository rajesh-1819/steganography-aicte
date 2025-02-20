import cv2
import os

# Load the image
img = cv2.imread("moon.jpg") 

# Get the secret message and passcode
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Append a special marker to indicate the end of the message
msg += "~"

# Mapping of characters to numbers
d = {chr(i): i for i in range(32, 127)}  # ASCII printable characters

n, m, z = 0, 0, 0
height, width, _ = img.shape  # Get image dimensions
max_chars = height * width  # Maximum number of characters

# Ensure the message fits in the image
if len(msg) > max_chars:
    print("Message too large to fit in the image!")
    exit()

# Encrypt the message into the image
for char in msg:
    img[n, m, z] = d[char]  # Store ASCII value
    z = (z + 1) % 3  # Cycle through RGB channels
    if z == 0:
        m += 1
        if m >= width:  # Move to next row if needed
            m = 0
            n += 1

# Save the encrypted image as PNG 
cv2.imwrite("encryptedImage.png", img)
print("Encryption completed! Encrypted image saved as 'encryptedImage.png'.")

# Open the encrypted image
os.system("start encryptedImage.png")
