import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):

    return bool(re.fullmatch(r"(?:(?:[1-9]?\d|1\d\d|2[0-4]\d|2[5][0-5])\.){3}(?:[1-9]?\d|1\d\d|2[0-4]\d|2[5][0-5])", ip))

if __name__ == "__main__":
    main()
