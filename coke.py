def main():

    coke_price = 50
    due_amount = 0
    owed_amount = 0

    while True:

        amount = int(input("Insert coin: "))

        if amount ==  25 or  amount == 10 or amount == 5:

            due_amount = coke_price - amount
            coke_price = coke_price - amount

            if due_amount > 0:

                print("Amount Due:", due_amount)

            elif due_amount < 0:

                owed_amount = 0 - due_amount

                print("Change Owed:", owed_amount)

                break

            else:

                print("Amount Due:", due_amount)

                print("Change Owed:", owed_amount)

                break

        else:

            print("Amount Due:", coke_price)

main()
