"""
i want to do a for loop and its list comprehension in python to implement a program that 
prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
Assume that the user’s input will indeed be in camel case.
"""



"""
Logic:
Input: preferredFirstName

Start with an empty result.
Read each letter.
If the letter is lowercase:
    add it to the result.

If the letter is uppercase:
    add an underscore.
    add the lowercase version of the letter.

Print the result.
"""


"""
One more observation: when you're stuck, your instinct is often to ask:
"What's the code?"
A better question is:
"What should happen to one character at a time?"
Programming is mostly solving tiny problems repeatedly.

For this challenge, the real insight wasn't Python syntax. It was realizing:
When I see an uppercase letter,
replace it with:
    "_" + lowercase version

"""

# FOR LOOP
def main():
    camel = input("camelCase: ")

    snake = ""

    for letter in camel:
        if letter.isupper():
            # snake = snake + "_" + letter.lower()
            snake += "_" + letter.lower()
        else:
            # snake = snake + letter
            snake += letter

    print("snake_case:", snake)


main()



# USING A LIST + JOIN
# this is the decomposed list comprehension seen below
def main():
    camel = input("camelCase: ")

    snake = []

    for letter in camel:
        if letter.isupper():
            snake.append("_")
            snake.append(letter.lower())
        else:
            snake.append(letter)

    print("snake_case:", "".join(snake))


main()




# LIST COMPREHENSION
def main():
    camel = input("camelCase: ")

    snake = "".join(
        ["_" + letter.lower() if letter.isupper() else letter for letter in camel]
    )

    print("snake_case:", snake)

main()



