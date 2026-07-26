def main():



    while True:
        coin = int(input("Insert Coin: "))
        price = 50
        change = 0

        if coin == 25 or coin == 10 or coin == 5:
            change = price - coin
        else:
            


        while change != 0:
            change = price - coin
            print(f"Change owed: {change}")









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