def validate_inputs(
    height: list[int | float],
    weight: list[int | float],
) -> bool:
    """
    Validate the input lists for height and weight.

    Args:
        height: list of heights in meters (int or float)
        weight: list of weights in kilograms (int or float)
    Returns:
        True if inputs are valid, False otherwise
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        print("Error: height and weight must be lists.")
        return False
    if not height or not weight:
        print("Error: height and weight lists cannot be empty.")
        return False
    if len(height) != len(weight):
        print("Error: lists must have the same length.")
        return False
    for item in height:
        if not isinstance(item, (int, float)):
            print("Error: height must contain only int or float values.")
            return False
    for item in weight:
        if not isinstance(item, (int, float)):
            print("Error: weight must contain only int or float values.")
            return False
    return True


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """
    Calculate BMI values from lists of heights and weights.

    Args:
        height: list of heights in meters (int or float)
        weight: list of weights in kilograms (int or float)

    Returns:
        list of BMI values, or empty list on error
    """
    if not validate_inputs(height, weight):
        return []
    bmi_list = []
    for h, w in zip(height, weight):
        if h == 0:
            print("Error: height cannot be zero.")
            return []
        bmi_list.append(w / (h ** 2))
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return booleans indicating which BMI values exceed the limit.

    Args:
        bmi: list of BMI values (int or float)
        limit: integer threshold to compare against

    Returns:
        list of booleans: True if BMI > limit, else False
    """
    if not isinstance(bmi, list):
        print("Error: bmi must be a list.")
        return []
    if not isinstance(limit, int):
        print("Error: limit must be an integer.")
        return []
    for item in bmi:
        if not isinstance(item, (int, float)):
            print("Error: bmi list must contain only int or float values.")
            return []
    return [x > limit for x in bmi]
