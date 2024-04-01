# Traditional for loop
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []
for number in numbers:
    doubled_numbers.append(number * 2)

# Using map
doubled_numbers = list(map(lambda x: x * 2, numbers))
