def ft_filter(_function_, iterable):
    """
    Custom implementation of Python's built-in filter function.

    Parameters:
        _function_ (callable or None): A function that takes an item and
        returns True or False.
        If None, all truthy items are kept.
        iterable (iterable): An iterable of items to filter.

    Yields:
        item: Each item from the iterable that satisfies the filter condition.
    """
    for item in iterable:
        if _function_(item) if _function_ is not None else item:
            yield item
