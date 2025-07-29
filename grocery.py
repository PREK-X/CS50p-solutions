grocery = {
    
}

def main():

    while True:

        try:

            items = input()
            if items not in grocery:
                grocery[items] = 1
            elif items in grocery:
                grocery[items] += 1

        except EOFError:

            for item in sorted(grocery):
                print(grocery[item],item.upper())

            break

main()
