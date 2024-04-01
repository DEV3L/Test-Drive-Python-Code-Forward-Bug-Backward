# Traditional approach
numbers = range(1, 11)
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

# Using filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
