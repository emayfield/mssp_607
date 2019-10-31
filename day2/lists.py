# Up to this point, we've mostly only assigned integers and strings
# to our variables.
size = 5
name = 'Alice'

# The one more complex type of variable we've used is the file object,
# which lets us open files for reading and writing.
state_file = open("state_names.txt")

# The next type of object we're going to work with is a list. This is a
# data structure for keeping an in-order list of other objects.
animals = ["lions", "tigers", "bears"]

# We can call length on a list to find out how many objects it currently holds.
print(f"The length of the list is {len(animals)}")

# We can look up items in the list, either from first to last (starting from 0)
# or from last to first (starting from -1).
first_animal = animals[0]
last_animal = animals[-1]

print(f"The first animal is {first_animal} and the last animal is {last_animal}")

# We can add objects one at a time to a list using .append()
animals.append("pigs")

print(f"The new length of the animals list is {len(animals)}")

# We can also add new objects in a group using .extend()
new_animals = ["pigs", "pandas"]
animals.extend(new_animals)

print(f"The new length is now {len(animals)}")

# Using a for loop, we can iterate through a list, performing the code in a 
# block once for each object that the list contains.
for row in animals:
    print(f"This animal is {row}")
    print(f"The animal name length is {len(row)}")
    print("---THE LOOP IS OVER---")

# We can also "slice" the list and work with a subset. For instance, the following
# print() function will run once each for the first 3 elements of the list.
for row in animals[0:-2]:
    print(row)
