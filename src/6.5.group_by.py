"""
This function groups items in an iterable based on the result of a function `f`.
It returns a dictionary where the keys are the results of applying `f` to each item,
and the values are lists of items that share the same result.
"""

from collections import defaultdict


def group_by(f, iterable):
    """
    Groups the items in the iterable based on the function `f`.

    Parameters:
    - f (function): A function to apply to each item in the iterable to generate the key.
    - iterable (iterable): The iterable of items to group.

    Returns:
    - dict: A dictionary where the keys are the results of applying `f` to each item,
            and the values are lists of items that share the same key.
    """
    result = defaultdict(list)
    for item in iterable:
        key = f(item)
        result[key].append(item)
    return dict(result)


if __name__ == "__main__":
    group_by(len, ["hi"])
