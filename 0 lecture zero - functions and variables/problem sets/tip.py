

# the replace method
# syntax:
# string.replace(oldvalue, newvalue, count)
# Parameter	Description
# oldvalue	Required. The string to search for
# newvalue	Required. The string to replace the old value with
# count	Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences

# don't forget: 
# strings are immutable
# you need to create a new variable to store change


# this is a common pattern in Python programs that accept currency input



def main():
    dollars = dollars_to_float(input("How much was the meal? Enter format $00.00 "))
    percent = percent_to_float(input("What percentage would you like to tip? Enter format 00% "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$", "")
    return float(d)


def percent_to_float(p):
    p = p.replace("%", "")
    return float(p) / 100


main()