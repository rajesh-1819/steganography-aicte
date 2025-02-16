import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")

# Ensure image is loaded properly
if img is None:
    print("Error: Image not found. Make sure 'encryptedImage.png' exists.")
    exit()

# Mapping of numbers to characters
c = {i: chr(i) for i in range(32, 127)}

# Ask the user for the passcode
pas = input("Enter passcode for Decryption: ")

# If passcode is correct, begin decryption
if pas:
    message = ""
    n, m, z = 0, 0, 0
    height, width, _ = img.shape  # Get image dimensions

    while n < height and m < width:
        try:
            char = c[img[n, m, z]]  # Retrieve character from pixel value
            if char == "~":  # Stop reading when end marker is found
                break
            message += char

            z = (z + 1) % 3  # Cycle through RGB channels
            if z == 0:
                m += 1
                if m >= width:
                    m = 0
                    n += 1
        except KeyError:
            break  # Stop if there's an issue
        except IndexError:
            break  # Stop if out of bounds

    print("Decryption message:", message)
else:
    print("Invalid passcode.")
