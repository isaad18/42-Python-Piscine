from typing import Any


def callLimit(limit: int):
    """
    Decorator factory that restricts a function to at most `limit` calls.

    Returns a decorator. Each decorated function gets its own independent
    call counter. Once the limit is exceeded, calls print an error message
    and do not execute the function.

    Args:
        limit: Maximum number of times the decorated function may be called.

    Returns:
        A decorator that enforces the call limit.
    """
    def callLimiter(function):
        count = 0

        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: <function {function.__name__}"
                      f" at {hex(id(function))}> call too many times")
                return

            return function(*args, **kwds)

        return limit_function

    return callLimiter
