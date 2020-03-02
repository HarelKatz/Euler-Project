from math import factorial
x = []
for num in range(3, 1000000):
    temp = 0
    for i in str(num):
        temp += factorial(int(i))

    if temp == num:
        x.append(num)

print(x)
print(sum(x))
