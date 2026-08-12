'''
In a file called taqueria.py, implement a program that enables a user to place an order, 
prompting them for items, one per line, until the user inputs control-d 
(which is a common way of ending one’s input to a program). 
After each inputted item, display the total cost of all items inputted thus far, 
prefixed with a dollar sign ($) and formatted to two decimal places. 
Treat the user’s input case insensitively. Ignore any input that isn’t an item. 
Assume that every item on the menu will be titlecased.
'''


def main():
    food = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
    }


    count = 0

    while True:
        choice = input("Item: ")

        for item, price in food.items():
            if choice == item:
                count += price
                print(count)
            else:
                pass



main()



"""
Taqueria Order Program — Review Notes

This program uses a dictionary to store menu items as keys and their
prices as values. The user's input is compared against the dictionary's
keys to determine whether the item exists.

Important concept:
Checking whether an item exists with:

```
    if item in food:

checks the dictionary's keys by default. It does NOT attempt to
access a value, so this type of check does not raise a KeyError.
```

A KeyError happens when you try to access a dictionary key that does
not exist, for example:

```
food[item]

if item is not a key in food, Python raises KeyError.
```

This program avoids that problem because it first checks whether the
user's input is a valid key before using it.

General lesson:
Not every possible error needs to be handled with try/except.
If the program can be designed so that an exception is never
triggered, that can be simpler and clearer.

The important distinction is:

```
- `item in food` → checks whether the key exists.
- `food[item]` → retrieves the value associated with the key and
  can raise KeyError if the key does not exist.
```

This is an example of preventing an error through program logic rather
than catching the error after it happens.
"""