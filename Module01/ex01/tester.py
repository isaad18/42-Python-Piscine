from array2D import slice_me


def test_v2():
    """Demonstrate 2D array slicing with example data from the subject."""
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    print(slice_me(family, 0, 2))
    print()
    print(slice_me(family, 1, -2))

    print()
    print("-- not a list --")
    print(slice_me("not a list", 0, 2))

    print("-- empty list --")
    print(slice_me([], 0, 2))

    print("-- jagged rows --")
    print(slice_me([[1.80, 78.4], [2.15]], 0, 2))

    print("-- non-int start --")
    print(slice_me(family, 0.5, 2))


def main():
    """Demonstrate 2D array slicing with example data from the subject."""
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    print(slice_me(family, 0, 2))

    print("\n")

    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
    test_v2()
