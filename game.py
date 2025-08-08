import random


def main():

    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level > 0:
                number = random.randint(1, level)
                break
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess == number:
                print("Just right!")
                break
            elif guess <= 0:
                pass
            elif guess > number:
                print("Too large!")
            else:
                print("Too small!")


main()
