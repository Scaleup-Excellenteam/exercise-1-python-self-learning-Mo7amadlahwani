"""
This function merges multiple lists into one, optionally inserting a separator between them.
If a separator is provided, it will be added after each list.
"""
def cup_of_join(*lists,sep=None):
    """
        Merges multiple lists into one list, optionally inserting a separator between them.

        Args:
        *lists (list): One or more lists to be merged. Each list can contain any type of elements.
        sep (optional): The separator to be inserted between the lists. Defaults to None.
                         If provided, it will be added after each list in the result.

        Returns:
        list: A new list containing all elements from the input lists. If a separator is provided, it will be added
              after each list. If no lists are provided, returns None.

        Example:
        >>> cup_of_join([1, 2], [3, 4], [5, 6], sep=",")
        [1, 2, ',', 3, 4, ',', 5, 6]

        >>> cup_of_join([1, 2], [3, 4])
        [1, 2, 3, 4]

        >>> cup_of_join()
        None
        """
    if len(lists)==0:
        return None
    cup = []
    for lst in lists:
        for item in lst:
            cup.append(item)
        if sep is not None:
            cup.append(sep)
    return cup


if __name__=="__main__":
    cup_of_join()
