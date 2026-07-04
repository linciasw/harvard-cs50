text = input("Enter text: ")

result = "...".join(text.split()) 


# alternative way of writing this 
"""
words = text.split()
result = "...".join(words)
"""

print(result)
# parentheses gets done first 
# so the text will get split into [this, is, CS50]
# that gets passed to "...".join



# JOIN()
# join() takes a collection of strings (usually a list or tuple)
# and combines them into a single string, placing the string before .join() between each item.
# syntax is 'separator.join(iterable)'



# example code
"""
fruits = ["apple", "banana", "orange"]

print(", ".join(fruits))
"""
# output: apple, banana, orange



