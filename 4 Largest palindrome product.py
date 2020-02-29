import math


arr = []

for i in range(100, 1000):
    for j in range(100, 1000):
        if str(i*j) == str(i*j)[::-1]:
            arr.append(i*j)

print(arr)
print(max(arr))
