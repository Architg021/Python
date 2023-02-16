def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n-1)

result = sum_of_natural_numbers(6)
print(result)
