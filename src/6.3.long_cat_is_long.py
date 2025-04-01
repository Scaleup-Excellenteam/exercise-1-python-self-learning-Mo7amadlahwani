"""
This function processes a string by:
1. Converting it to lowercase.
2. Removing punctuation.
3. Splitting it into words.
4. Filtering only alphabetic words.
5. Returning a dictionary of each word and its length.
"""
import string
def long_cat_is_long(text):
    """
        Process the input text to create a dictionary where each word is mapped to its length.
        Only alphabetic words are considered, and punctuation is removed.

        Parameters:
        - text (str): The input string to process.

        Returns:
        - dict: A dictionary with words as keys and their corresponding lengths as values.
        """
    text = text.lower()  # Convert to lowercase
    words = text.translate(str.maketrans('', '', string.punctuation)).split()  # Remove punctuation and split
    words = [word for word in words if word.isalpha()]  # Keep only alphabetic words
    return {word: len(word) for word in words}

if __name__=="__main__":
    long_cat_is_long("")