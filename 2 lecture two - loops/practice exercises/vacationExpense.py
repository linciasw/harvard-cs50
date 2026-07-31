'''
To build an interactive menu loop in Python that lets a user choose from a list of options, 
you use a while True loop paired with an input() statement and conditional if-elif-else structures. 
This is the industry standard for creating command-line interface (CLI) tools
'''

# In Python, functions need to be defined before they're called.
# define all fnctions outside of main, call them within main.
# that's the standard and recommended approach


def create_trip():
    destination = ""
    days = 0
    budget = 0

    destination = input("Destination: ").lower()
    days = int(input("Days: "))
    budget = float(int("Budget: "))











def main_menu():
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
        elif choice == "0":
            break






def main():

    main_menu()


main()