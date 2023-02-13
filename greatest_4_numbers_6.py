def  find_greatest_of_four_numbers(a, b, c, d):
    greatest = a
    if b > greatest:
        greatest = b
    if c > greatest:
        greatest = c
    if d > greatest:
        greatest = d
    return greatest

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

result = find_greatest_of_four_numbers(a, b, c, d)
print("The greatest of four numbers is", result)
