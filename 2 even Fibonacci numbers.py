x = 1
y = 2
temp = 0
sum = 0
while x < 4000000:
    if not x % 2:
        sum += x
    temp = x
    x = y
    y += temp
print(sum)
