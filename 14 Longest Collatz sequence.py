
longest, length = 0, 0
for i in range(1, 1000000):
    temp = 0
    num = i
    while num != 1:
        if num % 2:
            num = 3*num+1
            temp += 1
        else:
            num /= 2
            temp += 1
    if temp == max(length, temp):
        length = temp
        longest = i
    # print(length)
    # print(longest)

print(length)
print(longest)
