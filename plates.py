def main():

    take = input("plate: ")

    if is_valid(take):

        print("Valid")

    else:

        print("Invalid")


def is_valid(s):

    first_digit = False

    if not s[0:2].isalpha():

        return False

    if not (len(s) > 1 and len(s) < 7):

        return False

    if not s.isalnum():

        return False

    for letter in s[2:]:

        if letter.isdigit():

            if letter == "0":

                return False

            break

    for letter in s[2:]:

        if letter.isdigit():

            first_digit = True

        elif letter.isalpha() and first_digit == True:

            return False

    return True

main()
