def all_thing_is_obj(object: any) -> int:
    type_map = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
    }

    obj_type = type(object)

    if obj_type in type_map:
        print(f"{type_map[obj_type]} : {obj_type}")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")
        return 42
