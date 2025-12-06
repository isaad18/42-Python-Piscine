from ft_string import ft_string
from ft_string import string_info


def get_string_info(text: str) -> string_info:
    info: string_info = string_info()
    for char in text:
        if char in ft_string.punctuation:
            info.punctuation += 1
        if char in ft_string.ascii_lowercase:
            info.lowercase += 1
        if char in ft_string.ascii_uppercase:
            info.uppercase += 1
        if char in ft_string.digits:
            info.digits += 1
        if char in ft_string.whitespace:
            info.whitespace += 1
    return info
