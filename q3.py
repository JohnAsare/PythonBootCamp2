# John Asare
# May 27 2020


""" Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3."""

numbers = [x for x in range(1, 51) if x % 3 == 0]
print(numbers)