from math import sqrt
from itertools import count, islice


def isPrime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


j = 2
i = 0
sum = 0
while j < 2000000:
    if isPrime(j):
        # print(j)
        i += 1
        sum += j
    j += 1
print(sum)
