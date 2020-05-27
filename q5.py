# John Asare
# may 27 2020


""" Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
instead of the number, and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz"."""


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(f'{number}\tFizzBuzz')
    elif number % 3 == 0:
        print(f'{number}\tFizz')
    elif number % 5 == 0:
        print(f'{number}\tBuzz')
    else:
        print(number)
