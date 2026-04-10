from typing import Callable


def square(x: int | float) -> int | float:
    """Return x squared."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return x raised to the power of x."""
    return x ** x


def outer(x: int | float, function: Callable) -> object:
    """
    Return a closure that repeatedly applies function to its own result.

    Each call to the returned inner function updates the stored value by
    applying function to it and returns the new value.

    Args:
        x: The initial value.
        function: A function that takes and returns a numeric value.

    Returns:
        A zero-argument callable that applies function to the accumulated
        value.
    """
    def inner() -> int | float:
        nonlocal x
        x = function(x)
        return x
    return inner
