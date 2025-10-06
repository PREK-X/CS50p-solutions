from validator_collection import validators # pyright: ignore[reportMissingImports]

def main():

    print(is_email(input("Enter Your Email: ")))

def is_email(s):
    try:
        result = validators.email(s)
    except ValueError:
        return "Invalid"
    if result:
        return "Valid"


if __name__ == "__main__":
    main()
