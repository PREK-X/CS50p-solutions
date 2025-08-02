import emoji


def main():

    take = input("Input: ")
    print(emoji.emojize(take, language = "alias"))

main()
