# Evaluation and Assignment
# Many places in Python need to evaluate whether a certain expression is true or false.
# The simplest version of this is the == test, which evaluates whether the left and right
# sides are equal
3 == 3 # This is an expression that evaluates to True
3 == 4 # This is an expression that evaluates to False

# There are several other tests you can do this with, like "greater than" or "less than",
# "greater/less than or equal to", and "not equal to":
3 > 5  # False 
4 < 5  # True
3 <= 6 # True
5 >= 5 # True
5 != 6 # True

# We can also link together these evaluations with and, or, and not.

3 > 5 and 5 > 6 # False
4 < 5 or 5 > 6 # True
not 2 < 3 # True

# Next, we can assign values to variables. This is done with a single = sign, instead of
# a double equals sign, ==. The expression on the right-hand side will be evaluated,
# and the result will be saved under the variable name on the left-hand side.
    
name = "Alice"
age = 12

# It is really important to get the difference between assignment (=) and evaluation (==). 
# With assignment, for instance, you can only put a single variable on the left-hand side.


# The following lines will create errors:
# 6 = age 
# (6 - (5 + 1)) = 0

# But if they were == they would be fine!
6 == age # False
(6 - (5 + 1)) == 0 # True

