# function syntax 
the basic syntax for a python function definition:



```python
def name(parameter1, parameter2, ...)

    body
```


<br>
<br>


# docstrings
- the intention of docstrings is to describe the external behavior of a function and the parameter it takes, 
whereas comments should document internal information about how the code works
- you can get a docstring's value by:


```python 
function_name.__doc__
```

<br>




# parameter options
- positional parameters
- the simplest way to pass parameters to a function is by position ie the parameters used in the function call are matched to the function's parameter variables based on their order
- function parameters can have default values which remains as the default value unless you specify otherwise


<br>

## passing arguments by parameter name aka keyword passing
- if (x, y) are the parameters for a function, you can pass (y=2, x=3) and it'll work

```python
>>> power(2, 3)
8
>>> power(3, 2)
9
>>> power(y=2, x=3)
9
```

- you can combine keyword passing with default values to identify what you want from a function specifically
- if the default values are all set to False and you specify which ones you want by putting True when you call the function, the function will pull just those


<br>
<br>


## variable numbers of arguments
- if you use the * like (*numbers), you can send a list of items:
```python
>>> def maximum(*numbers):
... if len(numbers) == 0:
... return None
... else:
... maxnum = numbers[0]
... for n in numbers[1:]:
... if n > maxnum:
... maxnum = n
... return maxnum
...
```

<br>
Now, test out the behavior of the function:
```python
>>> maximum(3, 2, 8)
8
>>> maximum(1, 5, 9, -2, 2)
```

<br>
<br>

# procedures versus functions in python
- in other languages, a procedure is a function that doesn't return a value
- in python, if no explicit return is executed in the procedure body, the special python value None is returned
- nothing else in the function body is executed once a return has been executed 

<br>
<br>



# mutable objects as arguments 
- arguments are passed in by object reference to a function 
- the parameter that the function receives, becomes a new reference to the object 
- for immutable objects (such as tuples, strings, and numbers), what
is done with a parameter has no effect outside the function. But if you pass in a mutable object (for example, a list, dictionary, or class instance), any change made to the object will change what the argument is referencing outside the function


```python
>>> def f(n, list1, list2):
... list1.append(3)
... list2 = [4, 5, 6]
... n = n + 1
...
>>> x = 5
>>> y = [1, 2]
>>> z = [4, 5]
>>> f(x, y, z)
>>> x, y, z
(5, [1, 2, 3], [4, 5])
```


<br>
<br>



# local, nonlocal and global variables
- bottom line is that if you want to assign to a variable existing outside a function,
you must explicitly declare that variable to be nonlocal or global. But if you’re
accessing a variable that exists outside the function, you don’t need to declare it
nonlocal or global 
- if python can’t find a variable name in the local function scope, it
will attempt to look up the name in the global scope. Hence, accesses to global variables
will automatically be sent through to the correct global variable
- it's much clearer to a reader if all global variables are explicitly declared as global 
- also, limit the use of global variables withing functions to only rare occasions


<br>
<br>




# assigning functions to variables 
- functions can be assigned to variables

>>> def f_to_kelvin(degrees_f):
... return 273.15 + (degrees_f - 32) * 5 / 9
...
>>> def c_to_kelvin(degrees_c):
... return 273.15 + degrees_c
...
>>> abs_temperature = f_to_kelvin
>>> abs_temperature(32)
273.14999999999998
>>> abs_temperature = c_to_kelvin
>>> abs_temperature(0)
273.14999999999998


You can place them in lists, tuples, or dictionaries:
>>> t = {'FtoK': f_to_kelvin, 'CtoK': c_to_kelvin}
>>> t['FtoK'](32)
273.14999999999998
>>> t['CtoK'](0)
273.14999999999998

<br>
<br>




# summary
- Python functions provide exceedingly powerful argument-passing features:
    - Arguments may be passed by position or by parameter name.
    - Default values may be provided for function parameters.
    - Functions can collect arguments into tuples, giving you the ability to define
        functions that take an indefinite number of arguments.
    - Functions can collect arguments into dictionaries, giving you the ability to
    define functions that take an indefinite number of arguments passed by parameter
    name.

- Functions are first-class objects in Python, which means that they can be assigned to
variables, accessed by way of variables, and decorated.







