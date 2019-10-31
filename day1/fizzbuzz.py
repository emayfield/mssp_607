# Task: Write code that accomplishes the following:
#  Loop from 0 to 100
#  If the value is divisible by 3:
#  print "Fizz"
#  If the value is divisible by 5:
#  print "Buzz"
#  If the value is divisible by 15:
#  print "FizzBuzz"
#  If none of the above:
#  Just print the number
for x in range(100):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
