import inflect
import sys
from datetime import date

p = inflect.engine()

class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

def main():

    time = input("Date of Birth: ")
    print(get_time(time))


def get_time(s1):

    get_date = s1

    try:
        year, month, day = get_date.split("-")
    except ValueError:
        sys.exit("Wrong Format!")

    year = int(year)
    month = int(month)
    day = int(day)

    d = Date(year, month, day)
    d1 = date(d.year, d.month, d.day)
    d2 = date.today()
    
    d3 = d2 - d1
    d3 = d3.days * 24 * 60

    return f"{p.number_to_words(d3, andword = "").capitalize()} minutes"

if __name__ == "__main__":
    main()
