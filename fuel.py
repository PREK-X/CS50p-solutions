def main():

    x = take_perc()
    check_con(x)

def take_perc():

    while True:
        try:
            num1, num2 = input("Fraction: ").split("/")
            num1 = int(num1)
            num2 = int(num2)
            if num1 < 0 or num2 < 0:
                continue
            if num2 >= num1:
                return round(num1/num2 * 100)
            else:
                continue
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def check_con(n):

    if n >= 99:
        print("F")
    elif n <= 1:
        print("E")
    else:
        print(n,"%", sep = "")

main()
