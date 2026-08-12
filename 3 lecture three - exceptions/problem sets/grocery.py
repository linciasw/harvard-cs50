'''
In a file called grocery.py, implement a program that prompts the user for items, one per line, 
until the user inputs control-d (which is a common way of ending one’s input to a program). 
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, 
prefixing each line with the number of times the user inputted that item. No need to pluralize the items. 
Treat the user’s input case-insensitively.
'''


def main():

    grocery_items = {}
    count = 1

    while True:
        try:
            item = input("Grocery list item: ")
        except EOFError:
            ("End of list")
            print(grocery_items)
            break

        if item not in grocery_items:
            grocery_items[item] = count
        elif item in grocery_items:
            grocery_items[item] += count
        else:
            pass
            

    # format output
    # research how to use sorted
    # think about where to put keyError



main()