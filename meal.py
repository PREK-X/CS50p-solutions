def main():

    time = input("Enter the time: ")
    newtime = convert(time)

    if 7.00 <= newtime <= 8.00:
         print("breakfast time")
    elif 12.00 <= newtime <= 13.00:
        print("lunch time")
    elif 18.00 <= newtime <= 19.00:
        print("dinner time")
    else:
        print("Enter valid time")


def convert(time):

    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes/60
    time = hours + minutes
    time = float(time)
    return time

if __name__ == "__main__":
    main()
