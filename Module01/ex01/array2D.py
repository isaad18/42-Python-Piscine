import numpy as np


def validate_input(family: list, start: int, end: int) -> bool:
    """
    Validate the input for the slice_me function.

    Args:
        family: 2D list where all rows are lists of equal length
        start: start index for slicing (must be int)
        end: end index for slicing (must be int)
    Returns:
        True if inputs are valid, False otherwise
    """
    if not isinstance(family, list):
        print("Error: family must be a list.")
        return False
    if not family:
        print("Error: family list cannot be empty.")
        return False
    if not isinstance(start, int) or not isinstance(end, int):
        print("Error: start and end must be integers.")
        return False
    if not isinstance(family[0], list):
        print("Error: family must be a 2D list (list of lists).")
        return False
    return True


def slice_me(family: list, start: int, end: int) -> list:
    """
    Print the shape of a 2D list and return a sliced version.

    Args:
        family: 2D list where all rows are lists of equal length
        start: start index for slicing (must be int)
        end: end index for slicing (must be int)

    Returns:
        sliced 2D list, or empty list on error
    """
    if not validate_input(family, start, end):
        return []
    row_len = len(family[0])
    for member in family:
        if not isinstance(member, list) or len(member) != row_len:
            print("Error: all rows must be lists of the same length.")
            return []
    np_family = np.array(family)
    print(f"My shape is : {np_family.shape}")
    new_family = np_family[start:end]
    print(f"My new shape is : {new_family.shape}")
    return new_family.tolist()
