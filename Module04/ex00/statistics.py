from typing import Any


def parse_input(*args: Any) -> bool:
    """Return True if args is non-empty and every element is int or float."""
    if not args:
        return False
    for item in args:
        if not isinstance(item, (int, float)):
            return False
    return True


def ft_mean(*args: Any) -> str:
    """Return the arithmetic mean of args as a string, or 'ERROR' on bad input.
    """
    if not parse_input(*args):
        return "ERROR"
    return str(sum(args) / len(args))


def ft_median(*args: Any) -> str:
    """Return the median of args as a string, or 'ERROR' on bad input."""
    if not parse_input(*args):
        return "ERROR"
    sorted_args = sorted(args)
    n = len(sorted_args)
    mid = n // 2
    if n % 2 == 0:
        return str((sorted_args[mid - 1] + sorted_args[mid]) / 2)
    else:
        return str(sorted_args[mid])


def ft_quartile(*args: Any) -> str:
    """Return [Q1, Q3] of args as a string, or 'ERROR' on bad input."""
    if not parse_input(*args):
        return "ERROR"
    sorted_args = sorted(args)
    n = len(sorted_args)
    q1 = sorted_args[n // 4]
    q3 = sorted_args[3 * n // 4]
    return f"[{q1}, {q3}]"


def ft_standard_deviation(*args: Any) -> str:
    """Return the population standard deviation of args as a string, or
    'ERROR'.
    """
    if not parse_input(*args):
        return "ERROR"
    mean = sum(args) / len(args)
    variance = sum((x - mean) ** 2 for x in args) / len(args)
    return str(variance ** 0.5)


def ft_variance(*args: Any) -> str:
    """Return the population variance of args as a string, or 'ERROR' on bad
    input.
    """
    if not parse_input(*args):
        return "ERROR"
    mean = sum(args) / len(args)
    variance = sum((x - mean) ** 2 for x in args) / len(args)
    return str(variance)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Print requested statistics for the given numeric arguments.

    Each value in kwargs must be one of: 'mean', 'median', 'quartile', 'std',
    'var'.
    The key names are arbitrary; only the values are used as stat selectors.
    Unknown stat names are silently ignored.
    If args contains no values or any non-numeric value, each stat prints
    'ERROR'.

    Args:
        args: Numeric values (int or float) to compute statistics on.
        kwargs: Arbitrary keys mapping to stat names ('mean', 'median',
                  'quartile', 'std', 'var').

    Returns:
        None
    """
    result = {
        "mean": ft_mean,
        "median": ft_median,
        "quartile": ft_quartile,
        "std": ft_standard_deviation,
        "var": ft_variance
    }

    for command in kwargs.values():
        if command in result.keys():
            print(f"{command}: {result[command](*args)}")
