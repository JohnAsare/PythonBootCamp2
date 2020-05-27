# John Asare
# 5 27 2020


""" Use range() to print all the even numbers from 0 to 10."""

print('Using computation')
for number in range(0, 11):
    if number % 2 == 0:
        print(number)

print('\nusing range steps of 2')
for number in range(0, 11, 2):
    print(number)

print('\nUsing list and range')
print(list(range(0, 11, 2)))

