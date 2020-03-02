
x = []
for num in range(2, 1000000):
    temp = 0
    for i in str(num):
        temp += pow(int(i), 5)

    if temp == num:
        x.append(num)

print(x)
print(sum(x))
