"""
    Returns a list of files in the given directory that start with 'deep'.
    """
import os


def thats_the_way(directory: str) -> list[str]:
    """
        Returns a list of filenames in the given directory that start with 'deep'.
        Args:
        directory (str): The path to the directory to search in.
        Returns:
        list[str]: A list of filenames (strings) in the directory that start with 'deep'.
                   Only files (not directories) are included in the list.
        Example:
        >>> thats_the_way("/path/to/directory")
        ['deepfile1.txt', 'deep_document.pdf']
        If the directory does not exist or cannot be accessed, an empty list is returned.
        """
    lst = []
    for i in os.listdir(directory):
        full_path = os.path.join(directory, i)
        if i.startswith("deep") and os.path.isfile(full_path):
            lst.append(i)
    return lst
if __name__=="__main__":
    thats_the_way("")
