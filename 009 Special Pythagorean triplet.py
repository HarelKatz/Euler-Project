def compute():
    for i in range(1000):
        for j in range(i):
            for k in range(j):
                if pow(k, 2) + pow(j, 2) == pow(i, 2) and i + k + j == 1000:
                    print(i, j, k)
                    print(i*j*k)
                    return


compute()
