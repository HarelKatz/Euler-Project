num = 5*7*11*12*13*14*15*16*17*18*19*20
'''check = True
arr = []
for i in reversed(range(20, num+1, 2)):
    if not(i % 5 or i % 7 or i % 11 or i % 12 or i % 13 or i % 14 or i % 15 or i % 16 or i % 17 or i % 18 or i % 19 or i % 20):
        # print(i)
        arr.append(i)


print(arr)
print(min(arr))
'''
i = 20
arr2 = []
while i <= num:
    if not(i % 5 or i % 7 or i % 11 or i % 12 or i % 13 or i % 14 or i % 15 or i % 16 or i % 17 or i % 18 or i % 19 or i % 20):
        print(i)
        arr2.append(i)
    i += 2
print(arr2)
print(min(arr2))
