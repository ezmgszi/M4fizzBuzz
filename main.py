# FizzBuzz
# lip
# program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

# takes an integer value and determines if it is a multiple of 3 using mod
# returns 1 if it is a multiple of 3 or 0 if it is not
def mod3(i):
    if i % 3 == 0:
        return 1
    else:
        return 0


# takes an integer value and determines if it is a multiple of 5 using mod
# returns 1 if it is a multiple of 5 or 0 if it is not
def mod5(i):
    if i % 5 == 0:
        return 1
    else:
        return 0


# main
for i in range(1, 101):
    if mod3(i) and mod5(i):
        print("FizzBuzz")
    elif mod5(i):
        print("Buzz")
    elif mod3(i):
        print("Fizz")
    else:
        print(i)
