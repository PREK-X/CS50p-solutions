def main():

    expression = input("Expression: ")
    result = func(expression)
    print(f"{float(result):.1f}")

def func(expression):

    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z
    else:
        return"Enetr a valid Expression"


main()
