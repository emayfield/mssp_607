# Let's start with some variables to work with.
age = 12
test_age = 1

# Much like with an if statement, a while statement checks whether a value is true.
# Then, if it is, it does everything under it, in the indented block,
# then returns to the top and checks the condition again.
while test_age < age:
    print("Age is at least:")
    print(test_age)
    test_age = test_age + 1

# The last line above is very important in a while loop. If you don't change the condition
# that's being checked, somewhere in the loop, it will evaluate the same way every time.
# This means that your loop will run forever!

# There are a couple ways to clean up the code above. First, we can replace the unwieldy
# increment line (adding one) with the shortcut +=. Next, we can shrink down the code
# to a single print statement by adding a formatted string. To do this, we do three things:
# First, insert the letter 'f' prior to the string itself.
# Next, add curly braces, {}, wherever you want a variable's value to be pasted.
# Finally, add the name of the variable to paste inside the curly braces.
while test_age <= age:
    print(f"Found the age! {test_age}")
    test_age += 1

print("test with while loop completed")

# Next we can look at for loops. These loops behave very similarly to while loops,
# But they do some of the bookkeeping for us. Instead of having to manually change the 
# condition being tested each time, a for loop will do it for us.

# The easiest way to do this is with range(). This function will tell the for loop to
# iterate through a loop five times, each time changing the value of the variable in the 
# for _____ statement. In the case below, that's test_age.
for test_age in range(20):
    if test_age == age:
        print(f"Found the age! {test_age}")
        print(test_age)

print("test with for loop completed")