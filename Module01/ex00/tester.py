from give_bmi import give_bmi, apply_limit


def test_v2():
    """Demonstrate BMI calculation with example data from the subject."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    print()
    # Error cases
    print("-- height=0 --")
    print(give_bmi([0, 1.15], [165.3, 38.4]))

    print("-- different lengths --")
    print(give_bmi([2.71], [165.3, 38.4]))

    print("-- invalid type in list --")
    print(give_bmi([2.71, "tall"], [165.3, 38.4]))

    print("-- not a list --")
    print(give_bmi("2.71", [165.3]))

    print("-- non-int limit --")
    print(apply_limit([22.5, 29.0], 26.5))


def main():
    """Demonstrate BMI calculation with example data from the subject."""
    height = [0, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    print("\n")

    height = [2.71]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    print("\n")

    height = [2.71]
    weight = []
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    print("\n")

    height = [2.71, 88]
    weight = [(165.3, 38.4), 99]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
    test_v2()
