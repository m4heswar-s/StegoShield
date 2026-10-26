import numpy as np
from PIL import Image

def encodeImage(imgPath,outputPath,secretText):
    img = Image.open(imgPath)
    img_array = np.array(img)  #3D array:height,width,RGB Channels
    
    binary_text = "".join(format(ord(chr),"08b")for chr in secretText)
    #so it changes each character to 8 bit binary number and then join

    header_text = format(len(binary_text),"032b")
    binary_messg = header_text + binary_text
    #here header_text store the lenght of the message so that the decoder know when to stop

    flat_img_array = img_array.flatten() #convert 3D array to 1D array of pixels

    #Check if image can store the message:
    if (len(binary_messg)>len(flat_img_array)):
        raise ValueError("Error: Message is too large for the given image")
        #Raise valueError and stop program

    #encoding message to the image pixels
    for  i in range(len(binary_messg)):
        flat_img_array[i] =(flat_img_array[i] & 254) | int(binary_messg[i])

    #saving the image
    encode_img_array = flat_img_array.reshape(img_array.shape)
    stego_img = Image.fromarray(encode_img_array.astype("uint8"))
    stego_img.save(outputPath)

    print("Stego_image is created successfully!")
    print(f"Saved as:{outputPath}")


def decodeImage(imgPath):
    img = Image.open(imgPath)
    img_array = np.array(img) #3D array:height,width,RGB Channels
    flat_array = img_array.flatten()

    bit_array = [str(pixel & 1) for pixel in flat_array]
    #store the LSB of the pixels

    lengthBits = "".join(bit_array[:32])
    length_messg = int(lengthBits, 2)
    #this will give us the length of the  secret message

    messgBit = bit_array[32:32+length_messg]
    charByte = ["".join(messgBit[i:i+8]) for i in range(0,len(messgBit),8)]
    #this will group the 8bits of each character and form a list

    #this  will convert each  Byte to the character
    decoded_messg = "".join([chr(int(b,2)) for b in charByte])
    return decoded_messg 


def getImageCapacity(imgPath):
    try:
        img = Image.open(imgPath)
        img_array = np.array(img) #3D array
        total_bits = img_array.size
        max_chars = (total_bits -32)//8 #32bit for the header and rest for the message
        return max(0,max_chars)
    except Exception:
        return 0