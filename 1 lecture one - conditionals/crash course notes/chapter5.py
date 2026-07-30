# CONDITIONAL TESTS 

"""
at the heart of every if statement is an expression that 
can be evaluated as True or False and is called a conditional 
test. python executes the code following the if statement if 
the conditional test evaluates to True. if the test evaluates to 
false, python ignores the code following the if statement. 
"""


"""
= versus ==
a single equal sign is really a statement; 
car = 'audi' reads as "set the value of car equal to audi"
on the other hand, 
car == 'bmw' asks a question: "Is the value of car equal to bmw?"
"""


"""
types of conditional tests:
- checking for equality 
- checking for inequality: !=
- numerical comparisons
- checking multiple conditions using and, or 
"""

# ignoring case when checking for equality
# testing for equality is case-sensitive
car = "Audi"
car == "audi"
# this returns false

# if case matters okay, but if case doesn't matter and instead,
# you just want to test the value of a variable, you can convert
# the variable's value to lowercase before doing the comparison:
car = "Audi"
car.lower() == "audi"
# this returns true
# what's happening is car.lower() becomes "audi" which is compared to
# the string "audi" so this will return true
# the car variable "Audi" remains unaffected 



# IF STATEMENTS

# several if statements exist, and your choice of which
# to use depends on the number of conditions you need 
# to test 
"""
- if-else: two possible situations
- if-elif-else: more than two possible situations
- multiple elifs
- omitting the else block 
- testing multiple conditions
"""




"""
OMITTING THE ELSE BLOCK
python does not require an else block at the end of an 
if-elif chain.
the else block is a catchall statement. it matches any condition
that wasn't matched by a specific if or elif test, and that can 
sometimes include invalid or even malicious data. 
"""


"""
TESTING MULTIPLE CONDITIONS
sometimes it's important to check all of the conditions of interest.
in this case, you should use a series of simple if statements with 
no elif or else blocks. this is when more than one conditions could be 
True, and you want to act on every condition that is True.
think of a pizzeria, if someone requests a 3-topping pizza, you'll 
have to include three toppings, not one. 
"""