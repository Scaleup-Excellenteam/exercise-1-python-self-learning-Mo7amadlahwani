"""
Module for interleaving items from multiple iterables.
This module provides two functions for interleaving:
- `generator_interleave`: A generator that interleaves items from multiple iterables.
- `interleave`: Interleaves items from multiple iterables and handles cases where the iterables are of unequal lengths.
"""



def generator_interleave(*iterables):
    """
       Interleave items from multiple iterables using a generator.

       This function takes multiple iterables as input and yields one item at a time from each iterable in round-robin fashion.
       The function continues until all iterables are exhausted.

       Args:
       - *iterables (iterable): Multiple iterables to be interleaved.

       Yields:
       - Each item from the iterables, interleaved in the order they are provided.

       Example:
       >>> list(generator_interleave([1, 2, 3], ['a', 'b', 'c']))
       [1, 'a', 2, 'b', 3, 'c']
       """
    for group in zip(*iterables):
        for item in group:
            yield item


def interleave(*iterables):
    """
    Interleave items from multiple iterables. If the iterables have different lengths,
    the remaining items from the longest iterable are yielded.

    This function handles cases where the iterables have unequal lengths by continuing to yield items from
    the longest iterable after all shorter iterables are exhausted.

    Args:
    - *iterables (iterable): Multiple iterables to be interleaved.

    Yields:
    - Each item from the iterables, interleaved in the order they are provided. If some iterables are shorter,
      their elements will be exhausted first, and remaining items from the longest iterable will be yielded.

    Example:
    >>> list(interleave([1, 2], ['a', 'b', 'c'], [True, False]))
    [1, 'a', True, 2, 'b', False, 'c']
    """
    if not iterables:
        return
    for group in zip(*iterables):
        for item in group:
            yield item
    longest_iterable = max(iterables, key=len, default=[])
    for item in longest_iterable[len(min(iterables, key=len)):]:
        yield item


if __name__ == "__main__":
    res = interleave()
    print(list(res))
