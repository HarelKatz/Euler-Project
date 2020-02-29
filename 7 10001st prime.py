from math import sqrt
from itertools import count, islice


def isPrime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


pos = int(input("pos: "))
prime = 2
j = 0
i = 2
while j < pos:
    if isPrime(i):
        j += 1
        prime = i
    i += 1
print(prime)
