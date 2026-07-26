'''
In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, 
each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
'''




def main():
    price = 50

    while price > 0:
        print(f"Amount due: {price}")
        coin = int(input(f"Insert coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            price = price - coin
        else:
            continue

    print("Change owed: 0")





    # while price > 0:
    #     coin = int(input("Insert Coin: "))
    #     change = price - coin
    #     amount_due = 0


    #     if coin == 25 or coin == 10 or coin == 5:
    #         amount_due = price - change
    #         print(f"Amount due: {amount_due}")
    #         price = price - amount_due
    #         print(price)
    #     else:
    #         continue


            

        # if amount_due > 0:
        #     change = price - change
        #     print(f"Amount due: {change}")
        # else:
        #     print("Changed owed: 0")





        # if coin == 25 and change == 25:
        #     print(f"Change due: {change}")
        # elif coin == 10 and change == 40:
        #     print(f"Change due: {change}")
        # elif coin == 5 and change == 45:
        #     print(f"Change due: {change}")
        # elif coin 
        # else:
        #     change = 0
        #     print("Change owed: 0")


main()