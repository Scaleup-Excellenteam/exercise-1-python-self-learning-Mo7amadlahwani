"""
This function decodes a message hidden in an image.
It looks for specific pixels (in this case, white pixels [255, 255, 255]) in the image,
and the row index where these pixels are found corresponds to a character in the decoded message.
"""

def remember_remember(img_path):
    """
    Decodes a hidden message in an image by checking columns for the first white pixel
    and using the row index of that white pixel as an ASCII character code.
    """
    from PIL import Image
    image = Image.open(img_path).convert('RGB')
    width, height = image.size
    pixels = image.load()
    message = []
    for x in range(width):
        for y in range(height):
            if pixels[x, y] == (1, 1, 1):
                message.append(chr(y))
                break  # Only first white pixel per column
    return ''.join(message)


if __name__=="__main__":
    remember_remember("code.png")
