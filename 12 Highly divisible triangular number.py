
x = []
t = 1
while 1:

    n = int((t/2)*(t+1))
    # print(n)
    x = (i for i in range(1, n+1) if not n % i)
    # print(list(x))
    if len(list(x)) > 500:
        print(list(x))
        print(n)
        break
    t += 1

print(x)
print(n)
print(t)
