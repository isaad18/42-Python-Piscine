import sys
from ft_string import ft_string
from ft_string import string_info


def get_string_info(text: str) -> string_info:
    """
    Analyze the input text and count different types of characters.

    Parameters:
        text (str): The string to analyze.

    Returns:
        string_info: An object containing counts of uppercase letters,
                     lowercase letters, digits, punctuation, and whitespace.
    """
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


def main(*args):
    """
    Read input from command line arguments or standard input,
    analyze the text using get_string_info, and print character counts.

    Parameters:
        args: Optional command line arguments (ignored in this version).

    Returns:
        None
    """
    text: str = ""
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    text = "\n".join(lines)
    string_info = get_string_info(text)
    print(f"{string_info.uppercase} upper letters")
    print(f"{string_info.lowercase} lower letters")
    print(f"{string_info.punctuation} punctuation marks")
    print(f"{string_info.whitespace} spaces")
    print(f"{string_info.digits} digits")


if __name__ == "__main__":
    main(*sys.argv[1:])
