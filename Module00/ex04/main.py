import sys
from whatis import what_is


def perform_check(args) -> bool:
    try:
        assert not len(args) == 0
    except AssertionError:
        print("AssertionError: argument is not present")
        return False

    try:
        assert not len(args) > 1
    except AssertionError:
        print("AssertionError: more than one argument is provided")
        return False

    return True


def main(*args):
    if not perform_check(args):
        return

    try:
        print(what_is(int(args[0])))
    except (IndexError, ValueError):
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    main(*sys.argv[1:])
