# Write a short program that prints each number from 1 to 100 on a new line. 

# For each multiple of 3, print "Fizz" instead of the number. 

# For each multiple of 5, print "Buzz" instead of the number. 

# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.


def fizzbuzzold():

    for i in range(0,101,1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)

def fizzengine():
    for i in range(0,101,1):
        if fizzbuzz(i):
            print("FizzBuzz")
        elif fizz(i):
            print("Fizz")
        elif buzz(i):
            print("Buzz")
        else:
            print(i)


def fizzbuzz(i):
    if i%3 == 0 and i%5 == 0:
        return True

def fizz(i):
    if i%3 == 0:
        return True

def buzz(i):
    if i%5 == 0:
        return True

fizzengine()