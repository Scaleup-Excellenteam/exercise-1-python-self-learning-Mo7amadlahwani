"""
Module for reading a binary file, decoding it, and extracting valid lowercase letter sequences
that end with an exclamation mark ('!'). Sequences with at least 5 characters before '!' are considered valid.

The module defines a function `parsle_tongue` that reads a file in chunks, processes its content, and yields valid sequences.
"""
def parsle_tongue():
    """
       Reads a binary file in chunks, decodes it, and extracts lowercase letter sequences ending with '!' that are at least 5 characters long.
       Each valid sequence is yielded one by one.

       The function works as follows:
       - It reads the file in chunks and decodes each chunk using UTF-8 encoding (ignoring errors).
       - It extracts sequences of lowercase letters that end with '!', and yields those sequences if they contain
         at least 5 characters before the '!'.
       - Sequences are reset if an invalid character (non-lowercase or non-ASCII) is found.

       Yields:
       - str: A valid lowercase letter sequence ending with '!' and at least 5 characters before '!'.

       Exceptions:
       - FileNotFoundError: If the specified file does not exist, a message will be printed.
    """
    file_path = "logo.jpg"
    chunk_size = 500
    try:
        with open(file_path, "rb") as file:
            new_str = ""
            while chunk := file.read(chunk_size):
                decoded_chunk = chunk.decode("utf-8", errors="ignore")
                for char in decoded_chunk:
                    if char.islower():
                        new_str += char
                    elif char == '!':
                        if len(new_str) >= 5:
                            yield new_str
                        new_str = ""
                    else:
                        new_str = ""
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    for i in parsle_tongue():
        print(i)
