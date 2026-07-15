# reached 8:19 in video


student = {"name": "John", "age": 25, "courses": {"Math", "CompSci"}}

# print(student["name"]) # this prints the value of the first key

# values in a dictionary can be any data types:
# int, string, boolean, list, tuple, set or a dictionary

# keys can also be any data type

# the get method returns "None" if you're trying to get a key that does not exist
# print(student.get("phone")) 

# you can put a default value to replace "None"
# print(student.get("phone", "Not Found"))

# to put in a new key with a value
# student["phone"] = "555-5555"

# to replace the value of an exisiting key
# student["name"] = "Jane"

# update method, to add new keys, values into the dictionary
# student.update({"name": "Jane", "age": 26, "phone": "555-5555"})

# to delete a key, value 
# del student["age"]

# another way of deleting a key, value is using the pop() method
# the pop method also returns the removed value, we can add it to a variable
# age = student.pop("age")
# print(age)


# to check length of dictionary
# print(len(student))

# to print out all keys
# print(student.keys())


# to print out all values 
# print(student.values())

# to print out both keys and values, items() method
print(student.items())


# print(student.get("phone", "Not Found"))
# print(student)
