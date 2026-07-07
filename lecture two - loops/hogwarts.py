
# LISTS

students = ["Hermione", "Harry", "Ron"]

# to go inside a list and print a specific value -
# what you want to do is go inside and index the list like so:
# print(students[0])
# print(students[1])
# print(students[2])
# lists in python are zero-indexed, they start from index 0 and go up


# a better way of doing this, using a loop
# you can use python to iterate over anything, not just strings
for student in students: # student in this line is just another way of saying i for first index
    print(student)
