x = []
for i in range(2, 101):
    for j in range(2, 101):
        x.append(pow(i, j))

x = list(dict.fromkeys(x))
# print(x)
print(len(x))
