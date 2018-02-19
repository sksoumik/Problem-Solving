from itertools import islice, count
from math import sqrt


# Check if a number is prime of not
def isPrime(number):
    return number > 1 and all(number % i for i in islice(count(2), int(sqrt(number) - 1)))


number = int(input('Enter a number'))

if isPrime(number) == True:
    print("Prime")

else:
    print("Not Prime")
