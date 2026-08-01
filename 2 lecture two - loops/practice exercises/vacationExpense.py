'''
To build an interactive menu loop in Python that lets a user choose from a list of options, 
you use a while True loop paired with an input() statement and conditional if-elif-else structures. 
This is the industry standard for creating command-line interface (CLI) tools
'''




# In Python, functions need to be defined before they're called.
# define all functions outside of main, call them within main.
# that's the standard and recommended approach


# all functions will be able to modify/access both these things
trip = {}
expenses = []


def create_trip():

    trip["destination"] = input("Destination: ").strip()
    trip["days"] = int(input("Days: "))
    trip["budget"] = float(input("Budget: "))

    print (
    f"""
    Trip created successfully!

    Destination: {trip.get("destination")}
    Trip Length (days): {trip.get("days")}      
    Budget: ${trip.get("budget")}   
    """
    )

    return 



def add_expense():

    categories = ["flight", "accomodation", "food", "activities", "transport", "esim"]
    expense = {}



    for key, value in expense.items():


        '''
        How the below for loop works:
        enumerate(categories) pairs each item with an index.
        start=1 makes the numbering begin at 1 instead of Python's default of 0.
        f"{number}. {category}" formats the output nicely.

        Since you're starting to structure programs more cleanly, 
        enumerate() is the standard Pythonic way to print numbered lists. It's something you'll use often.
        '''
        for number, category in enumerate(categories, start=1):
            print(f"{number}. {category}")

            category_choice = input("Choose expense category: ")
            if category_choice in categories:
                expense["category"] = choice
            elif category_choice not in categories:
                print("Invalid category! Please choose from list")
            else: 
                continue


        
        description = input("Enter description: ")
        expense.update["Description": description]


        amount = float(input("Enter amount: "))
        expense.update["Amount": amount]


        for key, value in expense.items():
            print(key, value)




    





def display_menu():
    # 1. Define the available options in a list
    menu_options = ["1", "2", "3", "4", "5", "6"]

    # 2. Start an infinite loop to keep the menu active
    while True:
        print("=== Vacation Expense Tracker ===\n\n")
        print("1. Create Trip")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. View Budget Status")
        print("5. View Spending by Category")
        print("6. Exit")


        # 3. Capture and process user input 
        # The .strip() function acts as a safety barrier against accidental typos. 
        # It trims blank spacing prefixes or suffixes if a user keys in a space bar alongside their numeric choice.
        choice = input("\nEnter your choice: ").strip()


        # 4. Route choice to the correct action 
        if choice not in menu_options:
            print("Invalid selection! Please enter 1, 2, 3, 4, 5, or 6.")
            continue

        if choice == "1":
            create_trip()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_expenses()
        elif choice == "4":
            view_total_spending()
        elif choice == "5":
            view_category_summary()
        elif choice == "6":
            break






def main():

    display_menu()



main()