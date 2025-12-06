from find_ft_type import all_thing_is_obj

if __name__ == "__main__":
    print(all_thing_is_obj(42))                         # int
    print(all_thing_is_obj(3.14))                       # float
    print(all_thing_is_obj(2 + 3j))                     # complex
    print(all_thing_is_obj(True))                       # bool
    print(all_thing_is_obj("Hello"))                    # str
    print(all_thing_is_obj([1, 2, 3]))                  # list
    print(all_thing_is_obj((1, 2, 3)))                  # tuple
    print(all_thing_is_obj({1, 2, 3}))                  # set
    print(all_thing_is_obj({'a': 1}))                   # dict
    print(all_thing_is_obj(None))                       # NoneType
    print(all_thing_is_obj(lambda x: x))                # function
    print(all_thing_is_obj(map(str, ['a', 'b', 'c'])))  # map
