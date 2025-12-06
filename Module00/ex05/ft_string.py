class ft_string:
    whitespace = ' \t\n\r\v\f'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_letters = ascii_lowercase + ascii_uppercase
    digits = '0123456789'
    hexdigits = digits + 'abcdef' + 'ABCDEF'
    octdigits = '01234567'
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    printable = digits + ascii_letters + punctuation + whitespace


class string_info:
    whitespace = 0
    lowercase = 0
    uppercase = 0
    letters = 0
    digits = 0
    hexdigits = 0
    octdigits = 0
    punctuation = 0
    printable = 0
