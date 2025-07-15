def main():

    take = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    take = take.casefold().strip()
    if take.isnumeric():
        take = str(take)
    print(answer(take))

def answer(n):

    if n == "42":
        return "Yes"
    elif n == "forty-two":
        return "Yes"
    elif n == "forty two":
        return "Yes"
    else:
        return "No"

main()

