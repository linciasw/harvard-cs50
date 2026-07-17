# LISTS METHODS

# results = ["Mario", "Luigi"]

# to add an item onto the existing list 
# results.append("Princess")
# results.append("Yoshi")
# results.append("Koopa Troopa")
# results.append("Toad")


# to add a list into a list 
# results.append(["Bowser", "Donkey Kong Jr."])
# output is:
# ['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', ['Bowser', 'Donkey Kong Jr.']]

# to remove items 
# results.remove(["Bowser", "Donkey Kong Jr."])


# to add items into the list properly
# results.extend(["Bowser", "Donkey Kong Jr."])
# output is:
# ['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Bowser', 'Donkey Kong Jr.']

results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr"]

# if we want to remove Bowser from the list
results.remove("Bowser")

# to add Bowser back at a specific index 
results.insert(0, "Bowser")

# to reverse the order of the list
results.reverse()



print(results)