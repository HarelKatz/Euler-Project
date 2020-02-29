import math
num = int(input("check prime factors: "))
primes = []


while num % 2 == 0:
    num /= 2
    primes.append(2)

i = 3
while pow(i, 2) <= num:
    #print(i, num % i)
    while num % i == 0:
        # print(i)
        primes.append(i)
        num //= i
    i += 2
if num > 1:
    primes.append(int(num))
primes = list(dict.fromkeys(primes))
print(primes)
print(max(primes))
