import sys
from ft_filter import ft_filter


def main(*args):
    """
    Filter words from a string based on a minimum length provided as argument.

    Parameters:
        args: Command line arguments:
            args[0] (str): The text string containing words.
            args[1] (str): Minimum word length (must be a digit).

    Returns:
        None
    """
    try:
        text = args[0]
        assert args[1].isdigit()
        nb = int(args[1])
    except (AssertionError, IndexError):
        print("AssertionError: the arguments are bad.")
        return

    filtered = ft_filter(lambda x: len(x) >= nb, text.split())
    print(list(filtered))


if __name__ == "__main__":
    main(*sys.argv[1:])
