months= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():

    while True:

        try:
            date = input("Date: ")
            month, day, year = date.strip().split("/")
            day = int(day)
        except ValueError:
            try:
                month, day, year = date.split(" ")
                if "," not in day:
                    raise ValueError
                org_day = day.replace(",", "")
                org_day = int(org_day)
                try:
                    if month in months and org_day < 32:
                        print(f"{year}-{months.index(month)+1:02}-{org_day:02}")
                        break
                except TypeError:
                    pass
                else:
                    continue
            except ValueError:
                pass
        else:
            try:
                month = int(month)
                if month < 13 and day < 32:
                    print(f"{year}-{month:02}-{day:02}")
                    break
            except TypeError and ValueError:
                pass


main()
