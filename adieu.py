import inflect

p = inflect.engine()
name_list = []


def main():

    while True:
        try:
            name = input("name: ")
            name_list.append(name)
        except EOFError:
            new_list = p.join((name_list))
            print("Adieu, adieu, to " + new_list)
            break


main()
