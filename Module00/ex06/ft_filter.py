def ft_filter(_function_, iterable):
    for item in iterable:
        if _function_(item) if _function_ is not None else item:
            yield item
