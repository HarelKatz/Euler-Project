import itertools
import math

x = 0
n = 0
for i in itertools.count(1):
    x = 0
    n += i

    t = 1
    while t <= int(math.sqrt(n)):
        if (n % t == 0):
            x += 2
        t += 1

    if x > 500:
        print(x)
        print(n)
        break
