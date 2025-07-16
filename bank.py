def main():

    greeting = input("Greeting: ").strip().casefold()
    print(func(greeting))

def func(greet):

    if greet.startswith("hello"):
        return "$0"
    elif greet.startswith("h"):
        return "$20"
    else:
        return "$100"

main()
