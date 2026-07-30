# LISTS METHODS
# FROM CS50 SHORTS
# append(), pop(), clear()

# append(): to add items to the end of a list
# pop(); to remove last element of the list, you can store in a variable
# clear(): to clear all items in list


def main():
    history = []


    while True:
        action = input("Action: ")

        if action == "Undo":
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "Restart":
            history.clear()
        else:
            history.append(action)
    
        print(history)


main()