def main():

    lower_case = input("Input: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_c = ['A', 'E', 'I', 'O', 'U']

    for letter in lower_case:

        if letter in vowels or letter in vowels_c:

            lower_case = lower_case.replace(letter, "")

    print(lower_case)

main()
