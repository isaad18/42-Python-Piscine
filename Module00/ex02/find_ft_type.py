def all_thing_is_obj(object: any) -> int:
    switcher = {
        int: "int",
        float: "float",
        complex: "complex",
        bool: "bool",
        str: "str",
        list: "list",
        tuple: "tuple",
        set: "set",
        dict: "dict",
        type(None): "NoneType",
        map: "map",
    }
    return switcher.get(type(object), "function")
