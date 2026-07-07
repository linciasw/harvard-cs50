
# LISTS

# students = ["Hermione", "Harry", "Ron"]

# to go inside a list and print a specific value -
# what you want to do is go inside and index the list like so:
# print(students[0])
# print(students[1])
# print(students[2])
# lists in python are zero-indexed, they start from index 0 and go up


# a better way of doing this, using a loop
# you can use python to iterate over anything, not just strings
# for student in students: 
#     print(student) 
# student on line 16 is just another way of saying i for first index
# python initializes it to the first index for you


# LEN 
# to create a loop that starts at index 0 and ends at 2:
# for i in range(len(students)):
#     print(students[i])

# this will print the index location 
# for i in range(len(students)):
#     print(i, students[i])


# this will print a top 3
# for i in range(len(students)):
#     print(i + 1, students[i])




# DICTIONARIES
# key-value pairs
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# to print out specific indexes
# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])


# when you use a for loop to iterate over a dictionary,
# it will print all keys
# for student in students:
#     print(student)


# to get it to print key-value pairs, use an index identifier and the key 
# for student in students:
#     print(student, students[student], sep=", ")






