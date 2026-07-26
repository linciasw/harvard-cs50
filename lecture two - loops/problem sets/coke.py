'''
In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, 
each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
'''


'''
Use a while loop when you don't know how many repetitions.
Use a for loop when you know the number of repetitions.
In the problem below, we don't know how much coins the user
would enter. It could be 2 25cents, 10 5 cents etc. 
A while loop doesn't run a fixed number of times—it keeps checking a condition.
continue means:
"Stop this current loop iteration right now and go back to the top of the loop."
but it's not necessary here. 
the while loop runs until the end of the indentation and goes back to the top to
check if price > 0 in all instances
'''



def main():
    price = 50

    while price > 0:
        print(f"Amount due: {price}")
        coin = int(input("Insert coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            price = price - coin
        # else:
        #     continue

    print("Change owed: 0")


main()