import cv2
img = cv2.imread("encryptedImage.png")
if img is None:
    print("Error: Image not found. Make sure 'encryptedImage.png' exists.")
    exit()

c = {i: chr(i) for i in range(32, 127)}
pas = input("Enter passcode for Decryption: ")
if pas:
    message = ""
    n, m, z = 0, 0, 0
    height, width, _ = img.shape  

    while n < height and m < width:
        try:
            char = c[img[n, m, z]]  
            if char == "~":  
                break
            message += char

            z = (z + 1) % 3 
            if z == 0:
                m += 1
                if m >= width:
                    m = 0
                    n += 1
        except KeyError:
            break  
        except IndexError:
            break  

    print("Decryption message:", message)
else:
    print("Invalid passcode.")
