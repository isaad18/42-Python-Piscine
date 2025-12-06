import time


class TimeInfo:
    seconds: int
    formattedDate: str

    def __init__(self, seconds: int, formattedDate: str):
        self.seconds = seconds
        self.formattedDate = formattedDate


def formatTime(date: str, formatString: str):
    date = time.strptime(date, formatString)
    seconds = time.mktime(date)
    formattedDate = time.strftime("%B %d, %Y", date)
    return TimeInfo(seconds, formattedDate)
