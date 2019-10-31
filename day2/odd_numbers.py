# Start of day warmup task:
# 1. Create a new file and save it as 'odd_numbers.py'
# 2. Using a for or while loop, print all the numbers from 0 to 100
# 3. Now write code to add those numbers together to a new variable
# 4. Using an f-string, print:
#            "The sum of the numbers from 0 to 100 is ____"
# 5. Next calculate the mean of those numbers (sum / count)
sum_100 = 0
for i in range(101):
    print(f"The sum so far is {sum_100} at i={i}")
    sum_100 += i
print(f"The sum of the numbers from 0 to 100 is {sum_100}")
mean = sum_100 / 100
print(f"The mean is {mean}")

