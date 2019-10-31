
# This function takes an input one parameter: list_a, which can contain
# any number of objects.
#
# The function prints out the natural English representation of the contents of a list.
# For lists with one object, it just prints that object.
# For lists with two objects x and y, it prints "x and y"
# For lists with three or more objects x, y, and z:
#    "x, y, and z"
# And so on.
def english_string(list_a):
    punctuated_string = ""

    if len(list_a) == 0:
        punctuated_string = ""
    
    elif len(list_a) == 2:
        punctuated_string = f"{list_a[0]} and {list_a[1]}"
    
    elif len(list_a) != 1:
        for item in list_a[0:-1]:
            punctuated_string += f"{item}, "
        punctuated_string += f"and {list_a[-1]}"
    
    else:
        punctuated_string = list_a[0]
        
    print(punctuated_string)

animals = ["lions", "tigers"]

english_string(animals)