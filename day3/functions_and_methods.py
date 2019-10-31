
animals = ["lions", "tigers"]

# Object methods are always associated with an object, in this case the animals list.
# Because of this, the list does not need to be given as a parameter to append().
# The append method takes one input: a string. It does not return anything.
animals.append("bears")

# The length function, on the other hand, is a function that is not associated with a particular object.
# That means that we need to pass in the list we want to evaluate as a parameter.
len(animals)

# Next, let's look at the difference between printing information and returning it.

# In a function that prints its result, the user sees the result in the terminal.
# However, the value is not accessible once the function finishes; all information is only available
# locally within the scope of the function itself.
def print_length_of_list(list_a):
    print(len(list_a))

# On the other hand, functions that return variables do not show any information to the user, by default.
# No information is printed to the command line, but the variable that is returned can be accessed and used
# by future code.
def return_length_of_list(list_a):
    return len(list_a)

# Nothing prevents you from using both print statements and return values in the same function.
def length_of_list(list_a):
    length = len(list_a)
    print(f"The length is {length}")
    return length

# We can't do anything with any of the variables created in this function call.
print_length_of_list(animals)

# We can, however, use the variable returned by these functions.
returned_length = return_length_of_list(animals)
animal_length = length_of_list(animals)




