import re

def main():
    print(count(input("Text: ")))

def count(s):
    i = 0

    pattern = r"\bum\b"

    match = re.findall(pattern, s, re.IGNORECASE)

    for words in match:
        i += 1
    return i


if __name__ == "__main__":
    main()
