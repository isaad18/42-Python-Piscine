def editList(list: list[str], newValue: str):
    list.pop()
    list.append(newValue)


def editTuple(tuple: tuple[str], newValue: str) -> tuple[str]:
    tuple = tuple[:-1] + (newValue,)
    return tuple


def editSet(set: set[str], toChange: str, newValue: str):
    set.remove(toChange)
    set.add(newValue)


def editDict(dict: dict[str, str], toChange: str, newValue: str):
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
