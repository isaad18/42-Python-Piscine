def filterstring(text: str, nb: int):
    if len(text) > nb:
        yield text
