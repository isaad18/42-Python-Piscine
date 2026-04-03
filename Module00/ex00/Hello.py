"""
Hello.py

This file contains functions to edit lists, tuples, sets, and dictionaries.

Functions:
    - editList(list: list[str], newValue: str): Edits a list by removing the
    last element and appending a new value.
    - editTuple(tuple: tuple[str], newValue: str) -> tuple[str]: Edits a tuple
    by replacing the last element with a new value.
    - editSet(set: set[str], toChange: str, newValue: str): Edits a set by
    removing an existing value and adding a new one.
    - editDict(dict: dict[str, str], toChange: str, newValue: str): Edits a
    dictionary by changing the value associated with a key.

"""


def editList(list: list[str], newValue: str):
    """
    Edits a list by removing the last element and appending a new value.

    Args:
        list (list[str]): The list to be edited.
        newValue (str): The new value to be appended.

    Returns:
        None
    """
    list.pop()
    list.append(newValue)


def editTuple(tuple: tuple[str], newValue: str) -> tuple[str]:
    """
    Edits a tuple by replacing the last element with a new value.

    Args:
        tuple (tuple[str]): The tuple to be edited.
        newValue (str): The new value to replace the last element.

    Returns:
        tuple[str]: The edited tuple.
    """
    tuple = (*(tuple[:-1]), newValue)
    return tuple


def editSet(set: set[str], toChange: str, newValue: str):
    """
    Edits a set by removing an existing value and adding a new one.

    Args:
        set (set[str]): The set to be edited.
        toChange (str): The value to be removed.
        newValue (str): The new value to be added.

    Returns:
        None
    """
    set.remove(toChange)
    set.add(newValue)


def editDict(dict: dict[str, str], toChange: str, newValue: str):
    """
    Edits a dictionary by changing the value associated with a key.

    Args:
        dict (dict[str, str]): The dictionary to be edited.
        toChange (str): The key whose value is to be changed.
        newValue (str): The new value for the specified key.

    Returns:
        None
    """
    dict[toChange] = newValue


def main():
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    editList(ft_list, "World!")
    print(f"List {ft_list}")

    ft_tuple = editTuple(ft_tuple, "UAE!")
    print(f"Tuple {ft_tuple}")

    editSet(ft_set, "tutu!", "Abu Dhabi!")
    print(f"Set {ft_set}")

    editDict(ft_dict, "Hello", "42 Abu Dhabi!")
    print(f"Dict {ft_dict}")


if __name__ == "__main__":
    main()
