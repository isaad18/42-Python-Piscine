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


if __name__ == "__main__":
    formatString = "%Y-%m-%d %H:%M:%S"
    currentTimeString = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    pastDateString = "1970-01-01 12:00:00"

    currentTimeInfo = formatTime(currentTimeString, formatString)
    pastDateInfo = formatTime(pastDateString, formatString)

    timeSincePastSeconds = currentTimeInfo.seconds - pastDateInfo.seconds

    print(
        f"Seconds since {pastDateInfo.formattedDate}: "
        f"{timeSincePastSeconds} or "
        f"{'{:e}'.format(timeSincePastSeconds)} in scientific notation"
    )
    print(currentTimeInfo.formattedDate)
