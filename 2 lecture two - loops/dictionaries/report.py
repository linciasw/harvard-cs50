# DICTIONARIES
# FROM CS50 SHORTS


# The important thing is: """ is not automatically a comment. In Python, triple quotes create a multi-line string.
# and is also commonly used for docstrings. 
# a docstring is a special string in Python that is used to describe what a function, class, or module does.
# the name comes from documentation string.
# it usually goes immediately inside a function, class, or file after the definition line.


# an f string offer a concise and efficient way to interpolate variables, objects, and expressions directly into strings. 
# by prefixing a string with f or F, you can embed expressions within curly braces ({}), which are evaluated at runtime.



"""
def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))




def create_report(spacecraft):
    return f"""
#     ============== REPORT =============

#     Name: {spacecraft["name"]}
#     Distance: {spacecraft["distance"]} AU

#     ===================================
#     """

# main()


def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    # another way of creating a value instead of including it right in the dictionary
    # spacecraft["distance"] = 0.01 
    
    # another way of creating a value 
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))



# get prevents key errors if value does not exist with the argument "Unknown"
def create_report(spacecraft):
    return f"""
    ============== REPORT =============

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU     
    Orbit: {spacecraft.get("orbit", "Unknown")}   

    ===================================
    """

main()
