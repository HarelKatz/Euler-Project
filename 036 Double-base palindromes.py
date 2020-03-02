
i = 585
x = []
for i in range(1000000):
    num = str(i)
    binNum = "{0:b}".format(i)
    if num == num[::-1] and binNum == binNum[::-1]:
        x.append(i)


print(x)
print(sum(x))
