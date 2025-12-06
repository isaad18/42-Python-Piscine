def isNan(value: float) -> bool:
    return value != value


def all_thing_is_obj(object: any) -> int:
    switcher = {
        int: "int",
        float: "float",
        bool: "bool",
        str: "str",
        type(None): "NoneType",
    }
    result = switcher.get(type(object), 1)
    return result


def NULL_not_found(object: any) -> int:
    objectType = all_thing_is_obj(object)
    if objectType == 1:
        print("Type not Found")
        return 1

    match objectType:
        case "NoneType" if object is None:
            print(f"Nothing: {object} <class 'NoneType'>")
        case "float" if isNan(object):
            print(f"Cheese: {object} <class 'float'>")
        case "int" if object == 0:
            print(f"Zero: {object} <class 'int'>")
        case "str" if object == "":
            print(f"Empty: {object} <class 'str'>")
        case "bool" if object is False:
            print(f"Fake: {object} <class 'bool'>")
        case _:
            print("Type not Found")
            return 1
    return 0
