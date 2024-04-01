from functools import reduce

# Traditional for loop for summing
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number

# Using reduce
total = reduce(lambda x, y: x + y, numbers)
