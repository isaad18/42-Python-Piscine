import sys
from building import get_string_info


def main(*args):
    text: str = ""
    if len(args) != 1:
        while 1:
            try:
                text = input()
                text += "\n"
            except EOFError:
                break
    else:
        text = args[0]
    string_info = get_string_info(text)
    print(f"{string_info.uppercase} upper letters")
    print(f"{string_info.lowercase} lower letters")
    print(f"{string_info.punctuation} punctuation marks")
    print(f"{string_info.whitespace} spaces")
    print(f"{string_info.digits} digits")


if __name__ == "__main__":
    main(*sys.argv[1:])
