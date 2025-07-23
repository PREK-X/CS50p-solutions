def main():

    name = input("Enter the name in camel case: ")

    snake_name = ""

    for letter in name:

        if letter.isupper():

            snake_name += "_" + letter.casefold()

        else:

            snake_name += letter

    print(snake_name)



main()
