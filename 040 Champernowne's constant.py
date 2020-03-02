
frac = ""
num = 1
for i in range(1, 1000001):
    frac += str(i)

for i in range(7):
    #print(frac[pow(10, i) - 1])
    num *= int(frac[pow(10, i) - 1])

print(num)
