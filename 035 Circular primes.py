from collections import deque
from itertools import count, islice
from math import sqrt


def isPrime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


def rotation(N):
    for i in range(len(N)):
        if not isPrime(int(N[i:] + N[:i])):
            break
    else:
        x.append(int(N))


x = []

for num in range(2, 1000000):
    rotation(str(num))

print(x)
print(sum(x))
print(len(x))
