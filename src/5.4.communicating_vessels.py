"""
Module for interleaving items from multiple iterables.
This module provides two functions for interleaving:
- `generator_interleave`: A generator that interleaves items from multiple iterables.
- `interleave`: Interleaves items from multiple iterables and handles cases where the iterables are of unequal lengths.
"""


def generator_interleave(*iterables):
    """
    Interleave items from multiple iterables using a generator.

    This function takes multiple iterables as input and yields one item at a time from each iterable
    in round-robin fashion. The function continues until all iterables are exhausted.

    Args:
    - *iterables (iterable): Multiple iterables to be interleaved.

    Yields:
    - Each item from the iterables, interleaved in the order they are provided.
    """
    for group in zip(*iterables):
        yield from group


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
    min_len = min(map(len, iterables), default=0)
    for group in zip(*iterables):
        yield from group
    for iterable in iterables:
        yield from iterable[min_len:]


if __name__ == "__main__":
    res = interleave()
    print(list(res))
