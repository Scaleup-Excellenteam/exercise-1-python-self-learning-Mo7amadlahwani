"""
Calculates the total cost of ingredients based on given prices.
Optional ingredients can be excluded from the cost calculation.

Parameters:
- prices (dict): A dictionary mapping ingredient names to their price per 100 units.
- optionals (iterable, optional): A set of ingredient names to exclude from pricing.
- **ingredients: Keyword arguments representing ingredient names and their respective amounts.

Returns:
- float: The total calculated price of the selected ingredients.
"""
def piece_of_cake(prices, optionals=None, **ingredients):
    """
    Calculates the total cost of ingredients based on given prices.
    Optional ingredients can be excluded from the cost calculation.

    Parameters:
    - prices (dict): A dictionary mapping ingredient names to their price per 100 units.
    - optionals (iterable, optional): A set of ingredient names to exclude from pricing. Default is None.
    - **ingredients: Keyword arguments representing ingredient names and their respective amounts (in units).

    Returns:
    - float: The total calculated price of the selected ingredients.
    """
    if not prices or not ingredients:
        return 0
    final_price = 0
    if optionals:
        optionals = set(optionals)
    else:
        optionals = set()
    for ingredient, amount in ingredients.items():
        if ingredient not in optionals and ingredient in prices:
            final_price += (amount / 100) * prices[ingredient]
    return final_price


if __name__ == "__main__":
    piece_of_cake({})
