from load_image import ft_load


def test_v2():
    """Load and display image information."""
    ft_load("./landscape.jpg")
    print()
    print("-- invalid extension --")
    ft_load("./landscape.png")

    print("-- file not found --")
    ft_load("./missing.jpg")

    print("-- non-string path --")
    ft_load(42)


def main():
    print(ft_load("./landscape.jpg"))


if __name__ == "__main__":
    main()
    test_v2()
