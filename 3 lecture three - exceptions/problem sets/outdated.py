'''
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, 
which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. 
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). 
Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, 
no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, 
formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


NOTES:
- a delimiter is just some character that you put between different items to separate them
- pass statement does absolutely nothing, just acts as a placeholder 

'''



# help(str.split)



def main():
        
        months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]


        while True:
            
                date = input("Date: ")

                try:

                    if "/" in date:
                        
                        month, day, year = date.split("/")

                        month = int(month)
                        day = int(day)
                        year = int(year)


                        if 1 <= month <= 12 and 1 <= day <= 31:
                            print(f"{year}/{month:02}/{day:02}")
                            break


                    elif "," in date:

                        replacement = date.replace(",", "")

                        month, day, year = replacement.split(maxsplit=2)

                        if month in months:

                            new_month = months.index(month) + 1
                            day = int(day)
                            year = int(year)


                            if 1 <= day <= 31:
                                pass
                            print(f"{year}/{new_month:02}/{day:>02}")
                            break

                        elif month not in months:
                            pass
                        else:
                            break

                except ValueError:
                     print("Invalid values!")




main()



"""
PYTHON DOCUMENTATION NOTES
str.split(sep=None, maxsplit=-1) -> list[str]

Return a list of the words in the string, using `sep` as the delimiter.

## Parameters

sep : str | None, optional
The delimiter used to split the string.

```
If `sep` is None (the default):
    - Splits on whitespace.
    - Consecutive whitespace is treated as one separator.
    - Leading and trailing whitespace is ignored.
    - Whitespace includes spaces, tabs, and newlines.

If `sep` is a string:
    - Splits strictly at each occurrence of that string.
    - Consecutive delimiters produce empty strings (`''`).
```

maxsplit : int, optional
The maximum number of splits to perform.

```
- `-1` (default): No limit; split the entire string.
- `0`: No splits are performed.
- Positive integer `N`: Perform at most `N` splits.
  The remaining text becomes the final element.
```

## Returns

list[str]
A list containing the resulting substrings.

## Examples

Default behavior:

```
>>> "   Python    is   fun   ".split()
['Python', 'is', 'fun']
```

Using a specific delimiter:

```
>>> "apple,,banana,cherry".split(",")
['apple', '', 'banana', 'cherry']
```

Limiting the number of splits:

```
>>> "2026-08-13 ERROR Failed to connect to database".split(maxsplit=2)
['2026-08-13', 'ERROR', 'Failed to connect to database']
```

Using a delimiter with maxsplit:

```
>>> "name:John Smith".split(":", maxsplit=1)
['name', 'John Smith']
```

## Notes

`split()` and `split(" ")` behave differently.

```
>>> "Python    is    fun".split()
['Python', 'is', 'fun']

>>> "Python    is    fun".split(" ")
['Python', '', '', '', 'is', '', '', '', 'fun']
```

`split()` with no argument handles all whitespace, while
`split(" ")` splits only on literal space characters.

General rule:

```
maxsplit = N
maximum number of resulting elements = N + 1
```

"""
