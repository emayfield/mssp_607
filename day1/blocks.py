# Now that we have expressions and variables, we can start putting code in blocks.
# The simplest type of block is an 'if' statement. 
# First, let's assign values to some variables.
x = "book"
y = 5

# The if statement needs to be formatted with punctuation. The rest of the code 
if x == "book":
    print("We matched our target") # This code will run, because the expression above is True.
else:
    print("We did not match our target") # This code would only run if the expession is False.


# You can make the conditions in your if statement as long as you need them to be.
# Use and, or, not to add additional conditions
if x == "chair" and y == 5:
    print("We matched both targets.") # This code will not run because x did not match.
else:
    print("At least one target did not match.")

# If you want more control over what to do in specific circumstances, you can add
# nested statements:

if x == "chair"
    if y == 4:
        print("Double Match")
    else: 
        print("Single Match")
else:
    print("No Match")

# Now let's look at our second function: len(). This will get us
# the number of characters in a string, returned as an integer

len("chair") # Evaluates to 5
5 == len("chair") # Evaluates to True

# The result of len() can be used inside of an if statement's evaluation.
# Let's create some new variables.

name = "Alice"
age = 12

# Now let's use len() within an if statement. Say that we want to categorize someone's age,
# but only if their name is greater than a certain length. Then we can use the following code:
if len(name) > 5:
    print("Long name")
    if age > 20:
        print("Adult")
    if age > 12 and age < 20:
        print("Teenage")
    else:
        print("Child")
else:
    print("Short name")
    
    
