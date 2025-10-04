import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        times = re.split(r" to ", s)
        time1 = times[0]
        time2 = times[1]

    except IndexError:

        raise ValueError

    match1 = re.search(
        r"^(?P<hour>[1][0-2]|[1-9])(:(?P<minutes>\d|[0]\d|[1-5]\d))? (?P<format>AM|PM)$",
        time1,
    )
    match2 = re.search(
        r"^(?P<hour>[1][0-2]|[1-9])(:(?P<minutes>\d|[0]\d|[1-5]\d))? (?P<format>AM|PM)$",
        time2,
    )

    if match1 and match2:

        hour1 = match1.group("hour")
        hour2 = match2.group("hour")

        minutes1 = match1.group("minutes")
        minutes2 = match2.group("minutes")

        format1 = match1.group("format")
        format2 = match2.group("format")

        if format1 == "AM" and format2 == "AM":
            if hour1 == "12":
                hour1 = 0
            else:
                hour1 = int(hour1)
            if hour2 == "12":
                hour2 = 0
            else:
                hour2 = int(hour2)

        elif format1 == "AM" and format2 == "PM":
            if hour1 == "12":
                hour1 = 0
            else:
                hour1 = int(hour1)
            if hour2 == "12":
                hour2 = 12
            else:
                hour2 = int(hour2) + 12

        elif format1 == "PM" and format2 == "AM":
            if hour1 == "12":
                hour1 = 12
            else:
                hour1 = int(hour1) + 12
            if hour2 == "12":
                hour2 = 0
            else:
                hour2 = int(hour2)

        else:
            if hour1 == "12":
                hour1 = 12
            else:
                hour1 = int(hour1) + 12
            if hour2 == "12":
                hour2 = 12
            else:
                hour2 = int(hour2) + 12

        if minutes1 == None:
            minutes1 = 0
        if minutes2 == None:
            minutes2 = 0

        return f"{hour1:02}:{minutes1:02} to {hour2:02}:{minutes2:02}"

    else:
        raise ValueError("Wrong Format!")


if __name__ == "__main__":
    main()
