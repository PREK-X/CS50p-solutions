import random


def main():
    level = get_level()
    i = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        try:
            ans = int(input(f"{x} + {y} = "))
        except ValueError:
            continue
        else:
            if ans == x + y:
                i += 1
                continue
            else:
                print("EEE")
                for _ in range(2):
                    try:
                        ans = int(input(f"{x} + {y} = "))
                    except ValueError:
                        continue
                    else:
                        if ans == x + y:
                            i += 1
                            break
                        else:
                            print("EEE")
                            continue
                print(f"{x} + {y} = {x + y}")
    print(i)


def get_level():
    while True:
        try:
            level = int(input())
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)

    elif level == 2:
        return random.randint(10, 99)

    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid Level")


if __name__ == "__main__":
    main()
