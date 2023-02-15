n = int(input("Enter the value of n: "))

# initialize variables
i = 1
sum = 0

# loop through first n natural numbers and calculate sum
while i <= n:
    sum += i
    i += 1

# display the sum
print("The sum of first", n, "natural numbers is:", sum)
