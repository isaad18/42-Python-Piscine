from ex01.format_ft_time import formatTime

if __name__ == "__main__":
    formatString = "%Y-%m-%d %H:%M:%S"
    currentTimeString = "2022-10-21 12:00:00"
    pastDateString = "1970-01-01 12:00:00"

    currentTimeInfo = formatTime(currentTimeString, formatString)
    pastDateInfo = formatTime(pastDateString, formatString)

    timeSincePastSeconds = currentTimeInfo.seconds - pastDateInfo.seconds

    print(
        f"Seconds since {pastDateInfo.formattedDate}: "
        f"{timeSincePastSeconds} or "
        f"{"{:e}".format(timeSincePastSeconds)} in scientific notation"
    )
    print(currentTimeInfo.formattedDate)
