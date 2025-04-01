
"""
This function groups items in an iterable based on the result of a function `f`.
It returns a dictionary where the keys are the results of applying `f` to each item,
and the values are lists of items that share the same result.
"""

from collections import defaultdict
"""
    Groups the items in the iterable based on the function `f`.

    Parameters:
    - f (function): A function to apply to each item in the iterable to generate the key.
    - iterable (iterable): The iterable of items to group.

    Returns:
    - dict: A dictionary where the keys are the results of applying `f` to each item,
            and the values are lists of items that share the same key.
    """
def group_by(f, iterable):
    result = defaultdict(list) # יצירת מילון שבו הערכים הם רשימות
    for item in iterable:  # עבור כל איבר ב-iterable
        key = f(item)  # הפעלת הפונקציה על האיבר והוספתו לרשימה במילון
        result[key].append(item)
    return dict(result)  # המרת defaultdict למילון רגיל לפני החזרת התוצאה


if __name__=="__main__":
    group_by(len,["hi"])

