"""
This function decodes a message hidden in an image.
It looks for specific pixels (in this case, white pixels [255, 255, 255]) in the image,
and the row index where these pixels are found corresponds to a character in the decoded message.
"""
import cv2

def remember_remember(img):
    """
        Decodes a hidden message in an image by checking the rows where the pixels are [255, 255, 255].

        Parameters:
        - img (str): The path to the image file containing the hidden message.

        Returns:
        - str: The decoded message as a string.
        """
    image = cv2.imread(img)
    height, width,_= image.shape
    message=[]
    for col in range (width):
        for row in range (height):
            if all(image[row,col,]==[1,1,1]):
                message.append(row)
                break
    decoded_message="".join([chr(pixel) for pixel in message])
    return decoded_message

if __name__ == '__main__':
    remember_remember("./code")