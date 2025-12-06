from ft_filter import ft_filter
from filterstring import filterstring
import sys


def main(*args):
    try:
        text = args[0]
        assert args[1].isdigit()
        nb = int(args[1])
    except (AssertionError, IndexError):
        print("AssertionError: the arguments are bad.")
        return

    filtered = ft_filter(lambda x: filterstring(x, nb), text.split())
    print(list(filtered))


if __name__ == "__main__":
    main(*sys.argv[1:])
